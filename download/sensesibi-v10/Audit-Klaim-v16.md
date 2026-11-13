# Matriks Klaim → Bukti (Gelombang 16, Brief v2 — Revisi Additif)

Tanggal: 13 November 2026. Metode verifikasi: halaman sumber dibuka langsung (WebFetch) pada 13 Nov 2026, kecuali yang berstatus data pemilik. Prinsip brief v2: revisi additif — sistem dua arah SenseSIBI utuh dipertahankan; hanya blok model jalur SIBI menjadi teks yang diperbarui menjadi encoder CSI terpralatih + dua kepala tugas.

## A. Tabel perubahan per bagian (bagian → masalah → revisi → alasan sumber)

| Bagian | Masalah pada naskah acuan | Revisi | Alasan (sumber) |
|---|---|---|---|
| Judul & identitas | Judul dokumen acuan pemilik memakai "CLOUD PROCESSING" | Judul mengikuti dokumen acuan pemilik | Brief v2 §2.1 |
| 1.1 Latar belakang | Uraian model lama "distilasi pengetahuan guru ke murid backbone WiFi-DensePose" | Paragraf model ditulis ulang: encoder terpralatih beku + dua kepala; guru visual YOLO26m-Pose pemberi label; istilah distilasi dikoreksi | Kartu model encoder [11]; brief v2 §6.1 |
| 1.2-1.3 Rumusan & tujuan | Butir model menyebut distilasi + kepala 1D-CNN + pembanding SVM | Butir pertama dan kedua diperbarui: dua kepala tugas, supervisi lintas modalitas, ablasi; SVM diganti pembanding ablasi kepala tunggal | Brief v2 §7 BAB I, §8 |
| 1.4 Batasan | Tidak ada butir encoder checkpoint | Tambah butir encoder checkpoint + audit bentuk masukan + status LoRA sebagai pembanding opsional | Brief v2 §3A pemeriksaan kompatibilitas |
| 2.3 RuView | Baris tabel memetakan "WiFi-DensePose int8 sebagai backbone murid" | Baris diganti checkpoint encoder terpralatih (embedding 128) beku pada baseline | Kartu model [11] |
| 2.4 (baru) Encoder terpralatih | Tidak ada subbab; tiga model ekosistem RuView berisiko tercampur | Subbab baru + Tabel pembedaan: encoder CSI 8 fitur→128 (9.280 param), model pose MM-Fi 17 keypoint tubuh (terpisah), YOLO26m-Pose guru visual | Kartu model [11], [15]; dataset MM-Fi [16] |
| 2.5 (baru) Transfer learning | Tidak ada | Frozen encoder baseline; LoRA W=W0+BA sebagai opsi (bukan prasyarat); fine-tuning pembanding | LoRA [17]; brief v2 §5.1 |
| 2.6-2.8 (baru) Kepala klasifikasi, kepala regresi, multitugas | Matematika klasifikasi/regresi/multitugas belum ada; isu temporal J/Z dan istilah 1D-CNN belum ditangani | Persamaan logits-softmax-CE, reshape+Smooth L1 bermask, joint loss terbobot, aturan pembaruan θ0 beku; modul temporal (1D-CNN warisan) dievaluasi sebagai komponen antara, bukan kepala | Brief v2 §4-§5; Smooth L1 [20]; multitask [21] |
| 2.9 Guru visual | "Distilasi pengetahuan" dipakai untuk label keras | Istilah dikoreksi: supervisi lintas modalitas berpandu guru / pseudo-label; KD klasik hanya disebut sebagai leluhur konsep; status pseudo-label dinyatakan | Brief v2 §6.1; Hinton [22] |
| 2.14 Evaluasi | Metrik hanya klasifikasi + WER | Tambah MPJPE, NME, PCK@α dengan definisi koordinat dan ambang | Brief v2 §7 BAB III |
| 3.7 Pelatihan | "Backbone WiFi-DensePose int8 berkepala 1D-CNN" + SVM pembanding | Ditulis ulang: audit bentuk masukan (8 fitur @1 Hz vs 56 subcarrier @50 Hz) + adapter masukan; encoder per bingkai + modul temporal; joint loss; ablasi; LoRA/fine-tune opsional; pelatihan Python/PyTorch; ekspor realistis | Kartu model [11]; brief v2 §3A, §9 |
| 3.8 Uji & gerbang | G1 tidak menilai manfaat dua kepala | 3.8.2 menjadi uji klasifikasi dan regresi (ablasi berdampingan); G1 menambah manfaat multitugas dari ablasi | Brief v2 §8 |
| Tabel 3.7/3.8 | Parameter dan risiko model lama | Tambah parameter bentuk masukan/adapter, λ, T, r LoRA, koordinat, ambang PCK; tambah risiko ketidaksesuaian masukan dan konflik gradien | Brief v2 §10 |
| Seluruh bagian sistem | Tidak ada masalah | TTS/ASR, pemetaan teks→SIBI, server/cloud, topologi, pinout, enclosure, uji pengguna, validator, biaya, G0-G4, jadwal DIPERTAHANKAN | Brief v2 §1 |

## B. Klaim terverifikasi lewat sumber terbuka (dibuka 13 Nov 2026)

| No. | Klaim pada naskah | Sumber bukti | Catatan |
|---|---|---|---|
| 1 | Encoder: 2 lapis FC (BatchNorm+GELU), 8 fitur → embedding 128-d ternormalisasi L2, 9.280 parameter; triplet+InfoNCE τ=0,1; positif ≤2 s, negatif >30 s; 60 epoch AdamW; EWC kuat 2000; split temporal 80/20 | Kartu model HF ruvnet/wifi-densepose-pretrained + docs/huggingface/MODEL_CARD.md repo RuView (dua sumber konsisten) | Subbab 2.4 |
| 2 | 82,3% = akurasi triplet-temporal held-out (P(d(anchor,positif)<d(anchor,negatif)) pada 20% akhir rekaman menurut waktu); pembanding 66,4% fitur mentah, 69,6% encoder acak; BUKAN akurasi SIBI | Sumber sama | Penegasan wajib di 2.4 |
| 3 | **Ketidaksesuaian bentuk masukan**: kartu model mencatat 8 fitur turunan @1 Hz (kehadiran, gerak, napas, detak jantung, varians fase, jumlah orang, deteksi jatuh, RSSI), bukan 56 subcarrier mentah @50 bingkai/dtk → adapter masukan/front-end wajib diaudit | Sumber sama + esp-csi [9] | Temuan utama; subbab 2.4 + 3.7 + risiko |
| 4 | Berkas: 48 KB penuh; model-q8 16 KB, q4 8 KB, q2 4 KB; presence-head 2,6 KB; adapter LoRA ruangan node-1.json/node-2.json ±21 KB; lisensi MIT | Sumber sama | Subbab 2.4, 2.5 |
| 5 | Model pose MM-Fi terpisah: masukan [3,114,10] amplitudo CSI @100 Hz, Transformer 4 lapis 8 kepala, keluaran [17,2] keypoint tubuh COCO dalam [0,1], ±2,3 juta parameter; PCK@20 82,69% (ansambel 83,59%, MultiFormer 72,25%); lintas subjek ±64%, lintas lingkungan 17,5%, kalibrasi 50-1000 bingkai → 72-78%; CC BY-NC 4.0 | Kartu model HF ruvnet/wifi-densepose-mmfi-pose | Subbab 2.4, 2.9 |
| 6 | MM-Fi: 40 subjek, 27 kategori aksi, >320 ribu bingkai tersinkron lima modalitas, NeurIPS 2023 D&B | arXiv:2305.10345 + halaman proyek | DP [16] |
| 7 | ADR-024 (AETHER, 56→64→128 via CsiToPoseTransformer, InfoNCE τ=0,07, tiga fase): berstatus Proposed; angka kinerjanya target rancangan | docs/adr/ADR-024 RuView | Dilabeli Proposed; tidak dipakai sebagai bukti |
| 8 | ADR-146 (encoder bersama d_model 64, tujuh kepala, ketidakpastian per kepala) dan ADR-150 (foundation encoder; adapter ±11 KB; 100-200 sampel/ruang → ±72%; temuan negatif pretraining pose-kontrastif) berstatus Proposed | docs/adr RuView | Estimasi rancangan, bukan hasil terukur |
| 9 | MediaPipe Hands: 21 landmark tangan | arXiv:2006.10214 | DP [19] |
| 10 | LoRA: W' = W0 + BA, peringkat r kecil | Hu dkk., ICLR 2022 | DP [17] |
| 11 | Smooth L1 | Girshick, Fast R-CNN, ICCV 2015 | DP [20] |
| 12 | Multitask learning berbagi representasi | Caruana, Machine Learning 28(1), 1997 | DP [21] |
| 13 | Distilasi pengetahuan (leluhur konsep guru-murid; soft target) | Hinton dkk., arXiv:1503.02531 | DP [22]; dipakai untuk MENJELASKAN mengapa istilah KD klasik tidak dipakai |
| 14 | Klaim v15 yang dipertahankan (juru bahasa ±500 vs 1,92 juta; UU 8/2016; Kamus SIBI; survei 91% BISINDO; CNN BISINDO; survei CSI; SignFi; datasheet ESP32-S3; esp-csi 56 subcarrier; RuView 50 bingkai/dtk, kalibrasi 600 bingkai 8 anchor; Fresnel/Doppler/Nyquist/CSI-ratio; Widar3.0; Chow reject; ESP-DL; Kokoro; MMS-TTS; Whisper; TRL; Likert) | Terverifikasi gelombang sebelumnya (catatan-pengemasan.md) | Dibawa utuh dengan nomor baru |

## C. Data pemilik (tidak masuk Daftar Pustaka)

| No. | Klaim | Sumber | Perlakuan |
|---|---|---|---|
| 15 | Dataset visual WPC v2: 49 kelas (25 huruf + 24 kata), 7.210 gambar (6.231/650/329), kpt_shape [21, 3] (komponen ketiga = visibility, bukan koordinat z), pseudo-labeling MediaPipe HandLandmarker, model visual YOLO26m-Pose (bukan YOLOv6m) | Brief v2 + repositori ILoveTahuTek/WPC (privat) | Subbab 2.9, Tabel 3.2; ditegaskan hasil visual bukan hasil CSI |
| 16 | exp11_huruf24: mAP50 0,8944 (49 kelas); mAP50 0,9580 + akurasi huruf 97,6% (24 huruf statis); C termasuk statis; J/Z dinamis | Sumber sama | Subbab 2.9; metrik visual dipisah dari metrik CSI |
| 17 | Skrip WPC train_sibi_v2.py, inference_sibi.py | Sumber sama | Tabel 3.2 |
| 18 | Anggaran biaya perangkat pemilik (ESP32-S3 ±Rp150.000; sepasang node < Rp350.000) | Data anggaran pemilik (gelombang 6) | 1.1, Tabel 3.8 |

## D. Batas klaim yang dijaga (tidak boleh muncul di naskah)

1. YOLO26m-Pose disebut sebagai encoder CSI.
2. Pose 17 keypoint MM-Fi disebut sebagai 21 keypoint tangan.
3. 82,3% disebut sebagai akurasi SIBI.
4. WPC dinyatakan punya pasangan CSI tersinkron.
5. LoRA dinyatakan tersedia untuk tugas SIBI tanpa verifikasi (hanya adapter ruangan yang terdokumentasi).
6. Encoder dinyatakan menerima 56 subcarrier mentah (temuan audit: 8 fitur turunan; adapter wajib diaudit).
7. Dimensi masukan, panjang jendela, koordinat target ditetapkan pasti sebelum audit (semua [PERLU VALIDASI]).
8. Hasil mAP YOLO dipakai sebagai hasil model CSI.
9. mAP50/akurasi WPC disebut akurasi SenseSIBI.
10. Deployment dinyatakan berhasil sebelum pengukuran perangkat fisik.
11. TTS/ASR/cloud/arah kedua dihapus atau diremehkan.
12. Komponen ketiga kpt_shape [21,3] disebut koordinat z spasial (ini visibility).
13. Referensi atau hasil eksperimen fiktif.

## E. Asumsi terbuka yang memerlukan konfirmasi penulis/pembimbing

1. Bentuk masukan encoder final (fitur bawaan RuView vs adapter masukan terpelajara) — T0.
2. Sistem koordinat target regresi (ternormalisasi bounding box vs pergelangan) — Tahap 3.
3. Keluaran regresi per timestep (T×21×2) vs satu pose — keterkaitan J/Z — Tahap 3.
4. Status modul temporal 1D-CNN (dipertahankan vs agregasi statistik) — hasil ablasi.
5. Bobot λ dan skema normalisasi skala kerugian — data validasi.
6. Skema kuantisasi final (float16/int8/int4) — dukungan operator runtime.
7. Ambang gerbang G1 dan kriteria manfaat multitugas — bersama pembimbing.
