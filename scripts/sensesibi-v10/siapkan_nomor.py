#!/usr/bin/env python3
"""Siapkan naskah v10: geser penomoran tabel/gambar BAB III (tubuh naskah saja,
log di bawah penanda AKHIR NASKAH tidak disentuh), lalu audit integritas sitasi.

Pergeseran (sebelum penyisipan konten baru):
  Tabel 3.8->3.9, 3.7->3.8, 3.6->3.7, 3.5->3.6, 3.4->3.5  (urutan terbalik)
  Gambar 3.8->3.10, 3.7->3.9                              (urutan terbalik)
Catatan penyusunan (baris awal) diperbarui manual terpisah.
"""
import re, sys

P = "/home/z/my-project/download/sensesibi-v10/Proposal-SenseSIBI-v10.md"
teks = open(P, encoding="utf-8").read()

MARK = "<!-- ===== AKHIR NASKAH"
idx = teks.index(MARK)
head, tail = teks[:idx], teks[idx:]

# --- Geser tabel (terbalik) ---
for old, new in [("Tabel 3.8", "Tabel 3.9"), ("Tabel 3.7", "Tabel 3.8"),
                 ("Tabel 3.6", "Tabel 3.7"), ("Tabel 3.5", "Tabel 3.6"),
                 ("Tabel 3.4", "Tabel 3.5")]:
    head = head.replace(old, new)

# --- Geser gambar (terbalik) ---
for old, new in [("Gambar 3.8", "Gambar 3.10"), ("Gambar 3.7", "Gambar 3.9")]:
    head = head.replace(old, new)

open(P, "w", encoding="utf-8").write(head + tail)
print("Penomoran digeser. Tubuh:", len(head), "karakter; log:", len(tail), "karakter.")

# --- Audit sitasi tubuh naskah ---
head2 = head.split("# DAFTAR PUSTAKA")[0]
cites = re.findall(r"\[(\d{1,2})\]", head2)
seen, order = set(), []
for c in cites:
    n = int(c)
    if n not in seen:
        seen.add(n); order.append(n)
print("Jumlah rujukan unik dikutip:", len(order))
missing = [n for n in range(1, 84) if n not in seen]
print("Rujukan [1..83] tidak dikutip di tubuh:", missing if missing else "tidak ada — semua terpakai")
firsts = order[:12]
print("12 kemunculan pertama:", firsts)
naik = all(order[i] < order[i + 1] for i in range(len(order) - 1))
print("Urutan kemunculan pertama monoton naik:", naik)
if not naik:
    # tampilkan pelanggaran urutan (angka muncul lebih awal dari seharusnya)
    pos = {n: i for i, n in enumerate(order)}
    bad = [(order[i], order[i + 1]) for i in range(len(order) - 1) if order[i] > order[i + 1]]
    print("Pasangan melanggar urutan (awal, sesudah):", bad[:10])
