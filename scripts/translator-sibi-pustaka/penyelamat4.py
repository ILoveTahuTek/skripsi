#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""penyelamat4.py — fokus cepat: OJS via CDX terarah, UNC Dataverse, sesi De Gruyter, debug href penulis."""
import html as mod_html
import json
import re
import sys
from pathlib import Path
from urllib.parse import urljoin

import requests

sys.path.insert(0, str(Path(__file__).parent))
from unduh_pustaka import DIR_PDF, DIR_WEB, HDR, get_url, pdf_ok, html_ok
from data_pustaka import REFS

KEY = {r["no"]: r["key"] for r in REFS}
HASIL_PATH = DIR_PDF.parent / "_hasil.json"
hasil = json.loads(HASIL_PATH.read_text(encoding="utf-8"))


def catat(no, **kw):
    e = hasil.get(str(no), {})
    e.update(kw)
    e["key"] = KEY[no]
    hasil[str(no)] = e
    print(f"{no:02d} [{kw.get('status','?'):7}] {kw.get('cara', kw.get('catatan',''))[:78]}")


def simpan_pdf(no, data, sumber, cara):
    t = DIR_PDF / f"{no:02d} - {KEY[no]}.pdf"
    t.write_bytes(data)
    catat(no, status="pdf", berkas=str(t), sumber=sumber, cara=cara)
    return True


def cdx(u, limit=6, prefix=True):
    try:
        r = requests.get("https://web.archive.org/cdx/search/cdx",
                         params={"url": u + ("*" if prefix else ""), "output": "json",
                                 "limit": limit, "filter": "statuscode:200"},
                         headers=HDR, timeout=25)
        if r.status_code != 200 or not (r.text or "").strip():
            return []
        return [(row[1], row[2]) for row in r.json()[1:]]
    except Exception:
        return []


def sudah(no):
    return hasil.get(str(no), {}).get("status") == "pdf"


# A. OJS via CDX (snapshot unduhan)
OJS = {
    9:  "https://ejournal.uin-suka.ac.id/pusat/inklusi/article/download/2202",
    12: "https://jurnal.poltekba.ac.id/index.php/jst/article/download/732",
    14: "http://ijcs.stmikindonesia.ac.id/ijcs/index.php/ijcs/article/download/3539",
    73: "https://jurnal.univrab.ac.id/index.php/rabit/article/download/8340",
}
for no, u in OJS.items():
    if sudah(no):
        continue
    snap = cdx(u)
    ok = False
    for ts, asli in snap[:3]:
        w = f"https://web.archive.org/web/{ts}id_/{asli}"
        b = get_url(w, timeout=(15, 120))
        if b and pdf_ok(b[0]):
            simpan_pdf(no, b[0], w, "cdx-ojs")
            ok = True
            break
    if not ok:
        catat(no, status="masih-gagal", cara=f"cdx-ojs {len(snap)} snap")

# 69 UNIST: snapshot handle → bitstream
if not sudah(69):
    snap = cdx("https://scholarworks.unist.ac.kr/handle/201301/8342")
    ok = False
    for ts, asli in snap[:3]:
        w = f"https://web.archive.org/web/{ts}id_/{asli}"
        b = get_url(w, timeout=(15, 120))
        if b and pdf_ok(b[0]):
            simpan_pdf(69, b[0], w, "cdx-unist")
            ok = True
            break
        if b and html_ok(b[0]):
            t = b[0].decode("utf-8", "ignore")
            for u in re.findall(r'href="([^"]+\.pdf[^"]*)"', t, re.I):
                u2 = urljoin("https://scholarworks.unist.ac.kr/", mod_html.unescape(u))
                b2 = get_url(u2, timeout=(15, 120))
                if b2 and pdf_ok(b2[0]):
                    simpan_pdf(69, b2[0], u2, "unist-bitstream")
                    ok = True
                    break
        if ok:
            break
    if not ok:
        catat(69, status="masih-gagal", cara=f"cdx-unist {len(snap)} snap")

# B. Dataverse Bowen 77
if not sudah(77):
    kand = []
    b = get_url("https://doi.org/10.17615/eavc-4296", timeout=(15, 60))
    if b:
        t = b[0].decode("utf-8", "ignore")
        for u in re.findall(r'href="([^"]+)"', t, re.I):
            if "api/access/datafile" in u:
                kand.append(urljoin(b[2], mod_html.unescape(u)))
    print(f"   dataverse 77: {len(kand)} kandidat")
    for u in kand[:4]:
        b = get_url(u, timeout=(15, 120))
        if b and pdf_ok(b[0]):
            simpan_pdf(77, b[0], u, "unc-dataverse")
            break

# C. De Gruyter dengan sesi utk 3
if not sudah(3):
    s = requests.Session()
    s.headers.update(HDR)
    try:
        for i in range(3):
            r = s.get("https://www.degruyterbrill.com/document/doi/10.1515/applirev-2021-0120/pdf",
                      timeout=(15, 60))
            if pdf_ok(r.content):
                simpan_pdf(3, r.content, r.url, "degruyter-sesi")
                break
    except Exception as e:
        print("   degruyter err", type(e).__name__)

# D. EuropePMC backend utk 26
if not sudah(26):
    for u in ("https://europepmc.org/backend/ftpmc/PMC9830631",
              "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC9830631/fullTextPDF"):
        b = get_url(u, timeout=(15, 60))
        if b and pdf_ok(b[0]):
            simpan_pdf(26, b[0], u, "epmc-backend")
            break

# E. debug href penulis
for label, halaman in (("gzhou", "https://gzhou.pages.wm.edu/"),
                       ("steven", "https://stevenmhernandez.com/research")):
    try:
        r = requests.get(halaman, headers=HDR, timeout=(15, 45))
        pdfs = re.findall(r'href="([^"]+\.pdf[^"]*)"', r.text, re.I)
        print(f"   {label}: {len(pdfs)} tautan-pdf")
        for u in pdfs[:14]:
            print("      ", u[:112])
    except Exception as e:
        print(f"   {label} err", type(e).__name__)

HASIL_PATH.write_text(json.dumps(hasil, ensure_ascii=False, indent=1, sort_keys=True),
                      encoding="utf-8")
n = {}
for v in hasil.values():
    n[v.get("status", "?")] = n.get(v.get("status", "?"), 0) + 1
print("\n=== RINGKASAN ===")
for k in sorted(n):
    print(f"{k:16}: {n[k]}")
