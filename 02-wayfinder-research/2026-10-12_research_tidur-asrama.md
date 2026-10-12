# Hasil Riset — Kebaruan WiFi-CSI Tidur/Asrama & Rentang Vital Anak

> Resolusi tiket [wayfinder #3](https://github.com/ILoveTahuTek/skripsi/issues/3) · 2026-10-12 · Method: skill web-search, 28 query (24 efektif, EN+ID) · Agent riset AFK
> **Evidence-state klaim: SEARCH-LIMITED** untuk gap (akses web umum; verifikasi Scopus/IEEE Xplore wajib sebelum klaim ditulis).

## Metode pencarian

±24 query efektif via web-search (EN + ID). Query kunci: "Wi-Sleep CSI contactless sleep monitoring", "WiFi sensing child respiration breathing rate children", "CSI breathing rate children WiFi sensing pediatric", "WiFi sensing dormitory student sleep", "Fleming normal ranges heart rate respiratory rate children Lancet", "pediatric vital signs reference card PALS", "sleeping respiratory rate normal children school age", "pemantauan tidur WiFi tanpa kontak channel state information skripsi", "contactless heart rate children WiFi CSI", "apnea deteksi napas bayi WiFi sensor tanpa kontak", dsb.

## Temuan kelompok (a) CSI sleep/vitals dewasa

| Judul | Penulis/Tahun | Venue/Sumber | Ringkasan |
|---|---|---|---|
| Wi-Sleep: Contactless Sleep Monitoring via WiFi Signals | X. Liu et al., 2014 (~422 sitasi) | IEEE | Pionir: CSI WiFi off-the-shelf untuk napas/gerakan/bangun saat tidur. |
| Tracking Vital Signs During Sleep Leveraging Off-the-shelf WiFi | J. Liu et al., 2015 (~654 sitasi) | Rutgers WINLAB | Napas + detak jantung saat tidur, WiFi komoditas, tanpa wearable. |
| Monitoring Vital Signs and Postures During Sleep Using WiFi Signals | J. Liu et al., 2018 (~287 sitasi) | IEEE | Napas, HR, pola/postur tidur dengan 1 pasang WiFi + AP. |
| Sleep Monitoring Using WiFi Signal (review) | X. Wang et al. | bab buku Auburn | Review teknik tidur RSS & CSI. |
| On CSI-Based Vital Sign Monitoring Using Commodity WiFi | X. Wang et al., 2020 (~153 sitasi) | Auburn | Eksperimen 4 orang, 3 bulan, indoor nyata. |
| A survey on vital signs monitoring based on Wi-Fi CSI data | J.C.H. Soto et al., 2022 (~68 sitasi) | PMC (NCBI) | Survei; menegaskan WiSleep sebagai karya pertama RR tidur berbasis CSI. |
| Contactless Respiration Monitoring During Sleep with a pair of WiFi devices | H. Zhuo et al., 2022 | Harvard/ADS | Pasangan perangkat WiFi, CSI fine-grained untuk RR tidur. |
| Sleep Stage Monitoring Using Commodity Wi-Fi ("WiFi-Sleep") | — | Semantic Scholar | Sleep staging deep learning dengan WiFi komoditas. |
| Attention-based Learning for Sleep Apnea and Limb Movements (WiFi CSI) | 2023 | alphaxiv | CSI untuk napas + gerakan tubuh, apnea & limb movement. |
| Wi-Fi CSI Sensing for Sleep Disturbances in the Care of Older People | Sep 2024 | IEEE DataPort | **Dataset publik** CSI gangguan tidur lansia. |
| VitalCSI: Contactless Respiratory Rate Estimation | T. Michaelis et al., 2025 (~5 sitasi) | MDPI | AP WiFi + RPi; **118 partisipan 18–64 th (semua dewasa)**. |
| Non-Contact Heart Rate Monitoring Method Based on Wi-Fi CSI | J. Sun et al., 2024 (~21 sitasi) | PMC | HR non-kontak berbasis CSI. |
| PulseFi | Okt 2025 | arXiv | ML murah untuk HR + RR via WiFi. |
| UCSC WiFi heart rate (118 partisipan) | Sep 2025 | news.ucsc.edu | HR via CSI single-antenna; semua dewasa. |
| Survei contactless vital sign monitoring | M.S. Raheel et al., 2024 | ScienceDirect | Survei sistem vital non-kontak (WiFi/radar). |

**Kesimpulan (a): aktif 2014→2025, matang, mayoritas/eksklusif partisipan DEWASA.**

## Temuan kelompok (b) anak / kebutuhan khusus

| Judul | Tahun/Sumber | Populasi | Ringkasan |
|---|---|---|---|
| WiFi-Based Robust Child Presence Detection (motion + breathing) | 2023, sigport | Anak | Deteksi kehadiran anak: akurasi 99%, FA 3% — bukan studi tidur/asrama. |
| Wi-Fi sensing Child Presence Detection (CPD) | 2021, Murata | Anak | Solusi komersial deteksi napas/gerak anak (konteks kabin mobil). |
| In-Vehicle Breathing Rate Monitoring Based on WiFi Signals | — | Anak | Detection rate anak 91,45%, FA 6,14% — konteks mobil. |
| Noncontact Infant Apnea Detection for Hypoxia Prevention | L. Wen et al., 2024 (~22 sitasi), PubMed 37851550 | Bayi | Apnea non-kontak + algoritma adjustable; modality perlu cek. |
| Contactless Respiration Monitoring using Wi-Fi and AI | P. Kontou et al. (~25 sitasi), Heriot-Watt | Dewasa, membahas bayi | Menyebut RR bayi sampai 55 BPM (0,92 Hz) sebagai alasan desain filter. |
| Real Time Apnoea Monitoring of Children Using Microsoft Kinect | A. Al-Naji et al., 2017 (~124 sitasi) | Anak/bayi | Apnea anak real-time — berbasis KAMERA. |
| Sensing Technologies for Autism Spectrum Disorder (review) | J.J. Cabibihan et al., 2016 (~107 sitasi) | ASD | Review sensor ASD — didominasi wearable/vision. |
| NeuroSense / wearable stress sensors for children with autism | 2016–2026 | ASD | Monitoring perilaku/stres anak ASD — wearable. |
| Wireless Sensing-based Daily Activity Tracking (senior housing) | M. Touhiduzzaman et al., 2024 | Lansia | WiFi sensing di senior housing (dewasa tua). |
| A Contactless Health Monitoring System for the Nursing Home | S.I. Lopes et al., 2024 | Lansia | Vital non-kontak nursing home. |
| Monitoring the Sleep Respiratory Rate with Microcontroller Wi-Fi | R. Burimas, 2023, tesis Thammasat | Umum | RR tidur via WiFi CSI untuk sleep apnea. |

**Kesimpulan (b): TIDAK DITEMUKAN satu pun studi WiFi-CSI tidur pada anak usia sekolah, dan tidak ada studi WiFi-CSI di asrama kebutuhan khusus (24 query).** Karya "dormitory" yang ada (SleepMore 2023, Packets-to-Prediction 2023) memakai TRAFIK jaringan WiFi, bukan CSI, pada mahasiswa.

## Temuan kelompok (c) rentang vital anak

| Sumber medis | RR (BPM) per usia | HR (BPM) per usia |
|---|---|---|
| **Fleming et al., Lancet 2011;377:1011** (systematic review, 69 studi) | Median RR 44 (lahir) → 26 (2 th); tabel centile per usia (paywalled) | Tabel centile 0–18 th (paywalled) |
| **Herbert et al. 2020** (PMC) | Median RR **tidur** 41,4 (bayi) → 22,0 (3 th); RR tidur < RR bangun | — |
| **PALS/AHA 2015** (kartu vital) | — | **School-age (6–12 th) bangun: 75–118**; Toddler 98–140; Preschool 80–120; Adolescent 60–100 |
| **ACLS Medical Training (2021)** | Preschool 4–5 th: 22–34; **School age 6–12 th: 18–30**; Adolescent: 12–16 | — |
| **Sleep Foundation (2025)** — tidur | **Anak 6–12 th: 18–30**; remaja 13–17: 13–21 | — |
| **SleepApnea.org** — tidur | Toddler 25–46; 2–3 th 22–34; 3–6 th 20–29 | — |
| **Lotus Medical (AU, 2023)** — tidur | 6–12 th: ±15–30 | — |
| **Cleveland Clinic (2022)** | 0–3 bln 30–60; … 1–3 th 20–30 | Newborn 110–160 |
| **Don't Forget The Bubbles** | 10–14 th: 16–20 (bangun) | 10 th: 70–110; 12 th: 60–110 |

## Verdict evidence-state + kelayakan band

**Klaim 1 — "WiFi-CSI sleep monitoring dewasa sudah ramai": VERIFIED.** Rantai bukti 2014→2025 kontinu; kebaruan tidak boleh ditaruh di "CSI tidur dewasa".

**Klaim 2 — "WiFi-CSI konteks anak/kebutuhan khusus asrama masih kosong": SEARCH-LIMITED** (condong kuat ke "kosong/lubang riset"). Tidak ada satu pun studi WiFi-CSI **tidur** pada anak usia sekolah dan tidak ada di **asrama kebutuhan khusus**; tetangga terdekat: child presence detection, deteksi napas anak dalam mobil, apnea bayi non-kontak, WiFi sensing lansia. Wajib cek ulang Scopus/IEEE Xplore ("child"/"adolescent"/"special education"/"dormitory" + "channel state information") sebelum klaim gap ditulis.

**Apakah band bawaan 0,1–0,5 Hz (6–30 BPM) memadai untuk anak sekolah tidur (6–12+ th)?**
**Sebagian besar YA, tapi tepi atas kritis.** RR tidur anak 6–12 th = **18–30 BPM** (Sleep Foundation; sumber lain 15–30), nilai khas tidur ≈15–25 BPM (0,25–0,42 Hz) jatuh aman di tengah band. Namun: (1) batas atas normal tidur (30 BPM = 0,50 Hz) **tepat di tepi** filter — takipnea ringan >30 BPM akan teredasi/dianggap noise; (2) untuk anak lebih muda (3–6 th 20–29; toddler sampai 46 BPM ≈ 0,77 Hz; bayi sampai 55–60 BPM) band ini TIDAK memadai. **Rekomendasi:** jika target anak usia sekolah, pertahankan 0,1 Hz tapi **naikkan tepi atas ke ±0,66–0,77 Hz (40–46 BPM)** sebagai margin, atau band adaptif per usia; dokumentasikan bahwa 0,5 Hz hanya aman untuk dewasa/remaja.

## Implikasi untuk skripsi

Gap yang tampak nyata: aplikasi WiFi-CSI tidur pada **populasi anak/kebutuhan khusus di asrama** — seluruh literatur CSI tidur kuat berbasis dewasa; framing kebaruan sebaiknya di situ, bukan pada teknik dasar. Selaraskan parameter sinyal dengan fisiologi anak (RR tidur 18–30 BPM → pertimbangkan perlebar band napas >0,5 Hz; HR bangun school-age 75–118 BPM ≈ 1,25–1,97 Hz untuk jalur jantung). Gunakan Fleming 2011 (Lancet) dan Herbert 2020 sebagai rujukan rentang vital anak, bukan blog kesehatan.

## Keterbatasan

1. Mesin pencari tidak stabil utk query teknis panjang (5–6 query gagal, 1 no-results) → temuan negatif bisa artefak indexing (SEARCH-LIMITED).
2. DOI/venue persis tak muncul di snippet → tidak dicantumkan; angka sitasi dari snippet (bisa usang). Lancet 2011 & Herbert 2020 paywalled.
3. Beberapa nilai tabel (c) terpotong di snippet; situs kesehatan populer dipisahkan dari sumber primer (Lancet, PALS).
4. Pencarian Indonesia nyaris nihil untuk CSI (hanya sensor kontak) — temuan tersendiri, tapi bisa juga indeksasi buruk.
