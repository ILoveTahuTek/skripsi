#!/usr/bin/env python3
"""Analisis audit gelombang 9: klasifikasi temuan badan naskah vs zona log."""
import re, sys

MD = "/home/z/my-project/download/sensesibi-v10/Proposal-SenseSIBI-v10.md"
AUDIT = "/home/z/my-project/scripts/sensesibi-v10/audit_humanizer_gel9.txt"

with open(MD, encoding="utf-8") as f:
    md_lines = f.readlines()

# cari batas zona log (gelombang 6 ke atas)
log_start = None
for i, ln in enumerate(md_lines, 1):
    if ln.startswith("Catatan kejujuran gelombang 6"):
        log_start = i
        break

with open(AUDIT, encoding="utf-8") as f:
    blocks = f.read().split("-" * 72)

body, log_zone = [], []
for b in blocks:
    m = re.search(r"Baris (\d+) \[([A-Z]+-\d+|[A-Z]{3}-\d+) - ([^\]]+)\]", b)
    if not m:
        continue
    line_no, rule, cat = int(m.group(1)), m.group(2), m.group(3).strip()
    # ambil kutipan teks
    q = re.search(r"Kutipan teks\s+:\s+(.*)", b)
    quote = q.group(1).strip() if q else ""
    rec = (line_no, rule, cat, quote)
    (log_zone if log_start and line_no >= log_start else body).append(rec)

print(f"BATAS LOG = baris {log_start}")
print(f"TEMUAN BADAN NASKAH = {len(body)} | ZONA LOG/KUTIPAN = {len(log_zone)}")
print()
from collections import Counter
cnt = Counter(r for _, r, _, _ in body)
print("=== Badan naskah per kaidah ===")
for rule, n in cnt.most_common():
    print(f"  {rule}: {n}")
print()
print("=== Daftar temuan badan naskah (baris | kaidah | kutipan 90k) ===")
for line_no, rule, cat, quote in sorted(body):
    print(f"  L{line_no} [{rule}] {quote[:90]}")
