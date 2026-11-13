# PENGEMBANGAN HEAD KLASIFIKASI DAN REGRESI PADA ENCODER WI-FI CSI PRETRAINED UNTUK PENGENALAN ISYARAT SIBI

**PROPOSAL PENELITIAN**

| Identitas | Keterangan |
|---|---|
| Judul | PENGEMBANGAN HEAD KLASIFIKASI DAN REGRESI PADA ENCODER WI-FI CSI PRETRAINED UNTUK PENGENALAN ISYARAT SIBI |
| Jenis dokumen | Proposal penelitian (seminar proposal), BAB I sampai III + Daftar Pustaka — arah penelitian dirumuskan ulang dari purwarupa penerjemah dua arah menjadi pengembangan dua kepala tugas di atas encoder Wi-Fi CSI terpralatih, ±30 halaman |
| Disusun oleh | [PERLU DATA: nama penulis] |
| NIM | [PERLU DATA: NIM penulis] |
| Program studi | [PERLU DATA: program studi] |
| Universitas | [PERLU DATA: nama universitas] |
| Pembimbing | [PERLU DATA: nama pembimbing, jika sudah ditentukan] |
| Tahun | [PERLU DATA: tahun penyusunan] |

> Catatan penyusunan: versi ini merumuskan ulang arah penelitian menjadi pengembangan dua kepala tugas (*head*) di atas *encoder* Wi-Fi CSI terpralatih. Kepala klasifikasi mengenali 26 huruf alfabet manual SIBI, sedangkan kepala regresi memprediksi 21 koordinat *keypoint* tangan dari *embedding* yang sama; guru visual YOLO26m-Pose hanya bekerja pada tahap akuisisi data sebagai pemberi label, bukan bagian produk akhir. Dua puluh lima persamaan bernomor disusun beserta definisi lambang dan contoh perhitungan, mulai dari koefisien kanal, zona Fresnel, Doppler, kaidah Nyquist, dan CSI-ratio, sampai pemetaan encoder, LoRA, kedua kepala tugas, kerugian gabungan, dataset berpasangan, Delta-CSI, metrik klasifikasi dan regresi, kuantisasi affine, serta anggaran latensi. Sembilan tabel dan lima gambar menyertainya; arsitektur model dua kepala menjadi gambar inti baru pada Gambar 2.2, sedangkan diagram tahapan dan inferensi tepi digambar ulang mengikuti tujuh tahap metodologi yang baru. Daftar pustaka tetap 22 entri: tujuh rujukan baru yang terverifikasi masuk (kartu model encoder, kartu model pose MM-Fi, dataset MM-Fi, MediaPipe Hands, LoRA, Smooth L1, multitask learning) menggantikan tujuh rujukan yang keluar bersama arah penelitian lamanya (SVM, Chow, Kokoro, MMS-TTS, Whisper, TRL, Likert). Konteks Jawa Timur tanpa mitra lembaga dipertahankan; penanda [PERLU DATA] kini ditemani penanda baru [PERLU VALIDASI] untuk hal yang baru dapat ditetapkan setelah audit model atau audit data; istilah asing tetap ditulis asing (*checkpoint*, *embedding*, *deployment*).

---
