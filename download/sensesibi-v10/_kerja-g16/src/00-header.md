# STUDI KELAYAKAN PURWARUPA SenseSIBI: SISTEM PENERJEMAHAN DUA ARAH HURUF SIBI BERBASIS WI-FI CSI DENGAN INFERENSI ESP32-S3 DAN CLOUD PROCESSING

**PROPOSAL PENELITIAN**

| Identitas | Keterangan |
|---|---|
| Judul | STUDI KELAYAKAN PURWARUPA SenseSIBI: SISTEM PENERJEMAHAN DUA ARAH HURUF SIBI BERBASIS WI-FI CSI DENGAN INFERENSI ESP32-S3 DAN CLOUD PROCESSING |
| Jenis dokumen | Proposal penelitian (seminar proposal), BAB I sampai III + Daftar Pustaka — revisi additif: ruang lingkup sistem dua arah dipertahankan, blok model jalur isyarat menjadi teks diperbarui menjadi encoder CSI terpralatih dengan dua kepala tugas, ±30-an halaman |
| Disusun oleh | [PERLU DATA: nama penulis] |
| NIM | [PERLU DATA: NIM penulis] |
| Program studi | [PERLU DATA: program studi] |
| Universitas | [PERLU DATA: nama universitas] |
| Pembimbing | [PERLU DATA: nama pembimbing, jika sudah ditentukan] |
| Tahun | [PERLU DATA: tahun penyusunan] |

> Catatan penyusunan: versi ini menyunting naskah v15 sebagai revisi additif atas arah pemilik. Ruang lingkup sistem tidak berubah: purwarupa penerjemah dua arah huruf SIBI dengan inferensi ESP32-S3 dan pemrosesan awan tetap menjadi objek, demikian pula mesin ucapan, pengenalan ucapan, kamus representasi, server dan cadangannya, gerbang keputusan, serta seluruh uji kelayakan. Yang berubah hanya blok model pada jalur isyarat menjadi teks: uraian lama berupa *backbone* WiFi-DensePose berkepala tunggal 1D-CNN diganti menjadi *encoder* CSI terpralatih RuView yang dibekukan dengan dua kepala tugas, yaitu kepala klasifikasi 26 huruf dan kepala regresi 21 *keypoint* tangan, dilatih di bawah supervisi guru visual YOLO26m-Pose. Persamaan bernomor bertambah dari 18 menjadi 29 (pemetaan *encoder*, LoRA, kedua kepala, kerugian gabungan, dataset berpasangan, MPJPE dan PCK, kuantisasi affine, anggaran latensi, ketahanan baterai, biaya total); gambar menjadi tujuh dengan satu gambar baru berupa diagram blok model dua kepala (Gambar 2.2) dan tiga diagram yang digambar ulang; tabel menjadi dua belas dengan dua tabel baru berupa pembedaan tiga model ekosistem RuView dan baris justifikasi dua kepala. Daftar pustaka menjadi 28 entri: tujuh rujukan primer baru masuk (kartu model *encoder*, kartu model pose MM-Fi, dataset MM-Fi, MediaPipe Hands, LoRA, Smooth L1, multitask learning) menggantikan rujukan SVM yang keluar bersama pembanding lamanya. Penanda [PERLU DATA] kini ditemani penanda baru [PERLU VALIDASI] untuk hal yang baru dapat ditetapkan setelah audit *checkpoint* atau pembakuan koordinat. Konteks Jawa Timur tanpa mitra lembaga dipertahankan; istilah asing tetap ditulis asing (*checkpoint*, *embedding*, *deployment*).

---
