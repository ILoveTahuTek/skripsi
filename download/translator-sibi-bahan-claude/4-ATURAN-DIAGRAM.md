# 4 — Aturan Diagram (8 figur Mermaid)

## Status: SUDAH DIREDESAIN & TERVALIDASI — JANGAN REDESAIN

Kedelapan diagram adalah hasil audit 27 Oktober 2026 yang sudah memenuhi standar cetak: huruf efektif 9,2–11,8 pt pada lebar sematan 14 cm, rasio tinggi/lebar ≤ 1,34, lolos pemeriksa integritas otomatis (76 simpul & 64 sisi terwakili), dan lolos inspeksi PDF ekspor (8 gambar sehalaman dengan caption). **Meredesain ulang berarti merusak hasil terukur.**

## Sumber tunggal

Blok ` ```mermaid ` di dalam `naskah-sumber.md` adalah sumber tunggal (tersinkron dengan berkas `.mmd` di luar paket). Perlakukan **verbatim**: jangan mengubah teks simpul, sisi, label, arah alur, subgraf, atau konfigurasi.

## Peta 8 figur

| G | Caption (inti) | Level | Lokasi | Tujuan komunikasi |
|---|---|---|---|---|
| 3.1 | Tahapan T0–T5 + gerbang G0–G4 (jalur lolos) | L1 | §3.2 | Kronologi 6 tahap + posisi 5 gerbang |
| 3.2 | Jalur gagal & remediasi gerbang G0–G4 | L3 | §3.2 | Aksi korektif, uji ulang, terminal bila gagal |
| 3.3 | Distilasi (I): perekaman, guru, penyandingan | L2 | §3.2.3 | Data multimodal tersinkron + kualitas guru |
| 3.4 | Distilasi (II): murid, pembanding, deployment | L2 | §3.2.3 | Pelatihan murid 1D-CNN hingga modul |
| 3.5 | Arsitektur produk akhir tanpa kamera | L2 | §3.5.1 | Dua jalur operasional + jalur guru + cadangan lokal |
| 3.6 | Topologi perangkat & jaringan | L2 | §3.5.2 | Siapa tersambung ke apa lewat media apa |
| 3.7 | Inferensi langsung pada ESP32-S3 | L3 | §3.7.8 | Alur inferensi per segmen + ambang penolakan |
| 3.8 | Alur evaluasi hingga artefak | L2 | §3.8 | Dari model terpilih ke laporan kelayakan |

Caption lengkap (resmi) ada di naskah, satu paragraf di bawah tiap blok — ikuti apa adanya.

## Sistem desain (konteks — jangan diubah)

Tema `neutral` (lulus cetak grayscale); bentuk bermakna (persegi = proses, belah ketupat/sudut membulat = keputusan, garis putus-putus = jalur cadangan); huruf sumber 22–26 px; label keputusan eksplisit ("lolos/gagal", "ya/tidak", "belum").

## Tugas Claude terhadap diagram (verifikasi, bukan redesain)

1. **Rujukan silang:** pastikan setiap Gambar 3.1–3.8 dirujuk di prosa minimal sekali dan setiap rujukan menunjuk gambar yang benar — periksa khusus prosa §3.2, §3.2.3, §3.5.1, §3.5.2, §3.7.8, §3.8.
2. **Koreksi wajib (satu-satunya perubahan figur yang diizinkan):** catatan penyusunan di kepala naskah masih menulis "(Gambar 3.1–3.6)" — **koreksi menjadi "(Gambar 3.1–3.8)"** (sisa audit lama). Catat di log perubahan.
3. **Kesesuaian makna:** bila menemukan ketidaksesuaian antara isi diagram dan prosa (istilah, arah alur, kondisi gerbang, jumlah pihak), JANGAN perbaiki senyap — catat di daftar temuan dengan lokasi dan usulan perbaikan.
4. **Larangan:** menambah/menghapus simpul atau sisi; mengganti istilah di simpul; mengubah nomor/judul gambar; memecah atau menggabungkan figur; mengubah caption kecuali koreksi rujukan silang yang salah nomor.
