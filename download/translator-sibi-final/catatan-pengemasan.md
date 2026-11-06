# Catatan Pengemasan — translator-sibi-final

**Tanggal:** 28 Oktober 2026 · **Sumber:** `draft-final.md` hasil suntingan Claude (dikembalikan pemilik via Drive) + skill `sempro-mepet` & `naskah-id` (arah pakai dari pemilik)

## 1. Isi paket

| Berkas | Keterangan |
|---|---|
| `draft-final.md` | Naskah final hasil Claude: baris 1–981 = naskah (judul baru + BAB I–III + DP [1]–[80]); setelah penanda `AKHIR NASKAH` = Log Perubahan + Daftar Temuan + Pernyataan verifikasi (TIDAK dikonversi ke DOCX) |
| `Proposal-Studi-Kelayakan-Purwarupa-SIBI-CSI-ESP32S3.docx` | **Deliverable utama** — 68 hlm A4, TNR 12 pt, spasi 1,5, margin 4-3-3-3, sampul judul baru 5 baris, TOC 64 entri, 9 tabel tiga-garis, 8 gambar 14 cm, 44 penanda `[PERLU DATA]` tersorot (6 sampul + 38 tubuh), DP 80 entri |
| `Pratinjau-Proposal-Studi-Kelayakan-Purwarupa-SIBI.pdf` | Pratinjau PDF 68 hlm |
| `_kerja/` | Jejak Claude (`_kerja/draft-final.sebelum-selaras.md`, hasil-workflow.json, chunk c0–c8, cek.py) + `naskah-untuk-docx.md` (naskah murni hasil pemisahan dari log) + `split/` (4 berkas bab untuk generator) |

## 2. Judul baru (keputusan pemilik, 28 Okt 2026)

STUDI KELAYAKAN PURWARUPA SISTEM PENERJEMAHAN DUA ARAH ANTARA SISTEM ISYARAT BAHASA INDONESIA (SIBI) DAN TEKS ATAU UJARAN BAHASA INDONESIA BERBASIS WI-FI CHANNEL STATE INFORMATION (CSI) DENGAN INFERENSI MODEL PADA ESP32-S3 DAN PEMROSESAN BAHASA PADA SERVER UNTUK KOSAKATA TERBATAS

Terpasang: sampul (5 baris, menggantikan judul terkunci lama) — mengikuti `draft-final.md`. Penutup latar belakang, rumusan no. 1 & 3, tujuan no. 1 & 3 sudah diselaraskan Claude dengan judul baru.

## 3. Verifikasi sebelum dan sesudah bangun DOCX

**Invarian mandiri (naskah vs naskah-sumber):** 44 penanda `[PERLU DATA]` · DP [1]–[80] lengkap · 8 blok mermaid verbatim · caption Gambar 3.1–3.8 urut · judul baru di baris 1 · angka jangkar identik (`26+9` = singkatan prompt; bentuk naskah "26 huruf … 9 angka" identik di 4 lokasi) · diff 76 baris (7,8%) konsisten dengan Log Perubahan Claude.

**Skill `naskah-id` (`periksa.py`):** 6 temuan — 4× penghubung gaya (AI-17) + 2 positif palsu lama yang diterima sejak Task 17 ("F1 makro" istilah metrik; "Respon" judul asli paper [9]). **Tidak ada galat EYD baru.**

**Skill `sempro-mepet`:** standar struktur/register — naskah sudah memenuhinya (disusun dengannya); pekerjaan sesi ini adalah *pengemasan*, bukan penulisan.

**Ekspor:** postcheck 0 galat (1 peringatan lama: spasi tabel 9 pt) · qa_ekspor 8/8 gambar 14,0 cm tanpa pemangkasan (hlm 31–50) + 14 spot-check teks OK · VLM: sampul bersih (judul 5 baris utuh), halaman Tabel 3.6 bersih.

## 4. Sisa keputusan pemilik (tidak disentuh siapa pun)

1. **44 penanda `[PERLU DATA]`** — 6 sampul + 32 BAB I–III (identitas, perangkat, layanan awan, dst.) + 27 Tabel 3.6 (parameter rancangan, menunggu pembimbing/hasil T0–T4).
2. **Tabel 2.2 baris 17 + 2.11 ¶3** masih frasa judul lama — sel tabel terkunci saat penyuntingan Claude (lihat Daftar Temuan draft-final.md).
3. **"ujaran" (judul) vs "ucapan" (prosa)** — sinonim; menunggu keputusan pemilik untuk penyeragaman.
4. **±40 temuan Claude** di Daftar Temuan `draft-final.md` (istilah *kata-level*/*chip*/*router*, urutan tampil-kirim, ketidakseragaman diagram↔prosa, dst.) — semuanya dibiarkan sesuai protokol minimal-intervensi.
5. **6+1 konfirmasi pembimbing** (gaya sitasi IEEE, ambang G2/G3, dua ruang mitra, token validator, jalur ucapan awan, Kaggle, jumlah bab sistematika).
6. **Update Field** daftar isi di Word/WPS setelah dokumen diedit (petunjuk tercetak di bawah daftar isi).

---

# Revisi 6 November 2026 — Integrasi pipeline WPC + pangkas rujukan sulit dijangkau

**Pemicu:** permintaan pemilik: (1) repositori `github.com/ILoveTahuTek/WPC` berisi pipeline pelatihan YOLO26 + kode + data latih — harus tercermin dalam proposal; (2) "hapus referensi yang sulit dijangkau".

**Hasil audit keterjangkauan (verifikasi ulang 6 Nov 2026, jam 21–23):**
- 17 rujukan DIHAPUS — naskah penuh di balik paywall penerbit tanpa salinan terbuka legal: [1],[2] Mitchell & Karchmer (MUSE); [4] Ritmeester (Oxford JDSDE); [18] MLMSign (Elsevier ISWA); [22] DF-WiSLR (Elsevier PMC + salinan penangguh Taylors mati); [23] Baldeo (IEEE TENCON); [24] WiSign (ACM TIST); [39] Chen (ACM CSUR, tanpa salinan penulis); [43] Picron (bab Springer); [44] Hakozaki (ACM ASSETS); [45] Kamus SIBI cetak 1994 (tanpa versi digital); [46] Stokoe (Oxford JDSDE); [66] Ahmed (IEEE IAICT); [67] Qin (Elsevier Measurement); [71] Chow (IEEE TIT; memo MIT tak terverifikasi dari sandbox); [74] Rakun (IEEE TIME-E); [75] Anggraini (IEEE ICEEI).
- 63 rujukan DIPERTAHANKAN — semuanya bisa diunduh gratis: arXiv (Whisper, MMS, YOLO26, MediaPipe, DensePose-WiFi, Kiranyaz, Hinton, Zheng-pose), repo GitHub (esp-csi, RuView, esp-nn, esp-dl, faster-whisper, tflite-micro), OJS kampus (UIN Suka, UAI AUDHI, umj Holistika, um-sorong Insect, nurulfikri DBESTI, STIAYP Concept, ipm2kpe INTECOMS, mdp Rabit, poltekba JST, TMJ), thesai (Dwijayanti, Wiguna), salinan penulis resmi (vhil Stanford-Bailenson, gzhou-Ma CSUR, Tsinghua-Widar3.0, UW-Ong&Ranganath, CVF-Person-in-WiFi, Temple-Shang&Wu, Oregon-Cortes&Vapnik, aboutgis-Mountrakis, VIPL-Sagawa, Isfahan-Sokolova, bayes.wustl-Nyquist, Paris-Shannon, sigmobile-WiKey, ebulutvcu-Hernandez), arsip (archive.org-Likert, PMC-Lieberman/Bowen/Mosleh), dokumen resmi (Espressif datasheet, UU 8/2016, Kemenko PMK, BRIN, Kamus SIBI Digital, Google/Azure/Ultralytics docs, kartu model HF MMS-TTS & Kokoro).
- 8 di antaranya memblokir unduhan otomatis (Cloudflare/portal) tetapi tetap gratis di peramban: KASIBI, OpenSIBI, SignFi, WiKey, Kindy, Sebastian, HandFi, Safrida.

**Perubahan naskah:**
- DAFTAR PUSTAKA 80 → 63 entri; seluruh sitasi dinomori ulang [1]–[63] (skrip `scripts/wpc-integrasi/renumber_pustaka.py`, peta tercatat di Log Perubahan draft).
- Klaim yang kehilangan sumber direbut/ditulis ulang: 90–95% Mitchell→[3]; overfitting lintas domain→Widar3.0 [40→32 baru]; masalah terbuka SLMT→survei Ong & Ranganath; Kamus SIBI cetak→Kamus SIBI Digital [10→7 baru]; mekanisme penolakan→keputusan rancangan (tanpa sitasi); kalimat mouthing avatar, kata berinfleksi Rakun/Anggraini, DF-WiSLR/FSL/WiSign/LSTM/WiASL dihapus.
- Tabel 2.2: 17→13 baris (baris WiSign, DF-WiSLR, Baldeo, Rakun dihapus; "Penelitian ini" kini baris 13, sel terkunci tetap verbatim).
- Integrasi WPC: 3.2.3 (pelatihan guru memakai pipeline terimplementasi), Tabel 3.2 +baris 5 "Repositori pipeline pelatihan YOLO26 (WPC)" (12 baris), 3.4 bahan, 3.7.4 (pipeline + data latih tersedia; alur baku Ultralytics [42→34]). Repositori WPC PRIVAT saat revisi (endpoint git 401) — tidak dimasukkan Daftar Pustaka; rincian konfigurasinya menunggu akses pemilik.

**Verifikasi ekspor ulang:** 65 hlm (sebelumnya 68) · TNR 12 pt, spasi 1,5, margin 4-3-3-3 tetap · 9 tabel tiga-garis (2.2 kini 13 baris; 3.2 kini 12 baris) · 8 gambar 14 cm (aset dipakai ulang, tidak berubah) · 44 penanda [PERLU DATA] tersorot di XML (38 tubuh + 6 sampul) · DP 63 entri [1]–[63] seluruhnya dirujuk balik di tubuh, tanpa sitasi menggantung · VLM: sampul utuh, Tabel 2.2/3.2 rapi, diagram 3.3/3.5 utuh berketerangan, halaman akhir [63] · pdftotext: tanpa jejak penulis terhapus.

**Sisa keputusan pemilik:** tetap sama (44 penanda PERLU DATA — kini 6 sampul + 38 tubuh; baris 13 Tabel 2.2 & 2.11 ¶3; ujaran vs ucapan; 6+1 konfirmasi pembimbing; update field daftar isi di Word/WPS) + BARU: akses ke repo WPC (privat) bila ingin rincian pipeline dimasukkan.

---

# Revisi 6 November 2026, gelombang 2 — Verifikasi isi repositori WPC (akses pemilik)

**Pemicu:** pemilik memberi akses token GitHub → repositori `github.com/ILoveTahuTek/WPC` (privat) berhasil dikloning penuh (495 berkas, 2,3 GB) dan diaudit.

**Isi repositori terverifikasi:** README 12 bab — model juara exp06b pose mAP50 0,8944 / box 0,9098 pada 49 kelas (25 huruf + 24 kata); rantai pretraining COCO-pose → hand-keypoints (box 0,991/pose 0,895) → SIBI v1 (pose 0,821); dataset v2 FROZEN: 4 sumber 9.953 gambar → dedup md5 −2.215 → leak-guard dHash −18 → MediaPipe 7.210 gambar/7.627 objek, split 6.231/650/329; ratchet Kaggle T4×2 seed 42 EPS 0,002 dengan ledger 9 eksperimen (exp00 0,8445 → exp03 mosaic 0,3 → exp05 lr0 0,004+cos → exp10 60 epoch 0,8888 → juara exp06b pose 16/kobj 3 0,8944); exp11 24 huruf murni pose mAP50 0,9580, akurasi huruf 97,6% @conf 0,25; bobot juara 50,5 MB dengan MANIFEST sha256; `inference_sibi.py` keluaran JSON 21 keypoint; aplikasi: 24 huruf statis + J/Z huruf gerak, label stabil + tahan 0,5 s.

**Perubahan naskah (draft-final.md):**
- Tabel 3.2 baris 5: fungsi repositori dirinci (skrip konversi bergate kualitas, pelatihan deterministik GPU Kaggle, pencatatan eksperimen otomatis, verifikasi artefak, bobot terlatih).
- 3.4: bahan penelitian ditambah "yang telah diverifikasi kelengkapannya".
- 3.7.4 ¶2: ditulis ulang — alur kerja teruji ujung-ke-ujung, bukti 9 eksperimen (pose mAP50 0,8944, 49 kelas), penyesuaian eksplisit: penargetan ulang kepala keypoint pose tangan 21 titik → 17 keypoint COCO jalur guru.
- Catatan revisi 1 (Log gelombang 1) diperbarui; Log Perubahan gelombang 2 ditambahkan (bagian log, tidak masuk DOCX).
- Daftar pustaka: tidak ada perubahan (63 entri; pemangkasan 17 paywall selesai di gelombang 1).

**Ekspor ulang & verifikasi:** DOCX 65 hlm (2.744.802 byte), TNR 12/1,5/4-3-3-3 tetap, 10 tabel, 8 gambar, H1×4, H2×28 — struktur identik baseline; 5 frasa kunci revisi terkonfirmasi di DOCX (0,8944, penargetan ulang kepala, checksum, perceptual hash, diverifikasi kelengkapannya); verifikasi visual Tabel 3.1/3.2 (hlm 32–33) dan 3.7.4 (hlm 41) rapi tanpa overflow; pratinjau PDF diperbarui; penanda PERLU tubuh 38 (tetap).

**Keamanan:** token GitHub pemilik sempat lewat percakapan — wajib di-revoke setelah selesai (README WPC Bab 12 juga mensyaratkannya); token tidak pernah ditulis ke berkas yang di-commit (repo WPC dikloning ke `wpc-repo/` yang masuk `.gitignore`).
