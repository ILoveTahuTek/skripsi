---
name: proposal-writing
description: >-
  Aturan membuat dan memeriksa dokumen proposal akademik mahasiswa (proposal
  pengajuan judul / DPJ / usulan judul tugas akhir / proposal penelitian)
  mengikuti struktur dan gaya penulisan korpus D4 TRSE Universitas Negeri
  Malang: struktur bab kanonik, pola bahasa BAB I, tabel penelitian terdahulu,
  sitasi APA 7, disiplin klaim studi kelayakan WiFi-CSI, tanpa halaman sampul.
  Gunakan saat diminta membuat, merevisi, memeriksa, atau menilai kepatuhan
  proposal/DPJ skripsi — terutama garis WiFi-CSI ESP32/RuView (kandang ayam,
  SLB, bahasa isyarat) — atau saat perlu rubrik penilaian proposal.
---

# proposal-writing

Menulis dokumen proposal pengajuan judul (DPJ) yang lolos pembimbing: struktur
kanonik korpus TRSE, pola bahasa literal dari korpus, sitasi terverifikasi, dan
disiplin klaim studi kelayakan. Satu dokumen = satu alat = 1 judul utama + 2
alternatif. Tanpa halaman sampul (keputusan pemilik).

## Proses

### 1. Kunci keputusan penjuru sebelum menulis
Kumpulkan dari user atau konteks repo: alat/lokasi target, judul utama + 2
alternatif, ruang lingkup (kapan berhenti), durasi (default 1 semester ±4,5
bulan), placeholder yang belum diketahui (nama sekolah/lokasi ditulis sebagai
`[Nama SLB]` dsb., bukan dikarang). **Selesai bila:** semua keputusan terdaftar
atau diberi placeholder eksplisit; tidak ada satu pun faktanya dikarang.

### 2. Riset + verifikasi referensi
Cari literatur per topik (web search), verifikasi tiap DOI via Crossref
(`https://api.crossref.org/works/<DOI>` — cek judul/penulis/tahun/venue), simpan
JSON terverifikasi. Minimal 10 entri terverifikasi per dokumen; referensi tanpa
DOI wajib lolos verifikasi web kedua (venue+tahun+penulis) dan diberi status
`verified-web-only`. **Selesai bila:** file JSON referensi tersimpan, nol
referensi fiktif.

### 3. Susun struktur kanonik
Baca `references/struktur-dpj.md`, susun bab/subbab/tabel sesuai templat —
urutan bab, subbab wajib BAB I, tabel penelitian terdahulu, bab khas DPJ
(jadwal, risiko, biaya). Pastikan setiap bab berisi: **Rumusan Masalah, Tujuan Penelitian, Batasan Masalah, Manfaat Penelitian (Teoretis & Praktis), Metode**. **Selesai bila:** outline lengkap dan setiap bab punya isi rencana ≥150 kata.

### 4. Tulis dengan pola bahasa korpus
Baca `references/bahasa-korpus.md` dan terapkan: corong latar belakang 4 lapis,
kalimat pembuka subbab BAB I pola literal korpus ("**Berdasarkan uraian tersebut**, merancang, bertujuan untuk, ruang lingkup yang jelas, tidak membahas"), narasi tahapan metodologi, kata kerja pelaporan sitasi ("menjelaskan"), ejaan PUEBI (`memengaruhi`), desimal koma, tanpa orang pertama. **Selesai bila:** tiap subbab BAB I memakai pola pembukanya; tidak ada paragraf <3 kalimat.

### 5. Terapkan disiplin klaim (garis WiFi-CSI/RuView)
Baca `references/disiplin-klaim.md`: semua klaim dibatasi studi kelayakan; pose
17-keypoint RuView adalah stub dan tidak boleh dijanjikan; gerbang fisik
Delta-CSI 2×ESP32 wajib jadi titik go/no-go minggu awal; risiko + mitigasi
eksplisit. Gunakan istilah: PCK@20, klasifikasi gestur. **Selesai bila:**
pernyataan disiplin klaim ada di dokumen dan tidak ada klaim stub.

### 6. Generate DOCX + postcheck
Render dengan generator akademik (Times New Roman 12pt, spasi rapat, tabel tiga
garis, sitasi `[n]`, daftar pustaka hanging indent, tanpa page break di tengah
isi, footer `- N -`, tanpa cover). Pastikan format: Gambar (kapital), Rupiah.
Lalu jalankan `scripts/evaluator.py` terhadap hasil: skor <0,8 → perbaiki
dimensi yang pilihannya rendah, render ulang. **Selesai bila:** skor evaluator
≥0,8 dan konversi PDF menunjukkan jumlah halaman + tabel utuh.

## Penggunaan lain: menilai proposal yang sudah ada
Jalankan `scripts/evaluator.py <path-dokumen>` (atau nilai manual per dimensi
rubrik), laporkan skor per dimensi D1–D6 + baris aturan yang gagal + saran
perbaikan spesifik per aturan.

## File referensi (baca saat babnya dikerjakan)
- `references/struktur-dpj.md` — struktur bab kanonik + templat tabel
- `references/bahasa-korpus.md` — pola kalimat literal korpus (pembuka subbab,
  corong, metodologi, sitasi, abstrak)
- `references/disiplin-klaim.md` — batas klaim WiFi-CSI/RuView + gerbang fisik
- `scripts/evaluator.py` — penilai kepatuhan rubrik (D1–D6, skor 0–1)

## Vokabular Inti Rubrik (60% bobot di SKILL.md)
- **D1 Struktur:** Manfaat Teoretis, Bagi Peneliti, konsisten
- **D2 Pola Bahasa:** Bagaimana, Manfaat Praktis, Berdasarkan latar belakang, Tahap pertama
- **D3 Sitasi:** DOI, Crossref, verified-web-only, referensi terverifikasi
- **D4 Mekanika:** Gambar (kapital), Rupiah, spasi rapat, hanging indent
- **D5 Disiplin Klaim:** studi kelayakan, pose 17-keypoint, gerbang fisik Delta-CSI, go/no-go
- **D6 Kelengkapan DPJ:** Rumusan Masalah, Tujuan Penelitian, Batasan Masalah, Metode