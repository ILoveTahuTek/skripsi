#!/usr/bin/env python3
"""Ukur huruf efektif cetak tiap diagram: render SVG via mmdc, parse font-size & lebar.
Asumsi penyematan DOCX: lebar konten 14 cm = 396,85 pt; tinggi maks tampil 780 px (20,6 cm).
print_pt = font_px * 396.85 / svg_width_px  (sebelum pemangkasan tinggi)."""
import re, subprocess, sys, os

SRC = '/home/z/my-project/download/translator-sibi-draft/diagram'
FILES = ['G3.1-tahapan-gerbang.mmd', 'G3.2-alur-teacher-student.mmd',
         'G3.3-arsitektur-akhir.mmd', 'G3.4-topologi-jaringan.mmd',
         'G3.5-inferensi-tepi.mmd', 'G3.6-alur-dataset-evaluasi.mmd']

def svg_metrics(path):
    svg = open(path, encoding='utf-8').read()
    m = re.search(r'viewBox="([\d.]+)[ ,]([\d.]+)[ ,]([\d.]+)[ ,]([\d.]+)"', svg)
    x, y, w, h = map(float, m.groups())
    fonts = [float(v) for v in re.findall(r'font-size:\s*([\d.]+)px', svg)]
    fonts += [float(v) for v in re.findall(r'font-size="([\d.]+)"', svg)]
    return w, h, fonts

for f in FILES:
    src = os.path.join(SRC, f)
    out = f'/tmp/ukur-{f}.svg'
    r = subprocess.run(['mmdc', '-i', src, '-o', out, '-b', 'white', '-p',
                        '/home/z/my-project/scripts/translator-sibi-docx/diagram-docx/puppeteer-wide.json'],
                       capture_output=True, text=True, timeout=120)
    if r.returncode != 0:
        print(f'{f}: GAGAL render: {r.stderr[:200]}')
        continue
    w, h, fonts = svg_metrics(out)
    aspek = h / w
    minf = min(fonts) if fonts else 0
    # print pada 14 cm = 396.85 pt
    pt_full = minf * 396.85 / w
    # bila tinggi terpangkas ke 20,6 cm (780px@96dpi): lebar tampil menyusut
    h_cm_full = 14 * aspek
    if h_cm_full > 20.6:
        w_disp = 20.6 / aspek
        pt_disp = minf * (w_disp / 14) * 396.85 / w * (14 / 14)
        pt_disp = minf * 396.85 / w * (w_disp / 14)
        disp = f'-> terpangkas: lebar tampil {w_disp:.1f} cm, huruf {pt_disp:.1f} pt'
    else:
        disp = ''
    print(f'{f}: svg {w:.0f}x{h:.0f} aspek {aspek:.2f} (tinggi-cetak {h_cm_full:.1f} cm) '
          f'font min {minf:.0f}px -> {pt_full:.1f} pt {disp}')
