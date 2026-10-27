#!/usr/bin/env python3
"""Ukur varian yang BENAR-BENAR tertanam di DOCX saat ini (sumber render_diagrams.sh)."""
import re, subprocess, os

D = '/home/z/my-project/scripts/translator-sibi-docx/diagram-docx'
DW = f'{D}/puppeteer-wide.json'
PAIRS = [  # (nomor, berkas sumber aktual, config)
    ('3.1', f'{D}/G3.1-tahapan-gerbang-3kolom.mmd', f'{D}/rapat.json'),
    ('3.2', f'{D}/G3.2-alur-teacher-student.mmd', None),
    ('3.3', '/home/z/my-project/download/translator-sibi-draft/diagram/G3.3-arsitektur-akhir.mmd', None),
    ('3.4', f'{D}/G3.4-topologi-jaringan.mmd', None),
    ('3.5', f'{D}/G3.5-inferensi-tepi.mmd', None),
    ('3.6', f'{D}/G3.6-alur-dataset-evaluasi-3kolom.mmd', None),
]

def metrics(path):
    svg = open(path, encoding='utf-8').read()
    m = re.search(r'viewBox="([\d.]+)[ ,]([\d.]+)[ ,]([\d.]+)[ ,]([\d.]+)"', svg)
    x, y, w, h = map(float, m.groups())
    fonts = [float(v) for v in re.findall(r'font-size:\s*([\d.]+)px', svg)]
    fonts += [float(v) for v in re.findall(r'font-size="([\d.]+)"', svg)]
    fonts = [f for f in fonts if 6 < f < 60]  # buang font-size sistem (0.024 dsb.)
    return w, h, fonts

for num, src, cfg in PAIRS:
    out = f'/tmp/ukur-var-{num}.svg'
    cmd = ['mmdc', '-i', src, '-o', out, '-b', 'white', '-p', DW]
    if cfg: cmd += ['-c', cfg]
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
    if r.returncode != 0:
        print(f'G{num}: GAGAL: {r.stderr[:150]}'); continue
    w, h, fonts = metrics(out)
    aspek = h / w
    minf, maxf = (min(fonts), max(fonts)) if fonts else (0, 0)
    pt_full = minf * 396.85 / w
    h_cm = 14 * aspek
    if h_cm > 20.6:
        wd = 20.6 / aspek
        pt = minf * 396.85 / w * (wd / 14)
        info = f'TERPANGKAS -> lebar tampil {wd:.1f} cm, huruf {pt:.1f} pt'
    else:
        info = f'muat (tinggi {h_cm:.1f} cm)'
    print(f'Gambar {num}: svg {w:.0f}x{h:.0f} aspek {aspek:.2f} | font {minf:.0f}-{maxf:.0f}px | '
          f'pada 14cm: {pt_full:.1f} pt | {info}')
