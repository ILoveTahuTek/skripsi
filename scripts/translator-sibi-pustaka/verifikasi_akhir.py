#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verifikasi_akhir.py — perbaiki rujukan 09 (salin salah artikel) via pencarian
dokumen Garuda, lalu verifikasi judul seluruh PDF dengan pdftotext.
"""
import html as mod_html
import json
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import urljoin, unquote

import requests

sys.path.insert(0, str(Path(__file__).parent))
from unduh_pustaka import DIR_PDF, HDR, get_url, pdf_ok
from data_pustaka import REFS

AKAR = DIR_PDF.parent
HASIL_PATH = AKAR / "_hasil.json"
hasil = json.loads(HASIL_PATH.read_text(encoding="utf-8"))
KEY = {r["no"]: r["key"] for r in REFS}

# ---------- 1. perbaiki rujukan 09 ----------
tujuan9 = DIR_PDF / "09 - Mursita-2015-SIBI-BISINDO-INKLUSI.pdf"


def pdftotext(path, maxc=3000):
    try:
        out = subprocess.run(["pdftotext", "-l", "3", str(path), "-"],
                             capture_output=True, timeout=60)
        return out.stdout.decode("utf-8", "ignore")[:maxc]
    except Exception:
        return ""


kandidat9 = []
for url in ("https://garuda.kemdiktisaintek.go.id/documents?q=RESPON+TUNARUNGU+PENGGUNAAN+SISTEM+BAHASA+ISYARAT+MURSITA",
            "https://garuda.kemdiktisaintek.go.id/documents?q=Mursita+SIBI+BISINDO"):
    b = get_url(url, timeout=(15, 60))
    if not b:
        continue
    t = b[0].decode("utf-8", "ignore")
    for u in re.findall(r'href="([^"]+)"', t, re.I):
        u2 = urljoin("https://garuda.kemdiktisaintek.go.id/", mod_html.unescape(u))
        if "download.garuda" in u2 or re.search(r'(/article/download/|/document/view/\d+)', u2, re.I):
            kandidat9.append(u2)
    if kandidat9:
        break

# juga scrape halaman issue: blok sekitar 'RESPON TUNARUNGU'
b = get_url("https://garuda.kemdiktisaintek.go.id/journal/view/10423?issue=Vol.%202%20No.%202%20(2015)",
            timeout=(15, 90))
if b:
    t = b[0].decode("utf-8", "ignore")
    i = t.find("RESPON TUNARUNGU")
    if i < 0:
        i = t.lower().find("mursita")
    if i >= 0:
        blok = t[max(0, i - 3000):i + 3000]
        for u in re.findall(r'href="([^"]+)"', blok, re.I):
            u2 = urljoin("https://garuda.kemdiktisaintek.go.id/", mod_html.unescape(u))
            if "download.garuda" in u2 or "/article/download/" in u2:
                kandidat9.insert(0, u2)

print(f"kandidat 09: {len(kandidat9)}")
ok9 = False
tmp = Path("/tmp/tes09.pdf")
for u in kandidat9[:10]:
    print("  coba:", u[:110])
    b = get_url(u, timeout=(15, 120))
    if b and pdf_ok(b[0]):
        tmp.write_bytes(b[0])
        teks = pdftotext(tmp, 6000)
        if re.search(r'tunarungu', teks, re.I) and re.search(r'(SIBI|BISINDO)', teks, re.I):
            tujuan9.write_bytes(b[0])
            e = hasil["9"]
            e.update(status="pdf", berkas=str(tujuan9), sumber=u, cara="garuda-doc-perbaikan")
            hasil["9"] = e
            print("  09 DIPERBAIKI dari:", u[:100])
            ok9 = True
            break
        else:
            kepala = " ".join(teks.split())[:120]
            print("    salah isi:", kepala)
if not ok9:
    print("  09: tidak ditemukan kandidat yang cocok")

# ---------- 2. verifikasi judul semua PDF ----------
KUNCI = {
    4: ("sign language", "hearing parents"),
    6: ("penyandang disabilitas",),
    7: ("assistive", "deaf"),
    9: ("tunarungu",),
    11: ("sibi", "tunarungu"),
    13: ("opensibi", "isyarat"),
    15: ("convolutional", "sign language"),
    16: ("mediapipe", "isyarat"),
    17: ("jetpack", "isyarat"),
    20: ("channel state information",),
    22: ("df-wislr", "sign language"),
    26: ("respiratory",),
    29: ("esp32-s3",),
    32: ("robust speech recognition", "whisper"),
    34: ("scaling speech technology", "1,000"),
    40: ("widar",),
    41: ("yolo26",),
    47: ("sign language",),
    48: ("pgmi", "tunarungu", "holistik"),
    49: ("pembina", "isyarat", "sibi"),
    50: ("bahasa isyarat",),
    52: ("bisindo", "lstm"),
    54: ("csi", "gesture"),
    55: ("telegraph",),
    56: ("presence of noise",),
    57: ("wi-sl", "gesture"),
    60: ("pose estimation",),
    61: ("yolo26",),
    62: ("mediapipe",),
    63: ("person-in-wifi", "person perception"),
    64: ("densepose",),
    68: ("support",),
    70: ("convolutional neural network", "1-d"),
    79: ("attitudes",),
    80: ("distilling",),
}

print("\n=== VERIFIKASI JUDUL PDF ===")
perlu_perhatian = []
for no in sorted(KUNCI):
    kunci = KUNCI[no]
    p = DIR_PDF / f"{no:02d} - {KEY[no]}.pdf"
    if not p.exists():
        print(f"{no:02d} HILANG: {p.name}")
        perlu_perhatian.append(no)
        continue
    teks = pdftotext(p, 8000).lower()
    if not teks.strip():
        print(f"{no:02d} teks kosong (kemungkinan pindai/gambar) — {p.name[:58]}")
        continue
    if any(k.lower() in teks for k in kunci):
        print(f"{no:02d} OK — {p.name[:64]}")
    else:
        cuplik = " ".join(teks.split())[:100]
        print(f"{no:02d} COCOK-TIDAK? kunci={kunci} | {cuplik}")
        perlu_perhatian.append(no)

print("\nperlu perhatian:", perlu_perhatian or "tidak ada")
HASIL_PATH.write_text(json.dumps(hasil, ensure_ascii=False, indent=1, sort_keys=True),
                      encoding="utf-8")
