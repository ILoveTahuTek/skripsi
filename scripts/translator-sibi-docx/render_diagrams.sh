#!/bin/bash
# Render 8 diagram BAB III — sumber tunggal dari translator-sibi-draft/diagram/ (varian docx tidak
# dipakai lagi sejak redesain 27 Okt 2026; sumber lama diarsip di diagram/lama-20261026/).
# Kunci keterbacaan: config-24.json (fontSize 24px, wrappingWidth 700 — mermaid 12 "neo" membungkus
# label di 120px jika tidak disetel), skala 3x, viewport puppeteer lebar.
# Ukur ulang huruf efektif: python3 bangun_diagram.py  (target >= 9 pt pada sematan 14 cm)
set -e
SRC=/home/z/my-project/download/translator-sibi-draft/diagram
OUT=/home/z/my-project/download/translator-sibi-docx/assets
CFG=/home/z/my-project/scripts/translator-sibi-docx/diagram-docx/config-24.json
DW=/home/z/my-project/scripts/translator-sibi-docx/diagram-docx/puppeteer-wide.json
mkdir -p "$OUT"
cd "$SRC"
render() { mmdc -i "$1" -o "$OUT/gambar-$2.png" -b white -s 3 -t neutral -p "$DW" -c "$CFG" -q; }
render G3.1-tahapan-utama.mmd            3.1
render G3.2-remediasi-gerbang.mmd        3.2
render G3.3-distilasi-data-guru.mmd      3.3
render G3.4-distilasi-murid-deployment.mmd 3.4
render G3.5-arsitektur-akhir.mmd         3.5
render G3.6-topologi-jaringan.mmd        3.6
render G3.7-inferensi-tepi.mmd           3.7
render G3.8-alur-evaluasi.mmd            3.8
echo "--- Hasil ---"
node -e "
const fs=require('fs');
for (let i=1;i<=8;i++) {
  const n='3.'+i;
  const b=fs.readFileSync('$OUT/gambar-'+n+'.png');
  const w=b.readUInt32BE(16), h=b.readUInt32BE(20);
  console.log('gambar-'+n+'.png: '+w+'x'+h+' aspek '+(h/w).toFixed(2));
}"
