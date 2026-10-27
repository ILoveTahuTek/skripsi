# Catatan — Peta Literatur Titik Temu

**Paket:** `download/translator-sibi-literatur/` · 26 Oktober 2026

## Isi paket

| Berkas | Fungsi |
|---|---|
| `Peta-Literatur-Titik-Temu.png` | Papan kanban visual (3729×4068 px, skala 1,5) — 79 kartu rujukan pada 9 kolom titik temu |
| `Peta-Literatur-Titik-Temu.html` | Sumber visual yang sama, dapat dibuka di peramban untuk memperbesar (zoom) dan mencari (Ctrl+F "SignFi", "[24]", dsb.) |

## Struktur visual

- **Strip konvergensi (paling atas):** Masalah inti → 4 kesenjangan (K1–K4) → Titik temu penelitian — cermin "peta masalah" yang tadinya menjadi Gambar 1.1 draft.
- **9 kolom = 9 pertanyaan titik temu** tersusun mengikuti alur argumen proposal (kiri → kanan): konteks masalah → solusi eksisting berbasis kamera → kelayakan CSI → sensitivitas & risiko → supervisi visi → perangkat tepi → arah balik → suara Indonesia → metode & evaluasi. Kepala tiap kolom mencantumkan subbab proposal yang ditopang kolom itu.
- **Kartu = 1 rujukan**: nomor [n] (sama dengan Daftar Pustaka draft), penulis-tahun, venue, klaim inti satu kalimat, label peran, dan jenis sumber. Huruf grup kecil di pojok kanan atas kartu (A–H) = kelompok asli pada `Matriks-Literatur-dan-Bukti.md`.
- **Kotak kuning putus-putus** di dasar tiap kolom = celah/implikasi — batas bukti yang menjadi ruang kontribusi riset.

## Disiplin kejujuran

- Seluruh klaim kartu bersumber dari `../translator-sibi-revisi/Matriks-Literatur-dan-Bukti.md` (status verifikasi 24–25 Oktober 2026); tidak ada klaim baru yang dikarang.
- Dua kartu berlabel "(metadata)" ([43], [44]) adalah rujukan yang terverifikasi hanya sampai metadata DOI — disesuaikan dengan kualifikasi pada matriks.
- Kartu [38] Kokoro sengaja ditampilkan sebagai bukti disiplin pemilihan teknologi (8 bahasa tanpa Indonesia), bukan kegagalan.

## Regenerasi

```
python3 /home/z/my-project/scripts/translator-sibi-literatur/buat_peta_literatur.py   # bangun HTML + render PNG
python3 /home/z/my-project/scripts/translator-sibi-literatur/verifikasi_peta.py      # cek luapan/tumpang tindih/jumlah kartu
```

Data kartu tersimpan terpisah di `scripts/translator-sibi-literatur/data_literatur.py` — sunting klaim/tambah rujukan di sana lalu jalankan ulang skrip pertama.
