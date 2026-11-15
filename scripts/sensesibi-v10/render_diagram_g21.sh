#!/usr/bin/env bash
# Render diagram G3.3 yang berubah di v21 (simpul TX: penjana trafik OFDM + accDescr);
# lima diagram lain tidak berubah (salin dari assets-v20).
# Ambang huruf efektif cetak mengikuti nilai yang diterima v19/v20 (G3.3 6,4 pt).
set -e
V10=/home/z/my-project/download/sensesibi-v10
CFG=/home/z/my-project/scripts/sensesibi-v10/diagram/config-24.json
DW=/home/z/my-project/scripts/sensesibi-v10/diagram/puppeteer-wide.json
MD=$V10/Proposal-SenseSIBI-v21.md
DIR=$V10/diagram-g21
OUT=$V10/assets-v21
mkdir -p "$DIR" "$OUT"

# 1) ekstrak blok mermaid Gambar 3.3 dari naskah v21
python3 - "$MD" "$DIR" <<'EOF'
import re, sys
from pathlib import Path
md, out = Path(sys.argv[1]), Path(sys.argv[2])
s = md.read_text(encoding="utf-8")
blok = re.findall(r"```mermaid\n(.*?)\n```", s, re.S)
target = None
for b in blok:
    if "Arsitektur produk akhir tanpa kamera dengan cadangan TTS on-device" in b:
        target = b
assert target is not None, "blok G3.3 tidak ditemukan"
# pastikan simpul TX v21 memakai penjana trafik OFDM (bukan injeksi NDP)
assert 'TX["Node TX: penjana trafik OFDM"]' in target, "simpul TX belum berganti"
assert "injeksi NDP" not in target, "sisa injeksi NDP di G3.3"
assert "self-ping" in target, "accDescr belum memuat self-ping"
(out / "G3.3.mmd").write_text(target + "\n", encoding="utf-8")
print("G3.3 ->", len(target.split("\n")), "baris")
EOF

# 2) salin PNG tak berubah lalu render G3.3
for g in 2.1 2.2 3.1 3.2 3.4 3.5; do cp -f "$V10/assets-v20/gambar-${g}.png" "$OUT"/; done
mmdc -i "$DIR/G3.3.mmd" -o "$OUT/gambar-3.3.png" -b white -s 3 -t neutral -p "$DW" -c "$CFG" -q

# 3) periksa aspek + huruf efektif cetak (lebar cetak 14 cm, tinggi maks 20,6 cm)
python3 - <<'EOF'
import json, struct
CFG = "/home/z/my-project/scripts/sensesibi-v10/diagram/config-24.json"
OUT = "/home/z/my-project/download/sensesibi-v10/assets-v21"
cfg = json.load(open(CFG))
F_NODE = float(cfg['themeVariables']['fontSize'].replace('px',''))
path = f"{OUT}/gambar-3.3.png"
with open(path, 'rb') as f:
    data = f.read()
w, h = struct.unpack('>II', data[16:24])
# skala render mmdc -s 3 => piksel CSS = px/3
w_css, h_css = w/3.0, h/3.0
LEBAR_CETAK_CM = 14.0
faktor = LEBAR_CETAK_CM / (w_css/96.0*2.54)   # 96 dpi CSS
tinggi_cetak = h_css/96.0*2.54*faktor
font_pt = F_NODE * 0.75 * faktor   # px->pt (0.75) lalu faktor cetak
print(f"G3.3: {w}x{h}px | aspek {w/h:.2f} | tinggi cetak {tinggi_cetak:.1f} cm | font efektif {font_pt:.1f} pt")
assert tinggi_cetak <= 20.6, "tinggi cetak melebihi 20,6 cm"
assert font_pt >= 6.2, f"font efektif {font_pt:.1f} pt di bawah ambang 6,2 pt (nilai diterima v20: 6,4)"
print("G3.3 LOLOS ambang (font >= 6,2 pt; tinggi <= 20,6 cm)")
EOF
echo "assets-v21 siap."
