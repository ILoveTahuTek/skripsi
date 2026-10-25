# T17-R2 — Riset Kemampuan Teknis ESP32-S3 & Perolehan Wi-Fi CSI

- **Task ID**: T17-R2 (subagent pengumpul bahan riset)
- **Tanggal akses semua sumber daring**: 2026-10-25
- **Untuk**: proposal skripsi penerjemah dua arah bahasa isyarat SIBI (2–3 modul ESP32-S3 + layar + baterai + speaker/mikrofon I2S; server lokal laptop RTX 3070); platform riset RuView (klon lokal `/home/z/my-project/ruview-repo`, commit `fefb0f9`).
- **Metode**: inspeksi langsung klon lokal RuView (bukti kode = bukti terkuat, kutip path:baris) + unduhan langsung datasheet Espressif (PDF v2.2) + README/kode repositori resmi Espressif (esp-csi, esp-tflite-micro, esp-nn, esp-dl) + dokumen ESP-IDF v5.4. arXiv API tidak dipakai. Tidak ada WebSearch/WebFetch tool di lingkungan; akses web via `curl` langsung ke sumber primer.
- **Label status**: [DIVERIFIKASI] = sumber dilihat/unduh langsung; [CUPILIKAN] = hanya snippet pencarian; [TIDAK DITEMUKAN] = dicari jujur tidak ada; [ESTIMASI] = hitungan penulis dari angka terverifikasi (bukan klaim sumber).

---

## 1. Spesifikasi resmi ESP32-S3 (Pertanyaan 1)

Sumber primer: **ESP32-S3 Series Datasheet v2.2 (tanggal revisi 2026-03-05)** — diunduh langsung dari
`https://www.espressif.com/sites/default/files/documentation/esp32-s3_datasheet_en.pdf` (1,05 MB, 74+ halaman, teks diekstrak `pdftotext`); halaman produk `https://www.espressif.com/en/products/socs/esp32-s3`.

### 1.1 CPU & memori (semua [DIVERIFIKASI], datasheet v2.2)

| Parameter | Nilai | Lokasi datasheet |
|---|---|---|
| CPU | Xtensa 32-bit **dual-core LX7**, pipeline 5 tahap, bus data 128-bit + instruksi SIMD | bag. "CPU and Memory" (hlm. 3) & 4.1.1 |
| Clock | hingga **240 MHz** | hlm. 3 |
| CoreMark | 1329,92 (2 core @240 MHz); 5,54 CoreMark/MHz | hlm. 3 |
| **ROM internal** | **384 KB** (boot + fungsi inti) | hlm. 3 & 4.1.2.1 |
| **SRAM internal** | **512 KB** (data+instruksi, hingga 240 MHz) | hlm. 3 & 4.1.2.1 |
| SRAM RTC | 16 KB total = RTC FAST 8 KB + RTC SLOW 8 KB (bertahan deep-sleep) | 4.1.2.1 |
| eFuse | 4096 bit, 1792 bit untuk pengguna | hlm. 3 |
| **PSRAM in-package** (varian chip) | ESP32-S3RH2: **2 MB Quad**; ESP32-S3R8: **8 MB Octal**; **ESP32-S3R16V: 16 MB Octal** (1,8 V); ESP32-S3FH4R2: 4 MB flash + 2 MB PSRAM; ESP32-S3R2 & S3R8V = EOL | Tabel 1-1 (hlm. ~9) |
| **Flash in-package** | ESP32-S3FN8: **8 MB Quad SPI** (default 80 MHz, tanpa auto-suspend) | Tabel 1-1 + catatan kaki |
| Flash/PSRAM eksternal | SPI/Dual/Quad/Octal/QPI/OPI; **hingga 1 GB** flash+RAM eksternal teralamatkan; cache memetakan hingga **32 MB ruang instruksi + 32 MB ruang data** (blok 64 KB) | 4.1.2.2 |
| Cache | L1 cache (hlm. 3); ESP-DL mencantumkan **data cache 64 KB** pada konfigurasi benchmark S3 | esp-dl model README (lihat §3) |
| ULP | ULP-RISC-V + ULP-FSM coprocessor | hlm. 3 |

Catatan modul pasaran: modul umum (ESP32-S3-WROOM-1, XIAO ESP32-S3) membawa flash 8–16 MB + PSRAM octal 8 MB — RuView memakai konfigurasi "8 MB flash + 8 MB PSRAM" pada hardware requirements-nya [DIVERIFIKASI: `firmware/esp32-csi-node/README.md` bag. Hardware Requirements].

### 1.2 Akselerasi AI/DSP — PIE (semua [DIVERIFIKASI])

Datasheet 4.1.1.2 "Processor Instruction Extensions (PIE)":
- **Instruksi fixed-point DSP** (daftar fitur: "Fixed-point DSP instructions" pada ringkasan fitur, hlm. 3) — [catatan: kalimat "fixed-point" ada di baris ringkasan atas dokumen; seksi PIE merinci 2 butir di bawah].
- **Operasi vektor 128-bit**: kompleks multiply, add, sub, mul, shift, compare; **16 register umum baru 128-bit**; data vektor 128-bit non-aligned; load/store digabung dengan data handling.
- Halaman produk: "ESP32-S3 has additional support for vector instructions in the MCU, which provides acceleration for neural network computing and signal processing workloads … take advantage … through ESP-DSP and ESP-NN libraries" [DIVERIFIKASI: www.espressif.com/en/products/socs/esp32-s3].
- Implikasi untuk skripsi: bobot/aktivasi jaringan **int8 128-bit SIMD** adalah jalur percepatan utama (dipakai ESP-NN, lihat §3).

### 1.3 Wi-Fi & BLE (semua [DIVERIFIKASI] datasheet)

| Parameter | Nilai | Lokasi |
|---|---|---|
| Radio Wi-Fi | IEEE **802.11b/g/n**, **2,4 GHz single-band**; lebar pita **20 MHz (HT20) & 40 MHz (HT40)** | "Features > Wi-Fi" (hlm. 2) & 4.3.2.1 |
| Konfigurasi antena | **1T1R (SISO, 1 antena)** — "1T1R mode with data rate up to 150 Mbps" | Features (hlm. 2), 4.3.2.1 |
| MIMO/STBC | Tidak ada MIMO TX; **RX STBC (single spatial stream)** | 4.3.2.1 |
| Daya pancar | hingga +21 dBm (802.11b), +19,5 dBm (11n) | hlm. 4 |
| Antena diversity | Didukung **dengan RF switch eksternal** dikendalikan GPIO (bukan 2 radio) | 4.3.2.1 |
| Mode MAC | STA, SoftAP, **STA+SoftAP simultan**; 4 antarmuka Wi-Fi virtual; WMM; A-MPDU/A-MSDU; 802.11mc FTM | Features (hlm. 2), 4.3.2.2 |
| BLE | **Bluetooth 5 (LE)** + Mesh; 125 kbps–2 Mbps; Coded PHY long-range; advert extension; koeksistensi internal Wi-Fi/BLE berbagi 1 antena | Features (hlm. 2) |
| Throughput (IDF v5.4 S3) | "Up to 20 MBit/s TCP and 30 MBit/s UDP over the air"; ESP-NOW + **Long Range mode "supports up to 1 km of data traffic"** | docs.espressif.com ESP-IDF v5.4 esp32s3 api-guides/wifi.html [DIVERIFIKASI, diunduh 2026-10-25] |

### 1.4 Konsumsi daya (semua [DIVERIFIKASI] datasheet v2.2 Tabel 5-7/5-9/5-10, 3,3 V, 25 °C)

| Mode | Nilai |
|---|---|
| **Active TX Wi-Fi (peak)** | 340 mA (11b 1 Mbps @21 dBm); 291 mA (11g 54 Mbps); **283 mA (11n HT20 MCS7 @18,5 dBm)**; 286 mA (HT40 MCS7 @18 dBm) |
| **Active RX Wi-Fi (peak, periferal mati, CPU idle)** | **88 mA (HT20)**; 91 mA (HT40) |
| BLE TX peak | 335 mA @21 dBm; 193 mA @9 dBm; 116 mA @−15 dBm; BLE RX 93 mA |
| **Modem-sleep** (Wi-Fi clock-gated) @240 MHz, dual-core | 66,2–91,7 mA (32-bit vs 128-bit instruksi; jam periferal mati vs nyala) |
| Modem-sleep @40 MHz | 13,2–23,0 mA |
| **Light-sleep** | **240 µA** (+140 µA jika PSRAM octal 8 MB @3,3 V aktif) |
| **Deep-sleep** | **7 µA** (RTC saja) / 8 µA (RTC+periferal) / 18 µA (pola ULP sensor 1%) |
| Power off | 1 µA |

PENTING untuk desain CSI: modem-sleep mematikan clock Wi-Fi → RuView menonaktifkannya demi CSI (`WIFI_PS_NONE`, lihat §4). Mode tidur dalam angka di atas TIDAK kompatibel dengan penangkapan CSI kontinu; lihat §5 untuk estimasi baterai realistis.

---

## 2. Perolehan Wi-Fi CSI pada keluarga ESP32 (Pertanyaan 3)

### 2.1 API resmi ESP-IDF (semua [DIVERIFIKASI])

- Sumber: ESP-IDF Programming Guide v5.4 (ESP32-S3), "Wi-Fi Driver > Wi-Fi Channel State Information", `https://docs.espressif.com/projects/esp-idf/en/v5.4/esp32s3/api-guides/wifi.html` (diunduh penuh 2026-10-25); struct `wifi_csi_config_t` di `esp-idf/components/esp_wifi/include/local/esp_wifi_types_native.h` (master, diunduh dari GitHub).
- API: `esp_wifi_set_csi_config()` → `esp_wifi_set_csi_rx_cb()` → `esp_wifi_set_csi(true)`. Konfigurasi non-HE (berlaku ESP32-S3): `lltf_en`, `htltf_en`, `stbc_htltf2_en`, `ltf_merge_en`, `channel_filter_en`, `manu_scale`+`shift`, `dump_ack_en`. (Chip Wi-Fi 6 C6/C5 memakai `wifi_csi_acquire_config_t` berbeda.)
- **Dokumentasi resmi merekomendasikan promiscuous/sniffer demi CSI lebih banyak**: "Because station does not receive any packet when it is disconnected and only receives packets from AP when it is connected, **it is suggested to enable sniffer mode to receive more CSI data by calling esp_wifi_set_promiscuous()**." (v5.4, seksi CSI Configure) — fondasi langsung bagi skenario koeksistensi §4.
- Callback CSI berjalan di **Wi-Fi task** — dokumentasi melarang operasi panjang di callback (antrekan ke task lain). Konsisten dengan arsitektur RuView (ring buffer SPSC).

### 2.2 Jumlah subcarrier & format data (semua [DIVERIFIKASI] dari tabel IDF v5.4)

Tabel resmi ESP32-S3 (S3 = non-HE path) untuk kombinasi kanal/paket:

| Kondisi | Subcarrier indeks | Total byte `len` |
|---|---|---|
| 20 MHz, non-HT, non-STBC (LLTF) | 0~31, −32~−1 = **64 pasang I/Q** | **128** |
| 20 MHz, HT, non-STBC (LLTF + HT-LTF) | masing-masing 64 pasang | **256** |
| 20 MHz, HT, STBC (+STBC-HT-LTF) | — | **384** |
| 40 MHz (secondary above/below), HT | 0~63 / −64~−1 per LTF | hingga **612** |

Tabel subcarrier PHY (IDF v5.4, seksi CSI):
- 802.11a/g: −26..+26, pilot −21/−7/+7/+21 → **52 total, 48 data usable**
- **802.11n 20 MHz (HT20): −28..+28 → 56 total, 52 data usable** (pilot −21/−7/+7/+21)
- 802.11n 40 MHz (HT40): −57..+57 → **114 total, 108 data usable** (6 pilot)

Jadi: buffer CSI ESP32-S3 HT20 = hingga **64 pasang I/Q per LTF** (2 byte per pasang, imajiner dulu lalu riil; LLTF+HT-LTF = 256 byte), sedangkan **jumlah subcarrier fisik 802.11n HT20 = 56 (52 data)** — dua angka yang berbeda makna dan sering tertukar di literatur. RuView memakai "64 subcarriers, ~5 KB/s @ 20 Hz" di README firmware dan "56 subcarriers" di ADR-018 — keduanya konsisten dengan tabel di atas (buffer vs grid fisik). Keterangan pertama `first_word_invalid` (4 byte pertama tak valid karena batasan HW S3) terdokumentasi di IDF dan disanitasi RuView (bit 5 byte 19 ADR-018).

### 2.3 esp-csi (github.com/espressif/esp-csi) (semua [DIVERIFIKASI], master diunduh 2026-10-25)

- README: "**Full series support: All ESP32 series support CSI, including ESP32 / ESP32-S2 / ESP32-C3 / ESP32-S3 / ESP32-C5 / ESP32-C6 / ESP32-C61**." → **ESP32-S3 didukung penuh**.
- Tiga pola perolehan CSI di README:
  1. **csi_recv_router** — ESP32 STA terhubung ke router, ping gateway → CSI dari balasan router (contoh mendukung ESP32/S2/C3/**S3**/C5/C6/C61 per README-nya; ping `1000/CONFIG_SEND_FREQUENCY` ms; catatan kode: "only LLTF sub-carriers are selected" demi kompatibilitas router).
  2. **CSI antar-perangkat** (dua ESP32 sama-sama ping router; A mendengar ping B).
  3. **csi_send + csi_recv** — pengirim khusus: `csi_send` mengirim **ESP-NOW broadcast** (peer FF:FF:FF:FF:FF:FF, `ifidx = WIFI_IF_STA`, kanal `CONFIG_LESS_INTERFERENCE_CHANNEL`, `esp_wifi_set_channel()` manual, laju `CONFIG_SEND_FREQUENCY` Hz; HT20 atau HT40 dengan secondary-below; `esp_now_set_peer_rate_config` mengatur phymode/rate) dan penerima `csi_recv` (WIFI_MODE_STA, tidak terhubung AP, konfigurasi `acquire_csi_ht20/ht40`, callback CSI). Inilah pola "TX ESP-NOW → RX collector".
- Contoh aplikasi **esp-radar** (console_test, wifi_sensing_demo) di dalam esp-csi: "Supported Targets | ESP32 | ESP32-C3 | ESP32-C5 | ESP32-C6 | ESP32-C61 | ESP32-S2 | **ESP32-S3**" — deteksi kehadiran/gerak on-device dengan kalibrasi.

### 2.4 esp32-csi-tool (Steven Hernandez dkk., WoWMoM 2020) (semua [DIVERIFIKASI], master diunduh 2026-10-25)

- **Repo sekarang: `https://github.com/StevenMHernandez/ESP32-CSI-Tool`** — URL `github.com/espressif/esp32-csi-tool` **TIDAK ADA lagi** (HTTP 404 pada 2026-10-25; dicoba pula `stevenmh/...` → 404). Ini koreksi penting untuk daftar pustaka proposal bila mengutip URL lama.
- Tiga sub-proyek: `active_sta` (CSI-TX: STA yang terhubung AP lalu menghujani AP dengan **paket UDP "1\n" ke 192.168.4.1:2223** secepat `CONFIG_PACKET_RATE` — bukan ESP-NOW), `active_ap` (CSI-RX: softAP `WIFI_MODE_AP` yang menerima UDP tersebut; mengirim timestamp ke STA), `passive` (RX pasif `esp_wifi_set_promiscuous(true)` + filter, kanal default 3).
- CSI config `active`*: `lltf_en=1, htltf_en=1, stbc_htltf2_en=1, channel_filter_en=0` + `esp_wifi_set_csi(1)` + callback → CSV `CSI_DATA` ke serial (baud tinggi hingga 1,5 Mbaud disarankan) + SD card.
- **Persyaratan ESP-IDF v4.3** (README) → target aslinya ESP32 klasik; **dukungan/ujian ESP32-S3 tidak tercantum di repo** [DIVERIFIKASI tidak adanya]; untuk S3 gunakan esp-csi resmi.
- Paper: BibTeX resmi repo — S. M. Hernandez & E. Bulut, "**Lightweight and Standalone IoT Based WiFi Sensing for Active Repositioning and Mobility**", 21st Int. Symposium on "A World of Wireless, Mobile and Multimedia Networks" (WoWMoM 2020), Cork, Ireland, 14 Juni 2020 (ada juga varian bibtex `esp32_csi_tool_percom.bib`). [DIVERIFIKASI berkas `docs/bibtex/esp32_csi_tool_wowmom.bib`]
- Koreksi atas dugaan tugas: pada master saat ini, **TX memakai UDP socket, bukan ESP-NOW**; pola TX-ESP-NOW→RX ada di repo **esp-csi** resmi (csi_send/csi_recv), dan RuView memakai ESP-NOW untuk time-sync (§4).

### 2.5 Bukti kode RuView (klon lokal commit `fefb0f9`) (semua [DIVERIFIKASI], path:baris)

- `firmware/esp32-csi-node/main/csi_collector.c:98` — `#define CSI_MIN_SEND_INTERVAL_US (20 * 1000)` dengan komentar "Default: 20 ms = **50 Hz max send rate**" (pelindung buffer lwIP dari ENOMEM).
- `csi_collector.c:115` — `CSI_MIN_PROCESS_INTERVAL_US (20*1000)` = 50 Hz gate pemrosesan (pelindung crash `wDev_ProcessFiq` core 0 saat callback 100–500 Hz).
- `csi_collector.c:160` — "ESP32-S3 typically reports **1 antenna** for CSI."
- `csi_collector.c:678-691` — konfigurasi S3 (non-HE): `lltf_en`, `htltf_en`, `stbc_htltf2_en`, `ltf_merge_en` → `esp_wifi_set_csi_config` + `esp_wifi_set_csi_rx_cb` + `esp_wifi_set_csi(true)`.
- `csi_collector.c:637-650` — `esp_wifi_set_promiscuous(true)` + filter **MGMT-only** (workaround RuView#396): komentar "DATA frames cause 100-500+ WiFi HW interrupts/sec which crashes Core 0 in wDev_ProcessFiq (SPI flash cache race in ESP-IDF WiFi blob). MGMT-only gives ~10 Hz (beacons)"; `csi_collector_enable_data_capture()` (baris ~846: filter MGMT+DATA) dipakai untuk papan tanpa layar.
- `csi_collector.c:705-708` + `496-539` — **self-ping ke gateway** sebagai sumber lantutan OFDM unicast (meniru `csi_recv_router` esp-csi; komentar "Mirrors Espressif's esp-csi csi_recv_router reference"); catatan #2287: sebagian AP membalas ping pada rate 802.11b DSSS yang **tidak menghasilkan CSI**.
- `csi_collector.c:422` — "At **10 Hz observed CSI rate**" pada bench ADR-110 (laju CSI riil bergantung lalu lintas).
- `csi_collector.h:24` — `CSI_MAX_FRAME_SIZE = 20 + 4*256*2` (header 20 B + maksimum 4 antena × 256 subcarrier × 2 B).
- README firmware: Tier 0 "~20 Hz per channel, ~5 KB/s per node (64 subcarriers, 1 antenna)"; "On S3, STBC frames can carry **192 I/Q entries**; edge processing uses the first 128 entries" (isu #2286).
- ADR-018 (`docs/adr/ADR-018-esp32-dev-implementation.md`): "For 3 antennas, 56 subcarriers: 20 + 336 = 356 bytes per frame"; "~100 Hz at 56 subcarriers = ~35 KB/s per node"; "Most ESP32-S3-DevKitC boards have one on-board antenna"; **"No on-device FFT"** — agregator Rust yang mengekstraksi fitur (rujuk ADR-012 vs ADR-018).
- Kesimpulan laju CSI: **batas atas desain RuView 50 frame/detik** (gate 20 ms), laju riil teramati ~10–20 Hz bergantung trafik lingkungan (beacon + probe + ping reply), bandwidth ~3–5 KB/s/node pada HT20 1 antena.

---

## 3. Framework ML on-device di ESP32-S3 (Pertanyaan 2)

### 3.1 ESP-DL (github.com/espressif/esp-dl) (semua [DIVERIFIKASI], master diunduh 2026-10-25)

- Kuantisasi **w8a8 / w16a16 / campuran w8a16** (v3.3.11+); format model `.espdl` (FlatBuffers, zero-copy); tool kuantisasi **ESP-PPQ** (ONNX/PyTorch/TensorFlow → ONNX); **memory planner** menempatkan bobot per lapisan ke SRAM internal/PSRAM/flash sesuai anggaran; **dual-core scheduling** untuk Conv2D/DepthwiseConv2D; aktivasi via LUT 8-bit.
- Model Zoo mendukung **ESP32-S3** (plus S31/P4): YOLO26 (NMS-free), YOLO11n detect/pose/seg, MobileNetV2 (imagenet_cls), deteksi wajah/kucing/anjing/tangan/pedestrian (MSR/MNP/ESPDet-Pico), **hand gesture 8+ kelas** (MobileNetV2-0.5), speaker verification (S31/P4 saja), dsb.
- **Latensi di ESP32-S3 (240 MHz, int8, `CONFIG_COMPILER_OPTIMIZATION_PERF`, octal PSRAM 80 MHz, data cache 64 KB)** — dari `models/*/README.md`:

| Model | Input | Latensi model (ms) | Catatan |
|---|---|---|---|
| MobileNetV2 s8 (imagenet_cls) | 224×224×3 | **437,9 (1 core) / 389,7 (multi-core)**; Prec@1 70,543% | model README imagenet_cls |
| MSR wajah | 120×160×3 | 32,5 | human_face_detect |
| MNP wajah | 48×48×3 | 5,9 | human_face_detect |
| ESPDet-Pico wajah | 224×224×3 | 129,4 | human_face_detect |
| ESPDet-Pico wajah | 416×416×3 | 422,1 | human_face_detect |
| YOLO11n | 640×640×3 | **3906,3** (terlalu berat) | flash 8 MB + PSRAM 8 MB; ~3 MB parameter + 6 MB memori manajer |
| YOLO11n 320 | 320×320×3 | 961,5 | coco_detect |
| YOLO26n | 512×512×3 / 640 | 2348,2 / 3792,9 | yolo26 |
| Hand gesture MobileNetV2-0.5 | 128×128×3 | **69,2** | hand_gesture_recognition |

- Benchmark operator (`benchmark_report.md`, v3.3.10): ESP32-S3 vs ESP32 klasik — Conv **22,9×**, ConvTranspose 31,8×, MaxPool 37,1×, Resize 8×, Gemm 2,4×, MatMul 3×, GRU 3,8×, LSTM 3,9× lebih cepat.
- Operator didukung: Conv, Gemm, MatMul, GRU, **LSTM**, LayerNorm, RMSNorm, pooling, dsb. (`operator_support_state.md`) — arsitektur 1D-CNN/GRU untuk deret waktu CSI masuk jangkauan.

### 3.2 esp-tflite-micro (github.com/espressif/tflite-micro-esp-examples → kini **espressif/esp-tflite-micro**) (semua [DIVERIFIKASI], master diunduh 2026-10-25)

- Komponen `esp-tflite-micro` via `idf.py add-dependency`; dukung ESP-IDF v5.0–v6.0 (v5.0 ke bawah EOL). Contoh: `hello_world`, `micro_speech`, `person_detection`.
- **Ukuran model contoh (dihitung langsung dari berkas sumber)**:
  - `person_detect_model_data.cc` → `g_person_detect_model_data_len = 300568` B = **293,5 KB** (MobileNetV1 96×96 int8 Visual Wake Words); tensor arena **100 KB + scratch** (`person_detection/main/main_functions.cc:54`).
  - `micro_speech` model KWS → `g_model_len = 18800` B = **18,4 KB**; audio preprocessor int8 model di `audio_preprocessor_int8_model_data.h` (54,6 KB sumber); tensor arena **30 KB** (`micro_speech/main/main_functions.cc:47`).
- **Batasan operator**: TFLite Micro hanya mendukung operator inti mikro (FULLY_CONNECTED, CONV_2D, DEPTHWISE_CONV_2D, RESHAPE, SOFTMAX, dsb.) — operator di luar set inti perlu custom op/registrasi manual (dok. tflite-micro upstream; tidak dihitung ulang di sini → rincian operator micro_speech/person_detection memakai set standar). [sebagian CUPILIKAN dari struktur repo; batas operator umum TFLM = DIVERIFIKASI dari keberadaan MicroOpResolver di contoh]

### 3.3 ESP-NN (github.com/espressif/esp-nn) (semua [DIVERIFIKASI], master diunduh 2026-10-25)

- Kernel teroptimasi assembly untuk **ESP32-S3 (instruksi vektor)**, P4/S31 (PIE/QACC), ESP32/C3 (generic); terintegrasi otomatis ke esp-tflite-micro (flag `-DESP_NN`).
- **Person Detection (VWW int8, invoke())**: ESP32-S3 **2300 ms → 54 ms** dengan ESP-NN (42,6×); catatan: dengan memori internal 47 ms. ESP32 380 ms; C3 426 ms; P4 73 ms.
- **MobileNetV3-Small int8 224×224**: S3 **26679 → 729 ms** (dual-core 690 ms). **YOLO11n int8 192×192**: S3 **130753 → 1253 ms** (dual-core 1053 ms).
- Kernelwise S3 (ticks): depthwise conv 5–6,3×; conv 5,5–14,2×; fully connected 5,5×; max pool 7,8×.
- Fungsi `esp_nn_dual_core_enable()` membagi kernel berat ke 2 core.

### 3.4 Kesimpulan realistis untuk klasifikasi isyarat CSI di ESP32-S3

- **Fakta**: model int8 vision kelas VWW (293,5 KB) berjalan 54 ms; model 1D time-series (input 64 subcarrier × ~30–50 frame, 5–8 kelas) secara struktural jauh lebih kecil dari VWW (orde puluhan–ratusan KB, lihat micro_speech 18,4 KB sebagai tolok ukur kelasnya).
- **Fakta anggaran memori RuView saat ini** (flash 8 MB terpakai ~943 KB; PSRAM 8 MB terpakai 640 KB untuk arena WASM 4×160 KB; sisa PSRAM 7,36 MB) — ruang sangat longgar untuk bobot model int8 ratusan KB + tensor arena < 100 KB.
- **Fakta anggaran waktu RuView**: WASM budget guard **10 ms/frame** pada DSP 20 Hz; ESP-DL/TFLM native (bukan WASM) memberi ruang lebih besar (54 ms @ person detection).
- **Hipotesis desain (bukan fakta)**: klasifikasi jendela CSI 1–2 detik (50–100 frame × 56–64 subcarrier) dengan 1D-CNN/GRU kecil int8 via ESP-DL/TFLM+ESP-NN diperkirakan puluhan–~300 KB dan puluhan–ratusan ms per inferensi — kelas kompleksitas berada DI BAWAH person detection (54 ms) hingga MobileNetV2-0.5 gesture (69 ms); harus diukur sendiri karena belum ada benchmark publik model CSI isyarat di S3 [TIDAK DITEMUKAN benchmark CSI-gesture on-device ESP32-S3].
- Referensi dalam RuView untuk klasifikasi isyarat on-device: modul WASM **gesture.rs (DTW template matching: wave/push/pull/swipe)** — pendekatan non-DL yang sudah teruji di firmware, tetapi DTW vs CNN untuk SIBI 5–8 kelas adalah keputusan desain T1 [DIVERIFIKASI keberadaan modul, `v2/crates/wifi-densepose-wasm-edge`, README firmware].

---

## 4. KOEKSISTENSI RADIO: CSI + STA-TCP/IP + ESP-NOW pada SATU ESP32-S3 (Pertanyaan 4 — paling kritis)

### 4.1 Jawaban singkat

**[DIVERIFIKASI — bukti kode produksi] YA untuk kombinasi (STA terhubung AP + UDP/TCP ke server + penangkapan CSI promiscuous dari semua paket yang didengar) — persis arsitektur firmware RuView esp32-csi-node yang berjalan di ESP32-S3.** **[DIVERIFIKASI — bukti kode + komentar] YA untuk ESP-NOW bersamaan dengan STA terhubung** (dipakai RuView untuk time-sync lintas node "Works on both S3 and C6"; dokumentasi ESP-NOW mengizinkan pengiriman lewat antarmuka Station). **BUTIR PENTING: semua aktivitas harus pada KANAL YANG SAMA** (kanal AP tempat STA terhubung); node ESP-NOW pengirim harus set kanal yang sama. Lalu lintas TX node lain yang berada pada kanal berbeda TIDAK akan menghasilkan CSI di penerima.

### 4.2 Bukti per skenario

**Skenario A — satu S3 menangkap CSI dari paket node lain SAMBIL terhubung STA & mengirim UDP ke server [DIVERIFIKASI]:**
- RuView `main.c:189-267` `wifi_init_sta()`: `WIFI_MODE_STA`, tunggu `IP_EVENT_STA_GOT_IP` (baris 256-266).
- Setelah terhubung, `csi_collector.c:637-650`: `esp_wifi_set_promiscuous(true)` + filter → callback CSI menyala untuk **semua frame yang didengar** (beacon AP, frame node lain, ping reply), dengan MAC filter opsional (`csi_collector.c:343-350`, ADR-060).
- CSI lalu dikirim via UDP oleh `stream_sender.c:48,105` (`SOCK_DGRAM`/`sendto`) ke server — jadi radio yang sama menangkap CSI dan mengalirkan data IP.
- Dokumentasi ESP-IDF v5.4 mendukung pola ini secara eksplisit (rekomendasi sniffer mode di §2.1) dan datasheet menyatakan STA+SoftAP koeksisten pada MAC (§1.3).
- esp-csi `csi_recv_router` (mendukung S3) adalah contoh resmi sejenis: STA terhubung router + ping + CSI.

**Skenario B — ESP-NOW + STA terhubung pada satu chip [DIVERIFIKASI]:**
- RuView `main.c:554-566`: komentar kode "ADR-110 D1 workaround: **ESP-NOW cross-node sync. Initialized after WiFi STA connects** (ESP-NOW needs the WiFi driver up). **Works on both S3 and C6**". `c6_sync_espnow.c:33` — beacon broadcast **setiap 100 ms** (10 Hz), payload 16 byte, MAC broadcast FF:FF:FF:FF:FF:FF; dipakai untuk sinkronisasi epoch lintas node (presisi ~490–540 µA-level µs terukur di ADR-110 §A0.7–A0.10, dikutip komentar kode).
- Dokumentasi ESP-NOW (esp_now.rst, IDF master, diunduh 2026-10-25): "ESP-NOW data must be transmitted after Wi-Fi is started … **You can send ESP-NOW data via both the Station and the SoftAP interface**"; "If the channel is set to 0, data will be sent on the current channel. **Otherwise, the channel must be set as the channel that the local device is on**" → batasan kanal tunggal.
- esp-csi `csi_send`: contoh resmi TX ESP-NOW (peer channel = kanal tetap) yang oleh penerima (`csi_recv`, STA tidak terhubung) menghasilkan CSI — kombinasi TX-ESP-NOW→RX-CSI terdokumentasi resmi.

**Skenario C — alternatif bila koeksistensi penuh dirasa berisiko [keputusan desain, bukan keharusan]:**
- **Dua peran terpisah** (node CSI khusus + node gateway WiFi) — didukung arsitektur RuView (mesh 3–6 node, TDM slot, `rv_mesh.c`), tetapi MENAMBAH perangkat; bukti kode menunjukkan tidak diperlukan untuk kasus 2–3 modul pada satu AP.
- **Time-slicing / duty-cycle** — RuView punya `power_mgmt.c` (light-sleep duty cycling NVS `power_duty`) tetapi **modem-sleep mematikan CSI**; duty-cycling CSI = celah deteksi (angka laju 50 Hz maksimum akan turun). [DIVERIFIKASI adanya power_mgmt; implikasi = analisis]
- **ESP-NOW untuk hasil label antar modul** (bukan lewat AP) — dimungkinkan (payload ≤250 B cukup untuk label+timestamp), dengan catatan kanal sama dan throughput 1 Mbps default.

### 4.3 Batasan/risiko koeksistensi yang terdokumentasi (semua [DIVERIFIKASI])

1. **Kanal tunggal**: STA terhubung → terkunci kanal AP; semua TX node lain harus di kanal itu untuk menghasilkan CSI. RuView: auto-detect kanal AP (`csi_collector.c:605-614`) + MAC filter. ADR-029 channel-hop (tabel hop 1/6/11, dwell 50 ms) BERTENTANGAN dengan STA terhubung (hop akan memutus asosiasi) — di RuView, hop hanya aktif `hop_count>1` dan mode default single-channel; dokumentasi csi_send juga bekerja tanpa AP.
2. **Beban interrupt**: filter DATA penuh memicu 100–500+ interrupt/s yang bisa **crash Core 0** (race cache SPI flash di blob Wi-Fi; RuView#396) — RuView memilih MGMT-only pada papan berlayar, MGMT+DATA pada papan tanpa layar, plus gate 50 Hz. → untuk modul berlayar (skripsi ini), ikuti pola MGMT-only + sumber trafik terkendali.
3. **Modem-sleep harus mati** (`WIFI_PS_NONE`) untuk CSI andal (`csi_collector.c:619-632`; RuView#521) → konsekuensi daya §5 dan peringatan termal RuView untuk papan mungil.
4. **AP yang membalas ping pada rate 802.11b tidak menghasilkan CSI** (#2287) — solusi RuView: host LAN mengirim UDP `csi-udp-poke.py` 50 Hz ke node.
5. **Streaming audio I2S + CSI pada radio yang sama** (rencana modul penerjemah dengan mikrofon): belum ada bukti di RuView (audio bukan fitur RuView). Wi-Fi STA ~20 Mbps TCP kapasitas (IDF) secara teoretis cukup untuk Opus/PCM terkompresi, tetapi **interaksi beban TX audio dengan laju CSI belum teruji** → risiko terbuka untuk diuji T0. [BELUM TERSELESAIKAN]

---

## 5. Baterai & periferal (Pertanyaan 5)

### 5.1 Angka terverifikasi (datasheet; RuView)

- ESP32-S3 RX Wi-Fi aktif: **88–91 mA** (periferal mati, CPU idle) — Tabel 5-7.
- TX Wi-Fi puncak: 283–340 mA (berganting mode/rate) — Tabel 5-7.
- Modem-sleep 240 MHz dual-core: 66,2–91,7 mA — Tabel 5-9 (tidak bisa dipakai untuk CSI kontinu).
- Light-sleep 240 µA; deep-sleep 7–8 µA; PSRAM octal 8 MB menambah ±140 µA saat light-sleep (catatan Tabel 5-10).
- RuView README (peringatan termal): firmware berjalan "WiFi radio with modem sleep disabled (WIFI_PS_NONE …) plus a full edge-processing DSP pipeline on Core 1" = "sustained high current draw with no duty-cycling"; papan seukuran koin pernah overheat sampai regulator rusak (laporan lapangan); DevKitC-1/XIAO aman.
- Peringatan desain [DIVERIFIKASI komentar RuView]: CSI kontinu + tampilan aktif = kelas arus kontinu, bukan pulsa.

### 5.2 Periferal umum (status bukti per baris)

| Periferal | Angka arus | Status |
|---|---|---|
| INMP441 (mikrofon I2S MEMS) | ~1,4 mA | **[TIDAK DIVERIFIKASI]** — PDF datasheet TDK gagal diunduh (URL kini HTML); angka umum dikutip komunitas, wajib cek lembar data saat beli |
| MAX98357A (amplifier I2S 3 W class-D) | idle/quiescent ~2–4 mA; aktif bergantung beban speaker (puluhan mA) | **[TIDAK DIVERIFIKASI]** — datasheet Analog Devices memblokir unduhan; cek saat beli |
| Layar SPI ILI9341 2,8"/ST7789 1,8–2,0" | backlight umumnya puluhan mA (LED); panel+driver ~5–15 mA | **[TIDAK DIVERIFIKASI]** — halaman vendor (Waveshare/Adafruit) tidak menampilkan arus pada HTML yang dapat diunduh |
| Speaker 3 W @ 4–8 Ω via MAX98357A | puncak ratusan mA saat volume penuh (P = V²/R) | [ESTIMASI] dari spesifikasi daya modul |

### 5.3 Estimasi umur baterai [ESTIMASI — hitungan penulis, bukan klaim sumber]

Asumsi operasi penerjemah: `WIFI_PS_NONE` (CSI), RX dominan + TX sesekali (duty ~10–20% TX), CPU 240 MHz aktif (DSP ringan + tampilan), layar menyala terus:

- Arus rata-rata modul ≈ RX 90 mA + CPU/margin aktif +30–60 mA + layar 30–80 mA + audio 5–40 mA (sewaktu) ≈ **150–250 mA**.
- Baterai Li-ion/LiPo:
  - 2000 mAh → **~8–13 jam** kontinu
  - 3500 mAh → **~14–23 jam**
  - 5000 mAh → **~20–33 jam**
- Mode hemat (layar dim saat idle, duty-cycle 20%: RuView `power_duty`) memperpanjang beberapa kali lipat dengan konsekuensi celah CSI — angka pasti harus diukur T0 (alat: ammeter/USB power meter). Skenario sidang (jam-jaman) jauh di bawah kapasitas ini → baterai 2000–3000 mAh lebih dari cukup untuk demo; spesifikasi proposal sebaiknya menyebut "pengisian ulang harian" alih-alih "multi-hari".

---

## 6. Komunikasi antarmodul — ESP-NOW & alternatif (Pertanyaan 6)

Semua [DIVERIFIKASI] dari `esp_now.rst` (IDF master, diunduh 2026-10-25) + IDF v5.4 S3 Wi-Fi guide kecuali diberi label lain:

- **Payload maksimum**: v1.0 = **250 byte** (`ESP_NOW_MAX_DATA_LEN`); **v2.0 = 1470 byte** (`ESP_NOW_MAX_DATA_LEN_V2`, perangkat v2 bisa terima keduanya; v1 hanya terima ≤250 B dari v2, selebihnya dipotong/dibuang). → label isyarat + timestamp + confidence (+ frasa pendek) muat di 250 B.
- **Rate default 1 Mbps**; rate/phymode per-peer bisa diatur (`esp_now_set_peer_rate_config` — dipakai esp-csi csi_send untuk menjamin rate OFDM tertentu demi kualitas CSI).
- **Keamanan**: CCMP; PMK + LMK 16 byte; multicast tidak dienkripsi; **maks 20 perangkat peer** (17 terenkripsi, default 7) di ESP32/S3.
- **Kanal**: peer channel 0 = kanal lokal saat ini; selain itu **harus sama dengan kanal lokal** (batasan utama untuk koeksistensi dengan STA, lihat §4.3).
- **Latensi**: ESP-NOW connectionless satu hop MAC — tidak ada angka latensi resmi di dokumen [TIDAK DITEMUKAN angka resmi]; pengukuran komunitas umumnya milidetik-level (tidak dikutip sebagai fakta). → latensi antarmodul harus diukur T0. RuView memakai beacon 10 Hz dengan stdev offset ~540 µs (ADR-110 §A0.8, dikutip kode) — indikasi latensi propagasi+software rendah.
- **Jarak praktis**: dokumen resmi hanya menyebut mode **Long Range hingga 1 km** (IDF v5.4 S3 Wi-Fi feature list). Jarak mode normal [TIDAK DITEMUKAN angka resmi] — bergantung antena/lingkungan; untuk ruang kelas (≤10 m) bukan risiko.
- **Alternatif**: (a) via AP server (TCP/UDP, sudah berjalan di jalur RuView); (b) WiFi Direct / SoftAP — didukung chip (STA+SoftAP), dipakai esp32-csi-tool `active_ap`; (c) ESP-NOW — paling sederhana untuk label ringan antar modul pada kanal sama.

---

## 7. Kontradiksi & ketidakpastian yang ditemukan

1. **"esp32-csi-tool ada di organisasi espressif"** (dugaan tugas) vs **kenyataan**: repo hanya ada di `StevenMHernandez/ESP32-CSI-Tool`; path espressif 404. → perbaiki rujukan proposal bila perlu.
2. **"TX-nya ESP-NOW" pada esp32-csi-tool** vs kode master: TX-nya UDP socket (active_sta); **ESP-NOW dipakai esp-csi csi_send** dan RuView sync. Dua klaim ini sering dicampur dalam literatur — kutip dengan hati-hati.
3. **Angka "56 subcarrier" vs "64 pasang I/Q"**: keduanya benar pada konteks berbeda (grid fisik 802.11n HT20 = 56 total/52 data vs buffer CSI per LTF = 64 pasang). ADR-018 RuView memakai 56 (3 antena hipotetis), README firmware memakai 64. Proposal sebaiknya menyatakan definisi eksplisit.
4. **Laju CSI**: klaim "hingga 100 Hz" (ADR-018, teoretis) vs gate 50 Hz (kode) vs laju teramati 10–20 Hz (komentar kode & README) — gunakan "hingga 50 frame/s (gate firmware), 10–20 Hz tipikal" di proposal.
5. **Ukuran model "hingga 16 MB PSRAM"**: benar di level chip (ESP32-S3R16V) tetapi varian EOL/1,8 V; modul umum dipasaran 8 MB octal — jangan menjanjikan 16 MB.

## 8. Yang belum terverifikasi / perlu tindak lanjut

- Arus INMP441, MAX98357A, ILI9341/ST7789 (datasheet vendor gagal diunduh — halaman diblokir/JS) → ukur langsung atau baca PDF dari distributor saat pengadaan.
- Latensi ESP-NOW end-to-end dan jarak efektif mode normal (ukur T0).
- Benchmark model klasifikasi CSI isyarat (5–8 kelas SIBI) on-device di S3 — belum ada publikasi; ukur sendiri setelah training (perkirakan dulu dengan tolok ukur §3.4).
- Interaksi streaming audio I2S (mikrofon→server) dengan laju/puncak CSI pada satu radio — uji T0 (§4.3 butir 5).
- Rujukan DOI resmi paper WoWMoM 2020 Hernandez & Bulut (bibtex repo tidak memuat DOI) — verifikasi via IEEE Xplore bila akan dikutip di daftar pustaka.

## 9. Ringkasan klaim kunci untuk proposal (angka penting)

- ESP32-S3: dual-core Xtensa LX7 240 MHz; 512 KB SRAM + 384 KB ROM; modul 8–16 MB flash + hingga 8 MB PSRAM octal (chip hingga 16 MB); Wi-Fi 802.11 b/g/n 2,4 GHz **1T1R 150 Mbps**; BLE 5; instruksi vektor 128-bit (PIE).
- Daya: RX Wi-Fi 88 mA; TX puncak 283–340 mA; light-sleep 240 µA; deep-sleep 7 µA; **CSI kontinu menuntut `WIFI_PS_NONE`** → modul penerjemah ≈ 150–250 mA [ESTIMASI] → baterai 2000–5000 mAh ≈ 8–33 jam.
- CSI: API `esp_wifi_set_csi_config/rx_cb/set_csi`; **HT20: 56 subcarrier (52 data), buffer 64 I/Q-pair per LTF (LLTF+HT-LTF 256 B)**; HT40 114 subcarrier; laju firmware RuView maks **50 frame/s**, tipikal 10–20 Hz; **ESP32-S3 didukung penuh esp-csi/esp-radar**.
- ML on-device: ESP-DL (w8a8; MobileNetV2 390–438 ms; gesture MobileNetV2-0.5 69 ms), TFLM+ESP-NN (person detection 293,5 KB / **54 ms**; micro_speech 18,4 KB / arena 30 KB); WASM RuView ≤128 KB modul, 10 ms/frame @20 Hz.
- Koeksistensi: **STA terhubung + UDP server + CSI promiscuous + ESP-NOW pada SATU S3 = terbukti di firmware produksi RuView (S3) dan direkomendasikan dokumentasi IDF**; syarat: satu kanal, filter MGMT untuk papan berlayar, modem-sleep off.
- ESP-NOW: payload 250 B (v1) / 1470 B (v2); 20 peer; rate default 1 Mbps; Long Range 1 km; **latensi resmi tidak dipublikasikan**.

## 10. Daftar sumber (diakses 2026-10-25)

**Lokal (klon RuView commit fefb0f9):**
1. `/home/z/my-project/ruview-repo/firmware/esp32-csi-node/main/csi_collector.c` (baris 98, 115, 160, 244-251, 343-350, 368, 421-422, 478-539, 560-709, 846)
2. `/home/z/my-project/ruview-repo/firmware/esp32-csi-node/main/csi_collector.h` (baris 24)
3. `/home/z/my-project/ruview-repo/firmware/esp32-csi-node/main/main.c` (baris 189-267, 545-566)
4. `/home/z/my-project/ruview-repo/firmware/esp32-csi-node/main/c6_sync_espnow.c` (baris 5-15, 31-44)
5. `/home/z/my-project/ruview-repo/firmware/esp32-csi-node/main/stream_sender.c` (baris 48, 105)
6. `/home/z/my-project/ruview-repo/firmware/esp32-csi-node/README.md` (hardware, tier, memori, termal, #2286/#2287)
7. `/home/z/my-project/ruview-repo/docs/adr/ADR-018-esp32-dev-implementation.md`
8. `/home/z/my-project/01-ruview-exploration/01_EKSPLORASI_DEEP_RUVIEW.md`
9. `/home/z/my-project/worklog.md` (Task 1, 11, 13, 16)

**Daring (semua diunduh/dibaca langsung 2026-10-25):**
10. ESP32-S3 Series Datasheet v2.2 (2026-03-05): https://www.espressif.com/sites/default/files/documentation/esp32-s3_datasheet_en.pdf
11. Halaman produk ESP32-S3: https://www.espressif.com/en/products/socs/esp32-s3
12. ESP-IDF v5.4 ESP32-S3 Wi-Fi Driver (tabel CSI & rekomendasi sniffer): https://docs.espressif.com/projects/esp-idf/en/v5.4/esp32s3/api-guides/wifi.html
13. esp-csi (master): https://github.com/espressif/esp-csi — README + `examples/get-started/{csi_send,csi_recv,csi_recv_router}` + `examples/esp-radar/console_test`
14. ESP32-CSI-Tool (master): https://github.com/StevenMHernandez/ESP32-CSI-Tool — README, `active_sta/main/main.cc`, `_components/{csi_component.h,sockets_component.h}`, `docs/bibtex/esp32_csi_tool_wowmom.bib`
15. esp-dl (master): https://github.com/espressif/esp-dl — README, `benchmark_report.md`, `models/{imagenet_cls,human_face_detect,coco_detect,yolo26,hand_gesture_recognition}/README.md`
16. esp-tflite-micro (master): https://github.com/espressif/esp-tflite-micro — README, `examples/{person_detection,micro_speech}/main/*` (ukuran model dihitung dari `person_detect_model_data.cc` & `model.cc`)
17. esp-nn (master): https://github.com/espressif/esp-nn — README (tabel performa)
18. ESP-IDF esp_wifi.h & esp_wifi_types_native.h (master): https://github.com/espressif/esp-idf/blob/master/components/esp_wifi/include/local/esp_wifi_types_native.h
19. ESP-NOW docs (master): https://docs.espressif.com/projects/esp-idf/en/latest/esp32s3/api-reference/network/esp_now.html (via sumber rst GitHub)

— Selesai T17-R2 —
