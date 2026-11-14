#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Verifikasi gelombang 20 (v19 -> v20) terhadap ledger 25 isu + invariant gelombang 19."""
import re
import sys
from pathlib import Path

V10 = Path("/home/z/my-project/download/sensesibi-v10")
md = (V10 / "Proposal-SenseSIBI-v20.md").read_text(encoding="utf-8")
MARK = "<!-- ===== AKHIR NASKAH"
tubuh = md[: md.index(MARK)]
log = md[md.index(MARK):]

ok = 0
gagal = []

def cek(nama, kondisi):
    global ok
    if kondisi:
        ok += 1
    else:
        gagal.append(nama)
        print("GAGAL:", nama)

# === A. Tebakan hilang dari tubuh (disiplin penanda terbuka) ===
for c in [
    "PCM 16-bit mono 16 kHz", "PCM 16-bit", "500 sampai 800 mA", "500-800 mA",
    "2.500–3.000 mAh", "di-*pre-cache* agar pemutaran tetap instan",
    "ditetapkan secara eksplisit sebelum G3", "yaitu rata-rata besar perubahan koefisien kanal kompleks antarbingkai pada seluruh 56",
]:
    cek(f"A tebakan hilang: {c[:40]}", c not in tubuh)

# === B. Konten baru gelombang 20 ===
for c in [
    "(a) verifikasi koeksistensi", "(b) penetapan format audio", "(c) sinkronisasi penanda waktu antarmodul dan server",
    "(d) dampak beban lalu lintas audio", "[PERLU DATA: spesifikasi protokol audio hasil audit T0]",
    "uji bangku T0 dan G3", "[PERLU DATA: profil arus puncak terukur, regulasi beban saat pengisian, dan kapasitas regulator terpilih]",
    "dengan cakupan yang dirinci pada catatan Tabel 3.3",
    "Seluruh baris Tabel 3.3 wajib diverifikasi ulang pada unit papan fisik",
    "pin *strapping* (GPIO 0, 3, 45, 46), jalur USB, kemampuan kanal ADC1, potensi konflik periferal I2C/I2S/SPI, dan revisi papan",
    "opsi pra-penyimpanan (*pre-cache*) klip audio 26 huruf dievaluasi pada G3",
    "[PERLU DATA: keputusan opsi *pre-cache* dan hasil uji bandingnya terhadap sintesis langsung]",
    "metode penyelarasan dan resampling *keypoint* ke pusat jendela CSI",
    "repetisi yang benar-benar dipakai per kelas dan per sesi setelah pembuangan",
    "laju paket hilang, panjang buffer CSI, RSSI dan *noise floor*, dan penanganan fase pada *callback*",
    "konfigurasi jari dan orientasi telapak berbeda, termasuk percobaan awal huruf dinamis J dan Z",
    "ditambah uji pilot beberapa konfigurasi tangan statis yang berbeda, orientasi telapak yang berbeda, serta percobaan awal huruf J dan Z",
    "mengikuti keputusan Tabel 3.7 no. 17 (kandidat default MMS-TTS-ind ONNX dengan opsi *pre-cache* 26 huruf tunggal)",
    "dengan opsi *pre-cache* 26 huruf), lokasi sintesis D3",
    "kandidat konfigurasi utama menunggu konfirmasi, lalu cadangan server lokal",
    "(aktivasi kepala regresi Pilihan 2 menunggu konfirmasi Tabel 3.7 no. 19)",
    "Li-Po 3,7 V [PERLU DATA: kapasitas final ditetapkan dari uji arus T0 dan G3]",
    "Sumber Rujukan Harga", "Sepasang node antarmuka lengkap (di luar laptop, ponsel, dan *access point*)",
    "N~valid~ hasil audit T0 (Subbab 2.2):",
]:
    cek(f"B konten baru: {c[:50]}", c in tubuh)

# === C. Keadaan akhir ledger 25 isu (hasil gelombang 18/19 tetap utuh) ===
cek("C01 ISS-01 trainable", "tetapan yang diperbarui mencakup adapter masukan (jika dipakai), modul temporal, dan kedua kepala" in tubuh)
cek("C02 ISS-02 Jalur B1/B2", "Jalur B1 (adapter rekonstruksi fitur)" in tubuh and "Jalur B2 (adapter terpandu tugas)" in tubuh)
cek("C03 ISS-02 Pembanding C", "Pembanding C" in tubuh and "Pembanding C" in (V10 / "_kerja-g20/split/bab3-metodologi.md").read_text(encoding="utf-8"))
cek("C04 ISS-03 audit artefak", "NUL-padding" in tubuh and "32,97%" in tubuh and "sendi distal" in tubuh)
cek("C05 ISS-04 overlap", "3,75 detik" in tubuh and "4,75 detik" in tubuh and "75%" in tubuh)
cek("C06 ISS-05 interpolasi", "tidak menciptakan informasi temporal baru" in tubuh)
cek("C07 ISS-06 pose-hold", "pose-hold window" in tubuh and "tahan pose" in tubuh)
cek("C08 ISS-08 mask 2.13a", "(2.13a)" in tubuh and "m∗~itj~" in tubuh)
cek("C09 ISS-09 kosinis", "2.14a" in tubuh)
cek("C10 ISS-10 permutasi", "p~perm~" in tubuh and "1.000 iterasi" in tubuh)
cek("C11 ISS-11 purge gap", "purge gap" in tubuh)
cek("C12 ISS-12 first_word_invalid", "first_word_invalid" in tubuh and "LLTF" in tubuh)
cek("C13 ISS-13 no19 KONFIRMASI", re.search(r"\| 19 \|.*PERLU KONFIRMASI", tubuh) is not None)
cek("C14 ISS-14 pustaka baru", "DF-WiSLR" in tubuh and "Wi-SignFi" in tubuh and "Permenristekdikti" in tubuh)
cek("C15 ISS-15 Kokoro jujur", "tidak tersedianya suara bahasa Indonesia" in tubuh and "Kokoro-82M ONNX tetap disiapkan sebagai pembanding" in tubuh)
cek("C16 ISS-16 WER", "1 − WER" in tubuh)  # hadir sebagai larangan eksplisit
cek("C17 ISS-17 latensi a/b", "(3.3a)" in tubuh and "(3.3b)" in tubuh)
cek("C18 ISS-18 biaya", "Rp350.000" not in tubuh and "Rp300.000" in tubuh)
cek("C20 ISS-20 keypoint J/Z", "detection rate" in tubuh and "diacak di dalam setiap blok" in tubuh)
cek("C21 ISS-21 etika", "child assent" in tubuh and "identifikasi ulang" in tubuh)
cek("C22 ISS-22 feasibility", "kelayakan ilmiah awal" in tubuh and "cakupan diterima" in tubuh and "MobileNetV2-0.5" in tubuh)
cek("C23 ISS-23 G0b jadwal", "G0b (awal T2 / M4)" in tubuh)
cek("C24 ISS-24/25 typo", all(x not in tubuh for x in ["kehati-hatianya", "Paramete/r", "Jumla/h", "1 − WER karena"]))
# Invariant gelombang 19 (ESP-NOW)
cek("C25 v19 beacon hilang", "Beacon ESP-NOW" not in tubuh and "pemancar beacon" not in tubuh and "beacon" not in tubuh)
cek("C26 v19 NDP/UDP", "injeksi NDP" in tubuh and "ADR-018" in tubuh)
cek("C27 v19 no21 ESP-NOW", re.search(r"\| 21 \|.*ESP-NOW dikeluarkan dari jalur inti", tubuh) is not None)
cek("C28 v19 G0 pin firmware", "Versi atau komit *firmware* RuView dikunci" in tubuh)
cek("C29 v19 instalasi bukan akurasi", "instalasi" not in tubuh or "bukan bukti" in tubuh or "bukan asumsi" in tubuh)

# === D. Penanda dan struktur naskah ===
pd_ = len(re.findall(r"\[PERLU DATA:", tubuh))
pv = len(re.findall(r"\[PERLU VALIDASI:", tubuh))
pk = len(re.findall(r"\[PERLU KONFIRMASI:", tubuh))
cek("D1 PERLU DATA = 38 (v19 35 + 3 baru)", pd_ == 38)
cek("D2 PERLU VALIDASI = 10", pv == 10)
cek("D3 PERLU KONFIRMASI = 2", pk == 2)
cek("D4 DP 33 entri", len(re.findall(r"^\[(\d+)\]", md[md.index("# DAFTAR PUSTAKA"):], re.M)) == 33)
cek("D5 Log gel 20", "gelombang 20" in log)
cek("D6 Log gel 19 utuh", "gelombang 19" in log)

# === E. QC bahasa tubuh (sempro-mepet) ===
cek("E1 bila = 0", re.search(r"\bbila\b", tubuh) is None)
cek("E2 di mana/yang mana = 0", re.search(r"\bdi mana\b|\byang mana\b", tubuh) is None)
# em dash di luar baris tabel (penanda jadwal "—" pada Tabel 3.6 adalah konvensi warisan)
prosa_tanpa_tabel = "\n".join(l for l in tubuh.split("\n") if not l.lstrip().startswith("|"))
cek("E3 em dash prose = 0", " — " not in prosa_tanpa_tabel)
koma_sehingga = len(re.findall(r", sehingga", tubuh))
cek("E4 koma-sehingga <= 10", koma_sehingga <= 10)
tak_baku = ["dikarenakan", "dimana", "krn", "dgn", "utk", "tsb", "yg ", "gak ", "nggak", "bikin "]
cek("E5 kata tak baku", not any(t in tubuh.lower() for t in tak_baku))
cek("E6 'signifikan' berpasangan uji", all(("uji" in tubuh[max(0, m.start() - 200):m.start() + 200] or "permutasi" in tubuh[max(0, m.start() - 200):m.start() + 200]) for m in re.finditer(r"\bsignifikan\b", tubuh)))

# === F. Struktur DOCX via python-docx ===
from docx import Document
doc = Document(str(V10 / "Proposal-SenseSIBI-Studi-Kelayakan-v20.docx"))
h1 = sum(1 for p in doc.paragraphs if p.style.name == "Heading 1")
h2 = sum(1 for p in doc.paragraphs if p.style.name == "Heading 2")
h3 = sum(1 for p in doc.paragraphs if p.style.name == "Heading 3")
# tiap persamaan dirender sebagai tabel 1x3; tabel konten = >=5 baris
konten = [t for t in doc.tables if len(t.rows) >= 5]
tabel = len(konten)
gambar = sum(1 for s in doc.inline_shapes)
cek("F1 H1=4", h1 == 4)
cek("F2 H2=34", h2 == 34)
cek("F3 H3=8", h3 == 8)
cek("F4 tabel konten=13", tabel == 13)
cek("F5 gambar=7", gambar == 7)

# Tabel BOM: header dan sel terisi
bom = None
for t in doc.tables:
    hdr = [c.text.strip() for c in t.rows[0].cells]
    if "Sumber Rujukan Harga" in hdr:
        bom = t
        break
cek("F6 tabel BOM ada", bom is not None)
if bom is not None:
    cek("F7 BOM 8 baris data", len(bom.rows) == 9)
    kosong = sum(1 for r in bom.rows for c in r.cells if not c.text.strip())
    cek("F8 BOM tanpa sel kosong", kosong == 0)

# Teks docx memuat konten baru dan bebas tebakan
full = "\n".join(p.text for p in doc.paragraphs) + "\n" + "\n".join(c.text for t in doc.tables for r in t.rows for c in r.cells)
cek("F9 docx: protokol audio terbuka", "spesifikasi protokol audio hasil audit T0" in full)
cek("F10 docx: tebakan hilang", all(x not in full for x in ["PCM 16-bit", "500 sampai 800 mA", "2.500–3.000 mAh"]))
cek("F11 docx: tanpa placeholder liar", all(x not in full for x in ["TODO", "XXX", "undefined", "NaN", "【"]))

print(f"\nHasil: {ok} OK, {len(gagal)} GAGAL")
if gagal:
    print("Butir gagal:", gagal)
    sys.exit(1)
print("VERIFIKASI G20 LULUS SEMUA")
