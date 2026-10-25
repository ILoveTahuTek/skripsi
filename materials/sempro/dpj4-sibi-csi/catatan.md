# Catatan Penyusunan Proposal DPJ-4

**Judul:** Alat Pembelajaran Isyarat SIBI Tanpa Kamera Berbasis Wi-Fi Channel State Information pada ESP32: Studi Kelayakan Umpan Balik Latihan bagi Pembelajar Pendengar

Disusun 23 Oktober 2026 dengan bantuan AI (Claude); penanda diisi dari sumber terverifikasi pada 24 Oktober 2026. Semua isi berasal dari bahan pemilik (draf DPJ-4, dossier, transkrip council) dan dari metadata DOI yang dicek langsung. Data, angka, atau rujukan yang tidak tersedia tidak dikarang, tetapi ditandai `[PERLU DATA: …]` atau `[PERLU RUJUKAN: …]`.

## 1. Isi folder

| Berkas | Isi |
|---|---|
| `bab1-pendahuluan.md` | BAB I, sitasi IEEE bernomor |
| `bab2-kajian-pustaka.md` | BAB II, sitasi IEEE bernomor |
| `bab3-metodologi.md` | BAB III, sitasi IEEE bernomor, dua diagram Mermaid |
| `daftar-pustaka.md` | 62 rujukan, urut sesuai kemunculan pertama |
| `_berkunci/` | Salinan ketiga bab dengan sitasi berupa kunci `[@kunci]`. Pakai versi ini bila menambah atau menghapus sitasi, lalu nomori ulang. |
| `_lembar-fakta.md` | Sumber fakta, istilah, dan desain penelitian yang dipakai semua bab |
| `_metadata-doi.json` | Metadata DOI hasil pengecekan |
| `_nomori-sitasi.py` | Skrip penomoran ulang sitasi dan pembuat daftar pustaka |
| `laporan-penanda.md` | Daftar semua penanda `[PERLU …]` yang tersisa |
| `_laporan-penanda.py` | Skrip pembuat `laporan-penanda.md` |
| `_berkunci/bab3-metodologi.sebelum-padat.md` | Cadangan BAB III sebelum dipadatkan; hapus bila versi padat sudah disetujui |

## 2. Jenis pekerjaan per bab

Ketiga bab berjenis **Tulis**, yaitu teks baru yang disusun dari bahan pemilik. Setiap bab ditulis, lalu ditinjau dari tiga sudut (kesetiaan fakta, bahasa dan register, sudut pandang penguji), direvisi, dan terakhir dicek konsistensinya lintas bab.

## 3. Keputusan yang dikunci pemilik

- Cakupan **SIBI saja**. BISINDO disebut sebagai konteks dan kerja lanjutan.
- Framing: alat latihan bagi pembelajar pendengar. Latar belakang berangkat dari masalah sosial dan pendidikan, bukan dari teknologi.
- Format sempro standar tiga bab: tanpa tabel usulan judul, rencana biaya, dan tabel risiko.
- Sitasi IEEE numerik.

## 4. Perubahan penting dibanding draf DPJ-4 lama

| Aspek | Draf lama | Sekarang |
|---|---|---|
| Bahasa | SIBI dan BISINDO | SIBI saja, angka 1,9% (BRIN) dibuka di BAB I beserta alasan memilih SIBI |
| Orientasi | Pengenalan gestur untuk prasarana edukasi | Umpan balik latihan bagi pembelajar pendengar |
| Peran kamera | "Pelabelan *ground truth*" | Label kelas berasal dari kartu pemandu; MediaPipe hanya memverifikasi batas segmen, menyaring kualitas, dan membantu diagnosis |
| Makna "benar" | Tidak dibatasi | "Cocok" hanya berarti lintasan lengan, tubuh atas, dan kepala sesuai; bentuk jari tidak dinilai; ada penolakan berbasis skor keyakinan |
| Gerbang | Satu gerbang Delta-CSI di minggu ke-3 | G0–G4; ambang numerik tidak ditulis sebagai janji |
| Pembagian data | Validasi silang per sesi | Pembagian data temporal per blok, lintas sesi, *leave-one-subject-out*, *leave-one-room-out*, dan pengguna baru |
| Uji pengguna | Tidak ada | 3–5 pemula; uji awal dan akhir dinilai validator; kuesioner persepsi pada kondisi kamera menyala dan mati (urutan acak); analisis deskriptif |
| Keterlibatan tunarungu | Tidak ada | Validator penutur tunarungu wajib |
| MQTT/Home Assistant | Dipakai | Dihapus; umpan balik ditampilkan di *dashboard* |

## 5. Koreksi rujukan hasil pengecekan DOI

Semua DOI dicek langsung lewat doi.org pada 23 Oktober 2026.

- **BlazePose:** DOI di dossier (`arXiv:2004.03486`) ternyata menunjuk ke paper lain. Yang benar `arXiv:2006.10204`.
- **Judul yang keliru di draf lama:**
  - Shang dan Wu: judul benarnya "…with Multiple Wi-Fi Devices".
  - Sanjaya dkk.: judul benarnya "…Deep Learning Techniques for Image Processing". Karena itu tinjauan ini tidak dipakai untuk klaim "belum ada pendekatan nirkabel".
  - Judul Cai dkk., Kindy dkk., Sebastian dkk., Wiguna dan Rojali, dan MediaPipe juga diperbaiki.
- **Daftar penulis:** Rodríguez-Correa dkk. dan SignFi diperbaiki.
- **Volume:** DF-WiSLR terbit di vol. 69, bukan 68.
- **Isi:** WiASL memakai perangkat Wi-Fi komersial, bukan kamera.
- **Widar3.0:** Crossref hanya menyimpan versi *early access* (2021). Daftar pustaka memakai data terbitan cetak (vol. 44, no. 11, pp. 8671–8685, 2022), yang tidak tercatat di metadata DOI. **Cocokkan dengan IEEE Xplore.**
- **Belum dicek ulang di sesi 23 Okt (kemudian diselesaikan 24 Okt, lihat bagian 5b):**
  - URL berita BRIN (dari dossier);
  - rilis Kemenko PMK (URL belum ada);
  - fakta teknis RuView (ADR-018, ADR-079, kalibrasi 600 *frame* + 8 *anchor*, mode privasi), yang semuanya berasal dari dossier dan belum dicocokkan langsung dengan repositori.
- **Kamus SIBI** masih berupa penanda, karena data terbitan resminya belum ada.

## 5b. Pengisian penanda 24 Oktober 2026 (putaran kedua)

Atas perintah pemilik ("isikan dengan kebenaran mutlak dengan mencari artikel/jurnal"), 61 kemunculan penanda diisi atau dijawab secara jujur; sisa 38 kemunculan (35 unik, semua PERLU DATA) sengaja dibiarkan karena berupa keputusan pembimbing, data pribadi, atau parameter rancangan yang memang ditetapkan kemudian.

**Rujukan baru (28, DOI dicek lewat Crossref 24 Okt 2026):** Stokoe 2005 (JDSDE, cetak ulang monograf 1960); Ong dan Ranganath 2005 (TPAMI 27(6), survei SLR sensor+visi); Cortes dan Vapnik 1995; Kiranyaz dkk. 2021; Sigrist dkk. 2013; Bowen dkk. 2009; Sokolova dan Lapalme 2009; Chow 1970 (DOI benar 10.1109/TIT.1970.1054406, bukan ...54508); Mountrakis dkk. 2011; Zheng dkk. 2023 (DOI benar 10.1145/3603618); Zajonc 1965; Bailenson 2021 (DOI benar 10.1037/tmb0000030); Nyquist 1928; Shannon 1949; Likert 1932 (tanpa DOI); Sadeghzadeh dkk. 2024 (MLMSign, ISWA 22); Sagawa dan Takeuchi 2002 (ACM Multimedia, sistem pembelajaran isyarat Jepang); Daniel dkk. 2024 (URTC); Hassan dkk. 2026 (CHI); As Satillah dkk. 2024 (AUDHI, SIBI di SLB N Ogan Ilir); Nugraheni dkk. 2023 (Holistika 5(1); Crossref terbit daring 21-2-2023 - Google Scholar menampilkan 2021, pakai 2023); Malika dan Berlianti 2025 (Concept 4(3)); Rodhiyah dan Wulandari 2024 (INTECOMS 7(1)); Fatmawati dkk. 2022 (Technomedia 7(1), OpenSIBI); Zikky dan Akbar 2019 (JST 5(2)); Maulana dkk. 2026 (DBESTI 3(1)); Soekarta dkk. 2024 (Insect 10(2):90-100, MediaPipe Android); Lemlitbang SIBI, Kamus SIBI Digital 2020 (laman resmi).

**Entri lama yang diisi:** [5] Kemenko PMK (URL kemenkopmk.go.id terverifikasi, akses 24 Okt 2026); [7] BRIN (tanggal akses); [8] Kamus SIBI (Depdikbud 1994, edisi pertama, diluncurkan 2 Mei 1994 dengan SK Mendikbud 0190/P/1994); [23] RuView (commit fefb0f9, 22 Okt 2026, akses 24 Okt 2026).

**Fakta teknis RuView yang kini dicocokkan langsung ke repositori:** ADR = *architecture decision record*; varian yang direkomendasikan untuk node CSI = ESP32-S3; firmware membatasi pengiriman frame CSI paling sering setiap 20 ms (`CSI_MIN_SEND_INTERVAL_US` di `csi_collector.c`) = maksimum 50 frame/detik; mode privasi menekan keluaran biometrik detak jantung, laju napas, dan pose agar tidak keluar dari server. Jarak antarnode tidak dipreskripsi repo sehingga tetap ditetapkan pada T0.

**Fakta sistem pembanding (dari makalahnya):** SignFi = Intel 5300 + 3 antena penerima via 802.11n CSI Tool; Wi-SL = TP-Link WDR4310 (Atheros AR9580), 2 antena TX x 3 RX, kanal 40 MHz, cuplik 400 Hz, 12 gestur; HandFi = Intel 5300 sebagai RX dari router komersial, 12 gestur tangan; WiSign (Shang-Wu) = router TP-Link TL-WR1043ND + 2 laptop Lenovo X100e, tidak menyebut bahasa isyarat tertentu; DF-WiSLR = 49 gestur (30 statis + 19 dinamis), tidak menyebut bahasa tertentu; Dwijayanti dkk. 2021 = BISINDO (26 huruf + 10 angka, 39.455 data).

**Dijawab jujur tanpa fabrikasi (data tidak tersedia di literatur):** proporsi anak tunarungu dari orang tua pendengar di Indonesia (dinyatakan tidak ditemukan pada penelusuran Google Scholar/Crossref/OpenAlex hingga Okt 2026, angka AS tetap dipakai sebagai gambaran); proporsi kosakata Kamus SIBI yang dibedakan lintasan gerak dan jumlah kandidat isyarat (dinyatakan belum terdokumentasi, ditetapkan saat kurasi T1); kebutuhan belajar khusus pembelajar pendengar SIBI (belum ada studi khusus; tercermin dari aplikasi dan SLB); orientasi pembelajaran kelompok WiFi-SLR (tidak dijumpai; keempatnya menargetkan pengenalan); ketersediaan kursus SIBI bagi keluarga (belum terdokumentasi dalam kajian ekosistem). Klaim "batas resolusi spasial CSI" ditata ulang menjadi fakta perangkat multi-antena sistem pembanding + asumsi eksplisit yang diperiksa lewat uji Delta-CSI, karena tidak ditemukan sumber terverifikasi yang menyatakan batas resolusi untuk satu tautan ESP32.

Arsip verifikasi: `scripts/sempro-isi/crossref/*.json`, `scripts/sempro-isi/ss/*.json`, salinan `13-sempro-docx/verifikasi-rujukan-2026-10-24/`.

## 5c. Ralat pemilik 25 Oktober 2026: MediaPipe diganti model pose YOLO26

Atas perintah pemilik ("ralat, aku tidak menggunakan mediapipe tapi yolo26 pose model"), estimator pose pada jalur pelabelan diganti dari MediaPipe menjadi model pose YOLO26. Total 41 suntingan lokasi di `_berkunci/` (bab1 1, bab2 4, bab3 5, lembar fakta 7, kamus REF 1 blok) + node diagram Gambar 3.2.

**Rujukan:** 3 rujukan MediaPipe-spesifik dihapus (BlazePose, MediaPipe Hands, Kim dkk. 2023 — tidak relevan lagi dengan metode); 3 rujukan baru ditambahkan, semuanya diverifikasi 25 Okt 2026: [33] Jocher dkk. 2026 "Ultralytics YOLO26: Unified real-time end-to-end vision models" (arXiv:2606.03748, paper resmi tim Ultralytics — doi 10.48550/arXiv.2606.03748); [52] Sapkota dkk. 2025 "YOLO26: Key architectural enhancements..." (arXiv:2509.25164 — doi 10.48550/arXiv.2509.25164); [51] Ultralytics "Pose estimation" (docs.ultralytics.com/tasks/pose/, menyatakan "The default YOLO26 Pose models predict the 17 COCO keypoints", varian n/s/m/l/x terlatih COCO). MediaPipe [49] TETAP dipakai tetapi hanya sebagai fakta repositori RuView (skrip ADR-079 memakai PoseLandmarker) — bukan alat penelitian ini; kejadian MediaPipe lain yang tersisa adalah karya pihak lain (Soekarta dkk. 2024 [61], Tabel 2.2).

**Perubahan substansi teks:** (1) deret keypoint kini "17 keypoint tubuh format COCO" TANPA keypoint ji — konsisten dengan cakupan pengenalan yang memang dibatasi lintasan lengan/tubuh atas/kepala (Subbab 2.3); kalimat lama tentang landmark tangan MediaPipe Hands dihapus. (2) Pembingkaian jujur: skrip `collect-ground-truth.py` ADR-079 RuView aslinya memakai MediaPipe PoseLandmarker yang mengonversi 33 landmark menjadi 17 keypoint COCO; penelitian ini mengikuti pola sinkronisasi ADR-079 dengan estimator diganti model pose YOLO26 terlatih (tanpa pelatihan ulang) yang keluarannya 17 keypoint COCO langsung — format data identik. (3) Tabel 3.2: baris 3 "ADR-079, diadaptasi", baris 4 "Model pose YOLO26 (Ultralytics)". (4) Diagram Gambar 3.2: node "MediaPipe" menjadi "Model pose YOLO26".

**Perbaiki tumpang tindih blok pada Gambar 3.1 dan 3.2** (juga atas perintah pemilik). Akar masalah G3.1: elemen diamond dibuat dengan rotasi CSS 45° atas persegi panjang 280x340 sehingga *bounding box* sebenarnya 440x440 dan puncak diamond menabrak kotak T/P/GU/S di sekelilingnya; label "gagal/lolos" juga jatuh di dalam diamond. Perbaikan: diamond kini persegi (rotasi = belah ketupat simetris, AABB terkontrol 354px untuk G, 212px untuk GU), seluruh kolom dan jalur disusun ulang, kanvas 1550x2200. G3.2: node kolom B menempel tepat border panel (digeser, jeda 27px), koridor putus-putus diberi lajur terpisah (x616/x640/x648 di celah antar-panel), label "pelatihan" dipindah agar tidak menimpa border panel. Verifikasi: `check_layout.js` (pemeriksa geometri deterministik baru — 0 luapan teks, 0 irisan blok termasuk diamond rotasi, 0 garis menembus blok, 0 di luar kanvas, 0 node menempel border panel) + PDF 55 halaman, postcheck 0 error, sinkron pandoc 596/596 unit.

## 6. Keputusan yang masih terbuka (bawa ke bimbingan)

1. **5–8 isyarat versus pemangkasan 3–5 isyarat.** Rumusan masalah dan batasan menyebut 5–8, sedangkan cabang gagal G2 memangkas menjadi 3–5. Perlu diputuskan apakah rumusan cukup menyebut "5–8, dapat dipangkas menjadi 3–5".
2. **Klausa empati pada batasan 6.** Kalimat aspirasi empati di bagian manfaat sudah dihapus, jadi klausa "empati tidak diukur secara psikometrik" kini tidak punya acuan lain di BAB I. Pilihannya: hapus klausa itu, atau kembalikan satu kalimat aspirasi empati.
3. **Istilah "separabilitas fisik".** Kata ini tidak ada di KBBI. Alternatifnya "keterpisahan fisik", dan bila diganti, harus diganti di ketiga bab sekaligus.
4. **"Tunarungu" versus "Tuli".** Proposal memakai "tunarungu" sesuai KBBI. Komunitas sering lebih memilih "Tuli", jadi sebaiknya dikonfirmasi dengan pembimbing dan validator.
5. **Subbab Kerangka Berpikir di BAB II.** Belum dibuat, karena tergantung pedoman prodi.
6. **Sistematika tiga bab.** Perlu dikonfirmasi bahwa proposal di prodi memang cukup BAB I–III.
7. **Uji sinkronisasi T0 tanpa partisipan.** Ini keputusan rancangan yang ditambahkan saat revisi lintas bab dan perlu disetujui pembimbing.
8. **Redaksi rumusan masalah no. 3.** Redaksi saat ini mengikuti lembar fakta. Peninjau menilai frasa "umpan balik latihan" belum operasional dan mengusulkan tiga alternatif. Ketiganya mengubah objek, jadi tujuan no. 3 harus ikut diubah:
   - a) "…ditinjau dari perubahan skor peragaan sebelum dan sesudah latihan, latensi umpan balik, persepsi kenyamanan pengguna, dan penilaian validator penutur tunarungu?"
   - b) "…ditinjau dari kesesuaian keputusan sistem dengan penilaian validator penutur tunarungu pada peragaan pemula, latensi, laju deteksi palsu, dan persepsi kenyamanan pengguna?" (paling selaras dengan BAB III saat ini)
   - c) "…ditinjau dari perubahan ketepatan peragaan menurut rubrik validator penutur tunarungu, latensi dan keandalan operasional sistem, serta persepsi kenyamanan pengguna?"

## 7. Penanda yang masih harus diisi

Daftar lengkapnya ada di `laporan-penanda.md`, dikelompokkan menurut pihak yang mengisi dan disertai lokasi berkas:baris. Laporan itu dibuat ulang dengan `python _laporan-penanda.py` setiap kali ada penanda yang diisi. Per 24 Oktober 2026 tersisa 35 penanda unik (38 kemunculan), seluruhnya PERLU DATA: keputusan bersama pembimbing (ambang G2/G3, batas operasional, tindakan gagal), data pribadi dan mitra (identitas, sekolah, jadwal, laptop), serta parameter rancangan Tabel 3.6. Seluruh 24 penanda PERLU RUJUKAN telah terisi.

Parameter rancangan BAB III yang baru ditetapkan menjelang eksperimen, seperti ambang gerbang, pembagian data, durasi, rubrik, dan kuesioner, kini terkumpul di **Tabel 3.6 (Subbab 3.10)**. Prosa cukup merujuk "(Tabel 3.6, butir n)".

## 8. Daftar istilah yang dipakai

Wi-Fi *Channel State Information* (CSI) · Sistem Isyarat Bahasa Indonesia (SIBI) · Bahasa Isyarat Indonesia (BISINDO) · tunarungu · pengisyarat · pembelajar pendengar · validator penutur tunarungu · isyarat terisolasi · umpan balik · *dataset* · *subcarrier* · estimasi pose · *keypoint* / *landmark* · klasifikator · *Support Vector Machine* (SVM) · *one-dimensional Convolutional Neural Network* (1D-CNN) · gerbang keputusan · node pemancar (TX) / node penerima (RX) · *dashboard* · sumber terbuka · pembagian data temporal · *leave-one-subject-out* · *leave-one-room-out* · laju pencuplikan (*sampling rate*).

## 9. Catatan teknis

- **Menomori ulang sitasi** setelah mengedit:
  1. Sunting berkas di `_berkunci/` (sitasi `[@kunci]`).
  2. Salin berkas itu ke folder `penomoran/` (atau folder kosong lain).
  3. Jalankan `python _nomori-sitasi.py penomoran`.

  Skrip menulis ulang ketiga bab di folder tersebut dengan nomor IEEE dan membuat `daftar-pustaka.md`. Daftar kunci dan entri IEEE-nya ada di dalam skrip. Kunci baru harus ditambahkan dulu ke kamus `REF` di skrip. Kalau mengedit langsung versi bernomor, nomor dan urutan daftar pustaka harus disesuaikan manual.
- **Diagram Mermaid** (Gambar 3.1 dan 3.2) tampil di penampil Markdown yang mendukung Mermaid. Untuk Word, gambar ulang di draw.io dengan struktur yang sama.
- **Panjang naskah:** BAB I sekitar 2.400 kata, BAB II sekitar 4.000 kata, BAB III sekitar 5.100 kata termasuk tabel dan diagram (prosa saja sekitar 2.900 kata).
- **Pemadatan BAB III:** Sebelum dipadatkan, BAB III sekitar 6.300 kata. Bagian yang mengulang BAB II diganti rujukan subbab, daftar prosedur dirampingkan, dan penanda keputusan rancangan dipindah ke Tabel 3.6. Hasilnya diverifikasi dari tiga sudut: kesetiaan isi, bahasa, dan konsistensi lintas bab. Kunci sitasi, angka wajib, tabel, dan diagram tetap utuh.
- **Kalimat *dashboard* di BAB I 1.1:** "skor keyakinannya" dihapus agar sama dengan lembar fakta dan BAB III, yang hanya menyebut isyarat terdeteksi dan kecocokannya.
- **Rujukan yang tidak dipakai:** Chadha dkk. (laporan WHO) dihapus dari BAB I karena dinilai sebagai angka hiasan yang memutus alur, sehingga tidak masuk daftar pustaka.
