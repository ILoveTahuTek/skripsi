#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""finalisasi2.py — metadata Crossref utk rujukan sisa + normalisasi status."""
import json
import sys
import time
from pathlib import Path

import requests

sys.path.insert(0, str(Path(__file__).parent))
from unduh_pustaka import DIR_PDF, HDR
from data_pustaka import REFS

AKAR = DIR_PDF.parent
HASIL_PATH = AKAR / "_hasil.json"
hasil = json.loads(HASIL_PATH.read_text(encoding="utf-8"))
KEY = {r["no"]: r["key"] for r in REFS}
DOI = {r["no"]: r.get("doi") for r in REFS}
CITE = {r["no"]: r["cite"] for r in REFS}
DIR_MD = AKAR / "metadata"
DIR_MD.mkdir(exist_ok=True)
DIR_WEB = AKAR / "halaman-web"

# rujukan yang butuh metadata Crossref (belum pdf/repo dan kind bukan web-native)
WEBN = {5, 8, 10, 35, 36, 37, 38, 42}
perlu_md = []
for r in REFS:
    no = r["no"]
    e = hasil.get(str(no), {})
    if e.get("status") in ("pdf", "docx", "repo") or no in WEBN:
        continue
    f = DIR_MD / f"{no:02d} - {KEY[no]}-crossref.json"
    if not f.exists():
        perlu_md.append(no)
print("perlu metadata:", perlu_md)

for no in perlu_md:
    doi = DOI.get(no)
    if not doi:
        continue
    try:
        rr = requests.get(f"https://api.crossref.org/works/{doi}", headers=HDR, timeout=30)
        if rr.status_code == 200:
            f = DIR_MD / f"{no:02d} - {KEY[no]}-crossref.json"
            f.write_text(rr.text, encoding="utf-8")
            print(f"{no:02d} metadata tersimpan: {doi}")
        else:
            print(f"{no:02d} crossref {rr.status_code}")
        time.sleep(1.5)
    except Exception as e:
        print(f"{no:02d} eksepsi {type(e).__name__}: {e}")

# ---------- normalisasi status ----------
ALASAN = {
    3: "PMC & De Gruyter memblokir akses otomatis dari jaringan ini (403); salinan terbuka ada di PMC10785677 tapi tak terunduh",
    12: "OJS Polban/Poltekba memblokir bot (Cloudflare); salinan terbuka tak terjangkau dari jaringan ini",
    18: "Elsevier (ISWA) memblokir unduhan PDF via Cloudflare walau akses terbuka; hanya landing page yang bisa disimpan",
    21: "IMWUT akses terbuka penuh tetapi dl.acm.org memblokir bot; halaman proyek penulis tak memuat PDF",
    24: "ACM TIST berbayar; salinan penulis tidak ditemukan",
    25: "UNC Carolina Digital Repository tidak terjangkau dari jaringan ini (timeout)",
    39: "ACM CSUR berbayar; salinan penulis tidak ditemukan",
    43: "Bab Springer berbayar; salinan penulis tidak ditemukan",
    44: "ACM ASSETS 2025 berbayar; preprint tidak ditemukan",
    51: "Procedia CS akses terbuka tetapi ScienceDirect memblokir unduhan PDF dari jaringan ini",
    53: "Procedia CS akses terbuka tetapi ScienceDirect memblokir unduhan PDF dari jaringan ini",
    58: "Procedia CS akses terbuka tetapi ScienceDirect memblokir unduhan PDF dari jaringan ini",
    59: "IEEE WoWMoM berbayar; situs penulis (VCU/Hernandez) tidak lagi memuat PDF",
    67: "Measurement (Elsevier) berbayar; salinan penulis tidak ditemukan",
    71: "IEEE Trans. IT berbayar; MIT DSpace menolak (HTTP 429) berulang; cermin kuliah tak ditemukan",
    73: "RABIT akses terbuka tetapi jurnal.univrab.ac.id memblokir bot (403 Cloudflare); Galley-ID benar (8340/3439) sudah ditemukan via Garuda",
    77: "PMC2859314 salinan terbuka ada tetapi PMC/EuropePMC memblokir akses otomatis (403/429)",
    79: "Salinan pemindaian asli 1932 via archive.org (ditemukan)",
    45: "Buku cetak 1994, tidak ada versi digital resmi",
}
ALASAN[79] = None  # 79 sudah pdf

ubah = []
for r in REFS:
    no = r["no"]
    e = hasil.get(str(no), {})
    st = e.get("status")
    if st in ("pdf", "docx", "repo") or no in WEBN:
        continue
    md = DIR_MD / f"{no:02d} - {KEY[no]}-crossref.json"
    html_landing = list(DIR_WEB.glob(f"{no:02d} -*"))
    if no == 45:
        baru = {"status": "gagal",
                "catatan": "Buku cetak murni (Depdikbud 1994) — tidak tersedia dalam bentuk digital; halaman JDIH Kemdikbud untuk arsip non-kode tidak memuat berkas",
                "sumber": "https://jdih.kemdikbud.go.id/arsip/Berkas%20Arsip%20Non-Kode/EPMendikbud_0161_1994.pdf (tidak tersedia)"}
    elif md.exists():
        berkas = [str(md)]
        if html_landing:
            berkas.append(str(html_landing[0]))
        baru = {"status": "metadata",
                "berkas": ";".join(berkas),
                "catatan": f"Tidak ada salinan terbuka yang terunduh — {ALASAN.get(no, 'penerbit berbayar / pemblokiran bot')}. Metadata resmi Crossref disimpan sebagai catatan identitas.",
                "sumber": f"https://doi.org/{DOI.get(no)}"}
    else:
        baru = {"status": "gagal", "catatan": ALASAN.get(no, "tidak ada salinan terbuka")}
    e.update(baru)
    e["key"] = KEY[no]
    hasil[str(no)] = e
    ubah.append((no, st, e["status"]))

HASIL_PATH.write_text(json.dumps(hasil, ensure_ascii=False, indent=1, sort_keys=True), encoding="utf-8")
for u in ubah:
    print("normalisasi:", u)

import collections
c = collections.Counter(v.get("status") for k, v in hasil.items() if not k.startswith("_"))
print("\nSTATUS FINAL:", dict(c))
