# Catatan Pengemasan — DOCX Proposal Penerjemah Dua Arah SIBI

**Paket:** `download/translator-sibi-docx/` · Disusun 26 Oktober 2026 · **Direvisi 27 Oktober 2026: redesain seluruh diagram BAB III (6 → 8 figur, huruf cetak 3,2–6,4 pt → 9,2–11,8 pt) atas audit keterbacaan pemilik — lihat `Audit-dan-Rencana-Diagram.md` dan bagian 2b.**
**Berkas utama:** `Proposal-Penerjemah-Dua-Arah-SIBI-CSI-ESP32S3.docx` (68 halaman A4, 2,8 MB)
**Pratinjau:** `Pratinjau-Proposal-Penerjemah-Dua-Arah-SIBI.pdf` (hasil konversi LibreOffice; pembagian halaman di MS Word dapat sedikit bergeser)
**Sumber isi:** `download/translator-sibi-draft/` (Task 21 — draft final dengan metodologi utama distilasi guru–murid YOLO26-Pose → model murid CSI → inferensi tepi ESP32-S3). Seluruh angka, sitasi, dan fakta TIDAK diubah satu pun; pekerjaan ini murni pengemasan DOCX.

## 1. Struktur dokumen

| Bagian | Nomor halaman | Keterangan |
|---|---|---|
| Sampul | tanpa nomor | Judul kapital 3 baris + tabel identitas 5 baris (nilai `[PERLU DATA]` disorot kuning) + baris tahun |
| Daftar Isi | romawi kecil i–iii | Bidang TOC otomatis (klik kanan → *Update Field* setelah menyunting); 64 entri H1–H3 |
| BAB I–III + Daftar Pustaka | arab 1–63 | Tanpa pemisah halaman paksa antarbab (mengikuti keputusan Task 19–21 dan proposal DPJ-4 sebelumnya) |

Format: Times New Roman 12pt, spasi 1,5 (line 360), margin 4-3-3-3 cm, paragraf rata kanan-kiri berindentasi baris pertama 1,25 cm, tabel tiga-garis 9pt dengan keterangan di atas (kiri), keterangan gambar di bawah (tengah), daftar pustaka indentasi gantung 80 entri [1]–[80], sitasi IEEE `[n]` apa adanya, penanda `[PERLU DATA: ...]` disorot kuning agar mudah dicari-ganti di Word.

## 2. Diagram BAB III — varian tata letak lama (26 Okt, digantikan)

Pada penyusunan pertama, lima dari enam diagram dirender dari varian tata letak khusus DOCX (`scripts/translator-sibi-docx/diagram-docx/`, 3.1 tiga kolom, 3.2 dua kolom, 3.5 alur ular, 3.4 arah TB, 3.6 tiga kolom) karena rantai TD sandbox ber-aspek 1:5–1:9. Hasil ukur pasca-ekspor: huruf efektif cetak hanya **3,2–6,4 pt** pada lebar konten 14 cm — di bawah ambang keterbacaan; varian 3.1 bahkan terpangkas tinggi (aspek 1,78 > batas 20,6 cm) sehingga lebar tampil menyusut menjadi 12,0 cm. Salinan varian dipertahankan sebagai arsip, tidak dipakai lagi.

## 2b. Redesain 27 Oktober 2026 — audit, pemecahan, dan hasil ukur

Atas audit pemilik (dua gambar contoh = masalah keterbacaan dan kepadatan; audit diperluas ke seluruh diagram), seluruh diagram BAB III didesain ulang dari sumber tunggal `translator-sibi-draft/diagram/G3.x-*.mmd` (Mermaid, dapat diedit; tanpa lapisan varian). Laporan audit lengkap, arsitektur figur, dan jejak integritas: `Audit-dan-Rencana-Diagram.md`.

| Gambar | Isi (level) | Kanvas (px logis) | Huruf cetak | Sebelum |
|---|---|---|---|---|
| 3.1 Tahapan T0–T5 + gerbang, jalur lolos (L1) | 12 simpul, ular 2 kolom | 924×950 (1,03) | **10,3 pt** | 3,2–4,8 pt |
| 3.2 Jalur gagal & remediasi gerbang (BARU, L3) | 5 baris urut G0–G4, lingkaran keluaran | 997×1334 (1,34) | **9,5 pt** | — (bagian dari 3.1 lama) |
| 3.3 Distilasi (I): perekaman, penyaringan, guru, penyandingan (L2) | 8 simpul, 2 kolom | 1039×886 (0,85) | **9,2 pt** | 4,3–5,8 pt |
| 3.4 Distilasi (II): pelatihan murid → deployment (L2) | 7 simpul, TD cabang alami | 987×1230 (1,25) | **9,6 pt** | — (bagian dari 3.2 lama) |
| 3.5 Arsitektur produk akhir (L2) | 16 simpul, 3 rantai sejajar | 1016×1136 (1,12) | **9,4 pt** | 3,5–4,7 pt |
| 3.6 Topologi jaringan (L2) | 10 simpul | 1035×1356 (1,31) | **9,2 pt** | 4,8–6,4 pt |
| 3.7 Inferensi tepi ESP32-S3 (L3) | 8 simpul, 2 kolom | 930×690 (0,74) | **10,2 pt** | 6,4–8,5 pt |
| 3.8 Alur evaluasi hingga artefak (L2) | 9 simpul, TD cabang alami | 809×1072 (1,32) | **11,8 pt** | 5,3–7,1 pt |

**Keputusan pemecahan/penggabungan (logika ilmiah utuh, terverifikasi pemeriksa otomatis `cek_integritas.py` — 76 simpul & 64 sisi sumber seluruhnya terwakili):**
1. **3.1 dipecah**: jalur utama (lolos) tetap 3.1; seluruh jalur gagal (P0–P4), uji ulang (G0U/G1U), dan terminal (S0/S1) pindah ke 3.2 — keputusan uji ulang menjadi label sisi "lolos/gagal lagi" (percabangan dipertahankan, notasi diringkas); kriteria lengkap gerbang di prosa §3.2.1–3.2.5.
2. **3.2 lama (distilasi) dipecah** pada keluaran gerbang kualitas data: akuisisi+guru+penyandingan (3.3) dan pelatihan murid+pembanding+deployment (3.4); simpul penyaringan (FLT) dari 3.6 lama disisipkan ke 3.3 sehingga rantai perekaman–penyaringan–guru utuh.
3. **3.6 lama difokuskan ke evaluasi** (rantai perekaman–pelatihan tidak diulang — terwakili 3.3–3.4; simpul masuk menunjuk Gambar 3.4); akibatnya sisi DEP→OP dan DEP→COVER kini digambar utuh (generalisasi sisi klaster lama hilang).
4. **3.5 (arsitektur) & 3.6 (topologi) dirapikan**: teks simpul dipadatkan (rincian tetap di prosa), 3.5 memakai tiga rantai sejajar tanpa kotak kelompok (pengelompokan dijelaskan caption); 3.6 memakai sisi taklihat AWAN~~~SERVER hanya untuk penataan.
5. **Simpul NOTE pada inferensi dihapus dari gambar**: batas perangkat sudah di BAB II [29]; kewajiban satu kanal + WIFI_PS_NONE dipindah ke prosa §3.7.8 [28].
6. Terminologi, nomor subbab/tabel, loop umpan balik, pembanding, dan label keputusan ("lolos/gagal", "ya/tidak/belum") dipertahankan verbatim; konfigurasi desain bersama: `config-24.json` (fontSize 24 px; `wrappingWidth: 700` — mermaid 12 membungkus label di 120 px bila tak disetel; tema neutral, aman grayscale).

## 3. Hasil verifikasi

- `postcheck.py` (skill docx): **0 galat**, 1 peringatan diterima — spasi baris campuran 360 (badan, 1,5 spasi) vs 276 (sel tabel, rapat) memang disengaja mengikuti konvensi skripsi; profil spasi identik dengan proposal DPJ-4 yang sudah diterima.
- Peta halaman PDF (redesain): 8 gambar masing-masing **sehalaman penuh dengan keterangannya** (hlm. 31, 32, 34, 35, 40, 42, 49, 50); seluruhnya 14,0 cm selebar konten tanpa pemangkasan tinggi (maks 18,7 cm).
- QA visual VLM (glm-5v-turbo) versi 26 Okt: PASS; versi redesain 27 Okt diverifikasi deterministik (`qa_ekspor.py`: posisi/lebar 8 gambar + 16 pemeriksaan teks — semua OK) dan inspeksi halaman (3.2, 3.5, 3.3, 3.1) perender PDF.
- Jumlah penanda di DOCX: **38 `[PERLU DATA]`** badan naskah + 6 sampul, **0 `[PERLU RUJUKAN]`**; caption Gambar 3.2 memuat legenda keluaran (bukan penanda).
- Daftar pustaka: 80 entri [1]–[80] utuh, semuanya dikutip di badan naskah (diverifikasi `rakit_draft.py`, LOLOS 13 ok / 0 galat).
- Perbaikan kecil pada sumber: baris T3 pada Tabel 3.5 (jadwal) di `bab3-metodologi.md` memuat satu sel kosong berlebih (18 vs 17 kolom) sehingga kolom Gerbang bergeser; sel berlebih dihapus dan dokumen gabungan dirakit ulang — verifikasi otomatis tetap LOLOS. Isi data tidak berubah.

## 4. Sisa pekerjaan pemilik (human-owned)

- Mengisi 44 penanda `[PERLU DATA]` (sorotan kuning): identitas sampul (6), keputusan Tabel 3.6 (27), spesifikasi layar/audio/baterai/AP (4), layanan awan TTS+ASR (2), waktu-lokasi (2), isyarat terpilih (1), etika (1), frasa uji kegunaan (1).
- 7 konfirmasi pembimbing yang tercantum pada `translator-sibi-draft/catatan.md` (5 lama + kebijakan jalur awan + kuota Kaggle). **Pembaruan 27 Okt 2026: butir 2 (frasa judul) sudah dikunci final oleh pemilik** — judul final *"Purwarupa Penerjemah Dua Arah Isyarat SIBI Berbasis Wi-Fi Channel State Information pada Modul ESP32-S3 dengan Inferensi Tepi dan Pemrosesan Bahasa pada Server: Studi Kelayakan Kosakata Terbatas"* — sehingga sisa konfirmasi tinggal 6 butir; judul pada sampul DOCX sudah sesuai dan tidak perlu di-render ulang.
- (Redesain 27 Okt) Meninjau hasil pemecahan figur: 3.1/3.2 (jalur lolos vs gagal), 3.3/3.4 (distilasi dua tahap), dan fokus evaluasi 3.8 — struktur antarfigur dijelaskan `Audit-dan-Rencana-Diagram.md`; tidak ada lagi generalisasi sisi klaster yang perlu ditinjau karena seluruh sisi digambar utuh.

## 5. Cara regenerasi

```bash
bash /home/z/my-project/scripts/translator-sibi-docx/render_diagrams.sh   # 8 PNG dari sumber sandbox -> assets/
python3 /home/z/my-project/scripts/translator-sibi-docx/bangun_diagram.py # ukur huruf efektif (target >= 9 pt)
python3 /home/z/my-project/scripts/translator-sibi-docx/cek_integritas.py # integritas simpul/sisi vs sumber lama
cd /home/z/my-project/scripts/translator-sibi-docx
node parse_md.js            # markdown draft -> parsed.json
node generate_docx.js       # parsed.json -> DOCX
python3 patch_footer.py     # patch field halaman (kompatibilitas WPS)
python3 /home/z/my-project/skills/docx/scripts/add_toc_placeholders.py \
  /home/z/my-project/download/translator-sibi-docx/Proposal-Penerjemah-Dua-Arah-SIBI-CSI-ESP32S3.docx --auto
```
