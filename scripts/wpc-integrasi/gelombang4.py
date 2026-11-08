#!/usr/bin/env python3
"""Gelombang 4 (Task 38): objek pengenalan = alfabet manual SIBI 26 huruf,
guru = pose tangan 21 keypoint (repo WPC), judul SenseSIBI.
Anchor pendek + fallback regex dash-toleran. Gagal keras bila ada yang tidak cocok."""
import re
import shutil
import sys
from pathlib import Path

DRAFT = Path("/home/z/my-project/download/translator-sibi-final/draft-final.md")
BACKUP = Path("/home/z/my-project/download/translator-sibi-final/_kerja/draft-final.sebelum-gelombang4.md")

teks = DRAFT.read_text(encoding="utf-8")
BACKUP.write_text(teks, encoding="utf-8")

EDITS = [
    # --- BAB II --- (2.3 sudah terganti oleh MultiEdit sebelumnya; tidak diulang)
    ("2.5 kpt_shape",
     "YOLO26-Pose dilatih pada *dataset keypoint* COCO dan menghasilkan 17 *keypoint* tubuh per orang, mencakup titik wajah, bahu, siku, dan pergelangan tangan, tanpa *keypoint* jari [42].",
     "Kerangka tersebut mendukung konfigurasi *keypoint* khusus melalui parameter *kpt_shape* pada *dataset* pelatihan dan menyediakan *dataset* *hand-keypoints* dengan 21 *keypoint* per tangan yang dianotasi memakai MediaPipe [42], sehingga model pose tangan dapat dilatih dengan alur kerja yang sama."),
    ("2.5 tubuh manusia",
     "memperkirakan posisi *keypoint* tubuh manusia dari citra atau video",
     "memperkirakan posisi *keypoint* manusia dari citra atau video"),
    ("2.5 estimator",
     "estimatornya diganti dengan YOLO26-Pose yang keluarannya juga 17 *keypoint* format COCO sehingga formatnya setara dengan skrip asli.",
     "estimatornya diganti dengan model guru pose tangan YOLO26-Pose dari repositori peneliti yang keluarannya 21 *keypoint* per tangan (Subbab 3.7.4)."),
    ("2.5 guru tidak klasifikasi",
     "sehingga model guru tidak mengklasifikasikan isyarat; klasifikasi gerakan otomatis dari video menuntut pengklasifikasi temporal di atas deret *keypoint* dan menjadi pengembangan lanjutan di luar cakupan.",
     "sehingga makna huruf tidak bergantung pada dugaan model visi; keluaran klasifikasi huruf yang juga dimiliki model guru repositori peneliti tidak dipakai pada jalur pelatihan murid."),
    ("2.5 keluaran guru",
     "Batas ini penting karena keluaran model hanya mencakup tubuh tanpa *keypoint* jari; batas tersebut sejalan dengan cakupan pengenalan yang memang dibatasi pada lintasan lengan, tubuh atas, dan kepala (Subbab 2.3).",
     "Keluaran guru berupa 21 *keypoint* pose tangan sehingga konfigurasi jari pada setiap huruf ikut tersupervisi; cakupan supervisi tersebut sejalan dengan objek pengenalan alfabet manual (Subbab 2.3)."),
    ("2.6 akurasi preseden",
     "dan pendekatan CSI dicoba pada *Filipino Sign Language* [23]. WiSign memperluas arah tersebut",
     "dan pendekatan CSI dicoba pada *Filipino Sign Language* dengan akurasi 69,3% [23]. Akurasi yang dilaporkan pada karya-karya tersebut berkisar dari angka itu hingga 99,8% pada kondisi laboratorium [21], [66] dan menurun pada pengguna baru, misalnya 86,66% lintas lima pengguna pada SignFi [21]. WiSign memperluas arah tersebut"),
    ("2.6 jumlah kelas",
     "sehingga klasifikasi 5–8 kelas berada pada kelas kompleksitas yang lebih rendah daripada contoh-contoh tersebut",
     "sehingga klasifikasi 26 kelas huruf berada pada kelas kompleksitas yang lebih rendah daripada contoh-contoh tersebut"),
    ("Tabel 2.2 baris 17",
     "| 17 | Penelitian ini | CSI dua-tiga modul ESP32-S3, distilasi guru–murid YOLO26-Pose ke CSI, inferensi tepi; dua arah | SIBI | Ya | Purwarupa penerjemah dua arah kosakata terbatas |",
     "| 17 | Penelitian ini | CSI dua-tiga modul ESP32-S3, distilasi guru–murid YOLO26-Pose pose tangan ke CSI, inferensi tepi; dua arah | SIBI, alfabet manual 26 huruf | Ya | Purwarupa penerjemah dua arah alfabet manual SIBI |"),
    ("2.11 kelompok kedua",
     "Kelompok kedua membuktikan kepekaan CSI terhadap gerak halus [25], [26] sehingga asumsi kelayakan penginderaan gerak lengan memiliki dasar, tetapi keduanya bukan sistem isyarat.",
     "Kelompok kedua membuktikan kepekaan CSI terhadap gerak halus [25], [26], termasuk pada tingkat ketukan jari, sehingga hipotesis kepekaan CSI terhadap konfigurasi tangan dan jari memiliki dasar, tetapi keduanya bukan sistem isyarat."),
    ("2.11 kebaruan",
     "yaitu menggabungkan penginderaan CSI satu tautan antarmodul untuk SIBI, distilasi guru–murid dari YOLO26-Pose ke model CSI",
     "yaitu menggabungkan penginderaan CSI satu tautan antarmodul untuk alfabet manual SIBI, distilasi guru–murid dari YOLO26-Pose pose tangan ke model CSI"),
    # --- BAB III ---
    ("3.1 kuantitatif",
     "dapat membedakan 5–8 isyarat SIBI terisolasi.",
     "dapat membedakan 26 huruf alfabet manual SIBI, yaitu 24 huruf statis serta huruf gerak J dan Z."),
    ("3.1 guru deret",
     "Model guru kamera YOLO26-Pose mengekstrak deret pose gerakan SIBI dari video perekaman; deret tersebut menjadi supervisi tambahan bagi model murid yang mengenali isyarat dari jendela CSI dan berjalan langsung pada modul (Subbab 3.7).",
     "Model guru kamera YOLO26-Pose mengekstrak deret 21 *keypoint* pose tangan dari video perekaman; deret tersebut menjadi supervisi tambahan bagi model murid yang mengenali huruf dari jendela CSI dan berjalan langsung pada modul (Subbab 3.7)."),
    ("Gambar 3.1 G1",
     'G1("G1 M3: separabilitas awal<br/>2–3 isyarat (nearest-centroid)")',
     'G1("G1 M3: separabilitas awal<br/>2–3 pasang huruf (nearest-centroid)")'),
    ("Gambar 3.2 P2",
     'P2["Pemangkasan ke 3–5 isyarat<br/>yang bertumpu pada lintasan"]',
     'P2["Pemangkasan ke himpunan huruf<br/>yang pembeda CSI-nya paling kuat"]'),
    ("T1 kurasi",
     "T1 mencakup kurasi 5–8 isyarat bersama validator penutur tunarungu, kalibrasi ruang mitra, penyusunan protokol perekaman dan etika, serta perizinan (Subbab 3.6). Kurasi juga menetapkan himpunan tampilan arah kedua, yaitu isyarat terpilih ditambah 26 huruf dan 9 angka sebagai kosakata ejaan jari (Subbab 2.8). G1 menguji separabilitas awal 2–3 isyarat dengan uji *nearest-centroid* sederhana yang rata-ratanya dihitung tanpa repetisi yang sedang diuji.",
     "T1 mencakup kurasi 26 huruf alfabet manual SIBI bersama validator penutur tunarungu, kalibrasi ruang mitra, penyusunan protokol perekaman dan etika, serta perizinan (Subbab 3.6). Kurasi juga menetapkan himpunan tampilan arah kedua, yaitu 26 huruf dan 9 angka ditambah kata terpilih dari kamus (Subbab 2.8), serta pasangan huruf dengan konfigurasi tangan yang paling mirip sebagai bahan G1. G1 menguji separabilitas awal 2–3 pasang huruf tersebut dengan uji *nearest-centroid* sederhana yang rata-ratanya dihitung tanpa repetisi yang sedang diuji."),
    ("T2 pemangkasan",
     "bila G2 gagal, cakupan dipangkas menjadi 3–5 isyarat yang pembedanya paling bertumpu pada lintasan (Tabel 3.6).",
     "bila G2 gagal, cakupan dipangkas menjadi himpunan huruf yang pembeda CSI-nya paling kuat (Tabel 3.6)."),
    ("Gambar 3.3 FLT",
     "keypoint YOLO26-Pose: buang<br/>orang hilang, jitter, terpotong",
     "keypoint YOLO26-Pose: buang<br/>tangan hilang, jitter, terpotong"),
    ("Gambar 3.3 Y26",
     "guru di laptop: 17 titik<br/>COCO + penanda waktu",
     "guru di laptop: 21 titik<br/>pose tangan + penanda waktu"),
    ("T5 keterbatasan",
     "Laporan memuat keterbatasan secara eksplisit, yaitu konfigurasi jari dan ekspresi wajah tidak dikenali, arah kedua berbentuk kamus kata-level dan ejaan jari, serta seluruh klaim terikat pada kosakata terbatas (Subbab 1.4).",
     "Laporan memuat keterbatasan secara eksplisit, yaitu klaim pengenalan terikat pada alfabet manual 26 huruf, ekspresi wajah dan penanda nonmanual tidak dikenali, arah kedua berbentuk kamus kata-level dan ejaan jari, serta keluaran berupa huruf atau kata, bukan kalimat isyarat (Subbab 1.4)."),
    ("3.5.3 zona",
     "mengapit zona isyarat agar gerak lengan dan tubuh atas berada di antara keduanya",
     "mengapit zona isyarat agar tangan dan lengan pengisyarat berada di antara keduanya"),
    ("3.6.1 validator",
     "validator menentukan kosakata, memeriksa sampel segmen, dan menilai kewajaran keluaran purwarupa",
     "validator memeriksa lembar definisi huruf, memeriksa sampel segmen, dan menilai kewajaran keluaran purwarupa"),
    ("3.6.2 kurasi",
     "Isyarat pengenalan dipilih melalui dua saringan (Subbab 1.4) dengan acuan *Kamus SIBI* [45], sedangkan kosakata tampilan arah kedua mencakup isyarat terpilih tersebut ditambah 26 huruf dan 9 angka sebagai landasan ejaan jari [13]. Hasilnya adalah daftar 5–8 isyarat terisolasi [PERLU DATA: daftar isyarat SIBI terpilih] yang dideskripsikan dalam lembar definisi isyarat sebagai acuan perekaman dan penilaian.",
     "Alfabet manual yang menjadi objek pengenalan mencakup 26 huruf, yaitu 24 huruf statis serta huruf gerak J dan Z, dengan bentuk baku mengacu pada *Kamus SIBI* [45]. Lembar definisi setiap huruf memuat deskripsi konfigurasi tangan dan jari serta lintasan gerak untuk J dan Z, validator menyetujui lembar tersebut, dan pasangan huruf dengan konfigurasi tangan yang paling mirip ditetapkan sebagai bahan gerbang G1. Kosakata tampilan arah kedua mencakup 26 huruf dan 9 angka ditambah kata terpilih sebagai landasan ejaan jari [13]."),
    ("3.6.3 elisitasi",
     "yaitu satu isyarat per segmen dengan jeda antarrepetisi. Adapun prosedur perekaman setiap sesi adalah sebagai berikut.",
     "yaitu satu huruf per segmen dengan jeda antarrepetisi; huruf statis diperagakan sebagai pose yang ditahan sejenak, sedangkan J dan Z diperagakan sebagai lintasan gerak. Adapun prosedur perekaman setiap sesi adalah sebagai berikut."),
    ("3.6.3 langkah 5",
     "5. Menampilkan kartu pemandu isyarat target, merekam satu repetisi, memberi jeda, dan mengulanginya hingga setiap isyarat mencapai kurang lebih 30 repetisi.",
     "5. Menampilkan kartu pemandu huruf target, merekam satu repetisi, memberi jeda, dan mengulanginya hingga setiap huruf mencapai kurang lebih 30 repetisi."),
    ("3.6.3 langkah 6",
     "6. Membuang segmen bila orang tidak terdeteksi YOLO26-Pose, terjadi *jitter* *keypoint* ekstrem, atau segmen terpotong, lalu mencatat tingkat segmen terbuang per isyarat dan per pengisyarat.",
     "6. Membuang segmen bila tangan tidak terdeteksi model guru, terjadi *jitter* *keypoint* ekstrem, atau segmen terpotong, lalu mencatat tingkat segmen terbuang per huruf dan per pengisyarat."),
    ("3.7.2 segmentasi",
     "Deret CSI dipotong menjadi segmen isyarat dengan segmentasi berbasis energi gerak RuView [28].",
     "Deret CSI dipotong menjadi segmen huruf dengan segmentasi berbasis energi gerak RuView [28]; huruf gerak J dan Z terpotong jelas dari energi geraknya, sedangkan huruf statis memerlukan jendela tahan pose yang ambang dan panjangnya ditetapkan pada Tabel 3.6."),
    ("3.7.4 guru COCO",
     "yang mengekstrak deret 17 *keypoint* format COCO dari video perekaman dan hasilnya menjadi supervisi tambahan bagi model murid CSI.",
     "yang mengekstrak deret 21 *keypoint* pose tangan dari video perekaman dan hasilnya menjadi supervisi tambahan bagi model murid CSI."),
    ("3.7.4 mAP50",
     "Sembilan eksperimen yang tercatat pada repositori menghasilkan model juara dengan *pose* mAP50 0,8944 pada 49 kelas isyarat pada *split* validasi, sehingga kemampuan melatih guru pada data visual SIBI telah terbukti sebelum penelitian ini dimulai.",
     "Sembilan eksperimen yang tercatat pada repositori menghasilkan model juara pose tangan 21 *keypoint* dengan *pose* mAP50 0,8944 pada 49 kelas isyarat (25 huruf dan 24 kata) pada *split* validasi, dan eksperimen lanjutan pada himpunan 24 huruf statis mencatat mAP50 0,9580 dengan akurasi huruf 97,6%, sehingga kemampuan melatih guru pose tangan pada data visual SIBI telah terbukti sebelum penelitian ini dimulai."),
    ("3.7.4 retargeting",
     "Penyesuaian yang diperlukan adalah penargetan ulang kepala *keypoint* dari pose tangan 21 titik milik repositori ke 17 *keypoint* format COCO yang dibutuhkan jalur guru, disertai penyiapan data visual SIBI hasil perekaman ke format *dataset* pelatihan, penyetelan konfigurasi, dan validasi hasil mengikuti alur baku pelatihan, validasi, dan ekspor model Ultralytics [42].",
     "Model juara tersebut dipakai sebagai bentuk awal guru sehingga penargetan ulang kepala *keypoint* tidak diperlukan. Penyesuaian yang diperlukan adalah penyiapan data visual SIBI hasil perekaman T2 ke format *dataset* pelatihan, penyetelan konfigurasi, dan validasi hasil mengikuti alur baku pelatihan, validasi, dan ekspor model Ultralytics [42]."),
    ("3.7.4 deteksi orang",
     "Pelatihan lanjutan dipilih agar deteksi orang dan kestabilan *keypoint* pada gerakan tangan SIBI meningkat dibandingkan model awal.",
     "Pelatihan lanjutan dipilih agar deteksi tangan dan kestabilan *keypoint* pada konfigurasi huruf SIBI meningkat dibandingkan model awal."),
    ("3.7.4 proporsi orang",
     "kualitas guru dievaluasi melalui tiga ukuran, yaitu proporsi bingkai dengan orang terdeteksi",
     "kualitas guru dievaluasi melalui tiga ukuran, yaitu proporsi bingkai dengan tangan terdeteksi"),
    ("3.7.4 sumber label",
     "Model guru tidak mengklasifikasikan isyarat. Label kelas SIBI berasal dari anotasi protokol *elisitasi*, yaitu kartu pemandu yang menentukan isyarat pada setiap segmen (Subbab 3.6) sehingga makna isyarat tidak bergantung pada dugaan model visi.",
     "Model guru dipakai sebagai penyedia deret *keypoint*, bukan sebagai sumber label; meskipun model pose tangan repositori peneliti juga memuat keluaran klasifikasi huruf, label kelas SIBI tetap berasal dari anotasi protokol *elisitasi*, yaitu kartu pemandu yang menentukan huruf pada setiap segmen (Subbab 3.6) sehingga makna huruf tidak bergantung pada dugaan model visi."),
    ("3.7.5 jendela",
     "Masukan murid berupa jendela deret CSI, bukan cuplikan tunggal, karena gerakan SIBI bersifat temporal sehingga polanya hanya tampak pada urutan waktu (Subbab 2.3).",
     "Masukan murid berupa jendela deret CSI, bukan cuplikan tunggal: huruf statis memerlukan jendela agar pola kanal saat pose ditahan dan getar mikro tangan terekam, sedangkan huruf gerak J dan Z bersifat temporal sehingga polanya hanya tampak pada urutan waktu (Subbab 2.3)."),
    ("Gambar 3.7 MOD",
     "TFLM/ESP-DL: 5–8 kelas,",
     "TFLM/ESP-DL: 26 kelas huruf,"),
    ("3.8.2 peluang acak",
     "yaitu 20% untuk lima kelas dan 12,5% untuk delapan kelas, serta 33,3% bila cakupan dipangkas menjadi tiga isyarat.",
     "yaitu satu dibagi jumlah kelas, sekitar 3,8% untuk 26 kelas huruf, dan dihitung ulang bila cakupan dipangkas ke himpunan huruf yang lebih kecil."),
    ("3.8.7 diagnosis",
     "dengan kemiripan lintasan tubuh dari deret *keypoint* YOLO26-Pose untuk membedakan kesalahan akibat lintasan yang mirip dari kesalahan akibat sinyal CSI yang lemah.",
     "dengan kemiripan pose tangan pada deret *keypoint* guru untuk membedakan kesalahan akibat konfigurasi tangan yang mirip dari kesalahan akibat sinyal CSI yang lemah."),
    ("Tabel 3.4 G1",
     "Separabilitas awal 2–3 isyarat (*nearest-centroid*) | Repetisi isyarat yang sama lebih dekat satu sama lain daripada ke isyarat lain",
     "Separabilitas awal 2–3 pasang huruf mirip (*nearest-centroid*) | Repetisi huruf yang sama lebih dekat satu sama lain daripada ke huruf lain"),
    ("Tabel 3.4 G2",
     "Cakupan dipangkas menjadi 3–5 isyarat yang bertumpu pada lintasan",
     "Cakupan dipangkas menjadi himpunan huruf yang pembeda CSI-nya paling kuat"),
    ("Tabel 3.5 baris 2",
     "T1 Kurasi isyarat dan kosakata tampilan",
     "T1 Kurasi alfabet manual SIBI dan kosakata tampilan"),
    ("Tabel 3.6 butir 8",
     "| 8 | Kriteria pemangkasan isyarat |",
     "| 8 | Kriteria pemangkasan himpunan huruf |"),
    ("Tabel 3.6 butir 26",
     "ambang proporsi deteksi orang",
     "ambang proporsi deteksi tangan"),
    ("Tabel 3.6 tambah 28",
     "| 27 | Bentuk dan bobot suku supervisi guru | Dari data validasi | [PERLU DATA: bentuk suku distilasi dan bobotnya, ditetapkan dari data validasi] |",
     "| 27 | Bentuk dan bobot suku supervisi guru | Dari data validasi | [PERLU DATA: bentuk suku distilasi dan bobotnya, ditetapkan dari data validasi] |\n| 28 | Segmentasi huruf statis | Sebelum dipakai | [PERLU DATA: ambang energi dan panjang jendela tahan pose untuk huruf statis] |"),
    ("Tabel 3.7 tambah 10",
     "| 9 | Kuota atau aksesibilitas layanan server GPU Kaggle terbatas saat pelatihan | Jadwal pelatihan guru dan murid mundur | Lingkungan pelatihan dan data disiapkan terkompresi agar sesi efisien; pelatihan murid yang ringan dapat dipindahkan ke laptop; jadwal disesuaikan |",
     "| 9 | Kuota atau aksesibilitas layanan server GPU Kaggle terbatas saat pelatihan | Jadwal pelatihan guru dan murid mundur | Lingkungan pelatihan dan data disiapkan terkompresi agar sesi efisien; pelatihan murid yang ringan dapat dipindahkan ke laptop; jadwal disesuaikan |\n| 10 | Huruf dengan konfigurasi tangan yang sangat mirip tidak dapat dipisahkan CSI | Himpunan kelas efektif menyempit | Pemangkasan himpunan huruf pada G1–G2 mengikuti kriteria Tabel 3.6; pasangan yang gagal dilaporkan sebagai temuan kelayakan |"),
    # --- DP ---
    ("DP [42]",
     '[42] Ultralytics, "Pose estimation," Ultralytics YOLO Docs. [Online]. Available: https://docs.ultralytics.com/tasks/pose/, diakses 25 Okt. 2026.',
     '[42] Ultralytics, "Pose estimation" dan "Hand Keypoints Pose Estimation Dataset," Ultralytics YOLO Docs. [Online]. Available: https://docs.ultralytics.com/tasks/pose/ dan https://docs.ultralytics.com/datasets/pose/hand-keypoints/, diakses 8 Nov. 2026.'),
]

LOG4 = """

## Log Perubahan — Revisi 8 November 2026, gelombang 4 (SenseSIBI + objek pengenalan alfabet manual)

| Lokasi | Sebelum | Sesudah | Alasan |
|---|---|---|---|
| Judul | "…ANTARA SISTEM ISYARAT BAHASA INDONESIA (SIBI) DAN TEKS ATAU UJARAN… UNTUK KOSAKATA TERBATAS" | "STUDI KELAYAKAN PURWARUPA SenseSIBI: SISTEM PENERJEMAHAN DUA ARAH HURUF SIBI BERBASIS WI-FI CSI DENGAN INFERENSI ESP32-S3 DAN PEMROSESAN SERVER" | Judul baru pemilik 8 Nov 2026; bentuk SenseSIBI dipertahankan |
| 1.1–1.5 | Kosakata 5–8 isyarat lintasan; "konfigurasi jari dan ekspresi wajah tidak dikenali"; "bukti tidak berlaku bagi bentuk jari" | Objek pengenalan = alfabet manual SIBI 26 huruf (24 statis + J dan Z); konfigurasi tangan dan jari menjadi pembeda utama; ekspresi wajah dan penanda nonmanual tetap tidak dikenali | Keputusan pemilik 8 Nov 2026: proyek nyata memakai 24 huruf statis + J/Z dengan pose tangan dan jari |
| 2.3 ¶ akhir | "perbedaan konfigurasi jari dan ekspresi wajah diasumsikan terlalu halus untuk dibedakan secara andal; cakupan dibatasi lintasan lengan, tubuh atas, kepala" | Kelayakan satu tautan ESP32-S3 membedakan 26 konfigurasi tangan diperlakukan sebagai pertanyaan penelitian; hipotesis kerja dari bukti milimeter, Cai dkk. satu pemancar–penerima 98,3% [54], dan WiASL [67]; diuji Delta-CSI dan G1–G2 dengan pemangkasan bila gagal | Klaim lama bertentangan dengan literatur CSI tingkat jari ([21], [23], [25], [54], [58], [67]) dan dengan objek proyek pemilik |
| 2.5, 3.7.4 | Guru = YOLO26-Pose 17 keypoint COCO tubuh; "penargetan ulang kepala keypoint 21 titik pose tangan → 17 COCO"; "model guru tidak mengklasifikasikan" | Guru = model pose tangan 21 keypoint repositori WPC (juara mAP50 0,8944 pada 49 kelas; 24 huruf statis mAP50 0,9580, akurasi huruf 97,6%); tanpa retargeting; keluaran klasifikasi guru tidak dipakai sebagai label | Audit repositori WPC (Task 35): bobot pose tangan terlatih nyata; retargeting hanya diperlukan karena kosakata lama |
| 3.6–3.8, Tabel 3.4–3.7 | Saringan separabilitas fisik kurator kosakata; pemangkasan "3–5 isyarat lintasan"; peluang acak 20%/12,5%/33,3%; diagnosis kesalahan lintasan tubuh | Lembar definisi 26 huruf + pasangan mirip bahan G1; pemangkasan ke himpunan huruf berpembeda kuat; peluang acak 1/26 ≈ 3,8%; diagnosis kesalahan kemiripan pose tangan; risiko pasangan huruf mirip (Tabel 3.7 butir 10); parameter segmentasi huruf statis (Tabel 3.6 butir 28) | Konsistensi metode dengan objek pengenalan huruf |

Catatan: disiplin klaim tetap utuh — naskah tetap studi kelayakan; murid CSI tetap mengklasifikasi langsung dari pola CSI tanpa ekstraksi pose dari CSI; pose tangan hanya pada jalur guru kamera dengan bobot terlatih WPC; Delta-CSI 2×ESP32 tetap gerbang go/no-go. Daftar Pustaka tetap 80 entri (entri [42] hanya diperluas URL dokumen hand-keypoints Ultralytics yang terverifikasi).
"""

gagal = []
for label, old, new in EDITS:
    n = teks.count(old)
    if n == 1:
        teks = teks.replace(old, new)
        print(f"OK   {label}")
        continue
    # fallback: regex toleran perbedaan en-dash/hyphen
    pola = re.escape(old).replace("\\u2013", "[–-]").replace("-", "[–-]")
    m = re.findall(pola, teks)
    if len(m) == 1:
        teks = re.sub(pola, new.replace("\\", "\\\\"), teks, count=1)
        print(f"OK-R {label} (fallback dash)")
        continue
    gagal.append((label, n, len(m)))
    print(f"GAGAL {label}: exact={n} regex={len(m)}")

if gagal:
    print("\nGAGAL TOTAL:", len(gagal))
    for label, n, m in gagal:
        print(" -", label, f"exact={n} regex={m}")
    sys.exit(1)

if "Catatan: ke-17 rujukan yang dipulihkan" not in teks:
    print("GAGAL: anchor log gelombang 3 tidak ditemukan")
    sys.exit(1)
teks = teks.replace(
    "Catatan: ke-17 rujukan yang dipulihkan adalah rujukan berbayar/cetak yang akses salinannya terbatas; seluruh dokumennya tetap tersedia pada paket ZIP 80 rujukan (Gofile).",
    "Catatan: ke-17 rujukan yang dipulihkan adalah rujukan berbayar/cetak yang akses salinannya terbatas; seluruh dokumennya tetap tersedia pada paket ZIP 80 rujukan (Gofile)." + LOG4,
    1,
)
print("OK   log gelombang 4 ditambahkan")

DRAFT.write_text(teks, encoding="utf-8")
print("\nSelesai. Sisa '5–8':", teks.count("5–8"), "| '3–5 isyarat':", teks.count("3–5 isyarat"),
      "| 'bentuk jari':", teks.count("bentuk jari"), "| '17 *keypoint*':", teks.count("17 *keypoint*"),
      "| retarget:", teks.count("penargetan ulang"))
