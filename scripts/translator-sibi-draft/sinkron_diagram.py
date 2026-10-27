#!/usr/bin/env python3
# sinkron_diagram.py — Sinkronkan blok mermaid bab3 -> berkas .mmd + validasi mmdc
# Konvensi: berkas .mmd = 2 baris komentar %% (metadata) + isi blok mermaid naskah.
import re, subprocess, sys, os

BASE = '/home/z/my-project/download/translator-sibi-draft'
DIAG = os.path.join(BASE, 'diagram')
BAB3 = os.path.join(BASE, 'bab3-metodologi.md')

# Peta: urutan blok mermaid di bab3 -> berkas .mmd + header komentar
FILES = [
    ('G3.1-tahapan-gerbang.mmd',
     'G3.1 — Tahapan penelitian T0-T5 dengan gerbang keputusan G0-G4 (BAB III, Subbab 3.2)',
     'flowchart TD, tahapan T0-T5 dengan gerbang G0-G4; T2 memuat distilasi guru-murid'),
    ('G3.2-alur-teacher-student.mmd',
     'G3.2 — Alur pelatihan guru-murid YOLO26-Pose dan CSI hingga deployment (BAB III, Subbab 3.2.3)',
     'flowchart TD, metodologi utama: guru kamera -> penyandingan waktu -> murid CSI -> optimasi -> ESP32-S3'),
    ('G3.3-arsitektur-akhir.mmd',
     'G3.3 — Arsitektur produk akhir tanpa kamera (BAB III, Subbab 3.5.1)',
     'flowchart TD, dua jalur operasional (TTS/ASR awan) + jalur guru saat riset + cadangan lokal'),
    ('G3.4-topologi-jaringan.mmd',
     'G3.4 — Topologi perangkat, komunikasi antarmodul, layanan awan, dan server (BAB III, Subbab 3.5.2)',
     'flowchart LR, 2-3 modul + AP internet + layanan ucapan awan + server lokal riset/cadangan'),
    ('G3.5-inferensi-tepi.mmd',
     'G3.5 — Inferensi langsung pada ESP32-S3 (BAB III, Subbab 3.7.8)',
     'flowchart LR, penyangga geser -> segmentasi -> fitur -> murid int8 -> ambang penolakan'),
    ('G3.6-alur-dataset-evaluasi.mmd',
     'G3.6 — Alur dataset, pelatihan guru-murid, evaluasi, dan deployment (BAB III, Subbab 3.8)',
     'flowchart TD, perekaman -> saring -> guru -> murid + ablasi -> 5 skema -> deployment -> uji'),
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
