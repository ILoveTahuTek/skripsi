# 03 — METODE: BAHAN PENULISAN BAB III

Purpose: everything needed to write BAB III with the **learning-tool framing**. Base structure follows skill proposal-writing v4/v5 (stages 3.1–3.11) and the existing DPJ-4 draft; changes below reflect the SIBI-only + learner-first scope.

## 1. Research stages (3.1) — narrative skeleton

Tahapan tetap: studi literatur (verifikasi Crossref) → perancangan perangkat (2× ESP32 CSI) → uji Delta-CSI fisik (gerbang go/no-go) → pemilihan kosakata → pengambilan data → ekstraksi fitur & pelatihan → evaluasi klasifikasi → (opsional) uji coba pemakaian pembelajar → analisis & pelaporan. `ID-READY opener template from corpus: "Penelitian ini dilaksanakan melalui beberapa tahapan yang disusun secara berurutan mulai dari studi literatur hingga penarikan kesimpulan."`

## 2. Hardware design (3.3) — unchanged physics, new narrative

- 2 nodes ESP32 (1 TX, 1 RX), capture CSI via ESP32-CSI-Tool (Hernandez & Bulut 2020, DOI `10.1109/wowmom49955.2020.00056`), streaming UDP to laptop/edge host.
- Node placement: penandatangan/pembelajar berdiri di zona antar node; kalibrasi 600 frame + anchor enrollment mengikuti prosedur RuView.
- New narrative point: perangkat digambarkan sebagai **meja latihan/pojok SIBI** — corner of a classroom, teacher's room, or home; the same commodity hardware a school can replicate.
- Delta-CSI physical gate stays week-3 go/no-go (unchanged, mandatory).

## 3. Vocabulary selection (3.4) — NEW emphasis, SIBI-dictionary grounded

Selection criteria (write as numbered list):
1. **Sumber resmi**: semua gestur diambil dari Kamus SIBI Digital (Kemendikdasmen) agar definisi kelas tidak ambigu — cite the KSD page (OFFICIAL-WEB).
2. **Kemampuan sensorik**: dominan gerak lengan/tubuh bagian atas (micromotion jari sulit terpisah pada single-link ESP32 — ruview-fitur §3a).
3. **Dipilih untuk pemula**: kosakata sapaan/percakapan harian (mis. salam, kata tanya, angka kecil, kata dasar kebutuhan) — sesuai kebutuhan persona P1–P3.
4. **Terpisah secara kinematik**: hindari pasangan gestur yang mirip; confusion matrix akan melaporkan kelas yang bertabrakan (strategi FSL-2024 & Wi-SL).
5. **Jumlah**: 5–12 kelas (batas studi kelayakan satu semester).

`ID-READY batasan sentence: "Kosakata yang diuji dibatasi pada 5–12 gestur SIBI dasar yang dominan menggunakan gerakan lengan dan dipilih dari Kamus SIBI Digital, dengan satu penandatangan per sesi pengambilan data."`

## 4. Data collection protocol (3.5) — two-group design (NEW)

| Group | Who | Purpose |
|---|---|---|
| G-A (pelatihan & uji utama) | 1–3 penandatangan fasih (guru SIBI/anggota komunitas, sesuai izin) | Membangun model klasifikasi per gestur: N repetisi per kelas per sesi |
| G-B (pemakai pembelajar, opsional pilot) | 3–5 pembelajar mendengar pemula | Observasi pemakaian: gestur mereka masuk model atau tidak; kualitas umpan balik; waktu latihan sampai dikenali |

- Ethics: izin orang tua/wali bila melibatkan anak; asentasi guru; anonimisasi; sensing tanpa kamera diposisikan sebagai keunggulan etis (R5 mitigation, gap-analisis §6).
- Deliverable dataset: proto-dataset CSI SIBI per kelas (perangkat, posisi node, subjek, repetisi) — first public mini-dataset of its kind (R2 mitigation).

## 5. Pipeline & classifier (3.6–3.7)

- Preprocessing: cleansing fase, kompensasi CFO/sampling offset, filtering; analisis band gerak tubuh (Doppler komponen orde 1–60 Hz) — BUKAN band napas 0,1–0,5 Hz (ruview-fitur §1 adaptation).
- Feature representation: (a) amplitudo+fase subcarrier (Cai 2024 komplementer); (b) spektrogram time-frequency (Tong 2023); coba keduanya, pilih berdasar hasil.
- Classifier candidates: CNN ringan pada spektrogram (SignFi paradigm), LSTM pada sekuens CSI (Ahmed 2021 IAICT); pemrosesan off-device (laptop) — ESP32 hanya capture (R3 mitigation).
- Metrics: akurasi per-gestur in-domain, confusion matrix, akurasi cross-domain (ruang/peubah subjek — Chen 2023 cross-domain survey; Widar3.0 sebagai strategi domain-invariant referensi).

## 6. Evaluation & go/no-go (3.8) — keep structure, add learning criterion

- Go/no-go fisik: Delta-CSI 2×ESP32 menunjukkan modulasi terukur pada gerak lengan (bukan hanya presence).
- Go/no-go klasifikasi: akurasi in-domain ≥80% pada ≥ (jumlah kelas − 2) kelas; jika gagal → fallback: kurangi kelas ke subset paling terpisah + lapor analisis (Tabel risiko).
- NEW success criterion (learning-side, optional pilot): sistem memberi umpan balik yang dinilai "jelas/bermanfaat" oleh ≥ sebagian besar pembelajar pilot (kuesioner sederhana skala Likert + catatan kualitatif) — dilaporkan sebagai observasi awal, bukan efek pembelajaran.

## 7. Optional learner pilot design (NEW subsection for 3.7/3.8)

- Partisipan: 3–5 dewasa mendengar tanpa pengalaman isyarat (mahasiswa/keluarga).
- Prosedur singkat: sesi latihan 20–30 menit dengan perangkat pada 5 gestur; ukur (a) jumlah percobaan sampai umpan balik pertama "benar", (b) akurasi gestur di akhir sesi, (c) kuesioner pengalaman (kemudahan, kenyamanan privasi, perasaan memahami kesulitan komunikasi tunarungu — 3 pertanyaan terbuka).
- Klaim maksimum: "observasi awal kegunaan sarana latihan"; tidak mengukur efektivitas pembelajaran jangka panjang atau skala empati.
- Fallback: bila waktu/izin tidak memungkinkan, hilangkan subbab ini (tandai opsional sejak awal di batasan).

## 8. Jadwal (3.9) — 16-week semester template (adapt from DPJ-4)

W1-2 literatur & izin; W3 Delta-CSI gate; W4-5 kosakata & protokol (konsultasi guru SIBI); W6-8 pengambilan data G-A; W9-10 pipeline & pelatihan model; W11 evaluasi & confusion matrix; W12 (opsional) pilot G-B; W13-14 analisis & penyusunan laporan; W15-16 perbaikan & seminar. Table 3.1 format unchanged.

## 9. Biaya (3.10) — low-cost emphasis (strengthen with numbers)

| Item | Estimasi |
|---|---|
| 2× ESP32 (DevKit) | Rp 100.000–200.000 |
| Tripod/mounting + kabel | Rp 50.000–100.000 |
| Laptop eksisting | Rp 0 (punya peneliti) |
| Transportasi/izin lokasi | Rp 100.000–300.000 |
| Cetak & administrasi | Rp 50.000–100.000 |
| **Total (rentang aman)** | **Rp 300.000–700.000** |

`ID-READY sentence: "Total kebutuhan biaya berada pada rentang ratusan ribu rupiah karena seluruh pengolahan memanfaatkan perangkat yang telah tersedia, sehingga sarana ini berpotensi digandakan oleh sekolah dengan biaya kecil."`

## 10. Risiko (3.11) — carry 5 risks, add R6

Carry R1–R5 from gap-analisis §6 unchanged; ADD:
- **R6 — Validitas "alat belajar" terbatas.** Uji coba pembelajar hanya pilot kecil; tidak bisa klaim efektivitas pembelajaran. *Mitigasi:* posisikan eksplisit sebagai studi kelayakan; target klaim utama tetap klasifikasi teknis; pelaporan pengalaman pembelajar bersifat kualitatif.

## 11. Rumusan–tujuan–batasan (ID-READY, updated set)

Rumusan masalah (Bagaimana…?):
1. `Bagaimana merancang dan membangun sarana latihan bahasa isyarat SIBI berbasis Wi-Fi CSI pada ESP32 yang mampu mengenali gestur terisolasi?`
2. `Bagaimana kelayakan klasifikasi gestur SIBI dari pola CSI pada rentang 5–12 kosakata dasar?`
3. `(Opsional) Bagaimana respons awal pembelajar mendengar terhadap penggunaan sarana latihan tersebut?`

Tujuan (mirror):
1. `Merancang dan membangun sarana latihan…`
2. `Menguji kelayakan klasifikasi…`
3. `(Opsional) Mengamati respons awal pembelajar…`

Batasan (7 butir — ambil 5–7): gestur terisolasi 5–12 kelas dari Kamus SIBI Digital; dominan gerak lengan; 1 penandatangan per sesi; ruang terkalibrasi; penerjemahan kalimat kontinu tidak dibahas; ekstraksi pose/kerangka tangan tidak dibahas; identifikasi personal tidak dibahas; (jika pilot diadakan: uji coba pembelajar bersifat observasi awal, bukan pengukuran efektivitas).
