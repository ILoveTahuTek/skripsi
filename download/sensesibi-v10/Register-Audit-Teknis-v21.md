# Register Audit Teknis SenseSIBI v21

**Mandat:** SENSESIBI-PROPOSAL-AUDIT-QA-001 · **Tanggal audit:** 15 November 2026 · **Baseline:** `Proposal-SenseSIBI-Studi-Kelayakan-v20.pdf` (komi repositori skripsi `a0f2d7a`)
**Metode:** pembacaan langsung kode sumber, kartu model, artefak eksperimen, dan dokumen rancangan pada komit yang dikunci; unduhan dan penguraian header berkas bobot; penelusuran penuh pemanggil fungsi. Status: *PASS* (terverifikasi mendukung), *CONDITIONAL* (benar dengan batasan atau menuntut tindakan), *FAIL* (bertentangan dengan klaim naskah), *NOT VERIFIED* (menunggu artefak atau pengukuran).

## Artefak yang diaudit

| Sumber | Identitas dikunci | Perubahan terakhir |
|---|---|---|
| RuView | komit `3bae24a1231e0d9809e84eb35edba7231b8d1913`, firmware `esp32-csi-node` v0.8.18 | 13 Nov 2026 |
| HF `ruvnet/wifi-densepose-pretrained` | `sha` `98b29a35f962996d6e8207e4f46818dedb5764d5` | 13 Okt 2026 |
| WPC (`ILoveTahuTek/WPC`, privat) | komit `249a63dff4a7` | 2 Nov 2026 |
| wifi-sensing-kit | komit `7fb77fc0c0adb98bcf0a102d68fa8718b2f98625` (dasar RuView tag v0.8.8-esp32, `e04f269f`) | 11 Okt 2026 |
| DensePose From WiFi | arXiv:2301.00250v1 (31 Des 2022), DOI 10.48550/arXiv.2301.00250 | tetap |
| Naskah v20 | komi `a0f2d7a`; jalur ringkas `35c1ade` terdokumentasi terpisah | 14 Nov 2026 |

## Register temuan

### AUD-01 — Injeksi NDP masih stub tanpa pemanggil · KRITIS · FAIL (klaim lama)

**Temuan:** Fungsi `csi_inject_ndp_frame()` berlabel "ADR-029: NDP frame injection stub". Ia membangun bingkai Null Data 24 byte (FC 0x0048, Addr1/Addr3 broadcast) lalu memancarkannya lewat `esp_wifi_80211_tx()` sebagai penampung agar antarmuka terhubung; komentar TODO menyatakan bingkai NDP sesungguhnya belum dibangun. Penelusuran seluruh pohon kode menemukan nol pemanggil fungsi ini. Berkas `rv_radio_ops_esp32.c` menegaskan perilaku TX menunggu pengendali: "actual TX behavior is triggered by the controller calling csi_inject_ndp_frame() directly once the controller PR lands."

**Bukti:** `firmware/esp32-csi-node/main/csi_collector.c:940-982` (komentar stub + TODO + konstruksi bingkai); `firmware/esp32-csi-node/main/rv_radio_ops_esp32.c:84-88`; `docs/adr/ADR-029-ruvsense-multistatic-sensing-mode.md` (Status: Proposed, 2026-03-02, diperbarui 2026-10-04); README firmware diagram arsitektur menampilkan blok "NDP Inject" (janji dokumentasi, bukan implementasi).

**Dampak dan koreksi:** Narasi v20 ("TX menyuntikkan bingkai sounding NDP") tidak didukung kode. Koreksi v21: Batasan no. 12, Tabel 2.1 baris 2, 2.3, 3.4, Tabel 3.1 baris 1, 3.5, Gambar 3.3, kriteria G0, Tabel 3.7 no. 22, Tabel 3.8 no. 13. **Gerbang:** G0.

### AUD-02 — Sumber CSI aktual terverifikasi · PASS

**Temuan:** Akuisisi CSI berjalan lewat API ESP-IDF (`esp_wifi_set_csi_config` dengan `acquire_csi_force_lltf=1`, `lltf_en=true`; `esp_wifi_set_csi_rx_cb`; `esp_wifi_set_csi(true)`) pada mode promiscuous; filter MGMT bawaan dinaikkan ke MGMT+DATA untuk papan tanpa layar (isu #893). Sumber trafik ialah self-ping ke gateway: `CONFIG_CSI_SELF_PING_HZ` baku 50, rentang tervalidasi perangkat keras 10-50 (`#error` di luar rentang); komentar menyebut jaminan "lantai OFDM unicast ~50 Hz" dari balasan ICMP router. Laju pelaporan CSI dibatasi `CSI_MIN_PROCESS_INTERVAL_US = 20*1000` (50 Hz).

**Bukti:** `csi_collector.c:67-75` (rentang self-ping), `:109-116` (batas 50 Hz), `:415-430` (komentar #954 lantai OFDM), `:523-534` dan `:678-743` (promiscuous + konfigurasi CSI + `WIFI_PS_NONE`), `:895-916` (peningkatan filter MGMT+DATA).

**Dampak:** Mendukung klaim naskah "paling sering setiap 20 ms atau 50 bingkai per detik; laju aktual diukur T0". G0 tetap mengukur laju aktual. **Gerbang:** G0.

### AUD-03 — Atribusi bingkai ke pengirim belum tersedia · CONDITIONAL

**Temuan:** Bingkai CSI ADR-018 baku tidak memuat MAC pengirim. Kit wifi-sensing-kit menambahkan 6 byte MAC TX pada bingkai (bit 7 byte 19) beserta penyaringan bingkai hanya dari router/papan lewat patch di atas firmware yang sama, dan itulah yang membuat tautan antar-papan (R>1, 2>3) dapat dipisahkan di sisi server.

**Bukti:** `firmware/ruview-v0.8.8-kit.patch:12-13` (penyaringan pengirim); `kit/server.py:5-8` (format 0xC5110001 + MAC TX kondisional bit 7 byte 19); `NOTICE.md` kit (modifikasi `main.c` dan `csi_collector.c`).

**Dampak dan tindakan:** Konfigurasi dua node peran tetap membutuhkan penandaan atau penyaringan MAC agar tautan TX-RX terisolasi. Tindakan: patch minimal berpola kit [34] diaudit dan diuji pada T0 (QA-FW-04); tercatat sebagai penyimpangan terdokumentasi. **Gerbang:** G0.

### AUD-04 — Format UDP ADR-018 terverifikasi · PASS

**Temuan:** Magic `0xC5110001` (CSI) dan `0xC5110002` (vitals) ke port 5005; header 20 byte memuat banyak subcarrier, tanda PPDU, dan bendera; empat byte I/Q pertama dinolkan lalu ditandai `CSI_FLAG_FIRST_WORD_SANITIZED` bila `first_word_invalid`; terdapat penghitung validitas HE; sinkronisasi lintas node menandai bit 4 byte 19 dari kanal ESP-NOW (ADR-110) atau 802.15.4 (C6).

**Bukti:** `csi_collector.c:157-215` (serialisasi ADR-018), `:260-293` (sanitasi first_word_invalid), `:284-293` (bit sinkronisasi), `edge_processing.h:17-28`; panduan pengguna `docs/user-guide.md:379`.

**Dampak:** Konsisten dengan klaim 2.2, 2.3, dan kriteria G0. Parser diuji QA-ACQ-07. **Gerbang:** G0.

### AUD-05 — ESP-NOW hanya sinkronisasi mesh · PASS

**Temuan:** ESP-NOW dipakai `c6_sync_espnow` sebagai jalur sinkronisasi waktu lintas node (solusi D1 atas 802.15.4 yang rusak pada IDF v5.4), bukan pengangkut bingkai CSI. **Bukti:** `csi_collector.c:266-280`; `main.c:343-345` ("ADR-110 D1 workaround: ESP-NOW cross-node sync… Works on both S3 and C6"). **Dampak:** Konsisten keputusan Tabel 3.7 no. 21. **Gerbang:** G0.

### AUD-06 — Mesh multistatik 3-6 node TDM berstatus konfigurasi lanjutan · PASS (dokumentasi), NOT VERIFIED (dua node)

**Temuan:** Panduan pengguna mendokumentasikan "deploy 3-6 ESP32-S3 nodes in a multistatic mesh… each node acts as both transmitter and receiver" dengan protokol TDM, dan menunjuk ADR-029/ADR-032 untuk rancangan penuh (keduanya Proposed). Konfigurasi dasar setiap node mengalirkan UDP 5005 mandiri. Konfigurasi dua node peran tetap bukan konfigurasi terdokumentasi sehingga tetap wajib diuji pada perangkat nyata.

**Bukti:** `docs/user-guide.md:85` (tabel biaya, catatan jujur pose 17 keypoint), `:440-460` (mesh advanced + TDM). **Dampak:** Konsisten dengan catatan verifikasi 2.3 dan risiko Tabel 3.8 no. 13. **Gerbang:** G0.

### AUD-07 — NUL-padding model.safetensors telah diperbaiki · CONDITIONAL (klaim naskah basi)

**Temuan:** Klaim v20 bahwa `model.safetensors` "ditolak oleh safetensors.torch.load_file" sudah usang: komit HEAD repo model berjudul "Fix NUL-padded safetensors header (RuView #1522)" (2026-10-13) mengganti byte padding NUL dengan spasi JSON. Verifikasi ulang atas berkas terunduh menunjukkan header 1.464 byte tanpa satu pun byte NUL dan 17 tensor termuat utuh (verifikasi mandiri: muat ulang safetensors sukses).

**Bukti:** `https://huggingface.co/api/models/ruvnet/wifi-densepose-pretrained/commits/main` (sha `98b29a35`, pesan komit); sha256 berkas `17c9acc1…11a1` cocok dengan penunjuk LFS. **Dampak dan koreksi:** Paragraf 2.4 diperbarui; audit T0 tetap memverifikasi pemuatan langsung. **Gerbang:** T0.

### AUD-08 — Dua keluarga berkas dengan metadata saling bertentangan · CONDITIONAL

**Temuan:** Keluarga `model.safetensors`/`config.json`/`training-metrics.json` (dari skrip latih berbeda) mencatat 20 epoch, temperatur InfoNCE 0,07, pasangan positif 1 s dan negatif 10 s, LoRA rank 8/alpha 16; paragraf teknis kartu untuk keluarga `csi-embed-v2` mencatat 60 epoch, temperatur 0,1, positif ≤2 s dan negatif >30 s, LoRA "rank-4", sementara `node-1.json`/`node-2.json` memuat rank 4/alpha 8. `model.rvf.jsonl` tidak terdokumentasi pada tabel berkas kartu; klaim "Training time 12 minutes" bertentangan dengan `totalDurationMs` ≈ 34,9 menit; Quick Start kartu menunjuk repo `ruv/ruview` yang keliru.

**Bukti:** `config.json`, `training-metrics.json`, `model.rvf.jsonl`, `node-1.json`, `node-2.json`, README kartu (semua pada repo model sha `98b29a35`). **Dampak dan tindakan:** Pemilihan keluarga berkas wajib eksplisit di T0 beserta rekonsiliasi angka; Tabel 3.7 no. 6 diperluas; kutipan naskah memakai cakupan keluarga `csi-embed-v2`. **Gerbang:** T0, G0b.

### AUD-09 — Catatan SISO ada di README RuView, bukan kartu model · PASS (dengan koreksi kutipan)

**Temuan:** Peringatan "single-antenna, 56-subcarrier CSI stream at a 20-frame window does not carry the fine-grained spatial information the multi-antenna NIC research relies on… distal/face joints near-random" tercantum pada README utama RuView (isu #509). Kata "SISO" tidak muncul di mana pun pada kartu model HF. **Bukti:** `README.md:342-346` RuView; penelusuran nol kemunculan pada seluruh berkas kartu. **Koreksi:** Kutipan 2.4 dari "[10], [11]" menjadi "[10]". **Gerbang:** -.

### AUD-10 — Kontrak encoder terverifikasi · PASS

**Temuan:** Kartu menyatakan "8-dim features @ 1 Hz → Encoder → 128-dim embedding"; arsitektur dua lapis FC (BatchNorm+GELU), 9.280 parameter, ternormalisasi L2; triplet-temporal held-out 82,3% (pembanding fitur mentah 66,4%, encoder acak 69,6%) diukur pada 20% akhir rekaman menurut waktu; EWC Fisher 2000 dengan tingkat lupa 32,97% pada empat tugas; supervisi PIR + BME280; data 60.630 sampel dari 2 node ESP32-S3 selama 8 jam; lisensi MIT. `csi-embed-v2.py` memastikan bentuk masukan `[B, 8]` dan keluaran `[B, 128]`.

**Bukti:** README kartu; `csi-embed-v2.py` ("x: [B, 8] standardized CSI features"); `csi-embed-v2-metrics.json` (6.063 frame; train 4.850; heldout 1.213); `training-metrics.json` (triplet 610.615). **Dampak:** Konsisten Subbab 2.4. **Gerbang:** G0b.

### AUD-11 — Varian kuantisasi tersedia, kinerja tugas belum teruji · NOT VERIFIED (kinerja tugas)

**Temuan:** Repo model memuat `model-q2.bin` (4.096 B), `model-q4.bin` (8.192 B), `model-q8.bin` (16.384 B), dan `csi-embed-v2-int4.bin` (4.672 B, "fits the 8 KB ESP32 SRAM budget") beserta standardizer FP16 pada `csi-embed-v2.py`. Metrik RMSE pada berkas: q2 0,3396; q4 0,0576; q8 0,0027. Kinerja varian kuantisasi pada tugas SIBI tidak teruji siapa pun. **Bukti:** daftar berkas + `csi-embed-v2-metrics.json`. **Dampak:** Menjadi objek QA-EDGE-02/03. **Gerbang:** G1, G3.

### AUD-12 — Visibilitas label guru konstan · KRITIS · CONDITIONAL

**Temuan:** `write_label()` menuliskan nilai `'2'` (terlihat) untuk setiap keypoint tanpa pemeriksaan oklusi: `parts += [f'{x:.6f}', f'{y:.6f}', '2']`. Konsekuensinya seluruh label dataset v2 memakai visibilitas konstan; nilai itu tidak membawa informasi oklusi dan tidak boleh diperlakukan sebagai ground truth visibility. Pada inferensi, komponen ketiga keluaran model berperilaku sebagai skor keyakinan yang dapat dipakai sebagai saringan kualitas.

**Bukti:** `scripts/convert_sibi_v2.py:286-297` (WPC komit `249a63d`); `docs/DATASET_V2.md` (tidak membahas visibilitas). **Dampak dan tindakan:** Kebijakan mask diperjelas pada 2.7, 2.9, Tabel 3.8 no. 14, QA-DS-02: mask efektif = penanda langkah valid + saringan kualitas deteksi + verifikasi sampel validator; perbaikan pipeline anotasi didokumentasikan sebelum label dipakai. **Gerbang:** G0b, G1.

### AUD-13 — flip_idx identitas terverifikasi empiris · PASS

**Temuan:** Konverter v2 memverifikasi pemetaan flip secara empiris (flip gambar, deteksi ulang, voting bijeksi greedy; n=16, konsistensi 0,91) menghasilkan `flip_idx` identitas; dokumentasi menyatakan permutasi COCO-WholeHand v1 salah untuk urutan MediaPipe sehingga augmentasi fliplr v1 merusak semantik keypoint, dan hal itu diperbaiki. **Bukti:** `convert_sibi_v2.py:422-466`; `DATASET_V2.md` butir 5. **Dampak:** Urutan 21 keypoint MediaPipe dikunci sebagai konvensi. **Gerbang:** G1.

### AUD-14 — Komposisi dataset v2 terverifikasi · PASS

**Temuan:** Empat sumber (Roboflow sibi-bieme v2 5.831 gambar 49 kelas bbox label manusia CC BY 4.0; Kaggle combined 2.306; lemlitbang RAW 525 + V02 1.291); 9.953 ditemukan; dedup md5 persis −2.215; leak-guard dHash (ambang Hamming ≤8) −18 khusus Kaggle yang mirip val/test; MediaPipe 7.210 sukses, 510 gagal (6,6%, terkonsentrasi kelas kata dua tangan); 417 gambar dua tangan (2 objek); total 7.627 objek; split terkunci train 6.231 / val 650 / test 329; split resmi Roboflow dipakai verbatim (audit source-stem: 0 bocor lintas split, 3.430 sumber unik); Kaggle hanya masuk train; near-dupe di dalam train dipertahankan dengan dokumentasi jujur; varian augmentasi Roboflow dalam split yang sama (2.401 sumber) dinyatakan aman.

**Bukti:** `docs/DATASET_V2.md` (angka resmi + catatan); `convert_sibi_v2.py` (logika dedup/leak-guard/gating dua tangan). **Dampak:** Konsisten klaim 2.9. **Gerbang:** G1.

### AUD-15 — exp11_huruf24 = A sampai Y tanpa J dan Z · PASS (menjawab penanda terbuka)

**Temuan:** Eksperimen `exp11_huruf-murni-24` melatih ulang resep juara exp06b (60 epoch, yolo26m-pose, batch 16 DDP, pose 16, kobj 3, mosaic 0,3, lr0 0,004 kosinus, seed 42) pada dataset v2 yang sama dengan penyaringan runtime: hanya gambar memuat minimal satu huruf statis (4.054 dari 6.231 train) dan label dipetakan ulang ke 24 kelas huruf (A-Y tanpa J dan Z); dataset 49 kelas tidak diubah. Evaluasi pada 333 instance huruf validasi: pose mAP50 0,9580; mAP50-95 0,7235; box mAP50 0,9942; box mAP50-95 0,8918. Pada conf 0,25: 325/333 (97,6%) benar; 8 galat = 5 pertukaran (M→N, T→S, T→X, U→R, V→K) + 3 tak terdeteksi (N, Q, W).

**Bukti:** `README.md` WPC bagian "Evaluasi murni 24 huruf (exp11)"; `experiments/kaggle/exp11_huruf24/SUMMARY.json` (dataset_counts, val_split 333/317); folder eksperimen memuat confusion matrix dua ambang, kernel latih dan evaluasi, metrik per kelas. **Dampak:** Penanda [PERLU VALIDASI: kelas J dan Z pada model juara WPC] terjawab; 2.9 diperbarui; supervisi J/Z tetap dari lintasan keypoint dan kartu protokol. **Gerbang:** G1.

### AUD-16 — Bobot exp11 belum diarsipkan · NOT VERIFIED (artefak)

**Temuan:** Folder `experiments/kaggle/exp11_huruf24/` memuat metrik, kernel, dan konfigurasi, tetapi tidak memuat berkas bobot; `weights/MANIFEST.json` hanya mencatat exp00-exp10 dan exp06b (juara 49 kelas: `yolo26m_pose_sibi_exp06b_kpt_gain_best.pt`, sha256 `073ccf71e94bb89425519a746dc0e22a1a04dd826b65c4bb94afa753b0ab3ea0`, 50.532.034 byte). **Bukti:** pohon repo pada komit `249a63d`; MANIFEST.json. **Tindakan:** Pemilik menerbitkan tag rilis dan hash bobot exp11; penanda [PERLU DATA] pada rujukan [12] tetap berlaku. **Gerbang:** -.

### AUD-17 — Pelatihan guru deterministik · PASS

**Temuan:** Seluruh eksperimen memakai seed 42 dan dicatat sebagai deterministik lintas lingkungan; buku besar eksperimen lengkap (exp00 sampai exp11) dengan jejak ratchet (exp00 0,8445 → exp03 0,8553 → exp05 0,8578 → exp10 0,8888 → exp06b 0,8944). **Bukti:** README WPC; MANIFEST.json; SUMMARY.json. **Dampak:** Keterulangan pra-penelitian terdukung. **Gerbang:** G1.

### AUD-18 — wifi-sensing-kit adalah kit orkestrasi di atas firmware RuView · PASS (sebagai pola)

**Temuan:** Kit (MIT, 4 komit, 10-11 Okt 2026, 206 bintang, 0 isu) terdiri atas skrip bangun/flash/provisioning Python, dasbor, dan patch kecil; firmware CSI diunduh saat build dari RuView tag v0.8.8-esp32 dan dipatch (penyaringan bingkai router/papan + penambahan MAC TX). Kit tidak memiliki injeksi NDP (stub yang sama), tidak memakai peran TX/RX tetap (semua papan simetris self-ping dan saling mendengar), laju dibatasi ~50 Hz dibagi antar tautan, 52 subcarrier valid (indeks 1-26 dan 38-63), hanya ESP32-S3, ESP-IDF v5.4/5.5, tidak memakai pustaka esp-csi, power save dimatikan.

**Bukti:** `README.md` kit; `firmware/build.py:63`; `firmware/flash.py:21`; `NOTICE.md`; `kit/server.py:5-8,26-28`; `docs/how-it-works.md:10-12,22`; patch kit. **Dampak:** Tidak menjadi komponen inti; dipakai sebagai pola atribusi MAC (AUD-03) dan opsi jalur pembanding pasif. **Gerbang:** G0.

### AUD-19 — DensePose From WiFi pracetak tanpa konten tangan · CONDITIONAL

**Temuan:** Makalah (Geng, Huang, De la Torre; CMU) hanya ada sebagai pracetak arXiv v1 (31 Des 2022; templat ACM dengan CCS Concepts, tanpa jejak penerimaan bertelaah sejawat; DBLP mencatat jurnal CoRR). Setup: 3 antena TX × 3 antena RX, 30 subcarrier (2,4 GHz ± 20 MHz), CSI 100 Hz tersinkron dengan video 20 FPS; keluaran IUV 24 wilayah tubuh + 17 keypoint tubuh COCO; ground truth berupa pseudo-GT dari DensePose-RCNN dan Keypoint R-CNN citra. Nol kemunculan "finger/hand/wrist/palm" sebagai objek. Terdapat inkonsistensi internal (AP@75 35,6 pada teks lawan 44,6 pada tabel; Tabel 2 lawan Tabel 4/6) dan penurunan drastis lintas tata ruang (AP 43,5 → 27,3).

**Bukti:** `ref-73_Geng-2023-DensePoseWiFi.pdf` (13 hlm, salinan lokal); https://arxiv.org/abs/2301.00250. **Dampak:** Nama `wifi-densepose-pretrained` adalah penamaan lini riset, bukan warisan teknis makalah; dikutip sebagai latar dengan label pracetak [35] pada 3.12. **Gerbang:** -.

### AUD-20 — Pemisahan model pose MM-Fi konsisten · PASS

**Temuan:** `ruvnet/wifi-densepose-mmfi-pose` adalah checkpoint terpisah (masukan amplitudo CSI [3,114,10] @ 100 Hz, Transformer 4 lapis 8 kepala, keluaran [17,2] keypoint tubuh COCO; ±2,3 juta parameter; PCK@20 82,69% random split, 83,59% ansambel; lintas subjek zero-shot ±64%, lintas lingkungan 17,5%, naik 72-78% setelah kalibrasi; lisensi CC BY-NC 4.0 mengikuti data MM-Fi [16]). **Bukti:** kartu model mmfi-pose (audit 13-14 Nov 2026, sesi sebelumnya) + naskah 2.4. **Dampak:** Pemisahan tiga model pada Tabel 2.2 konsisten. **Gerbang:** G0b.

## Rekapitulasi

| Status | Jumlah | Temuan |
|---|---|---|
| PASS | 10 | AUD-02, AUD-04, AUD-05, AUD-09, AUD-10, AUD-13, AUD-14, AUD-15, AUD-17, AUD-18, AUD-20 (AUD-06 sebagian) |
| CONDITIONAL | 6 | AUD-03, AUD-06 (dua node), AUD-07, AUD-08, AUD-12, AUD-19 |
| FAIL | 1 | AUD-01 (klaim naskah lama; telah dikoreksi) |
| NOT VERIFIED | 3 | AUD-06 (dua node), AUD-11, AUD-16 |

Tautan sumber: https://github.com/ruvnet/RuView (komi 3bae24a) · https://huggingface.co/ruvnet/wifi-densepose-pretrained (sha 98b29a35) · https://github.com/ILoveTahuTek/WPC (komi 249a63d, privat) · https://github.com/andrisgauracs/wifi-sensing-kit (komi 7fb77fc) · https://arxiv.org/abs/2301.00250 · repositori skripsi (komi a0f2d7a untuk v20).
