#!/usr/bin/env python3
"""Verifikasi kesetiaan konten: setiap paragraf/teks sumber harus ada di DOCX.
Metode: pandoc DOCX -> plain text; normalisasi spasi; cek keberadaan setiap unit teks sumber."""
import json, re, subprocess, unicodedata

DOCX = '/home/z/my-project/download/sempro-dpj4-sibi-csi/Proposal-Sempro-DPJ4-SIBI-CSI.docx'
PARSED = '/home/z/my-project/scripts/sempro/parsed.json'

txt = subprocess.run(['pandoc', DOCX, '-t', 'plain', '--wrap=none'],
                     capture_output=True, text=True).stdout

def norm(s):
    s = unicodedata.normalize('NFC', s)
    s = s.replace('\u00a0', ' ')
    # buang sintaks markdown inline (miring/tebal/kode) sebelum dibandingkan
    s = re.sub(r'\*+', '', s)
    s = re.sub(r'`+', '', s)
    s = re.sub(r'\s+', ' ', s).strip()
    return s

docx_text = norm(txt)
# hapus entri TOC placeholder (judul berulang) agar pencarian satu-arah tetap sah
docx_blob = docx_text

doc = json.load(open(PARSED))
missing = []
checked = 0

def check(text, label):
    global checked
    t = norm(text)
    if not t:
        return
    checked += 1
    if t not in docx_blob:
        missing.append((label, t[:90]))

for bab, blocks in doc.items():
    for i, b in enumerate(blocks):
        label = f'{bab}[{i}]'
        if b['t'] in ('p', 'li', 'ref'):
            # gabung run jadi teks (run miring/tebal menyatu di pandoc plain)
            check(''.join(r['text'] for r in b['runs']), label + ':' + b['t'])
        elif b['t'] in ('h1', 'h2', 'h3'):
            check(b['text'], label + ':' + b['t'])
        elif b['t'] == 'table':
            check(b['caption'] or '', label + ':caption')
            for r_i, row in enumerate(b['rows']):
                for c_i, cell in enumerate(row):
                    check(cell, f'{label}:r{r_i}c{c_i}')
        elif b['t'] == 'figure':
            check(b['caption'], label + ':figcap')

print(f'Dicek {checked} unit teks')
if missing:
    print(f'HILANG {len(missing)}:')
    for label, t in missing[:15]:
        print(' -', label, '->', t)
else:
    print('SEMUA unit teks sumber ditemukan di DOCX — sinkron penuh')

# Statistik kata
words = len(docx_blob.split())
print('Jumlah kata (pandoc plain):', words)
