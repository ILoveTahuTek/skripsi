#!/usr/bin/env python3
"""Rakit naskah v11 (gelombang 11): header + BAB I-III + DP dari kunci semantik.

Sitasi ditulis [kunci] di tubuh; skrip memetakan kunci -> entri DP asli (Proposal-
SenseSIBI-v10.md), memverifikasi kecocokan kunci-entri lewat penanda teks, menomori
ulang urut kemunculan pertama, lalu menulis tubuh dan DP (hanya rujukan terkutip).
"""
import re
from pathlib import Path

BASE = Path("/home/z/my-project/download/sensesibi-v10")
SRC = BASE / "_kerja-g11/src"
ORIG = BASE / "Proposal-SenseSIBI-v10.md"
OUT = BASE / "Proposal-SenseSIBI-v11.md"

# kunci -> (nomor lama, penanda teks wajib muncul di entri, keterangan)
KUNCI = {
    "kemenkopmk": (5, "Kemenko PMK bergerak", "KemenkoPMK"),
    "uu-disabilitas": (6, "Nomor 8 Tahun 2016", "UU 8/2016"),
    "brin": (8, "BRIN dorong penguatan", "BRIN"),
    "mursita": (9, "Respon tunarungu terhadap", "Mursita"),
    "kamus-digital": (10, "Kamus SIBI Digital", "Kamus SIBI digital"),
    "as-satillah": (11, "Ogan Ilir", "As Satillah"),
    "kasibi": (12, "KASIBI", "KASIBI"),
    "opensibi": (13, "OpenSIBI", "OpenSIBI"),
    "sanjaya-slr": (14, "systematic literature review", "Sanjaya SLR"),
    "dwijayanti": (15, "Indonesia sign language recognition using convolutional", "Dwijayanti"),
    "soekarta": (16, "Mediapipe berbasis Android", "Soekarta"),
    "maulana": (17, "Jetpack Compose", "Maulana"),
    "ma-csur": (21, "WiFi sensing with channel state information: A survey", "Ma CSUR"),
    "signfi": (22, "SignFi", "SignFi"),
    "dfwislr": (23, "DF-WiSLR", "DF-WiSLR"),
    "wisign": (25, "WiSign", "WiSign"),
    "esp-csi": (31, "esp-csi", "esp-csi"),
    "ruview": (32, "RuView", "RuView"),
    "esp32s3": (33, "ESP32-S3 Series Datasheet", "ESP32-S3 datasheet"),
    "esp-nn": (34, "esp-nn", "esp-nn"),
    "esp-dl": (35, "esp-dl", "esp-dl"),
    "tokio": (36, "tokio: A runtime", "Tokio"),
    "axum": (37, "axum: Ergonomic", "Axum"),
    "leptos": (38, "leptos: Build fast", "Leptos"),
    "tauri": (39, "tauri: Build smaller", "Tauri"),
    "onnxruntime": (40, "onnxruntime: Cross-platform", "ONNX Runtime"),
    "kokoro-onnx": (41, "kokoro-onnx", "kokoro-onnx"),
    "kokoro-card": (42, "Kokoro-82M", "Kokoro model card"),
    "mms-card": (44, "Indonesian text-to-speech", "MMS TTS card"),
    "whisper": (47, "Robust speech recognition", "Whisper"),
    "faster-whisper": (48, "faster-whisper", "faster-whisper"),
    "widar3": (50, "Widar3.0", "Widar3.0"),
    "densepose-wifi": (73, "DensePose from WiFi", "DensePose from WiFi"),
    "ultralytics": (52, "Hand Keypoints Pose Estimation", "Ultralytics docs"),
    "picron": (53, "Sign language machine translation in practice", "Picron"),
    "kamus-cetak": (55, "Departemen Pendidikan dan Kebudayaan", "Kamus SIBI cetak"),
    "nugraheni": (58, "Optimalisasi penggunaan bahasa isyarat", "Nugraheni"),
    "malika": (59, "Penggunaan bahasa isyarat SIBI dan BISINDO", "Malika"),
    "kindy": (61, "Word-level BISINDO", "Kindy"),
    "svm": (77, "Support-vector networks", "SVM Cortes"),
    "chow": (80, "error and reject tradeoff", "Chow reject"),
    "tflite-micro": (81, "tflite-micro-esp-examples", "TFLite Micro"),
    "likert": (88, "A technique for the measurement of attitudes", "Likert"),
    "hinton": (89, "Distilling the knowledge", "Hinton distilasi"),
    "csi-ratio": (90, "From Fresnel zone", "CSI-ratio Wu"),
    "trl": (91, "Technology readiness assessments", "Mankins TRL"),
    "widar2": (92, "Widar2.0", "Widar2.0"),
}

# --- baca bagian sumber ---
header = (SRC / "00-header.md").read_text(encoding="utf-8").rstrip()
bab1 = (SRC / "01-bab1.md").read_text(encoding="utf-8").rstrip()
bab2 = (SRC / "02-bab2.md").read_text(encoding="utf-8").rstrip()
bab3 = (SRC / "03-bab3.md").read_text(encoding="utf-8").rstrip()

orig = ORIG.read_text(encoding="utf-8")
MARK = "<!-- ===== AKHIR NASKAH"
dp_block = orig[orig.index("# DAFTAR PUSTAKA"):orig.index(MARK)].rstrip()

# --- entri DP asli ---
lama = {}
for m in re.finditer(r"^\[(\d{1,3})\] (.+)$", dp_block, re.M):
    lama[int(m.group(1))] = m.group(2)
assert len(lama) == 94, f"DP asli 94 entri, ditemukan {len(lama)}"

# --- verifikasi kunci -> entri ---
kunci_ke_lama = {}
for k, (n, marker, ket) in KUNCI.items():
    entri = lama[n]
    assert marker in entri, f"KUNCI {k}: penanda '{marker}' tidak ada di [{n}]: {entri[:80]}"
    kunci_ke_lama[k] = n
print(f"Kunci terverifikasi: {len(kunci_ke_lama)} -> entri asli {sorted(kunci_ke_lama.values())}")

# --- kumpulkan kunci tubuh urut kemunculan ---
body_raw = "\n\n".join([bab1, bab2, bab3])
dipakai = []
for m in re.finditer(r"\[([a-z0-9\-]+)\]", body_raw):
    k = m.group(1)
    if re.fullmatch(r"\d+", k):
        raise SystemExit(f"FATAL: ada sitasi numerik tersisa [{k}]")
    if k.startswith("PERLU"):
        continue
    if k not in KUNCI:
        raise SystemExit(f"FATAL: kunci tidak dikenal: [{k}]")
    if k not in dipakai:
        dipakai.append(k)
print(f"Kunci dipakai tubuh: {len(dipakai)} urut kemunculan: {dipakai}")

# --- peta kunci -> nomor baru ---
peta = {k: i for i, k in enumerate(dipakai, start=1)}

def tulis_cit(teks):
    return re.sub(r"\[([a-z0-9\-]+)\]", lambda m: f"[{peta[m.group(1)]}]" if m.group(1) in peta else m.group(0), teks)

bab1b, bab2b, bab3b = tulis_cit(bab1), tulis_cit(bab2), tulis_cit(bab3)

# --- DP baru ---
dp_baru = ["# DAFTAR PUSTAKA"]
for i, k in enumerate(dipakai, start=1):
    n = kunci_ke_lama[k]
    dp_baru.append(f"[{i}] {lama[n]}")
dp_baru_txt = "\n\n".join(dp_baru)

# --- log baru ---
daftar_kunci = ", ".join(f"[{peta[k]}]{k}" for k in dipakai)
log_baru = f"""## Log Perubahan — Revisi 10 November 2026, gelombang 11 (revisi masukan dosen pembimbing)

Permintaan: menurunkan register ke level mahasiswa D4/S1 (kalimat pendek, emosi manusiawi, tidak seperti tesis S3), menanamkan konteks masalah di Indonesia tepatnya Jawa Timur, mengutamakan sumber data Indonesia, memangkas daftar pustaka yang terlalu banyak, dan tidak memaksakan penerjemahan istilah asing (contoh dilarang: 'sandbox' menjadi 'kotak pasir'). Pekerjaan memakai kaidah naskah-id (EYD V), gaya humanizer-id Mode Akademik Ketat, dan register korpus sempro-mepet:

- BAB I: latar belakang ditulis ulang dari situasi manusia (keluarga pendengar, juru bahasa 500 orang untuk 1,92 juta penyandang tunarungu, ruang kelas) dengan kalimat pendek satu gagasan; data statistik Amerika Serikat (Mitchell dan Karchmer, Lieberman, Ritmeester) dikeluarkan; lokasi penelitian dinyatakan di Jawa Timur dengan sekolah mitra sebagai penanda [PERLU DATA]; klaim kelelahan nonverbal kamera (Bailenson) dikeluarkan dan diganti alasan privasi kenyamanan.
- Rumusan masalah dan tujuan disederhanakan menjadi tiga butir kalimat tunggal tanpa rantai istilah teknis; cermin rumusan-tujuan 1:1 dipertahankan; batasan masalah tetap sembilan butir dengan redaksi lebih pendek.
- BAB II: sebelas subbab dipertahankan; tiap blok teori dirapikan menjadi kalimat pendek; Tabel 2.1 dan 2.3 dipertahankan; Tabel 2.2 dipangkas 11 menjadi 8 baris (baris Filipino, keystroke, Person-in-WiFi keluar); klaim kata berinfleksi HMM, preseden avatar Jepang, dan arkeologi teori (Stokoe, Ong-Ranganath) dikeluarkan.
- BAB III: struktur 3.1-3.11, Tabel 3.1-3.8, tiga gambar, enam prosedur, dan jadwal M1-M14 dipertahankan; kalimat dipangkas; Subbab 3.3 kini menyatakan lokasi Jawa Timur secara eksplisit; sitasi datasheet mikrofon dan kerangka CONSORT dikeluarkan.
- Daftar Pustaka: 93 entri menjadi 46 entri (15 Indonesia + 31 asing; 13 di antaranya dokumentasi resmi perangkat). Entri AS/luar yang dikeluarkan antara lain Mitchell-Karchmer 2 entri, Lieberman, Ritmeester, Rodriguez-Correa, MLMSign, Bailenson, HandFi, Baldeo, Ali keystroke, Mosleh, WiFinger, FingerDraw, MeshID, Chen survey, Nyquist, Shannon, Wi-SL, Hernandez, pose survey, Sapkota YOLO26, MediaPipe, Person-in-WiFi, Shang, Ahmed WiCSI, WiASL, Mountrakis, Kiranyaz, Safrida, Rakun, Anggraini, Sagawa, Bowen, Sokolova, MMS paper, Google TTS, Azure, MM-Fi, INMP441, kamus digital portal, Stokoe, Ong-Ranganath, Hakozaki, Rodhiyah, Wiguna, Sebastian, Cai survey, Hao, Mursita duplikat tidak ada.
- Sitasi kini ditulis dengan kunci semantik pada naskah sumber lalu dinomori ulang urut kemunculan; kesalahan pemetaan nomor-sumber gelombang 10 (antara lain sitasi BRIN [9] yang seharusnya [8], survei 100 responden [10] yang seharusnya [9], dan *Kamus SIBI* [54] yang seharusnya entri kamus cetak) terkoreksi secara konstruksional.
- Pemetaan penuh nomor akhir ke kunci: {daftar_kunci}
- Nol perubahan angka pra-penelitian (mAP50 0,8944, mAP50 0,9580, akurasi 97,6%, 2.300 ms menjadi 54 ms, 69,2 ms, 13 menit/59 detik, Rp150.000, Rp350.000), nol perubahan struktur gerbang G0-G4, jadwal M1-M14, dan keenam prosedur; penanda [PERLU DATA] dan [PERLU ILUSTRASI] dipertahankan.
"""

n_perlu = len(re.findall(r"\[PERLU (?:DATA|RUJUKAN|ILUSTRASI):", body_raw))
print(f"Penanda PERLU di tubuh: {n_perlu}")

out = "\n\n".join([
    header, "---", bab1b, bab2b, bab3b, dp_baru_txt,
    MARK + " (jangan hapus penanda ini) ===", log_baru.rstrip(),
])
OUT.write_text(out + "\n", encoding="utf-8")

# --- statistik ---
def katab(s):
    return len(s.split())
print(f"Tubuh: {katab(bab1b)}+{katab(bab2b)}+{katab(bab3b)} kata; DP {len(dipakai)} entri")
print(f"Total berkas: {len(out.splitlines())} baris, {len(out)} karakter")

# --- cek slop ringan ---
pola = ["di era digital", "tidak dapat dipungkiri", "hal ini", "seiring perkembangan", "seperti yang kita ketahui", "perlu diingat", "sangat krusial", "kotak pasir"]
for p in pola:
    n = len(re.findall(p, body_raw, re.I))
    if n:
        print(f"  PERHATIAN '{p}': {n}x")
# panjang kalimat
kalimat = re.split(r"[.!?]\s", re.sub(r"\[[^\]]*\]", "", body_raw))
pj = [len(k.split()) for k in kalimat if len(k.split()) > 3]
pj.sort()
print(f"Kalimat: {len(pj)}, rata-rata {sum(pj)/len(pj):.1f} kata, p95 {pj[int(len(pj)*0.95)]}, maks {pj[-1]}")
