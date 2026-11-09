#!/usr/bin/env python3
"""Bangun manifes akses 94 rujukan: status unduh + jalur akses + tautan, dari hasil_unduh.json + DP naskah."""
import json, re

MD = "/home/z/my-project/download/sensesibi-v10/Proposal-SenseSIBI-v10.md"
OUT = "/home/z/my-project/download/sensesibi-v10/referensi/Akses-94-Rujukan.md"
teks = open(MD, encoding="utf-8").read()
dp = teks[teks.index("# DAFTAR PUSTAKA"):teks.index("<!-- ===== AKHIR NASKAH")]
dp = dp.replace("# DAFTAR PUSTAKA\n\n", "")
entri = {}
for m in re.finditer(r"^\[(\d+)\] (.+)$", dp, re.M):
    entri[int(m.group(1))] = m.group(2).strip()

H = {x["no"]: x for x in json.load(open("/home/z/my-project/scripts/sensesibi-v10/hasil_unduh.json"))}
assert set(H) == set(entri) == set(range(1, 95))

baris = []
n_t = n_p = n_b = 0
for n in range(1, 95):
    h = H[n]
    st = h["status"]
    if "BERBAYAR" in st or "TANPA" in st: label = "berbayar/cetak"
    elif st == "TERUNDUH": label = "terunduh"
    elif st == "PERAMBAN": label = "peramban"
    else: label = st
    if label == "terunduh": n_t += 1
    elif label == "peramban": n_p += 1
    else: n_b += 1
    info = h["info"]
    jalur = info
    berkas = ""
    if label == "terunduh":
        m = re.search(r"ref-\d+_.+?\.(pdf|html|md)", OUT if False else "")
        # nama berkas bisa dirunut dari kunci
        ext = "pdf" if "(pdf)" in info else ("md" if "(md)" in info else "html")
        berkas = f"`ref-{n:02d}_{h['kunci']}.{ext}`"
    if label == "berbayar/cetak":
        jalur = info  # keterangan penerbit
    elif label == "peramban":
        m = re.search(r"\((.+?)\)", info)
        jalur = m.group(1) if m else info
    baris.append(f"| {n} | {entri[n][:150]} | {label} | {berkas} | {jalur} |")

isi = f"""# Akses 94 Rujukan — Proposal SenseSIBI v10 (revisi 9 November 2026)

Peta jalur akses seluruh Daftar Pustaka versi v10 (94 entri, urut kemunculan).
Status: **terunduh** = berkas tersimpan pada folder ini; **peramban** = gratis
dan legal, tetapi situs memblokir unduhan otomatis sehingga perlu dibuka di
peramban; **berbayar/cetak** = naskah penuh di balik paywall penerbit atau tanpa versi digital.

Rekap: {n_t} terunduh · {n_p} peramban · {n_b} berbayar/cetak.

| No. | Rujukan | Status | Berkas | Jalur akses |
|---|---|---|---|---|
{chr(10).join(baris)}

Catatan: untuk rujukan repositori GitHub, berkas tersimpan adalah README resmi
repositori pada 9 November 2026; untuk dokumentasi daring dan lembar data,
tersimpan halaman resmi dalam format HTML. Rujukan [32] RuView mengacu pada
repositori pada *commit* fefb0f9. Rujukan [91] Mankins 2009 adalah artikel
berlangganan Elsevier; kerangka TRL dapat dipahami lewat ringkasan pada
*abstract* resmi (doi: 10.1016/j.actaastro.2009.03.058) atau salinan
institusi pemilik penelitian bila tersedia.
"""
open(OUT, "w", encoding="utf-8").write(isi)
print("manifes ditulis:", OUT)
print(f"rekap: terunduh={n_t} peramban={n_p} berbayar/cetak={n_b}")
