# Hasil Riset — Kebaruan WiFi-CSI Kelas SLB

> Resolusi tiket [wayfinder #2](https://github.com/ILoveTahuTek/skripsi/issues/2) · 2026-10-12 · Method: skill web-search, 33 upaya query (~20 efektif, EN+ID) · Agent riset AFK
> **Evidence-state klaim: SEARCH-LIMITED** (akses web umum saja; verifikasi Scopus/WoS penuh masih wajib sebelum klaim gap ditulis di proposal).

## Metode pencarian

Tool: web-search (z-ai CLI). Query efektif utama:

**Inggris:**
1. "WiFi sensing classroom activity recognition channel state information"
2. `"WiFi CSI" classroom occupancy counting students`
3. `device-free crowd counting classroom WiFi RSSI CSI`
4. `WiFi sensing teacher activity classroom lecture detection`
5. `"WiFi sensing" "special education" classroom`
6. `"channel state information" autism stereotypic behavior recognition radar`
7. `WiFi CSI fall detection elderly school classroom`
8. `WiFi CSI student engagement attention classroom detection`
9. `"WiFi sensing" "children with autism" contactless detection`
10. `WiFi CSI stereotypy stereotypic movement detection wireless signal`
11. `"WiFi sensing" "special needs" OR "special school" students monitoring`
12. `mmWave radar autism classroom stereotypic behavior monitoring`
13. `arxiv WiFi sensing classroom occupancy teacher student activity recognition`
14. Verifikasi judul spesifik: "A Framework to Estimate Classroom Occupancy using WiFi", "Enabling Smart Classrooms...", "Monitoring Engagement in Online Classes Through WiFi CSI"
15. `WiFi CSI wheelchair activity assistive sensing rehabilitation`

**Indonesia:**
16. "WiFi sensing ruang kelas deteksi kehadiran siswa penelitian"
17. "CSI Wi-Fi pengenalan aktivitas manusia jurnal Indonesia skripsi"
18. "SLB sekolah luar biasa sensor deteksi aktivitas IoT" / "teknologi sensor WiFi sekolah luar biasa SLB" / "WiFi sensing anak berkebutuhan khusus deteksi gerakan jurnal Indonesia" → tidak menghasilkan situs ilmiah relevan (kebanyakan absensi QR/fingerprint/PIR).

## Temuan kelompok (a) WiFi-CSI classroom umum

| Karya | Tahun | Venue | DOI/URL | Ringkas |
|---|---|---|---|---|
| S. Mondal dkk., *A Framework to Estimate Classroom Occupancy using WiFi Channel State Information* | 2023 | ICCIT, IEEE | ieeexplore.ieee.org (DOI tidak terlihat) | Estimasi okupansi kelas nyata dari CSI; device-free. |
| V.K. Singh, P. Kar, M. Maity dkk., *Monitoring Engagement in Online Classes Through WiFi CSI* | 2023 | IEEE conf. | ieeexplore.ieee.org / semanticscholar.org | Engagement via gerak kepala dari waveform CSI ESP32; privacy-preserving. |
| *Modeling Classroom Occupancy Using Data of WiFi* (judul terpotong) | t.a. | Semantic Scholar | semanticscholar.org | Model ML infer okupansi kelas dari WiFi sensing. |
| H. Choi dkk., *Wi-CaL: WiFi Sensing and ML Based Device-free Crowd Counting and Localization* | 2022 | IPSN | catalog.lib.kyushu-u.ac.jp | Crowd counting device-free hingga 10 orang, ~55% count accuracy. |
| R. Zhou dkk., *Device-free crowd counting with WiFi CSI* | 2020 | ACM | dl.acm.org | Inferensi jumlah orang dari satu pasang TX-RX CSI. |
| R.F. Brena dkk., *Device-Free Crowd Counting Using Multi-Link Wi-Fi CSI* | 2021 | MDPI Sensors | mdpi.com | Crowd counting multi-link; membahas FreeCount. |
| B. Korany dkk., *Counting a Stationary Crowd Using Off-the-Shelf WiFi* | 2021 | IEEE | par.nsf.gov | Menghitung orang yang diam dari bandwidth CSI. |
| Y. Ma, G. Zhou dkk., *WiFi Sensing with Channel State Information: A Survey* | 2019 | ACM Computing Surveys | gzhou.pages.wm.edu | Survey pangkal WiFi-CSI (sudah jadi ref #1 laporan dewan garis ayam). |
| S. Yousefi dkk., *A Survey of HAR Using WiFi CSI* | 2017 | arXiv | arxiv.org | Survey awal behavior recognition pasif indoor berbasis CSI. |
| E. de Armas dkk., *EHUNAM, a WiFi CSI-based dataset* | 2025 | Nature Scientific Data | nature.com | Dataset CSI publik untuk aktivitas/counting. |
| I. Picallo, E. Batista dkk., *Enabling Smart Classrooms with Connectivity and Sensing via Heterogeneous Wireless Systems* | 2026 (preprint) | Research Square | researchsquare.com | Smart classroom sensing nirkabel heterogen (belum peer-reviewed). |
| T.H. Tan dkk., *Intelligent Lecturer Tracking and Capturing System* | 2019 | MDPI | mdpi.com | Face detection + wireless sensing untuk lokalisasi dosen. |
| Vintea (skripsi S1), *Room occupancy analysis using Wi-Fi CSI* | t.a. | Univ. Twente | essay.utwente.nl | CSI akurat untuk estimasi okupansi ruangan. |

**Simpulan (a):** literatur WiFi-CSI *untuk kelas* ada namun **tipis** — didominasi okupansi/crowd counting dan satu-dua karya engagement; jauh lebih sedikit dibanding HAR umum.

## Temuan kelompok (b) konteks special education / SLB

| Karya | Tahun | Venue | Ringkas |
|---|---|---|---|
| C.M.V. Wong dkk., *Enhanced Applied Behavior Analysis (ABA) for Special Education* | 2021 | MDPI | IoT untuk terapi ABA di kelas SEN — bukan WiFi-CSI (sensor IoT lain); karya terdekat di kelas pendidikan khusus. |
| *Simulation-Based Smart Home Architecture for Autism Support* | t.a. | IEEE MASS | Smart-home autisme mengadaptasi konsep WiFi-CSI activity recognition — konteks rumah, bukan kelas. |
| A.M. Amiri dkk., *WearSense: Detecting Autism Stereotypic Behaviors through Smartwatch* | 2017 | PMC | Deteksi stereotypi autisme via smartwatch (wearable, bukan RF) — metrik/target perilaku bisa ditiru CSI. |
| *Detecting stereotypical motor movements in the classroom* | t.a. | ResearchGate | Deteksi SMM anak autisme di kelas dengan sensor wearable — bukan device-free. |
| *WiFi CSI Dataset of Patients with Gait-Affecting Disorders* (UCSB) | t.a. | web.ece.ucsb.edu | Dataset CSI 234 langkah, 114 partisipan termasuk gangguan bunjang — populasi disabilitas, konteks lab. |
| *Patient Behavior Recognition Methods Based on WIFI-CSI* | t.a. | Springer | Pengenalan perilaku pasien via WiFi-CSI — konteks perawatan. |
| *Human Perception Recognition Based on CSI… Monitoring Sensitive Populations* | t.a. | SCITEPRESS | CSI untuk pemantauan "populasi sensitif". |

**Simpulan (b):** Tidak ada satu pun publikasi yang ditemukan menerapkan WiFi-CSI di ruang kelas SLB. Query Indonesia (`SLB`, `sekolah luar biasa`, `anak berkebutuhan khusus` × WiFi/CSI) nihil — karya Indonesia yang muncul (absensi QR/sidik jari/PIR) bukan sensing RF.

## Temuan kelompok (c) tetangga terdekat

| Karya | Tahun | Venue | Ringkas |
|---|---|---|---|
| Z. Zhou dkk., *TCS-Fall: Cross-individual fall detection (WiFi CSI)* | 2024 | PMC | Deteksi jatuh lintas-individu dari CSI. |
| Y. Hu dkk., *Mobile receiver WiFi-CSI fall detection for construction workers* | 2025 | ScienceDirect | Jatuh pekerja, smartphone sebagai penerima. |
| Preechakarnjanadit dkk., *Real-Time Non-Intrusive Fall Detection via Wi-Fi CSI* | 2025 | IntechOpen | HAR CSI untuk deteksi jatuh non-kontak. |
| H. Jiang dkk., *Smart Home Based on WiFi Sensing: A Survey* | 2018 | IEEE | Survey health monitoring WiFi sensing. |
| M. Touhiduzzaman dkk., *Wireless Sensing-based Daily Activity Tracking for older adults* | 2024 | PMC | Tracking aktivitas lansia non-invasif. |
| L. Monti dkk., *Edge-Based Transfer Learning for Classroom Occupancy* | 2022 | Sensors/PMC | Okupansi kelas pakai KAMERA + RPi — pembanding modalitas. |
| Z. Trabelsi dkk., *Real-Time Attention Monitoring System for Classroom* | 2023 | MDPI | Attention kelas berbasis visi-AI. |
| R. Yuvaraj dkk., *Automated Recognition of Teacher and Student Activities* | 2024 | IEEE Access | Deep learning aktivitas guru-murid (visi). |
| A. Ogan, *Reframing classroom sensing: Promise and peril* | 2019 | ACM Interactions | Kritik etika/privasi classroom sensing (kamera/mikrofon) — argumen kuat mengapa WiFi-CSI menarik untuk kelas. |
| Karya Indonesia: Ibrahim (UGM), Pahlevi, Kurniawati (Prosiding PNJ), dsb. | 2023–2026 | etd.ugm.ac.id; journal.aptii.or.id; prosiding.pnj.ac.id | WiFi-CSI di Indonesia hanya HAR umum — belum menyasar kelas, apalagi SLB. |

## Verdict evidence-state

1. **"WiFi-CSI classroom umum sudah ada"** → **VERIFIED** (Mondal ICCIT 2023; Singh 2023; Wi-CaL IPSN 2022; Zhou 2020; Brena 2021; survey Ma & Zhou 2019). Catatan: jumlahnya tipis dan didominasi okupansi/counting.
2. **"WiFi-CSI pada kelas SLB/special-education kosong"** → **SEARCH-LIMITED** (condong kuat ke "kosong"): nihil positif di ~20 query efektif EN+ID, tetangga terdekat di modality lain. "Tidak ditemukan" lewat mesin pencari umum ≠ absensi terverifikasi → wajib cek Scopus/WoS sebelum klaim gap. Rumuskan sebagai "belum ditemukan pada penelusuran ini", bukan "tidak ada".

## Implikasi untuk skripsi

Celah cukup jelas: WiFi-CSI kelas umum (okupansi/engagement) sudah ada sebagai fondasi metodologis, tapi belum ada yang menerapkan pada ruang kelas SLB (internasional maupun Indonesia). Skripsi bisa memposisikan diri sebagai studi pertama (to our searched knowledge) penerapan device-free WiFi sensing di kelas SLB — deteksi kehadiran/aktivitas/stereotypi motorik tanpa kamera, dengan privacy-preserving sebagai argumen utama (relevan mengingat sensitivitas kamera pada anak pendidikan khusus). Fondasi teknis tersedia (ESP32 CSI, dataset EHUNAM/Wi-CaL, survey Ma & Zhou 2019) → risiko metodologis rendah, kebaruan di konteks + validasi lapangan.

## Keterbatasan

- Hanya mesin pencari web umum + agregator; tanpa akses Scopus/WoS/EBSCO penuh → absensi tak terverifikasi menyeluruh (SEARCH-LIMITED).
- Sebagian besar snippet tidak menampilkan DOI → cek landing page sebelum dikutip di skripsi.
- Noise query (kolisi kata: "classroom"→Google Classroom; "CSI"→ institusi/forensik).
- Beberapa hasil preprint/skripsi (kualitas evidence lebih rendah).
- Tanpa penelusuran cite-graph. Saran lanjutan untuk mahasiswa (punya akses kampus): Scopus/IEEE Xplore dengan kata kunci: "RF sensing" + "classroom" + ("autism" OR "special education" OR "SEN" OR "intellectual disability").
