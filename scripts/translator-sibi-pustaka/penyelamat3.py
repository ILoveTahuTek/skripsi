#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
penyelamat3.py — Putaran 5 (terakhir otomatis):
- Wayback CDX API (lebih andal daripada availability) utk PDF yang diblokir bot
- Crossref alternative-id → arnumber IEEE → stampPDF
- UNC Dataverse utk Bowen 2009
- landing-penerbit via CDX sebagai halaman (bukti akses) utk yang tetap berbayar
"""
import html as mod_html
import json
import re
import sys
import time
from pathlib import Path
from urllib.parse import urljoin

import requests

sys.path.insert(0, str(Path(__file__).parent))
from unduh_pustaka import DIR_PDF, DIR_WEB, HDR, EMAIL, get_url, pdf_ok, html_ok
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


def cdx(u, limit=8, prefix=False):
    """Kembalikan [(timestamp, original_url)] snapshot status 200."""
    try:
        r = requests.get("https://web.archive.org/cdx/search/cdx",
                         params={"url": u + ("*" if prefix else ""), "output": "json",
                                 "limit": limit, "filter": "statuscode:200"},
                         headers=HDR, timeout=30)
        if r.status_code != 200 or not (r.text or "").strip():
            return []
        j = r.json()
        out = []
        for row in j[1:]:
            out.append((row[1], row[2]))
        return out
    except Exception:
        return []


def coba_cdx(hasil, no, urls, cara="cdx", prefix=False, simpan_html=False):
    for u in urls:
        for ts, asli in cdx(u, prefix=prefix)[:4]:
            w = f"https://web.archive.org/web/{ts}id_/{asli}"
            b = get_url(w, timeout=(15, 180))
            if b and pdf_ok(b[0]):
                tujuan = DIR_PDF / f"{no:02d} - {KEY[no]}.pdf"
                tujuan.write_bytes(b[0])
                catat(hasil, no, status="pdf", berkas=str(tujuan), sumber=w, cara=cara)
                return True
            if simpan_html and b and html_ok(b[0]):
                p = DIR_WEB / f"{no:02d} - {KEY[no]} (halaman penerbit).html"
                p.write_bytes(b[0])
                e = hasil.get(str(no), {})
                if e.get("status") != "pdf":
                    catat(hasil, no, status="halaman", berkas=str(p), sumber=w, cara=cara + "-halaman")
                    return True
        time.sleep(0.2)
    return False


def coba_langsung(hasil, no, urls, cara="langsung5"):
    for u in urls:
        b = get_url(u, timeout=(15, 180))
        if b and pdf_ok(b[0]):
            tujuan = DIR_PDF / f"{no:02d} - {KEY[no]}.pdf"
            tujuan.write_bytes(b[0])
            catat(hasil, no, status="pdf", berkas=str(tujuan), sumber=u, cara=cara)
            return True
    return False


def crossref(doi):
    try:
        r = requests.get(f"https://api.crossref.org/works/{doi}", headers=HDR, timeout=25)
        if r.status_code == 200:
            return r.json().get("message", {})
    except Exception:
        pass
    return {}


def jina(url):
    try:
        r = requests.get("https://r.jina.ai/" + url, headers=HDR, timeout=(15, 120))
        if r.status_code == 200 and len(r.text or "") > 200:
            return r.text
    except Exception:
        pass
    return None


def main():
    hasil = muat()
    belum = sorted(int(k) for k, v in hasil.items() if v.get("status") != "pdf")
    print("BELUM PDF:", ",".join(map(str, belum)), "\n")

    # ---------- A. CDX untuk PDF spesifik ----------
    CDX_PDF = {
        3:  [("https://europepmc.org/articles/PMC10785677?pdf=render", False),
             ("https://pmc.ncbi.nlm.nih.gov/articles/PMC10785677/pdf/alr-15-1-applirev-2021-0120.pdf", False),
             ("https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10785677/pdf/", False)],
        19: [("https://tmb.apaopen.org/pub/nonverbal-overload/download/pdf", False)],
        21: [("https://dl.acm.org/doi/pdf/10.1145/3191755", False),
             ("https://dl.acm.org/doi/pdf/10.1145/3191755", True)],
        24: [("https://dl.acm.org/doi/pdf/10.1145/3377553", False)],
        26: [("https://europepmc.org/articles/PMC9830631?pdf=render", False),
             ("https://pmc.ncbi.nlm.nih.gov/articles/PMC9830631/pdf/", True)],
        39: [("https://dl.acm.org/doi/pdf/10.1145/3570325", False)],
        44: [("https://dl.acm.org/doi/pdf/10.1145/3663547.3759693", False)],
        59: [("https://ieeexplore.ieee.org/iel7/9210704/9217631/09217780.pdf", False)],
        65: [("https://dl.acm.org/doi/pdf/10.1145/3097620.3097624", False)],
        68: [("https://link.springer.com/content/pdf/10.1007/BF00994018.pdf", False),
             ("http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.15.9362&rep=rep1&type=pdf", False),
             ("http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.294.7243&rep=rep1&type=pdf", False),
             ("http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.454.6140&rep=rep1&type=pdf", False)],
        71: [("https://dspace.mit.edu/bitstream/handle/1721.1/6177/", True),
             ("http://dspace.mit.edu/bitstream/handle/1721.1/6177/", True),
             ("https://scispace.com/pdf/on-optimum-recognition-error-and-reject-tradeoff-4ugvowtm6a.pdf", False)],
        76: [("https://dl.acm.org/doi/pdf/10.1145/641007.641035", False)],
        77: [("https://cdr.lib.unc.edu/downloads/bc386t01s", False)],
        25: [("http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.709.1921&rep=rep1&type=pdf", False)],
        9:  [("http://ejournal.uin-suka.ac.id/pusat/inklusi/article/download/2202/", True),
             ("https://ejournal.uin-suka.ac.id/pusat/inklusi/article/download/2202/", True)],
        14: [("http://ijcs.stmikindonesia.ac.id/ijcs/index.php/ijcs/article/download/3539/", True),
             ("https://ijcs.stmikindonesia.ac.id/ijcs/index.php/ijcs/article/download/3539/", True)],
        73: [("https://jurnal.univrab.ac.id/index.php/rabit/article/download/8340/", True)],
        12: [("https://jurnal.poltekba.ac.id/index.php/jst/article/download/732/", True)],
        69: [("https://scholarworks.unist.ac.kr/handle/201301/8342/", True),
             ("http://scholarworks.unist.ac.kr/handle/201301/8342/", True)],
    }
    for no, targets in CDX_PDF.items():
        if no not in belum:
            continue
        urls = [u for u, _ in targets]
        pre = [u for u, p in targets if p]
        if not coba_cdx(hasil, no, urls, cara="cdx"):
            if pre and coba_cdx(hasil, no, pre, cara="cdx-prefix"):
                continue
        else:
            continue
        if pre:
            coba_cdx(hasil, no, pre, cara="cdx-prefix")
        if hasil.get(str(no), {}).get("status") != "pdf":
            catat(hasil, no, status="masih-gagal", cara=f"cdx({len(urls)+len(pre)})")

    # ---------- B. Crossref arnumber IEEE → stampPDF ----------
    IEEE = [23, 26, 47, 59, 63, 66, 71, 74, 75]
    for no in IEEE:
        if no not in belum:
            continue
        msg = crossref(DOI.get(no) or "")
        arnumber = next((a for a in (msg.get("alternative-id") or [])
                         if a.isdigit() and len(a) >= 6), None)
        kand = []
        for l in (msg.get("link") or []):
            if (l.get("content-type") or "").find("pdf") >= 0 and l.get("URL"):
                kand.append(l["URL"])
        if arnumber:
            kand.append(f"https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber={arnumber}")
        if kand:
            if coba_langsung(hasil, no, kand, "crossref-ieee"):
                continue
        if arnumber:
            if coba_cdx(hasil, no, [f"https://ieeexplore.ieee.org/document/{arnumber}"],
                        cara="ieee-cdx", simpan_html=True):
                continue
            if coba_cdx(hasil, no, [f"https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber={arnumber}"],
                        cara="ieee-cdx", simpan_html=True):
                continue

    # ---------- C. UNC Dataverse utk Bowen ----------
    if 77 in belum:
        kand = []
        b = get_url("https://doi.org/10.17615/eavc-4296", timeout=(15, 60))
        if b:
            t = b[0].decode("utf-8", "ignore")
            for u in re.findall(r'href="([^"]+)"', t, re.I):
                if "api/access/datafile" in u:
                    kand.append(urljoin(b[2], mod_html.unescape(u)))
        print(f"   dataverse 77: {len(kand)} kandidat")
        if kand:
            coba_langsung(hasil, 77, kand[:4], "unc-dataverse")

    # ---------- D. 9/12/73/69 via jina (lihat tautan galley) ----------
    for no, landing in ((9, "https://journal.uin-suka.ac.id/pusat/inklusi/article/view/2202"),
                        (12, "https://jurnal.poltekba.ac.id/index.php/jst/article/view/732"),
                        (73, "https://jurnal.univrab.ac.id/index.php/rabit/article/view/8340"),
                        (69, "https://scholarworks.unist.ac.kr/handle/201301/8342")):
        if no not in belum:
            continue
        t = jina(landing)
        if not t:
            print(f"   jina {no:02d}: gagal")
            continue
        kand = [u for u in re.findall(r'\((https?://[^\s)]+)\)', t)
                if re.search(r'(/article/(view|download)/\d+(/\d+)?|\.pdf|bitstream|datafile)', u, re.I)]
        kand = [u.replace("/article/view/", "/article/download/") for u in kand]
        print(f"   jina {no:02d}: {len(kand)} kandidat")
        for k in kand[:6]:
            print("      ", k[:104])
        if kand:
            if coba_langsung(hasil, no, kand[:6], "jina-galley"):
                continue
            coba_cdx(hasil, no, kand[:4], cara="jina-galley-cdx")

    # ---------- E. 8 BRIN via CDX ----------
    if hasil.get("8", {}).get("status") not in ("halaman", "pdf"):
        coba_cdx(hasil, 8, ["https://brin.go.id/news/130095"], cara="brin-cdx", simpan_html=True)

    # ---------- F. landing penerbit via CDX utk sisa ----------
    LANDING_CDX = {
        1:  ["https://muse.jhu.edu/article/51652/summary", "https://muse.jhu.edu/article/51652"],
        2:  ["https://muse.jhu.edu/article/176936/summary", "https://muse.jhu.edu/article/176936"],
        4:  [],
        18: [],
        20: [],
        21: ["https://dl.acm.org/doi/10.1145/3191755"],
        23: [],
        24: ["https://dl.acm.org/doi/10.1145/3377553"],
        25: ["https://dl.acm.org/doi/10.1145/2789168.2790109"],
        39: ["https://dl.acm.org/doi/10.1145/3570325"],
        44: ["https://dl.acm.org/doi/10.1145/3663547.3759693"],
        46: [],
        65: ["https://dl.acm.org/doi/10.1145/3097620.3097624"],
        66: [],
        76: ["https://dl.acm.org/doi/10.1145/641007.641035"],
        74: [],
        75: [],
    }
    for no, urls in LANDING_CDX.items():
        if no not in belum:
            continue
        if not urls and DOI.get(no):
            urls = [f"https://doi.org/{DOI[no]}"]
        if not urls:
            continue
        if coba_cdx(hasil, no, urls, cara="landing-cdx", simpan_html=True):
            continue

    HASIL_PATH.write_text(json.dumps(hasil, ensure_ascii=False, indent=1, sort_keys=True),
                          encoding="utf-8")
    n = {}
    for v in hasil.values():
        n[v.get("status", "?")] = n.get(v.get("status", "?"), 0) + 1
    print("\n=== RINGKASAN PUTARAN 5 ===")
    for k in sorted(n):
        print(f"{k:16}: {n[k]}")
    print(f"total            : {len(hasil)}/80")


if __name__ == "__main__":
    main()
