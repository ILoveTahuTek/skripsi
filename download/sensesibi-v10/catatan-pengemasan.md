# Catatan Pengemasan — sensesibi-v10

**Tanggal:** 10 November 2026 (gelombang 9) · **Pemicu:** Agent Brief v10 Master (gelombang 6, 9 Nov) + penyuntingan humanizer-id (gelombang 7–9, 10 Nov) · **Skill:** sempro-mepet + naskah-id (arah pakai pemilik), poteto-mode untuk alur kerja, GEPA pada kalimat kritis, humanizer-id Mode Akademik Ketat (gelombang 7–9)

## 1. Isi paket

| Berkas | Keterangan |
|---|---|
| `Proposal-SenseSIBI-v10.md` | Naskah lengkap sumber tunggal: judul resmi + BAB I–III + Daftar Pustaka [1]–[94] + Log Perubahan gelombang 1–9 (log tidak dikonversi ke DOCX) |
| `Proposal-SenseSIBI-Studi-Kelayakan-v10.docx` | **Deliverable utama** — 91 hlm A4, TNR 12 pt, spasi 1,5, margin 4-3-3-3 cm, sampul judul SenseSIBI, TOC bidang, 13 tabel tiga-garis, 10 gambar 14 cm (semua ≥ 9,2 pt), 40 penanda `[PERLU DATA]` + 1 `[PERLU ILUSTRASI]` tersorot |
| `Proposal-SenseSIBI-Studi-Kelayakan-v10.pdf` | Pratinjau PDF 91 hlm (nomor halaman daftar isi terisi setelah "Update Field" di Word/WPS — sama seperti perilaku pratinjau versi sebelumnya) |
| `referensi/` | 63 berkas rujukan terunduh (PDF jurnal/arXiv/lembar data, halaman resmi HTML, README repo) + `Akses-94-Rujukan.md` manifes 94 entri: 56 terunduh · 20 peramban (gratis, blokir unduhan otomatis) · 18 berbayar/cetak |
| `assets/gambar-3.1..3.10.png` | 10 diagram BAB III hasil render Mermaid (metrik font ≥ 9,2 pt pada sematan 14 cm) |
| `diagram/G3.1..G3.10.mmd` | Sumber tunggal diagram, diekstrak langsung dari naskah |
| `_kerja/` | Jejak proses: `naskah-untuk-docx.md`, `split/` (4 berkas bab untuk generator) |
| `Review-Humanizer-Gelombang-8.md` | Laporan review humanizer-id gelombang 8 sesuai protokol luaran skill (mode, klasifikasi temuan, integritas, poin konfirmasi) |
| `Review-Humanizer-Gelombang-9.md` | Laporan review humanizer-id gelombang 9 (ritme KRF-003, deiksis sisa, deduplikasi lintas bab, koreksi konsistensi 2.10) |

## 2. Perubahan gelombang 9 (review humanizer-id: ritme kalimat + deiksis sisa, 10 Nov) — ringkas

Menindaklanjuti rekomendasi laporan gelombang 8: (a) **koreksi konsistensi** 2.10 "tiga" → "empat dimensi tambahan" (butir yang dirinci memang Pertama–Keempat); (b) **deduplikasi lintas bab** — definisi distilasi pengetahuan yang hampir verbatim di 3.7.4 dipindah tanggung jawabnya ke 2.5, 3.7.4 kini langsung membenarkan pilihan teknik dengan [78] tetap menempel; (c) **KRF-003 ritme**: 3.7.6 dipecah (CV 0,25→0,40), 3.2.5 empat kalimat 29–41 kata dipecah (RUN 6→3), 3.6.1 kalimat tiga peran dipecah + verba ulang *memeriksa…memeriksa* dipangkas; (d) **anfora 3.1** "Rumusan masalah pertama/kedua/ketiga…" dipecah; (e) **2.5** dua kopula *merupakan* beruntun → apositif, dua *yaitu* apositif → em-dash/titik dua; (f) **R.1**: dua paragraf raksasa 1.1 (±370/±350 kata) dipecah lima paragraf; (g) **deiksis dekat** 15 *tersebut* (1.1:4, 2.3:6, 2.4:5) → *itu*/nomina ulang; "penerimaan tersebut" → "ketiganya". Hasil badan naskah: *tersebut* 48→32, *yaitu* 53→50, *sehingga* 55 stabil, *Adapun* 0. Audit pra=pasca 154 pemicu (0 riil baru — kelas positif palsu terdokumentasi). Integritas: 94 sitasi, token numerik, dan struktur identik; DOCX+PDF 91 hlm di-build ulang; verifikasi python-docx + pypdf + uji frasa + inspeksi visual VLM lulus semua. Laporan: `Review-Humanizer-Gelombang-9.md`; rincian per lokasi: Log Perubahan gelombang 9 di ujung naskah MD.

## 3. Perubahan gelombang 8 (review humanizer-id: pengurangan ritme slop, 10 Nov) — ringkas

Review lanjutan atas keluhan "masih terlalu slop": audit `scripts/audit.py` (145 pemicu, 8 riil + 137 positif palsu terdokumentasi) + telaah manual dimensi ritme. Suntingan riil: (a) 6× pembuka *Adapun* dihapus (3.6.3, 3.8.1–3.8.4, 3.8.6); (b) penipisan deiksis *tersebut* 63→46 (±20 lokasi → *itu/ini*/nomina ulang); (c) penipisan rantai *sehingga* 69→55 (14 kausal longgar → titik koma/karena itu/yang membuat); (d) 9 appositive *yaitu* non-enumeratif → koma/titik dua/tanda kurung (*yaitu* enumeratif sahih dipertahankan); (e) 9 template anfora formulaik pecah ("Kondisi tersebut menandakan/mendorong", "X tersebut menjadi dasar/titik Y", "Berdasarkan X tersebut", signposting "Berdasarkan uraian tersebut" dibuang); (f) 3 kausal bersarang *karena…sehingga* dibongkar (N-1, modalitas dijaga); (g) caption Gambar 3.4 *deployment* dicetak miring. Integritas: 94 sitasi + 30 bilangan kunci terverifikasi utuh; struktur 4 BAB/30 subbab/14 tabel/10 gambar identik; DOCX+PDF 91 hlm di-build ulang; verifikasi python-docx + pypdf lulus semua. Laporan lengkap: `Review-Humanizer-Gelombang-8.md`; rincian per lokasi: Log Perubahan gelombang 8 di ujung naskah MD.

## 4. Perubahan gelombang 7 (humanizer-id, 10 Nov) — ringkas

Penyuntingan gaya semata (Mode Akademik Ketat; audit `scripts/audit.py` repo apissaj/humanizer-id + telaah manual 144 pemicu; 12 suntingan riil, 132 positif palsu ditelaah dan dibiarkan): 3 koma terlarang sebelum *sehingga* (SPE-001); 3 korelatif *tidak … melainkan* → *tidak … tetapi* (SYT-001); 2 verba ringan dipangkas — *melakukan validasi* → *memvalidasi*, *melakukan segmentasi, ekstraksi fitur, dan inferensi* → *menyegmentasi … mengekstraksi … menjalankan inferensi* (VRB-001); hapus pembuka *Adapun* + kopula (KEH-001); *metodologi pelatihan* → *metode pelatihan* (BAK-006); deiksis semu *tabel berikut* → *Tabel 3.6* (TBG-001); frasa *itu sendiri* ditanggalkan (SPB-002). Tanpa perubahan substansi, angka, sitasi, struktur, tabel, gambar, atau penanda `[PERLU]`. Rincian per baris tercatat pada Log Perubahan gelombang 7 di ujung naskah MD.

## 5. Perubahan gelombang 6 (Agent Brief v10) — ringkas

1. **Judul resmi dipertahankan**: *Studi Kelayakan Purwarupa SenseSIBI: Sistem Penerjemahan Dua Arah Huruf SIBI Berbasis Wi-Fi CSI dengan Inferensi ESP32-S3 dan Pemrosesan Server*.
2. **BAB I tiga pilar**: (a) filosofi *social-first* dengan ESP32-S3 ~Rp150.000 (data anggaran pemilik, diverifikasi ulang pada analisis biaya G4); (b) paradigma Wi-Fi sebagai penginderaan spasial + RTLS (Widar2.0); (c) pembuktian jalur bebas kamera. Rumusan–tujuan tetap cermin 1:1; batasan diperbarui (Poco F4 5G, rantai daya Li-Po/BMS/TP4056, TTS *on-device*).
3. **BAB II**: matriks justifikasi "Mengapa X dan Bukan Y?" (Tabel 2.3, 7 keputusan); BoM 11 komponen dengan deskripsi/tujuan/poin spesifik (Tabel 2.4 + uraian); SLR ditambah WiFinger (MobiHoc 2016), FingerDraw (IMWUT 2020), MeshID (Sensors 2024) — Tabel 2.2 kini 20 baris; 2.7 TTS ditulis ulang (Kokoro ONNX *on-device* utama, prasyarat suara Indonesia di G3, alternatif MMS-TTS-ind ONNX); 2.9 menambah tumpukan purna Rust (Tokio/Axum, Leptos WASM, Tauri) dengan tiga justifikasi; 2.10 menambah kerangka TKT/TRL (Mankins 2009).
4. **BAB III**: subbab baru 3.5.5 (enclosure cetak 3D + Tabel 3.4 pinout GPIO 13 baris, menghindari pin strapping 0/3/45/46), 3.5.6 (perangkat lunak purna Rust + Gambar 3.8), 3.5.7 (inferensi Kokoro TTS ONNX di Poco F4 5G, target < 100 ms, fallback MMS); gerbang G0–G4 ditulis ulang sesuai brief: G0 baseline CSI-jaringan (pendengar UDP Rust, kehilangan paket ≤ 0,1%), G1 model tepi int8 + distilasi (inferensi < 100 ms), G2 konsultasi tiga pilar pakar (SIBI, RF, *embedded AI*), G3 integrasi Rust + mesin ucapan, G4 sintesis kelayakan + rekomendasi TKT/TRL 3–4 (Tabel 3.6 berisi ambang kuantitatif usulan); Tabel 3.1 kini 13 baris (11 BoM + AP + webcam), Tabel 3.2 kini 17 baris (menambah Rust/Tokio/Axum, Leptos, Tauri, Kokoro+ONNX Runtime); risiko bertambah 2 baris.
5. **Penomoran**: tabel BAB III bergeser (skema pembagian → 3.5; kriteria gerbang → 3.6; jadwal → 3.7; parameter → 3.8; risiko → 3.9); gambar bertambah (enclosure → 3.7, pipeline Rust → 3.8; inferensi → 3.9; evaluasi → 3.10). Sitasi dinomori ulang 83 → **94** mengikuti urutan kemunculan pertama; seluruh 94 dikutip di tubuh, tanpa sitasi menggantung (audit otomatis lolos).

## 6. Kejujuran klaim (disiplin yang dijaga)

- Target kinerja Rust (parsing < 0,2 ms; memori < 40 MB) dan TTS (< 100 ms) dinyatakan eksplisit sebagai **target rancangan yang diukur pada G3**, bukan hasil.
- *Model card* Kokoro (audit Okt 2026): 8 bahasa, 54 suara, **tanpa Indonesia** — ketersediaan suara Indonesia dijadikan **prasyarat G3** dengan alternatif ekspor ONNX MMS-TTS-ind; audit ini tetap dicantumkan apa adanya.
- Klaim ukuran murid int8 "~8–55 KB" pada brief **tidak diadopsi** karena bertentangan dengan tolok ukur ESP-DL yang dikutip naskah (ratusan kilobita); ukuran final dilaporkan pada uji *deployment*.
- Sitasi lembar data MAX98357A tidak dimasukkan (URL penerbit tidak terverifikasi dari *sandbox*); spesifikasinya berstatus data BoM pemilik. INMP441 dikutip dengan URL resmi TDK yang terverifikasi.
- WPC: dirujuk sebagai repositori milik peneliti yang telah diaudit penuh (gelombang 2, 6 Nov 2026); tidak masuk Daftar Pustaka karena masih privat bagi pembaca umum.
- Jumlah rujukan tidak dipaksa: 11 rujukan baru hanya ditambah karena dikutip dan terlacak (Crossref/ACM/arXiv/MDPI/GitHub resmi, diverifikasi 9 Nov 2026).

## 7. Verifikasi ekspor

- Gelombang 9: verifikasi ulang penuh — DOCX 91 hlm + PDF 91 hlm di-build ulang; 7 frasa suntingan baru masuk dan 5 frasa lama ("tiga dimensi tambahan", "Rumusan masalah kedua dijawab melalui", "Distilasi pengetahuan merupakan teknik", "G4 menilai penerimaan tersebut", "YOLO26 merupakan keluarga") hilang (python-docx + pdftotext hlm. 5/32/40/48/64/66); audit pra=pasca 154 pemicu tanpa regresi; 94 sitasi + token numerik utuh (multiset pra=pasca); inspeksi visual VLM 8 halaman (sampul, hlm. suntingan, DP) bersih.

- Gelombang 8: verifikasi ulang penuh — DOCX 91 hlm (4 BAB/30 subbab/14 tabel/10 gambar, 0 placeholder); frasa suntingan baru masuk dan frasa lama ("Adapun…", "Berdasarkan uraian tersebut", "Kondisi tersebut menandakan/mendorong") hilang di DOCX (python-docx) dan PDF (pypdf, hlm. 5–8/62/72); audit pasca-suntingan tanpa regresi (145 pemicu, semua sisa = positif palsu terdokumentasi); 94 sitasi + 30 bilangan kunci utuh.

- Gelombang 7: verifikasi ulang penuh — DOCX 91 hlm; 12/12 suntingan masuk DOCX (audit python-docx) dan PDF (ekstraksi pypdf, hlm. 28/39/40); audit presisi ulang bersih; pemicu audit turun 144 → 124 (sisa positif palsu regex baris-panjang: nomor IEEE 802.11, judul bab baku, baris log).

- `parse_md.js` → 94 entri DP, 10 gambar, 13 tabel konten, 40+1 penanda tersorot.
- `postcheck.py` (skill docx): 0 galat; 2 peringatan lama (spasi tabel 9 pt by design; TOC field) — konsisten baseline.
- Metrik diagram: 10/10 LOLOS (font efektif 9,2–12,7 pt @ 14 cm; tanpa pemangkasan).
- VLM pratinjau PDF: sampul utuh; Tabel 2.3/2.4 rapi setelah lantai kolom "No." dinaikkan 4%→6%; pinout, enclosure, pipeline Rust, kriteria gerbang, dan DP bersih; duplikasi TOC akibat placeholder dihilangkan (kembali ke perilaku bidang Word standar).
- `periksa.py` (naskah-id): tanpa galat EYD baru; temuan gaya lama tetap diterima (penghubung ritual, "Respon" pada judul paper, "F1 makro" istilah metrik).

## 8. Sisa keputusan pemilik

1. 40 penanda `[PERLU DATA]` (identitas sampul, frasa uji, rubrik pakar, model final layar, kapasitas baterai, dsb.) + 1 `[PERLU ILUSTRASI]` (foto/render komponen BoM + model enclosure 3D).
2. Suara bahasa Indonesia untuk Kokoro (mis. suara komunitas/penyetelan lanjutan) — prasyarat G3; tanpa itu jalur *on-device* otomatis ke MMS-TTS-ind ONNX.
3. 20 rujukan jalur peramban (gratis) perlu diunduh manual bila ingin arsip PDF lengkap; 18 rujukan berbayar/cetak tercatat pada manifes.
4. Konfirmasi pembimbing: ambang gerbang usulan (Tabel 3.6), rubrik tiga pilar pakar, dan daftar frasa uji ucapan.
5. "Update Field" daftar isi setelah menyunting DOCX di Word/WPS (petunjuk tercetak di bawah daftar isi).
