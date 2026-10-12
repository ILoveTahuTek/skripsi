# GLOSSARY

Kamus istilah domain skripsi. Setiap skill harus memakai istilah sesuai definisi di sini — jangan berganti sinonim. (Dibuat oleh `/setup-matt-pocock-skills`; diperkaya oleh `/domain-modeling` saat keputusan istilah baru terkunci.)

## Teknologi inti

- **WiFi CSI (Channel State Information)** — data per-subcarrier yang melaporkan bagaimana sinyal Wi-Fi termodulasi oleh lingkungan fisik; modalitas sensing utama skripsi ini. Jangan tulis "Wi-Fi sensing" saat yang dimaksud adalah datanya (CSI).
- **ESP32-S3 / ESP32-C6** — mikrokontroler (~Rp150–250 rb/node) yang menangkap CSI; S3 = target produksi, C6 = riset (Wi-Fi 6, belum tervalidasi penuh di RuView).
- **Amplitudo-only** — praktik memakai amplitudo CSI dan membuang fase, karena fase ESP32 satu-antena berderau tinggi. Konsekuensi desain fitur.
- **Bandpass napas/jantung** — rentang filter 0,1–0,5 Hz (napas manusia 6–30 BPM) dan 0,8–2,0 Hz (jantung manusia 40–120 BPM), HARDCODE di semua lapisan RuView. Jantung ayam (250–330 BPM) di luar band → tak terukur tanpa ubah kode.
- **Delta-CSI** — uji gerbang minggu-1: selisih kontras sinyal antara kondisi kosong vs subjek bergerak terhadap noise floor. Hasilnya menentukan go/no-go semua garis.
- **Split blok-waktu** — protokol evaluasi time-series: latih hari A–B, uji hari C. Wajib; split acak pada data time-series = kebocoran (leakage).
- **Leave-one-subject-out** — evaluasi antar-penandatangan/subjek yang dilaporkan TERPISAH, tidak digabung dengan split blok-waktu.

## Objek/lingkup 3 alat

- **Kawanan (flock-level)** — unit analisis alat ayam: indeks aktivitas kolektif kawanan 10–50 ekor, BUKAN per-ekor. Kata ini wajib muncul di judul garis ayam.
- **Indeks aktivitas** — metrik kontinyu garis ayam (versi reformulasi dewan): agregasi motion-energy/varians CSI kawanan per window. Bukan klasifikasi penyakit.
- **Dilusi sinyal** — fenomena 1 ayam sakit di kawanan = 2–10% gangguan total; alasan utama deteksi penyakit per-ekor gugur sebagai klaim.
- **SLB (Sekolah Luar Biasa)** — konteks alat 2 (ruang kelas) dan 3 (kamar asrama): pemantauan aktivitas/keselamatan siswa berkebutuhan khusus tanpa kamera.
- **Screening (skrining)** — framing wajib untuk segala output terkait napas/tidur/distress: alat bantu pendamping BUKAN diagnosis/alat medis.

## RuView

- **RuView** — proyek open-source github.com/ruvnet/RuView; posisi di skripsi: **infrastruktur capture CSI + DSP dasar + alert**, bukan mesin pengenalan siap-pakai.
- **ADR-018** — format frame biner CSI RuView (magic 0xC5110001, header 20 byte + I/Q) yang dipakai ESP32 → server.
- **Kalibrasi 600-frame + 8 anchor** — protokol wajib per ruangan: baseline ruang kosong ≥600 frame lalu enrollment 8 pose/aktivitas (±4 menit).
- **Pose stub** — status fitur pose 17-keypoint RuView: PCK@20 3,0%, runtime confidence=0. TERLARANG dijanjikan sebagai kemampuan.
- **State semantik** — 10 FSM RuView (someone-sleeping, possible-distress, no-movement, dst.); threshold-nya untuk orang dewasa, perlu setel ulang untuk anak.

## Proses & tata kelola klaim

- **DPJ (Dokumen Pengajuan Judul)** — deliverable pengajuan ke pembimbing: 1 dokumen per alat (ayam / kelas SLB / asrama SLB), penuh 10+ halaman, tanpa halaman identitas (identitas diisi manual setelahnya). Tiga DPJ dibuat terpisah, bukan satu skripsi tiga judul.
- **Judul utama + alternatif** — struktur judul tiap DPJ: 1 judul kandidat terkuat (⭐) + 2 judul cadangan dari kandidat §2.4/§3.3/§4.3; semua judul harus tetap dipetakan ke fitur RuView yang MEASURED.
- **Jadwal semester** — rentang rencana kerja di DPJ: ±4–5 bulan; Delta-CSI & kalibrasi digabung minggu 1–3, eksperimen dipadatkan; bukan rencana 6 bulan atau 8–12 bulan.

- **Evidence-state** — label status klaim: VERIFIED / SUPPORTED / SEARCH-LIMITED. Semua klaim kebaruan wajib berlabel.
- **Kebaruan dikualifikasi** — klaim yang diizinkan = "studi kelayakan X"; klaim yang dilarang = "pertama untuk hewan/manusia", "pertama di Indonesia" sebagai kebaruan utama.
- **Human-owned decision** — keputusan yang tidak boleh diambil agent: pemilihan topik final, kosakata/judul final, persetujuan etika (pembimbing, sekolah SLB, komunitas).
- **BISINDO** — Bahasa Isyarat Indonesia (garis riset sebelumnya; ditangguhkan, artefak tetap disimpan). Berbeda dari SIBI.
- **Go/no-go** — keputusan minggu-1/2 setelah Delta-CSI & uji instrumen; kegagalan = pivot desain sebelum pipeline dibangun (bukan kegagalan skripsi).
