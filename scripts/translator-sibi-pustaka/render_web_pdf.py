#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""render_web_pdf.py — print-to-PDF untuk 8 rujukan web-native (kartu model,
dokumentasi, berita) supaya tiap rujukan punya artefak dokumen (PDF)."""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from data_pustaka import REFS

AKAR = Path("/home/z/my-project/download/pustaka-sibi")
DIR_WEB = AKAR / "halaman-web"
DIR_PDF = AKAR / "pdf"
HASIL_PATH = AKAR / "_hasil.json"
hasil = json.loads(HASIL_PATH.read_text(encoding="utf-8"))
KEY = {r["no"]: r["key"] for r in REFS}

WEBN = {5, 8, 10, 35, 36, 37, 38, 42}

from weasyprint import HTML

ok = []
for no in sorted(WEBN):
    e = hasil.get(str(no), {})
    if e.get("status") != "halaman":
        continue
    berkas_html = e.get("berkas", "")
    if not berkas_html or not Path(berkas_html).exists():
        cand = list(DIR_WEB.glob(f"{no:02d} -*"))
        if not cand:
            print(f"{no:02d}: sumber html tidak ada — lewati")
            continue
        berkas_html = str(cand[0])
    tujuan = DIR_PDF / f"{no:02d} - {KEY[no]} (render halaman web).pdf"
    try:
        HTML(filename=berkas_html).write_pdf(str(tujuan))
        size = tujuan.stat().st_size
        if size > 20000:
            e["berkas"] = f"{berkas_html};{tujuan}"
            e["catatan"] = (e.get("catatan", "") +
                            " | Ditambahkan PDF render halaman (print-to-PDF) agar berbentuk dokumen.")
            hasil[str(no)] = e
            ok.append((no, size))
            print(f"{no:02d} PDF render OK ({size//1024} KB)")
        else:
            tujuan.unlink()
            print(f"{no:02d} render terlalu kecil ({size} B) — html asli dipertahankan")
    except Exception as ex:
        print(f"{no:02d} gagal render: {type(ex).__name__}: {str(ex)[:60]}")
        if tujuan.exists():
            tujuan.unlink()

HASIL_PATH.write_text(json.dumps(hasil, ensure_ascii=False, indent=1, sort_keys=True), encoding="utf-8")
print("render selesai:", ok)
