#!/usr/bin/env python3
"""Pemindai ritme kalimat KRF-003 untuk gelombang 9.
Mengukur variasi panjang kalimat per subbab badan naskah + kepadatan deiksis sisa."""
import re, statistics

MD = "/home/z/my-project/download/sensesibi-v10/Proposal-SenseSIBI-v10.md"
BODY_END = 1263  # sebelum Daftar Pustaka & log

with open(MD, encoding="utf-8") as f:
    lines = f.readlines()[:BODY_END]

# Pecah per subbab; buang baris non-prosa (tabel |, mermaid, heading, kosong, kode)
subchaps, cur_title, cur_buf = [], None, []
in_mermaid = False
for ln in lines:
    s = ln.strip()
    if s.startswith("```"):
        in_mermaid = not in_mermaid
        continue
    if in_mermaid:
        continue
    m = re.match(r"^(#{2,4})\s+(.*)", s)
    if m:
        if cur_title and cur_buf:
            subchaps.append((cur_title, "\n".join(cur_buf)))
        cur_title, cur_buf = m.group(2), []
        continue
    if not s or s.startswith("|") or s.startswith("**Tabel") or s.startswith("["):
        continue
    cur_buf.append(s)
if cur_title and cur_buf:
    subchaps.append((cur_title, "\n".join(cur_buf)))

def sentences(text):
    # pisah kasar kalimat; abaikan singkatan umum via sikon sederhana
    text = re.sub(r"\[\d+(?:,\s*\d+)*\]", "@", text)  # sitasi -> token tanpa titik
    text = re.sub(r"(?<=\w)(?:dkk\.|vs\.|hlm\.|no\.|vol\.)", lambda m: m.group(0).replace(".", "`"), text)
    parts = re.split(r"(?<=[.!?;])\s+", text)
    return [p.strip() for p in parts if len(p.split()) >= 3]

report = []
for title, text in subchaps:
    sents = sentences(text)
    lens = [len(s.split()) for s in sents]
    if len(lens) < 6:
        continue
    mean = statistics.mean(lens)
    sd = statistics.pstdev(lens)
    cv = sd / mean if mean else 0
    # rentetan panjang serupa: berapa kalimat berturut-turut berada pita ±5 kata
    run = best = 1
    for i in range(1, len(lens)):
        run = run + 1 if abs(lens[i] - lens[i - 1]) <= 5 else 1
        best = max(best, run)
    n_ter = text.count("tersebut")
    n_yak = text.count("yaitu")
    n_seh = text.count("sehingga")
    report.append((round(cv, 2), best, mean, title, len(lens), n_ter, n_yak, n_seh))

print("=== KRF-003: CV rendah = ritme monoton; RUN = rentetan terpanjang Δ≤5 kata ===")
print(f"{'CV':>5} {'RUN':>4} {'Rata2':>6}  {'Subbab':58} {'NK':>3} {'tersebut':>9} {'yaitu':>6} {'sehingga':>9}")
for cv, best, mean, title, n, t, y, s in sorted(report):
    flag = " <==" if (cv < 0.40 or best >= 5) else ""
    print(f"{cv:5.2f} {best:4d} {mean:6.1f}  {title[:58]:58} {n:3d} {t:9d} {y:6d} {s:9d}{flag}")
