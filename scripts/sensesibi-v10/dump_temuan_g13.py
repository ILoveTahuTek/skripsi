#!/usr/bin/env python3
"""Dump triplet, pendek lepas, dan kalimat terpanjang menurut logika metrik.py."""
import re
import sys
import importlib.util

spec = importlib.util.spec_from_file_location(
    "metrik", "/tmp/humanizer-indonesia/scripts/metrik.py")
metrik = importlib.util.module_from_spec(spec)
spec.loader.exec_module(metrik)

src = open(sys.argv[1], encoding="utf-8").read()
body = metrik.ambil_prosa(src)
kal = metrik.pecah_kalimat(body)

print("== TRIPLET ==")
for t in metrik.cari_triplet(kal):
    print(" *", t[:110])

print("\n== PENDEK LEPAS ==")
for p in metrik.pendek_lepas(src):
    print(" *", p)

print("\n== 22 KALIMAT TERPANJANG ==")
for k in sorted(kal, key=lambda s: -len(s.split()))[:22]:
    print(f" [{len(k.split())}] {k[:120]}")
