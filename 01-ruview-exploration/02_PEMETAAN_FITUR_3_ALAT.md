# PEMETAAN RuView → 3 OPSI JUDUL PROPOSAL SKRIPSI

**Dibuat:** 2026-10-12 · **Basis:** laporan eksplorasi deep-dive `01_EKSPLORASI_DEEP_RUVIEW.md` + handoff & spec Drive + laporan kritik dewan LLM (garis ayam).
**Prinsip:** setiap kata judul harus bisa dipetakan ke hasil yang terbukti dalam 6 bulan; RuView diposisikan sebagai infrastruktur, bukan janji.

---

## 1. Tiga Alat, Satu Platform

Rencana Anda: **3 alat** dari satu platform RuView — (1) kandang ayam broiler, (2) ruang kelas SLB, (3) kamar asrama SLB. Eksplorasi repo menunjukkan ini TIDAK berarti tiga skripsi: firmware, server, kalibrasi, dan dashboard RuView identik untuk ketiganya. Yang berubah adalah **penempatan node, parameter, target pengukuran, dan protokol validasi**. Maka strategi paling defensibel: pilih SATU sebagai objek utama skripsi; dua lainnya jadi catatan "kemungkinan perluasan" — ATAU pilih satu objek dengan 3 kandidat judul di dalamnya.

Di bawah ini analisis ketiganya lengkap, lalu §6 memberi rekomendasi keputusan.

---

## 2. ALAT 1 — WiFi CSI Kandang Ayam Broiler

### 2.1 Fitur RuView yang dipakai (tanpa/tanpa banyak ubah kode)
| Fitur RuView | Fungsi untuk alat ini | Perubahan kode |
|---|---|---|
| Capture CSI ESP32-S3 + streaming UDP (ADR-018) | Sumber data utama | Tidak ada |
| Presence heuristik (varians fase, kalibrasi ambient 60 dtk) | Deteksi ada/tidaknya aktivitas kawanan | Tidak ada |
| Motion-band power + akselerasi fase | **Indeks aktivitas kawanan** (inti skripsi versi reformulasi) | Tidak ada |
| Modul `ind_livestock_monitor` (stillness ≥5 mnt, escape, labored-breathing, poultry 15–30 BPM) | Template desain alert kesehatan kawanan | Tiru pola, bukan jalankan langsung |
| Kalibrasi ruang kosong ≥600 frame | Baseline kandang kosong | Tidak ada |
| Recording JSONL + adaptive classifier | Dataset percontohan + classifier baseline | Tidak ada |
| Dashboard web + MQTT/HA + notifikasi | Alarm ke peternak | Tidak ada |
| Bandpass napas 0,1–0,5 Hz (jika lanjut ke napas unggas) | Estimasi napas kawanan | **WAJIB ubah konstanta** di firmware+server+binding; jantung ayam (250–330 BPM) TIDAK mungkin tanpa re-desain filter |

### 2.2 Apa yang RuView TIDAK selesaikan (tetap tanggung jawab skripsi)
- **Dilusi sinyal kawanan** — 1 ayam sakit dari 30 ekor = 3% gangguan; fisika Doppler skala massa 2 kg 20–40× lebih lemah dari babi 80 kg (temuan dewan Anda, tidak berubah).
- **Konfound lingkungan** — jadwal pakan, panen, cahaya, kipas ventilasi (false-positive presence yang dikenal RuView!), orang lewat. Wajib log kejadian harian sebagai kovariat.
- **Ground truth** — kamera sinkron untuk pelabelan (premis "tanpa kamera" hanya berlaku saat runtime).
- **Pseudoreplikasi** — 1 kandang 1 kawanan = n=1; split blok-waktu wajib.

### 2.3 Status kebaruan (dari laporan dewan Anda, masih valid)
- ✅ Tidak ada publikasi WiFi CSI pada unggas di dunia (10 referensi terverifikasi, termasuk review He dkk. 2022 yang nol menyebut WiFi).
- ❌ "Pertama untuk hewan" TERLARANG (babi & sapi mendahului: Hao 2019, Lu 2019, Hao 2020).
- Kebaruan metodologis terkuat: **sensing kolektif device-free pada kawanan kecil** (belum dipetakan siapa pun).

### 2.4 Kandidat judul (dari dewan, Opsi 1 ⭐ tetap rekomendasi teraman)
1. ⭐ **Estimasi Indeks Aktivitas Kawanan Broiler Berbasis Wi-Fi Channel State Information pada ESP32: Studi Kelayakan Pemantauan Dini Kesehatan Unggas**
2. **Deteksi Perubahan Aktivitas Kawanan Ayam Berbasis Wi-Fi CSI untuk Sistem Peringatan Dini di Peternakan Rakyat**
3. **Sistem Monitoring Perilaku Kawanan Unggas Device-Free Berbasis Wi-Fi CSI pada ESP32 dengan Dataset Publik**

**Posisi RuView di proposal:** infrastruktur capture CSI + pipeline DSP + alert; diperkaya modul ternak (`ind_livestock_monitor`) sebagai acuan desain. Jangan menulis "memakai RuView untuk pose" — pose on-device stub (PCK@20 3,0%).

---

## 3. ALAT 2 — WiFi CSI Ruang Kelas SLB

### 3.1 Fitur RuView yang dipakai
| Fitur RuView | Fungsi untuk alat ini | Perubahan kode |
|---|---|---|
| Presence + person count (heuristik) | Kehadiran/kepadatan di kelas | Tidak ada (hitung = kasar, degradasi >2–3 orang) |
| Motion level + motion energy | Intensitas aktivitas kelas | Tidak ada |
| `room_active` FSM | Status kelas aktif/tidak | Tidak ada |
| **Fall detection** (akselerasi fase + debounce, <200 ms) | Deteksi anak jatuh/pingsan | Tidak ada |
| `no_movement` (30 mnt) + `sec_panic_motion` | Anomali inaktivitas/gerakan panik | Threshold perlu disetel |
| `possible-distress` FSM | Peringatan distress | Threshold perlu disetel |
| Privacy mode (strip biometrik) | Etika: kelas anak berkebutuhan khusus | Tidak ada — aktifkan |
| MQTT → Home Assistant → notifikasi guru | Alert real-time | Tidak ada |
| Kalibrasi 600 frame + enrollment 8 anchor | Per kelas, ±4 menit | Tidak ada |

### 3.2 Masalah & peluang riset yang khas SLB
- **Threshold dirancang untuk dewasa** — napas anak 6–12 th ~18–25 BPM (tepi/lewat atas band 6–30 BPM itu masih oke, tapi ambang FSM "sleeping" 8–20 BPM tidak cocok); dwelling dan ambang gerak perlu kalibrasi ulang per kelompok usia. Ini bisa Anda angkat jadi **kontribusi riset eksplisit**: "kalibrasi parameter sensing RuView untuk populasi anak SLB".
- **Perilaku atipikal tidak ada di data latih mana pun** (MM-Fi = dewasa neurotipikal): stimming/autoregulasi bisa terdeteksi sebagai "anomali" → fitur deteksi dini ATAU alarm palsu. Desain eksperimen + pelibatan guru/pendamping menentukan mana.
- **Privasi = argumen utama**: tanpa kamera di ruang kelas anak berkebutuhan khusus justru keunggulan etis; privacy mode bawaan + "identitas tidak terdeteksi dari WiFi" (terukur: gap 0,0005) adalah temuan yang MENGUNTUNGKAN proposal Anda.
- **Kebaruan:** aplikasi WiFi CSI pada ruang kelas pendidikan inklusi/SLB — perlu cek Scopus/DBLP (label SEARCH-LIMITED sampai dicek, disiplin yang sama dengan garis BISINDO). Literatur CSI classroom umum ada (occupancy/counting), tapi SLB-specific kemungkinan kosong.

### 3.3 Kandidat judul (draft — masih perlu dicek kebaruan + disepakati pembimbing)
1. ⭐ **Sistem Pemantauan Aktivitas dan Keselamatan Siswa Kelas SLB Berbasis Wi-Fi Channel State Information pada ESP32: Studi Kelayakan Tanpa Kamera**
2. **Deteksi Jatuh dan Anomali Aktivitas Siswa Berkebutuhan Khusus Berbasis Wi-Fi CSI pada Ruang Kelas: Studi Kelayakan Pemantauan Privasi-Preservasi**
3. **Kalibrasi Parameter Wi-Fi Sensing untuk Pemantauan Aktivitas Anak Berkebutuhan Khusus pada Ruang Kelas SLB Berbasis ESP32**

---

## 4. ALAT 3 — WiFi CSI Kamar Asrama SLB (Pemantauan Malam)

### 4.1 Fitur RuView yang dipakai
| Fitur RuView | Fungsi untuk alat ini | Perubahan kode |
|---|---|---|
| `someone_sleeping` FSM (F1 0,84 held-out) | Status sedang tidur | Tidak ada (asumsi 1 penghuni/kamar) |
| Breathing rate (0,1–0,5 Hz) | Pemantauan napas saat tidur | **Cek tepi band untuk anak** (18–25 BPM dekat batas atas 30) |
| `no_movement` + `elderly_anomaly` | Deteksi anak tidak bergerak terlalu lama / anomali inaktivitas malam | Threshold disetel ulang |
| `vital_trend` (tren mingguan BR) | Laporan tren kesehatan ke asrama | Tidak ada |
| `scripts/sleep-monitor.js` (hipnogram) + `apnea-detector.js` | Dashboard skrining tidur | Tidak ada (demo, disclaimers lengkap) |
| Apnea screening (`med_sleep_apnea`, AHI proxy) | **Eksperimental** — gated `medical-experimental` | Hanya bila dikompilasi dengan fitur khusus; jangan dijanjikan |
| OTA + node hemat daya (C6 LP-core, belum tervalidasi) | Deployment malam multi-kamar | C6 TWT/5 µA = klaim belum divalidasi hardware |

### 4.2 Masalah & batas yang harus jujur di proposal
- **Satu penghuni per kamar adalah asumsi keras** — WiFi tidak bisa membedakan identitas (terukur), dan bila 2 anak tidur dalam satu kandang sinyal, superposisi = masalah terbuka (out-of-scope Spec Anda pun sudah menulis ini untuk multi-penandatangan BISINDO — prinsip sama).
- **Skrining, bukan diagnosis**: sleep-stage & apnea di RuView eksplisit "not validated, bukan alat medis". Framing proposal wajib: "sistem peringatan dini untuk pendamping", bukan "alat kesehatan".
- **Privasi ruang tidur anak** = sensitivitas etis tertinggi dari ketiga alat: persetujuan orang tua/wali + asrama + anonimisasi + hak menarik diri; posisi sistem sebagai deteksi kondisi BUKAN pengawasan perilaku harus eksplisit (RUView sendiri tidak bisa identifikasi individu — pakai itu sebagai bukti desain privasi).
- **Kebaruan:** perlu cek literatur (WiFi CSI sleep monitoring = area ramai: Wi-Sleep, dkk.; tapi konteks asrama SLB/peduli kebutuhan khusus kemungkinan kosong — label SEARCH-LIMITED).

### 4.3 Kandidat judul (draft)
1. ⭐ **Sistem Pemantauan Pola Tidur dan Deteksi Anomali Nocturnal Siswa Asrama SLB Berbasis Wi-Fi CSI pada ESP32: Studi Kelayakan Non-Kontak Tanpa Kamera**
2. **Pemantauan Laju Napas dan Status Tidur Tanpa Kontak untuk Pendampingan Siswa Asrama SLB Berbasis Wi-Fi Channel State Information**
3. **Studi Kelayakan Wi-Fi Sensing untuk Sistem Peringatan Dini Kondisi Malam Siswa Berkebutuhan Khusus pada Asrama SLB**

---

## 5. Matriks Pemetaan Fitur RuView × 3 Alat (ringkasan satu halaman)

| Fitur RuView | 🐔 Kandang | 🏫 Kelas SLB | 🛏 Asrama SLB | Status jujur |
|---|---|---|---|---|
| Capture CSI + UDP ADR-018 | ✅ inti | ✅ inti | ✅ inti | MEASURED |
| Presence heuristik | ✅ (kipas = risiko FP) | ✅ | ✅ | MEASURED, FP di fan/microwave |
| Motion / indeks aktivitas | ✅ **inti** | ✅ inti | ◐ | Real-time |
| Breathing rate | ◐ perlu ubah band; tepi band unggas | ◐ tepi band anak | ✅ (cek anak) | MEASURED utk dewasa |
| Heart rate | ❌ mustahil (250–330 BPM di luar band) | ❌ tidak relevan | ◐ dewasa saja | MEASURED utk dewasa 40–120 |
| Fall detection | ❌ | ✅ **inti** | ◐ | MEASURED <200 ms |
| Sleeping FSM / hipnogram | ❌ | ❌ | ✅ **inti** | F1 0,84 held-out |
| No-movement / inactivity anomaly | ✅ (stillness) | ✅ | ✅ **inti** | FSM real, threshold perlu setel |
| Distress / panic motion | ◐ | ✅ | ✅ | FSM real, tidak diklinis |
| Livestock monitor (stillness/escape/labored) | ✅ **template alert** | ❌ | ❌ | DSP real, validasi hewan = nol |
| Person counting | ◐ (kawanan ≠ counting per-ekor) | ◐ kasar | ◐ | LEMAH (degradasi >2–3) |
| Pose 17-keypoint | ❌ | ❌ | ❌ | **STUB** (PCK@20 3,0%, confidence=0) |
| Kalibrasi ruangan 600 frame + 8 anchor | ✅ wajib | ✅ wajib | ✅ wajib | Real, ±4 menit/ruang |
| Record→train adaptive classifier | ✅ | ✅ | ✅ | Real <1 dtk |
| MQTT/HA + privacy mode | ✅ | ✅ **penting** | ✅ **penting** | MEASURED |
| mmWave fusion (MR60/LD2410) | ◐ opsi andal | ◐ | ◐ | Real |
| Sleep-stage/apnea klinis | ❌ | ❌ | ◐ skrining saja | EKSPERIMENTAL, tak tervalidasi |

Legenda: ✅ pakai langsung · ◐ pakai dengan penyesuaian/kondisi · ❌ tidak dipakai/terlarang diklaim

---

## 6. Rekomendasi Keputusan (jujur, bukan memanjakan)

**Faktor yang saya timbang:**
1. **Kesiapan bukti:** garis ayam sudah punya 10 referensi terverifikasi + sidang dewan LLM + verdict reformulasi + protokol uji Delta-CSI siap jalan. Garis SLB (kelas/asrama) masih perlu riset literatur dari nol (cepat, tapi belum ada).
2. **Kesesuaian dengan kemampuan RuView:** kelas SLB & asrama SLB adalah fit terbaik (fitur-nya sudah MEASURED); kandang ayam punya hambatan fisika ekstra (dilusi kawanan) yang TIDAK diselesaikan RuView.
3. **Risiko sidang:** garis ayam punya protokol go/no-go minggu-1 yang elegan (fallback "studi kelayakan tetap menghasilkan temuan"). Garis SLB punya fallback serupa (threshold calibration untuk populasi anak sebagai temuan).
4. **Bobot praktikal alat 2 vs 3:** kelas SLB lebih mudah izinnya daripada asrama malam (ruang tidur anak); kandang ayam paling mudah aksesnya (milik sendiri/komunitas?).

**Tiga skenario yang masuk akal:**
- **Skenario A (nilai riset tertinggi, risiko fisika tertinggi):** garis ayam dengan judul Opsi-1 dewan + RuView sebagai infrastruktur. Uji Delta-CSI minggu ini tetap gerbang pertama.
- **Skenario B (fit terbaik RuView, izin paling mudah):** ruang kelas SLB — presence/fall/anomali + kalibrasi populasi anak sebagai kontribusi; kebaruan perlu diverifikasi dulu (Scopus/DBLP).
- **Skenario C (gabungan paling elegan secara "satu platform"):** satu skripsi studi kelayakan platform WiFi-CSI ESP32 dengan SATU kasus utama + dua deployment sekunder ringan — hati-hati: ini risiko scope creep yang pernah dihukum dewan pada garis ayam; hanya layak bila pembimbing setuju dan kasus sekunder benar-benar ringan (mis. uji instrumen 2 minggu, bukan eksperimen penuh).

**Saran konkret untuk pengajuan proposal Anda:** siapkan **1 judul utama + 2 alternatif** (format yang diminta kampus biasanya), dengan pasangan (judul, fitur RuView, RQ, metrik, fallback) per opsi — tabel di §2.4/§3.3/§4.3 tinggal dipakai. Untuk itu saya sarankan urutan prioritas: **(1) kelas SLB jika data sekolah mudah diakses; (2) ayam broiler versi Opsi-1 dewan; (3) asrama SLB** — dan jalankan dua pemeriksaan murah SEBELUM fix: (a) cek Scopus/DBLP untuk "WiFi CSI classroom/SLB", (b) uji Delta-CSI fisik 2×ESP32 di lokasi target (kerja Minggu-1, berlaku untuk SEMUA garis karena platformnya sama).

---

## 7. Langkah Berikutnya yang Disarankan (urut biaya murah→mahal)

1. **Cek kebaruan** Scopus/DBLP/Google Scholar: "WiFi CSI classroom", "WiFi sensing special education", "CSI sleep dormitory" (jam pertama, gratis). Saya bisa bantu jalankan jika diminta.
2. **Beli 2× ESP32-S3** (±Rp500 rb) → flash release binary RuView v0.8.8 → uji presence/motion di: kandang (kosong vs 10 ekor bergerak), kelas kosong vs terisi, kamar siang vs malam. Satu sore per lokasi. Ini uji Delta-CSI yang dewan tuntut — platform sama, jadi sekali uji menguntungkan ketiga opsi.
3. Kalau go: **kunci judul dengan pembimbing** dari kandidat §2.4/§3.3/§4.3, lalu jalankan skill `to-tickets` atas Spec untuk pecah jadi tiket.
4. Kontak etika: sekolah SLB / puskeswan — jangan sampai minggu ke-4.
