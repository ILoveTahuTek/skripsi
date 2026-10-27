#!/usr/bin/env python3
# sinkron_diagram.py — Sinkronkan blok mermaid bab3 -> berkas .mmd + validasi mmdc
# Konvensi: berkas .mmd = 2 baris komentar %% (metadata) + isi blok mermaid naskah.
import re, subprocess, sys, os

BASE = '/home/z/my-project/download/translator-sibi-draft'
DIAG = os.path.join(BASE, 'diagram')
BAB3 = os.path.join(BASE, 'bab3-metodologi.md')

# Peta: urutan blok mermaid di bab3 -> berkas .mmd + header komentar
FILES = [
    ('G3.1-tahapan-utama.mmd',
     'G3.1 — Tahapan penelitian T0-T5 dan gerbang keputusan G0-G4, jalur utama (BAB III, Subbab 3.2)',
     'flowchart LR parent + dua kolom TB (ular); sisi klaster KA--lolos-->KB mewakili G2-->T2B; pasangan: G3.2-remediasi-gerbang'),
    ('G3.2-remediasi-gerbang.mmd',
     'G3.2 — Jalur gagal dan remediasi gerbang keputusan G0-G4 (BAB III, Subbab 3.2)',
     'flowchart TB lima baris (subgraf LR; sisi taklihat antarbaris hanya penata); lingkaran = keluaran baris; rincian S0/S1 dan kriteria gerbang di caption'),
    ('G3.3-distilasi-data-guru.mmd',
     'G3.3 — Distilasi guru-murid tahap data: perekaman, penyaringan, guru, penyandingan (BAB III, Subbab 3.2.3)',
     'flowchart LR parent + dua kolom TB; sisi klaster ya / video+CSI / belum; keluaran DQ-ya menuju Gambar 3.4; node FLT berasal dari G3.6 lama'),
    ('G3.4-distilasi-murid-deployment.mmd',
     'G3.4 — Distilasi guru-murid tahap pelatihan: dataset murid, pembanding, deployment (BAB III, Subbab 3.2.3)',
     'flowchart TD percabangan alami; loop EQ--belum(Tabel 3.4)-->SD; sisi klaster KA--ya-->KB mewakili EQ-->OPT'),
    ('G3.5-arsitektur-akhir.mmd',
     'G3.5 — Arsitektur produk akhir tanpa kamera (BAB III, Subbab 3.5.1)',
     'flowchart TD tiga rantai sejajar (arah 1, arah 2, jalur guru) + server lokal; kotak kelompok dihapus demi keterbacaan, pengelompokan di caption'),
    ('G3.6-topologi-jaringan.mmd',
     'G3.6 — Topologi perangkat, komunikasi antarmodul, layanan awan, dan server (BAB III, Subbab 3.5.2)',
     'flowchart TB; sisi taklihat AWAN~~~SERVER hanya penata'),
    ('G3.7-inferensi-tepi.mmd',
     'G3.7 — Inferensi langsung pada ESP32-S3 (BAB III, Subbab 3.7.8)',
     'flowchart LR parent + dua kolom TB; sisi klaster R1-->R2 mewakili FT-->MOD; batas perangkat pindah ke prosa/BAB II'),
    ('G3.8-alur-evaluasi.mmd',
     'G3.8 — Alur evaluasi: pembagian data, metrik, uji operasional, uji kegunaan, artefak (BAB III, Subbab 3.8)',
     'flowchart TD percabangan alami; rantai perekaman-pelatihan dirujuk ke Gambar 3.3-3.4; seluruh sisi evaluasi sumber dipertahankan'),
]

with open(BAB3, encoding='utf-8') as f:
    text = f.read()

blocks = re.findall(r'```mermaid\n(.*?)```', text, re.S)
if len(blocks) != len(FILES):
    print(f'GAGAL: {len(blocks)} blok mermaid di bab3, diharapkan {len(FILES)}')
    sys.exit(1)

for (fname, h1, h2), block in zip(FILES, blocks):
    content = f'%% {h1}\n%% Tipe: {h2}\n' + block.rstrip() + '\n'
    path = os.path.join(DIAG, fname)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'tulis {fname} ({len(block.splitlines())} baris isi)')

# Validasi mmdc setiap berkas
ok = True
for fname, _, _ in FILES:
    path = os.path.join(DIAG, fname)
    out = f'/tmp/mmdc-check-{fname}.svg'
    r = subprocess.run(['mmdc', '-i', path, '-o', out, '-b', 'white'],
                       capture_output=True, text=True, timeout=120)
    if r.returncode == 0:
        size = os.path.getsize(out)
        print(f'  mmdc OK: {fname} -> {size} bita')
    else:
        ok = False
        print(f'  mmdc GAGAL: {fname}\n{r.stderr[:800]}')

# Sinkronisasi verifikasi: isi blok naskah == isi .mmd tanpa 2 baris %%
sync_ok = True
for (fname, _, _), block in zip(FILES, blocks):
    with open(os.path.join(DIAG, fname), encoding='utf-8') as f:
        mmd = f.read()
    body = '\n'.join(mmd.splitlines()[2:]).strip()
    if body != block.strip():
        sync_ok = False
        print(f'SINKRON GAGAL: {fname}')
if sync_ok:
    print(f'Sinkronisasi naskah <-> berkas .mmd: {len(FILES)}/{len(FILES)} identik')

print('HASIL:', 'LOLOS' if (ok and sync_ok) else 'GAGAL')
sys.exit(0 if (ok and sync_ok) else 1)
