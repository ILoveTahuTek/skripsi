#!/usr/bin/env bash
# Render 10 diagram BAB III v10 + ukur huruf efektif cetak (adaptasi bangun_diagram.py).
set -e
SRC=/home/z/my-project/download/sensesibi-v10/diagram
OUT=/home/z/my-project/download/sensesibi-v10/assets
CFG=/home/z/my-project/scripts/sensesibi-v10/diagram/config-24.json
DW=/home/z/my-project/scripts/sensesibi-v10/diagram/puppeteer-wide.json
mkdir -p "$OUT"

for num in 3.1 3.2 3.3 3.4 3.5 3.6 3.7 3.8 3.9 3.10; do
  mmdc -i "$SRC/G${num}.mmd" -o "$OUT/gambar-${num}.png" -b white -s 3 -t neutral -p "$DW" -c "$CFG" -q
done

python3 - <<'EOF'
import re, os, json, struct
CFG = "/home/z/my-project/scripts/sensesibi-v10/diagram/config-24.json"
OUT = "/home/z/my-project/download/sensesibi-v10/assets"
cfg = json.load(open(CFG))
F_NODE = float(cfg['themeVariables']['fontSize'].replace('px',''))
m = re.search(r'edgeLabel \{ font-size: (\d+)px', cfg.get('themeCSS',''))
F_EDGE = float(m.group(1)) if m else F_NODE
F_TITLE = 18.0
ok = True
print(f'{"fig":6} {"kanvas":14} {"aspek":6} {"simpul":7} {"sisi":6} status')
for i in list(range(1,9)) + [9,10]:
    num = f'3.{i}' if i < 10 else f'3.{i}'
    num = f'3.{i}'
    png = os.path.join(OUT, f'gambar-{num}.png')
    svg = f'/tmp/render-v10-{num}.svg'
    os.system(f'mmdc -i "/home/z/my-project/download/sensesibi-v10/diagram/G{num}.mmd" -o "{svg}" -b white -p "/home/z/my-project/scripts/sensesibi-v10/diagram/puppeteer-wide.json" -c "{CFG}" -q >/dev/null 2>&1')
    s = open(svg, encoding='utf-8').read()
    mv = re.search(r'viewBox="([\d.]+)[ ,]([\d.]+)[ ,]([\d.]+)[ ,]([\d.]+)"', s)
    x,y,w,h = map(float, mv.groups())
    aspek = h/w
    n_edge = len(re.findall(r'class="edgeLabel"', s))
    pt_node = F_NODE*396.85/w
    pt_edge = F_EDGE*396.85/w if n_edge else None
    h_cm = 14*aspek
    if h_cm > 20.6:
        wd = 20.6/aspek
        pt_node *= wd/14; pt_edge = pt_edge*wd/14 if pt_edge else None
        status = f'TERPANGKAS lebar {wd:.1f} cm'; ok = False
    else:
        kand = [pt_node] + ([pt_edge] if pt_edge else [])
        mn = min(kand)
        status = 'OK' if mn >= 9.0 else f'FONT KURANG (min {mn:.1f} pt)'
        if mn < 9.0: ok = False
    b = open(png,'rb').read()
    pw, ph = struct.unpack('>II', b[16:24])
    e = f'{pt_edge:.1f}' if pt_edge else '-'
    print(f'{num:6} {f"{w:.0f}x{h:.0f}":14} {aspek:6.2f} {pt_node:7.1f} {e:6} {status}  PNG {pw}x{ph}')
print('HASIL:', 'LOLOS' if ok else 'PERLU ITERASI')
EOF
