# SPEC — Studi Kelayakan Pengenalan Kosakata Inti BISINDO Berbasis Wi-Fi CSI pada ESP32

> Dibuat dengan skill `to-spec` · 2026-10-12 · Sintesis dari percakapan riset judul (RuView → BISINDO).
> Status label kebaruan: SEARCH-LIMITED-plausible — wajib dicek Scopus/DBLP/literatur Mandarin sebelum klaim "pertama" ditulis.

## Problem Statement

Mahasiswa ingin membangun sistem yang membaca bahasa isyarat (BISINDO), postur, dan komunikasi visual manusia tanpa kamera, dengan memanfaatkan visualisasi WiFi dari proyek open-source RuView. Tiga hambatan terverifikasi membuat ide mentah itu tidak bisa langsung dijadikan judul skripsi: (1) pengenalan bahasa isyarat via WiFi CSI bukan hal baru — SignFi (2018) dan penerusnya sudah melakukannya, sehingga kebaruan modality gugur; (2) komponen pose on-device RuView masih berupa stub dengan akurasi jauh di bawah target, karena CSI satu-antena ESP32 secara fisika tidak menyelesaikan artikulasi tangan yang halus; (3) klaim "lebih efisien daripada kamera" belum pernah diukur pada kondisi pembanding yang setara. Di atas itu semua, tidak ada satu pun karya yang menerapkan WiFi CSI pada BISINDO — bahasa isyarat alami komunitas Tuli Indonesia — dan seluruh karya BISINDO yang ada berbasis kamera. Mahasiswa membutuhkan arah judul yang defensibel di sidang, layak untuk satu orang dalam enam bulan, dan tetap setia pada minat aslinya: komunikasi tanpa kamera.

## Solution

Skripsi studi kelayakan (feasibility study) yang mengukur seberapa jauh kosakata inti BISINDO — dibatasi 15–20 kata dengan gerakan lengan/lengan-atas yang besar, dipilih bersama komunitas Tuli — dapat dikenali dari Channel State Information (CSI) sinyal Wi-Fi murah berbasis ESP32, tanpa kamera pada waktu penggunaan. Sistem menangkap CSI dari beberapa pasang node TX-RX yang mengapit area penandatangan, mengekstrak fitur temporal-frekuensial per jendela waktu, dan mengklasifikasikannya dengan model kecil; video kamera dipakai HANYA sebagai ground-truth pelabelan saat pengumpulan data. Kontribusi tiga lapis: (a) hasil uji kelayakan fisik yang jujur (RQ1–RQ2), (b) dataset percontohan WiFi-CSI BISINDO pertama yang dirilis publik dengan DOI, (c) perbandingan empiris WiFi-CSI vs kamera pada kosakata yang sama (RQ3) yang menguji klaim efisiensi secara terukur. RuView diposisikan sebagai infrastruktur penangkapan CSI dan visualisasi, bukan sebagai mesin pengenalan.

## User Stories

1. As a mahasiswa peneliti, I want to mengukur kontras sinyal CSI antara kondisi diam dan gerakan kata BISINDO, so that saya punya dasar fisik go/no-go sebelum menulis pipeline apa pun.
2. As a mahasiswa peneliti, I want to mengenali 15–20 kata inti BISINDO dari CSI dengan akurasi top-3 yang dilaporkan jujur, so that skripsi saya punya hasil yang dapat dipertahankan di sidang.
3. As a mahasiswa peneliti, I want to membandingkan WiFi-CSI dan kamera pada kosakata dan kondisi yang sama, so that klaim "lebih efisien daripada kamera" menjadi temuan terukur, bukan asumsi.
4. As a mahasiswa peneliti, I want to mendeteksi kebocoran data lewat split blok-waktu dan evaluasi antar-penandatangan terpisah, so that akurasi yang saya laporkan tidak bohong karena data time-series bocor antar-split.
5. As a penandatangan BISINDO (komunitas Tuli), I want to dilibatkan sejak pemilihan kosakata dan protokol perekaman, so that dataset merepresentasikan bahasa yang benar-benar dipakai komunitas, bukan bahasa buatan.
6. As a penandatangan BISINDO, I want to memberi persetujuan informat yang jelas atas perekaman video dan sinyal RF saya, so that data saya tidak disalahgunakan dan martabat saya terjaga.
7. As a penandatangan BISINDO, I want to tahu bahwa sistem tidak mencoba mengidentifikasi pribadi saya, so that saya nyaman berpartisipasi.
8. As a komunitas Tuli Indonesia, I want to memiliki dataset BISINDO berbasis sensor alternatif yang dirilis publik, so that riset teknologi komunikasi Tuli tidak selalu bergantung pada kamera yang menatap wajah kami.
9. As a pembimbing, I want to melihat rancangan dengan jalur mundur elegan (jika sinyal terlalu lemah, studi kelayakan tetap menghasilkan temuan), so that risiko mahasiswa saya gugur di sidang menurun.
10. As a pembimbing, I want to melihat target metrik yang realistis (top-1/top-3, bukan klaim akurasi klinis), so that proposal tidak menjanjikan hal yang tak bisa dibuktikan dalam enam bulan.
11. As a penguji, I want to melihat klaim kebaruan yang dikualifikasi dengan benar (studi kelayakan BISINDO, bukan "pertama WiFi→isyarat"), so that saya tidak bisa menjatuhkan skripsi hanya dengan menyebut SignFi 2018.
12. As a penguji, I want to melihat protokol pengujian yang menutup konfounder (usia tanaman—bukan; penandatangan, posisi node, jadwal harian, orang lewat), so that kesimpulan kelayakan tidak mudah dipatahkan.
13. As a peneliti berikutnya, I want to mengunduh dataset WiFi-CSI BISINDO beserta label, log kejadian, dan deskripsi perangkat, so that saya bisa mereplikasi atau memperluas tanpa mengumpulkan data dari nol.
14. As a peneliti berikutnya, I want to membaca laporan keterbatasan fisika CSI satu-antena yang jujur, so that saya tidak mengulang kesalahan menargetkan fingerspelling halus pada hardware serupa.
15. As a pengembang RuView, I want to melihat hasil uji independen atas klaim presence/napas pada hardware ESP32 umum, so that proyek mendapat umpan balik validasi dari luar.
16. As a anggota rumah tangga Tuli, I want to sebuah sistem yang bekerja dalam gelap, di balik sekat, dan tanpa kamera menghadap ruang privat, so that komunikasi berjalan tanpa mengorbankan privasi.
17. As a mahasiswa peneliti, I want to memakai infrastruktur capture CSI yang sudah teruji (firmware ESP32-CSI-Tool/RuView), so that waktu enam bulan habis untuk pertanyaan riset, bukan membangun driver dari nol.
18. As a reviewer publikasi, I want to melihat perbandingan biaya-latensi-energi kedua modalitas dengan protokol yang sama, so that kontribusi sistemik paper lebih dari sekadar dataset.

## Implementation Decisions

- **Batasan kosakata:** 15–20 kata inti BISINDO dengan artikulasi besar (kanonik: MAKAN, MINUM, TIDAK, AKU, KAMU + usulan komunitas); fingerspelling dan handshape halus dikeluarkan karena di luar kemampuan fisika CSI satu-antena (didukung temuan repo RuView sendiri).
- **Perangkat keras:** 2–4 ESP32-S3 sebagai pasangan TX-RX yang mengapit area penandatangan (geometri memotong zona Fresnel); laptop sebagai gateway/pencatat; tripod dan penanda posisi tetap; housing pelindung konektor dari korosi. SBC opsional dan inferensi on-device TIDAK termasuk lingkup utama.
- **Capture:** firmware CSI standar (jalur ESP32-CSI-Tool atau firmware RuView — dipilih saat uji instrumen; yang lebih stabil menang). Data mentah CSI + video kamera tersinkron (flash/light cue awal sesi) untuk pelabelan.
- **Pipeline sinyal:** CSI amplitudo-only (fase ESP32 berderau) → pembersihan outlier (Hampel) → filter band-pass sesuai rentang gerakan manusia → jendela ±60 detik/overlap → fitur statistik waktu + spektral (varians antar-subcarrier, energi band gerak, entropy) → klasifikasi baseline kNN/SVM dulu; CNN/LSTM kecil hanya bila baseline menjanjikan; training di Colab.
- **Prosedur data:** minimal 3–5 penandatangan, ≥3 sesi pada hari berbeda, tiap kata diulang cukup untuk uji antar-hari; log kejadian harian (jam, posisi node, gangguan, orang lewat) wajib dicatat sebagai kovariat; usia/lingkungan perekaman dicatat.
- **Evaluasi dua sumbu:** (a) split blok-waktu (latih hari A–B, uji hari C) untuk RQ2; (b) leave-one-signer-out dilaporkan TERPISAH, tidak digabung, agar tidak mengklaim generalisasi palsu. Metrik: top-1, top-3, confusion matrix per kosakata.
- **Komparasi kamera (RQ3):** video yang sama diproses dengan pipeline kamera standar (pose/gestur MediaPipe atau setara) pada kondisi cahaya normal; variasi uji: cahaya mati, oklusi sebagian, jarak; tabel keluaran: akurasi, latensi per-frame, kebutuhan komputasi, biaya, skor privasi (kualitatif terdefinisi operasional).
- **Etika:** persetujuan informat tertulis; hak menarik diri; anonimisasi wajah pada video rilis dataset (blur/crop tangan saja bila komunitas meminta); koordinasi dengan organisasi komunitas Tuli; keputusan BISINDO (bukan SIBI) dikonfirmasi bersama komunitas.
- **Rilis dataset:** Zenodo dengan DOI sebagai kontribusi sekunder, hanya SETELAH eksperimen utama berjalan dan label tervalidasi; disertai log kejadian dan deskripsi perangkat.
- **Kebaruan dikualifikasi:** klaim yang diizinkan = "studi kelayakan/dataset percontohan BISINDO-CSI"; klaim yang dilarang = "pertama WiFi→bahasa isyarat", "pertama untuk hewan/manusia", "edge computing" tanpa inferensi on-device terukur.

## Testing Decisions

- **Uji instrumen (minggu 1–2, go/no-go):** validasi klaim dasar perangkat pada hardware sendiri — presence dan napas ala RuView, lalu kontras CSI 5 kata vs diam dianalisis kasar (t-SNE + kNN baseline). Kegagalan di sini = pivot desain sebelum pipeline dibangun.
- **Apa itu uji yang baik:** hanya menilai perilaku luar — akurasi pada data dari HARI dan PENANDATANGAN yang tidak pernah dilihat model; tidak menguji detail internal (nilai filter, bentuk fitur per-se). Setiap angka akurasi wajib menyertakan protokol split yang menghasilkannya.
- **Modul yang diuji:** (1) kontras sinyal per kata (RQ1, uji kelayakan fisik); (2) klasifikator pada split blok-waktu & leave-one-signer-out (RQ2); (3) tabel komparasi modalitas pada kondisi terkontrol (RQ3); (4) reprodusibilitas: satu orang lain menjalankan ulang analisis dari data mentah + skrip.
- **Prior art untuk protokol:** SignFi (IMWUT 2018) untuk struktur eksperimen CSI→isyarat; dataset word-level WiFi-CSI Bahasa Isyarat Bangladesh sebagai templat dataset bahasa isyarat nasional; praktik anti-leakage dari literatur time-series sensing (split blok-waktu, validasi antar-hari).

## Out of Scope

- Pengenalan multi-penandatangan bersamaan (superposisi sinyal — masalah terbuka, terlalu berat untuk enam bulan).
- Fingerspelling, handshape halus, dan kalimat kontinyu BISINDO.
- Inferensi on-device (TFLite/MCU) dan sistem produksi real-time; deployment ke smart home.
- Baseline pose 17-keypoint on-device (arah RuView ADR-079) — dicatat sebagai future work.
- Klaim klinis, terapi, atau diagnosis apa pun; penggantian penerjemah manusia.
- Pengembangan driver CSI baru dari nol.

## Further Notes

- **Risiko utama #1 = fisika:** jika kontras sinyal 5 kata uji terlalu kecil, seluruh desain dipivot; studi kelayakan tetap menghasilkan temuan (batas kemampuan CSI ESP32 untuk artikulasi) — ini jalur mundur yang elegan, bukan kegagalan.
- Referensi penopang sudah terverifikasi DOI (13 karya: SignFi, WiSign, DF-WiSLR, WiASL, DensePose-WiFi, Person-in-WiFi 3D, MM-Fi, survey edge Hernandez & Bulut, WiFine, Word-Level BISINDO, Sentence-Level BISINDO, dsb.) — lihat `verify_refs.json`.
- Spekulasi kebaruan berlabel SEARCH-LIMITED: jalankan pencarian Scopus/DBLP/Mandarin dulu; bila ditemukan karya BISINDO-CSI, judul bergeser ke replikasi/perluasan yang tetap layak.
- Kandidat judul (3): (1) "Studi Kelayakan Pengenalan Kosakata Inti Bahasa Isyarat BISINDO Berbasis Wi-Fi Channel State Information pada ESP32"; (2) versi dataset-forward; (3) versi komparatif kamera — pilih bersama pembimbing.
- Bila eksekusi ingin terstruktur: jalankan skill `to-tickets` atas spec ini untuk memecah menjadi tiket terurut (setup → instrumen → data → analisis → komparasi → rilis).
