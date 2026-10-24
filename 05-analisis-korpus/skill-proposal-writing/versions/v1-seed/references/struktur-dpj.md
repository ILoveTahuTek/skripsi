# Struktur kanonik DPJ (korpus TRSE UNM)

Sumber pola: 12 dokumen korpus (8 naskah/proposal dianalisis menyeluruh; 8/8 konsisten). Untuk DPJ (tahap pengajuan judul): bab inti I–III + bab rencana; tanpa halaman sampul, tanpa lembar pengesahan, tanpa kata pengantar, tanpa abstrak (semua itu milik naskah selesai).

## Urutan isi DPJ

1. **Judul dokumen** (kapital semua, terpusat, pola `RANCANG BANGUN / IMPLEMENTASI / PERANCANGAN / SISTEM … BERBASIS … PADA/UNTUK …: STUDI KELAYAKAN …`), diikuti `Judul Alternatif 1/2` bila diminta.
2. **BAB I PENDAHULUAN** — subbab wajib berurutan:
   - `1.1 Latar Belakang` (corong 4 lapis — lihat bahasa-korpus.md)
   - `1.2 Rumusan Masalah` (2–4 pertanyaan "Bagaimana …?")
   - `1.3 Tujuan Penelitian` (mirror rumusan, frasa kerja)
   - `1.4 Batasan Masalah` (bernomor; item terakhir "Penelitian ini tidak membahas …")
   - `1.5 Manfaat Penelitian` (1.5.1 Teoretis; 1.5.2 Praktis dengan sub-item Bagi …)
3. **BAB II KAJIAN PUSTAKA** (atau TINJAUAN PUSTAKA — pilih satu, konsisten):
   - 2.1…2.n satu subbab per teknologi/konsep, urut sistem → komponen (8–13 subbab)
   - subbab terakhir `2.n Penelitian Terdahulu` — WAJIB ada tabel komparasi:
     kolom = peneliti+tahun (dengan judul singkat), kolom fitur/teknologi;
     isi = tanda `√` / `−`; baris terakhir = `Penelitian Ini`;
     setelah tabel: prosa gap + daftar bernomor "mengisi celah".
4. **BAB III METODE PENELITIAN** (atau METODOLOGI PENELITIAN):
   - `3.1 Alur Penelitian` / `Tahapan Penelitian` — narasi tahapan + (di naskah: diagram alir; di DPJ: deskripsi teks tahapan)
   - `3.2 Studi Literatur`
   - 3.3… perancangan (arsitektur sistem, perangkat keras, perangkat lunak/dataset)
   - `3.n Pengujian` — satu sub-bab per fitur yang diuji (rencana pengujian + metrik)
   - `3.n+1 Evaluasi` — kriteria keberhasilan
5. **BAB IV RENCANA KEGIATAN DAN JADWAL PENELITIAN** (khas DPJ — tidak ada di korpus naskah):
   - rencana kegiatan per tahap + **tabel jadwal 1 semester (±4,5 bulan)**: baris kegiatan, kolom minggu/bulan
   - **gerbang go/no-go** (uji fisik awal) ditandai eksplisit di jadwal
6. **BAB V RENCANA BIAYA** (khas DPJ): tabel komponen biaya (perangkat, bahan, operasional) + estimasi total (Rupiah).
7. **BAB VI ANALISIS RISIKO DAN RENCANA CADANGAN** (khas DPJ): risiko utama + mitigasi + fallback per risiko.
8. **BAB VII BATASAN DAN DISIPLIN KLAIM** (khas DPJ, garis WiFi-CSI): apa yang TIDAK diklaim + pernyataan studi kelayakan.
9. **DAFTAR PUSTAKA** — APA 7, hanging indent, DOI URL.

> Variasi jumlah bab rencana diperbolehkan (gabung jadwal+biaya satu bab bila lebih ringkas); yang wajib: jadwal, biaya, risiko, batasan klaim masing-masing punya tempat jelas.

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

**Tabel Jadwal** (BAB IV): baris = kegiatan, kolom = minggu ke-1…18; isi = blok aktif.

**Tabel Biaya** (BAB V): kolom = Komponen | Spesifikasi | Jumlah | Estimasi Biaya (Rp).

## Mekanika dokumen

- Penomoran tabel/gambar per bab: `Tabel 2.1`, `Gambar 3.1` + judul.
- Paragraf 3–8 kalimat; setiap bullet/tabel didahului kalimat pengantar.
- Angka desimal pakai koma (`0,9967`), persen tanpa spasi (`99%`).
- Istilah asing Latin: computer vision, real-time, embedded system, hardware/software.
- Footer halaman `- N -`; tanpa page break di tengah isi (hanya setelah judul/daftar isi bila ada).
