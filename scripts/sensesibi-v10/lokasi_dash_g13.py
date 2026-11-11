#!/usr/bin/env python3
"""Replikasi penghitungan dash metrik.py: tampilkan baris prosa penyumbang pelanggaran."""
import re
import sys

LEWATI = re.compile(
    r"^\s*(\||!\[|#{1,6}\s|\[\d+\]|\d+\.\t|Gambar\s|Tabel\s|Pers\.|https?://|"
    r"Jl\.|e?ISSN|doi:|Vol\.|\u00a9|>\s|E-?mail|Received|Accepted|Published)", re.I)

src = open(sys.argv[1], encoding="utf-8").read()
# potong dari daftar pustaka
teks = re.split(r"(?im)^#{0,6}\s*(daftar pustaka|referensi|references|ucapan terima kasih)\s*$", src)[0]

total_em = 0
total_en = 0
for i, line in enumerate(teks.split("\n"), 1):
    if not line.strip() or LEWATI.match(line):
        continue
    body = re.sub(r"`{1,3}[^`]*`{1,3}", " ", line)
    body = re.sub(r"\$[^$]*\$", " ", body)
    body = re.sub(r"[*_]{1,3}", "", body)
    em = body.count("\u2014")
    en = len(re.findall(r"(?<!\d)\u2013|\u2013(?!\d)", body))
    if em or en:
        total_em += em
        total_en += en
        frag = [m for m in re.findall(r".{0,30}[\u2013\u2014].{0,30}", body)]
        print(f"baris-md {i}: em={em} en={en} | " + " || ".join(frag))

print(f"TOTAL em={total_em} en={total_en} -> pelanggaran={total_em + total_en}")
