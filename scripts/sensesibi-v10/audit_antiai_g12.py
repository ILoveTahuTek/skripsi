#!/usr/bin/env python3
"""Audit naskah v11 terhadap aturan anti-ai-writer (mchardyan/anti-ai-writer v2).

Memeriksa: kosakata terlarang, frasa terlarang, pembuka terlarang, em dash,
parataksis (>=3 kalimat deklaratif pendek beruntun), kalimat sama panjang
beruntun (>=3), dan ritme panjang kalimat.
"""
import re
import sys
from pathlib import Path

SRC = Path("/home/z/my-project/download/sensesibi-v10/_kerja-g12/src")

KOSAKATA = [
    "mendalami", "menyelami", "tapestri", "lanskap", "bukti nyata", "krusial",
    "kompleks", "rumit", "metikulus", "memperkuat", "meraih", "mengumpulkan",
    "menegaskan", "interaksi", "multidimensi", "bernuansa", "memupuk",
    "memanfaatkan", "memfasilitasi", "mencakup", "sangat penting", "mutakhir",
    "mengubah permainan", "transformatif", "merevolusi", "mulus", "tangguh",
    "komprehensif", "yang disebutkan sebelumnya", "memelopori", "menampilkan",
    "menyoroti", "menekankan", "meningkatkan", "luar biasa", "menakjubkan",
    "mendalam", "pada intinya", "sinergi", "ke depannya", "showcasing",
]
FRASA = [
    "Perlu dicatat bahwa", "Penting untuk dicatat", "Mari kita",
    "Dalam ranah", "Ketika berbicara soal", "Bukan hanya", "bukan cuma soal",
    "Di sinilah", "Pada akhirnya", "Intinya adalah", "Begini masalahnya",
    "Tanpa basa-basi", "Singkatnya", "Bersiaplah", "level berikutnya",
    "Buka potensi", "Memberdayakan", "menjembatangi kesenjangan",
    "menjembatani kesenjangan", "Kesimpulannya", "Secara keseluruhan",
    "Jangan ragu", "Di era", "tidak dapat dipungkiri", "hal ini",
    "seiring perkembangan", "seperti yang kita ketahui", "perlu diingat",
]
PEMBUKA = [
    "Tentu,", "Pastinya,", "Baik,", "Pertanyaan bagus", "Namun, penting untuk",
    "Selain itu,", "Lebih lanjut,", "Tambahan lagi,", "Menariknya,",
    "Perlu dicatat,", "Yang penting,", "Memang,", "Adapun",
]

def bersihkan(t):
    t = re.sub(r"```.*?```", "", t, flags=re.S)  # buang blok mermaid
    t = re.sub(r"^\|.*$", "", t, flags=re.M)      # buang baris tabel
    t = re.sub(r"^#{1,6} .*$", "", t, flags=re.M) # buang baris heading
    t = re.sub(r"^\d+\. .*$", "", t, flags=re.M)  # butir prosedur: paralel by konvensi
    t = re.sub(r"\[[^\]]*\]", "", t)              # buang [kunci]/[PERLU...]
    t = re.sub(r"[#>*`_]", "", t)
    return t

def main():
    teks = "\n\n".join(
        f.name.read_text if False else (SRC / f).read_text(encoding="utf-8")
        for f in ["00-header.md", "01-bab1.md", "02-bab2.md", "03-bab3.md"]
    )
    tubuh = bersihkan(teks)
    total_kata = len(tubuh.split())
    print(f"Total kata tubuh (tanpa tabel/mermaid): {total_kata}")

    print("\n== KOSAKATA/FRASA TERLARANG ==")
    n_temu = 0
    for p in KOSAKATA + FRASA + PEMBUKA:
        for m in re.finditer(re.escape(p), tubuh, re.I):
            ctx = tubuh[max(0, m.start() - 40):m.end() + 40].replace("\n", " ")
            print(f"  [{p}] ...{ctx}...")
            n_temu += 1
    if not n_temu:
        print("  (nol temuan)")

    print("\n== EM DASH (\u2014) ==")
    n = tubuh.count("\u2014")
    print(f"  {n}x (batas: 1 per 500 kata = ~{total_kata//500} izin)")

    print("\n== RITME KALIMAT ==")
    kalimat = [k.strip() for k in re.split(r"(?<=[.!?])\s+", tubuh) if len(k.split()) >= 3]
    pj = [len(k.split()) for k in kalimat]
    print(f"  Kalimat: {len(pj)}; rata-rata {sum(pj)/len(pj):.1f}; median {sorted(pj)[len(pj)//2]}; maks {max(pj)}")
    # 3 beruntun sama panjang (toleransi ±2 kata)
    run = 1
    for i in range(1, len(pj)):
        if abs(pj[i] - pj[i - 1]) <= 2:
            run += 1
            if run >= 3:
                print(f"  SERAGAM x{run} @{i}: {kalimat[i-2][:60]}... / {kalimat[i-1][:60]}... / {kalimat[i][:60]}...")
        else:
            run = 1
    # parataksis: >=3 kalimat <=8 kata beruntun
    run = 1
    for i in range(1, len(pj)):
        if pj[i] <= 8 and pj[i - 1] <= 8:
            run += 1
            if run >= 3:
                print(f"  PARATAKSIS x{run} @{i}: {kalimat[i-2][:50]} | {kalimat[i-1][:50]} | {kalimat[i][:50]}")
        else:
            run = 1
    # distribusi
    from collections import Counter
    c = Counter(pj)
    print(f"  Panjang paling sering: {c.most_common(5)}")
    pendek = sum(1 for x in pj if x <= 10)
    panjang = sum(1 for x in pj if x >= 28)
    print(f"  Kalimat <=10 kata: {pendek} ({100*pendek/len(pj):.0f}%); >=28 kata: {panjang} ({100*panjang/len(pj):.0f}%)")

    print("\n== RULE OF THREE (rangkaian 'X, Y, dan Z' retoris) ==")
    for m in re.finditer(r"(\w+(?:\s+\w+){0,3}),\s+(\w+(?:\s+\w+){0,3}),\s+dan\s+(\w+(?:\s+\w+){0,3})", tubuh):
        print(f"  ...{m.group(0)[:90]}...")

if __name__ == "__main__":
    main()
