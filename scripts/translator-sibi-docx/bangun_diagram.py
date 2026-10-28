#!/usr/bin/env python3
"""Bangun 8 diagram baru + ukur huruf efektif cetak (metrik bersih dari konfigurasi).
Huruf: simpul = fontSize (24px), label sisi = 24px (themeCSS), judul subgraf = 18px.
Target: semua >= 9 pt pada sematan 14 cm; aspek <= 1,45 (tidak terpangkas 20,6 cm)."""
import re, subprocess, os, struct, sys, json

SRC = '/home/z/my-project/download/translator-sibi-draft/diagram'
VAR = '/home/z/my-project/scripts/translator-sibi-docx/diagram-docx'
OUT = '/home/z/my-project/download/translator-sibi-docx/assets'
CFG = f'{VAR}/config-24.json'
DW = f'{VAR}/puppeteer-wide.json'
FIGS = [
    ('3.1', 'G3.1-tahapan-utama.mmd'),
    ('3.2', 'G3.2-remediasi-gerbang.mmd'),
    ('3.3', 'G3.3-distilasi-data-guru.mmd'),
    ('3.4', 'G3.4-distilasi-murid-deployment.mmd'),
    ('3.5', 'G3.5-arsitektur-akhir.mmd'),
    ('3.6', 'G3.6-topologi-jaringan.mmd'),
    ('3.7', 'G3.7-inferensi-tepi.mmd'),
    ('3.8', 'G3.8-alur-evaluasi.mmd'),
]
cfg = json.load(open(CFG))
F_NODE = float(cfg['themeVariables']['fontSize'].replace('px', ''))
m = re.search(r'edgeLabel \{ font-size: (\d+)px', cfg.get('themeCSS', ''))
F_EDGE = float(m.group(1)) if m else F_NODE
F_TITLE = 18.0  # flowchartTitleText bawaan mermaid

ok_all = True
print(f'{"fig":5} {"kanvas logis":14} {"aspek":6} {"simpul":7} {"sisi":6} {"judul":6} status')
for num, f in FIGS:
    src = os.path.join(SRC, f)
    svg = f'/tmp/bangun-{num}.svg'
    png = os.path.join(OUT, f'gambar-{num}.png')
    r = subprocess.run(['mmdc', '-i', src, '-o', png, '-b', 'white', '-s', '3',
                        '-t', 'neutral', '-p', DW, '-c', CFG, '-q'],
                       capture_output=True, text=True, timeout=180)
    if r.returncode != 0:
        print(f'gambar-{num}: RENDER GAGAL: {r.stderr[:300]}')
        ok_all = False
        continue
    subprocess.run(['mmdc', '-i', src, '-o', svg, '-b', 'white',
                    '-p', DW, '-c', CFG, '-q'], capture_output=True, text=True, timeout=180)
    s = open(svg, encoding='utf-8').read()
    mv = re.search(r'viewBox="([\d.]+)[ ,]([\d.]+)[ ,]([\d.]+)[ ,]([\d.]+)"', s)
    x, y, w, h = map(float, mv.groups())
    aspek = h / w
    n_edge = len(re.findall(r'class="edgeLabel"', s))
    n_title = len(re.findall(r'class=\"flowchartTitleText\"', s))
    pt_node = F_NODE * 396.85 / w
    pt_edge = F_EDGE * 396.85 / w if n_edge else None
    pt_title = F_TITLE * 396.85 / w if n_title else None
    h_cm = 14 * aspek
    if h_cm > 20.6:
        wd = 20.6 / aspek
        pt_node *= wd / 14; pt_edge = pt_edge * wd / 14 if pt_edge else None
        status = f'TERPANGKAS lebar {wd:.1f} cm'
        ok_all = False
    else:
        kand = [pt_node] + ([pt_edge] if pt_edge else []) + ([pt_title] if pt_title else [])
        mnn = min(kand)
        status = 'OK' if mnn >= 9.0 else f'FONT KURANG (min {mnn:.1f} pt)'
        if mnn < 9.0: ok_all = False
    b = open(png, 'rb').read()
    pw, ph = struct.unpack('>II', b[16:24])
    e = f'{pt_edge:.1f}' if pt_edge else '-'
    t = f'{pt_title:.1f}' if pt_title else '-'
    print(f'{num:5} {f"{w:.0f}x{h:.0f}":14} {aspek:6.2f} {pt_node:7.1f} {e:6} {t:6} {status}  PNG {pw}x{ph}')
print('HASIL:', 'LOLOS' if ok_all else 'PERLU ITERASI')
sys.exit(0 if ok_all else 1)
