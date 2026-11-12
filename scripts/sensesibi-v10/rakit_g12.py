#!/usr/bin/env python3
"""Rakit naskah v12 (gelombang 12): parafrase anti-ai-writer atas v11.

Sumber tetap memakai kunci semantik; skrip memetakan kunci -> entri DP asli
(Proposal-SenseSIBI-v10.md), memverifikasi kecocokan lewat penanda teks,
menomori ulang urut kemunculan pertama, lalu menulis tubuh dan DP.
"""
import re
from pathlib import Path

BASE = Path("/home/z/my-project/download/sensesibi-v10")
SRC = BASE / "_kerja-g12/src"
ORIG = BASE / "Proposal-SenseSIBI-v10.md"
OUT = BASE / "Proposal-SenseSIBI-v12.md"

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
log_baru = f"""## Log Perubahan — Revisi 11 November 2026, gelombang 12 (parafrase anti-ai-writer)

Permintaan: memparafrasekan ketiga dokumen (md, docx, pdf) memakai skill anti-ai-writer (mchardyan/anti-ai-writer v2) di atas naskah v11, tanpa mengubah isi. Pekerjaan tetap menjaga kaidah naskah-id (EYD V), register mahasiswa D4/S1, dan seluruh keputusan gelombang 11 (konteks Jawa Timur, prioritas sumber Indonesia, DP 46 entri, istilah asing tidak dipaksakan diterjemahkan):

- Kosakata dan frasa terlarang daftar hitam anti-ai-writer dibersihkan dari prosa: menegaskan (2), mencakup (4), menampilkan (8) diganti padanan konkret yang bervariasi (memunculkan, muncul, memperlihatkan, memuat, meliputi, menunjukkan).
- Ritme kalimat dirombak: 10 deretan tiga kalimat berpanjang seragam pada v11 (toleransi dua kata) dipecah menjadi nol melalui penggabungan, pemenggalan, dan pemanjangan kalimat terpilih; panjang kalimat kini menyebar dari 3 sampai 53 kata (13% kalimat pendek 10 kata ke bawah, 23% kalimat panjang 28 kata ke atas).
- Pola khas AI lain yang dihapus: enumerasi retoris "Pertama, ... Kedua, ..." pada latar belakang (diganti prosa mengalir), pembuka klise, dan ketergantungan pada transisi; beberapa paragraf kini ditutup tiba-tiba dan satu pertanyaan retoris dipertahankan sebagai penutup latar belakang.
- Yang tidak berubah: 46 kunci sitasi beserta urutan kemunculan dan penomoran, seluruh angka pra-penelitian (token angka pada prosa identik dengan v11), 25 penanda [PERLU DATA]/[PERLU ILUSTRASI], 12 tabel, 3 gambar beserta blok mermaid-nya, 39 heading, struktur gerbang G0-G4, jadwal M1-M14, dan keenam prosedur.
- Rumusan masalah dan tujuan diparafrase tercermin tetap 3:3; batasan tetap sembilan butir.
- Pemetaan penuh nomor akhir ke kunci: {daftar_kunci}
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
