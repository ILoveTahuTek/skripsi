#!/usr/bin/env python3
"""Ekstrak blok mermaid dari naskah v10 sesuai keterangan Gambar 3.x -> berkas .mmd."""
import re, sys

MD = "/home/z/my-project/download/sensesibi-v10/Proposal-SenseSIBI-v10.md"
OUT = "/home/z/my-project/download/sensesibi-v10/diagram"

teks = open(MD, encoding="utf-8").read()
blok = re.findall(r"```mermaid\n(.*?)\n```\n\nGambar (\d+\.\d+)", teks, re.S)
print("Blok mermaid ditemukan:", len(blok))
if len(blok) != 10:
    print("GAGAL: harus 10 blok (3.1-3.10)"); sys.exit(1)

import os
os.makedirs(OUT, exist_ok=True)
urut = []
for isi, num in blok:
    path = f"{OUT}/G{num}.mmd"
    open(path, "w", encoding="utf-8").write(isi + "\n")
    urut.append(num)
    print(f"  Gambar {num} -> G{num}.mmd ({len(isi.splitlines())} baris)")

print("Urutan:", urut)
print("Nomor berurutan 3.1..3.10:", urut == [f"3.{i}" for i in range(1, 11)])
