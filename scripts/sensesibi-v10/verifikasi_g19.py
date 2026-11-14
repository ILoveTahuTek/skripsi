#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Verifikasi isi v19: koreksi mekanisme akuisisi CSI RuView."""
from docx import Document
from pathlib import Path
import re, sys

DOCX = Path("/home/z/my-project/download/sensesibi-v10/Proposal-SenseSIBI-Studi-Kelayakan-v19.docx")
doc = Document(str(DOCX))

# kumpulkan seluruh teks (paragraf + sel tabel)
paras = [p.text for p in doc.paragraphs]
teks = "\n".join(paras)
ntabel = 0
for t in doc.tables:
    ntabel += 1
    for r in t.rows:
        for c in r.cells:
            teks += "\n" + c.text

def cek(nama, frasa, n=1):
    hitung = teks.count(frasa)
    status = "OK" if hitung >= n else "HILANG"
    print(f"[{status}] {nama}: {hitung}x")
    return hitung >= n

ok = True
def C(nama, frasa, n=1):
    global ok
    if not cek(nama, frasa, n): ok = False

# --- inti koreksi mekanisme ---
C("2.3 pemisahan tiga mekanisme", "Peran tiga mekanisme radio pada firmware RuView dibedakan")
C("2.3 injeksi NDP + callback CSI", "injeksi NDP (Null Data Packet) beserta callback CSI")
C("2.3 ADR-018", "format biner ADR-018")
C("2.3 ESP-NOW opsional", "hanya muncul sebagai sinkronisasi mesh opsional pada implementasi tertentu")
C("2.3 tidak prasyarat", "tidak menjadikan ESP-NOW prasyarat akuisisi CSI")
C("2.3 mesh 3-6 node TDM", "mesh multistatik dengan tiga sampai enam node")
C("2.3 instalasi bukan bukti", "belum membuktikan akurasi penginderaan maupun kestabilan jangka panjang")
C("2.3 G0 wajib versi/komit", "versi atau komit firmware dikunci dan dicatat")
C("2.3 G0 dua node tanpa ESP-NOW", "konfigurasi dua node dijalankan tanpa implementasi ESP-NOW tambahan")
C("Tabel 2.1 baris mekanisme baru", "Station Wi-Fi + callback CSI + injeksi NDP + UDP pada satu chip; ESP-NOW hanya sinkronisasi mesh opsional")
C("Tabel 2.1 baris firmware ADR-018", "Mengalirkan bingkai CSI mentah saat akuisisi")
C("2.13 UDP + penanda waktu terpisah", "ditangani lewat penanda waktu yang diuji terpisah")
C("2.13 ESP-NOW opsional", "hanya dipakai sebagai jalur sinkronisasi mesh opsional jika konfigurasi node memerlukannya")
C("3.4 TX suntik NDP", "TX menyuntikkan bingkai sounding NDP")
C("3.4 versi/komit firmware dicatat", "versi atau komit firmware RuView serta perangkat lunak lain dicatat")
C("Tabel 3.1 node TX baru", "pemancar bingkai sounding NDP")
C("3.5 bingkai sounding NDP melintasi", "bingkai sounding NDP yang disuntikkan node pemancar melintasi zona isyarat")
C("3.5 topologi baru", "mengirim bingkai CSI mentah saat akuisisi serta label dan skor saat deployment")
C("3.7 bingkai hasil callback", "Bingkai hasil callback CSI masuk ke penyangga geser")
C("Batasan no. 12", "Akuisisi CSI mengikuti mekanisme bawaan firmware RuView")
C("Tabel 3.5 G0 kriteria firmware", "Versi atau komit firmware RuView dikunci dan tercatat")
C("Tabel 3.5 G0 dua node", "konfigurasi dua node peran tetap terverifikasi berjalan tanpa implementasi ESP-NOW tambahan")
C("Tabel 3.5 G0 NDP+UDP bersamaan", "terbaca stabil saat injeksi NDP dan pengiriman UDP berjalan bersamaan")
C("3.10 kelompok teknis + baris 21", "baris 2 sampai 12, 15, 18, dan 21")
C("Tabel 3.7 baris 21", "Peran ESP-NOW dan konfigurasi node akuisisi CSI")
C("Tabel 3.7 baris 21 keputusan", "Keputusan pemilik 14 Nov 2026 atas audit dokumentasi firmware RuView")
C("Tabel 3.8 baris 13", "Konfigurasi dua node peran tetap tidak terverifikasi pada firmware RuView yang dipakai")
C("DP [32]", "[32] ruvnet, \u201cESP32 CSI Node Firmware,\u201d", 1) if "\u201c" in teks else C("DP [32]", "[32] ruvnet")
C("DP [32] URL", "github.com/ruvnet/RuView/blob/main/firmware/esp32-csi-node/README.md")
C("DP [33] URL", "github.com/ruvnet/RuView/blob/main/docs/user-guide.md")

# --- tidak ada sisa keliru ---
def N(nama, frasa):
    global ok
    hitung = teks.count(frasa)
    status = "OK" if hitung == 0 else "MASIH ADA"
    print(f"[{status}] {nama}: {hitung}x")
    if hitung: ok = False

N("sisa 'beacon ESP-NOW'", "beacon ESP-NOW")
N("sisa 'Station + UDP + CSI promiscuous'", "Station + UDP + CSI promiscuous")
N("sisa 'sinkronisasi ESP-NOW secara serentak'", "sinkronisasi ESP-NOW secara serentak")
N("sisa 'pemancar beacon'", "pemancar beacon")
N("sisa kata beacon di tubuh", "beacon")

# --- struktur ---
h1 = sum(1 for p in doc.paragraphs if p.style.name == "Heading 1")
h2 = sum(1 for p in doc.paragraphs if p.style.name == "Heading 2")
h3 = sum(1 for p in doc.paragraphs if p.style.name == "Heading 3")
gambar = sum(1 for r in doc.part.rels.values() if "image" in r.reltype)
print(f"\nstruktur: H1={h1} H2={h2} H3={h3} tabel={ntabel} gambar={gambar}")
print("identitas versi:", "33 rujukan" in teks)

# --- QC bahasa prosa baru ---
tubuh_md = Path("/home/z/my-project/download/sensesibi-v10/Proposal-SenseSIBI-v19.md").read_text(encoding="utf-8")
tubuh = tubuh_md[:tubuh_md.index("<!-- ===== AKHIR NASKAH")]
blok_baru = tubuh[tubuh.index("Peran tiga mekanisme radio"):tubuh.index("## 2.4")]
masalah = []
if re.search(r"\bbila\b", blok_baru): masalah.append("bila")
if "—" in blok_baru: masalah.append("em dash")
if ", sehingga" in blok_baru: masalah.append("koma-sebelum-sehingga")
if re.search(r"\bhal ini\b|\byang mana\b", blok_baru): masalah.append("pola AI")
print("QC prosa baru:", "BERSIH" if not masalah else f"MASALAH {masalah}")
if masalah: ok = False

# koma-sebelum-sehingga total (warisan v18 = 10, tidak boleh bertambah)
koma_sehingga = len(re.findall(r",\s+sehingga", tubuh))
print(f"koma-sebelum-sehingga total (warisan diperiksa terpisah): {koma_sehingga}")

print("\nHASIL:", "LOLOS" if ok else "GAGAL")
sys.exit(0 if ok else 1)
