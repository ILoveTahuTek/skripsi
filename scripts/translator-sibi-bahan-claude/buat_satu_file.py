#!/usr/bin/env python3
"""Bangun PROMPT-SATU-FILE-LENGKAP.md — varian SATU BERKAS:
prompt satu-pesan (utuh, tak diubah) + naskah sumber (utuh, tak diubah)
digabung dengan penanda jelas, agar pemilik cukup menempel ISI SATU BERKAS
ke Claude sebagai satu pesan — tanpa lampiran apa pun."""
from pathlib import Path

PAKET = Path("/home/z/my-project/download/translator-sibi-bahan-claude")

prompt = (PAKET / "PROMPT-SATU-PESAN.md").read_text(encoding="utf-8").rstrip("\n")
naskah = (PAKET / "naskah-sumber.md").read_text(encoding="utf-8").rstrip("\n")

CATATAN = (
    "> **Catatan pengiriman (baca dulu):** Pesan ini berisi dua bagian — "
    "(1) perintah kerja utuh, lalu (2) lampiran `naskah-sumber.md` yang "
    "disertakan utuh setelah penanda \"MULAI NASKAH SUMBER\". Perlakukan "
    "seluruh bagian setelah penanda itu sebagai berkas `naskah-sumber.md`. "
    "Tidak ada lampiran terpisah."
)

MULAI = ("<!-- ===================== MULAI NASKAH SUMBER "
         "(isi berkas naskah-sumber.md, utuh dan tak diubah) "
         "===================== -->")
SELESAI = "<!-- ===================== SELESAI NASKAH SUMBER ===================== -->"

isi = (
    CATATAN + "\n\n"
    + prompt + "\n\n"
    + MULAI + "\n\n"
    + naskah + "\n\n"
    + SELESAI + "\n"
)

keluaran = PAKET / "PROMPT-SATU-FILE-LENGKAP.md"
keluaran.write_text(isi, encoding="utf-8")

baris = isi.count("\n") + 1
print(f"OK ditulis: {keluaran}")
print(f"  ukuran   : {keluaran.stat().st_size:,} byte")
print(f"  baris    : {baris:,}")
print(f"  memuat prompt utuh : {'## 6. Format output' in isi}")
print(f"  memuat naskah utuh : {naskah.splitlines()[0][:60] in isi}")
