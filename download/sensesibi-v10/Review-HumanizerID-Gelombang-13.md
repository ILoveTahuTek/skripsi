# Review Gelombang 13 — Humanizer Indonesia + Penghapusan Mitra

**Tanggal:** 12 November 2026 · **Pemicu:** permintaan pemilik memakai skill https://github.com/adhiprib/humanizer-indonesia.git (v1.7, register akademik) atas naskah v12, sekaligus pernyataan pemilik bahwa penelitian **tidak bersama mitra** · **Jenis pekerjaan:** suntingan gaya bertarget + revisi isi kemitraan, tanpa mengubah data, sitasi, dan struktur.

## 1. Lingkup dan metode

1. Skill diunduh ke `/tmp/humanizer-indonesia` (SKILL.md + references/id-ai-tells.md + scripts/metrik.py v1.4) dan seluruh alurnya dijalankan: ukur (Langkah 2), baca katalog (Langkah 3), draf bertarget (5), uji kalke/diksi (5b), uji personifikasi/pembuka (5c), audit (6), revisi akhir (7), serah (8).
2. **Kalibrasi suara tidak dilakukan** karena tidak ada contoh tulisan pemilik; sesuai aturan skill, dipakai suara netral register akademik dan hal ini dinyatakan terbuka.
3. Pengukuran memakai `scripts/metrik.py --preset akademik` bawaan skill atas tubuh naskah (BAB I–III, tanpa tabel/daftar/DP yang memang dikecualikan skrip).
4. Pekerjaan pada salinan `Proposal-SenseSIBI-v13.md`; pipeline build g13 diturunkan dari g12 sehingga tata letak DOCX/PDF identik dengan gelombang sebelumnya.

## 2. Penghapusan klaim kemitraan (permintaan pemilik)

Lima titik disunting; dua penanda `[PERLU DATA: nama SLB atau lembaga mitra...]` dihapus dari naskah (sisa penanda PERLU DATA 32 menjadi 30):

| Lokasi | Sebelum | Sesudah |
|---|---|---|
| 1.1 akhir paragraf 2 | "bekerja sama dengan sekolah mitra di Jawa Timur [PERLU DATA...]" | "Seluruh pelaksanaannya direncanakan di Jawa Timur tanpa mengikat kerja sama dengan lembaga tertentu." |
| Batasan butir 7 | "dua ruang mitra di Jawa Timur" | "dua ruang berbeda di Jawa Timur" |
| 1.5.2 manfaat praktis | "Bagi sekolah mitra," | "Bagi sekolah yang kelak memakainya," |
| 3.3 waktu dan lokasi | "bekerja sama dengan [PERLU DATA: nama SLB mitra]" | "tidak bersandar pada mitra lembaga; partisipan direkrut langsung oleh peneliti ... di sedikitnya dua ruang berbeda, misalnya ruang kelas dan ruang kerja" |
| 3.6 etika | "persetujuan lembaga mitra dan persetujuan tertulis ... [PERLU DATA]" | "persetujuan etik dari [PERLU DATA: lembaga atau komisi pemberi persetujuan etik] serta persetujuan tertulis" |

Konsistensi ikutan: protokol partisipan (3.6) memang tidak pernah menyebut jalur rekrutmen lewat sekolah sehingga tidak perlu diubah; satu-satunya sebutan "mitra" yang tersisa adalah kalimat penegas "tidak bersandar pada mitra lembaga" itu sendiri.

## 3. Metrik sebelum vs sesudah (preset akademik)

| Metrik | v12 | v13 | Status |
|---|---|---|---|
| Rerata panjang kalimat | 20,5 (PERIKSA) | **19,1** | LULUS (target 14–20) |
| Simpangan baku | 9,8 | **7,9** | LULUS (min 6,4) |
| Kalimat ≥28 kata | 20,6% (PERIKSA) | **13,9%** | LULUS (maks 20%) |
| Em/en dash di prosa | 8 (PERIKSA) | **0** | LULUS |
| Verba ringan per 100 kata | 0,04 (2 temuan) | **0,00** | LULUS |
| Penyangkalan antisipatif | 1 | **0** | LULUS (sasaran 0) |
| Konjungsi "bila" | 18 | **0** | LULUS (ganti "jika") |
| Konektor per 100 kata | 0,02 | 0,04 | LULUS (maks 0,4) |
| Kalimat dibuka konektor | 0,0% | 0,3% | jauh di bawah kebiasaan |
| Jumlah kalimat prosa / kata | 272 / 5.588 | 295 / 5.639 | +51 kata dari pemecahan kalimat |

Diagnostik tanpa ambang, dilaporkan apa adanya: **kepadatan pemadat 43,1 → 44,9** per 1.000 kata (pita korpus penulis skill 73–139; naskah memang dipadatkan demi batas ±40 halaman; skill melarang menambah kata isian demi angka, jadi tidak dipaksakan); **triplet 52 → 46** (sisanya daftar isi nyata: komponen, angka, sitasi, tahap prosedur — kategori D3/F9 yang tidak boleh dibuang); **kalimat pendek lepas 21 → 11** (sisa: butir prosedur paralel, artefak diagram, dan kalimat berpartikel *pun/sendirinya* yang menurut pengukuran skill justru terbaca manusiawi); deret pembuka S terpanjang 10 → 9 (berada di blok daftar bernomor yang memang sejajar).

## 4. Keputusan diksi (wewenang pemilik, mohon ditinjau)

| Keputusan | Sebelum | Sesudah | Alasan (katalog) |
|---|---|---|---|
| Bentuk terikat | "purna Rust" (3x, termasuk 2 tabel) | "seluruhnya dalam Rust" / "Seluruhnya Rust" | kaidah bentuk terikat + kata "purna" tidak hidup di bidang ini |
| Verba ringan | "menjalankan penangkapan CSI / pendengar UDP / konkurensi" | "menangkap CSI sambil memelihara koneksi...", "pendengar UDP berjalan di atas Tokio", "konkurensi ditangani Tokio" | A1 verba kerja menggantikan konstruksi ringan |
| Konjungsi syarat | "bila" (18x) | "jika" | kaidah register akademik skill (7 Nov 2026) |
| Tanda pisah majemuk kata | "guru–murid", "kamera–CSI", "label–teks" (en dash) | "guru-murid", "kamera-CSI", "label-teks" (tanda hubung) | nol en dash kata-ke-kata; EYD V |
| Rentang alfanumerik di prosa | "G0–G4", "M1–M14", "T0–T2", "T3–T5" | "G0 sampai G4", dst. | en dash hanya untuk rentang angka di spesifikasi; di tabel/takarir tetap en dash |
| Penyangkalan antisipatif | "Kebaruan penelitian ini jadi bukan pada pengenalan kontinu, melainkan pada..." | "Kebaruan penelitian ini ada pada penerapan CSI untuk alfabet SIBI serta..." | D7 nyatakan positif |
| Kalimat pendek berpartikel | "Angkanya timpang." | "Angkanya memang timpang." | 2.15: partikel membuat kalimat pendek terbaca manusiawi |
| Pembuka paragraf | "Sinyal Wi-Fi membuka jalan lain tanpa kamera." | "Untuk menghindari dua kendala itu, sinyal Wi-Fi membuka jalan lain tanpa kamera." | kohesi antarparagraf + variasi pembuka (SSS-run dipecah) |

## 5. Integritas (diverifikasi skrip)

- **Sitasi:** 161 kemunculan `[n]` dengan urutan kemunculan identik dengan v12; penomoran 1–46 dan isi Daftar Pustaka tidak bergeser.
- **Angka:** seluruh token angka tubuh naskah identik; satu-satunya selisih berasal dari rombakan "Catatan penyusunan" sampul (v11→v12, v2→v1.7) yang memang mendeskripsikan gelombang baru.
- **Struktur:** 39 heading (judul 3.7 kini "Guru-Murid" dengan tanda hubung), 12 tabel, 3 gambar beserta blok mermaid, struktur G0–G4, jadwal M1–M14, keenam prosedur, batasan 9 butir, cermin rumusan-tujuan 3:3.
- **Dokumen:** DOCX 4 H1 + 28 H2 + 8 H3, 12 tabel, 3 gambar, nol paragraf ganda, nol sel header kosong, nol `**`, nol placeholder bocor (XXX/TODO/NaN); PDF **37 halaman** (v12: 37), nol halaman kosong (rasio tinta terendah 1,5%), DP ditutup [46] di halaman 37.

## 6. Poin konfirmasi untuk pemilik

1. Contoh dua ruang uji pada 3.3 ("misalnya ruang kelas dan ruang kerja") adalah ilustrasi pilihan, bukan komitmen; silakan ganti dengan ruang yang memang akan dipakai.
2. Penegas "tanpa mengikat kerja sama dengan lembaga tertentu" (1.1) dan "tidak bersandar pada mitra lembaga" (3.3) dipakai agar penguji tidak menanyakan surat kemitraan; bila dosen pembimbing menilai kalimat ini tidak perlu, keduanya dapat dihapus tanpa mengganggu alur.
3. Jalur "Update Field" pada daftar isi tetap diperlukan setelah menyunting di Word/WPS.
4. Kepadatan pemadat sengaja tidak dikejar sampai pita 73–139 demi batas halaman; bila dosen menghendaki prosa lebih longgar, komprominya adalah +2–3 halaman.
