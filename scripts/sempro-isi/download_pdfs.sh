#!/usr/bin/env bash
# Unduh PDF sumber untuk verifikasi fakta perangkat/bahasa (penanda sempro DPJ-4).
set -u
D=/home/z/my-project/scripts/sempro-isi/pdfs
mkdir -p "$D"
UA="Mozilla/5.0 (X11; Linux x86_64; rv:120.0) Gecko/20100101 Firefox/120.0"

dl () { # dl <nama> <url>
  local out="$D/$1.pdf"
  if [ -s "$out" ]; then echo "[skip] $1"; return; fi
  curl -sL -A "$UA" --max-time 120 -o "$out" "$2"
  # verifikasi: bukan halaman HTML error
  if head -c 200 "$out" 2>/dev/null | grep -qi "<!doctype html\|<html"; then
    echo "[GAGAL-html] $1"; rm -f "$out"
  elif [ ! -s "$out" ]; then
    echo "[GAGAL-kosong] $1"; rm -f "$out"
  else
    echo "[ok] $1 ($(du -h "$out" | cut -f1))"
  fi
}

dl densepose_wifi "https://arxiv.org/pdf/2301.00250"
dl signfi_acm "https://dl.acm.org/doi/pdf/10.1145/3191755"
dl dfwislr_taylor "https://expert.taylors.edu.my/file/rems/publication/109291_8483_1.pdf"
dl shangwu_acm "https://dl.acm.org/doi/pdf/10.1145/3097620.3097624"
dl dwijayanti_ijacsa "https://thesai.org/Downloads/Volume12No10/Paper_46-Indonesia_Sign_Language_Recognition_using_Convolutional_Neural_Network.pdf"
ls -la "$D"
