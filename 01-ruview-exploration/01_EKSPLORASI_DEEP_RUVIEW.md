# EKSPLORASI DEEP-DIVE REPO RuView (github.com/ruvnet/RuView)

**Dibuat:** 2026-10-12 · **Metode:** clone repo penuh + baca README/PROOF/ADR-079 + audit menyeluruh firmware, Rust workspace (v2/), Python package, modul edge, dan dokumen kalibrasi.
**Versi repo saat dieksplorasi:** firmware v0.8.12, server v2 (Axum, ~60 crate Rust).
**Untuk:** pengambilan keputusan proposal skripsi — apa yang BISA dipakai, apa yang TIDAK BISA, apa yang harus DIUBAH.

---

## 1. Apa Itu RuView (Pemahaman Dasar yang Benar)

RuView adalah platform open-source yang mengubah sinyal Wi-Fi biasa menjadi "spatial intelligence" — kemampuan mendeteksi kehadiran orang, mengukur napas dan detak jantung, melacak gerakan, dan memantau ruangan **tanpa kamera dan tanpa wearable**. Caranya: saat sinyal Wi-Fi merambat, tubuh manusia yang bergerak atau bernapas memodulasi sinyal tersebut; modulasi ini terekam sebagai **Channel State Information (CSI)** — data per-subcarrier yang bisa dibaca dari mikrokontroler murah ESP32 (±Rp150 ribu/node). RuView menangkap CSI ini, mengolahnya dengan pipeline DSP (digital signal processing), dan menyajikannya lewat server REST + WebSocket + dashboard web + integrasi Home Assistant.

**Satu hal yang membedakan repo ini dari proyek "hype" lain:** RuView punya budaya "honest labeling" yang sangat ketat. Setiap klaim diberi label MEASURED (terukur), CLAIMED (dikutip), atau DATA-GATED/HARDWARE-GATED (kodenya nyata tapi akurasinya belum dibuktikan). Klaim-kclaim berlebihan versi lama ("100% presence", "94.2% pose") sudah ditarik kembali (retracted) secara terbuka. Bagi skripsi, ini berkuntang: kita TAHU persis batas kemampuan setiap fitur, dan ada dokumen `PROOF.md` yang bisa dijalankan sendiri untuk memverifikasi klaim.

**Posisi RuView yang benar untuk skripsi Anda:** RuView adalah **infrastruktur capture CSI + DSP dasar + integrasi alert** — BUKAN mesin pengenalan siap-pakai untuk kasus spesifik Anda. Anda akan memakai fondasinya (firmware, parsing, filter, kalibrasi, dashboard) lalu membangun lapisan eksperimen sendiri di atasnya. Ini justru ideal: user story #17 di Spec Anda sudah bilang "memakai infrastruktur capture CSI yang sudah teruji supaya waktu enam bulan habis untuk pertanyaan riset, bukan membangun driver dari nol."

---

## 2. Arsitektur & Aliran Data

```
[Router Wi-Fi / trafik tetangga]  ← iluminator "gratis"
        │ gelombang radio
        ▼
┌─────────────────────────────────────────────────────┐
│  ESP32-S3 / C6 (firmware C, ESP-IDF v5.4)           │
│  esp_wifi_set_csi_rx_cb() → callback CSI            │
│  ├─ Tier 1: capture mentah → serialize ADR-018      │
│  │    (header 20 byte + I/Q per subcarrier)         │
│  ├─ Tier 2: DSP on-node (core kedua):               │
│  │    • napas: bandpass 0.1–0.5 Hz + zero-crossing  │
│  │    • detak jantung: bandpass 0.8–2.0 Hz          │
│  │    • presence: varians fase + ambang adaptif     │
│  │      (kalibrasi ambient 60 dtk saat boot)        │
│  │    • jatuh: akselerasi fase + debounce 3 frame   │
│  └─ Tier 3 (alpha): runtime WASM3 → modul hot-swap  │
└────────────┬────────────────────────────────────────┘
             │ UDP :5005 (±20 fps S3 / 8 fps C6)
             ▼
┌─────────────────────────────────────────────────────┐
│  Sensing Server (Rust, Axum — v2/crates/…)          │
│  parse frame → fitur → vital signs (FFT/FIR) →      │
│  smoothing → person count → pose (heuristic/model)  │
│  ├─ REST ±40 endpoint (/api/v1/…)                   │
│  ├─ WebSocket /ws/sensing (broadcast JSON)          │
│  ├─ Dashboard web statis (ui/)                      │
│  ├─ MQTT → Home Assistant (21 entitas/node)         │
│  └─ 10 state semantik FSM (sleeping, distress, dst) │
└────────────┬────────────────────────────────────────┘
             ▼
[Python client / Node.js demo / Home Assistant / script alert Anda]
```

**Bahasa per bagian:** C (firmware ESP32) · Rust (seluruh stack server) · Python (binding tipis + klien WS/MQTT) · Node.js (demo skrining kesehatan).

---

## 3. INVENTARIS FITUR NYATA (terukur, bisa langsung dipakai/diandalkan)

Ini daftar yang **bisa Anda jadikan fondasi** dengan status sesuai label repo sendiri:

| # | Fitur | Status | Lokasi kode | Catatan penting |
|---|-------|--------|-------------|-----------------|
| 1 | **Capture CSI ESP32-S3/C6** + streaming UDP format ADR-018 | MEASURED (uji fleet 9-node) | `firmware/esp32-csi-node/main/csi_collector.c`; parser: `v2/crates/wifi-densepose-sensing-server/src/csi.rs` | Firmware punya release binary siap-flash; pipeline uji transport stabil (0 gagal kirim 5 menit) |
| 2 | **Deteksi presence** (heuristik varians fase + ambang adaptif 60 dtk) | MEASURED, tapi false-positive pada kipas/microwave | `edge_processing.c` (firmware) | Perlu kalibrasi ulang per ruangan; ini fitur paling tahan banting |
| 3 | **Estimasi laju napas** (bandpass 0.1–0.5 Hz, zero-crossing BPM, 6–30 BPM) | MEASURED untuk manusia dewasa | `v2/crates/wifi-densepose-vitals/src/breathing.rs`; Python: `BreathingExtractor` | "Experimental — kalibrasi terhadap referensi sebelum dipakai" |
| 4 | **Estimasi detak jantung** (bandpass 0.8–2.0 Hz, 40–120 BPM) | MEASURED untuk manusia | `heartrate.rs`; Python: `HeartRateExtractor` | **TIDAK berlaku untuk ayam** (ayam 250–330 BPM = 4,2–5,5 Hz, di luar band 2×) |
| 5 | **Deteksi jatuh** (akselerasi fase + debounce 3 frame + cooldown 5 dtk) | MEASURED (<200 ms) | firmware + `semantic/fall_risk.rs` | Threshold configurable; validasi pada kasus nyata tetap perlu |
| 6 | **Gerakan/aktivitas** (motion-band power + akselerasi fase) | Real-time | `motion.rs` (signal crate) | Cocok untuk indeks aktivitas — tanpa perlu model |
| 7 | **Pipeline DSP lengkap + bukti deterministik SHA-256** | MEASURED | `wifi-densepose-signal` (Hampel, SpotFi, Fresnel, BVP, STFT, normalisasi hardware); `archive/v1/data/proof/verify.py` | Bisa dijalankan: `python verify.py` → VERDICT: PASS — bagus untuk bab metode |
| 8 | **Sensing server REST + WebSocket + dashboard web** | MEASURED | `v2/crates/wifi-densepose-sensing-server` (main.rs 16.898 baris), `ui/` | Endpoint: `/api/v1/vital-signs`, `/api/v1/sensing/latest`, `/ws/sensing`, dll. |
| 9 | **Integrasi Home Assistant via MQTT (HA-DISCO)** — 21 entitas/node | MEASURED (benchmark 717 ns/tick) | `mqtt/discovery.rs`, `mqtt/publisher.rs` | Entitas: presence, person_count, breathing_rate, heart_rate, motion_level, fall, dst. |
| 10 | **10 state semantik FSM** (someone-sleeping, possible-distress, room-active, elderly-inactivity-anomaly, fall-risk-elevated, no-movement, dst.) | Real FSM; F1 0,63–0,98 pada subset held-out | `v2/crates/wifi-densepose-sensing-server/src/semantic/*.rs` | Lihat §5 — beberapa entitas tidak dipublikasikan karena belum punya sumber |
| 11 | **Pipeline kalibrasi ruangan** (baseline ruang kosong ≥600 frame + 8 anchor enrollment ±4 menit) | Real | `wifi-densepose-calibration`, `docs/calibration-guide.md` | Anchor: empty, stand_still, sit, lie_down, breathe_slow, breathe_normal, small_move, sleep_posture |
| 12 | **Workflow rekam→latih classifier adaptif** (record JSONL → logistic regression 15 fitur, <1 dtk) | Real (ADR-048) | `/api/v1/recording/*`, `/api/v1/adaptive/train` | Ini jalur TERGAMPANG untuk dataset percontohan Anda! |
| 13 | **Trainer model besar** (MM-Fi/Wi-Pose → RVF + LoRA per-ruangan) | Real, butuh GPU untuk training besar | `wifi-densepose-train` | Kemungkinan out-of-scope skripsi 6 bulan; pakai jalur #12 saja |
| 14 | **Encoder CSI pretrained** (128-dim, 82,3% temporal-triplet held-out) | MEASURED & dipublikasi | HuggingFace `ruvnet/wifi-densepose-pretrained` | Bisa jadi baseline fitur; catatan: file `model.safetensors` korup (#1522), pakai `csi-embed-v2.safetensors` |
| 15 | **±65 modul edge WASM real-DSP** (intrusion, occupancy, vital-trend, livestock-monitor, dll.) | Real DSP, status validasi per-modul (ADR-160) | `v2/crates/wifi-densepose-wasm-edge/src/` | Detail modul relevan di §5 |
| 16 | **OTA firmware dengan health-check rollback** | MEASURED | `ota_update.c`, RUNBOOK | Bagus untuk deployment lapangan |
| 17 | **Fusion mmWave + CSI** (Seeed MR60BHA2 60 GHz / HLK-LD2410 24 GHz via UART) | Real | `mmwave_sensor.c` (ADR-063) | Opsi andalan tambahan: mmWave jauh lebih andal untuk napas/jantung daripada CSI-only |
| 18 | **Privacy mode** (strip data biometrik dari MQTT/API) | Real | `mqtt/privacy.rs`, `privacy_filter.rs` | Penting untuk etika SLB — argumen privasi kuat di proposal |

---

## 4. INVENTARIS FITUR STUB / SIMULASI / EKSPERIMENTAL (jangan dijanjikan di proposal)

Bagian ini sama pentingnya dengan §3 — ini yang membuat proposal Anda defensibel di sidang:

1. **Pose 17-keypoint on-device TIDAK BEKERJA.** Bobot yang di-commit (`pose_v1.safetensors`) hanya mencapai PCK@20 = 3,0% (target ≥35%), dan jalur runtime-nya masih stub yang mengembalikan `confidence=0`. Angka 82,69% MM-Fi adalah model benchmark offline, bukan jalur live. Penyebab fisika: CSI satu antena ESP32 (56 subcarrier) tidak memuat informasi spasial halus untuk artikulasi tubuh/tangan. → **Konsekuensi:** jangan janjikan pose/gesture/handshape apa pun. Ini KONSISTEN dengan temuan riset BISINDO Anda sebelumnya (issue #509).
2. **Person counting lemah.** Firmware pakai heuristik "slot-capacity"; server pakai P95 normalisation ÷ dedup factor; model `cog-person-count` degenerate (65,1% akurasi, recall kelas-1 = 0%). Akurasi degradasi >2–3 subjek. → Hitungan orang = perkiraan kasar, bukan occupancy akurat.
3. **Presence false-positive** pada kipas, microwave, fluktuasi AP. Perlu kalibrasi ruang kosong ulang.
4. **Sleep-stage classification & apnea screening = heuristik tak tervalidasi.** `exo_dream_stage.rs` (Awake/Light/Deep/REM dari breathing-CV + motion + HRV) dan `med_sleep_apnea.rs` (BR<4 BPM >10 dtk) berlabel EKSPERIMENTAL, feature-gated `medical-experimental`, disclaimer "bukan alat medis". Tidak ada validasi polysomnografi di repo.
5. **6 dari 21 entitas HA tidak pernah dipublikasikan** (zone_occupancy, bathroom_occupied, bed_exit, multi_room_transition, meeting_in_progress, pose) — belum punya sumber data (issue #2085). Blueprint "bed-exit" HA terdokumentasi tidak akan menyala.
6. **`fall_risk_elevated` v1 = proxy kasar** dari jumlah jatuh 24 jam + varians gerak — bukan skor gait.
7. **Model loading punya celah:** HF `model.safetensors` NUL-padded (#1522); `model.rvf.jsonl` ditolak server; file quantized `model-q*.bin` belum ada reader-nya.
8. **Identitas personal dari WiFi: TIDAK tercapai** (gap 0,0005 — dua orang tak terpisahkan pada kanal WiFi-only; ini justru kabar baik untuk privasi SLB).
9. **Mode Docker tanpa hardware = data simulasi** (by design, berlabel `is_synthetic: true`).
10. **ADR-301 (autocal) & ADR-302 (OOD gating)** — arsitektur accepted, implementasi awal saja; belum jadi perilaku default.

---

## 5. Modul Edge ("Cogs") yang Paling Relevan untuk 3 Alat Anda

Dari ±65 modul real-DSP di `wifi-densepose-wasm-edge/src/` + FSM semantik server:

**Untuk ayam broiler:**
- `ind_livestock_monitor.rs` — satu-satunya modul animal-aware: presence hewan, deteksi stillness abnormal (≥5 menit, indikasi sakit), alert napas tertekan (debounce), alert kabur (hilang mendadak setelah presence terkonfirmasi). Rentang BPM napas per spesies: sapi 12–30, domba 12–20, **unggas 15–30** (custom range didukung). Status: DSP nyata, **validasi nol pada hewan**.
- Pola yang bisa ditiru: event ID 530–533 (present/stillness/labored/escape) → model alert Telegram Anda.

**Untuk ruang kelas SLB:**
- `occupancy.rs`, `room_active` (FSM), `sec_panic_motion.rs` (gerakan panik), `tmp_pattern_sequence.rs` (urutan pola), `intrusion.rs`.
- Fall detection (firmware + `fall_risk.rs`), `no_movement` (kelas biner 30 menit).
- Integrasi HA untuk notifikasi guru/wali (blueprint tersedia).

**Untuk kamar asrama SLB:**
- `someone_sleeping` (F1 0,84 — butuh availability BR), `no_movement`, `elderly_anomaly` (anomali inaktivitas — baseline v1 tidak persisten antar-restart), `vital_trend.rs` (tren BR/HR mingguan).
- `scripts/sleep-monitor.js` (hipnogram 5 menit/window, mode replay) + `scripts/apnea-detector.js` — demo skrining, disclaimers medis lengkap.
- `med_sleep_apnea.rs` (AHI proxy) — hanya bila di-compile dengan feature `medical-experimental`.

---

## 6. Kalibrasi & Adaptasi Ruangan (Krusial untuk Ketiga Alat)

Ini bagian yang harus Anda pahami dalam-dalam karena menentukan kelayakan lapangan:

1. **Baseline ruang kosong:** minimal **600 frame** (hard gate di `ruvsense/calibration.rs`), default 30 detik, durasi <10 detik ditolak. Praktiknya: kosongkan ruangan, jalankan `calibrate`.
2. **Enrollment 8 anchor** (±4 menit): empty → stand_still → sit → lie_down → breathe_slow → breathe_normal → small_move → sleep_posture. Ada quality gate (min 60 frame, presence z ≥ 1,5, dst.); anchor gagal diulang maks 2× lalu dilewati (set parsial tetap mungkin).
3. **Specialist bank:** dari anchor terlatih, sistem fit classifier presence / anomaly / restlessness / posture per ruangan.
4. **Bootstrap prior (ADR-355):** model ruang kosong hanya persist bila ≥1000 frame DAN ≥600 detik, dengan expiry 24 jam dan binding instalasi.
5. **Batas honest:** zero-shot cross-room/antar-orang RENDAH (studi MM-Fi: akurasi cross-environment runtuh ke ~17–64%); kalibrasi ~30 detik per ruangan adalah PRASYARAT setiap deployment. Untuk skripsi: rencanakan kalibrasi ulang per lokasi (kandang, kelas, kamar) dan catat sebagai bagian protokol.

---

## 7. Workflow yang Paling Realistis untuk Skripsi: Record → Train → Evaluate

Bukan training model besar, melainkan jalur "adaptive classifier" yang sudah terbukti jalan:

```
1. Flash firmware ke 2–4 ESP32-S3 (release binary tersedia, tak perlu build dari nol)
2. Jalankan sensing server (Rust, atau Docker)
3. Rekam data: POST /api/v1/recording/start → beri label kelas → stop
   (output: JSONL per kelas di data/recordings/)
4. Latih: POST /api/v1/adaptive/train  → logistic regression 15 fitur, <1 detik
5. Evaluasi: split blok-waktu & antar-penandatangan/subjek (lakukan SENDIRI
   di Python — jangan pakai split acak, ini jebakan time-series leakage)
```

Alternatif lebih "murni riset": lewati model server, simpan JSONL mentah, dan buat pipeline Python Anda sendiri (Hampel → bandpass → windowing → fitur statistik/spektral → kNN/SVM di Colab) — persis seperti Spec_Eksekusi Anda. RuView tetap berguna sebagai alat capture + ground truth sinkron.

**Ground truth:** video kamera hanya untuk pelabelan saat pengumpulan data (konsisten dengan keputusan Spec Anda). ADR-079 RuView sendiri memakai pola ini: kamera + MediaPipe sebagai "guru" saat training, dibuang saat deployment.

---

## 8. Keterbatasan Fisika untuk Ayam Broiler (PENTING — baca sebelum menulis proposal)

Ini temuan paling kritis dari eksplorasi:

1. **Bandpass napas/jantung HARDCODE untuk manusia, di SEMUA lapisan** (`bindings/vitals.rs`, `wifi-densepose-vitals/src/*.rs`, `vital_signs.rs` server, `edge_processing.c` firmware):
   - Napas manusia: 0,1–0,5 Hz (6–30 BPM). Napas broiler dewasa ~15–30 BPM — pas di TEPI ATAS band; anak ayam/chick bisa >30 BPM → keluar band.
   - Jantung manusia: 0,8–2,0 Hz (40–120 BPM). **Jantung ayam 250–330 BPM ≈ 4,2–5,5 Hz → DI LUAR band 2× lipat**, dan server sengaja MENOLAK estimasi di luar 40–120 BPM sebagai "implausible". Detak jantung ayam via RuView TANPA modifikasi kode = mustahil.
   - Konsekuensi untuk skripsi: jika ingin napas ayam, Anda WAJIB mengubah konstanta filter (di firmware DAN server DAN binding) lalu validasi ulang. Ini kerja nyata tapi scoped (beberapa konstanta + re-run). Alternatif yang TIDAK perlu ubah kode: pakai hanya motion/variance/stillness (indeks aktivitas kawanan) — persis reformulasi yang direkomendasikan dewan LLM Anda!
2. **Skala massa tubuh (RCS):** dokumen riset internal `docs/research/sota-2026-05-22/R19-agricultural-livestock.md` menilai ayam 1,5–2,5 kg = RCS "very low"; sinyal dominan dada; sistem dirancang 1–5 subjek manusia, bukan kawanan 10–50 ekor. → Kembali ke temuan dewan: deteksi level kawanan (agregat), bukan per-ekor.
3. **Lingkungan kandang:** debu + amonia → korosi konektor (housing/pigtail wajib — sudah ada di blind-spot dewan), kipas ventilasi = sumber false-positive presence (kelemahan dikenal RuView), suhu tinggi memengaruhi elektronika.
4. **Modalitas saingan lebih kuat di kandang:** modul mmWave (MR60BHA2/LD2410) yang sudah terintegrasi di firmware RuView kemungkinan memberi sinyal vital jauh lebih bersih daripada CSI murni di lingkungan berdebu — tapi ini menambah biaya ±Rp250 ribu/node dan mengubah premis "CSI murni".

**Kesimpulan untuk garis ayam:** RuView mempercepat capture + alert + dashboard, tapi tidak menyelesaikan masalah fisika inti Anda (dilusi sinyal kawanan, konfound lingkungan). Uji Delta-CSI fisik minggu pertama tetap GERBANG GO/NO-GO nomor satu. Keunggulan: `ind_livestock_monitor.rs` memberi template alert (stillness/escape/labored) yang bisa Anda jadikan desain sistem, dan arsitektur presence-based TIDAK perlu ubah kode — selaras dengan judul Opsi 1 dewan (indeks aktivitas kawanan).

---

## 9. Keterbatasan untuk Konteks SLB (kelas & asrama)

1. **Kekuatan struktural:** konteks SLB sebenarnya adalah fit terbaik RuView — presence/motion/fall/sleep tidak butuh pose halus, privasi (tanpa kamera) adalah argumen etis utama, dan RuView punya privacy mode bawaan. Anomali inaktivitas (`elderly_anomaly`), distress, no_movement persis kebutuhan pendampingan siswa berkebutuhan khusus.
2. **Semua state semantik diasumsikan manusia tunggal/keluaran alat dewasa** — threshold (napas 8–20 BPM untuk "sleeping", dwelling 300 detik, dsb.) belum tentu cocok untuk anak-anak (napas anak lebih cepat: usia 6–12 tahun ~18–25 BPM saat tidur — dekat/melewati tepi atas band!). → Rencanakan kalibrasi ulang threshold per kelompok usia; ini bisa jadi kontribusi riset Anda.
3. **Perilaku atipikal tidak ada dalam data latih mana pun** (MM-Fi = orang dewasa neurotipikal). Gerakan stimming, autoregulasi, dsb. akan masuk "anomali" — bisa jadi fitur (deteksi dini distress) ATAU sumber alarm palsu; desain eksperimen Anda harus menanganinya dengan pelibatan komunitas (prinsip user story #5 Spec Anda berlaku di sini juga: koordinasi dengan pihak SLB, persetujuan informat orang tua/wali).
4. **Identitas tidak terdeteksi dari WiFi** (§4 no. 8) → untuk asrama, sistem TIDAK bisa membedakan siapa yang tidur di ranjang mana bila >1 penghuni; asumsi 1 penghuni/kamar atau tambahkan node per ranjang.
5. **Etika khusus:** perekaman sinyal RF di ruang privat anak berkebutuhan khusus menuntut persetujuan orang tua/wali + izin sekolah + asrama; blur/anonim video ground truth; dan framing "bukan alat medis, bukan pengawasan" harus eksplisit.

---

## 10. Rute Pemakaian RuView yang Realistis per Alat (ringkas)

**ALAT 1 — Kandang ayam broiler:** pakai presence variance + motion-band energy + stillness detection (tanpa ubah kode) untuk INDEKS AKTIVITAS KAWANAN; tiru pola event `ind_livestock_monitor`; kalibrasi ambient di kandang kosong; tambah log kejadian (pakan, cahaya, panen); uji Delta-CSI dulu. YANG PERLU DIUBAH KODE bila lanjut ke napas: konstanta bandpass 0,1–0,5 Hz → rentang unggas (mis. 0,25–0,55 Hz utk 15–33 BPM), di firmware + server.

**ALAT 2 — Ruang kelas SLB:** pakai presence, motion level, room_active, fall detection, no_movement; kalibrasi 600 frame + enrollment per kelas; MQTT → Home Assistant → notifikasi guru; privacy mode aktif. TANPA ubah kode besar; threshold anak-anak perlu disetel ulang (kontribusi riset).

**ALAT 3 — Kamar asrama SLB (malam):** pakai someone_sleeping, no_movement, breathing_rate (dengan catatan tepi band anak), vital_trend; sleep-monitor.js sebagai dashboard hipnogram; skrining bukan diagnosis. TANPA ubah kode untuk prototipe; ubah threshold untuk anak.

**Lingkup bersama (1 sistem, 3 deployment):** firmware sama, server sama, dashboard sama, protokol kalibrasi sama — yang berbeda hanya: penempatan node, threshold, kebutuhan alert, dan label data. Ini argumen KONSOLIDASI yang bagus untuk proposal: satu platform sensing, tiga studi kasus.

---

## 11. Peta File Penting (cheat-sheet referensi)

| Topik | Path |
|---|---|
| README utama (fitur, BOM, quick start) | `README.md` |
| Bukti reproduksibel semua klaim | `PROOF.md`, `docs/proof-of-capabilities.md` |
| Firmware capture + DSP on-node | `firmware/esp32-csi-node/main/csi_collector.c`, `main/edge_processing.c` |
| Runbook operasional firmware (flash/OTA/tuning) | `firmware/esp32-csi-node/RUNBOOK.md` |
| Parser frame ADR-018 | `v2/crates/wifi-densepose-sensing-server/src/csi.rs` |
| Vital signs (napas/jantung) | `v2/crates/wifi-densepose-vitals/src/{breathing,heartrate,anomaly}.rs` |
| Signal DSP library | `v2/crates/wifi-densepose-signal/src/` (hampel.rs, fresnel.rs, bvp.rs, spectrogram.rs…) |
| Server utama + REST API | `v2/crates/wifi-densepose-sensing-server/src/main.rs` |
| State semantik FSM | `v2/crates/wifi-densepose-sensing-server/src/semantic/*.rs` |
| MQTT/Home Assistant | `v2/crates/wifi-densepose-sensing-server/src/mqtt/` |
| Modul livestock | `v2/crates/wifi-densepose-wasm-edge/src/ind_livestock_monitor.rs` |
| Modul medis (gated, eksperimental) | `v2/crates/wifi-densepose-wasm-edge/src/med_*.rs`, `exo_dream_stage.rs` |
| Kalibrasi ruangan | `docs/calibration-guide.md`, `v2/crates/wifi-densepose-calibration/` |
| Training adaptif | `v2/crates/wifi-densepose-sensing-server/src/{recording.rs, adaptive_classifier.rs}` |
| Trainer besar MM-Fi | `v2/crates/wifi-densepose-train/` |
| Python binding + klien | `python/wifi_densepose/`, `python/src/bindings/vitals.rs` |
| Pose stub (bukti jujur) | `v2/crates/cog-pose-estimation/src/inference.rs` (confidence=0), README §"Model weights" |
| Studi MM-Fi honest picture | `docs/benchmarks/mmfi-wifi-sensing-study.md` |
| Riset ternak internal | `docs/research/sota-2026-05-22/R19-agricultural-livestock.md` |
| ADR kunci | ADR-012 (mesh), ADR-018 (format frame), ADR-021 (vitals), ADR-029 (mesh multistatik), ADR-041 (edge modules), ADR-048 (adaptive classifier), ADR-079 (camera-supervised), ADR-110 (C6), ADR-160 (honest labeling edge), ADR-187 (archive deprecation), ADR-347 (rate-aware), ADR-355 (bootstrap prior) |
