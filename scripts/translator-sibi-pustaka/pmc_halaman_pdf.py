#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""pmc_halaman_pdf.py — halaman PMC (artikel lengkap) -> PDF utk rujukan biomedis."""
import json
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from data_pustaka import REFS

AKAR = Path("/home/z/my-project/download/pustaka-sibi")
DIR_PDF = AKAR / "pdf"
DIR_WEB = AKAR / "halaman-web"
HASIL_PATH = AKAR / "_hasil.json"
hasil = json.loads(HASIL_PATH.read_text(encoding="utf-8"))
KEY = {r["no"]: r["key"] for r in REFS}

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36")

PMC = {3: "PMC10785677", 77: "PMC2859314"}


def simpan():
    HASIL_PATH.write_text(json.dumps(hasil, ensure_ascii=False, indent=1, sort_keys=True),
                          encoding="utf-8")


for no, pmcid in PMC.items():
    if hasil.get(str(no), {}).get("status") == "pdf":
        print(f"{no:02d}: sudah pdf")
        continue
    fhtml = DIR_WEB / f"{no:02d} - {KEY[no]} (PMC).html"
    subprocess.run(["curl", "-sL", "--max-time", "90", "-A", UA,
                    "-o", str(fhtml), f"https://pmc.ncbi.nlm.nih.gov/articles/{pmcid}/"],
                   capture_output=True, timeout=120)
    if not fhtml.exists() or fhtml.stat().st_size < 30000:
        print(f"{no:02d}: unduh halaman gagal (curl)")
        continue
    from weasyprint import HTML
    out = DIR_PDF / f"{no:02d} - {KEY[no]}.pdf"
    try:
        HTML(filename=str(fhtml)).write_pdf(str(out))
        sz = out.stat().st_size
        if sz > 50000:
            hasil[str(no)] = {"status": "pdf", "key": KEY[no], "berkas": str(out),
                              "sumber": f"https://pmc.ncbi.nlm.nih.gov/articles/{pmcid}/",
                              "catatan": "Artikel teks lengkap resmi (PMC, salinan terbuka) "
                                         "dicetak ke PDF"}
            simpan()
            print(f"{no:02d}: PDF PMC OK ({sz // 1024} KB)")
        else:
            out.unlink()
            print(f"{no:02d}: render kecil ({sz} B)")
    except Exception as ex:
        print(f"{no:02d}: render gagal: {type(ex).__name__} {str(ex)[:60]}")
print("selesai")
