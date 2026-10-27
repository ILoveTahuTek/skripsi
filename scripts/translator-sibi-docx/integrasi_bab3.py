#!/usr/bin/env python3
"""Integrasikan 8 diagram baru ke bab3-metodologi.md:
- ganti 6 blok mermaid lama -> isi baru (3.1, 3.3, 3.5, 3.6, 3.7, 3.8)
- sisipkan blok + caption Gambar 3.2 (remediasi) dan Gambar 3.4 (distilasi II)
- perbarui semua caption dan rujukan silang prosa
- tambah kalimat WIFI_PS_NONE di 3.7.8 dan rewording pengantar evaluasi 3.8"""
import re, sys

BASE = '/home/z/my-project/download/translator-sibi-draft'
BAB3 = f'{BASE}/bab3-metodologi.md'
DIAG = f'{BASE}/diagram'

def body(fname):
    lines = open(f'{DIAG}/{fname}', encoding='utf-8').read().splitlines()
    i = 0
    while i < len(lines) and lines[i].strip().startswith('%%'):
        i += 1
    return '\n'.join(lines[i:]).strip()

B = {k: body(f) for k, f in {
    '3.1': 'G3.1-tahapan-utama.mmd', '3.2': 'G3.2-remediasi-gerbang.mmd',
    '3.3': 'G3.3-distilasi-data-guru.mmd', '3.4': 'G3.4-distilasi-murid-deployment.mmd',
    '3.5': 'G3.5-arsitektur-akhir.mmd', '3.6': 'G3.6-topologi-jaringan.mmd',
    '3.7': 'G3.7-inferensi-tepi.mmd', '3.8': 'G3.8-alur-evaluasi.mmd'}.items()}

s = open(BAB3, encoding='utf-8').read()
blocks = re.findall(r'```mermaid\n(.*?)```', s, re.S)
assert len(blocks) == 6, f'{len(blocks)} blok, harusnya 6'

CAP = {
 '3.1': 'Gambar 3.1 Tahapan penelitian T0–T5 dan gerbang keputusan G0–G4 (jalur lolos; jalur gagal dirinci pada Gambar 3.2)',
 '3.2': ('Gambar 3.2 Jalur gagal dan remediasi gerbang keputusan G0–G4. Lingkaran kosong = lanjut ke tahap yang tertera '
         'pada label sisi; lingkaran "temuan" = penelitian berlanjut dengan hasil dilaporkan sebagai temuan. Bila G0 gagal '
         'kedua kali, jalur CSI dihentikan dan dilaporkan sebagai temuan karakterisasi, lalu penelitian lanjut ke T5; bila G1 '
         'gagal kedua kali, tindakan mengikuti Tabel 3.6 dan dicatat sebagai temuan. Kriteria lengkap: G0 (akhir M2) akuisisi '
         'stabil, pola gerak terpisah dari diam dan kosong, serta CSI + STA + ESP-NOW berjalan serentak; G1 (M3) separabilitas '
         'awal 2–3 isyarat dengan uji nearest-centroid; G2 (M6–M7) akurasi dalam sesi jauh di atas peluang acak; G3 (M10) '
         'kinerja lintas domain di atas peluang acak; G4 (M12) kelengkapan uji dan persetujuan validator.'),
 '3.3': 'Gambar 3.3 Distilasi guru–murid tahap data: perekaman tersinkron, penyaringan segmen, model guru, dan penyandingan berbasis waktu',
 '3.4': 'Gambar 3.4 Distilasi guru–murid tahap pelatihan: dataset murid ber-supervisi guru, pembanding, gerbang kinerja, dan deployment',
 '3.5': ('Gambar 3.5 Arsitektur produk akhir tanpa kamera. Rantai kiri = arah 1 (isyarat menjadi teks dan suara); '
         'rantai tengah = arah 2 (ucapan menjadi representasi SIBI); rantai kanan = jalur guru yang hanya aktif saat '
         'akuisisi data dan pelatihan; garis putus-putus = beralih ke server lokal ketika internet tidak tersedia.'),
 '3.6': 'Gambar 3.6 Topologi perangkat, komunikasi antarmodul, layanan awan, dan server',
 '3.7': 'Gambar 3.7 Inferensi langsung pada ESP32-S3',
 '3.8': 'Gambar 3.8 Alur evaluasi: pembagian data, metrik, uji operasional, uji kegunaan, dan artefak akhir',
}

# 1) ganti enam blok lama secara berurutan
urutan = ['3.1', '3.3', '3.5', '3.6', '3.7', '3.8']
it = iter(urutan)
def repl_block(m):
    k = next(it)
    return f'```mermaid\n{B[k]}\n```'
s = re.sub(r'```mermaid\n.*?```', repl_block, s, flags=re.S)

# 2) sisipkan blok 3.2 setelah caption 3.1 (caption lama diganti dulu)
s = s.replace('Gambar 3.1 Tahapan penelitian T0–T5 dengan gerbang keputusan G0–G4\n',
              CAP['3.1'] + '\n\n```mermaid\n' + B['3.2'] + '\n```\n\n' + CAP['3.2'] + '\n', 1)

# 3) caption lama 3.2 -> caption baru 3.3, lalu sisipkan blok 3.4 setelahnya
cap32_lama = 'Gambar 3.2 Alur pelatihan guru–murid dari perekaman tersinkron hingga deployment\n'
assert cap32_lama in s
s = s.replace(cap32_lama, CAP['3.3'] + '\n\n```mermaid\n' + B['3.4'] + '\n```\n\n' + CAP['3.4'] + '\n', 1)

# 4) caption lama 3.3-3.6 -> nomor/teks baru
s = s.replace('Gambar 3.3 Arsitektur produk akhir tanpa kamera\n', CAP['3.5'] + '\n', 1)
s = s.replace('Gambar 3.4 Topologi perangkat, komunikasi antarmodul, layanan awan, dan server\n', CAP['3.6'] + '\n', 1)
s = s.replace('Gambar 3.5 Inferensi langsung pada ESP32-S3\n', CAP['3.7'] + '\n', 1)
s = s.replace('Gambar 3.6 Alur dataset, pelatihan guru–murid, evaluasi, dan deployment\n', CAP['3.8'] + '\n', 1)

# 5) rujukan prosa
s = s.replace(
 'Lima tahap pertama ditutup gerbang keputusan G0–G4 seperti ditunjukkan pada Gambar 3.1.',
 'Lima tahap pertama ditutup gerbang keputusan G0–G4: jalur lolos dirangkum pada Gambar 3.1, sedangkan jalur gagal, tindakan korektif, dan uji ulang tiap gerbang dirinci pada Gambar 3.2.', 1)
s = s.replace(
 'Alur pelatihan pada tahap ini berbentuk distilasi guru–murid yang ditunjukkan pada Gambar 3.2.',
 'Alur pelatihan pada tahap ini berbentuk distilasi guru–murid: tahap perekaman, penyaringan segmen, pelatihan guru, dan penyandingan data ditunjukkan pada Gambar 3.3, sedangkan pelatihan murid, pembanding, dan deployment ditunjukkan pada Gambar 3.4.', 1)
s = s.replace(
 'seperti ditunjukkan pada Gambar 3.3. Pada jalur arah pertama',
 'seperti ditunjukkan pada Gambar 3.5. Pada jalur arah pertama', 1)
s = s.replace(
 'Topologi jaringan purwarupa ditunjukkan pada Gambar 3.4.',
 'Topologi jaringan purwarupa ditunjukkan pada Gambar 3.6.', 1)
s = s.replace(
 'Alur inferensi pada perangkat ditunjukkan pada Gambar 3.5:',
 'Alur inferensi pada perangkat ditunjukkan pada Gambar 3.7:', 1)
s = s.replace(
 'Rantai lengkap dari *dataset* hingga pengemasan ditunjukkan pada Gambar 3.6.',
 'Rantai perekaman hingga pelatihan telah ditunjukkan pada Gambar 3.3 dan Gambar 3.4, sedangkan rantai evaluasi dari model terpilih hingga artefak akhir ditunjukkan pada Gambar 3.8.', 1)

# 6) kalimat WIFI_PS_NONE di 3.7.8 (memindahkan isi simpul NOTE ke prosa, bersitasi)
s = s.replace(
 'Model murid terpilih dikuantisasi int8 lalu dijalankan pada modul penerima melalui TensorFlow Lite Micro atau ESP-DL dengan penyangga pada PSRAM.',
 'Model murid terpilih dikuantisasi int8 lalu dijalankan pada modul penerima melalui TensorFlow Lite Micro atau ESP-DL dengan penyangga pada PSRAM. Selama penangkapan CSI, radio modul terikat pada satu kanal bersama *access point* dengan *power save* dimatikan (WIFI_PS_NONE) [28], sebagaimana dipakai *firmware* RuView.', 1)

open(BAB3, 'w', encoding='utf-8').write(s)

# verifikasi cepat
blocks2 = re.findall(r'```mermaid\n(.*?)```', s, re.S)
caps = re.findall(r'^Gambar (3\.\d) ', s, re.M)
print(f'blok mermaid: {len(blocks2)}; caption: {caps}')
refs = {n: len(re.findall(rf'Gambar {n}\b', s)) - 1 for n in caps}
print('rujukan prosa per gambar (di luar caption):', refs)
assert len(blocks2) == 8 and caps == [f'3.{i}' for i in range(1, 9)], 'struktur tak sesuai'
assert all(v >= 1 for v in refs.values()), 'ada gambar tak dirujuk prosa'
print('INTEGRASI bab3: OK')
