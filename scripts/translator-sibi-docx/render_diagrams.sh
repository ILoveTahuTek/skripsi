#!/bin/bash
# Render 6 diagram BAB III untuk DOCX.
# G3.3: render langsung dari .mmd sandbox (aspek sudah sehat, aspek 1.03).
# G3.1, G3.2, G3.4, G3.5, G3.6: render dari VARIAN TATA LETAK docx (diagram-docx/)
#   karena versi sandbox berupa rantai vertikal ekstrem (aspek 1:5-1:9) atau
#   baris horizontal ekstrem yang tidak terbaca pada halaman A4.
#   Varian memakai subgraf kolom/baris + sisi klaster atau pembalikan arah;
#   isi node/sisi/label 100% identik dengan sandbox.
# Viewport Puppeteer lebar diperlukan agar mmdc tidak memeras diagram ke ~800px logis.
set -e
SRC=/home/z/my-project/download/translator-sibi-draft/diagram
VARIAN=/home/z/my-project/scripts/translator-sibi-docx/diagram-docx
OUT=/home/z/my-project/download/translator-sibi-docx/assets
mkdir -p "$OUT"
cd "$VARIAN"

render_varian() { # $1=berkas.mmd $2=nomor $3=config(opsional)
  local f="$1" n="$2" cfg="${3:-}"
  if [ -n "$cfg" ]; then
    mmdc -i "$f" -o "$OUT/gambar-$n.png" -b white -s 3 -t neutral -p puppeteer-wide.json -c "$cfg" -q
  else
    mmdc -i "$f" -o "$OUT/gambar-$n.png" -b white -s 3 -t neutral -p puppeteer-wide.json -q
  fi
}

render_varian G3.1-tahapan-gerbang-3kolom.mmd        3.1 rapat.json
render_varian G3.2-alur-teacher-student.mmd          3.2
render_sandbox_g33() {
  mmdc -i "$SRC/G3.3-arsitektur-akhir.mmd" -o "$OUT/gambar-3.3.png" -b white -s 3 -t neutral -p puppeteer-wide.json -q
}
render_sandbox_g33
render_varian G3.4-topologi-jaringan.mmd            3.4
render_varian G3.5-inferensi-tepi.mmd               3.5
render_varian G3.6-alur-dataset-evaluasi-3kolom.mmd 3.6

echo "--- Hasil ---"
node -e "
const fs=require('fs');
for (const n of ['3.1','3.2','3.3','3.4','3.5','3.6']) {
  const b=fs.readFileSync('$OUT/gambar-'+n+'.png');
  const w=b.readUInt32BE(16), h=b.readUInt32BE(20);
  console.log('gambar-'+n+'.png: '+w+'x'+h+' aspek '+(h/w).toFixed(2));
}"
