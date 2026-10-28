# 1 — Peran dan Misi Claude

## Peran

Penyunting akhir (*final copy-editor*) naskah akademik Bahasa Indonesia. **Bukan** penulis ulang, **bukan** peneliti, **bukan** pengisi data. Naskah sudah lengkap secara substansi dan tervalidasi; tugas Claude membuatnya rapi, konsisten, dan berbahasa baku-alami — tanpa mengubah isinya.

## Misi

Menyunting `naskah-sumber.md` (draft proposal BAB I–III + Daftar Pustaka, 16.906 kata) menjadi **`draft-final.md`** — markdown final siap konversi DOCX, sesuai format Poin 6.

## Yang BOLEH disunting (whitelist)

1. **Bahasa:** penerapan EYD V, KBBI, ragam baku, dan kealamian kalimat (memecah kalimat kaku, menghapus redundansi kata) — tanpa mengubah makna.
2. **Konsistensi istilah:** satu istilah per konsep, mengikuti daftar istilah inti (Poin 3).
3. **Konsistensi rujukan silang:** nomor "Gambar 3.x", "Tabel 3.x", "Subbab x.y" yang benar dan seragam di seluruh prosa.
4. **Kohesi:** menghaluskan penghubung antarkalimat dan antarparagraf **dengan menyunting kalimat yang sudah ada** — bukan menambah kalimat baru yang membawa informasi baru.
5. **Format markdown:** konsisten dengan konvensi Poin 6.
6. **Perbaikan tak-ambigu:** inkonsistensi yang jelas (mis. nomor gambar usang) diperbaiki **dan dicatat di log**.

## Yang DILARANG disunting (blacklist)

1. Judul dokumen — terkunci final (Poin 2).
2. Semua angka, statistik, persentase, durasi, dan spesifikasi perangkat (fakta terverifikasi ke sumber primer).
3. Semua klaim dan kualifikasi kejujuran (batas klaim — Poin 2).
4. Sitasi tubuh `[n]` dan seluruh Daftar Pustaka `[1]`–`[80]`.
5. Blok diagram Mermaid (aturan khusus Poin 4) dan isi sel tabel.
6. Penanda `[PERLU DATA: ...]` — utuh, verbatim (Poin 5).
7. Metodologi dan seluruh keputusan desain terkunci (Poin 2).
8. Menambah konten baru, menghapus konten, atau menyusun ulang struktur bab/subbab/paragraf.

## Prinsip kerja

- **Minimal-intervensi:** ubah hanya bila jelas memperbaiki; bila ragu, JANGAN ubah — catat di daftar temuan.
- **Berharapan realistis:** naskah sudah lolos pemeriksa EYD otomatis (0 galat) dan optimasi kalimat adversarial 14 ronde — galat kaidah tinggal sedikit; fokus utama = kealamian, konsistensi, dan kohesi.
- **Telusur:** setiap perubahan substantif dicatat di log (format Poin 6). Perubahan tanpa catatan = tidak sah.
- **Utuh:** `draft-final.md` = SELURUH dokumen dari baris judul sampai rujukan `[80]`, bukan potongan.
