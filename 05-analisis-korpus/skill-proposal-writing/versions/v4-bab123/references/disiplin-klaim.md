# Disiplin klaim WiFi-CSI / RuView (wajib di setiap DPJ garis ini)

Sumber: eksplorasi deep RuView (01-ruview-exploration/), verifikasi kode
mandiri, gap-analisis literatur (06-referensi-isyarat/). Tujuan: dokumen tidak
pernah menjanjikan yang belum terbukti — pembimbing menguji klaim, bukan harapan.

## 1. Aturan inti

1. **Semua klaim dibatasi studi kelayakan.** Framing: "menguji kelayakan",
   "mengevaluasi kemampuan", "menghasilkan dataset dan rekomendasi" — bukan
   "membangun sistem jadi yang …".
2. **Pose 17-keypoint RuView = stub (PCK@20 ≈ 3%).** DILARANG menulis
   "ekstraksi pose/kerangka tangan". Paradigma yang benar: **klasifikasi gestur
   langsung dari pola CSI** (preseden: SignFi 2018; DF-WiSLR 2020; Widar3.0
   2021; FSL-CSI TENCON 2024).
3. **Gerbang fisik Delta-CSI 2×ESP32 = go/no-go minggu awal.** Setiap jadwal
   wajib menempatkan uji fisik dua node ESP32 di lokasi target sebagai titik
   keputusan lanjut/berhenti/ganti topik.
4. **Risiko + mitigasi eksplisit** per risiko utama (cross-domain, dataset,
   lingkungan, etika) di bab risiko.

## 2. Batas klaim per kasus

| Kasus | Boleh diklaim | Tidak boleh diklaim |
|---|---|---|
| Kandang broiler | indeks aktivitas kawanan (studi kelayakan), dataset publik, alert perubahan | identifikasi individu ayam, diagnosis penyakit, jantung ayam (band kode 2× di luar) |
| Kelas SLB | presence/motion kelas, deteksi anomali/jatuh (threshold disetel), privasi-preserving | person count akurat >2–3, identitas individu, penilaian perilaku klinis |
| Asrama SLB | pola tidur kasar, peringatan anomali malam untuk pendamping | hipnogram klinis, apnea screening (eksperimental RuView), multi penghuni |
| Isyarat SIBI/BISINDO | klasifikasi gestur terisolasi 5–12 kelas dominan-gerak-lengan, dataset CSI isyarat pertama SIBI/BISINDO | penerjemah kontinu, ekstraksi pose tangan, multi-penandatangan, generalisasi lintas-ruang tanpa kalibrasi |

## 3. Kalimat pernyataan disiplin (templat, sisipkan di batasan/klaim)

> Penelitian ini merupakan studi kelayakan [kasus] berbasis Wi-Fi Channel State
> Information pada platform RuView (capture, DSP, alert). Penelitian ini tidak
> mengklaim [daftar hal yang tidak diklaim]. Kelayakan diuji pada [lingkup
> terbatas], dengan [asumsi keras]. Uji fisik Delta-CSI 2×ESP32 pada lokasi
> target menjadi titik go/no-go penelitian.

## 4. Etika (wajib bila melibatkan manusia, terutama anak)

- Persetujuan orang tua/wali + institusi + hak menarik diri, dinyatakan di batasan.
- Posisi sistem: deteksi kondisi untuk pendamping, BUKAN pengawasan perilaku.
- Kamera hanya untuk pelabelan ground truth saat rekam dataset; runtime bebas kamera.
- WiFi tidak mengidentifikasi individu (gap 0,0005) — pakai sebagai bukti desain privasi.

## 5. Kebaruan yang boleh diklaim (dari gap-analisis terverifikasi)

- Kombinasi: bahasa target + platform + konteks (mis. "pertama pada SIBI/BISINDO via CSI", "pertama unggas") — selalu berbentuk **kombinasi**, bukan "pertama menemukan X secara umum".
- Kontribusi dataset publik berlabel.
- Kalibrasi parameter sensing untuk populasi baru (anak, kawanan kecil).

## 6. Ketika menulis tentang RuView

Sebut sebagai "platform open-source capture CSI + DSP + alert berbasis ESP32"
dengan rujukan repo. Fitur nyata (MEASURED) boleh dirujuk; fitur stub
(pose, apnea) hanya boleh disebut sebagai "tidak digunakan / di luar lingkup".
Daftar lengkap: 06-referensi-isyarat/ruview-fitur-isyarat.md.
