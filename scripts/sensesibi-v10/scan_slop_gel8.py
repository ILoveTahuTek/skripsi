#!/usr/bin/env python3
"""Pemindai slop gelombang 8 — dimensi manual humanizer-id."""
import re
from collections import Counter

PATH = '/home/z/my-project/download/sensesibi-v10/Proposal-SenseSIBI-v10.md'
with open(PATH) as f:
    lines = f.read().split('\n')

print('=== C. SUBJEK PEMBUKA KALIMAT BERULANG ===')
starts = Counter()
subj_pat = re.compile(
    r'^(Penelitian ini|Purwarupa ini|Sistem ini|Pendekatan ini|Arsitektur ini|'
    r'Kajian ini|Bab ini|Subbab ini|Bagian ini|Tahap ini|Pengujian ini|'
    r'Data tersebut|Hasil tersebut|Penelitian tersebut|Sistem tersebut|Kombinasi ini|Model ini)\b')
for line in lines:
    for s in re.split(r'(?<=[.!?])\s+', line):
        m = subj_pat.match(s.strip())
        if m:
            starts[m.group(1)] += 1
for k, c in starts.most_common(20):
    print(f'{k}: {c}x')

print()
print('=== D. POLA FREKUENSI LEXIS ===')
pats = [
    (r' — ', 'em-dash tengah kalimat'),
    (r'\byaitu\b', 'yaitu'),
    (r'\byakni\b', 'yakni'),
    (r'\bdiharapkan\b', 'diharapkan'),
    (r'\bmemungkinkan\b', 'memungkinkan'),
    (r'\bmendorong\b', 'mendorong'),
    (r'\bsecara umum\b', 'secara umum'),
    (r'\bsecara keseluruhan\b', 'secara keseluruhan'),
    (r'\bkontribusi\b', 'kontribusi'),
    (r'\btantangan\b', 'tantangan'),
    (r'\bhal ini\b', 'hal ini'),
    (r'\bhal tersebut\b', 'hal tersebut'),
    (r'\bkondisi ini\b', 'kondisi ini'),
    (r'\bkondisi tersebut\b', 'kondisi tersebut'),
    (r'\bperlu\b', 'perlu'),
    (r'\bdapat\b', 'dapat'),
    (r'\bmampu\b', 'mampu'),
    (r'\bberpotensi\b', 'berpotensi'),
    (r'\bmenjawab\b', 'menjawab'),
    (r'\bmemenuhi\b', 'memenuhi'),
    (r'\bmenjadi tantangan\b', 'menjadi tantangan'),
    (r'\bmemberikan kontribusi\b', 'memberikan kontribusi'),
    (r'\bberperan penting\b', 'berperan penting'),
    (r'\bmemainkan peran\b', 'memainkan peran'),
    (r'\bmelakukan\b', 'melakukan (verba ringan)'),
    (r'\bmengalami\b', 'mengalami (verba ringan)'),
    (r'\bmemberikan\b', 'memberikan (verba ringan)'),
    (r'\bmelaksanakan\b', 'melaksanakan (verba ringan)'),
    (r'\bpenggunaan\b', 'penggunaan'),
    (r'\bpemanfaatan\b', 'pemanfaatan'),
    (r'\bpenerapan\b', 'penerapan'),
    (r'\bpengembangan\b', 'pengembangan'),
]
whole = '\n'.join(lines)
for pat, name in pats:
    n = len(re.findall(pat, whole, re.I))
    if n:
        print(f'{name}: {n}x')

print()
print('=== E. AWAL PARAGRAF (frekuensi 2+ kata pertama) ===')
cnt3 = Counter()
para_starts = []
for i, line in enumerate(lines, 1):
    if (line and not line.startswith(('#', '|', '>', '-', '[', '!', '`', '*', 'BAB', 'Tabel', 'Gambar', 'Dep', 'Stakeholder', 'G0', 'G1', 'G2', 'G3', 'G4', 'R', 'P', 'O', 'T', 'M', 'S', 'D'))
            and len(line) > 100):
        first = line.split()[0] if line.split() else ''
        cnt3[first] += 1
        para_starts.append((i, ' '.join(line.split()[:6])))
for k, c in cnt3.most_common(20):
    if c >= 2:
        print(f'{c:3d}x  {k}')

print()
print('=== F. "Adapun" & kandidat hapus (kaidah J.3) ===')
for i, line in enumerate(lines, 1):
    for m in re.finditer(r'(?:^|(?<=[.!?])\s+)Adapun', line):
        print(f'L{i}: ...{line[max(0,m.start()-30):m.start()+120]}...')

print()
print('=== G. "Dengan demikian/Meskipun demikian/Oleh karena itu" (ilusi kohesi?) ===')
for i, line in enumerate(lines, 1):
    for m in re.finditer(r'(?:^|(?<=[.!?])\s+)(Dengan demikian|Meskipun demikian|Oleh karena itu|Selain itu|Selanjutnya|Sementara itu|Di sisi lain)', line):
        print(f'L{i} [{m.group(1)}]: ...{line[m.start():m.start()+110]}...')
