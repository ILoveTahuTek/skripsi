## 3.12 Brief Audit Teknis

Subbab ini merangkum audit kesesuaian antara klaim naskah dan implementasi nyata pada enam sumber yang dipakai penelitian. Audit dilakukan pada 15 November 2026 dengan membuka kode sumber, kartu model, artefak eksperimen, dan dokumen rancangan langsung pada komit yang dikunci; hasilnya direkam sebagai register temuan AUD-01 sampai AUD-20 dengan status *PASS*, *CONDITIONAL*, *FAIL*, atau *NOT VERIFIED*. Klaim naskah yang terbukti bertentangan dengan kode dikoreksi pada revisi ini; yang belum terbukti tetap diberi penanda terbuka. Register lengkap beserta kutipan bukti per temuan tersimpan sebagai berkas pendamping Register-Audit-Teknis-v21.md di repositori penelitian agar setiap barisnya dapat diperiksa ulang.

### 3.12.1 Ruang Lingkup dan Artefak yang Diaudit

Tabel 3.9 memuat keenam sumber beserta versi yang diaudit. Penguncian komit dan *hash* bertujuan agar audit dapat direproduksi: pembaca dapat membuka berkas pada komit yang sama dan memperoleh bukti yang sama.

Tabel 3.9 Artefak yang diaudit dan versi yang dikunci

| Sumber | Versi atau identitas yang dikunci | Perubahan terakhir | Metode audit |
|---|---|---|---|
| RuView (ruvnet/RuView) | Komit `3bae24a1231e0d9809e84eb35edba7231b8d1913`; *firmware* `esp32-csi-node` v0.8.18 | 13 Nov 2026 | Baca kode `csi_collector.c`, `rv_radio_ops_esp32.c`, `edge_processing.c`, README *firmware*, panduan pengguna, dokumen ADR-018/029/110, panduan kalibrasi |
| *Checkpoint* `ruvnet/wifi-densepose-pretrained` | *Repo* Hugging Face pada `sha` `98b29a35f962996d6e8207e4f46818dedb5764d5`; `model.safetensors` sha256 `17c9acc1…11a1`; `csi-embed-v2.safetensors` sha256 `183c988b…ed72` | 13 Okt 2026 | Baca kartu model, seluruh berkas metadata, unduh dan urai *header* dua berkas bobot |
| WPC (ILoveTahuTek/WPC) | Komit `249a63dff4a7` pada cabang utama | 2 Nov 2026 | Baca `scripts/convert_sibi_v2.py`, `docs/DATASET_V2.md`, `weights/MANIFEST.json`, ringkasan eksperimen `exp11_huruf24` |
| *wifi-sensing-kit* (andrisgauracs) | Komit `7fb77fc0c0adb98bcf0a102d68fa8718b2f98625`; dasar *firmware* RuView tag v0.8.8-esp32 (`e04f269f`) | 11 Okt 2026 | Kloning dangkal; baca *patch* kit, skrip bangun dan *flash*, pustaka penerima, dokumentasi |
| *DensePose From WiFi* (arXiv) | arXiv:2301.00250v1, 31 Des 2022, DOI 10.48550/arXiv.2301.00250 | Tidak berubah sejak terbit | Baca teks lengkap 13 halaman; verifikasi metadata versi pada halaman abstrak |
| Naskah proposal v20 | Komit repositori skripsi `a0f2d7a` | 14 Nov 2026 | Telusur seluruh klaim mekanisme, angka, dan penanda terbuka terhadap lima sumber di atas |

Dua catatan menyertai tabel ini. Pertama, jalur ringkas naskah (komi `35c1ade`) tetap terdokumentasi terpisah dan tidak memengaruhi jalur utama; pemilik memutuskan untuk mempertahankan v20 sebagai dasar revisi ini. Kedua, seluruh tanggal pada tabel ialah tanggal komit terakhir artefak, bukan tanggal audit; seluruh audit dilakukan serentak pada 15 November 2026.

### 3.12.2 Ringkasan Temuan

Audit menemukan dua temuan berat, satu klaim basi, satu penanda terbuka yang terjawab, dan selebihnya temuan yang memperkuat atau membatasi rancangan. Temuan berat pertama menyangkut mekanisme akuisisi CSI: fungsi injeksi NDP pada *firmware* RuView masih berstatus *stub* tanpa satu pun pemanggil, sementara sumber CSI yang benar-benar berjalan ialah trafik *self-ping* OFDM yang ditangkap secara *promiscuous* (AUD-01); narasi naskah karenanya dikoreksi pada Subbab 2.3, 3.4, 3.5, Tabel 2.1, Tabel 3.1, Gambar 3.3, dan kriteria G0. Temuan berat kedua menyangkut kualitas anotasi guru: label visibilitas pada dataset WPC bernilai konstan untuk seluruh *keypoint* sehingga tidak dapat diperlakukan sebagai kebenaran oklusi (AUD-12); kebijakan mask efektif pada Subbab 2.7 dan 2.9 karenanya diperjelas. Tabel 3.10 merangkum keseluruhan register.

Tabel 3.10 Register audit ringkas (bukti lengkap pada berkas pendamping)

| ID | Temuan | Status | Tindakan korektif | Gerbang |
|---|---|---|---|---|
| AUD-01 | Injeksi NDP masih *stub* ADR-029 tanpa pemanggil; bingkai Null Data 24 byte hanya penampung; pengendali TX belum mendarat | FAIL (klaim lama) | Mekanisme *baseline* diganti trafik OFDM *self-ping* + *callback* CSI *promiscuous*; NDP dicatat rancangan masa depan; Tabel 3.7 no. 22 | G0 |
| AUD-02 | Sumber CSI aktual terverifikasi: *self-ping* gateway 10–50 Hz (baku 50), pembatasan laju 50 Hz, mode *promiscuous* MGMT+DATA pada papan tanpa layar | PASS | G0 tetap mengukur laju aktual | G0 |
| AUD-03 | Bingkai ADR-018 baku tidak memuat MAC pengirim; atribusi tautan TX-RX memerlukan penandaan MAC | CONDITIONAL | Patch penandaan MAC pola *kit* [34] atau tambahan minimal setara diaudit di T0; QA-FW-04 | G0 |
| AUD-04 | Format UDP ADR-018 terverifikasi: magic 0xC5110001/0xC5110002, port 5005, sanitasi `first_word_invalid`, LLTF dipaksa aktif | PASS | Parser Rust diuji bolak-balik; QA-ACQ-07 | G0 |
| AUD-05 | ESP-NOW hanya sinkronisasi *mesh* (ADR-110), bukan jalur CSI | PASS | Konsisten Tabel 3.7 no. 21 | G0 |
| AUD-06 | *Mesh* multistatik 3–6 node TDM terdokumentasi sebagai konfigurasi lanjutan yang menunjuk ADR-029/032 (masih usulan); konfigurasi dasar tiap node mengalirkan UDP mandiri | PASS (dokumentasi), NOT VERIFIED (dua node) | Uji konfigurasi dua node pada perangkat nyata di G0 | G0 |
| AUD-07 | Cacat *NUL-padding* `model.safetensors` (isu #1522) telah diperbaiki 13 Okt 2026; verifikasi ulang menunjukkan *header* bersih dan 17 tensor termuat utuh | CONDITIONAL (klaim naskah basi) | Teks 2.4 diperbarui; audit T0 tetap memverifikasi pemuatan langsung | T0 |
| AUD-08 | Dua keluarga berkas *checkpoint* bersaldo metadata berbeda (epoch 20 lawan 60, temperatur 0,07 lawan 0,1, jendela temporal, peringkat LoRA 4 lawan 8, `model.rvf.jsonl` tak terdokumentasi) | CONDITIONAL | Pemilihan keluarga berkas direkonsiliasi eksplisit di T0; Tabel 3.7 no. 6 diperluas | T0, G0b |
| AUD-09 | Catatan SISO 56 *subcarrier* berada pada README utama RuView (isu #509), bukan kartu model | PASS | Kutipan 2.4 dikoreksi ke [10] saja | - |
| AUD-10 | Kontrak *encoder* terverifikasi: 8 fitur @ 1 Hz, *embedding* 128 ternormalisasi L2, 9.280 parameter, triplet-temporal 82,3% (pembanding 66,4% dan 69,6%), EWC lupa 32,97%, lisensi MIT | PASS | Angka dikutip dengan cakupan aslinya | G0b |
| AUD-11 | Varian kuantisasi q2/q4/q8 serta int4 4,56 KB dengan *standardizer* FP16 tersedia; kinerjanya pada tugas SIBI belum teruji | NOT VERIFIED (kinerja tugas) | Uji paritas kuantisasi; QA-EDGE-02 dan QA-EDGE-03 | G1, G3 |
| AUD-12 | `write_label()` WPC menulis visibilitas konstan 2 untuk seluruh 21 *keypoint*; label tidak mencerminkan oklusi nyata | CONDITIONAL | Mask visibilitas tidak diwarisi dari label; diganti saringan kualitas deteksi + verifikasi sampel; Tabel 3.8 no. 14; QA-DS-02 | G0b, G1 |
| AUD-13 | `flip_idx` identitas terverifikasi empiris (n = 16, konsistensi 0,91); koreksi atas permutasi COCO-WholeHand v1 yang salah untuk urutan MediaPipe | PASS | Urutan 21 *keypoint* MediaPipe dikunci sebagai konvensi | G1 |
| AUD-14 | Dataset v2 terverifikasi: 9.953 ditemukan, dedup md5 −2.215, *leak-guard* dHash −18, MediaPipe 7.210 sukses dan 510 gagal, 7.627 objek, split terkunci 6.231/650/329, split resmi Roboflow dipakai apa adanya, Kaggle hanya latih, Roboflow CC BY 4.0 | PASS | Angka 2.9 konsisten | G1 |
| AUD-15 | `exp11_huruf24` dipetakan ulang saat pelatihan ke 24 kelas huruf A sampai Y tanpa J dan Z; validasi 333 instance huruf; mAP50 0,9580, mAP50-95 0,7235; conf 0,25 membaca 325/333 (97,6%) dengan 5 pertukaran dan 3 deteksi hilang | PASS (menjawab penanda terbuka) | Penanda [PERLU VALIDASI kelas J/Z] diselesaikan; supervisi J/Z tetap dari lintasan dan protokol | G1 |
| AUD-16 | Bobot `exp11` belum diarsipkan di repositori WPC; MANIFEST hanya memuat exp00 sampai exp10 dan exp06b (sha256 `073ccf71…3ea0`) | NOT VERIFIED (artefak) | Pemilik diminta menerbitkan tag rilis dan *hash* bobot exp11 sebelum angka guru diaudit pihak lain | - |
| AUD-17 | Pelatihan guru deterministik (seed 42) dengan buku besar eksperimen lengkap dan resep diulang pada exp11 | PASS | Keterulangan pra-penelitian terdukung | G1 |
| AUD-18 | *wifi-sensing-kit* ialah kit orkestrasi di atas *firmware* RuView v0.8.8 dengan patch MAC; tanpa NDP (stub sama), tanpa peran TX/RX tetap, laju sekitar 50 Hz dibagi antar tautan, hanya ESP32-S3, lisensi MIT | PASS (sebagai pola) | Dipakai sebagai pola atribusi AUD-03 dan opsi jalur pembanding pasif, bukan komponen inti | G0 |
| AUD-19 | *DensePose From WiFi* berstatus pracetak tanpa telaah sejawat; setup 3 antena TX × 3 RX, 30 *subcarrier*, 100 Hz, keluaran IUV 24 wilayah tubuh + 17 *keypoint* tubuh, tanpa konten tangan; terdapat inkonsistensi internal tabel | CONDITIONAL | Dikutip sebagai latar penamaan lini riset dengan label pracetak [35], bukan dasar teknis *encoder* | - |
| AUD-20 | Model pose MM-Fi [15] terpisah: 17 *keypoint* tubuh, PCK@20 82,69%, lisensi CC BY-NC 4.0, lintas subjek *zero-shot* sekitar 64% | PASS | Pemisahan tiga model pada Tabel 2.2 konsisten | G0b |

### 3.12.3 Bukti dan Penelusuran

Setiap temuan dapat ditelusuri ke berkas dan baris kode pada komit yang dikunci pada Tabel 3.9. Untuk AUD-01, fungsi `csi_inject_ndp_frame()` pada `firmware/esp32-csi-node/main/csi_collector.c` baris 940 sampai 982 memuat komentar ADR-029 yang menyebut bingkai Null Data yang dikirim sebagai penampung semata, dan penelusuran seluruh pohon kode tidak menemukan satu pun pemanggil fungsi itu; berkas `rv_radio_ops_esp32.c` baris 84 sampai 88 menyatakan perilaku TX baru berjalan setelah *controller PR* pengendali mendarat. Untuk AUD-12, fungsi `write_label()` pada `scripts/convert_sibi_v2.py` baris 286 sampai 297 menuliskan angka visibilitas tetap untuk setiap *keypoint* tanpa memeriksa keadaan oklusi. Untuk AUD-15, dokumen evaluasi `exp11_huruf24` menyatakan label dipetakan ulang ke 24 kelas huruf A sampai Y tanpa J dan Z pada saat pelatihan. Kutipan lengkap ketiganya beserta bukti temuan lain tersimpan pada berkas pendamping register; seluruh tautan sumber juga dicatat di sana.

### 3.12.4 Dampak terhadap Rancangan

Koreksi pada revisi ini bersifat naratif dan kebijakan, bukan perubahan arah penelitian. Mekanisme akuisisi CSI dinyatakan ulang sesuai bukti kode sehingga klaim naskah tidak melampaui implementasi yang tersedia; kebijakan mask visibilitas diketatkan agar supervisi regresi tidak mewarisi label yang tidak informatif; klaim *NUL-padding* yang telah usang diperbarui; dan satu penanda terbuka tentang kelas J/Z terjawab dengan fakta audit. Ruang lingkup penelitian tidak berubah: objek tetap 26 huruf SIBI satu tangan, guru tetap YOLO26m-Pose dengan supervisi lintasan untuk J dan Z, gerbang tetap G0 sampai G4 dengan sub-gerbang G0b, dan deployment tetap mengikuti Pilihan 1 pada Tabel 3.7. Tidak ada hasil pengujian yang dikarang; seluruh uji pada Subbab 3.13 berstatus belum diuji sampai penelitian berjalan.

### 3.12.5 Tindakan Korektif dan Keputusan yang Ditimbulkan

Tiga keputusan lahir dari audit ini dan dicatat pada Tabel 3.7. Pertama, mekanisme akuisisi baseline ditetapkan pada baris 22: trafik OFDM terjadwal dengan *callback* CSI *promiscuous*, tanpa injeksi NDP, dengan atribusi bingkai lewat penandaan MAC pengirim. Kedua, pemilihan keluarga berkas *checkpoint* beserta rekonsiliasi metadata kartu model ditambahkan ke lingkup audit T0 pada baris 6. Ketiga, permintaan penerbitan bobot dan *hash* `exp11` (AUD-16) menjadi prasyarat agar angka pra-penelitian guru dapat diaudit pihak lain; sampai artefak itu tersedia, penanda [PERLU DATA] pada rujukan [12] tetap berlaku. Seluruh keputusan lain yang menunggu pembimbing atau data eksperimen tetap tidak diputuskan sepihak.
