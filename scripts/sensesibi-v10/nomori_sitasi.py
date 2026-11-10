#!/usr/bin/env python3
"""Nomori ulang sitasi v10: gabungkan 83 rujukan lama + 11 rujukan baru,
urut menurut kemunculan pertama di tubuh naskah; tulis ulang Daftar Pustaka.

Token baru di naskah: [WF] [FD] [MI] [KO] [OR] [TK] [AX] [LP] [TA] [MK] [IN]
"""
import re, sys

P = "/home/z/my-project/download/sensesibi-v10/Proposal-SenseSIBI-v10.md"
teks = open(P, encoding="utf-8").read()

AKHIR = "<!-- ===== AKHIR NASKAH"
HEAD_DP = "# DAFTAR PUSTAKA"
i_akhir = teks.index(AKHIR)
i_dp = teks.index(HEAD_DP)

# catatan penyusunan + identitas + BAB I..III (tubuh) ; lalu DP ; lalu log
pre_dp = teks[:i_dp]
dp_block = teks[i_dp:i_akhir]
log_block = teks[i_akhir:]

# --- entri rujukan baru (terverifikasi 9 Nov 2026) ---
BARU = {
    "WF": 'S. Tan and J. Yang, "WiFinger: Leveraging commodity WiFi for fine-grained finger gesture recognition," in *Proc. 17th ACM Int. Symp. Mobile Ad Hoc Networking and Computing (MobiHoc)*, 2016, doi: 10.1145/2942358.2942393.',
    "FD": 'D. Wu, R. Gao, Y. Zeng, J. Liu, L. Wang, T. Gu, and D. Zhang, "FingerDraw: Sub-wavelength level finger motion tracking with WiFi signals," *Proceedings of the ACM on Interactive, Mobile, Wearable and Ubiquitous Technologies*, vol. 4, no. 1, 2020, doi: 10.1145/3380981.',
    "MI": 'W. Zheng, Y. Zhang, L. Jiang, D. Zhang, and T. Gu, "MeshID: Few-shot finger gesture based user identification using orthogonal signal interference," *Sensors*, vol. 24, no. 6, Art. no. 1978, 2024, doi: 10.3390/s24061978.',
    "KO": 'thewh1teagle, "kokoro-onnx: ONNX versions of the Kokoro TTS model," repositori GitHub. [Online]. Available: https://github.com/thewh1teagle/kokoro-onnx, diakses 9 Nov. 2026.',
    "OR": 'Microsoft, "onnxruntime: Cross-platform, high performance ML inference and training accelerator," repositori GitHub. [Online]. Available: https://github.com/microsoft/onnxruntime, diakses 9 Nov. 2026.',
    "TK": 'Tokio, "tokio: A runtime for writing reliable asynchronous applications with Rust," repositori GitHub. [Online]. Available: https://github.com/tokio-rs/tokio, diakses 9 Nov. 2026.',
    "AX": 'tokio-rs, "axum: Ergonomic and modular web framework built with Tokio," repositori GitHub. [Online]. Available: https://github.com/tokio-rs/axum, diakses 9 Nov. 2026.',
    "LP": 'leptos-rs, "leptos: Build fast full-stack web apps in Rust," repositori GitHub. [Online]. Available: https://github.com/leptos-rs/leptos, diakses 9 Nov. 2026.',
    "TA": 'Tauri, "tauri: Build smaller, faster, and more secure desktop and mobile applications," repositori GitHub. [Online]. Available: https://github.com/tauri-apps/tauri, diakses 9 Nov. 2026.',
    "MK": 'J. C. Mankins, "Technology readiness assessments: A retrospective," *Acta Astronautica*, vol. 65, no. 9-10, pp. 1216-1223, 2009, doi: 10.1016/j.actaastro.2009.03.058.',
    "IN": 'TDK InvenSense, "INMP441: Omnidirectional MEMS microphone with bottom port and I2S digital output," lembar data. [Online]. Available: https://www.invensense.tdk.com/en-us/download-resource/ds-inmp441-00-inmp441-datasheet, diakses 9 Nov. 2026.',
}
PLACEHOLDER = {"WF", "FD", "MI", "KO", "OR", "TK", "AX", "LP", "TA", "MK", "IN"}

# --- parse entri DP lama ---
lama = {}
for m in re.finditer(r"^\[(\d{1,3})\] (.+)$", dp_block, re.M):
    lama[int(m.group(1))] = m.group(2).strip()
print("Entri DP lama terbaca:", len(lama))
assert len(lama) == 83 and sorted(lama.keys()) == list(range(1, 84)), "DP lama tidak lengkap"

# --- urutan kemunculan pertama di tubuh ---
token_re = re.compile(r"\[(\d{1,3})\]|" + r"\[(" + "|".join(PLACEHOLDER) + r")\]")
urutan, terlihat = [], set()
for m in token_re.finditer(pre_dp):
    if m.group(1):
        key = ("n", int(m.group(1)))
    else:
        key = ("p", m.group(2))
    if key not in terlihat:
        terlihat.add(key)
        urutan.append(key)

print("Token unik dikutip di tubuh:", len(urutan))
semua_kunci = [("n", i) for i in range(1, 84)] + [("p", t) for t in PLACEHOLDER]
hilang = [k for k in semua_kunci if k not in terlihat]
assert not hilang, f"Rujukan tidak dikutip: {hilang}"

nomor = {key: i + 1 for i, key in enumerate(urutan)}
assert len(nomor) == 94, f"jumlah rujukan {len(nomor)} != 94"

# --- ganti token di tubuh (nomor lama dulu, placeholder kemudian) ---
def sub_num(m):
    return f"[{nomor[('n', int(m.group(1)))]}]"
def sub_ph(m):
    return f"[{nomor[('p', m.group(2))]}]"
body_baru = token_re.sub(lambda m: sub_num(m) if m.group(1) else sub_ph(m), pre_dp)

# --- tulis ulang DP ---
entri = {}
for key, nn in nomor.items():
    if key[0] == "n":
        entri[nn] = lama[key[1]]
    else:
        entri[nn] = BARU[key[1]]
dp_baru = HEAD_DP + "\n\n" + "\n\n".join(f"[{i}] {entri[i]}" for i in range(1, 95)) + "\n\n"

open(P, "w", encoding="utf-8").write(body_baru + dp_baru + log_block)

# --- laporan pemetaan ---
print("Pemetaan nomor lama -> baru:")
for key, nn in sorted(nomor.items(), key=lambda kv: kv[1]):
    label = key[1] if key[0] == "n" else f"[{key[1]}] (baru)"
    print(f"  {label} -> [{nn}]")
print("TOTAL:", len(nomor), "entri; urut menurut kemunculan pertama.")
