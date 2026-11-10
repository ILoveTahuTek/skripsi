# Laporan Review Humanizer-id — Gelombang 9

**Naskah:** Proposal-SenseSIBI-Studi-Kelayakan-v10 (BAB I–III + Daftar Pustaka, 91 hlm DOCX/PDF)
**Tanggal:** 10 November 2026
**Skill:** [apissaj/humanizer-id](https://github.com/apissaj/humanizer-id) v1.5.1 — audit `scripts/audit.py` + telaah manual SKILL.md
**Lokasi sunting:** `Proposal-SenseSIBI-v10.md` (master), DOCX + PDF di-build ulang dari master

---

## 1. Informasi Mode Kerja

`[Mode: Akademik Ketat]`

Sudut pandang impersonal dan kalimat pasif metodologi dipertahankan (safeguard positif palsu SKILL.md §1.B); EYD V dan leksikon KBBI; sitasi terajut berbasis gagasan. Gelombang ini menjalankan rekomendasi laporan gelombang 8: **variasi panjang kalimat (KRF-003) pada zona paling monoton, penipisan deiksis dekat *tersebut* yang tersisa, dan pembersihan duplikasi lintas bab**. Tidak ada gelombang sunting mekanis baru (koma, morfologi, konjungsi) — seluruh kaidah tersebut sudah bersih sejak gelombang 7–8.

## 2. Ringkasan Temuan

### A. Audit otomatis (`scripts/audit.py`): 154 pemicu — 0 riil baru, semua kelas positif palsu terdokumentasi

| Kategori | Pemicu | Status |
|---|---|---|
| EJ-004/EYD-025 "angka 2 reduplikasi" | 64 | **Positif palsu semua** — label teknis: G2 (gerbang), T2 (tahap), M2 (mileston), R2/P2/O2/S2/DSP2 (aktor diagram), Widar2.0, MobileNetV2, CTranslate2, YOLO26; terverifikasi `rg '\b[A-Za-z]+2\b'`: 69 kemunculan, 100% label teknis |
| GLOS-TEK/LIN (deployment, deep learning, science, framework) | 17 | **Positif palsu** — judul asing entri Daftar Pustaka (zona terlarang sunting: kutipan harfiah) |
| Tabel log revisi (KJK/SPE/TBB/UIN/EYD) | 17 | **Positif palsu** — kutipan keadaan lampau pada log gelombang 1–8 |
| WDY-001 "pelesapan agen" | 8 | **Positif palsu** — butir daftar bernomor tujuan/langkah uji (konvensi daftar skripsi) |
| TBB-001/PFP-006 "antara … dengan/atau" | 12 | **Positif palsu** — regex lintas kalimat melampaui batas titik (mis. "antarmodul, dengan konfigurasi" terbaca "antara…dengan"); "antara SIBI dan teks atau ujaran" dipertahankan (judul resmi, poin konfirmasi gel. 8) |
| KJK-005 ", karena" (L178) | 1 | **Positif palsu** — koma milik konektor antarkalimat "Meskipun demikian,"; klausa kausal awal-kalimat sah dengan koma penutup klausa |
| BPK-010 "misalnya" (L697) | 1 | **Positif palsu** — "misalnya" di dalam kurung memberi contoh sebagian dari butir, bukan pembuka perincian tuntas |
| BRN-002 judul subbab generik | 4 | **Dibekukan** — format BAB skripsi mengikuti pedoman kampus (poin konfirmasi gel. 8, menunggu keputusan pemilik) |
| Lain-lain (TII-003 DP, BAK-012 antar-*split*, dst.) | sisanya | **Positif palsu** — kelas yang sama dengan gelombang 7–8 |

Audit pra-sunting dan pasca-sunting sama-sama 154 pemicu: **tidak ada pelanggaran mekanis baru; suntingan gelombang 9 tidak memperkenalkan kaidah yang dilanggar.**

### B. Telaah manual (pemindai ritme KRF-003 + pembacaan penuh) — temuan riil dan tindakannya

Pemindai ritme (`scripts/sensesibi-v10/scan_ritme_gel9.py`) mengukur koefisien variasi (CV) panjang kalimat dan rentetan kalimat sepanjang-pita-serupa (RUN) per subbab:

| Zona | Masalah riil | Tindakan | Hasil |
|---|---|---|---|
| **3.7.6 Skema Pembagian Data** (CV 0,25 — paling datar) | Lima kalimat 9–24 kata, ritme monoton | Kalimat kausal dipecah: "Pembagian acak tidak dipakai. Repetisi berurutan cenderung mirip, dan kemiripan itu berpotensi membocorkan…" | CV 0,25 → 0,40 |
| **2.10 Evaluasi Kelayakan** | **Bug konsistensi**: "dinilai dari *tiga* dimensi tambahan" padahal dirinci **Pertama–Keempat** (empat butir) | "tiga" → "empat" | Konsisten; angka kuantitatif lain tak tersentuh |
| **3.7.4 Model Guru Kamera** | Definisi distilasi pengetahuan **hampir verbatim duplikat** dengan 2.5 (ekor kalimat dan sitasi [78] identik) — *tell* AI klasik lintas bab | 3.7.4 langsung membenarkan pilihan teknik: "Distilasi pengetahuan [78] dipilih karena CSI tidak memuat citra tubuh; …" — definisi penuh tinggal di 2.5 (BAB II) | Duplikasi hilang; [78] tetap menempel pada nama teknik |
| **3.1 Desain Penelitian** | Anfora tiga kalimat "Rumusan masalah pertama… kedua… ketiga…" (pola template gel. 8) | Kalimat kedua dibalik: "Uji klasifikasi, uji *deployment*, dan uji jalur bahasa … menjawab rumusan masalah kedua." | Anfora pecah; ritme paragraf hidup |
| **3.2.5 Tahap T4** (RUN kalimat 29–41 kata) | Empat kalimat panjang beruntun, dua *yaitu* bersebelahan | Kalimat 38 kata dipecah dua; enumerasi antarmuka ke tanda kurung; kalimat 41 kata dipecah, "penerimaan tersebut" → "ketiganya" | RUN 6→3; kalimat terpanjang turun |
| **3.6.1 Partisipan** | Satu kalimat tiga peran (40 kata, tiga semikolon) + verba ulang *memeriksa…memeriksa* | Dipecah tiga kalimat, satu per peran; "memeriksa lembar definisi huruf dan sampel segmen" | Verba ringan ulang hilang (VRB); R.1 |
| **2.5 Estimasi Pose** | Dua kopula *merupakan* beruntun; dua *yaitu* apositif non-enumeratif | "YOLO26, keluarga model …, mendukung…" (apositif); "— distilasi pengetahuan —" (em-dash); "tanpa kamera: murid menyimpulkan…" (titik dua) | Ritme pembuka hidup; *yaitu* −3 |
| **1.1 Latar Belakang** | Dua paragraf raksasa (±370 dan ±350 kata) mencampur 3–5 ide pokok | Paragraf terakhir dipecah tiga (batasan & ketidakpastian / metode & gerbang / pernyataan penelitian & penamaan); paragraf rancangan dipecah dua (perangkat & arah pertama & server / arah kedua & jalur ucapan & infrastruktur) | R.1: satu paragraf satu ide pokok |
| **Deiksis dekat sisa** | 15 *tersebut* dengan anteseden pada kalimat yang sama/sebelumnya (1.1: 4, 2.3: 6, 2.4: 5) | → "itu" atau nomina diulang ("Komponen Doppler"); anteseden selektif ("Kedua preseden pertama tersebut") dipertahankan | *tersebut* 48 → 32 badan naskah |

**Zona yang sengaja tidak disentuh** (kesejajaran enumerasi adalah kaidah, bukan slop — SKILL.md AS.3/L.3): rentetan G0–G4 pada 3.2, butir daftar bernomor 3.8.3/3.8.5, katalog komponen 2.13, baris tabel, deskripsi alur dua arah 3.5.1 yang mencerminkan diagram, dan katalog penelitian terdahulu 2.2/2.11 (sitasi multi-nama terajut dalam satu kalimat, gaya sah BAB II). Konektor transisi antarkalimat dicek ulang: masih jauh di bawah ambang "maksimal satu per halaman" (4A). Retorika formulaik (*bukan berarti, menyelami, merajut, lanskap, Di era digital*) — nihil.

## 3. Integritas Ilmiah (Aturan Wajib SKILL.md)

- **Angka & data:** token numerik pra = pasca (verifikasi multiset; satu-satunya selisih adalah koma apositif "YOLO26," dari suntingan 2.5, bukan angka); 30 bilangan kunci gel. 8 (90–95%, 77,7%, 1,9%, 14,9%, 5,6%, 91%, 500 orang, 1,92 juta, 3.840, Rp150.000, Rp350.000, 96,4%, 99,54%, 0,2 ms, 2.300→54 ms, 69,2 ms, 82 juta, 100–300 MB, mAP50 0,8944/0,9580, 97,6%, 240 MHz, 512 KB, 8 MB, 12,5 cm, 120 Hz, 50 bingkai, dll.) tak berubah.
- **Sitasi:** 94 sitasi unik [1]–[94] utuh, nol hilang, nol baru; [78] tetap hadir di 2.5 dan 3.7.4.
- **Derajat modalitas:** tidak ada harapan dinaikkan/turunkan; "berpotensi membocorkan" (kalibrasi gel. 8) dipertahankan pada pemecahan kalimat 3.7.6; "telah terbukti" pada 3.7.4 tetap pada klaim pra-penelitian yang didukung angka repositori.
- **Struktur:** 3 BAB, 30 subbab, 35 sub-subbab, 14 tabel, 10 gambar (G3.1–3.10), 10 diagram mermaid, 46 penanda PERLU DATA — identik. DOCX 91 hlm, PDF 91 hlm. Verifikasi python-docx (386 paragraf, 14 tabel) + pypdf (91 hlm) + uji frasa (7 frasa baru masuk, 5 frasa lama hilang) lulus semua; pemeriksaan visual 8 halaman via VLM: tidak ada render rusak, placeholder PERLU DATA pada sampul memang disorot untuk data pemilik.

## 4. Tabel Selisih Beranotasi (ringkas)

Tabel lengkap 12 baris tercantum pada log gelombang 9 di bagian akhir naskah master. Ringkasan kaidah yang dipakai: KRF-003 (variasi panjang kalimat), R.1 (satu paragraf satu ide pokok), AJ-1 (koreferensi/anafora), AI-4 via gel. 8 (apositif non-enumeratif tanpa *yaitu*), VRB (pemangkasan verba ulang), dan satu koreksi konsistensi bilangan (2.10 tiga→empat dimensi; butir dirinci memang empat).

**Total: 154 pemicu audit ditelaah (0 riil baru); 28 suntingan diterapkan pada 12 lokasi naskah; ±960 kalimat badan naskah dipertahankan utuh.**

## 5. Poin Konfirmasi Penulis

1. **BRN-002 (judul bab generik; kelanjutan gel. 8):** "BAB II Kajian Pustaka" dan "BAB III Metode Penelitian" masih mengikuti format baku skripsi. Bila pedoman pembimbing mengizinkan judul substantif, penggantian dapat dipertimbangkan — menunggu keputusan pemilik.
2. **"antara SIBI dan teks atau ujaran" (kelanjutan gel. 8):** tetap dipertahankan karena menempel pada judul resmi penelitian. Bila dianggap taksa, alternatif "teks/ujaran" dapat menggantinya serentak di judul dan badan — menunggu persetujuan.
3. **Kepadatan sisa:** *tersebut* 32, *yaitu* 50, *sehingga* 55. Sisa *tersebut* adalah anteseden jauh/selektif/taksa, sisa *yaitu* enumeratif tuntas, sisa *sehingga* kausal kuat berpremis. Penipisan lebih lanjut berisiko merusak koreferensi dan keajegan istilah; rekomendasi gelombang berikutnya (bila masih diperlukan) adalah pembacaan menyeluruh bersama pembimbing, bukan suntingan otomatis.
4. **Dua poin konfirmasi gel. 8 masih terbuka** (lihat laporan gelombang 8): perluasan judul subbab dan frasa judul resmi.

## 6. Berkas Terkait

- Naskah master tersunting: `Proposal-SenseSIBI-v10.md` (log gelombang 9 tercantum di bagian akhir)
- DOCX di-build ulang: `Proposal-SenseSIBI-Studi-Kelayakan-v10.docx` (91 hlm)
- PDF di-build ulang: `Proposal-SenseSIBI-Studi-Kelayakan-v10.pdf` (91 hlm)
- Keluaran audit: `scripts/sensesibi-v10/audit_humanizer_gel9.txt` (pra-) dan `audit_humanizer_gel9_post.txt` (pasca-)
- Pemindai ritme & verifikasi: `scripts/sensesibi-v10/scan_ritme_gel9.py`, `analisis_audit_gel9.py`, `verifikasi_gel9.py`
