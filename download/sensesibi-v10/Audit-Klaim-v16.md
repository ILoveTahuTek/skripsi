# Matriks Klaim → Bukti (Gelombang 16)

Tanggal: 13 November 2026. Metode verifikasi: halaman sumber dibuka langsung (WebFetch) pada 13 Nov 2026, kecuali yang berstatus data pemilik. Setiap klaim pada naskah v16 dipetakan ke sumber di bawah ini; klaim tanpa baris pada tabel ini tidak boleh masuk naskah.

## A. Klaim terverifikasi lewat sumber terbuka

| No. | Klaim pada naskah | Sumber bukti | Status | Perlakuan pada naskah |
|---|---|---|---|---|
| 1 | Encoder CSI terpralatih: masukan 8 fitur CSI, keluaran embedding 128 dimensi ternormalisasi L2, arsitektur dua lapis FC (BatchNorm + GELU), 9.280 parameter | Kartu model HF ruvnet/wifi-densepose-pretrained (dibuka 13 Nov 2026) | Terverifikasi | Subbab 2.3; dimensi masukan diberi catatan [PERLU VALIDASI] karena laju fitur 1 Hz pada kartu model |
| 2 | Pelatihan encoder: triplet loss + InfoNCE, temperatur 0,1, positif temporal ≤ 2 s, negatif > 30 s, 60 epoch AdamW, EWC anti-lupa | Kartu model yang sama | Terverifikasi | Subbab 2.3 diringkas |
| 3 | Akurasi triplet-temporal held-out 82,3% (pembanding fitur mentah 66,4%, encoder acak 69,6%), diukur pada 20% akhir rekaman menurut waktu; definisi P(d(anchor, positif) < d(anchor, negatif)) | Kartu model yang sama | Terverifikasi | Subbab 2.3 + penegasan bahwa angka ini BUKAN akurasi SIBI |
| 4 | Ukuran berkas encoder: 48 KB penuh; 4 KB (2-bit), 8 KB (4-bit), 16 KB (8-bit) kuantisasi; lisensi MIT | Kartu model yang sama | Terverifikasi | Subbab 2.9 |
| 5 | Adapter LoRA ruangan node-1.json dan node-2.json (±21 KB) tersedia pada checkpoint yang sama | Kartu model yang sama | Terverifikasi | Subbab 2.4; kompatibilitas untuk tugas SIBI tetap [PERLU VALIDASI] |
| 6 | Model pose MM-Fi terpisah: masukan amplitudo CSI [3, 114, 10] (3 pasang antena, 114 subcarrier, 10 bingkai @ 100 Hz), Transformer 4 lapis 8 kepala, ±2,3 juta parameter, keluaran [17, 2] keypoint tubuh COCO dalam [0,1] | Kartu model HF ruvnet/wifi-densepose-mmfi-pose (dibuka 13 Nov 2026) | Terverifikasi | Subbab 2.3 + Tabel 2.1; 17 keypoint tubuh BUKAN 21 keypoint tangan |
| 7 | PCK@20 ternormalisasi badan: model tunggal 82,69%, ansambel+TTA 83,59%, SOTA sebelumnya (MultiFormer 2025) 72,25%; lintas subjek zero-shot ±64%; lintas lingkungan 17,5%; kalibrasi ±1000 bingkai per orang 78,3% | Kartu model yang sama | Terverifikasi | Subbab 2.3 dan 2.8 sebagai pembanding ekspektasi generalisasi |
| 8 | Lisensi CC BY-NC 4.0 melekat pada model pose MM-Fi karena data MM-Fi | Kartu model yang sama | Terverifikasi | Subbab 2.3 catatan lisensi |
| 9 | ADR-146 (status Proposed): RfEncoder bersama d_model 64, tujuh kepala tugas, ketidakpastian per kepala, HeadMask, ABI Rust f32, syarat waktu nyata 20 Hz | docs/adr/ADR-146 RuView (dibuka 13 Nov 2026) | Terverifikasi sebagai RANCANGAN (belum diimplementasikan) | Subbab 2.7; dilabeli eksplisit "berstatus Proposed" |
| 10 | ADR-150 (status Proposed): foundation encoder; LoRA ±11 KB; ±100–200 sampel berlabel per ruang → ±72%; temuan negatif pretraining kontrastif-pose tidak pernah meninggalkan lantai kemiripan seragam ln(B); kesenjangan 18 poin dalam domain vs lintas subjek = pergeseran distribusi subjek pada CSI | docs/adr/ADR-150 RuView (dibuka 13 Nov 2026) | Terverifikasi sebagai RANCANGAN + catatan temuan internal | Subbab 2.4 dan 3.13; angka dilabeli estimasi rancangan, bukan hasil terukur penelitian ini |
| 11 | MM-Fi: 40 subjek, 27 kategori aksi, >320 ribu bingkai tersinkron, NeurIPS 2023 Datasets and Benchmarks, CC BY-NC 4.0 | arXiv:2305.10345 + halaman proyek (dicari 13 Nov 2026) | Terverifikasi | Daftar Pustaka [16] + konteks subbab 2.3 |
| 12 | MediaPipe Hands: 21 landmark tangan per tangan | arXiv:2006.10214 (dicari 13 Nov 2026) | Terverifikasi | Subbab 2.6 dan 2.8 |
| 13 | LoRA: adaptasi peringkat rendah W' = W0 + BA | Hu dkk., ICLR 2022 | Kanonik, terverifikasi lewat penelusuran | Subbab 2.4 |
| 14 | Smooth L1 | Girshick, Fast R-CNN, ICCV 2015 | Kanonik | Subbab 2.6 |
| 15 | Multitask learning berbagi representasi | Caruana, Machine Learning 28(1), 1997 | Kanonik | Subbab 2.7 |
| 16 | Distilasi pengetahuan / pola guru-murid | Hinton dkk., arXiv:1503.02531 | Kanonik | Subbab 2.8; dipakai untuk leluhur pola guru-murid, bukan untuk mengklaim distilasi soft target |
| 17 | Klaim v15 yang dipertahankan (juru bahasa ±500 vs 1,92 juta [1]; UU 8/2016 [2]; Kamus SIBI [3]; survei 91% BISINDO [4]; CNN BISINDO [5]; survei CSI [6]; SignFi [7]; datasheet ESP32-S3 [8]; esp-csi 56 subcarrier [9]; RuView firmware 50 bingkai/dtk, kalibrasi 600 bingkai 8 anchor [10]; Fresnel/Doppler/Nyquist/CSI-ratio [6],[13]; Widar3.0 [14]; ESP-DL [22]; Ultralytics [12]) | Terverifikasi pada gelombang sebelumnya (lihat catatan-pengemasan.md) | Terverifikasi | Dibawa utuh dengan nomor baru |

## B. Data pemilik (repositori peneliti, tidak masuk Daftar Pustaka)

| No. | Klaim | Sumber | Perlakuan |
|---|---|---|---|
| 18 | Dataset visual WPC v2: 49 kelas, 7.210 gambar (6.231 latih, 650 validasi, 329 uji), kpt_shape [21, 3], keypoint hasil pseudo-labeling MediaPipe HandLandmarker, model visual YOLO26m-Pose (bukan YOLOv6m-Pose) | AGENT BRIEF pemilik + repositori ILoveTahuTek/WPC (privat; raw URL 404 saat dicek 13 Nov 2026) | Dilaporkan sebagai data pra-penelitian repositori peneliti (Subbab 2.8, Tabel 3.2); bukti fisik berupa repositori, skrip, dan log eksperimen milik pemilik |
| 19 | Eksperimen exp11_huruf24: mAP50 0,8944 pada 49 kelas; mAP50 0,9580 dan akurasi huruf 97,6% pada 24 huruf statis; 24 huruf statis termasuk C; J dan Z dinamis | Sumber yang sama | Subbab 2.8; ditegaskan sebagai hasil model visual pada data visual, bukan hasil model Wi-Fi |
| 20 | Skrip WPC train_sibi_v2.py, inference_sibi.py | Sumber yang sama | Tabel 3.2 perangkat lunak |

## C. Klaim yang dilarang (tidak boleh muncul di naskah)

1. YOLO26m-Pose disebut sebagai encoder CSI.
2. Pose 17 keypoint MM-Fi disebut sebagai 21 keypoint tangan.
3. 82,3% disebut sebagai akurasi SIBI.
4. WPC dinyatakan sudah memiliki pasangan CSI tersinkron.
5. LoRA dinyatakan tersedia untuk setiap checkpoint tanpa verifikasi.
6. Dimensi masukan, panjang jendela, atau sistem koordinat target ditetapkan sebagai angka pasti sebelum Tahap 1/3 (semua diberi [PERLU VALIDASI]).
7. Hasil mAP YOLO dipakai sebagai hasil model Wi-Fi.
8. Deployment ESP32-S3 dinyatakan berhasil sebelum pengukuran perangkat fisik.
9. Referensi atau hasil eksperimen fiktif.
