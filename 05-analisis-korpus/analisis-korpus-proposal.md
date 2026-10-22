# Analisis Korpus Proposal & Tugas Akhir — Drive Mahasiswa TRSE

**Sumber korpus:** Google Drive `1Dk8kygzZZkFQE9uc-Z2zPbltToQMz-lF` (69 dokumen terunduh; 43 PDF, 20 DOCX, 4 PPTX, 2 DOC).
**Konteks institusi:** Universitas Negeri Malang — Fakultas Vokasi — Program Studi Sarjana Terapan **Teknologi Rekayasa Sistem Elektronika (TRSE)**, jenjang D4. Terkonfirmasi dari halaman sampul, lembar pengesahan, dan NIM (2205327xxxxx) pada ≥6 dokumen.
**Teks terkonversi:** `tool-results/korpus-teks/` (7 dokumen teks penuh).

## 1. Dokumen yang dianalisis (≥8, menyeluruh)

| # | Dokumen | Jenis | Catatan |
|---|---------|-------|---------|
| 1 | Fuad Hylmi Haidar — *Proposal Tugas Akhir* (deteksi bentuk & warna mesin capit arcade, Raspberry Pi) | Proposal TA penuh | Struktur + bahasa paling lengkap; ada BAB IV hasil |
| 2 | Muhamad Hafiatul Annur — *Proposal TA* TERBARU (monitoring bahan bakar genset kereta, ESP32) | Proposal TA penuh | Abstrak model; tabel Penelitian Terdahulu model |
| 3 | Muhamad Hafiatul Annur — *Proposal TA* (_Sip, versi lama) | Proposal TA | Konfirmasi konsistensi antar-versi |
| 4 | Endah Wulandari — *Naskah Skripsi* (LoRa + ESP32-CAM banjir + Telegram) | Naskah penuh | Metodologi naratif "tahap pertama…tahap terakhir" |
| 5 | Brata Oktaviano J — *TA* (D4 TRSE) | Naskah penuh | Variasi judul bab (KAJIAN PUSTAKA, PENUTUP) |
| 6 | Zikri Mubarak — *Draft SEMHAS* | Seminar hasil | Struktur bab identik dengan naskah |
| 7 | Fatur Raman — *Seminar Hasil 2026* | Seminar hasil | BAB II TINJAUAN PUSTAKA (variasi penamaan) |
| 8 | Ario Wicaksono — *Laporan Tugas Akhir* | Laporan TA | Generasi lebih lama, struktur sama → stabilitas lintas angkatan |
| 9–12 | Template & berkas paten (Rahul, Rimbang, Naufal, Rafli, Brata, Ario) | Dokumen paten | Di luar cakupan skill proposal; hanya konteks korpus |

## 2. Struktur kanonik (konsisten 8/8 dokumen)

```
[Halaman sampul ×2 — untuk DPJ: TIDAK DIPAKAI (aturan user)]
LEMBAR PERSETUJUAN PEMBIMBING → PERNYATAAN KEASLIAN → KATA PENGANTAR
ABSTRAK → ABSTRACT → DAFTAR ISI → DAFTAR GAMBAR → DAFTAR TABEL

BAB I   PENDAHULUAN
        1.1 Latar Belakang
        1.2 Rumusan Masalah
        1.3 Tujuan Penelitian
        1.4 Batasan Masalah
        1.5 Manfaat Penelitian (1.5.1 Manfaat Teoretis; 1.5.2 Manfaat Praktis —
            bagi Peneliti / Pengembang / Pengguna / Praktisi)
BAB II  KAJIAN PUSTAKA  (variasi: TINJAUAN PUSTAKA)
        2.1..2.n — satu subbab per teknologi/konsep, urut dari sistem → komponen
        2.n  Penelitian Terdahulu — TABEL KOMPARASI: kolom judul+peneliti,
             kolom fitur √/−, baris terakhir "Penelitian Ini", lalu prosa gap
             + daftar bernomor "mengisi celah"
BAB III METODE PENELITIAN (variasi: METODOLOGI PENELITIAN)
        3.1 Alur/Tahapan Penelitian (narasi + diagram alir)
        3.2 Studi Literatur
        3.3.. Perancangan alat (skematik, diagram blok) & perangkat lunak
        3.n   Pengujian (satu sub-bab per fitur yang diuji)
        3.n+1 Evaluasi
BAB IV  HASIL DAN PEMBAHASAN   ← tidak ada pada tahap pengajuan judul
BAB V   KESIMPULAN DAN SARAN (variasi: PENUTUP)
DAFTAR PUSTAKA → Lampiran
```

**Implikasi untuk DPJ (pengajuan judul):** struktur inti = BAB I–III + rencana. Bab khas DPJ yang TIDAK ada di korpus (jadwal semester, risiko/fallback, biaya, batasan studi kelayakan) dipertahankan dari keputusan user sebelumnya, ditulis mengikuti gaya bahasa korpus.

## 3. Pola bahasa (dikutip literal dari korpus)

### 3.1 Latar belakang — corong 4 lapis
1. **Konteks umum** (1 paragraf): `Perkembangan teknologi telah memengaruhi …` / kondisi lapangan.
2. **Masalah spesifik**: `Pada [sistem] konvensional, … Kondisi tersebut menunjukkan bahwa …`
3. **Teknologi penyuluhan**: per teknologi satu paragraf + sitasi `Nama (Tahun) menjelaskan bahwa …`.
4. **Penutup latar belakang**: `Berdasarkan uraian tersebut, penelitian ini dilakukan untuk …`.

### 3.2 Kalimat pembuka subbab BAB I (literal)
- Rumusan: `Berdasarkan latar belakang permasalahan yang telah diuraikan …, maka dapat dirumuskan beberapa rumusan masalah … sebagai berikut.` → item = pertanyaan **Bagaimana …?** (2–4 item).
- Tujuan: `Penelitian ini bertujuan untuk … Adapun tujuan dari penelitian ini adalah sebagai berikut.` → item = frasa kerja: **Merancang… / Mengimplementasikan… / Mengetahui hasil pengujian…** (mirror rumusan).
- Batasan: `Agar penelitian ini memiliki ruang lingkup yang jelas dan terarah …, maka ditentukan batasan masalah … sebagai berikut.` → item bernomor; item terakhir selalu berpola `Penelitian ini tidak membahas …`.
- Manfaat: paragraf pengantar + `1.5.1 Manfaat Teoretis` (referensi bagi peneliti lain) & `1.5.2 Manfaat Praktis` (sub-item Bagi …).

### 3.3 Metodologi — narasi tahapan
`Penelitian … dilaksanakan melalui beberapa tahapan yang tersusun secara sistematis … Tahap pertama adalah studi literatur, … Tahap kedua adalah perancangan sistem … Tahap ketiga adalah implementasi … Tahap terakhir adalah pengujian dan evaluasi. Apabila … ditemukan kendala …, maka dilakukan evaluasi dan perbaikan secara berulang hingga sistem dapat bekerja secara optimal.`

### 3.4 Sitasi & daftar pustaka
- Dalam teks: `Nama (Tahun) menjelaskan bahwa …` / `… (Nama et al., Tahun)` / `Nama et al. (Tahun) menunjukkan bahwa …`. Kata kerja pelaporan: **menjelaskan, menunjukkan, menyoroti**.
- Daftar pustaka: **APA edisi 7**, hanging indent, pola `Nama, A. (Tahun). Judul. Venue, vol(issue), hal. https://doi.org/…` — DOI URL selalu disertakan bila ada.

### 3.5 Abstrak (1 paragraf, ±200 kata)
Konteks & krusialitas masalah → keadaan saat ini + kelemahan → tantangan teknis → `Penelitian ini bertujuan untuk …` → metode singkat → `Hasil pengujian menunjukkan bahwa …` → keunggulan utama + implikasi. Ditutup `Kata Kunci: 5–6 frasa` (+ versi Inggris `Keywords:`).

### 3.6 Mekanika penulisan
- Judul dokumen: **KAPITAL SEMUA**, pola `RANCANG BANGUN / IMPLEMENTASI / PERANCANGAN … BERBASIS … MENGGUNAKAN …` (2–3 baris, terpusat).
- Kode gambar/tabel: `Gambar <bab>.<urut>` / `Tabel <bab>.<urut>` + judul; tabel komparasi memakai tanda **√ / −**.
- Ejaan: `memengaruhi` (PUEBI), bukan `mempengaruhi`; istilah asing dibiarkan Latin (computer vision, real-time, embedded system, hardware/software).
- Orang pertama **tidak pernah** muncul; subjek = `penelitian ini`, `sistem`, `alat`.
- Paragraf 3–8 kalimat; tidak ada bullet tanpa kalimat pengantar.
- Angka desimal koma (gaya Indonesia): `0,9967 detik`, `99%`.

## 4. Variasi yang diizinkan (bukan kesalahan)
- KAJIAN PUSTAKA ↔ TINJAUAN PUSTAKA; METODE ↔ METODOLOGI PENELITIAN; KESIMPULAN DAN SARAN ↔ PENUTUP — pilih satu dan konsisten sepanjang dokumen.
- Jumlah subbab BAB II bebas (8–13), mengikuti teknologi yang dipakai.
- Bab metodologi bisa `Alur Penelitian` atau `Tahapan Pengembangan Sistem` sebagai subbab pembuka.

## 5. Hal yang TIDAK ditemukan di korpus (keputusan DPJ sebelumnya tetap berlaku)
- Tidak ada jadwal penelitian / RAB pada naskah selesai → untuk DPJ tetap disertakan (aturan user), ditulis dengan gaya kalimat korpus.
- Tidak ada disiplin klaim eksplisit → DPJ WiFi-CSI tetap wajib "studi kelayakan" + gerbang fisik (konsistensi dengan 3 DPJ sebelumnya).
- Korpus memakai halaman sampul/lembar pengesahan → DPJ TIDAK memakai cover (aturan user: "skip bagian cover").
