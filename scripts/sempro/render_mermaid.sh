#!/bin/bash
# Render both mermaid diagrams to print-friendly PNG (white bg, adequate scale)
set -e
cd /home/z/my-project/scripts/sempro
OUT=/home/z/my-project/download/sempro-dpj4-sibi-csi/assets
mkdir -p "$OUT"

for n in 1 2; do
  mmdc -i "gambar-3.${n}.mmd" \
    -o "$OUT/gambar-3.${n}.png" \
    -b white \
    -s 2.5 \
    -t neutral \
    -q 2>&1 | grep -v "^$" || true
done
ls -la "$OUT"
