#!/usr/bin/env python3
"""Gelombang 14: pangkas DAFTAR PUSTAKA 46 -> 22 entri di v14 + tulis log G14."""
import re
from pathlib import Path

MD = Path("/home/z/my-project/download/sensesibi-v10/Proposal-SenseSIBI-v14.md")
teks = MD.read_text(encoding="utf-8")

# 1) parse entri DP lama dari v14 (identik v13)
m = re.search(r"^# DAFTAR PUSTAKA\n(.*?)\n<!-- ===== AKHIR NASKAH", teks, re.S | re.M)
assert m, "blok DP tidak ditemukan"
blok = m.group(1)
entri = {}
for potong in re.split(r"\n\n+", blok.strip()):
    mm = re.match(r"^\[(\d+)\] (.*)$", potong, re.S)
    if mm:
        entri[int(mm.group(1))] = mm.group(2).strip()
assert len(entri) == 46, f"entri DP lama = {len(entri)}, harus 46"

# 2) peta baru: nomor baru -> nomor lama (urutan kemunculan pertama di teks)
peta = {1: 1, 2: 2, 3: 3, 4: 8, 5: 11, 6: 14, 7: 15, 8: 18, 9: 19, 10: 20, 11: 21,
        12: 25, 13: 27, 14: 29, 15: 30, 16: 31, 17: 33, 18: 35, 19: 38, 20: 39,
        21: 45, 22: 46}
baru = ["# DAFTAR PUSTAKA", ""]
for baru_n, lama_n in peta.items():
    baru.append(f"[{baru_n}] {entri[lama_n]}")
dp_baru = "\n\n".join(baru) + "\n\n"

teks = teks[:m.start()] + dp_baru + teks[m.end() - len("<!-- ===== AKHIR NASKAH"):]

# 3) log G14 di akhir berkas
log = """

## Log Perubahan — Revisi 12 November 2026, gelombang 14 (daftar pustaka 22 entri, sekitar 30 halaman, diagram direvisi)

Permintaan: memangkas daftar pustaka menjadi sekitar 20-an entri, memadatkan keseluruhan proposal menjadi sekitar 30 halaman, dan merevisi diagram dengan pedoman scientific-agent-skills (K-Dense: scientific-schematics, markdown-mermaid-writing, scientific-writing) di atas kaidah humanizer-indonesia (adhiprib v1.7, register akademik).

- Daftar pustaka dipangkas dari 46 menjadi 22 entri dan sitasi dinomori ulang 1 sampai 22 menurut urutan kemunculan. Enam sumber Indonesia dipertahankan (Kemenko PMK, UU Disabitias, Kamus SIBI, Mursita, Dwijayanti, MMS-TTS-ind) seluruh fondasi metode dipertahankan (survey CSI, SignFi, CSI-ratio, Widar3.0, ESP32-S3, esp-csi, RuView, Hinton, Ultralytics, SVM, Chow, ESP-DL, Kokoro, Whisper, Mankins, Likert).
- Dua puluh empat rujukan dibuang: berita BRIN, tiga studi SIBI/BISINDO tambahan (As Satillah, Nugraheni, Malika), dua sistem satu arah (KASIBI, OpenSIBI), tiga aplikasi kamera Indonesia (Soekarta, Maulana, tinjauan Sanjaya, dataset Kindy), dua sistem Wi-Fi SLR tambahan (DF-WiSLR, WiSign), DensePose from WiFi, Widar2.0, Picron, empat repositori kerangka Rust (Tokio, Axum, Leptos, Tauri), dan tiga repositori implementasi (esp-nn, tflite-micro, kokoro-onnx, onnxruntime, faster-whisper).
- Klaim yang kehilangan rujukan diperlunak, bukan dibiarkan tanpa sumber: angka 77,7%/1,9% BRIN, skor 3,362 KASIBI, 50 kosakata OpenSIBI, akselerasi 2.300 menjadi 54 ms esp-nn, dan 13 menit dalam 59 detik faster-whisper dihapus bersama rujukannya; klaim "masalah terbuka" penerjemahan kalimat diperlunak menjadi alasan rancangan tanpa klaim status riset; kosakata arah kedua kini mengacu ke Kamus SIBI.
- Naskah dipadatkan menjadi sekitar 30 halaman: 1.1 dari tujuh menjadi enam paragraf, 2.1 diringkas, Tabel 2.2 dari delapan menjadi empat baris, sel tabel 2.3 dan 3.2 dibersihkan dari sitasi kerangka; register mahasiswa D4/S1, konteks Jawa Timur tanpa mitra lembaga, dan seluruh angka pra-penelitian yang bertahan tetap sama sumbernya.
- Tiga diagram direvisi mengikuti pedoman scientific-agent-skills: anotasi aksesibilitas accTitle/accDescr ditambahkan pada ketiganya, subgraf tanpa judul diberi judul bermakna (fase pembangunan data/pengujian dan penulisan pada Gambar 3.1; arah 1/arah 2/jalur guru pada Gambar 3.2; akuisisi dan segmentasi/klasifikasi dan keluaran pada Gambar 3.3), setiap label simpul ditelusur ulang ke teks, dan keterangan Gambar 3.2 disesuaikan dengan pengelompokan subgraf.
- Yang tidak berubah: struktur BAB I sampai III, 12 tabel, tiga gambar beserta semantik alurnya, lima gerbang G0 sampai G4, jadwal M1 sampai M14, enam prosedur pengujian, sembilan batasan, rumusan dan tujuan 3:3, serta penanda [PERLU DATA]/[PERLU ILUSTRASI].
- Pemetaan nomor akhir ke kunci: [1]kemenkopmk, [2]uu-disabilitas, [3]kamus-cetak, [4]mursita, [5]dwijayanti, [6]ma-csur, [7]signfi, [8]esp32s3, [9]esp-csi, [10]ruview, [11]hinton, [12]csi-ratio, [13]widar3, [14]ultralytics, [15]svm, [16]chow, [17]esp-dl, [18]kokoro-card, [19]mms-card, [20]whisper, [21]trl, [22]likert
"""
teks = teks.rstrip() + log
MD.write_text(teks, encoding="utf-8")

# 4) verifikasi: sitasi tubuh hanya 1-22, berurutan kemunculan, DP 22 entri
tubuh = teks[: teks.index("# DAFTAR PUSTAKA")]
nomor = [int(x) for x in re.findall(r"\[(\d+)\]", tubuh)]
assert max(nomor) <= 22, f"masih ada sitasi > 22: {sorted(set(nomor) - set(range(1,23)))}"
pertama = []
for n in nomor:
    if n not in pertama:
        pertama.append(n)
print("urutan kemunculan pertama:", pertama)
print("monoton naik:", pertama == sorted(pertama))
dp_n = [int(x) for x in re.findall(r"^\[(\d+)\]", re.search(r"# DAFTAR PUSTAKA\n(.*?)\n<!--", teks, re.S).group(1), re.M)]
print("entri DP:", len(dp_n), dp_n)
print("semua tersitasi:", set(dp_n) == set(pertama))
print("total karakter naskah:", len(teks))
