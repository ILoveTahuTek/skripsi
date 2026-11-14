#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gelombang 20: v19 -> v20.
Menerapkan ledger 25 isu hasil koreksi terhadap baseline kebenaran v17 (HANDOFF):
(1) tebakan yang sebelumnya disisipkan sebagai spesifikasi final dikembalikan ke
    status terbuka [PERLU DATA] (PCM 16 kHz; regulator 500-800 mA; kapasitas
    baterai 2.500-3.000 mAh; pre-cache 26 klip sebagai strategi final);
(2) butir handoff yang terlewat dilengkapi (pinout T0, audit T0 buffer/RSSI/fase,
    repetisi terpakai, penyelarasan keypoint, uji pilot pose/J-Z, kerangka BOM);
(3) keputusan kondisional dijaga (Pilihan 1 -> Tabel 3.7 no. 19; MMS-TTS-ind ->
    Tabel 3.7 no. 17; Kokoro tidak dibuang).
Suntingan berjangkar (asersi hitung == 1) dan hanya pada TUBUH naskah (sebelum
penanda AKHIR NASKAH); area Log Perubahan dijaga sebagai rekam historis.
"""
from pathlib import Path

SRC = Path("/home/z/my-project/download/sensesibi-v10/Proposal-SenseSIBI-v19.md")
DST = Path("/home/z/my-project/download/sensesibi-v10/Proposal-SenseSIBI-v20.md")

teks = SRC.read_text(encoding="utf-8")
MARK = "<!-- ===== AKHIR NASKAH"
assert teks.count(MARK) == 1
tubuh, ekor = teks.split(MARK, 1)

suntingan = []

def ganti(lama, baru, nama):
    suntingan.append((nama, lama, baru))

# E1 - Subbab 3.5: protokol audio; tebakan PCM 16-bit mono 16 kHz dikembalikan
# menjadi kerangka uji terbuka (a)-(d) sesuai draf 5.3 ledger.
ganti(
    "Untuk menjamin aliran audio dua arah tidak melumpuhkan penangkapan CSI 50 bingkai per detik pada kanal Wi-Fi yang sama, spesifikasi protokol audio ditetapkan secara eksplisit sebelum G3. Jalur mikrofon Arah 2 (INMP441 I2S) menggunakan cuplikan PCM 16-bit mono 16 kHz yang dikirim dalam paket berukuran tetap melalui UDP berpenyangga atau aliran TCP/WebSocket saat tombol PTT ditekan, disertai nomor urut untuk mendeteksi paket hilang beserta batas waktu dan pengulangan pada server Rust. Jalur *speaker* Arah 1 (MAX98357A I2S) menerima aliran audio PCM 16-bit mono (atau berkas klip ter-*cache* untuk 26 huruf tunggal) ke penyangga cincin (*ring buffer*) di PSRAM modul RX guna mencegah *underrun* akibat jitter Wi-Fi. Dampak lalu lintas audio terhadap kestabilan laju CSI dan *packet loss* diukur langsung pada T0 dan G3; apabila koeksistensi pada satu modul RX menimbulkan degradasi CSI melampaui ambang G0, jalur cadangan C (memisahkan antarmuka audio ke modul ketiga atau pemutaran di ponsel) diaktifkan dan dilaporkan.",
    "Untuk menjamin aliran audio dua arah tidak melumpuhkan penangkapan CSI 50 bingkai per detik pada kanal Wi-Fi yang sama, protokol komunikasi dan audio ditetapkan serta diuji secara empiris pada T0 dan gerbang G3 dengan cakupan: (a) verifikasi koeksistensi *firmware* yang menjalankan *callback* CSI, koneksi *station*, dan pengiriman UDP secara serentak; (b) penetapan format audio, *codec*, laju pencuplikan, mekanisme *streaming* dan penyangga untuk aliran mikrofon (INMP441 I2S) maupun pengeras suara (MAX98357A I2S), beserta penanganan *packet loss*, batas waktu, dan pengulangan [PERLU DATA: spesifikasi protokol audio hasil audit T0]; (c) sinkronisasi penanda waktu antarmodul dan server; serta (d) dampak beban lalu lintas audio terhadap laju aktual CSI dan kestabilan jaringan. Sebagai kerangka kerja awal, cuplikan mikrofon dialirkan dalam paket bernomor urut melalui UDP berpenyangga atau *WebSocket* saat tombol PTT ditekan, dan aliran pengeras suara Arah 1 masuk ke penyangga cincin (*ring buffer*) di PSRAM modul RX guna mencegah *underrun* akibat jitter Wi-Fi; pemilihan format dan laju pencuplikan final mengikuti hasil uji T0, bukan asumsi di muka. Apabila koeksistensi pada satu modul RX menimbulkan degradasi CSI melampaui ambang G0, jalur cadangan C (memisahkan antarmuka audio ke modul ketiga atau pemutaran di ponsel) diaktifkan dan dilaporkan.",
    "E1 protokol audio",
)

# E2a - Subbab 3.5: verifikasi pinout diperluas (ADC1, konflik periferal, revisi papan).
ganti(
    "Pemetaan pin GPIO pada Tabel 3.3 dipilih agar tidak menabrak pin *strapping* (GPIO 0, 3, 45, 46) maupun kanal USB bawaan papan [8], dan diverifikasi ulang pada T0.",
    "Pemetaan pin GPIO pada Tabel 3.3 dipilih agar tidak menabrak pin *strapping* (GPIO 0, 3, 45, 46) maupun kanal USB bawaan papan [8], lalu diverifikasi ulang pada unit papan fisik saat T0 dengan cakupan yang dirinci pada catatan Tabel 3.3.",
    "E2a pinout paragraf",
)

# E2b - Subbab 3.5: rantai daya jadi uji bangku T0/G3; target 500-800 mA dihapus.
ganti(
    "Pada rantai daya itu, regulator 3,3 V dipastikan memiliki kapasitas arus kontinu memadai (target 500 sampai 800 mA guna menampung lonjakan arus Wi-Fi TX dan penguat kelas D MAX98357A saat *speaker* 8 Ω 3 W aktif), serta modul TP4056 diuji untuk memastikan tidak terjadi gangguan pengisian akibat beban puncak sistem (*load-sharing* atau larangan operasi aktif saat pengisian jika modul tanpa *power-path*).",
    "Pada rantai daya itu, kecukupan arus puncak regulator 3,3 V saat Wi-Fi TX dan penguat kelas D MAX98357A aktif bersama *speaker*, sekaligus keamanan pengisian daya pada modul TP4056 (*load-sharing* atau larangan operasi aktif saat pengisian jika modul tanpa *power-path*), diverifikasi pada uji bangku T0 dan G3 [PERLU DATA: profil arus puncak terukur, regulasi beban saat pengisian, dan kapasitas regulator terpilih]; nilai kapasitas arus tidak diasumsikan di muka.",
    "E2b rantai daya",
)

# E3 - Catatan verifikasi pinout setelah Tabel 3.3.
ganti(
    "| 6 | Pemantau tegangan baterai | ADC | GPIO 1 (ADC1_CH0) | Keluaran pembagi tegangan baterai |\n",
    "| 6 | Pemantau tegangan baterai | ADC | GPIO 1 (ADC1_CH0) | Keluaran pembagi tegangan baterai |\n\nSeluruh baris Tabel 3.3 wajib diverifikasi ulang pada unit papan fisik yang dibeli saat T0; verifikasi mencakup pin *strapping* (GPIO 0, 3, 45, 46), jalur USB, kemampuan kanal ADC1, potensi konflik periferal I2C/I2S/SPI, dan revisi papan, dengan penyesuaian pemetaan yang dicatat dan dilaporkan.\n",
    "E3 catatan Tabel 3.3",
)

# E4 - Subbab 3.5: pre-cache dari strategi final menjadi opsi yang dievaluasi G3.
ganti(
    "Untuk keluaran huruf tunggal pada Arah 1, klip audio 26 huruf di-*pre-cache* agar pemutaran tetap instan.",
    "Untuk keluaran huruf tunggal pada Arah 1, opsi pra-penyimpanan (*pre-cache*) klip audio 26 huruf dievaluasi pada G3 sebagai salah satu cara menjaga pemutaran tetap instan [PERLU DATA: keputusan opsi *pre-cache* dan hasil uji bandingnya terhadap sintesis langsung].",
    "E4 pre-cache opsi",
)

# E5 - Subbab 3.6 langkah 4: metode penyelarasan keypoint masuk daftar terbuka.
ganti(
    "[PERLU DATA: toleransi sinkronisasi akhir, misalnya 20 ms atau satu bingkai CSI]",
    "[PERLU DATA: toleransi sinkronisasi akhir, misalnya 20 ms atau satu bingkai CSI; metode penyelarasan dan resampling *keypoint* ke pusat jendela CSI]",
    "E5 penyelarasan keypoint",
)

# E6 - Subbab 3.6 langkah 6: repetisi terpakai per kelas/sesi dicatat.
ganti(
    "tingkat segmen terbuang dan skor kualitas anotasi tiap segmen dicatat.",
    "tingkat segmen terbuang, skor kualitas anotasi tiap segmen, serta jumlah dan proporsi repetisi yang benar-benar dipakai per kelas dan per sesi setelah pembuangan dicatat dan dilaporkan.",
    "E6 repetisi terpakai",
)

# E7a - Subbab 3.2: daftar audit T0 dilengkapi (buffer, paket hilang, RSSI, fase).
ganti(
    "uji Delta-CSI (Subbab 3.8.1), koeksistensi radio dengan *streaming* audio aktif, dan pengukuran laju pencuplikan.",
    "uji Delta-CSI (Subbab 3.8.1), koeksistensi radio dengan *streaming* audio aktif, serta pengukuran laju pencuplikan, laju paket hilang, panjang buffer CSI, RSSI dan *noise floor*, dan penanganan fase pada *callback*.",
    "E7a audit T0",
)

# E7b - Subbab 3.2: uji pilot pose memuat konfigurasi jari, orientasi telapak, J/Z.
ganti(
    "uji pilot keterpisahan awal beberapa pose tangan statis di samping pemisahan gerak dan diam",
    "uji pilot keterpisahan awal beberapa pose tangan statis dengan konfigurasi jari dan orientasi telapak berbeda, termasuk percobaan awal huruf dinamis J dan Z, di samping pemisahan gerak dan diam",
    "E7b pilot pose T0",
)

# E8 - Subbab 3.8.1 langkah 2: uji pilot konfigurasi tangan/orientasi/J-Z.
ganti(
    "2. Merekam CSI dalam tiga kondisi: ruang kosong, pengisyarat diam, dan pengisyarat bergerak.",
    "2. Merekam CSI dalam tiga kondisi dasar (ruang kosong, pengisyarat diam, dan pengisyarat bergerak) ditambah uji pilot beberapa konfigurasi tangan statis yang berbeda, orientasi telapak yang berbeda, serta percobaan awal huruf J dan Z.",
    "E8 pilot 3.8.1",
)

# E9 - Tabel 3.5 baris G3: konfigurasi TTS mengikuti keputusan no. 17; pre-cache opsi.
ganti(
    "konfigurasi TTS Indonesia default MMS-TTS-ind ONNX (dengan *pre-cache* 26 huruf tunggal) kecuali Kokoro mendukung bahasa Indonesia sebelum G3",
    "konfigurasi TTS Indonesia mengikuti keputusan Tabel 3.7 no. 17 (kandidat default MMS-TTS-ind ONNX dengan opsi *pre-cache* 26 huruf tunggal) kecuali Kokoro mendukung bahasa Indonesia sebelum G3",
    "E9 G3 TTS",
)

# E10 - Tabel 3.7 no. 17: opsi pre-cache.
ganti(
    "kandidat utama MMS-TTS-ind ONNX dengan *pre-cache* 26 huruf), lokasi sintesis D3",
    "kandidat utama MMS-TTS-ind ONNX dengan opsi *pre-cache* 26 huruf), lokasi sintesis D3",
    "E10 no17 opsi",
)

# E11 - Tabel 3.8 no. 8: kandidat konfigurasi menunggu konfirmasi.
ganti(
    "MMS-TTS-ind ONNX + *pre-cache* audio 26 huruf tunggal sebagai konfigurasi utama, lalu cadangan server lokal, ponsel, atau awan (cadangan D)",
    "MMS-TTS-ind ONNX dengan opsi *pre-cache* audio 26 huruf tunggal sebagai kandidat konfigurasi utama menunggu konfirmasi, lalu cadangan server lokal, ponsel, atau awan (cadangan D)",
    "E11 T38 no8",
)

# E12 - Keterangan Gambar 3.5: kondisional Pilihan 2 merujuk Tabel 3.7 no. 19.
ganti(
    "Gambar 3.5 Alur inferensi langsung pada ESP32-S3 menurut rancangan *deployment* Pilihan 1 tanpa kepala regresi, dengan segmentasi tiga fase dan mekanisme tolak; seluruh latensi dan memori diukur langsung pada perangkat, bukan dijanjikan",
    "Gambar 3.5 Alur inferensi langsung pada ESP32-S3 menurut rancangan *deployment* Pilihan 1 tanpa kepala regresi (aktivasi kepala regresi Pilihan 2 menunggu konfirmasi Tabel 3.7 no. 19), dengan segmentasi tiga fase dan mekanisme tolak; seluruh latensi dan memori diukur langsung pada perangkat, bukan dijanjikan",
    "E12 keterangan G3.5",
)

# E13 - Tabel 3.1 baris 6: kapasitas baterai tebakan menjadi terbuka.
ganti(
    "Li-Po 3,7 V 2.500–3.000 mAh [PERLU DATA: kapasitas final berdasarkan uji arus]; proteksi; pengisi 1 A USB-C",
    "Li-Po 3,7 V [PERLU DATA: kapasitas final ditetapkan dari uji arus T0 dan G3]; proteksi; pengisi 1 A USB-C",
    "E13 baterai 3.1",
)

# E14 - Kerangka BOM tanpa angka tebakan, disisipkan setelah Tabel 3.1.
bom = (
    "| 10 | *Webcam* | Bawaan laptop | 1 unit | Hanya untuk jalur guru |\n"
    "\n"
    "Rencana daftar komponen (*bill of materials*, BOM) pengadaan disusun dari baris Tabel 3.1 dan diisi hasil survei harga sebelum pembelian tanpa mengarang angka; sel berisi [PERLU DATA] dilengkapi dari survei harga, dan totalnya dinilai pada G4 (Persamaan 3.5) dengan memisahkan harga pasangan modul inti dari total node antarmuka lengkap:\n"
    "\n"
    "| No. | Komponen | Jumlah | Harga Satuan (Rp) | Subtotal (Rp) | Sumber Rujukan Harga |\n"
    "|---|---|---|---|---|---|\n"
    "| 1 | Modul ESP32-S3 (TX dan RX) | 2 unit | [PERLU DATA] | [PERLU DATA] | [PERLU DATA] |\n"
    "| 2 | Layar modul final (OLED 0,96 inci atau TFT 1,3 inci) | 1 unit | [PERLU DATA] | [PERLU DATA] | [PERLU DATA] |\n"
    "| 3 | *Rotary encoder* EC11 dan tombol PTT/reset | 1–2 set | [PERLU DATA] | [PERLU DATA] | [PERLU DATA] |\n"
    "| 4 | Mikrofon I2S INMP441 | 1 unit | [PERLU DATA] | [PERLU DATA] | [PERLU DATA] |\n"
    "| 5 | DAC I2S MAX98357A dan pengeras suara 8 Ω 3 W | 1 set | [PERLU DATA] | [PERLU DATA] | [PERLU DATA] |\n"
    "| 6 | Baterai Li-Po kapasitas final, BMS 1S, TP4056, komponen pasif, dan pembagi tegangan | 1–2 set | [PERLU DATA] | [PERLU DATA] | [PERLU DATA] |\n"
    "| 7 | *Enclosure* cetak tiga dimensi, kabel, header, dan PCB | 2 set | [PERLU DATA] | [PERLU DATA] | [PERLU DATA] |\n"
    "| Total | Sepasang node antarmuka lengkap (di luar laptop, ponsel, dan *access point*) | - | - | [PERLU DATA] | - |\n"
)
ganti(
    "| 10 | *Webcam* | Bawaan laptop | 1 unit | Hanya untuk jalur guru |\n",
    bom,
    "E14 kerangka BOM",
)

# E15 - Prosa Persamaan (3.1) selaras N~valid~ (Subbab 2.2), bukan 56 tetap.
ganti(
    "yaitu rata-rata besar perubahan koefisien kanal kompleks antarbingkai pada seluruh 56 *subcarrier*:",
    "yaitu rata-rata besar perubahan koefisien kanal kompleks antarbingkai pada himpunan *subcarrier* valid N~valid~ hasil audit T0 (Subbab 2.2):",
    "E15 prosa 3.1",
)

log_baru = """## Log Perubahan — Revisi 14 November 2026, gelombang 20 (disiplin penanda terbuka: spesifikasi belum diuji dikembalikan status terbuka; pelengkapan audit T0, pinout, repetisi, dan kerangka BOM)

Permintaan: menerapkan ledger 25 isu hasil koreksi terhadap baseline kebenaran v17 (HANDOFF) yang menegaskan tiga pelanggaran gelombang 18, yaitu mengisi celah terbuka dengan angka tebakan, mendahului konfirmasi pengguna, dan butir handoff yang terlewat. Kaidah bahasa mengikuti skill sempro-mepet; keputusan terbuka tidak diputuskan sepihak.

- Tebakan dikembalikan status terbuka: spesifikasi protokol audio "PCM 16-bit mono 16 kHz" diganti kerangka uji (a) sampai (d) dengan [PERLU DATA: spesifikasi protokol audio hasil audit T0] (Subbab 3.5); target regulator "500 sampai 800 mA" diganti uji bangku T0/G3 dengan [PERLU DATA: profil arus puncak, regulasi beban saat pengisian, kapasitas regulator] (Subbab 3.5); kapasitas baterai "2.500–3.000 mAh" pada Tabel 3.1 menjadi [PERLU DATA: kapasitas final dari uji arus]; strategi *pre-cache* 26 klip audio diganti opsi yang dievaluasi pada G3 (Subbab 3.5, Tabel 3.5 G3, Tabel 3.7 no. 17, Tabel 3.8 no. 8).
- Butir terlewat dilengkapi: catatan verifikasi pinout Tabel 3.3 (pin *strapping* GPIO 0, 3, 45, 46; jalur USB; kanal ADC1; konflik periferal I2C/I2S/SPI; revisi papan) pada unit fisik saat T0; daftar audit T0 ditambah panjang buffer CSI, laju paket hilang, RSSI dan *noise floor*, serta penanganan fase *callback* (Subbab 3.2); jumlah dan proporsi repetisi terpakai per kelas dan sesi pasca-pembuangan dicatat (Subbab 3.6); metode penyelarasan dan resampling keypoint ke pusat jendela CSI masuk daftar [PERLU DATA] sinkronisasi; uji pilot konfigurasi tangan, orientasi telapak, dan percobaan awal J/Z ditambahkan pada T0 dan Subbab 3.8.1; kerangka BOM pengadaan tanpa angka tebakan disisipkan setelah Tabel 3.1; prosa Persamaan (3.1) diselaraskan ke N~valid~.
- Keputusan kondisional dijaga: Pilihan 1 tetap preferensi teks yang menunggu konfirmasi (keterangan Gambar 3.5 kini menyebut Tabel 3.7 no. 19); MMS-TTS-ind tetap kandidat yang menunggu konfirmasi (Tabel 3.7 no. 17) tanpa membuang Kokoro sebagai pembanding; contoh angka di dalam penanda (misalnya "misalnya 20 ms") dipertahankan sebagai contoh, bukan keputusan.
- Yang tidak berubah: arsitektur dua arah, tiga mekanisme *firmware* RuView hasil gelombang 19, seluruh persamaan bernomor (33), Daftar Pustaka 33 entri, jadwal M1–M14, Batasan, dan kelompok keputusan terbuka Tabel 3.7.

"""

# Terapkan ke tubuh
for nama, lama, baru in suntingan:
    n = tubuh.count(lama)
    assert n == 1, f"{nama}: hitung {n}"
    tubuh = tubuh.replace(lama, baru)
    print(f"OK  {nama}")

# Sisipkan Log gelombang 20 sebelum Log gelombang 19 (di ekor, sesudah penanda)
jangkar_log = "## Log Perubahan — Revisi 14 November 2026, gelombang 19"
assert ekor.count(jangkar_log) == 1
ekor = ekor.replace(jangkar_log, log_baru + jangkar_log, 1)
print("OK  Log gelombang 20 disisipkan")

hasil = tubuh + MARK + ekor
DST.write_text(hasil, encoding="utf-8")
print("Tersimpan:", DST, len(hasil), "karakter")

# Pemeriksaan pasca-sunting pada tubuh
b = tubuh
cek_hilang = [
    "PCM 16-bit mono 16 kHz", "500 sampai 800 mA", "2.500–3.000 mAh",
    "di-*pre-cache* agar pemutaran tetap instan", "ditetapkan secara eksplisit sebelum G3",
    "seluruh 56 *subcarrier*:",
]
for c in cek_hilang:
    assert c not in b, f"MASIH ADA di tubuh: {c}"
print("Pemeriksaan tebakan hilang dari tubuh: OK")

cek_hadir = [
    "spesifikasi protokol audio hasil audit T0", "uji bangku T0 dan G3",
    "profil arus puncak terukur", "kanal ADC1", "I2C/I2S/SPI", "revisi papan",
    "panjang buffer CSI", "*noise floor*", "repetisi yang benar-benar dipakai per kelas dan per sesi",
    "resampling *keypoint* ke pusat jendela CSI", "konfigurasi jari dan orientasi telapak berbeda",
    "opsi pra-penyimpanan (*pre-cache*)", "Sumber Rujukan Harga", "N~valid~ hasil audit T0 (Subbab 2.2)",
    "menunggu konfirmasi Tabel 3.7 no. 19", "mengikuti keputusan Tabel 3.7 no. 17",
    "kandidat konfigurasi utama menunggu konfirmasi",
]
for c in cek_hadir:
    assert c in b, f"TIDAK ADA di tubuh: {c}"
print("Pemeriksaan konten baru hadir: OK")

# QC bahasa dasar pada teks BARU (gabungan semua 'baru'); judul Log memakai
# em dash mengikuti konvensi seluruh gelombang sebelumnya, jadi tidak ikut dicek.
import re
teks_baru = " ".join(baru for _, _, baru in suntingan) + log_baru.split("\n", 2)[2]
assert not re.search(r"\bbila\b", teks_baru), "kata 'bila' pada teks baru"
assert "—" not in teks_baru, "em dash pada teks baru"
assert ", sehingga" not in teks_baru, "koma-sebelum-sehingga pada teks baru"
assert not re.search(r"\bdi mana\b|\byang mana\b", teks_baru), "di mana/yang mana pada teks baru"
print("QC teks baru (bila/em dash/koma-sehingga/di mana): OK")
