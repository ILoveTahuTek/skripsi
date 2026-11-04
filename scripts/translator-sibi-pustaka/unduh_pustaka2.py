#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
unduh_pustaka2.py — Gelombang kedua untuk rujukan yang gagal di unduh_pustaka.py.

Strategi berurutan per rujukan gagal:
  1. kandidat terkurasi (CURATED di bawah)
  2. halaman "view" OJS -> temukan tautan galley (viewFile/download) -> unduh
  3. Unpaywall -> OpenAlex -> Semantic Scholar (SEKUENSIAL, jeda anti rate-limit)
  4. fallback: metadata Crossref (JSON) disimpan sebagai catatan sumber resmi

Resumable: berkas valid tidak diunduh ulang; hasil ditulis ke _hasil.json.
Jalur legal saja — tanpa situs bajakan.
"""
import json
import re
import sys
import threading
import time
import warnings
from pathlib import Path

import requests

warnings.filterwarnings("ignore")

sys.path.insert(0, str(Path(__file__).parent))
from data_pustaka import REFS

AKAR = Path("/home/z/my-project/download/pustaka-sibi")
DIR_PDF = AKAR / "pdf"
DIR_WEB = AKAR / "halaman-web"
DIR_META = AKAR / "metadata"
HASIL = AKAR / "_hasil.json"
for d in (DIR_PDF, DIR_WEB, DIR_META):
    d.mkdir(parents=True, exist_ok=True)

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36")
HDR = {"User-Agent": UA,
       "Accept": "text/html,application/xhtml+xml,application/pdf;q=0.9,*/*;q=0.8",
       "Accept-Language": "en-US,en;q=0.9,id;q=0.8"}
EMAIL = "pustaka.sibi.riset@gmail.com"

# ---- kandidat terkurasi hasil penelusuran manual (halaman lab penulis, JDIH, dsb.) ----
CURATED = {
    8:  ["https://www.brin.go.id/news/130095/survei-ungkap-777-penyandang-tuli-menggunakan-bisindo",
         "https://brin.go.id/news/130095/survei-ungkap-777-penyandang-tuli-menggunakan-bisindo"],
    9:  ["https://ejournal.uin-suka.ac.id/pusat/inklusi/article/viewFile/2202/1002",
         "https://ejournal.uin-suka.ac.id/pusat/inklusi/article/download/2202/1002"],
    14: ["https://ijcs.stmikindonesia.ac.id/ijcs/index.php/ijcs/article/viewFile/3539/298"],
    21: ["https://gzhou.pages.wm.edu/wp-content/blogs.dir/5736/files/sites/13/2017/12/SignFi_IMWUT18.pdf"],
    45: ["https://jdih.kemdikbud.go.id/arsip/Berkas%20Arsip%20Non-Kode/EPMendikbud_0161_1994.pdf"],
    48: ["https://jurnal.umj.ac.id/index.php/holistika/article/viewFile/9355/5468",
         "https://jurnal.umj.ac.id/index.php/holistika/article/download/9355/5468"],
    59: ["https://ebulutvcu.github.io/Wowmom20-Lightweight.pdf",
         "https://ebulutvcu.github.io/Lightweight20.pdf"],
    65: ["https://www.cs.temple.edu/~wu/robust17.pdf"],
    73: ["https://jurnal.mdp.ac.id/index.php/rabit/article/download/8340/4101"],
    76: ["https://vipl.ict.ac.cn/research/sign/hylw/202205/W020220524841131372266.pdf"],
    19: ["https://vhil.stanford.edu/sites/g/files/sbiybj29011/files/media/file/bailenson-apa-nonverbal-overload.pdf"],
    20: ["https://gzhou.pages.wm.edu/wp-content/blogs.dir/5736/files/sites/13/2017/12/WiFiSenseSurvey_CSUR19.pdf"],
    40: ["https://tns.thss.tsinghua.edu.cn/widar3.0/data/TPAMI_Widar3.0_paper.pdf"],
    79: ["https://www.communicationcache.com/uploads/1/0/8/8/108844984/a_technique_for_the_measurement_of_attitudes.pdf"],
    6:  ["https://id.wikisource.org/wiki/Undang-Undang_Republik_Indonesia_Nomor_8_Tahun_2016"],
}

# URL halaman "view" OJS untuk resolusi galley otomatis
OJS_VIEW = {
    9:  ["https://ejournal.uin-suka.ac.id/pusat/inklusi/article/view/2202",
         "http://ejournal.uin-suka.ac.id/pusat/inklusi/article/view/2202"],
    14: ["https://ijcs.stmikindonesia.ac.id/ijcs/index.php/ijcs/article/view/3539",
         "http://ijcs.stmikindonesia.ac.id/ijcs/index.php/ijcs/article/view/3539"],
    48: ["https://jurnal.umj.ac.id/index.php/holistika/article/view/9355"],
    73: ["https://jurnal.mdp.ac.id/index.php/rabit/article/view/8340"],
}

hasil = json.loads(HASIL.read_text(encoding="utf-8")) if HASIL.exists() else {}

KUNCI_API = threading.Lock()


def get_url(url, timeout=(15, 90)):
    for verify in (True, False):
        try:
            r = requests.get(url, headers=HDR, timeout=timeout,
                             allow_redirects=True, verify=verify)
            if r.status_code == 200:
                return r.content, r.headers.get("Content-Type", ""), r.url
            return None
        except requests.exceptions.SSLError:
            continue
        except Exception:
            return None
    return None


def pdf_ok(b):
    return bool(b) and len(b) > 15000 and b.lstrip()[:5].startswith(b"%PDF")


def pdf_kepala(path):
    try:
        return path.stat().st_size > 15000 and path.read_bytes()[:2048].lstrip()[:5].startswith(b"%PDF")
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


def simpan_pdf(no, key, data, sumber):
    tujuan = DIR_PDF / f"{no:02d} - {key}.pdf"
    tujuan.write_bytes(data)
    return {"status": "pdf", "berkas": str(tujuan), "sumber": sumber}


def api_with_cooldown(fn, doi):
    with KUNCI_API:
        time.sleep(2.0)
        return fn(doi)


def unpaywall_pdfs(doi):
    try:
        r = requests.get(f"https://api.unpaywall.org/v2/{doi}", params={"email": EMAIL},
                         headers=HDR, timeout=30)
        if r.status_code != 200:
            return []
        j = r.json()
        locs = []
        if j.get("best_oa_location"):
            locs.append(j["best_oa_location"])
        locs += [l for l in (j.get("oa_locations") or []) if l != j.get("best_oa_location")]
        return [l.get("url_for_pdf") for l in locs if l.get("url_for_pdf")]
    except Exception:
        return []


def openalex_pdfs(doi):
    try:
        r = requests.get(f"https://api.openalex.org/works/doi:{doi}", params={"mailto": EMAIL},
                         headers=HDR, timeout=30)
        if r.status_code != 200:
            return []
        j = r.json()
        locs = []
        if j.get("best_oa_location"):
            locs.append(j["best_oa_location"])
        locs += j.get("locations") or []
        return [l.get("pdf_url") for l in locs if l.get("pdf_url")]
    except Exception:
        return []


def s2_pdf(doi):
    try:
        r = requests.get(f"https://api.semanticscholar.org/graph/v1/paper/DOI:{doi}",
                         params={"fields": "openAccessPdf,title"}, headers=HDR, timeout=30)
        if r.status_code == 200:
            return (r.json().get("openAccessPdf") or {}).get("url")
        if r.status_code == 429:
            time.sleep(8)
            return s2_pdf(doi)
    except Exception:
        pass
    return None


def galley_dari_view(urls):
    """Scrape halaman view OJS: kumpulkan tautan galley PDF."""
    kand = []
    for u in urls:
        b = get_url(u)
        if not b or not html_ok(b[0]):
            continue
        t = b[0].decode("utf-8", "ignore")
        for m in re.findall(r'href=["\']([^"\']+)["\']', t, re.I):
            m = m.replace("&amp;", "&")
            if re.search(r'(article/(?:viewFile|download)/|/galley/\d+/download/)', m, re.I):
                if m.startswith("//"):
                    m = "https:" + m
                elif m.startswith("/"):
                    from urllib.parse import urljoin
                    m = urljoin(u, m)
                elif not m.startswith("http"):
                    continue
                if m not in kand:
                    kand.append(m)
        if kand:
            break
    return kand[:8]


def crossref_meta(doi):
    try:
        r = requests.get(f"https://api.crossref.org/works/{doi}", headers=HDR, timeout=30)
        if r.status_code == 200:
            return r.json().get("message")
    except Exception:
        pass
    return None


def catatan_metadata(no, key, doi, alasan):
    if not doi:
        return None
    j = crossref_meta(doi)
    if not j:
        return None
    p = DIR_META / f"{no:02d} - {key}-crossref.json"
    p.write_text(json.dumps(j, ensure_ascii=False, indent=1), encoding="utf-8")
    return {"status": "metadata",
            "berkas": str(p),
            "sumber": f"https://doi.org/{doi}",
            "catatan": alasan}


def proses(no):
    ref = next(r for r in REFS if r["no"] == no)
    key, kind, doi = ref["key"], ref["kind"], ref.get("doi")

    # 0a) PDF sudah ada lokal (mis. diunduh manual)? anggap selesai
    pdf_lokal = DIR_PDF / f"{no:02d} - {key}.pdf"
    if pdf_lokal.exists() and pdf_kepala(pdf_lokal):
        hasil[str(no)] = {"status": "pdf", "berkas": str(pdf_lokal),
                          "sumber": "cache lokal", "key": key, "cite": ref["cite"],
                          "kind": kind, "doi": doi}
        return f"{no:02d} PDF (cache lokal)"

    # 0b) sudah sukses sebelumnya? lewati
    prev = hasil.get(str(no), {})
    if prev.get("status") in ("pdf", "repo") and prev.get("berkas") and \
       Path(prev["berkas"]).exists():
        return f"{no:02d} skip (sudah {prev['status']})"

    # 1) kandidat terkurasi
    for u in CURATED.get(no, []):
        b = get_url(u, timeout=(15, 180))
        if b and pdf_ok(b[0]):
            hasil[str(no)] = simpan_pdf(no, key, b[0], u)
            return f"{no:02d} PDF (kurasi)"
        if b and html_ok(b[0]) and not captcha(b[0]) and kind in ("web", "book"):
            p = DIR_WEB / f"{no:02d} - {key}.html"
            p.write_bytes(b[0])
            hasil[str(no)] = {"status": "halaman", "berkas": str(p), "sumber": u,
                              "key": key, "cite": ref["cite"], "kind": kind, "doi": doi}
            return f"{no:02d} halaman (kurasi)"

    # 2) resolusi galley OJS
    if kind == "ojs" or no in OJS_VIEW:
        for u in galley_dari_view(OJS_VIEW.get(no, [])):
            b = get_url(u, timeout=(15, 120))
            if b and pdf_ok(b[0]):
                hasil[str(no)] = simpan_pdf(no, key, b[0], u)
                return f"{no:02d} PDF (galley OJS)"

    # 3) API OA berurutan
    if doi:
        for nama, fn in (("unpaywall", unpaywall_pdfs), ("openalex", openalex_pdfs),
                         ("s2", lambda d: [s2_pdf(d)] if s2_pdf(d) else [])):
            urls = [u for u in api_with_cooldown(fn, doi) if u]
            for u in urls:
                b = get_url(u, timeout=(15, 120))
                if b and pdf_ok(b[0]):
                    hasil[str(no)] = simpan_pdf(no, key, b[0], f"{nama}: {u}")
                    return f"{no:02d} PDF ({nama})"

    # 4) fallback metadata Crossref
    m = catatan_metadata(no, key, doi, "PDF terbuka tidak tersedia (penerbit berbayar); metadata Crossref disimpan")
    if m:
        hasil[str(no)] = m
        return f"{no:02d} metadata Crossref"
    hasil[str(no)] = {"status": "gagal", "key": key, "cite": ref["cite"], "kind": kind,
                      "doi": doi, "catatan": "tidak ada salinan terbuka/metadata"}
    return f"{no:02d} gagal total"


def main():
    daftar = sorted(int(k) for k, v in hasil.items()
                    if v.get("status") in ("gagal", "parsial"))
    print(f"=== Gelombang 2 untuk {len(daftar)} rujukan: {daftar}", flush=True)
    for no in daftar:
        try:
            print(proses(no), flush=True)
        except Exception as e:
            print(f"{no:02d} eksepsi {type(e).__name__}: {e}", flush=True)
        finally:
            HASIL.write_text(json.dumps(hasil, ensure_ascii=False, indent=1, sort_keys=True),
                             encoding="utf-8")
    HASIL.write_text(json.dumps(hasil, ensure_ascii=False, indent=1, sort_keys=True),
                     encoding="utf-8")
    n = {}
    for v in hasil.values():
        n[v["status"]] = n.get(v["status"], 0) + 1
    print("\n=== RINGKASAN AKHIR ===")
    for k in sorted(n):
        print(f"{k:10}: {n[k]}")


if __name__ == "__main__":
    main()
