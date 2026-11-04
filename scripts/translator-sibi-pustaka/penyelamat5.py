#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""penyelamat5.py — putaran pamungkas: cermin penulis (OregonState, MIT, VCU, NCSU), debug poltekba/univrab/brin."""
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


def sudah(no):
    return hasil.get(str(no), {}).get("status") == "pdf"


def coba(no, urls, cara):
    for u in urls:
        b = get_url(u, timeout=(15, 120))
        if b and pdf_ok(b[0]):
            return simpan_pdf(no, b[0], u, cara)
    return False


# 68 Cortes & Vapnik — cermin Oregon State
if not sudah(68):
    if not coba(68, ["https://web.engr.oregonstate.edu/~huanlian/teaching/ML/2018spring/extra/svn-1995.pdf"],
                "cermin-oregonstate"):
        catat(68, status="masih-gagal", cara="cermin-oregonstate")

# 59 Hernandez & Bulut — server VCU penulis
if not sudah(59):
    if not coba(59, ["https://www.people.vcu.edu/~ebulut/wowmom20-WiFiSensing.pdf"], "penulis-vcu"):
        catat(59, status="masih-gagal", cara="penulis-vcu")

# 71 Chow — MIT DSpace AIM-175.pdf
if not sudah(71):
    kand = ["https://dspace.mit.edu/bitstream/handle/1721.1/6177/AIM-175.pdf?sequence=1",
            "https://dspace.mit.edu/bitstream/handle/1721.1/6177/AIM-175.pdf"]
    b = get_url("https://dspace.mit.edu/entities/publication/3d09633b-df6a-4051-8915-66bb2ae5b236",
                timeout=(15, 60))
    if b:
        for u in re.findall(r'href="([^"]+)"', b[0].decode("utf-8", "ignore"), re.I):
            if "bitstream" in u.lower():
                kand.append(urljoin("https://dspace.mit.edu/", mod_html.unescape(u)))
    if not coba(71, kand[:8], "mit-dspace"):
        catat(71, status="masih-gagal", cara="mit-dspace")

# 25 Ali keystroke — halaman publikasi Shahzad (NCSU)
if not sudah(25):
    kand = []
    b = get_url("https://people.engr.ncsu.edu/mshahza/", timeout=(15, 60))
    if b:
        t = b[0].decode("utf-8", "ignore")
        for u in re.findall(r'href="([^"]+)"', t, re.I):
            if re.search(r'(publications?|papers?)', u, re.I):
                kand.append(urljoin("https://people.engr.ncsu.edu/", mod_html.unescape(u)))
        print(f"   ncsu 25: {len(kand)} halaman publikasi")
    pdf_kand = []
    for hal in kand[:4]:
        b2 = get_url(hal, timeout=(15, 60))
        if not b2:
            continue
        for u in re.findall(r'href="([^"]+\.pdf[^"]*)"', b2[0].decode("utf-8", "ignore"), re.I):
            u2 = urljoin(hal, mod_html.unescape(u))
            if re.search(r'(keystroke|key|wifi|ali)', u2, re.I):
                pdf_kand.append(u2)
    print(f"   ncsu 25: {len(pdf_kand)} kandidat pdf")
    for u in pdf_kand[:6]:
        print("      ", u[:104])
    if pdf_kand:
        if not coba(25, pdf_kand[:6], "penulis-ncsu"):
            catat(25, status="masih-gagal", cara="penulis-ncsu")
    else:
        catat(25, status="masih-gagal", cara="penulis-ncsu (tidak ada)")

# 12 poltekba — dump semua href utk lihat galley
if not sudah(12):
    b = get_url("https://jurnal.poltekba.ac.id/index.php/jst/article/view/732", timeout=(15, 60))
    if b:
        t = b[0].decode("utf-8", "ignore")
        hrefs = [mod_html.unescape(u) for u in re.findall(r'href="([^"]+)"', t, re.I)]
        menarik = [u for u in hrefs if re.search(r'(article|pdf|download|galley)', u, re.I)]
        print(f"   poltekba 12: {len(menarik)} href menarik:")
        for u in menarik[:15]:
            print("      ", u[:110])
        kand = []
        for u in menarik:
            u2 = urljoin("https://jurnal.poltekba.ac.id/", u)
            u3 = u2.replace("/article/view/", "/article/download/")
            kand += [u3, u2]
        if not coba(12, kand[:10], "poltekba-href"):
            catat(12, status="masih-gagal", cara="poltekba-href")
    else:
        catat(12, status="masih-gagal", cara="poltekba (landing gagal)")

# 73 univrab — jina + dump teks
if not sudah(73):
    t = None
    try:
        r = requests.get("https://r.jina.ai/https://jurnal.univrab.ac.id/index.php/rabit/article/view/8340",
                         headers=HDR, timeout=(15, 120))
        if r.status_code == 200:
            t = r.text
    except Exception:
        pass
    if t:
        print(f"   jina 73: {len(t)} karakter")
        kand = [u for u in re.findall(r'\((https?://[^\s)]+)\)', t)
                if re.search(r'(/article/(view|download)/\d+|\.pdf)', u, re.I)]
        kand = [u.replace("/article/view/", "/article/download/") for u in kand]
        for u in kand[:6]:
            print("      ", u[:110])
        if kand:
            if not coba(73, kand[:6], "jina-univrab"):
                catat(73, status="masih-gagal", cara="jina-univrab")
        else:
            print("   jina 73: cuplikan:", t[:400].replace("\n", " ")[:380])
            catat(73, status="masih-gagal", cara="jina-univrab (tanpa tautan)")
    else:
        catat(73, status="masih-gagal", cara="jina-univrab (gagal)")

# 8 brin — varian + jina + cdx
if hasil.get("8", {}).get("status") not in ("halaman", "pdf"):
    for u in ("https://brin.go.id/news/130095", "https://brin.go.id/news/130095/",
              "https://www.brin.go.id/news/130095"):
        b = get_url(u, timeout=(15, 45))
        if b and b[0] and 200:
            if pdf_ok(b[0]):
                p = DIR_WEB / "08 - BRIN-2026-Ekosistem-Bahasa-Isyarat.pdf"
                p.write_bytes(b[0])
                catat(8, status="halaman", berkas=str(p), sumber=u, cara="langsung")
                break
            if html_ok(b[0]) and "not found" not in b[0][:3000].lower():
                p = DIR_WEB / "08 - BRIN-2026-Ekosistem-Bahasa-Isyarat.html"
                p.write_bytes(b[0])
                catat(8, status="halaman", berkas=str(p), sumber=u, cara="langsung")
                break
    if hasil.get("8", {}).get("status") not in ("halaman", "pdf"):
        try:
            r = requests.get("https://r.jina.ai/https://brin.go.id/news/130095",
                             headers=HDR, timeout=(15, 90))
            if r.status_code == 200 and len(r.text or "") > 500:
                p = DIR_WEB / "08 - BRIN-2026-Ekosistem-Bahasa-Isyarat.md"
                p.write_text(r.text, encoding="utf-8")
                catat(8, status="halaman", berkas=str(p),
                      sumber="https://brin.go.id/news/130095", cara="jina-reader")
        except Exception:
            pass
    if hasil.get("8", {}).get("status") not in ("halaman", "pdf"):
        try:
            r = requests.get("https://web.archive.org/cdx/search/cdx",
                             params={"url": "brin.go.id/news/130095*", "output": "json",
                                     "limit": 8, "filter": "statuscode:200"},
                             headers=HDR, timeout=25)
            snap = [(row[1], row[2]) for row in r.json()[1:]] if (r.text or "").strip() else []
            print(f"   cdx 8: {len(snap)} snapshot")
            for ts, asli in snap[:4]:
                w = f"https://web.archive.org/web/{ts}id_/{asli}"
                b = get_url(w, timeout=(15, 120))
                if b and html_ok(b[0]):
                    p = DIR_WEB / "08 - BRIN-2026-Ekosistem-Bahasa-Isyarat.html"
                    p.write_bytes(b[0])
                    catat(8, status="halaman", berkas=str(p), sumber=w, cara="cdx")
                    break
        except Exception:
            pass

HASIL_PATH.write_text(json.dumps(hasil, ensure_ascii=False, indent=1, sort_keys=True),
                      encoding="utf-8")
n = {}
for v in hasil.values():
    n[v.get("status", "?")] = n.get(v.get("status", "?"), 0) + 1
print("\n=== RINGKASAN PUTARAN PAMUNGKAS ===")
for k in sorted(n):
    print(f"{k:16}: {n[k]}")
