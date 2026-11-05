#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""perbaiki_halaman.py — unduh ulang halaman Cloudflare via curl + render PDF."""
import json
import re
import subprocess
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

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36")

TARGET = {
    5: ("https://www.kemenkopmk.go.id/kemenko-pmk-bergerak-bersama-wujudkan-selaras-bahasa-isyarat", None),
    10: ("https://pkplk.kemendikdasmen.go.id/sibi", None),
    12: ("https://jurnal.poltekba.ac.id/index.php/jst/article/view/732", "galley"),
}


def simpan():
    HASIL_PATH.write_text(json.dumps(hasil, ensure_ascii=False, indent=1, sort_keys=True),
                          encoding="utf-8")


def catat(no, **kw):
    e = hasil.get(str(no), {})
    e.update(kw)
    e["key"] = KEY[no]
    hasil[str(no)] = e
    simpan()
    print(f"  {no:02d} [{kw.get('status')}] {str(kw.get('sumber', ''))[:90]}", flush=True)


# --- 38: markdown kartu model -> PDF ---
def kasus_38():
    md = DIR_WEB / "38 - Hexgrad-Kokoro-82M.md"
    if hasil.get("38", {}).get("status") == "pdf" or not md.exists():
        return
    teks = md.read_text(encoding="utf-8", errors="ignore")
    judul = "hexgrad/Kokoro-82M — Model Card (Hugging Face, Apache-2.0)"
    html = html_dari_teks(judul, teks)
    from weasyprint import HTML
    out = DIR_PDF / "38 - Hexgrad-Kokoro-82M (kartu model).pdf"
    HTML(string=html).write_pdf(str(out))
    if out.stat().st_size > 10000:
        catat(38, status="pdf", berkas=str(out),
              sumber="https://huggingface.co/hexgrad/Kokoro-82M",
              catatan="Kartu model resmi (Hugging Face, Apache-2.0) dirender ke PDF")
    else:
        print("38: render kecil")


for no, (url, mode) in TARGET.items():
    if hasil.get(str(no), {}).get("status") in ("pdf", "docx"):
        continue
    fhtml = DIR_WEB / f"{no:02d} - {KEY[no]}.html"
    subprocess.run(["curl", "-sL", "--max-time", "90", "-A", UA, "-o", str(fhtml), url],
                   capture_output=True, timeout=120)
    if not fhtml.exists() or fhtml.stat().st_size < 3000:
        print(f"{no:02d}: unduhan gagal/kecil")
        continue
    konten = fhtml.read_text(encoding="utf-8", errors="ignore")
    if "One moment, please" in konten or "Just a moment" in konten:
        print(f"{no:02d}: masih interstisial Cloudflare")
        fhtml.unlink()
        continue
    print(f"{no:02d}: HTML asli OK ({fhtml.stat().st_size // 1024} KB)")
    # 12: scan galley OJS
    if mode == "galley":
        kand = []
        for m in re.finditer(r'href="([^"]+(?:download|viewFile)[^"]*)"', konten, re.I):
            kand.append(m.group(1))
        for gal in re.findall(r'/article/view/(\d+)/(\d+)', konten):
            base = url.split("/article/")[0]
            kand.append(f"{base}/article/download/{gal[0]}/{gal[1]}")
        t = DIR_PDF / f"{no:02d} - {KEY[no]}.pdf"
        for u in list(dict.fromkeys(kand))[:8]:
            subprocess.run(["curl", "-sL", "--max-time", "90", "-A", UA, "-o", str(t), u],
                           capture_output=True, timeout=120)
            if t.exists() and t.stat().st_size > 15000 and t.read_bytes()[:5].startswith(b"%PDF"):
                catat(no, status="pdf", berkas=str(t), sumber=u,
                      catatan="PDF akses-terbuka (galley OJS Jurnal Sains Terapan)")
                break
        if hasil.get(str(no), {}).get("status") == "pdf":
            continue
    # render halaman -> PDF
    from weasyprint import HTML
    out = DIR_PDF / f"{no:02d} - {KEY[no]} (render halaman resmi).pdf"
    try:
        HTML(filename=str(fhtml)).write_pdf(str(out))
        sz = out.stat().st_size
        if sz > 20000:
            catat(no, status="pdf", berkas=f"{fhtml};{out}", sumber=url,
                  catatan="Halaman resmi sumber dirender ke PDF (print-to-PDF)")
        else:
            out.unlink()
            print(f"{no:02d}: render kecil ({sz} B) — html dipertahankan utk dokumentasi")
    except Exception as ex:
        print(f"{no:02d}: render gagal {type(ex).__name__}: {str(ex)[:60]}")

kasus_38()
print("selesai")
