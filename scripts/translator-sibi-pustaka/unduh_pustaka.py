#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
unduh_pustaka.py — Unduh 80 rujukan DAFTAR PUSTAKA proposal SIBI-CSI-ESP32S3.

Jalur legal saja: OA resmi penerbit, arXiv, repo resmi (codeload), kartu model
Hugging Face, salinan penulis/institusi yang terindeks Unpaywall / OpenAlex /
Semantic Scholar, Europe PMC untuk literatur biomedis, arsip web (Wayback).

Resumable: berkas valid tidak diunduh ulang.
Kandidat tambahan disuntikkan lewat tambahan.json: {"6": ["https://..."], ...}
"""
import concurrent.futures as cf
import html as mod_html
import json
import re
import threading
import time
import warnings
from pathlib import Path
from urllib.parse import urljoin

import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
warnings.filterwarnings("ignore")

from data_pustaka import REFS, PRESET

AKAR = Path("/home/z/my-project/download/pustaka-sibi")
DIR_PDF = AKAR / "pdf"
DIR_REPOS = AKAR / "repos"
DIR_WEB = AKAR / "halaman-web"
HASIL = AKAR / "_hasil.json"
TAMBAHAN_PATH = Path(__file__).parent / "tambahan.json"
for d in (DIR_PDF, DIR_REPOS, DIR_WEB):
    d.mkdir(parents=True, exist_ok=True)

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36")
HDR = {"User-Agent": UA,
       "Accept": "text/html,application/xhtml+xml,application/pdf;q=0.9,*/*;q=0.8",
       "Accept-Language": "en-US,en;q=0.9,id;q=0.8"}
EMAIL = "pustaka.sibi.riset@gmail.com"

TAMBAHAN = {}
if TAMBAHAN_PATH.exists():
    TAMBAHAN = json.loads(TAMBAHAN_PATH.read_text(encoding="utf-8"))

# ---------------- util jaringan ----------------

def get_url(url, timeout=(15, 90), verify=True):
    """Kembalikan (bytes, content_type, final_url) bila 200, selain itu None."""
    for v in ([verify, False] if verify else [False]):
        try:
            r = requests.get(url, headers=HDR, timeout=timeout,
                             allow_redirects=True, verify=v)
            if r.status_code == 200:
                return r.content, r.headers.get("Content-Type", ""), r.url
            return None  # status bukan 200: jangan coba verify=False
        except requests.exceptions.SSLError:
            continue
        except Exception:
            return None
    return None


def pdf_ok(b):
    return bool(b) and len(b) > 15000 and b.lstrip()[:5].startswith(b"%PDF")


def pdf_kepala(path):
    try:
        with open(path, "rb") as f:
            k = f.read(2048)
        return path.stat().st_size > 15000 and k.lstrip()[:5].startswith(b"%PDF")
    except Exception:
        return False


def html_ok(b):
    if not b or len(b) < 2000:
        return False
    k = b[:3000].lower()
    return b"<html" in k or b"<!doctype html" in k


def captcha(b):
    if not b:
        return True
    k = b[:6000].lower()
    return any(s in k for s in (b"just a moment", b"captcha", b"challenge-platform",
                                b"are you a robot", b"attention required",
                                b"verify you are human"))

# ---------------- sumber kandidat OA ----------------

def unpaywall_pdfs(doi):
    urls = []
    try:
        r = requests.get(f"https://api.unpaywall.org/v2/{doi}",
                         params={"email": EMAIL}, headers=HDR, timeout=30)
        if r.status_code == 200:
            j = r.json()
            locs = []
            if j.get("best_oa_location"):
                locs.append(j["best_oa_location"])
            locs += [l for l in (j.get("oa_locations") or []) if l != j.get("best_oa_location")]
            for l in locs:
                u = l.get("url_for_pdf")
                if u and u not in urls:
                    urls.append(u)
    except Exception:
        pass
    return urls


def openalex_pdfs(doi):
    urls = []
    try:
        r = requests.get(f"https://api.openalex.org/works/doi:{doi}",
                         params={"mailto": EMAIL}, headers=HDR, timeout=30)
        if r.status_code == 200:
            j = r.json()
            locs = []
            if j.get("best_oa_location"):
                locs.append(j["best_oa_location"])
            locs += j.get("locations") or []
            for l in locs:
                u = l.get("pdf_url")
                if u and u not in urls:
                    urls.append(u)
    except Exception:
        pass
    return urls


KUNCI_S2 = threading.Lock()
S2_TERAKHIR = [0.0]


def s2_pdf(doi):
    with KUNCI_S2:
        jeda = 1.1 - (time.time() - S2_TERAKHIR[0])
        if jeda > 0:
            time.sleep(jeda)
        S2_TERAKHIR[0] = time.time()
        for _ in range(2):
            try:
                r = requests.get(f"https://api.semanticscholar.org/graph/v1/paper/DOI:{doi}",
                                 params={"fields": "openAccessPdf,title"},
                                 headers=HDR, timeout=30)
                if r.status_code == 200:
                    return (r.json().get("openAccessPdf") or {}).get("url")
                if r.status_code == 429:
                    time.sleep(6)
                    continue
                break
            except Exception:
                break
    return None


def epmc_render(doi):
    try:
        r = requests.get("https://www.ebi.ac.uk/europepmc/webservices/rest/search",
                         params={"query": f'DOI:"{doi}"', "format": "json", "pageSize": 1},
                         headers=HDR, timeout=30)
        if r.status_code == 200:
            res = (r.json().get("resultList") or {}).get("result") or []
            if res and res[0].get("pmcid"):
                if res[0].get("isOpenAccess") == "N":
                    return None
                return f"https://europepmc.org/articles/{res[0]['pmcid']}?pdf=render"
    except Exception:
        pass
    return None


def scrape_landing(doi):
    """Ambil halaman penerbit via DOI; kembalikan (kandidat_pdf, bytes_html)."""
    try:
        r = requests.get(f"https://doi.org/{doi}", headers=HDR,
                         timeout=(15, 90), allow_redirects=True)
    except Exception:
        return [], None
    if r.status_code != 200:
        return [], None
    t = r.text or ""
    if len(t) < 500:
        return [], None
    kand = []
    m = (re.search(r'citation_pdf_url[^>]*content=["\']([^"\']+)["\']', t, re.I)
         or re.search(r'content=["\']([^"\']+)["\'][^>]*citation_pdf_url', t, re.I))
    if m:
        kand.append(mod_html.unescape(m.group(1)))
    for u in re.findall(r'href=["\']([^"\']+)["\']', t, re.I):
        u2 = mod_html.unescape(u)
        if re.search(r'(article/viewFile|article/download|/galley/\d+/download/|\.pdf(?:\?|$)|/download/)', u2, re.I):
            if u2.startswith("//"):
                u2 = "https:" + u2
            elif u2.startswith("/"):
                u2 = urljoin(r.url, u2)
            elif not u2.startswith("http"):
                u2 = urljoin(r.url, u2)
            if u2 not in kand:
                kand.append(u2)
    return kand[:10], (t.encode("utf-8", "ignore") if not captcha(t.encode("utf-8", "ignore")) else None)


def ie_alt(u):
    """Stamp IEEE → kandidat PDF langsung."""
    if "ieeexplore.ieee.org/stamp/stamp.jsp" in u and "arnumber=" in u:
        n = re.search(r"arnumber=(\d+)", u).group(1)
        return [u, f"https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber={n}"]
    return [u]

# ---------------- prosesor per rujukan ----------------

def proses_paper(r):
    no, key, doi = r["no"], r["key"], r["doi"]
    tujuan = DIR_PDF / f"{no:02d} - {key}.pdf"
    if tujuan.exists() and pdf_kepala(tujuan):
        return {"status": "pdf", "berkas": str(tujuan), "sumber": "cache"}

    t0 = time.time()
    kand = list(TAMBAHAN.get(str(no), [])) + list(PRESET.get(no, []))
    kand = [u for u in kand if not u.startswith("file:")]
    if doi.startswith("10.1145/"):
        kand.append(f"https://dl.acm.org/doi/pdf/{doi}")

    landing_html = None
    if r["kind"] == "ojs":
        lk, landing_html = scrape_landing(doi)
        kand += lk
    kand += unpaywall_pdfs(doi)
    kand += openalex_pdfs(doi)

    kand2 = []
    for u in kand:
        for v in ie_alt(u):
            if v not in kand2:
                kand2.append(v)
    kand = kand2[:14]

    for u in kand:
        if time.time() - t0 > 300:
            break
        b = get_url(u)
        if b and pdf_ok(b[0]):
            tujuan.write_bytes(b[0])
            return {"status": "pdf", "berkas": str(tujuan), "sumber": u}

    # Semantic Scholar
    u = s2_pdf(doi)
    if u:
        for v in ie_alt(u):
            b = get_url(v)
            if b and pdf_ok(b[0]):
                tujuan.write_bytes(b[0])
                return {"status": "pdf", "berkas": str(tujuan), "sumber": v}

    # Scrape halaman penerbit (kind paper belum discrape)
    if r["kind"] != "ojs":
        lk, landing_html = scrape_landing(doi)
        for u in lk:
            if time.time() - t0 > 360:
                break
            b = get_url(u)
            if b and pdf_ok(b[0]):
                tujuan.write_bytes(b[0])
                return {"status": "pdf", "berkas": str(tujuan), "sumber": u}

    # Europe PMC
    u = epmc_render(doi)
    if u:
        b = get_url(u)
        if b and pdf_ok(b[0]):
            tujuan.write_bytes(b[0])
            return {"status": "pdf", "berkas": str(tujuan), "sumber": u}

    # Fallback: simpan halaman penerbit
    if landing_html and html_ok(landing_html):
        p = DIR_WEB / f"{no:02d} - {key} (halaman penerbit).html"
        p.write_bytes(landing_html)
        return {"status": "halaman", "berkas": str(p),
                "catatan": "PDF tidak tersedia terbuka; halaman penerbit disimpan"}
    b = get_url(f"https://doi.org/{doi}")
    if b and html_ok(b[0]) and not captcha(b[0]):
        p = DIR_WEB / f"{no:02d} - {key} (halaman penerbit).html"
        p.write_bytes(b[0])
        return {"status": "halaman", "berkas": str(p),
                "catatan": "PDF tidak tersedia terbuka; halaman penerbit disimpan"}
    return {"status": "gagal", "catatan": "tidak ada salinan terbuka ditemukan (penerbit berbayar)"}


def proses_arxiv(r):
    no, key = r["no"], r["key"]
    tujuan = DIR_PDF / f"{no:02d} - {key}.pdf"
    if tujuan.exists() and pdf_kepala(tujuan):
        return {"status": "pdf", "berkas": str(tujuan), "sumber": "cache"}
    for u in (f"https://arxiv.org/pdf/{r['arxiv']}",):
        b = get_url(u)
        if b and pdf_ok(b[0]):
            tujuan.write_bytes(b[0])
            return {"status": "pdf", "berkas": str(tujuan), "sumber": u}
    # fallback: salinan lokal lama bila ada
    for u in PRESET.get(no, []):
        if u.startswith("file:///"):
            p = Path(u[8:])
            if p.exists() and pdf_kepala(p):
                tujuan.write_bytes(p.read_bytes())
                return {"status": "pdf", "berkas": str(tujuan), "sumber": f"salinan lokal: {p}"}
    return {"status": "gagal", "catatan": "arXiv tidak dapat diunduh"}


def gh_json(url):
    try:
        r = requests.get(url, headers=HDR, timeout=30)
        if r.status_code == 200:
            return r.json()
    except Exception:
        pass
    return None


def proses_repo(r):
    no, key = r["no"], r["key"]
    owner, repo, sha = r["gh"]
    tujuan = DIR_REPOS / f"{no:02d} - {key}.zip"
    if tujuan.exists() and tujuan.stat().st_size > 20000:
        with open(tujuan, "rb") as f:
            if f.read(2) == b"PK":
                return {"status": "repo", "berkas": str(tujuan), "sumber": "cache"}
    if sha:
        urls = [f"https://codeload.github.com/{owner}/{repo}/zip/{sha}"]
        note = f"commit {sha}"
    else:
        j = gh_json(f"https://api.github.com/repos/{owner}/{repo}")
        branch = (j or {}).get("default_branch") or "main"
        sz_kb = (j or {}).get("size") or 0
        note = f"cabang {branch}" + (f", ukuran repo ~{sz_kb // 1024} MB" if sz_kb else "")
        if sz_kb > 400_000:
            readme = get_url(f"https://raw.githubusercontent.com/{owner}/{repo}/{branch}/README.md")
            if readme and len(readme[0]) > 300 and not readme[0].lstrip()[:1] == b"<":
                p = DIR_WEB / f"{no:02d} - {key}-README.md"
                p.write_bytes(readme[0])
                return {"status": "halaman", "berkas": str(p),
                        "catatan": f"repo terlalu besar ({sz_kb // 1024} MB) — hanya README"}
            return {"status": "gagal", "catatan": f"repo terlalu besar ({sz_kb // 1024} MB)"}
        urls = []
        for br in ([branch] if branch else []) + ["master", "main"]:
            u = f"https://codeload.github.com/{owner}/{repo}/zip/refs/heads/{br}"
            if u not in urls:
                urls.append(u)
    for u in urls:
        b = get_url(u, timeout=(15, 300))
        if b and len(b[0]) > 20000 and b[0][:2] == b"PK":
            tujuan.write_bytes(b[0])
            return {"status": "repo", "berkas": str(tujuan), "sumber": u, "catatan": note}
    return {"status": "gagal", "catatan": f"repo {owner}/{repo} gagal diunduh"}


def proses_hf(r):
    no, key = r["no"], r["key"]
    tujuan_md = DIR_WEB / f"{no:02d} - {key}.md"
    if tujuan_md.exists() and tujuan_md.stat().st_size > 300:
        return {"status": "halaman", "berkas": str(tujuan_md), "sumber": "cache"}
    b = get_url(f"https://huggingface.co/{r['hf']}/raw/main/README.md")
    if b and len(b[0]) > 300 and not b[0].lstrip()[:1] == b"<":
        tujuan_md.write_bytes(b[0])
        return {"status": "halaman", "berkas": str(tujuan_md),
                "sumber": f"https://huggingface.co/{r['hf']}",
                "catatan": "kartu model (README) — dokumen sumbernya"}
    b2 = get_url(f"https://huggingface.co/{r['hf']}")
    if b2 and html_ok(b2[0]) and not captcha(b2[0]):
        p = DIR_WEB / f"{no:02d} - {key} (halaman).html"
        p.write_bytes(b2[0])
        return {"status": "halaman", "berkas": str(p), "sumber": b2[2]}
    return {"status": "gagal", "catatan": "Hugging Face tidak dapat diakses"}


def proses_web(r):
    no, key = r["no"], r["key"]
    urls = list(TAMBAHAN.get(str(no), [])) + list(r["urls"])
    if not urls:
        return {"status": "gagal", "catatan": "belum ada URL sumber (menunggu tambahan.json)"}
    berkas = []
    gagal = []
    for i, u in enumerate(urls):
        sfx = chr(ord("a") + i) if len(urls) > 1 else ""
        t_html = DIR_WEB / f"{no:02d}{sfx} - {key}.html"
        t_pdf = DIR_WEB / f"{no:02d}{sfx} - {key}.pdf"
        if t_pdf.exists() and pdf_kepala(t_pdf):
            berkas.append(t_pdf)
            continue
        if t_html.exists() and t_html.stat().st_size > 2000:
            berkas.append(t_html)
            continue
        b = get_url(u)
        if b and pdf_ok(b[0]):
            t_pdf.write_bytes(b[0])
            berkas.append(t_pdf)
            continue
        if b and html_ok(b[0]) and not captcha(b[0]):
            t_html.write_bytes(b[0])
            berkas.append(t_html)
            continue
        ok = False
        for wb in (f"https://web.archive.org/web/2026id_/{u}",
                   f"https://web.archive.org/web/2026/{u}"):
            b2 = get_url(wb, timeout=(15, 120))
            if b2 and pdf_ok(b2[0]):
                (DIR_WEB / f"{no:02d}{sfx} - {key}-arsip.pdf").write_bytes(b2[0])
                berkas.append(DIR_WEB / f"{no:02d}{sfx} - {key}-arsip.pdf")
                ok = True
                break
            if b2 and html_ok(b2[0]) and not captcha(b2[0]):
                p = DIR_WEB / f"{no:02d}{sfx} - {key}-arsip.html"
                p.write_bytes(b2[0])
                berkas.append(p)
                ok = True
                break
        if not ok:
            gagal.append(u)
    if len(berkas) == len(urls):
        return {"status": "halaman" if berkas else "gagal", "berkas": "; ".join(str(b) for b in berkas),
                "sumber": "; ".join(urls)}
    return {"status": "parsial", "berkas": "; ".join(str(b) for b in berkas),
            "catatan": "gagal: " + "; ".join(gagal)}


def proses_pdf(r):
    no, key = r["no"], r["key"]
    tujuan = DIR_PDF / f"{no:02d} - {key}.pdf"
    if tujuan.exists() and pdf_kepala(tujuan):
        return {"status": "pdf", "berkas": str(tujuan), "sumber": "cache"}
    for u in list(TAMBAHAN.get(str(no), [])) + list(r["urls"]):
        b = get_url(u, timeout=(15, 300))
        if b and pdf_ok(b[0]):
            tujuan.write_bytes(b[0])
            return {"status": "pdf", "berkas": str(tujuan), "sumber": u}
    return {"status": "gagal", "catatan": "PDF resmi tidak dapat diunduh"}


def proses_book(r):
    no, key = r["no"], r["key"]
    kand = list(TAMBAHAN.get(str(no), [])) + list(PRESET.get(no, []))
    for u in kand:
        b = get_url(u, timeout=(15, 300))
        if b and pdf_ok(b[0]):
            tujuan = DIR_PDF / f"{no:02d} - {key}.pdf"
            tujuan.write_bytes(b[0])
            return {"status": "pdf", "berkas": str(tujuan), "sumber": u}
        if b and html_ok(b[0]) and not captcha(b[0]):
            p = DIR_WEB / f"{no:02d} - {key}.html"
            p.write_bytes(b[0])
            return {"status": "halaman", "berkas": str(p), "sumber": u}
    if kand:
        return {"status": "gagal", "catatan": "kandidat ditemukan tapi gagal diunduh"}
    return {"status": "gagal", "catatan": "buku/cetak — tidak tersedia secara daring, butuh kandidat URL (tambahan.json)"}


def proses(r):
    k = r["kind"]
    if k in ("paper", "ojs"):
        return proses_paper(r)
    if k == "arxiv":
        return proses_arxiv(r)
    if k == "repo":
        return proses_repo(r)
    if k == "hf":
        return proses_hf(r)
    if k == "web":
        return proses_web(r)
    if k == "pdf":
        return proses_pdf(r)
    if k == "book":
        return proses_book(r)
    return {"status": "gagal", "catatan": f"kind tak dikenal: {k}"}


def main():
    print(f"=== Unduh {len(REFS)} rujukan — {time.strftime('%Y-%m-%d %H:%M:%S')} ===")
    hasil = {}
    with cf.ThreadPoolExecutor(max_workers=8) as ex:
        futs = {ex.submit(proses, r): r for r in REFS}
        for f in cf.as_completed(futs):
            r = futs[f]
            try:
                h = f.result()
            except Exception as e:
                h = {"status": "gagal", "catatan": f"eksepsi: {type(e).__name__}: {e}"}
            hasil[str(r["no"])] = {"key": r["key"], "cite": r["cite"],
                                   "kind": r["kind"], "doi": r.get("doi"), **h}
            print(f"{r['no']:02d} [{h.get('status', '?'):7}] {r['cite'][:60]}")
    HASIL.write_text(json.dumps(hasil, ensure_ascii=False, indent=1, sort_keys=True),
                     encoding="utf-8")
    n = {}
    for v in hasil.values():
        n[v["status"]] = n.get(v["status"], 0) + 1
    print("\n=== RINGKASAN ===")
    for k in sorted(n):
        print(f"{k:10}: {n[k]}")
    print(f"total      : {len(hasil)}/80")


if __name__ == "__main__":
    main()
