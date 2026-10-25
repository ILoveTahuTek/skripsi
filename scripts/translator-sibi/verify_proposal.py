#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Verifikasi akhir Proposal-Revisi-Translator-SIBI.md:
jumlah blok mermaid, caption vs rujukan Gambar, integritas sitasi [n] <-> daftar pustaka,
penomoran tabel, keterbacaan penanda PERLU."""
import re, pathlib

P = pathlib.Path("/home/z/my-project/download/translator-sibi-revisi/Proposal-Revisi-Translator-SIBI.md")
t = P.read_text(encoding="utf-8")
masalah = []

# 1) Blok mermaid
mer = re.findall(r"```mermaid\n(.*?)```", t, re.S)
print(f"Blok mermaid: {len(mer)}")
if len(mer) != 10:
    masalah.append(f"Jumlah mermaid {len(mer)} != 10")

# 2) Caption Gambar vs rujukan dalam teks
caps = re.findall(r"^Gambar (\d+\.\d+) ", t, re.M)
print("Caption gambar:", ", ".join(caps))
for g in caps:
    n_ref = len(re.findall(rf"Gambar {re.escape(g)}\b(?!\s+\w)", t)) - 1  # kurangi caption
    body_refs = len(re.findall(rf"(pada|ditunjukkan|memperlihatkan|sebagaimana) [^.]*Gambar {re.escape(g)}\b", t))
    if body_refs < 1:
        # longgar: cukup ada rujukan selain caption
        if len(re.findall(rf"Gambar {re.escape(g)}", t)) < 2:
            masalah.append(f"Gambar {g} tidak dirujuk dalam teks")
print("Semua gambar dirujuk dalam teks:", "OK" if not any("tidak dirujuk" in m for m in masalah) else "GAGAL")

# 3) Integritas sitasi
sitos = [int(x) for x in re.findall(r"\[(\d+)\]", t.split("# DAFTAR PUSTAKA")[0])]
dp = re.findall(r"^\[(\d+)\] ", t.split("# DAFTAR PUSTAKA")[1], re.M)
dp_nums = [int(x) for x in dp]
print(f"Sitasi teks: {len(sitos)} kali; entri DP: {len(dp_nums)}; nomor DP 1..{max(dp_nums) if dp_nums else 0}")
if sorted(set(dp_nums)) != list(range(1, len(dp_nums) + 1)):
    masalah.append("Penomoran DP tidak berurutan 1..N")
if max(sitos) != len(dp_nums):
    masalah.append("Sitasi maksimum != jumlah entri DP")

# 4) Tabel
tabs = re.findall(r"^Tabel (\d+\.\d+) ", t, re.M)
print("Caption tabel:", ", ".join(tabs))
for tb in tabs:
    if len(re.findall(rf"Tabel {re.escape(tb)}", t)) < 2:
        masalah.append(f"Tabel {tb} tidak dirujuk dalam teks")

# 5) Penanda
print("PERLU DATA:", len(re.findall(r"\[PERLU DATA:", t)), "| PERLU RUJUKAN:", len(re.findall(r"\[PERLU RUJUKAN:", t)))
print("Sisa [@...] (harus 0):", len(re.findall(r"\[@", t)))

# 6) Pola terlarang cepat
for pat, label in [(r"\bdi mana\b", "di mana sebagai konektor"), (r"yang mana", "yang mana"),
                   (r"Di era", "opener era digital"), (r"tidak dapat dipungkiri", "klise")]:
    n = len(re.findall(pat, t))
    if n:
        masalah.append(f"Pola {label}: {n} kali")

print()
if masalah:
    print("MASALAH:")
    for m in masalah:
        print(" -", m)
else:
    print("SEMUA PEMERIKSAAN LOLOS")
