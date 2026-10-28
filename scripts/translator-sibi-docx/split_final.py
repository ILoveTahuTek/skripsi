#!/usr/bin/env python3
"""Pisahkan naskah-untuk-docx.md (hasil Claude) menjadi 4 berkas bab agar kompatibel
dengan parse_md.js (yang membaca bab1/bab2/bab3/daftar-pustaka secara terpisah).
Blok kepala (judul, PROPOSAL PENELITIAN, tabel identitas, catatan penyusunan) TIDAK
ikut — sampul & identitas dibuat oleh generate_docx.js buildCover(), sama seperti
perilaku pipeline lama."""
from pathlib import Path

SUMBER = Path("/home/z/my-project/download/translator-sibi-final/_kerja/naskah-untuk-docx.md")
KELUARAN = Path("/home/z/my-project/download/translator-sibi-final/_kerja/split")

teks = SUMBER.read_text(encoding="utf-8")
baris = teks.split("\n")

# Cari indeks H1 batas
idx = {}
for i, l in enumerate(baris):
    if l.startswith("# "):
        if l.startswith("# BAB I "):
            idx["bab1"] = i
        elif l.startswith("# BAB II "):
            idx["bab2"] = i
        elif l.startswith("# BAB III "):
            idx["bab3"] = i
        elif l.startswith("# DAFTAR PUSTAKA"):
            idx["dp"] = i

urutan = ["bab1", "bab2", "bab3", "dp"]
for k in urutan:
    if k not in idx:
        raise SystemExit(f"H1 batas '{k}' tidak ditemukan")

nama_file = {
    "bab1": "bab1-pendahuluan.md",
    "bab2": "bab2-kajian-pustaka.md",
    "bab3": "bab3-metodologi.md",
    "dp": "daftar-pustaka.md",
}
batas = [idx["bab1"], idx["bab2"], idx["bab3"], idx["dp"], len(baris)]

KELUARAN.mkdir(parents=True, exist_ok=True)
for n, k in enumerate(urutan):
    potong = "\n".join(baris[batas[n]:batas[n + 1]]).strip("\n") + "\n"
    (KELUARAN / nama_file[k]).write_text(potong, encoding="utf-8")
    print(f"{nama_file[k]}: {batas[n+1]-batas[n]} baris, {len(potong.split()):,} kata")

# Verifikasi jumlah kata total = naskah - blok kepala
kepala = "\n".join(baris[:idx["bab1"]])
total_split = sum(len(("\n".join(baris[batas[n]:batas[n+1]])).split()) for n in range(4))
print(f"blok kepala dilewati: {idx['bab1']} baris ({len(kepala.split()):,} kata)")
print(f"total 4 berkas: {total_split:,} kata | naskah penuh: {len(teks.split()):,} kata")
assert total_split + len(kepala.split()) == len(teks.split()), "kata tidak balans!"
print("BALANS OK")
