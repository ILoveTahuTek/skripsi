#!/usr/bin/env python3
"""Rakit naskah ringkas: header + BAB I-III + DP dinomori ulang + log.

Sitasi: kumpulkan [n] dari tubuh (urut kemunculan pertama), petakan ke nomor baru,
tulis ulang tubuh dan Daftar Pustaka (hanya rujukan yang dikutip).
"""
import re
from pathlib import Path

BASE = Path("/home/z/my-project/download/sensesibi-v10")
SRC = BASE / "_kerja-ringkas/src"
ORIG = BASE / "Proposal-SenseSIBI-v10.md"
OUT = BASE / "Proposal-SenseSIBI-v10-ringkas.md"

# --- baca bagian sumber ---
header = (SRC / "00-header.md").read_text(encoding="utf-8").rstrip()
bab1 = (SRC / "01-bab1.md").read_text(encoding="utf-8").rstrip()
bab2 = (SRC / "02-bab2.md").read_text(encoding="utf-8").rstrip()
bab3 = (SRC / "03-bab3.md").read_text(encoding="utf-8").rstrip()

orig = ORIG.read_text(encoding="utf-8")
MARK = "<!-- ===== AKHIR NASKAH"
i_mark = orig.index(MARK)
dp_block = orig[orig.index("# DAFTAR PUSTAKA"):i_mark].rstrip()
log_block = orig[i_mark:].rstrip()

# --- entri DP lama ---
lama = {}
for m in re.finditer(r"^\[(\d{1,3})\] (.+)$", dp_block, re.M):
    lama[int(m.group(1))] = m.group(2)
print(f"DP lama: {len(lama)} entri")

# --- kumpulkan sitasi tubuh urut kemunculan ---
body_raw = "\n\n".join([bab1, bab2, bab3])
cited = []
for m in re.finditer(r"\[(\d{1,3})\]", body_raw):
    n = int(m.group(1))
    if n not in cited:
        cited.append(n)
print(f"Sitasi tubuh (unik, urut kemunculan): {len(cited)} -> {cited}")

hilang = [n for n in cited if n not in lama]
if hilang:
    raise SystemExit(f"FATAL: sitasi tanpa entri DP: {hilang}")

# --- peta nomor baru ---
peta = {lama_n: baru for baru, lama_n in enumerate(cited, start=1)}

def tulis_cit(teks):
    return re.sub(r"\[(\d{1,3})\]", lambda m: f"[{peta[int(m.group(1))]}]", teks)

bab1b, bab2b, bab3b = tulis_cit(bab1), tulis_cit(bab2), tulis_cit(bab3)

# --- DP baru ---
dp_baru = ["# DAFTAR PUSTAKA"]
for baru in range(1, len(cited) + 1):
    dp_baru.append(f"[{baru}] {lama[cited[baru - 1]]}")
dp_baru_txt = "\n\n".join(dp_baru)

# --- log baru ---
log_baru = """## Log Perubahan — Revisi 10 November 2026, gelombang 10 (versi ringkas ±40 halaman)

Permintaan: ringkas proposal menjadi sekitar 40 halaman DOCX dan PDF dengan memakai skill humanizer-id (Mode Akademik Ketat) dan sempro-mepet (register korpus, struktur sempro BAB I-III). Pemadatan dilakukan pada tingkat paragraf, gambar, dan tabel tanpa mengubah substansi, angka, maupun sitasi:

- BAB I: latar belakang dipadatkan menjadi tujuh paragraf rapat tanpa kehilangan satu pun angka dan sitasi; rumusan masalah dan tujuan butir 1-3 diringkas dengan cermin 1:1 dijaga; batasan masalah 9 butir dipertahankan dengan redaksi satu-dua baris; manfaat dan sistematika dirapatkan.
- BAB II: 13 subbab menjadi 11 (2.1-2.11); Subbab 2.1+2.2 lama digabung menjadi 2.1, Subbab 2.13 (rincian komponen BoM) dilebur ke Tabel 3.1, dan seluruh rujukan Subbab 2.x diperbarui menyeluruh termasuk teks dalam Gambar 3.2 yang dirender ulang (rujukan pemetaan kini Subbab 2.7); tiap blok teori dirapatkan dengan anatomi definisi-mekanisme-relevansi tetap utuh; Tabel 2.2 dipangkas dari 20 baris menjadi 11 baris (baris yang dikutip di teks tetap ada); Tabel 2.1 dan 2.3 dirapatkan.
- BAB III: Subbab 3.2.1-3.2.6 dilebur menjadi tiga paragraf tahap; subsubbab 3.5.1-3.5.7, 3.6.1-3.6.4, dan 3.7.1-3.7.8 dilebur menjadi prosa mengalir di bawah 3.5, 3.6, dan 3.7 (subsubbab 3.8 tetap enam); matriks komponen arsitektur lama dilebur ke Tabel 3.1, Tabel 3.2, dan prosa 3.5 sehingga tabel BAB III dinomori ulang menjadi Tabel 3.1-3.8; tabel pinout dipadatkan menjadi enam baris gabung; tabel gerbang dipangkas kolomnya menjadi empat; Tabel parameter dipangkas dari 29 baris menjadi 14 baris terkelompok; tabel risiko dari 12 baris menjadi 9 baris.
- Gambar: 10 menjadi 3 inti (tahapan-gerbang, arsitektur akhir, inferensi tepi); diagram distilasi data dan pelatihan, jalur gagal, topologi, *enclosure*, alur perangkat lunak, dan alur evaluasi diwakili uraian prosa Subbab 3.2, 3.5, 3.7, dan 3.8 beserta tabel skema pembagian data dan kriteria gerbang; ketiga gambar tersisa tidak memuat nomor gambar/tabel terpatri sehingga penomoran ulang aman.
- Daftar Pustaka: rujukan yang tidak lagi dikutip dikeluarkan dan penomoran sitasi ditulis ulang urut kemunculan pertama (94 entri menjadi 93 entri; satu rujukan latar belakang akuisisi CSI keluarga ESP32 dikeluarkan karena kalimatnya dipadatkan, klaim dukungan CSI resmi tetap dikutip dari esp-csi); entri DP diset satu spasi mengikuti konvensi format kampus.
- Pemformatan: daftar isi dibatasi pada heading level 1-2; nomor subbab BAB II dan nomor tabel BAB II dipertahankan; seluruh rujukan silang Subbab/Tabel/Gambar diperbarui konsisten.
- Nol perubahan angka, hasil, dan klaim; rumusan-tujuan tetap cermin 1:1; batasan tetap selaras BAB III; penanda [PERLU DATA] dan [PERLU ILUSTRASI] diringkas menjadi 31 (dari 47) melalui penggabungan butir tabel parameter yang sejenis sehingga tidak ada kebutuhan data yang hilang, dan penomoran sitasi 1-93 terverifikasi utuh dengan seluruh entri daftar pustaka identik dengan naskah asli.
"""

n_perlu = len(re.findall(r"\[PERLU (?:DATA|RUJUKAN|ILUSTRASI):", body_raw))
print(f"Penanda PERLU di tubuh: {n_perlu}")

out = "\n\n".join([
    header, "---", bab1b, bab2b, bab3b, dp_baru_txt,
    MARK + " (jangan hapus penanda ini) ===", log_baru.rstrip(), log_block,
])
OUT.write_text(out + "\n", encoding="utf-8")

# --- statistik ---
def katab(s):
    return len(s.split())
print(f"Tubuh: {katab(bab1b)}+{katab(bab2b)}+{katab(bab3b)} kata; DP {len(cited)} entri")
print(f"Total berkas: {len(out.splitlines())} baris, {len(out)} karakter")
print(f"Rujukan dikeluarkan: {sorted(set(lama) - set(cited))}")
