#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""penyelamat6.py — putaran akhir: BRIN slug asli, Garuda INKLUSI, debug VCU/DSpace/NCSU/poltekba."""
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


# ---------- 8 BRIN: URL slug asli ----------
u8 = "https://www.brin.go.id/news/130095/survei-ungkap-777-penyandang-tuli-menggunakan-bisindo"
b = get_url(u8, timeout=(15, 90))
if b and pdf_ok(b[0]):
    p = DIR_WEB / "08 - BRIN-2026-Ekosistem-Bahasa-Isyarat.pdf"
    p.write_bytes(b[0])
    catat(8, status="halaman", berkas=str(p), sumber=u8, cara="brin-slug")
elif b and html_ok(b[0]) and "not found" not in b[0][:3000].decode("utf-8", "ignore").lower():
    p = DIR_WEB / "08 - BRIN-2026-Ekosistem-Bahasa-Isyarat.html"
    p.write_bytes(b[0])
    catat(8, status="halaman", berkas=str(p), sumber=u8, cara="brin-slug")
else:
    print(f"   brin: status={None if not b else 'hal/other'} len={len(b[0]) if b else 0}")

# ---------- 9 INKLUSI: Garuda ----------
if hasil.get("9", {}).get("status") != "pdf":
    kand = []
    for hal in ("https://garuda.kemdiktisaintek.go.id/journal/view/10423?issue=Vol.%202%20No.%202%20(2015)",
                "https://garuda.kemdikbud.go.id/journal/view/10423"):
        b = get_url(hal, timeout=(15, 90))
        if not b:
            continue
        t = b[0].decode("utf-8", "ignore")
        for u in re.findall(r'href="([^"]+)"', t, re.I):
            if re.search(r'(mursita|inklusi|ijds)', u, re.I) or ("download" in u.lower() and "2202" in u):
                kand.append(urljoin(hal, mod_html.unescape(u)))
        # tautan "Full PDF" dekat judul
        if not kand:
            # cari blok <a> berisi 'Full PDF' dengan konteks mursita
            for m in re.finditer(r'<a[^>]+href="([^"]+)"[^>]*>\s*Full\s*PDF', t, re.I):
                kand.append(urljoin(hal, m.group(1)))
        if kand:
            break
    print(f"   garuda 9: {len(kand)} kandidat")
    for u in kand[:8]:
        print("      ", u[:110])
    ok = False
    for u in kand[:8]:
        b = get_url(u, timeout=(15, 120))
        if b and pdf_ok(b[0]):
            simpan_pdf(9, b[0], u, "garuda")
            ok = True
            break
    if not ok:
        catat(9, status="masih-gagal", cara=f"garuda({len(kand)})")

# ---------- 59 VCU: debug + wayback ----------
if hasil.get("59", {}).get("status") != "pdf":
    for u in ("https://www.people.vcu.edu/~ebulut/wowmom20-WiFiSensing.pdf",):
        try:
            r = requests.get(u, headers=HDR, timeout=(15, 60))
            print(f"   vcu 59: {r.status_code} {(r.headers.get('Content-Type') or '')[:40]} len={len(r.content)}")
            if r.status_code == 200 and pdf_ok(r.content):
                simpan_pdf(59, r.content, u, "penulis-vcu")
        except Exception as e:
            print("   vcu 59 err", type(e).__name__)

# ---------- 71 MIT: CDX bitstream ----------
if hasil.get("71", {}).get("status") != "pdf":
    try:
        r = requests.get("https://web.archive.org/cdx/search/cdx",
                         params={"url": "dspace.mit.edu/bitstream/handle/1721.1/6177*", "output": "json",
                                 "limit": 10, "filter": "statuscode:200"}, headers=HDR, timeout=30)
        snap = [(row[1], row[2]) for row in r.json()[1:]] if (r.text or "").strip() else []
        print(f"   cdx 71: {len(snap)} snapshot")
        for ts, asli in snap[:5]:
            print("      ", asli[:104])
            w = f"https://web.archive.org/web/{ts}id_/{asli}"
            b = get_url(w, timeout=(15, 120))
            if b and pdf_ok(b[0]):
                simpan_pdf(71, b[0], w, "cdx-dspace")
                break
    except Exception as e:
        print("   cdx 71 err", type(e).__name__)

# ---------- 25 NCSU: debug ----------
if hasil.get("25", {}).get("status") != "pdf":
    for hal in ("https://people.engr.ncsu.edu/mshahza/",
                "https://people.engr.ncsu.edu/mshahza/publications.html",
                "https://people.engr.ncsu.edu/mshahza/publications/"):
        b = get_url(hal, timeout=(15, 60))
        if not b:
            print(f"   ncsu: {hal[-30:]} gagal")
            continue
        t = b[0].decode("utf-8", "ignore")
        pdfs = re.findall(r'href="([^"]+\.pdf[^"]*)"', t, re.I)
        kand = [urljoin(hal, mod_html.unescape(u)) for u in pdfs if re.search(r'(keystroke|key)', u, re.I)]
        print(f"   ncsu {hal[-22:]}: {len(pdfs)} pdf, keystroke: {len(kand)}")
        for u in kand[:4]:
            print("      ", u[:104])
        if kand:
            for u in kand[:4]:
                b2 = get_url(u, timeout=(15, 90))
                if b2 and pdf_ok(b2[0]):
                    simpan_pdf(25, b2[0], u, "penulis-ncsu")
                    break
        if hasil.get("25", {}).get("status") == "pdf":
            break

# ---------- 12 poltekba: dump konteks PDF ----------
if hasil.get("12", {}).get("status") != "pdf":
    b = get_url("https://jurnal.poltekba.ac.id/index.php/jst/article/view/732", timeout=(15, 60))
    if b:
        t = b[0].decode("utf-8", "ignore")
        print(f"   poltekba: len={len(t)}")
        for m in re.finditer(r'PDF', t):
            awal = max(0, m.start() - 260)
            cuplik = t[awal:m.start() + 90].replace("\n", " ")
            print("      ...", cuplik[120:340])
            break
        # coba pola galley umum via jina
        try:
            r = requests.get("https://r.jina.ai/https://jurnal.poltekba.ac.id/index.php/jst/article/view/732",
                             headers=HDR, timeout=(15, 90))
            if r.status_code == 200:
                for u in re.findall(r'\((https?://[^\s)]+)\)', r.text):
                    if re.search(r'/article/(view|download)/732(/\d+)?', u):
                        print("      jina:", u[:110])
                        u2 = u.replace("/article/view/", "/article/download/")
                        b2 = get_url(u2, timeout=(15, 90))
                        if b2 and pdf_ok(b2[0]):
                            simpan_pdf(12, b2[0], u2, "poltekba-jina")
                            break
        except Exception:
            pass

HASIL_PATH.write_text(json.dumps(hasil, ensure_ascii=False, indent=1, sort_keys=True),
                      encoding="utf-8")
n = {}
for v in hasil.values():
    n[v.get("status", "?")] = n.get(v.get("status", "?"), 0) + 1
print("\n=== RINGKASAN PUTARAN 6 ===")
for k in sorted(n):
    print(f"{k:16}: {n[k]}")
