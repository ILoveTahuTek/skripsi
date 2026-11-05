#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""buat_pdf_teks.py — teks resmi hasil pengambilan halaman (WebFetch) -> PDF artikel."""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from data_pustaka import REFS
from artikelkan_semua import html_dari_teks

AKAR = Path("/home/z/my-project/download/pustaka-sibi")
DIR_PDF = AKAR / "pdf"
DIR_WEB = AKAR / "halaman-web"
HASIL_PATH = AKAR / "_hasil.json"
hasil = json.loads(HASIL_PATH.read_text(encoding="utf-8"))
KEY = {r["no"]: r["key"] for r in REFS}
HARI = "05-11-2026"

TEKS_PATH = Path(__file__).parent / "teks_webfetch.json"
data = json.loads(TEKS_PATH.read_text(encoding="utf-8"))

from weasyprint import HTML


def simpan():
    HASIL_PATH.write_text(json.dumps(hasil, ensure_ascii=False, indent=1, sort_keys=True),
                          encoding="utf-8")


for no_s, item in data.items():
    no = int(no_s)
    if hasil.get(no_s, {}).get("status") in ("pdf", "docx"):
        continue
    html = html_dari_teks(item["judul"], item["teks"])
    ftmp = DIR_WEB / f"{no:02d} - {KEY[no]} (teks resmi).html"
    ftmp.write_text(html, encoding="utf-8")
    out = DIR_PDF / f"{no:02d} - {KEY[no]}.pdf"
    try:
        HTML(string=html).write_pdf(str(out))
        sz = out.stat().st_size
        if sz > 10000:
            hasil[no_s] = {"status": "pdf", "key": KEY[no], "berkas": str(out),
                           "sumber": item["sumber"],
                           "catatan": item.get("catatan", "") +
                                      f" Isi teks resmi diambil langsung dari sumber pada {HARI} "
                                      "dan dicetak ke PDF (dokumen dokumen)."}
            simpan()
            print(f"{no:02d}: PDF OK ({sz // 1024} KB)")
        else:
            out.unlink()
            print(f"{no:02d}: render kecil ({sz} B)")
    except Exception as ex:
        print(f"{no:02d}: gagal {type(ex).__name__}: {str(ex)[:70]}")
print("selesai")
