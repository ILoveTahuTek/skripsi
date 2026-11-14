#!/usr/bin/env bash
# Render 3 diagram yang berubah di v19 (G3.1 accDescr, G3.3 simpul TX + accDescr,
# G3.5 accDescr) dari naskah v19; G2.2 dan foto 3.2 tidak berubah (salin dari v18).
# Pemeriksaan aspek + huruf efektif cetak dengan ambang per gambar mengikuti
# nilai v18 yang diterima (G3.1 8,0 pt; G3.3 6,4 pt; G3.5 9,0 pt).
set -e
V10=/home/z/my-project/download/sensesibi-v10
CFG=/home/z/my-project/scripts/sensesibi-v10/diagram/config-24.json
DW=/home/z/my-project/scripts/sensesibi-v10/diagram/puppeteer-wide.json
MD=$V10/Proposal-SenseSIBI-v19.md
DIR=$V10/diagram-g19
OUT=$V10/assets-v19
mkdir -p "$DIR" "$OUT"

# 1) ekstrak blok mermaid untuk Gambar 3.1, 3.3, 3.5 dari naskah v19
python3 - "$MD" "$DIR" <<'EOF'
import re, sys
from pathlib import Path
md, out = Path(sys.argv[1]), Path(sys.argv[2])
s = md.read_text(encoding="utf-8")
blok = re.findall(r"```mermaid\n(.*?)\n```", s, re.S)
target = {}
for b in blok:
    if "Tahapan penelitian T0 sampai T5 dengan gerbang G0 sampai G4 dan sub-gerbang G0b" in b: target["G3.1"] = b
    elif "Arsitektur produk akhir tanpa kamera dengan cadangan TTS on-device" in b: target["G3.3"] = b
    elif "Alur inferensi langsung pada ESP32-S3 menurut deployment Pilihan 1" in b: target["G3.5"] = b
    elif "Graf pelatihan dua kepala dan graf deployment" in b: target["G2.2"] = b
assert set(target) == {"G2.2", "G3.1", "G3.3", "G3.5"}, set(target)
# pastikan simpul TX v19 memakai injeksi NDP (bukan beacon ESP-NOW)
assert 'TX["Node TX: injeksi NDP"]' in target["G3.3"], "simpul TX belum berganti"
assert "beacon" not in target["G3.3"].lower(), "sisa beacon di G3.3"
for nama, isi in target.items():
    (out / f"{nama}.mmd").write_text(isi + "\n", encoding="utf-8")
    print(nama, "->", len(isi.split("\n")), "baris")
EOF

# 2) salin PNG tak berubah (2.1 Fresnel, 2.2, 3.2 foto, 3.4) lalu render 3 diagram
for g in 2.1 2.2 3.2 3.4; do cp -f "$V10/assets-v18/gambar-${g}.png" "$OUT"/; done
for num in 3.1 3.3 3.5; do
  mmdc -i "$DIR/G${num}.mmd" -o "$OUT/gambar-${num}.png" -b white -s 3 -t neutral -p "$DW" -c "$CFG" -q
done

# 3) periksa aspek + huruf efektif cetak (lebar cetak 14 cm, tinggi maks 20,6 cm)
python3 - <<'EOF'
import re, os, json, struct
CFG = "/home/z/my-project/scripts/sensesibi-v10/diagram/config-24.json"
DW = "/home/z/my-project/scripts/sensesibi-v10/diagram/puppeteer-wide.json"
OUT = "/home/z/my-project/download/sensesibi-v10/assets-v19"
cfg = json.load(open(CFG))
F_NODE = float(cfg['themeVariables']['fontSize'].replace('px',''))
m = re.search(r'edgeLabel \{ font-size: (\d+)px', cfg.get('themeCSS',''))
F_EDGE = float(m.group(1)) if m else F_NODE
AMBANG = {"3.1": 8.0, "3.3": 6.4, "3.5": 9.0}  # nilai v18 yang diterima
ok = True
print(f'{"fig":6} {"kanvas":14} {"aspek":6} {"simpul":7} {"sisi":6} status')
for num in ["3.1", "3.3", "3.5"]:
    svg = f'/tmp/render-g19-{num}.svg'
    os.system(f'mmdc -i "/home/z/my-project/download/sensesibi-v10/diagram-g19/G{num}.mmd" -o "{svg}" -b white -p "{DW}" -c "{CFG}" -q >/dev/null 2>&1')
    s = open(svg, encoding='utf-8').read()
    mv = re.search(r'viewBox="([\d.]+)[ ,]([\d.]+)[ ,]([\d.]+)[ ,]([\d.]+)"', s)
    x, y, w, h = map(float, mv.groups())
    aspek = h / w
    n_edge = len(re.findall(r'class="edgeLabel"', s))
    pt_node = F_NODE * 396.85 / w
    pt_edge = F_EDGE * 396.85 / w if n_edge else None
    h_cm = 14 * aspek
    if h_cm > 20.6:
        wd = 20.6 / aspek
        pt_node *= wd / 14
        pt_edge = pt_edge * wd / 14 if pt_edge else None
        status = f'TERPANGKAS lebar {wd:.1f} cm'
    else:
        kand = [pt_node] + ([pt_edge] if pt_edge else [])
        mn = min(kand)
        status = 'OK' if mn >= AMBANG[num] - 0.05 else f'FONT KURANG (min {mn:.1f} pt < {AMBANG[num]:.1f})'
        if mn < AMBANG[num] - 0.05: ok = False
    b = open(os.path.join(OUT, f'gambar-{num}.png'), 'rb').read()
    pw, ph = struct.unpack('>II', b[16:24])
    e = f'{pt_edge:.1f}' if pt_edge else '-'
    print(f'{num:6} {f"{w:.0f}x{h:.0f}":14} {aspek:6.2f} {pt_node:7.1f} {e:6} {status}  PNG {pw}x{ph}')
print('HASIL:', 'LOLOS' if ok else 'PERLU ITERASI')
EOF
