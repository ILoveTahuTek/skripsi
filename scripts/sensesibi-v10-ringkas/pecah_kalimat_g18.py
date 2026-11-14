#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gelombang 18 pemecahan kalimat panjang (metrik humanizer: rerata dan persentase
kalimat panjang); rumusan/tujuan no. 1 dibiarkan utuh demi konvensi cermin."""
import sys
from pathlib import Path

V10 = Path("/home/z/my-project/download/sensesibi-v10")
MARK = "<!-- ===== AKHIR NASKAH"
src = (V10 / "Proposal-SenseSIBI-v18.md").read_text(encoding="utf-8")
naskah = src[:src.index(MARK)]
log = src[src.index(MARK):]

E = []
def G(old, new):
    E.append((old, new))

# 3.6 langkah 6
G("lalu mencatat tingkat segmen terbuang dan skor kualitas anotasi tiap segmen; kualitas deteksi *keypoint* pada gerakan dinamis J dan Z dievaluasi khusus (laju deteksi berhasil, *jitter*, bingkai hilang, dan validitas lintasan) karena performa exp11_huruf24 hanya terukur pada 24 pose statis",
  "lalu mencatat tingkat segmen terbuang dan skor kualitas anotasi tiap segmen. Kualitas deteksi *keypoint* pada gerakan dinamis J dan Z dievaluasi khusus (laju deteksi berhasil, *jitter*, bingkai hilang, dan validitas lintasan) karena performa exp11_huruf24 hanya terukur pada 24 pose statis")
# 3.7 segmentasi
G("lalu untuk 24 huruf statis jendela penahanan pose (*pose-hold*) selama durasi observasi tetap untuk klasifikasi statis, sedangkan untuk J dan Z jendela lintasan penuh dari *onset* sampai *offset* gerak;",
  "lalu untuk 24 huruf statis jendela penahanan pose (*pose-hold*) selama durasi observasi tetap untuk klasifikasi statis. Untuk J dan Z digunakan jendela lintasan penuh dari *onset* sampai *offset* gerak;")
# Batasan 5
G("*encoder* dibekukan pada baseline, sedangkan LoRA dan pelatihan lanjutan diperlakukan sebagai eksperimen pembanding; masukan *checkpoint* berupa delapan fitur turunan per jendela satu detik disesuaikan lewat jalur fitur turunan atau adapter masukan yang dipilih pada gerbang G0b",
  "*encoder* dibekukan pada baseline, sedangkan LoRA dan pelatihan lanjutan diperlakukan sebagai eksperimen pembanding. Masukan *checkpoint* berupa delapan fitur turunan per jendela satu detik disesuaikan lewat jalur fitur turunan atau adapter masukan yang dipilih pada gerbang G0b")
# G0b + J-Z dash
G("Alat ujinya *probe* linear di atas *embedding* beku: *probe* 24 huruf statis pada skema blok temporal, *probe* sekuensial atas gabungan langkah tiap segmen, *probe* biner J terhadap Z, serta dua kontrol berupa *probe* pada fitur mentah ringkas dan uji permutasi label pada unit blok repetisi (p_perm < 0,05, skor label asli melampaui distribusi nol permutasi) agar hasilnya tidak menipu. Ambang usulannya: F1 makro sekurang-kurangnya 0,30 dan tiga kali peluang acak, *probe* J–Z sekurang-kurangnya 70%, seluruhnya difinalkan bersama pembimbing sebelum gerbang dinilai.",
  "Alat ujinya *probe* linear di atas *embedding* beku: *probe* 24 huruf statis pada skema blok temporal, *probe* sekuensial atas gabungan langkah tiap segmen, dan *probe* biner J terhadap Z. Dua kontrol menyertainya, yaitu *probe* pada fitur mentah ringkas dan uji permutasi label pada unit blok repetisi (p_perm < 0,05, skor label asli melampaui distribusi nol permutasi), agar hasilnya tidak menipu. Ambang usulannya: F1 makro sekurang-kurangnya 0,30 dan tiga kali peluang acak, *probe* biner J terhadap Z sekurang-kurangnya 70%, seluruhnya difinalkan bersama pembimbing sebelum gerbang dinilai.")
# 2.7 TTS
G("MMS-TTS-ind, model TTS Indonesia dari Meta [25], karena itu menjadi kandidat utama operasional, dengan Kokoro tercatat untuk verifikasi ulang jika suara Indonesia tersedia pada rilis berikutnya [PERLU KONFIRMASI: keputusan final mesin TTS, Tabel 3.8 #17]; keduanya berjalan di server lokal sebagai jalur utama dan di ponsel melalui ONNX Runtime sebagai cadangan, lalu diuji banding pada G3.",
  "MMS-TTS-ind, model TTS Indonesia dari Meta [25], karena itu menjadi kandidat utama operasional. Kokoro tetap tercatat untuk verifikasi ulang jika suara Indonesia tersedia pada rilis berikutnya [PERLU KONFIRMASI: keputusan final mesin TTS, Tabel 3.8 #17]. Keduanya berjalan di server lokal sebagai jalur utama dan di ponsel melalui ONNX Runtime sebagai cadangan, lalu diuji banding pada G3.")
# 3.1
G("dan kinerja kedua jalur penerjemahan; komponen yang lulus uji dikemas menjadi purwarupa lalu dinilai lewat uji operasional, uji kegunaan skala kecil, dan penilaian validator penutur tunarungu.",
  "dan kinerja kedua jalur penerjemahan. Komponen yang lulus uji dikemas menjadi purwarupa lalu dinilai lewat uji operasional, uji kegunaan skala kecil, dan penilaian validator penutur tunarungu.")
# 3.6 langkah 4
G("dengan sumber penanda waktu tunggal supaya perekaman CSI dan *webcam* berjalan sinkron, lalu memverifikasi ulang kualitas sinkronisasi lewat uji kejadian di awal sesi, misalnya satu ketukan tangan yang terbaca kedua sensor",
  "dengan sumber penanda waktu tunggal supaya perekaman CSI dan *webcam* berjalan sinkron. Kualitas sinkronisasi diverifikasi ulang lewat uji kejadian di awal sesi, misalnya satu ketukan tangan yang terbaca kedua sensor")
# 2.3 model mmfi
G("amplitudo CSI [3, 114, 10] pada 100 Hz diproses *encoder* Transformer menjadi 17 *keypoint* tubuh COCO dengan sekitar 2,3 juta parameter; kinerjanya PCK@20 82,69% (ansambel 83,59%), turun ke 64% lintas subjek *zero-shot* dan 17,5% lintas lingkungan, lalu naik ke 72–78% setelah kalibrasi 50–1.000 bingkai per orang [15].",
  "amplitudo CSI [3, 114, 10] pada 100 Hz diproses *encoder* Transformer menjadi 17 *keypoint* tubuh COCO dengan sekitar 2,3 juta parameter. Kinerjanya PCK@20 82,69% (ansambel 83,59%), turun ke 64% lintas subjek *zero-shot* dan 17,5% lintas lingkungan, lalu naik ke 72–78% setelah kalibrasi 50–1.000 bingkai per orang [15].")
# 2.5 peran guru
G("Untuk 24 huruf statis, label kelas pelatihan diambil dari protokol perekaman dan guru menyumbang deret 21 *keypoint* beserta visibilitasnya; untuk J dan Z, label juga berasal dari protokol, dan guru tidak diposisikan sebagai pengklasifikasi kedua huruf gerak itu kecuali model guru terbukti memuat kelasnya",
  "Untuk 24 huruf statis, label kelas pelatihan diambil dari protokol perekaman dan guru menyumbang deret 21 *keypoint* beserta visibilitasnya. Untuk J dan Z, label juga berasal dari protokol, dan guru tidak diposisikan sebagai pengklasifikasi kedua huruf gerak itu kecuali model guru terbukti memuat kelasnya")
# 2.4 klasifikator
G("Klasifikator himpunan tertutup selalu memilih satu kelas, sehingga keluarannya dilengkapi skor keyakinan dan mekanisme penolakan [18]: keyakinan rendah memunculkan pesan isyarat tidak dikenali alih-alih menebak salah, dan kelayakan operasionalnya dilaporkan lewat *accepted coverage*, akurasi pada segmen diterima (*selective accuracy*), akurasi keseluruhan, serta laju terima-salah dan tolak-salah dengan ambang dari data validasi (Subbab 3.7).",
  "Klasifikator himpunan tertutup selalu memilih satu kelas, sehingga keluarannya dilengkapi skor keyakinan dan mekanisme penolakan [18]: keyakinan rendah memunculkan pesan isyarat tidak dikenali alih-alih menebak salah. Kelayakan operasionalnya dilaporkan lewat *accepted coverage*, akurasi pada segmen diterima (*selective accuracy*), akurasi keseluruhan, serta laju terima-salah dan tolak-salah dengan ambang dari data validasi (Subbab 3.7).")
# 1.1 biaya
G("Sepasang modul inti diperkirakan sekitar Rp300.000, lebih ringan daripada kamera ditambah komputer pengolah citra; total biaya node lengkap dengan layar, audio, baterai, dan *enclosure* disusun lewat daftar komponen (BOM) yang diisi dari survei dan dinilai pada gerbang G4",
  "Sepasang modul inti diperkirakan sekitar Rp300.000, lebih ringan daripada kamera ditambah komputer pengolah citra. Total biaya node lengkap dengan layar, audio, baterai, dan *enclosure* disusun lewat daftar komponen (BOM) yang diisi dari survei dan dinilai pada gerbang G4")
# 2.4 regresi
G("dengan W~r~ berukuran 42 × 128 dan keluaran per segmen T × 21 × 2; bentuk ini dipilih karena J dan Z dibedakan lintasan gerak, bukan satu pose.",
  "dengan W~r~ berukuran 42 × 128 dan keluaran per segmen T × 21 × 2. Bentuk ini dipilih karena J dan Z dibedakan lintasan gerak, bukan satu pose.")
# 3.7 alur fitur
G("jendela fitur sepanjang W = 1 detik yang diringkas menjadi satu vektor masukan, dan langkah *embedding*, yaitu satu keluaran *encoder* per jendela; *encoder* diterapkan per jendela, bukan per bingkai, sesuai kontrak laju 1 Hz kartu model [11].",
  "jendela fitur sepanjang W = 1 detik yang diringkas menjadi satu vektor masukan, dan langkah *embedding*, yaitu satu keluaran *encoder* per jendela. *Encoder* diterapkan per jendela, bukan per bingkai, sesuai kontrak laju 1 Hz kartu model [11].")
# 2.2 fresnel
G("radius zona pertama r~1~ ≈ 0,18 meter sehingga ruang gerak tangan berada di zona yang paling peka terhadap perubahan jalur; artikulasi jari menggeser jalur pantulan pada orde sentimeter sampai milimeter, dan tiap bentuk huruf meninggalkan pola perubahan *subcarrier* yang khas.",
  "radius zona pertama r~1~ ≈ 0,18 meter sehingga ruang gerak tangan berada di zona yang paling peka terhadap perubahan jalur. Artikulasi jari menggeser jalur pantulan pada orde sentimeter sampai milimeter, dan tiap bentuk huruf meninggalkan pola perubahan *subcarrier* yang khas.")
# 2.2 nyquist
G("Pada laju *firmware* RuView 50 bingkai per detik [10], pita teramati hanya sampai 25 Hz, sehingga gerak tangan yang masih teramati tanpa pelipatan kira-kira 1,6 meter per detik; gerak jari yang lebih cepat berisiko terlipat, dan jika laju terukur lebih rendah, pita yang dianalisis ikut menyempit serta dilaporkan apa adanya.",
  "Pada laju *firmware* RuView 50 bingkai per detik [10], pita teramati hanya sampai 25 Hz, sehingga gerak tangan yang masih teramati tanpa pelipatan kira-kira 1,6 meter per detik. Gerak jari yang lebih cepat berisiko terlipat, dan jika laju terukur lebih rendah, pita yang dianalisis ikut menyempit serta dilaporkan apa adanya.")
# 1.1 paragraf 3
G("sistem yang mengubah ucapan menjadi animasi isyarat hanya melayani arah orang pendengar, sedangkan arah isyarat siswa yang dibaca mesin belum tersedia; riset di Indonesia masih berkutat di jalur kamera, misalnya pengenalan huruf BISINDO dari citra dengan CNN [5].",
  "sistem yang mengubah ucapan menjadi animasi isyarat hanya melayani arah orang pendengar. Arah isyarat siswa yang dibaca mesin belum tersedia; riset di Indonesia masih berkutat di jalur kamera, misalnya pengenalan huruf BISINDO dari citra dengan CNN [5].")
# 3.5 TTFA
G("Target latensinya didefinisikan sebagai waktu menuju audio pertama (*time-to-first-audio*, TTFA) di bawah 100 ms pada frasa uji paling banyak lima kata, dilaporkan menurut persentil p50 dan p95 pada lingkungan uji terdokumentasi [PERLU DATA: konfigurasi CPU/GPU, runtime, presisi model, dan opsi pre-cache audio huruf tunggal]; durasi sintesis keseluruhan dilaporkan terpisah.",
  "Target latensinya didefinisikan sebagai waktu menuju audio pertama (*time-to-first-audio*, TTFA) di bawah 100 ms pada frasa uji paling banyak lima kata. Pelaporannya menurut persentil p50 dan p95 pada lingkungan uji terdokumentasi [PERLU DATA: konfigurasi CPU/GPU, runtime, presisi model, dan opsi pre-cache audio huruf tunggal], dan durasi sintesis keseluruhan dilaporkan terpisah.")
# 3.7 tiga rute
G("Tiga rute karenanya disiapkan, yaitu Jalur A yang menghitung ulang delapan fitur turunan RuView, Jalur B1/B2 yang melatih adapter konvolusi satu dimensi (rekonstruksi atau tugas), dan Pembanding C yang memakai spektrum CSI tanpa penyempitan delapan fitur; keputusan rutenya diambil pada G0b",
  "Tiga rute karenanya disiapkan. Jalur A menghitung ulang delapan fitur turunan RuView, Jalur B1/B2 melatih adapter konvolusi satu dimensi (rekonstruksi atau tugas), dan Pembanding C memakai spektrum CSI tanpa penyempitan delapan fitur; keputusan rutenya diambil pada G0b")
# 3.8 pembuka
G("serta G4 di atas uji kegunaan, penilaian validator, dan analisis biaya; cakupan kamus melengkapi analisis tanpa menjadi syarat gerbang. Seluruh hasil dilaporkan sebagai bukti awal pada populasi terbatas sesuai Batasan no. 11 (Subbab 1.4).",
  "serta G4 di atas uji kegunaan, penilaian validator, dan analisis biaya. Cakupan kamus melengkapi analisis tanpa menjadi syarat gerbang, dan seluruh hasil dilaporkan sebagai bukti awal pada populasi terbatas sesuai Batasan no. 11 (Subbab 1.4).")
# 2.4 koordinat
G("Kandidat kuatnya koordinat ternormalisasi terhadap kotak deteksi guru atau titik pergelangan tangan, dengan konvensi *handedness*, skala acuan d~ref~, ambang PCK α, dan pemetaan target temporal ke pusat jendela ditetapkan pada T0 lalu dipakai konsisten oleh guru dan murid",
  "Kandidat kuatnya koordinat ternormalisasi terhadap kotak deteksi guru atau titik pergelangan tangan. Konvensi *handedness*, skala acuan d~ref~, ambang PCK α, dan pemetaan target temporal ke pusat jendela ditetapkan pada T0 lalu dipakai konsisten oleh guru dan murid")
# 2.12 penutup
G("Dengan rumusan itu, teori CSI dan zona Fresnel (Subbab 2.2) menyediakan sinyal, *encoder* terpralatih (Subbab 2.3) menyediakan representasi, kedua formulasi kepala (Subbab 2.4) menyediakan keluaran tugas, guru visual (Subbab 2.5) menyediakan labelnya, dan hasilnya diukur di tepi (Subbab 2.6) sebelum kedua arah disatukan menjadi purwarupa (BAB III).",
  "Dengan rumusan itu, teori CSI dan zona Fresnel (Subbab 2.2) menyediakan sinyal, *encoder* terpralatih (Subbab 2.3) menyediakan representasi, dan kedua formulasi kepala (Subbab 2.4) menyediakan keluaran tugas. Guru visual (Subbab 2.5) menyediakan labelnya, dan hasilnya diukur di tepi (Subbab 2.6) sebelum kedua arah disatukan menjadi purwarupa (BAB III).")
# 3.1 inti pelatihan
G("serta dua kepala tugas di atas *encoder* terpralatih yang dibekukan, lalu model terpilihnya dijalankan langsung di modul.",
  "serta dua kepala tugas di atas *encoder* terpralatih yang dibekukan. Model terpilihnya lalu dijalankan langsung di modul.")

print("total suntingan terdaftar:", len(E))
gagal = []
for old, new in E:
    c = naskah.count(old)
    if c != 1:
        gagal.append((old[:80], c))
    else:
        naskah = naskah.replace(old, new)
if gagal:
    for g_, c in gagal:
        print(f"GAGAL (ditemukan {c}): {g_}...")
    sys.exit(1)
print("seluruh suntingan diterapkan:", len(E))
out = V10 / "Proposal-SenseSIBI-v18.md"
out.write_text(naskah + log, encoding="utf-8")
print("tersimpan | tubuh:", len(naskah), "karakter")
