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
JSON terverifikasi. Minimal 10 entri referensi terverifikasi per dokumen;
referensi tanpa DOI wajib lolos verifikasi web kedua (venue+tahun+penulis) dan
diberi status `verified-web-only`. **Selesai bila:** file JSON referensi
tersimpan, nol referensi fiktif.

### 3. Susun struktur kanonik
Baca `references/struktur-dpj.md`, susun bab/subbab/tabel sesuai templat — ruang lingkup proposal hanya **BAB I–III + DAFTAR PUSTAKA** (proposal ≠ skripsi 5 bab); urutan bab, subbab wajib BAB I (Latar Belakang, Rumusan Masalah, Tujuan
Penelitian, Batasan Masalah, Manfaat Penelitian dengan Manfaat Teoretis + 
Manfaat Praktis "Bagi Peneliti" dst.), subbab Metode Penelitian/Metodologi
Penelitian, tabel Penelitian Terdahulu (kolom fitur, tanda √/−, baris "Penelitian
Ini"), subbab khas DPJ di BAB III (Rencana Kegiatan dan Jadwal penelitian 1
semester, Rencana biaya dalam Rupiah, Risiko+fallback) dan pernyataan disiplin
klaim di 1.4. Penamaan bab dibuat konsisten sepanjang dokumen. **Selesai bila:** outline lengkap dan setiap bab punya isi rencana
≥150 kata.

### 4. Tulis dengan pola bahasa korpus
Baca `references/bahasa-korpus.md` dan terapkan: corong latar belakang 4 lapis
yang ditutup "Berdasarkan uraian tersebut, penelitian ini dilakukan untuk …";
rumusan masalah berupa pertanyaan "Bagaimana …?" setelah pembuka "Berdasarkan
latar belakang …"; tujuan dengan frasa kerja "Merancang/Mengimplementasikan/"
"Mengetahui" setelah "Penelitian ini bertujuan untuk …"; batasan dibuka "Agar
penelitian ini memiliki ruang lingkup yang jelas …" dan ditutup item "Penelitian
ini tidak membahas …"; manfaat terbagi Teoretis/Praktis; metodologi sebagai
narasi tahapan ("Tahap pertama adalah studi literatur … Tahap terakhir adalah
pengujian dan evaluasi"); sitasi korpus ("Nama (Tahun) menjelaskan/menunjukkan
bahwa …"); ejaan PUEBI (`memengaruhi`), desimal koma, penomoran `Gambar`/`Tabel`
per bab, tanpa orang pertama. **Selesai bila:** tiap subbab BAB I memakai pola
pembukanya; tidak ada paragraf <3 kalimat.

### 5. Terapkan disiplin klaim (garis WiFi-CSI/RuView)
Baca `references/disiplin-klaim.md`: semua klaim dibatasi studi kelayakan; pose
17-keypoint RuView adalah stub (PCK@20 ≈ 3 persen) dan tidak boleh dijanjikan —
paradigma yang benar klasifikasi gestur langsung dari pola CSI; gerbang fisik
Delta-CSI 2×ESP32 wajib jadi titik go/no-go minggu awal; tabel batas klaim per
kasus dipatuhi; risiko + mitigasi eksplisit per risiko. **Selesai bila:**
pernyataan disiplin klaim ada di dokumen dan tidak ada klaim stub.

### 6. Generate DOCX + postcheck
Render dengan generator akademik (Times New Roman 12pt, spasi rapat, tabel tiga
garis, sitasi `[n]`, daftar pustaka APA 7 hanging indent + URL doi.org, tanpa
page break di tengah isi, footer `- N -`, tanpa cover). Lalu jalankan
`scripts/evaluator.py` terhadap hasil (mode `--doc`): skor <0,8 → perbaiki
dimensi D1–D6 yang pilihannya rendah, render ulang. **Selesai bila:** skor
evaluator ≥0,8 dan konversi PDF menunjukkan jumlah halaman + tabel utuh.

## Penggunaan lain: menilai proposal yang sudah ada
Jalankan `scripts/evaluator.py --doc <path-dokumen>` (atau nilai manual per
dimensi rubrik), laporkan skor per dimensi D1–D6 + baris aturan yang gagal +
saran perbaikan spesifik per aturan.

## Checklist rubrik (persingkat postcheck; detail aturan di rubric.json repo)
- D1 Struktur: hanya BAB I–III + DAFTAR PUSTAKA; subbab wajib BAB I + tabel
  Penelitian Terdahulu + subbab jadwal/biaya/risiko di BAB III; penamaan
  konsisten.
- D2 Pola bahasa: pembuka subbab BAB I pola korpus; item tujuan=frasa kerja;
  batasan ditutup "tidak membahas".
- D3 Sitasi: dalam teks `Nama (Tahun) menjelaskan/menunjukkan/menyoroti`;
  daftar pustaka APA 7 hanging indent + DOI; semua terverifikasi.
- D4 Mekanika: judul kapital; `Gambar`/`Tabel` bernomor per bab; `memengaruhi`
  (bukan mempengaruhi); desimal koma; tanpa orang pertama.
- D5 Disiplin: studi kelayakan; stub tidak dijanjikan; Delta-CSI go/no-go;
  risiko+mitigasi.
- D6 Kelengkapan: 1 judul + 2 alternatif; jadwal semester; biaya Rupiah;
  placeholder eksplisit; tanpa halaman sampul.

## File referensi (baca saat babnya dikerjakan)
- `references/struktur-dpj.md` — struktur bab kanonik + templat tabel
- `references/bahasa-korpus.md` — pola kalimat literal korpus (pembuka subbab,
  corong, metodologi, sitasi, abstrak)
- `references/disiplin-klaim.md` — batas klaim WiFi-CSI/RuView + gerbang fisik
- `scripts/evaluator.py` — penilai kepatuhan rubrik (D1–D6, skor 0–1)
