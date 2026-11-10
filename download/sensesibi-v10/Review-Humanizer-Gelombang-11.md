# Review Humanizer Gelombang 11 — Revisi Masukan Dosen Pembimbing

**Tanggal:** 10 November 2026 · **Pemicu:** permintaan pemilik menyampaikan masukan dosen pembimbing: tulisan masih terlalu AI dan terlalu kompleks (terkesan tesis S3/karya profesor), tidak ada emosi pada tiap kata, daftar pustaka terlalu banyak, sumber data harus dari Indonesia (masalah berada di Jawa Timur, bukan Amerika Serikat), dan bahasa masih terasa terjemahan kasar — jangan memaksakan padanan yang tidak lazim (contoh dilarang: "sandbox" menjadi "kotak pasir") · **Jenis pekerjaan (taksonomi sempro-mepet):** Tulis ulang BAB I + sunting menyeluruh BAB II–III + pemangkasan daftar pustaka; register mahasiswa D4/S1, kaidah naskah-id (EYD V), gaya humanizer-id Mode Akademik Ketat.

## 1. Lingkup dan metode

1. Keluaran berbasis versi ringkas gelombang 10 (44 hlm) yang diubah menjadi naskah baru v11 melalui salinan sumber terpisah (`_kerja-g11/src/`) dan pipeline terpisah (`rakit_g11.py` + `build_docx_g11.sh` + `parse_md_g11.js`/`generate_docx_g11.js`); gelombang 7–10 tidak tersentuh.
2. Sitasi ditulis dengan **kunci semantik** pada naskah sumber (mis. `[brin]`, `[mursita]`, `[kamus-cetak]`) lalu dinomori ulang urut kemunculan; setiap kunci dipetakan ke entri DP asli dengan penanda teks wajib yang diverifikasi skrip (`rakit_g11.py`), sehingga kesalahan pemetaan nomor-sumber gelombang 10 terkoreksi secara konstruksional.
3. Emosi ditafsirkan sesuai register ilmiah (humanizer-id melarang kata konotatif/kiasan): kehangatan dicapai lewat situasi konkret dan taruhan manusia — keluarga pendengar, guru menjelaskan sementara siswa menebak, satu juru bahasa untuk hampir 4.000 orang, harga Rp150.000 membuat sekolah berani memasang alat — bukan lewat kata sifat bombastis.

## 2. Perubahan utama

| Butiran | Gelombang 10 | Gelombang 11 | Dasar |
|---|---|---|---|
| Register kalimat | rata-rata ±26–30 kata, klausul berlapis | rata-rata **18,6 kata** (median 17), satu gagasan per kalimat | masukan "terlalu kompleks, seperti S3" |
| Pembuka BAB I | statistik demografi Amerika Serikat (Mitchell-Karchmer 90–95%) | situasi manusia Indonesia: keluarga pendengar, juru bahasa 1:±4.000, ruang kelas | masukan "sumber data dari Indonesia" |
| Konteks lokasi | tidak disebut | **Jawa Timur** eksplisit di 1.1, 1.4 butir 7, dan 3.3 (sekolah mitra `[PERLU DATA]`) | masukan "masalah di Jawa Timur" |
| Daftar Pustaka | 93 entri (≥73 asing) | **46 entri** — 15 Indonesia + 31 asing (13 di antaranya dokumentasi resmi perangkat) | masukan "daftar pustaka terlalu banyak" |
| Urutan DP awal | campuran AS lebih dulu | entri [1]–[13] seluruhnya sumber Indonesia (KemenkoPMK, UU 8/2016, Kamus SIBI, As Satillah, Nugraheni, Malika, BRIN, Mursita, KASIBI, OpenSIBI, Dwijayanti, Soekarta, Maulana) | prioritas sumber Indonesia |
| Rumusan/tujuan | butir 1 sepanjang tiga baris berisi lima istilah teknis (distilasi, server purna Rust, protokol perekaman) | tiga butir kalimat tunggal; rincian teknis pindah ke batasan dan BAB III | masukan "terlalu kompleks" |
| Klaim kamera | "paparan kamera diduga menimbulkan kelelahan nonverbal [Bailenson]" (spekulatif) | diganti alasan faktual: pencahayaan/garis pandang dan rasa diawasi | integritas klaim |
| Istilah asing | sudah miring, satu-dua padanan dipaksakan | tetap asing seluruhnya (*on-device*, *fallback*, *deploy*, *beacon*, *enclosure*, *smartphone*); nol padanan dipaksakan; "kotak pasir" tidak muncul | masukan "jangan memaksakan terjemahan" |
| Bab/struktur | 44 hlm, BAB II 11 subbab, BAB III 3.1–3.11, Tabel 3.1–3.8, 6 prosedur, 3 gambar | identik; Tabel 2.2 11→8 baris (baris Filipino, keystroke, Person-in-WiFi keluar) | substansi metode dijaga |

## 3. Integritas (verifikasi skrip + pemeriksaan dokumen)

- **Sitasi:** 46 unik urut kemunculan 1–46 tanpa celah; kunci→entri diverifikasi penanda teks wajib; sisa kunci di DOCX: nol; nol sitasi numerik lama tertinggal.
- **Koreksi bug gelombang 10:** sitasi BRIN yang menempel [9], survei 100 responden yang menempel [10], dan *Kamus SIBI* yang menempel [54] — ketiganya salah sumber — kini benar ([7], [8], [3]) karena penomoran diturunkan dari kunci semantik.
- **Angka kunci:** 34 dari 35 token pra-penelitian terverifikasi utuh (mAP50 0,8944/0,9580, akurasi 97,6%, 2.300 ms→54 ms, 69,2 ms, 13 menit/59 detik, Rp150.000, Rp350.000, 1,92 juta, 500 juru bahasa, 77,7%/1,9%/91%, 3,362/4, 99,8%/86,66%, 56 *subcarrier*, 600 bingkai/8 *anchor*, M1–M14, G0–G4, TKT/TRL 3–4); token "100–300 MB" memang tidak dibawa ke v11 karena kalimatnya dipadatkan, bukan berubah nilai.
- **Cermin rumusan–tujuan:** 3:3 verbatim ✓; batasan 9 butir selaras BAB III ✓.
- **Penanda:** 25 `[PERLU DATA]` + 1 `[PERLU ILUSTRASI]` tersorot; penanda baru yang wajar: nama sekolah mitra Jawa Timur.
- **Dokumen:** DOCX 12 tabel + 40 heading, PDF **36 hlm**, 3 gambar tertanam, nol halaman kosong pada inspeksi visual (sampul, daftar isi, pembuka BAB I, tabel 2.x/3.x, DP); nol asterisk literal; nol "XXX/TODO".

## 4. Audit humanizer-id resmi (repo apissaj/humanizer-id)

Audit `scripts/audit.py` atas naskah akhir: **52 temuan di tubuh, seluruhnya kelas positif palsu terdokumentasi** (tidak ada yang disunting tanpa dasar):

| Kode | Jumlah | Klasifikasi |
|---|---|---|
| EJ-004/EYD-025 | 30 | penanda teknis Widar2.0, DSP2, R1/R2, T0–T2, G2, M1–M14, TP4056 — bukan reduplikasi kata |
| GLOS-TEK | 8 | *deep learning*, *deployment*, API — istilah asing dominan dipertahankan miring (tangga keputusan istilah; juga permintaan eksplisit pemilik) |
| WDY-001 | 7 | butir tujuan dan langkah prosedur me- (agens elipsis = konvensi korpus) |
| BRN-002 | 2 | rumus korpus "manfaat teoretis dan manfaat praktis" |
| TBB-003/PT-002 | 2 | korelatif lintas kalimat ("…[2], tetapi jaminan itu…") — bukan kalke "bukan A tetapi B" |
| KJK-001 | 1 | "Karena itu," — penghubung awal kalimat sah |
| WDY-002 | 1 | subjek inanimat "Model juara mencatat…" — verba lapor standar |
| JRN-007 | 1 | "&" di nama diri *Sensing & Translation of SIBI* |

Tiga temuan riil pada pra-audit telah disunting: koma terlarang sebelum *karena* (SPE-001/KJK-005), pola "antara … dan … atau" pada rumusan/tujuan 1 (PFP-006) menjadi "menghubungkan SIBI dengan teks dan suara", dan pengulangan verba *mencatat…mencatat* (WDY-002 dorongan) → *mencapai*. Semua koma sebelum *sehingga* (8) dibersihkan. *"tersebut"* 1x (rumus korpus "Berdasarkan rumusan masalah tersebut"); *Adapun* 0; *hal ini* 0; pembuka klise 0.

## 5. Keputusan yang perlu diketahui pemilik

1. **36 hlm, sedikit di bawah target "sekitar 40".** Penurunan utama bersumber dari pemangkasan DP (93→46) dan kalimat yang lebih pendek; bila ingin naik mendekati 40, kandidat yang sehat: memulihkan 2–3 subsubbab prosedur 3.8, menambah 1–2 penelitian terdahulu Indonesia di Tabel 2.2, atau DP 12 pt lagi — semua tanpa menambah istilah kompleks.
2. **Klaim tanpa statistik demografi AS.** "Anak tunarungu umumnya lahir dari orang tua yang mendengar" kini berdiri sebagai penalaran awal tanpa angka; bila dosen meminta angka Indonesia, sumbernya perlu dicari lalu masuk sebagai `[PERLU DATA]` — tidak dipakai angka AS.
3. **Tabel 2.2 kehilangan tiga baris preseden internasional** (Filipino CSI, keystroke, Person-in-WiFi) sesuai pemangkasan DP; kelompok preseden masih terwakili SignFi/WiSign/DF-WiSLR/DensePose from WiFi.
4. **Entri [6] Malika dan Berlianti** memakai nama jurnal sebagaimana terverifikasi pada gelombang pemeriksaan rujukan (Consore: Journal of Social Sciences and Humanities) — tidak diubah.

## 6. Rekomendasi tindak lanjut

1. Isi `[PERLU DATA: nama SLB atau lembaga mitra di Jawa Timur]` (3.3, 1.1, 1.4) — satu-satunya data lokasi yang benar-benar belum ada.
2. Jalankan "Update Field" pada daftar isi setelah penyuntingan di Word/WPS.
3. Bila dosen masih menganggap DP 46 entri banyak, kandidat pemangkasan berikutnya adalah dokumentasi alat (Tokio/Axum/Leptos/Tauri) yang dapat digabung satu sitasi dokumentasi per keluarga — bukan sumber Indonesia.
