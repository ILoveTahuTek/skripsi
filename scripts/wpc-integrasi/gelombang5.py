#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gelombang 5 (Task 39): revisi Agent Brief v3 pada draft-final.md.
Tahap: backup -> global YOLO26m-Pose -> EDITS -> blok 3.2 & Tabel kriteria ->
renumber tabel -> sisip DP baru -> renumber sitasi urutan kemunculan -> log -> verifikasi."""
import re
import sys
from pathlib import Path

sys.path.insert(0, "/home/z/my-project/scripts/wpc-integrasi")
from gelombang5_edits import (EDITS_BAB1, EDITS_BAB1_B, EDITS_BAB2, EDITS_BAB3, EDITS_BAB3_B,
                              EDITS_BAB3_C, EDITS_BAB3_D, BLOK_32_LAMA, BLOK_32_BARU,
                              TABEL_KRITERIA_LAMA, TABEL_KRITERIA_BARU,
                              DP_BARU, LOG_GELOMBANG5)

DRAFT = Path("/home/z/my-project/download/translator-sibi-final/draft-final.md")
BACKUP = Path("/home/z/my-project/download/translator-sibi-final/_kerja/draft-final.sebelum-gelombang5.md")

teks = DRAFT.read_text(encoding="utf-8")
BACKUP.write_text(teks, encoding="utf-8")

# ---------- 0) Global: YOLO26-Pose -> YOLO26m-Pose ----------
n = teks.count("YOLO26-Pose")
assert n == 24, f"YOLO26-Pose: {n} (harus 24)"
teks = teks.replace("YOLO26-Pose", "YOLO26m-Pose")

# ---------- 1) EDITS ----------
SEMUA = EDITS_BAB1 + EDITS_BAB1_B + EDITS_BAB2 + EDITS_BAB3 + EDITS_BAB3_B + EDITS_BAB3_C + EDITS_BAB3_D
for nama, lama, baru in SEMUA:
    c = teks.count(lama)
    assert c == 1, f"anchor '{nama}': {c} kemunculan (harus 1)"
    teks = teks.replace(lama, baru)
print(f"EDITS diterapkan: {len(SEMUA)} suntingan")

# ---------- 2) Blok 3.2 + Tabel kriteria ----------
for nama, lama, baru in [("blok 3.2", BLOK_32_LAMA, BLOK_32_BARU),
                         ("Tabel kriteria", TABEL_KRITERIA_LAMA, TABEL_KRITERIA_BARU)]:
    c = teks.count(lama)
    assert c == 1, f"blok '{nama}': {c} kemunculan (harus 1)"
    teks = teks.replace(lama, baru)
print("Blok 3.2 dan Tabel kriteria gerbang diganti")

# ---------- 3) Renumber tabel BAB III (descending) ----------
urutan = [("Tabel 3.7", "Tabel 3.8"), ("Tabel 3.6", "Tabel 3.7"), ("Tabel 3.5", "Tabel 3.6"),
          ("Tabel 3.4", "Tabel 3.5"), ("Tabel 3.3", "Tabel 3.4")]
for a, b in urutan:
    teks = teks.replace(a, b)
teks = teks.replace("Tabel XX", "Tabel 3.3")
print("Tabel BAB III digeser: matriks arsitektur = Tabel 3.3; skema 3.4; kriteria 3.5; jadwal 3.6; parameter 3.7; risiko 3.8")

# ---------- 4) Sisip entri DP baru ----------
for e in DP_BARU:
    no = int(re.match(r"\[(\d+)\]", e).group(1))
    anchor = f"[{no - 1}] "
    i = teks.find("\n" + anchor, teks.find("# DAFTAR PUSTAKA"))
    assert i > 0, f"anchor DP {no-1} tidak ditemukan"
    j = teks.find("\n", i + 1)  # akhir baris entri [no-1]
    teks = teks[:j + 1] + e + "\n" + teks[j + 1:]
print("3 entri DP baru disisipkan (sementara [81]-[83])")

# ---------- 5) Renumber sitasi: urutan kemunculan pertama ----------
baris = teks.split("\n")
dp_mulai = next(i for i, l in enumerate(baris) if l.startswith("# DAFTAR PUSTAKA"))
akar = next(i for i, l in enumerate(baris) if "AKHIR NASKAH" in l)
kepala = "\n".join(baris[:dp_mulai])
dp_baris = baris[dp_mulai:akar]
log_baris = baris[akar:]

pos = {}
for m in re.finditer(r"\[(\d{1,3})\]", kepala):
    no = int(m.group(1))
    if no not in pos:
        pos[no] = m.start()
urutan_muncul = sorted(pos.items(), key=lambda x: x[1])
peta = {lama: baru + 1 for baru, (lama, _) in enumerate(urutan_muncul)}
semua_no = set(peta)
assert semua_no == set(range(1, 84)), f"rentang nomor tidak 1..83: {sorted(semua_no)[-5:]}"

def ganti(m):
    return "[" + str(peta[int(m.group(1))]) + "]"
kepala_baru = re.sub(r"\[(\d{1,3})\]", ganti, kepala)

# entri DP: renumber awalan + urut ulang
entri = {}
for l in dp_baris:
    m = re.match(r"^\[(\d{1,3})\] (.*)$", l)
    if m:
        entri[int(m.group(1))] = m.group(2)
assert sorted(entri) == list(range(1, 84)), f"DP tidak lengkap: {len(entri)}"
dp_urut = [f"[{no}] {entri[no]}" for no in range(1, 84)]

teks = kepala_baru + "\n# DAFTAR PUSTAKA\n\n" + "\n\n".join(dp_urut) + "\n\n" + "\n".join(log_baris)
DRAFT.write_text(teks, encoding="utf-8")
print(f"Sitasi dinomori ulang 1..83 mengikuti kemunculan pertama; DP terurut")

# ---------- 6) Log gelombang 5 ----------
teks = DRAFT.read_text(encoding="utf-8")
if not teks.endswith("\n"):
    teks += "\n"
teks += "\n" + LOG_GELOMBANG5
DRAFT.write_text(teks, encoding="utf-8")

# ---------- 7) Verifikasi ----------
t2 = DRAFT.read_text(encoding="utf-8")
b2 = t2.split("\n")
akar2 = next(i for i, l in enumerate(b2) if "AKHIR NASKAH" in l)
dp_mulai2 = next(i for i, l in enumerate(b2) if l.startswith("# DAFTAR PUSTAKA"))
prosa = "\n".join(b2[:dp_mulai2])
dp2 = [l for l in b2[dp_mulai2:akar2] if re.match(r"^\[\d+\] ", l)]
nomor = [int(re.match(r"^\[(\d+)]", l).group(1)) for l in dp2]
print(f"\nentri DP: {len(dp2)}, urut 1..{nomor[-1]}: {nomor == list(range(1, 84))}")
sitasi = sorted(set(int(x) for x in re.findall(r"\[(\d{1,3})\]", prosa)))
print(f"sitasi prosa unik: {len(sitasi)}, rentang {sitasi[0]}..{sitasi[-1]}")
print(f"entri DP tanpa sitasi: {[n for n in nomor if n not in set(sitasi)]}")
print(f"sitasi tanpa entri DP: {[n for n in sitasi if n not in set(nomor)]}")
# urutan kemunculan monoton?
pos2 = {}
for m in re.finditer(r"\[(\d{1,3})\]", prosa):
    no = int(m.group(1))
    pos2.setdefault(no, m.start())
seq = [no for no, _ in sorted(pos2.items(), key=lambda x: x[1])]
print(f"urutan kemunculan monoton naik: {seq == sorted(seq)}")
# frasa kunci gelombang 5
kunci_ada = ["YOLO26m-Pose", "SenseSIBI, singkatan dari", "zona Fresnel", "CSI-ratio",
             "wifi-densepose-pretrained", "wifi-densepose-mmfi-pose", "Widar2.0",
             "MM-Fi", "esp32-csi-node", "beacon ESP-NOW", "sepasang modul ESP32-S3",
             "56 *subcarrier*", "1T1R", "pra-penelitian", "ground truth",
             "G3 (integrasi pemrosesan suara dua arah)", "wali murid",
             "backbone", "Tabel 3.3 Matriks komponen arsitektur",
             "beacon ESP-NOW", "ruang terkontrol SLB", "pengujian bergerbang lima tahap",
             "0,8944", "0,9580", "97,6%", "82,3%"]
for k in kunci_ada:
    print(f"  ADA  {k}" if k in prosa + "\n".join(dp2) else f"  HILANG!  {k}")
kunci_hilang = ["YOLO26-Pose", "17 keypoint COCO", "2–3 modul", "dua hingga tiga modul",
                "Tabel 3.6 Parameter rancangan", "G1 M3: separabilitas awal"]
for k in kunci_hilang:
    print(f"  BERSIH  {k!r}" if k not in t2 else f"  MASIH ADA!  {k!r}")
print(f"\npanjang naskah: {len(t2):,} karakter")
print("Gelombang 5 selesai.")
