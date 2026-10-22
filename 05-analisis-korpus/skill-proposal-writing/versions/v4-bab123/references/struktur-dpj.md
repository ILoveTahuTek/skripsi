# Struktur kanonik DPJ (korpus TRSE UNM)

Sumber pola: 12 dokumen korpus (8 naskah/proposal dianalisis menyeluruh; 8/8 konsisten). **Ruang lingkup PROPOSAL (DPJ) = hanya BAB I–III + DAFTAR PUSTAKA** — proposal berbeda dari skripsi penuh (5 bab): tidak ada BAB IV dst. sebagai bab terpisah; konten rencana (jadwal, biaya, risiko) dikonsolidasikan menjadi subbab BAB III, dan pernyataan disiplin klaim disisipkan di 1.4. Tanpa halaman sampul, tanpa lembar pengesahan, tanpa kata pengantar, tanpa abstrak.

## Urutan isi DPJ

1. **Judul dokumen** (kapital semua, terpusat, pola `RANCANG BANGUN / IMPLEMENTASI / PERANCANGAN / SISTEM … BERBASIS … PADA/UNTUK …: STUDI KELAYAKAN …`), diikuti `Judul Alternatif 1/2` bila diminta.
2. **BAB I PENDAHULUAN** — subbab wajib berurutan:
   - `1.1 Latar Belakang` (corong 4 lapis — lihat bahasa-korpus.md) + tabel usulan judul utama dan alternatif
   - `1.2 Rumusan Masalah` (2–4 pertanyaan "Bagaimana …?")
   - `1.3 Tujuan Penelitian` (mirror rumusan, frasa kerja)
   - `1.4 Batasan Masalah` (bernomor; item terakhir "Penelitian ini tidak membahas …"; diakhiri paragraf pernyataan disiplin klaim — lihat disiplin-klaim.md)
   - `1.5 Manfaat Penelitian` (1.5.1 Teoretis; 1.5.2 Praktis dengan sub-item Bagi …)
3. **BAB II KAJIAN PUSTAKA** (atau TINJAUAN PUSTAKA — pilih satu, konsisten):
   - 2.1…2.n satu subbab per teknologi/konsep, urut sistem → komponen (8–13 subbab)
   - subbab terakhir `2.n Penelitian Terdahulu` — WAJIB ada tabel komparasi:
     kolom = peneliti+tahun (dengan judul singkat), kolom fitur/teknologi;
     isi = tanda `√` / `−`; baris terakhir = `Penelitian Ini`;
     setelah tabel: prosa gap + daftar bernomor "mengisi celah".
4. **BAB III METODE PENELITIAN** (atau METODOLOGI PENELITIAN) — bab terakhir; seluruh rencana dikonsolidasikan di sini sebagai subbab:
   - `3.1 Alur Penelitian` / `Tahapan Penelitian` — narasi tahapan korpus ("Tahap pertama adalah studi literatur … Tahap terakhir adalah pengujian dan evaluasi")
   - `3.2 Studi Literatur` — sumber literatur + cara verifikasi DOI
   - 3.3… perancangan (arsitektur sistem, perangkat keras, perangkat lunak/dataset, lokasi/partisipan/etika)
   - `3.n Rencana Pengujian` — satu subbab per kelompok fitur yang diuji (rencana pengujian + metrik)
   - `3.n+1 Evaluasi` — kriteria keberhasilan + keputusan gerbang go/no-go
   - `3.n+2 Rencana Kegiatan dan Jadwal Penelitian` (khas DPJ) — **tabel jadwal 1 semester (±4,5 bulan)**: baris kegiatan, kolom minggu; **gerbang go/no-go** (uji fisik awal) ditandai eksplisit
   - `3.n+3 Rencana Biaya Penelitian` (khas DPJ) — tabel komponen biaya (perangkat, bahan, operasional) + estimasi total (Rupiah)
   - `3.n+4 Analisis Risiko dan Rencana Cadangan` (khas DPJ) — risiko utama + mitigasi + fallback per risiko
5. **DAFTAR PUSTAKA** — APA 7, hanging indent, DOI URL.

> Yang wajib: jadwal, biaya, risiko, dan batasan klaim masing-masing punya tempat jelas — sebagai subbab BAB III / paragraf 1.4, bukan bab terpisah. Bila nanti dikembangkan menjadi naskah skripsi penuh, konten subbab rencana inilah yang diolah dan bab IV+ baru ditambahkan.

## Templat tabel wajib

**Tabel Penelitian Terdahulu** (BAB II):

```
Tabel 2.1 Perbandingan Penelitian Terdahulu
| Peneliti (Tahun) & Judul | Fitur A | Fitur B | Fitur C | Fitur D |
|--------------------------|---------|---------|---------|---------|
| Sidehabi et al. (2023) … |    √    |    √    |    −    |    √    |
| Hamdani et al. (2022) …  |    √    |    −    |    √    |    −    |
| Penelitian Ini           |    √    |    √    |    √    |    √    |
```

**Tabel Jadwal** (BAB III, subbab Rencana Kegiatan dan Jadwal): baris = kegiatan/periode, kolom = aktivitas + keluaran; isi = blok aktif.

**Tabel Biaya** (BAB III, subbab Rencana Biaya Penelitian): kolom = Komponen | Spesifikasi | Jumlah | Estimasi Biaya (Rp).

## Mekanika dokumen

- Penomoran tabel/gambar per bab: `Tabel 2.1`, `Gambar 3.1` + judul.
- Paragraf 3–8 kalimat; setiap bullet/tabel didahului kalimat pengantar.
- Angka desimal pakai koma (`0,9967`), persen tanpa spasi (`99%`).
- Istilah asing Latin: computer vision, real-time, embedded system, hardware/software.
- Footer halaman `- N -`; tanpa page break di tengah isi (hanya setelah judul/daftar isi bila ada).
