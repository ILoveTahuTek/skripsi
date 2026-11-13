<!-- ===== AKHIR NASKAH (jangan hapus penanda ini) ===

## Log Perubahan — Revisi 13 November 2026, gelombang 16 (revisi additif: dua kepala tugas pada encoder CSI terpralatih)

Permintaan: memperkuat proposal dengan pengembangan head klasifikasi dan regresi pada encoder Wi-Fi CSI terpralatih untuk jalur isyarat menjadi teks, tanpa mengubah ruang lingkup sistem SenseSIBI dua arah; judul dokumen acuan pemilik memakai frasa "CLOUD PROCESSING". Kaidah humanizer-indonesia (adhiprib v1.7, register akademik) dan pedoman scientific-agent-skills (scientific-writing, citation-management, markdown-mermaid-writing) tetap dipakai. Seluruh audit sumber di bawah dilakukan dengan membuka langsung kartu model Hugging Face, model card repositori, dan ADR pada 13 November 2026; matriks klaim lengkap pada Audit-Klaim-v16.md.

Changelog per subbab:

- Sampul: judul diganti mengikuti dokumen acuan pemilik (frasa "PEMROSESAN SERVER" menjadi "CLOUD PROCESSING"); kolom jenis dokumen dan catatan penyusunan ditulis ulang.
- 1.1 Latar belakang: paragraf keenam (model) ditulis ulang; kalimat arah 1 dan arah 2 serta paragraf studi kelayakan dipertahankan.
- 1.2 dan 1.3: butir 1 dan 2 diperbarui (encoder terpralatih beku, dua kepala tugas, supervisi lintas modalitas, ablasi); butir 3 (kelayakan) tetap; cermin rumusan-tujuan tetap 3:3.
- 1.4 Batasan: ditambah butir 5 tentang checkpoint encoder (bentuk masukan diaudit, LoRA berstatus pembanding); butir lama menjadi 1-4 dan 6-10.
- 1.5.1 Manfaat teoretis: ditambah pertanyaan embedding kontrastif untuk gestur jari dan formulasi multitugas lintas modalitas.
- 1.6 Sistematika: disesuaikan dengan subbab baru.
- 2.1: ditambah satu kalimat audit kelas (C statis; J dan Z dinamis) sebagai pemastian konsistensi seluruh naskah.
- 2.2 sampai 2.3: teks v15 dipertahankan; Tabel 2.1 baris "Model WiFi-DensePose terpralatih int8" diganti "Checkpoint encoder CSI terpralatih (embedding 128 dimensi)".
- 2.4 (baru) Encoder CSI terpralatih dan pembedaan tiga model: kartu model encoder (dua lapis FC BatchNorm+GELU, 9.280 parameter, embedding 128 ternormalisasi L2, triplet+InfoNCE temperatur 0,1, positif 2 detik, negatif 30 detik, 60 epoch AdamW, EWC); penegasan 82,3% sebagai akurasi triplet-temporal held-out (pembanding 66,4% fitur mentah dan 69,6% encoder acak), bukan akurasi SIBI; temuan ketidaksesuaian bentuk masukan (delapan fitur turunan pada 1 Hz lawan 56 subcarrier pada 50 bingkai per detik) beserta dua jalur penyelesaian; pembedaan model pose MM-Fi 17 keypoint tubuh (masukan [3, 114, 10] @ 100 Hz, PCK@20 82,69%/83,59%, lintas subjek ±64%, lintas lingkungan 17,5%, lisensi CC BY-NC 4.0) dan YOLO26m-Pose guru visual; status ADR-024, ADR-146, ADR-150 dinyatakan Proposed; Tabel 2.2 pembedaan tiga model; persamaan (2.6).
- 2.5 (baru) Transfer learning: alasan encoder beku; LoRA W = W0 + BA (persamaan 2.7) sebagai opsi adaptasi bukan prasyarat; adapter ruangan node-1/node-2 ±21 KB terdokumentasi; estimasi ADR-150 dilabeli estimasi rancangan; kompatibilitas ekspor ditandai [PERLU VALIDASI].
- 2.6 (baru) Kepala klasifikasi: logits, softmax, silang-entropi 26 kelas (persamaan 2.8-2.10); bobot kelas dari data latih; penolakan dengan skor keyakinan [18].
- 2.7 (baru) Kepala regresi: skema 21 landmark MediaPipe; komponen ketiga kpt_shape [21, 3] ditegaskan sebagai visibilitas, bukan koordinat kedalaman; keluaran (T, 21, 2) karena lintasan J dan Z (persamaan 2.11); pembakuan sistem koordinat [PERLU VALIDASI]; Smooth L1 bermask per keypoint (persamaan 2.12-2.13) [20].
- 2.8 (baru) Multitugas, modul temporal, kerugian gabungan: hipotesis supervisi keypoint merapikan batas kelas; persamaan 2.14-2.15 dengan θ0 beku; normalisasi skala kerugian dan pemantauan konflik gradien; 1D-CNN dari rancangan lama dievaluasi ulang sebagai kandidat modul temporal (peringkas barisan embedding), bukan kepala tugas.
- 2.9 Guru visual YOLO26m-Pose: istilah "distilasi pengetahuan" dikoreksi menjadi supervisi lintas modalitas berpandu guru / pseudo-label [22]; angka WPC (49 kelas, 7.210 gambar, 6.231/650/329, mAP50 0,8944 dan 0,9580, akurasi 97,6%) ditegaskan sebagai hasil visual pada data visual dan dataset tanpa CSI; ekspektasi generalisasi dari temuan MM-Fi.
- 2.10: kalimat SVM diganti pembanding ablasi kepala tunggal; ESP-DL [23] tetap.
- 2.11 sampai 2.13 (dulu 2.6 sampai 2.8): teks v15 dipertahankan; ditambah satu kalimat pemisahan bahasa pelatihan (Python/PyTorch) dan bahasa runtime (Rust).
- 2.14 Evaluasi (dulu 2.9): ditambah metrik regresi MPJPE, NME, PCK@α, dan galat per keypoint (persamaan 2.21-2.22) serta definisi d_ref yang mengikuti pembakuan koordinat; persamaan presisi-recall-F1-WER dipertahankan dengan nomor baru.
- 2.15 Penelitian terdahulu (dulu 2.10): baris "Penelitian ini" diperbarui (encoder terpralatih berkepala dua, supervisi guru visual).
- 2.16 Matriks justifikasi (dulu 2.11): baris model murid diperbarui; ditambah baris 7 (dua kepala lawan satu kepala) dan baris 8 (supervisi lintas modalitas lawan distilasi soft target); SVM keluar dari matriks.
- 2.17 (baru) Kerangka pemikiran: Gambar 2.2 arsitektur model dua kepala (encoder beku, adapter masukan bila perlu, modul temporal, dua kepala, jalur guru visual, deployment); dataset berpasangan D_pas diperluas dengan skor kualitas anotasi q_i (persamaan 2.24).
- 3.1 dan 3.2: kalimat model diperbarui (supervisi lintas modalitas; dua kepala); T0 menambah audit checkpoint; T2 menambah pelatihan dua kepala; Gambar 3.1 digambar ulang (label T0, T2, G1).
- 3.3 dan 3.4: Tabel 3.1 perangkat keras dipertahankan sepuluh baris; Tabel 3.2 diperbarui (checkpoint encoder masuk baris 2; scikit-learn keluar; Kaggle hanya pelatihan lanjutan guru dan pembanding adaptasi; sebelas baris).
- 3.5: Gambar 3.3 node RX diganti labelnya (encoder terpralatih berkepala dua terkuantisasi); teks topologi, kalibrasi, enclosure, Tabel 3.3 pinout, dan Gambar 3.4 dipertahankan.
- 3.6: langkah 4 menambah verifikasi sinkronisasi lewat uji kejadian [PERLU DATA: toleransi sinkronisasi]; langkah 6 menambah skor kualitas anotasi; langkah 7 menegaskan status pseudo-label.
- 3.7 (ditulis ulang): audit bentuk masukan dan adapter; encoder per bingkai plus modul temporal; dataset murid tiga deret selaras waktu; pelatihan Python/PyTorch di komputer (laptop atau Kaggle) dengan seed tetap dan early stopping; rangkaian ablasi (kepala klasifikasi saja, multitugas, variasi bobot λ); LoRA dan pelatihan lanjutan sebagai pembanding opsional; Tabel 3.4 skema pembagian dipertahankan enam baris; ekspor satu graph lalu kuantisasi affine (persamaan 3.2) dengan verifikasi operator runtime [PERLU VALIDASI]; Gambar 3.5 digambar ulang.
- 3.8: 3.8.2 menjadi "Uji Klasifikasi, Regresi, dan Ablasi" (menambah MPJPE, NME, PCK, galat per keypoint, pasangan mirip dan lintasan J/Z, ablasi berdampingan); 3.8.3 persamaan dinomori ulang (3.3 latensi, 3.4 baterai, 3.5 biaya); gerbang G1 pada Tabel 3.5 menambah pembanding ablasi dan laporan MPJPE; subbab lain dipertahankan.
- 3.9: jadwal M1-M14 dipertahankan; label baris 1 dan 3 diperbarui.
- 3.10: Tabel 3.7 dari 14 menjadi 18 baris (bentuk masukan dan adapter; koordinat, bentuk keluaran, dan ambang PCK; status modul temporal; peringkat LoRA; bobot λ dan skala kerugian).
- 3.11: Tabel 3.8 dari 9 menjadi 12 baris (risiko ketidaksesuaian bentuk masukan; embedding beku tidak memisahkan; konflik gradien).
- Daftar pustaka: 22 menjadi 28 entri. Masuk tujuh rujukan primer baru yang diverifikasi dengan membuka sumbernya pada 13 November 2026: kartu model encoder [11], kartu model pose MM-Fi [15], dataset MM-Fi [16], LoRA [17], MediaPipe Hands [19], Fast R-CNN untuk Smooth L1 [20], dan multitask learning [21]. Keluar satu rujukan bersama pembanding lamanya: SVM (Cortes dan Vapnik), karena pembanding klasifikasi kini berupa ablasi kepala tunggal pada model yang sama. Sitasi dinomori ulang menurut kemunculan pertama dan diverifikasi monoton 1-28; tanggal akses RuView dan kedua kartu model diperbarui ke 13 Nov 2026.
- Persamaan: 18 menjadi 29 bernomor (2.1-2.24 dan 3.1-3.5); seluruh persamaan lama dipertahankan isinya dengan nomor baru.
- Gambar: 6 menjadi 7. Gambar 2.1 zona Fresnel dan Gambar 3.2 foto perangkat serta Gambar 3.4 skema node dipertahankan dari gelombang 15; Gambar 2.2 arsitektur model dua kepala baru; Gambar 3.1, 3.3, dan 3.5 digambar ulang dengan label model baru, lengkap accTitle/accDescr dan subgraf berlabel.
- Penanda: [PERLU DATA] 23 sampul-isi, [PERLU VALIDASI] 9 (bentuk masukan dan adapter; koordinat dan ambang PCK; kompatibilitas LoRA; dukungan operator runtime; sistem koordinat; bentuk keluaran regresi), [PERLU ILUSTRASI] 1; penanda VALIDASI baru ditambahkan pada regex parser DOCX agar ikut tersorot.
- Yang tidak berubah: seluruh komponen sistem dua arah (TTS on-device Kokoro dengan prasyarat G3, ASR awan dengan cadangan faster-whisper, kamus representasi SIBI dengan fallback ejaan jari, server Rust, topologi satu kanal, enclosure dan pinout), gerbang G0-G4, jadwal M1-M14, uji kegunaan dan validator, analisis biaya, konteks Jawa Timur tanpa mitra lembaga, register mahasiswa D4/S1, dan seluruh angka pra-penelitian yang dipertahankan tetap bersumber sama.
- Pemetaan nomor ke kunci: [1]kemenkopmk, [2]uu-disabilitas, [3]kamus-cetak, [4]mursita, [5]dwijayanti, [6]ma-csur, [7]signfi, [8]esp32s3, [9]esp-csi, [10]ruview, [11]encoder-card, [12]ultralytics, [13]csi-ratio, [14]widar3, [15]mmfi-card, [16]mmfi-paper, [17]lora, [18]chow, [19]mediapipe, [20]girshick, [21]caruana, [22]hinton, [23]esp-dl, [24]kokoro-card, [25]mms-card, [26]whisper, [27]trl, [28]likert

## Log Perubahan — Revisi 11 November 2026, gelombang 12 (parafrase anti-ai-writer)

Permintaan: memparafrasekan ketiga dokumen (md, docx, pdf) memakai skill anti-ai-writer (mchardyan/anti-ai-writer v2) di atas naskah v11, tanpa mengubah isi. Pekerjaan tetap menjaga kaidah naskah-id (EYD V), register mahasiswa D4/S1, dan seluruh keputusan gelombang 11 (konteks Jawa Timur, prioritas sumber Indonesia, DP 46 entri, istilah asing tidak dipaksakan diterjemahkan):

- Kosakata dan frasa terlarang daftar hitam anti-ai-writer dibersihkan dari prosa: menegaskan (2), mencakup (4), menampilkan (8) diganti padanan konkret yang bervariasi (memunculkan, muncul, memperlihatkan, memuat, meliputi, menunjukkan).
- Ritme kalimat dirombak: 10 deretan tiga kalimat berpanjang seragam pada v11 (toleransi dua kata) dipecah menjadi nol melalui penggabungan, pemenggalan, dan pemanjangan kalimat terpilih; panjang kalimat kini menyebar dari 3 sampai 53 kata (13% kalimat pendek 10 kata ke bawah, 23% kalimat panjang 28 kata ke atas).
- Pola khas AI lain yang dihapus: enumerasi retoris "Pertama, ... Kedua, ..." pada latar belakang (diganti prosa mengalir), pembuka klise, dan ketergantungan pada transisi; beberapa paragraf kini ditutup tiba-tiba dan satu pertanyaan retoris dipertahankan sebagai penutup latar belakang.
- Yang tidak berubah: 46 kunci sitasi beserta urutan kemunculan dan penomoran, seluruh angka pra-penelitian (token angka pada prosa identik dengan v11), 25 penanda [PERLU DATA]/[PERLU ILUSTRASI], 12 tabel, 3 gambar beserta blok mermaid-nya, 39 heading, struktur gerbang G0-G4, jadwal M1-M14, dan keenam prosedur.
- Rumusan masalah dan tujuan diparafrase tercermin tetap 3:3; batasan tetap sembilan butir.

## Log Perubahan — Revisi 12 November 2026, gelombang 13 (humanizer-indonesia + tanpa mitra)

Permintaan: menyunting naskah v12 memakai skill humanizer-indonesia (adhiprib v1.7, register akademik) sekaligus menghapus seluruh klaim kemitraan karena penelitian dijalankan tanpa mitra lembaga. Pengukuran memakai scripts/metrik.py bawaan skill (preset akademik); kalibrasi suara penulis tidak dilakukan karena tidak ada contoh tulisan pemilik, sehingga dipakai suara netral register akademik.

- Klaim kemitraan dihapus dari lima titik (1.1, batasan butir 7, manfaat praktis, 3.3, 3.6): 3.3 kini menyatakan partisipan direkrut langsung oleh peneliti dan pengujian berlangsung di dua ruang berbeda tanpa mengikat lembaga; placeholder nama SLB mitra dihapus dari naskah.
- Sembilan metrik berambang kini lulus semua (sebelumnya tiga PERIKSA): rerata panjang kalimat 20,5 menjadi 19,1 kata; kalimat 28 kata ke atas 20,6% menjadi 13,9%; em dash/en dash di prosa 8 menjadi 0.
- Pola khas keluaran model yang dibersihkan: konstruksi verba ringan diganti verba kerja; penyangkalan antisipatif dinyatakan positif; 18 kemunculan konjungsi "bila" menjadi "jika" (kaidah register akademik skill); rentang alfanumerik di prosa menjadi bentuk "sampai".
- Ritme dirombak tanpa mengubah isi: 24 kalimat panjang dipecah; kalimat pendek lepas diberi partikel atau penghubung sesuai temuan skill bahwa kalimat pendek berpartikel terbaca manusiawi.
- Yang dikecualikan dari suntingan ritme menurut katalog skill: butir prosedur dan daftar batasan yang memang paralel, daftar teknis yang seluruh butirnya membawa isi, pasif bagian metode, dan metafora baku literatur teknik.
- Yang tidak berubah: 46 kunci sitasi beserta urutan kemunculan dan penomoran, seluruh angka pra-penelitian, 12 tabel, 3 gambar beserta blok mermaid, struktur heading, struktur gerbang G0-G4, jadwal M1-M14, keenam prosedur, dan konteks Jawa Timur.

## Log Perubahan — Revisi 12 November 2026, gelombang 14 (daftar pustaka 22 entri, sekitar 30 halaman, diagram direvisi)

Permintaan: memangkas daftar pustaka menjadi sekitar 20-an entri, memadatkan keseluruhan proposal menjadi sekitar 30 halaman, dan merevisi diagram dengan pedoman scientific-agent-skills di atas kaidah humanizer-indonesia.

- Daftar pustaka dipangkas dari 46 menjadi 22 entri dan sitasi dinomori ulang 1 sampai 22 menurut urutan kemunculan.
- Klaim yang kehilangan rujukan diperlunak, bukan dibiarkan tanpa sumber.
- Naskah dipadatkan menjadi sekitar 30 halaman.
- Tiga diagram direvisi mengikuti pedoman scientific-agent-skills: anotasi aksesibilitas accTitle/accDescr ditambahkan, subgraf tanpa judul diberi judul bermakna, setiap label simpul ditelusur ulang ke teks.
- Yang tidak berubah: struktur BAB I sampai III, tabel, gambar beserta semantik alurnya, jadwal, prosedur pengujian, batasan, rumusan dan tujuan, serta penanda [PERLU DATA]/[PERLU ILUSTRASI].

## Log Perubahan — Revisi 12 November 2026, gelombang 15 (rumusan teknologi, persamaan bernomor, ilustrasi tiga dimensi)

Permintaan: rumusan masalah mencantumkan teknologi inti (WiFi-DensePose, YOLO26m-Pose, dan lain-lain), menambah model perhitungan berupa rumus matematika, serta menambah gambar tiga dimensi dan gambar alat-bahan; kaidah humanizer-indonesia dan pedoman scientific-agent-skills tetap dipakai.

- Rumusan masalah dan tujuan kini mencantumkan teknologi intinya dengan cermin 3:3.
- Delapan belas persamaan bernomor ditambahkan beserta definisi lambang dan contoh perhitungan.
- Tiga ilustrasi baru ditambahkan (zona Fresnel tiga dimensi, foto perangkat, skema node penerima) sehingga gambar menjadi enam.
- Pipeline DOCX ditambah dukungan blok rumus serta token subskrip dan superskrip; daftar pustaka tetap 22 entri.
- Yang tidak berubah: struktur BAB I-III, tabel, gerbang, jadwal, prosedur, batasan, konteks Jawa Timur tanpa mitra, dan seluruh angka pra-penelitian.
