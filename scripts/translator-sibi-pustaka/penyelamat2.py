#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
penyelamat2.py — Putaran 4:
- fatcat/Scholar Archive (api.fatcat.wiki) untuk semua DOI tersisa
- kandidat langsung baru (gzhou.pages.wm.edu, degruyter, dsb.)
- proxy baca r.jina.ai utk halaman yang memblokir bot (OJS, BRIN)
- archive.org direktori utk Likert 1932
- wayback halaman penerbit sebagai fallback terakhir (bukti akses)
"""
import html as mod_html
import json
import re
import sys
from pathlib import Path
from urllib.parse import urljoin, quote

import requests

sys.path.insert(0, str(Path(__file__).parent))
from unduh_pustaka import DIR_PDF, DIR_WEB, HDR, EMAIL, get_url, pdf_ok, html_ok, pdf_kepala
from data_pustaka import REFS

KEY = {r["no"]: r["key"] for r in REFS}
DOI = {r["no"]: r.get("doi") for r in REFS}
HASIL_PATH = DIR_PDF.parent / "_hasil.json"


def muat():
    return json.loads(HASIL_PATH.read_text(encoding="utf-8")) if HASIL_PATH.exists() else {}


def catat(hasil, no, **kw):
    e = hasil.get(str(no), {})
    e.update(kw)
    e["key"] = KEY[no]
    hasil[str(no)] = e
    print(f"{no:02d} [{kw.get('status','?'):7}] {kw.get('cara', kw.get('catatan',''))[:78]}")


def wayback(u):
    try:
        r = requests.get("http://archive.org/wayback/available",
                         params={"url": u}, headers=HDR, timeout=20)
        j = r.json().get("archived_snapshots", {}).get("closest", {})
        if j.get("available") and j.get("timestamp"):
            return f"https://web.archive.org/web/{j['timestamp']}id_/{u}"
    except Exception:
        pass
    return None


def coba(hasil, no, urls, cara="langsung", wb=True, verbose=True):
    for u in urls:
        if not u:
            continue
        b = get_url(u, timeout=(15, 180))
        if b and pdf_ok(b[0]):
            tujuan = DIR_PDF / f"{no:02d} - {KEY[no]}.pdf"
            tujuan.write_bytes(b[0])
            catat(hasil, no, status="pdf", berkas=str(tujuan), sumber=u, cara=cara)
            return True
        if verbose:
            try:
                kode = requests.get(u, headers=HDR, timeout=(10, 30), stream=True).status_code
            except Exception as e:
                kode = type(e).__name__
            print(f"   .. {no:02d} [{cara}] {kode} {u[:96]}")
        if wb:
            w = wayback(u)
            if w:
                b = get_url(w, timeout=(15, 180))
                if b and pdf_ok(b[0]):
                    tujuan = DIR_PDF / f"{no:02d} - {KEY[no]}.pdf"
                    tujuan.write_bytes(b[0])
                    catat(hasil, no, status="pdf", berkas=str(tujuan), sumber=w, cara=cara + "+wayback")
                    return True
    return False


def id_(u):
    return re.sub(r"(/web/\d{4,14})/", r"\1id_/", u)


def fatcat(doi):
    urls = []
    try:
        r = requests.get("https://api.fatcat.wiki/v0/release/lookup",
                         params={"doi": doi, "expand": "files"}, headers=HDR, timeout=25)
        if r.status_code == 200:
            for f in (r.json().get("files") or []):
                for u in (f.get("urls") or []):
                    if u.get("url"):
                        urls.append(id_(u["url"]))
    except Exception:
        pass
    return urls[:8]


def jina(url):
    try:
        r = requests.get("https://r.jina.ai/" + url, headers=HDR, timeout=(15, 120))
        if r.status_code == 200 and len(r.text or "") > 200:
            return r.text
    except Exception:
        pass
    return None


def hrefs(teks, base=None):
    out = []
    for u in re.findall(r'\((https?://[^\s)]+)\)', teks) + re.findall(r'href=["\']([^"\']+)["\']', teks, re.I):
        u2 = mod_html.unescape(u.strip())
        if u2.startswith("//"):
            u2 = "https:" + u2
        elif not u2.startswith("http") and base:
            u2 = urljoin(base, u2)
        if u2 not in out:
            out.append(u2)
    return out


def simpan_halaman(hasil, no, path, sumber, cara):
    catat(hasil, no, status="halaman", berkas=str(path), sumber=sumber, cara=cara)


def main():
    hasil = muat()
    belum = [int(k) for k, v in hasil.items()
             if v.get("status") not in ("pdf", "repo", "halaman") or
             (v.get("status") in ("halaman",) and v.get("berkas", "x").startswith(str(DIR_PDF)))]
    # 12 masih halaman-tanpa-PDF? cek khusus: 12 ingin PDF
    if hasil.get("12", {}).get("status") == "halaman" and not (DIR_PDF / "12 - Zikky-Akbar-2019-KASIBI-Android.pdf").exists():
        belum.append(12)
    belum = sorted(set(belum))
    print("BELUM:", ",".join(map(str, belum)), "\n")

    # ---------- A. kandidat langsung baru ----------
    LANGSUNG2 = {
        3: ["https://pmc.ncbi.nlm.nih.gov/articles/PMC10785677/pdf/alr-15-1-applirev-2021-0120.pdf",
            "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10785677/pdf/alr-15-1-applirev-2021-0120.pdf",
            "https://europepmc.org/articles/PMC10785677?pdf=render",
            "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10785677/pdf/"],
        6: ["https://peraturan.bpk.go.id/Download/26352/UU%20Nomor%208%20Tahun%202016.pdf"],
        19: ["https://tmb.apaopen.org/pub/nonverbal-overload/download/pdf"],
        20: ["https://gzhou.pages.wm.edu/wp-content/blogs.dir/5736/files/sites/13/2017/12/WiFiSenseSurvey_CSUR19.pdf"],
        26: ["https://europepmc.org/articles/PMC9830631?pdf=render",
             "https://pmc.ncbi.nlm.nih.gov/articles/PMC9830631/pdf/",
             "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9830631/pdf/"],
        59: ["https://ieeexplore.ieee.org/iel7/9210704/9217631/09217780.pdf"],
        68: ["https://link.springer.com/content/pdf/10.1007/BF00994018.pdf"],
        77: ["https://cdr.lib.unc.edu/downloads/bc386t01s",
             "http://cdr.lib.unc.edu/downloads/bc386t01s",
             "https://europepmc.org/articles/PMC2859314?pdf=render"],
        79: ["https://archive.org/download/likert-1932/Likert%201932.pdf",
             "https://archive.org/download/likert-1932/Likert_1932.pdf"],
    }
    for no, urls in LANGSUNG2.items():
        if no not in belum:
            continue
        if not coba(hasil, no, urls, "langsung4"):
            catat(hasil, no, status="masih-gagal", cara="langsung4")

    # ---------- B. (fatcat dilewati — API fatcat.wiki sudah di-sunset) ----------

    # ---------- C0. UU 8/2016: scrape landing JDIH USU + wayback BPK ----------
    if 6 in belum:
        kand = []
        b = get_url("https://jdih.usu.ac.id/id/regulasi/undang-undang-republik-indonesia-nomor-8-tahun-2016-tentang-penyandang-disabilitas-", timeout=(15, 60))
        if b:
            t = b[0].decode("utf-8", "ignore")
            for u in re.findall(r'href="([^"]+)"', t, re.I):
                if re.search(r'\.pdf', u, re.I):
                    kand.append(urljoin("https://jdih.usu.ac.id/", mod_html.unescape(u)))
            print(f"   jdih-usu 06: {len(kand)} kandidat")
        if not coba(hasil, 6, kand[:6], "jdih-usu"):
            catat(hasil, 6, status="masih-gagal", cara="jdih-usu")

    # ---------- C. scrape khusus ----------
    # 21 SignFi + situs Gang Zhou / Yongsen Ma
    if 21 in belum or 20 in belum:
        for halaman in ("https://gzhou.pages.wm.edu/", "https://yongsen.github.io/"):
            t = jina(halaman) or (get_url(halaman) or [b"", "", ""])[0].decode("utf-8", "ignore")
            kand = [u for u in hrefs(t, halaman)
                    if u.lower().endswith(".pdf") and ("signfi" in u.lower() or "sign_fi" in u.lower())]
            if kand and 21 in belum:
                coba(hasil, 21, kand[:4], "penulis-gzhou")

    # 59 stevenmhernandez.com
    if 59 in belum:
        t = jina("https://stevenmhernandez.com/research") or ""
        kand = [u for u in hrefs(t, "https://stevenmhernandez.com/")
                if u.lower().endswith(".pdf") and ("wowmom" in u.lower() or "wifi" in u.lower())]
        if kand:
            coba(hasil, 59, kand[:4], "penulis-hernandez")

    # 71 MIT dspace via wayback handle
    if 71 in belum:
        w = wayback("http://hdl.handle.net/1721.1/6177")
        if w:
            b = get_url(w, timeout=(15, 120))
            if b:
                t = b[0].decode("utf-8", "ignore")
                kand = ["https://dspace.mit.edu" + u for u in re.findall(r'href="(/bitstream/[^"]+\.pdf[^"]*)"', t)]
                kand += [u for u in hrefs(t, w) if "/bitstream/" in u and ".pdf" in u.lower()]
                if kand:
                    coba(hasil, 71, kand[:4], "mit-dspace-wayback")

    # 25 & 68 CiteSeerX (via openalex landing) → pola unduh lama → wayback
    for no in (25, 68):
        if no not in belum:
            continue
        try:
            r = requests.get(f"https://api.openalex.org/works/doi:{DOI[no]}",
                             params={"mailto": EMAIL}, headers=HDR, timeout=25)
            for l in ((r.json().get("locations")) or []):
                lp = l.get("landing_page_url") or ""
                m = re.search(r'doi=([0-9.]+[/\.][0-9A-Za-z.]+)', lp)
                if "citeseerx" in lp and m:
                    dl = ("http://citeseerx.ist.psu.edu/viewdoc/download"
                          f"?doi={m.group(1)}&rep=rep1&type=pdf")
                    if coba(hasil, no, [dl], "citeseerx"):
                        break
        except Exception:
            pass

    # 12 poltekba: view-galley → download + debug href
    if 12 in belum:
        b = get_url("https://jurnal.poltekba.ac.id/index.php/jst/article/view/732")
        if b:
            t = b[0].decode("utf-8", "ignore")
            kand = []
            for u in re.findall(r'href=["\']([^"\']+)["\']', t, re.I):
                if re.search(r'(/article/(view|download)/\d+(/\d+)?|\.pdf)', u, re.I):
                    u = urljoin("https://jurnal.poltekba.ac.id/", mod_html.unescape(u))
                    u = u.replace("/article/view/", "/article/download/")
                    if u not in kand:
                        kand.append(u)
            print(f"   poltekba 12: {len(kand)} kandidat")
            for k in kand[:6]:
                print("      ", k[:100])
            coba(hasil, 12, kand[:8], "poltekba-galley")

    # OJS terblokir via jina → galley → (langsung → wayback)
    JINA_OJS = {
        9:  ("https://ejournal.uin-suka.ac.id/pusat/inklusi/article/view/2202",
             ["http://ejournal.uin-suka.ac.id/pusat/inklusi/article/download/2202/1002",
              "https://journal.uin-suka.ac.id/pusat/inklusi/article/download/2202/1002"]),
        14: ("http://ijcs.stmikindonesia.ac.id/ijcs/index.php/ijcs/article/view/3539",
             ["http://ijcs.stmikindonesia.ac.id/ijcs/index.php/ijcs/article/download/3539/298",
              "https://ijcs.stmikindonesia.ac.id/ijcs/index.php/ijcs/article/download/3539/298"]),
        73: ("https://jurnal.univrab.ac.id/index.php/rabit/article/view/8340", []),
        69: ("https://scholarworks.unist.ac.kr/handle/201301/8342", []),
    }
    for no, (landing, ekstra) in JINA_OJS.items():
        if no not in belum:
            continue
        kand = list(ekstra)
        t = jina(landing)
        if t:
            for u in hrefs(t, landing):
                if re.search(r'(/article/(view|download)/\d+(/\d+)?|\.pdf|bitstream)', u, re.I):
                    u = u.replace("/article/view/", "/article/download/")
                    if u not in kand:
                        kand.append(u)
            print(f"   jina {no:02d}: {len(kand)} kandidat")
        if kand:
            coba(hasil, no, kand[:8], "jina-ojs")
        else:
            catat(hasil, no, status="masih-gagal", cara="jina-ojs (kandidat kosong)")

    # ---------- D. arsip.org Likert (direktori) ----------
    if 79 in belum:
        b = get_url("https://archive.org/download/likert-1932/", timeout=(15, 60))
        if b and b"<html" in b[0][:200].lower():
            t = b[0].decode("utf-8", "ignore")
            pdfs = re.findall(r'href="([^"]+\.pdf)"', t, re.I)
            if pdfs:
                coba(hasil, 79, [f"https://archive.org/download/likert-1932/{quote(p)}" for p in pdfs],
                     "archive.org-direktori")
        if hasil.get("79", {}).get("status") != "pdf":
            catat(hasil, 79, status="masih-gagal", cara="archive.org-direktori")

    # ---------- E. BRIN via jina → simpan teks ----------
    if hasil.get("8", {}).get("status") != "halaman":
        t = jina("https://brin.go.id/news/130095")
        if t and len(t) > 500:
            p = DIR_WEB / "08 - BRIN-2026-Ekosistem-Bahasa-Isyarat.md"
            p.write_text(t, encoding="utf-8")
            simpan_halaman(hasil, 8, p, "https://brin.go.id/news/130095", "jina-reader")

    # ---------- F. wayback halaman penerbit utk yang tetap gagal ----------
    LANDING = {
        1: "https://muse.jhu.edu/article/51652/summary",
        2: "https://muse.jhu.edu/article/176936/summary",
    }
    for no in list(LANDING) + [n for n in (21, 23, 24, 39, 44, 46, 65, 66, 74, 75, 76, 19, 26, 59, 3, 68, 71, 9, 14, 73)
                               if n in belum and hasil.get(str(n), {}).get("status") != "halaman"]:
        u = LANDING.get(no) or (f"https://doi.org/{DOI[no]}" if DOI.get(no) else None)
        if not u:
            continue
        w = wayback(u)
        if w:
            b = get_url(w, timeout=(15, 120))
            if b and html_ok(b[0]):
                p = DIR_WEB / f"{no:02d} - {KEY[no]} (halaman penerbit).html"
                p.write_bytes(b[0])
                e = hasil.get(str(no), {})
                if e.get("status") != "pdf":
                    simpan_halaman(hasil, no, p, w, "wayback-landing")
        else:
            e = hasil.get(str(no), {})
            if e.get("status") not in ("pdf", "halaman"):
                catat(hasil, no, status="gagal", catatan="penerbit berbayar; tidak ada salinan terbuka terarsip")

    HASIL_PATH.write_text(json.dumps(hasil, ensure_ascii=False, indent=1, sort_keys=True),
                          encoding="utf-8")
    n = {}
    for v in hasil.values():
        n[v.get("status", "?")] = n.get(v.get("status", "?"), 0) + 1
    print("\n=== RINGKASAN PUTARAN 4 ===")
    for k in sorted(n):
        print(f"{k:16}: {n[k]}")
    print(f"total            : {len(hasil)}/80")


if __name__ == "__main__":
    main()
