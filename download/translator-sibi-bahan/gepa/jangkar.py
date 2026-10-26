# -*- coding: utf-8 -*-
"""Kontrak jangkar & klaim terlarang untuk dossier bahan Translator SIBI.

Jangkar = fakta/istilah kunci yang WAJIB bertahan pada tiap komponen saat
dimutasi GEPA. Pencocokan memakai normalisasi (en-dash -> hyfen, spasi rapat,
huruf kecil) supaya rephrasing yang sah tidak dihukum.

Sumber semua jangkar: Matriks-Literatur-dan-Bukti.md + Proposal-Revisi-Translator-SIBI.md
(Task 17, 25 Okt 2026) + Audit-Arsitektur-Translator-SIBI.md. Tidak ada
jangkar yang tidak bisa dilacak ke sana.
"""

import re

_KATA_NEGASI = ("tidak", "bukan", "tanpa", "jangan", "di luar", "menolak", "meniadakan")


def normalisasi(teks: str) -> str:
    """Normalisasi ringan agar pencocokan jangkar tahan rephrasing."""
    t = teks.lower()
    t = t.replace("\u2013", "-").replace("\u2014", "-").replace("\u2011", "-")
    t = t.replace("\u00a0", " ")
    t = re.sub(r"\s+", " ", t)
    return t


# ----------------------------------------------------------------------------
# Jangkar wajib per komponen (dicocokkan pada teks ternormalisasi)
# ----------------------------------------------------------------------------
JANGKAR = {
    "ringkasan": [
        "dua arah", "esp32-s3", "yolo26", "mms-tts-ind", "faster-whisper",
        "kokoro", "wisign", "purwarupa", "kosakata terbatas",
        "5-8 isyarat", "gerbang", "77,7", "1,9", "inferensi",
    ],
    "arah_latar": [
        "mitchell", "karchmer", "90-95", "1,92 juta", "3.840",
        "77,7", "1,9", "91%", "uu nomor 8 tahun 2016",
        "signfi", "276", "wisign", "bailenson", "kasibi", "opensibi",
        "tunarungu", "pendengar", "validator",
    ],
    "peta_masalah": [
        "12,5 cm", "1t1r", "intel 5300", "50 bingkai", "120 hz",
        "wifi_ps_none", "mgmt", "54 ms", "69,2 ms", "293,5 kb",
        "overfit", "ejaan jari", "doppler", "subcarrier",
        "t0", "g3", "validator",
    ],
    "konsep_alat": [
        "terima kasih", "ejaan jari", "validator", "purwarupa",
        "kosakata terbatas", "juru bahasa", "dataset", "g4",
        "layar", "speaker", "mikrofon", "dua arah",
    ],
    "kit_bab1": [
        "bagaimana", "merancang", "mengukur", "menguji", "perlu data",
        "gambar 1.1", "gambar 1.2", "mitchell", "batasan", "manfaat",
        "sistematika", "rumusan", "tujuan",
    ],
    "kit_bab23": [
        "t0", "t5", "g0", "g4", "menyiapkan", "collect-ground-truth",
        "30 repetisi", "confusion matrix", "latensi", "cakupan kamus",
        "penyaringan", "keypoint", "gerbang", "menganalisis",
    ],
    "sidang": [
        "77,7", "1,9", "wisign", "12,5", "kokoro", "juru bahasa",
        "yolo26", "baterai", "sibi", "menggantikan", "laptop",
    ],
    "keputusan": [
        "perlu data", "validator", "g0", "pembimbing", "dua ruang",
        "kanal", "tts", "asr", "senin", "mitra",
    ],
}

# Jumlah minimal penanda [PERLU DATA per komponen — penanda adalah keputusan
# manusia dan tidak boleh dihapus diam-diam oleh mutasi.
PENANDA_MIN = {
    "ringkasan": 0,
    "arah_latar": 0,
    "peta_masalah": 0,
    "konsep_alat": 1,
    "kit_bab1": 2,
    "kit_bab23": 2,
    "sidang": 0,
    "keputusan": 6,
}

# Panjang minimal komponen (karakter) — mencegah mutasi yang menipiskan isi.
PANJANG_MIN = {
    "ringkasan": 1800,
    "arah_latar": 2600,
    "peta_masalah": 2600,
    "konsep_alat": 2200,
    "kit_bab1": 2600,
    "kit_bab23": 3200,
    "sidang": 2600,
    "keputusan": 1500,
}

# ----------------------------------------------------------------------------
# Klaim terlarang — sah hanya bila ternegasi (kata negasi pada jendela 60
# karakter kiri/kanan) atau, pada komponen sidang, muncul sebagai pertanyaan
# penguji (tanda "?" dalam 40 karakter setelahnya).
# ----------------------------------------------------------------------------
_KLAIM_TERLARANG = [
    ("penerjemah kalimat", "klaim penerjemah kalimat penuh tanpa negasi"),
    ("penerjemahan kontinu", "klaim penerjemahan kontinu tanpa negasi (batas WiSign)"),
    ("pengenalan isyarat kontinu", "klaim pengenalan isyarat kontinu tanpa negasi"),
    ("bentuk jari", "klaim bentuk jari dari CSI tanpa negasi"),
    ("konfigurasi jari", "klaim konfigurasi jari tanpa negasi"),
    ("ekspresi wajah", "klaim ekspresi wajah tanpa negasi"),
    ("menggantikan juru bahasa", "klaim menggantikan juru bahasa tanpa negasi"),
    ("meningkatkan empati", "klaim meningkatkan empati sebagai hasil tanpa negasi"),
    ("akurasi dijamin", "janji akurasi"),
]

# Frasa terlarang mutlak: pola AI + ejaan tidak baku + angka tak layak kutip.
_FRASA_MUTLAK = [
    "di era digital", "seiring perkembangan zaman", "seiring dengan perkembangan",
    "tidak dapat dipungkiri", "sudah menjadi rahasia umum",
    "perlu diingat", "mari kita", "memainkan peran", "memainkan peranan",
    "adalah merupakan", "agar supaya", "sangat penting sekali",
    "menggunakkan", "di hadapi", "di tunjukkan", "yang mana",
    "merubah", "resiko", "praktek", "analisa", "sistim", "aktifitas",
    "kwalitas", "frekwensi", "prosentase", "standarisasi",
    "2.600 kosakata", "2600 kosakata",
]

# Batas kemunculan per komponen (teks ternormalisasi).
BATAS_KEMUNCULAN = {
    "hal ini": 1,
    "selain itu,": 3,
    "oleh karena itu,": 3,
    "di mana": 1,
    "secara keseluruhan": 0,
}


def _ternegasi(t: str, awal: int, akhir: int) -> bool:
    """True bila ada kata negasi pada jendela di sekitar kecocokan."""
    kiri = t[max(0, awal - 60):awal]
    kanan = t[akhir:akhir + 60]
    for n in _KATA_NEGASI:
        if n in kiri or n in kanan:
            return True
    return False


def periksa_klaim_terlarang(teks: str, komponen: str) -> list:
    """Kembalikan daftar pelanggaran klaim terlarang pada satu komponen."""
    t = normalisasi(teks)
    pelanggaran = []
    for frasa, alasan in _KLAIM_TERLARANG:
        f = normalisasi(frasa)
        pos = 0
        while True:
            i = t.find(f, pos)
            if i < 0:
                break
            pos = i + len(f)
            jendela_kanan = t[i + len(f):i + len(f) + 40]
            if komponen == "sidang" and "?" in jendela_kanan:
                continue  # pertanyaan penguji yang sah
            if _ternegasi(t, i, i + len(f)):
                continue  # ternegasi -> sah
            kutip = t[max(0, i - 30):i + len(f) + 30]
            pelanggaran.append(f"[{komponen}] {alasan}: ...{kutip}...")
    for frasa in _FRASA_MUTLAK:
        if frasa in t:
            pelanggaran.append(f"[{komponen}] frasa terlarang mutlak: '{frasa}'")
    for frasa, batas in BATAS_KEMUNCULAN.items():
        n = t.count(frasa)
        if n > batas:
            pelanggaran.append(f"[{komponen}] '{frasa}' muncul {n}x (batas {batas})")
    return pelanggaran


def periksa_jangkar(teks: str, komponen: str) -> list:
    """Kembalikan daftar jangkar yang hilang pada satu komponen."""
    t = normalisasi(teks)
    return [j for j in JANGKAR.get(komponen, []) if normalisasi(j) not in t]


def periksa_komponen(nama: str, teks: str) -> dict:
    """Seluruh cek objektif untuk satu komponen."""
    hasil = {
        "jangkar_hilang": periksa_jangkar(teks, nama),
        "pelanggaran": periksa_klaim_terlarang(teks, nama),
        "n_penanda": teks.count("[PERLU DATA"),
        "panjang": len(teks),
    }
    masalah = []
    if hasil["jangkar_hilang"]:
        masalah.append("jangkar hilang: " + ", ".join(hasil["jangkar_hilang"]))
    masalah.extend(hasil["pelanggaran"])
    if hasil["n_penanda"] < PENANDA_MIN.get(nama, 0):
        masalah.append(
            f"penanda [PERLU DATA] tinggal {hasil['n_penanda']} "
            f"(minimal {PENANDA_MIN[nama]}) - keputusan manusia tidak boleh dihapus diam-diam"
        )
    if hasil["panjang"] < PANJANG_MIN.get(nama, 0):
        masalah.append(
            f"komponen terlalu pendek ({hasil['panjang']} < {PANJANG_MIN[nama]} karakter)"
        )
    hasil["masalah"] = masalah
    return hasil


KOMPONEN_UTAMA = [
    "ringkasan", "arah_latar", "peta_masalah", "konsep_alat",
    "kit_bab1", "kit_bab23", "sidang", "keputusan",
]
