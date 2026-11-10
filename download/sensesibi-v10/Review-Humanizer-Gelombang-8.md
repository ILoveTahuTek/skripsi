# Laporan Review Humanizer-id — Gelombang 8

**Naskah:** Proposal-SenseSIBI-Studi-Kelayakan-v10 (BAB I–III + Daftar Pustaka, 91 hlm DOCX/PDF)
**Tanggal:** 10 November 2026
**Skill:** [apissaj/humanizer-id](https://github.com/apissaj/humanizer-id) v1.5.1 — audit `scripts/audit.py` + telaah manual SKILL.md
**Lokasi sunting:** `Proposal-SenseSIBI-v10.md` (master), DOCX + PDF di-build ulang dari master

---

## 1. Informasi Mode Kerja

`[Mode: Akademik Ketat]`

Sudut pandang impersonal dipertahankan; kalimat pasif metodologi dipertahankan (safeguard positif palsu SKILL.md §1.B); EYD V dan leksikon KBBI; sitasi terajut berbasis gagasan. Gelombang ini menindaklanjuti keluhan "masih terlalu slop" setelah gelombang 7 (yang memperbaiki 12 isu mekanis): sasaran gelombang 8 adalah **ritme leksis berulang** yang tidak tertangkap regex — sumber utama rasa "keluaran mesin".

## 2. Ringkasan Temuan

### A. Audit otomatis (`scripts/audit.py`): 145 pemicu — 8 riil, 137 positif palsu terdokumentasi

| Kategori | Pemicu | Status |
|---|---|---|
| EJ-004 / EYD-025 "angka 2 reduplikasi" | 64 | **Positif palsu semua** — regex `\b[a-zA-Z]+2\b` menangkap label teknis: G2 (gerbang uji), T2 (tahap), M2 (mileston), R2/P2/O2/S2/DSP2 (aktor diagram), Widar2.0, MobileNetV2, CTranslate2 |
| GLOS-TEK/GLOS-LIN (deployment, deep learning, science, framework, dll.) | 17 | **Positif palsu** — jatuh pada judul asing entri Daftar Pustaka (zona terlarang sunting: kutipan harfiah) |
| KJK-004/SPE-001/TBB-003/PT-002/UIN-004/EYD-020 di tabel log revisi | 10 | **Positif palsu** — kutipan keadaan lampau pada tabel log gelombang 1–7 |
| WDY-001 "pelesapan agen" | 8 | **Positif palsu** — butir daftar bernomor tujuan/langkah uji ("1. Merancang…", "2. Mengukur…"); konvensi daftar skripsi, bukan kalimat buntung |
| BRN-002 judul subbab generik | 4 | **Dibekukan** — kaidah penerbit buku BRIN; format BAB skripsi mengikuti pedoman kampus (dicatat sebagai poin konfirmasi) |
| TBB-001/PFP-006 "antara SIBI dan teks atau ujaran" | 6 | **Positif palsu** — "antara" sudah berpasangan "dan"; "teks atau ujaran" satu satuan nomina konsisten dengan judul resmi |
| TBB-003/PT-002/UIN-004 lintas kalimat | 6 | **Positif palsu** — regex `.+?` melampaui batas titik; "bukan/meskipun" dan "tetapi" berada di kalimat berbeda |
| **Adapun** pembuka kalimat (J-TBBBI/TMP-001) | **6** | **RIIL — disunting**: 3.6.3, 3.8.1–3.8.4, 3.8.6 |
| Caption *deployment* tanpa miring (4F/EYD V) | **1** | **RIIL — disunting**: caption Gambar 3.4 |
| Lain-lain (SPE-001 L178, BAK-012 L743, TII-001/003) | 3 | **Positif palsu** — klausa kausal mendahului induk (koma sah); "antarmodul" serangkai; kutipan log |

### B. Telaah manual dimensi ritme (sumber rasa "slop") — riil semua

| Pola | Sebelum (badan naskah) | Sesudah | Tindakan |
|---|---|---|---|
| `tersebut` (deiksis demonstratif) | 63 | **46** | ±20 lokasi → "itu/ini", nomina diulang, atau dirstrukturisasi; yang menunjuk anteseden jauh dipertahankan demi koreferensi (AJ-1) |
| `sehingga` (rantai kausal) | 69 | **55** | 14 rantai kausal longgar → titik koma, "karena itu", "yang membuat", "dengan begitu", "dan karenanya"; kausal kuat dipertahankan |
| `yaitu` (appositive) | 63 | **53** | 9 appositive non-enumeratif → koma / titik dua / tanda kurung; *yaitu* enumeratif pemerinci tuntas (Mustakim AI-4) dipertahankan karena sahih |
| `Adapun` pembuka | 6 | **0** | Dihapus semua (J-TBBBI) |
| Template anfora "Kondisi tersebut + verba", "X tersebut menjadi dasar/titik Y", "Berdasarkan X tersebut", "X tersebut menegaskan" | 9 | **0** | Dipecah: "Artinya,", "Keterbatasan itulah yang…", "Angka itu mendasari…", signposting dibuang |
| Kausal bersarang `karena…sehingga` (N-1) | 3 | **0** | Dibongkar jadi klausa sejajar; modalitas dijaga (*dapat bocor* → *berpotensi membocorkan*) |

Konektor transisi antarkalimat dicek: *Dengan demikian* 4×, *Meskipun demikian* 3×, *Oleh karena itu* 3×, *Selain itu* 2×, *Selanjutnya* 1× pada ~91 halaman — jauh di bawah ambang "maksimal satu per halaman" (4A), masing-masing ditelaah dan premisnya memadai. Retorika formulaik (bukan berarti, menyelami, merajut, lanskap, Di era digital) — nihil.

## 3. Integritas Ilmiah (Aturan Wajib SKILL.md §Aturan Integritas)

- **Angka & data:** seluruh 94 sitasi unik [1]–[94] utuh; 30 bilangan kunci (90–95%, 77,7%, 1,9%, 14,9%, 5,6%, 91%, 500 orang, 1,92 juta, 3.840, Rp150.000, Rp350.000, 96,4%, 99,54%, 0,2 ms, 2.300→54 ms, 69,2 ms, 82 juta, 100–300 MB, mAP50 0,8944/0,9580, 97,6%, 240 MHz, 512 KB, 8 MB, 12,5 cm, 120 Hz, 50 bingkai, dll.) terverifikasi tidak berubah.
- **Derajat modalitas:** tidak ada harapan yang dinaikkan menjadi hasil; satu penyesuaian setara (*dapat bocor* → *berpotensi membocorkan*, keduanya probabilitas).
- **Struktur:** 4 BAB, 30 subbab, 14 tabel, 10 gambar (G3.1–3.10) — identik. DOCX 91 hlm, PDF 91 hlm, 0 placeholder liar. Verifikasi python-docx + pypdf + frasa (baru masuk, lama hilang) lulus semua.

## 4. Poin Konfirmasi Penulis

1. **BRN-002 (judul bab generik):** Kaidah BRIN melarang subbab bertitel "Kajian Pustaka/Metode Penelitian" pada monograf buku. Untuk skripsi, format BAB I–III ini mengikuti pedoman kampus. Bila pedoman pembimbing mengizinkan judul subbab substantif (mis. "2.3 Fisika Wi-Fi CSI dan Model CSI-Ratio"), ini dapat dipertimbangkan pada revisi berikut — **menunggu keputusan pemilik penelitian**.
2. **"antara SIBI dan teks atau ujaran":** Frasa ini dipertahankan karena menempel pada judul resmi penelitian (tercantum pada tabel verifikasi judul). Bila dianggap taksa saat dibaca cepat, alternatif "antara SIBI dan teks/ujaran" dapat menggantikannya serentak di judul dan badan — menunggu persetujuan.
3. **Kepadatan sisa:** *tersebut* 46, *yaitu* 53, *sehingga* 55 masih berada di atas naskah tulis tangan alami karena sifat naskah teknis-argumentatif; penipisan lebih agresif berisiko merusak keajegan istilah (S.3) dan koreferensi (AJ.1). Gelombang berikutnya disarankan menyasar variasi panjang kalimat (KRF-003) pada subbab terpanjang (2.5, 3.7.4, 3.8) bila pembimbing masih menilai ritme kaku.

## 5. Berkas Terkait

- Naskah master tersunting: `Proposal-SenseSIBI-v10.md` (log gelombang 8 tercantum di bagian akhir)
- DOCX di-build ulang: `Proposal-SenseSIBI-Studi-Kelayakan-v10.docx` (91 hlm)
- PDF di-build ulang: `Proposal-SenseSIBI-Studi-Kelayakan-v10.pdf` (91 hlm)
- Keluaran audit: `scripts/sensesibi-v10/audit_humanizer_gel8.txt` (pra-) dan `audit_humanizer_gel8_post.txt` (pasca-)
- Pemindai ritme: `scripts/sensesibi-v10/scan_slop_gel8.py`
