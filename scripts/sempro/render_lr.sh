#!/bin/bash
set -e
cd /home/z/my-project/scripts/sempro
OUT=/home/z/my-project/download/sempro-dpj4-sibi-csi/assets
for n in 1 2; do
  mmdc -i "gambar-3.${n}.lr.mmd" -o "$OUT/gambar-3.${n}.png" -b white -s 2.5 -t neutral -q 2>&1 || true
done
