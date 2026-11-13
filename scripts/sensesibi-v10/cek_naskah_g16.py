#!/usr/bin/env python3
"""Pemeriksaan awal naskah v16: sitasi, persamaan, gambar, tabel, penanda, pola terlarang."""
import re
from pathlib import Path

MD = Path("/home/z/my-project/download/sensesibi-v10/Proposal-SenseSIBI-v16.md")
s = MD.read_text(encoding="utf-8")
mark = "<!-- ===== AKHIR NASKAH"
tubuh = s[:s.index(mark)]
dp = tubuh[tubuh.index("# DAFTAR PUSTAKA"):]
isi = tubuh[:tubuh.index("# DAFTAR PUSTAKA")]

# 1) Sitasi monoton menurut kemunculan pertama
nomor = [int(x) for x in re.findall(r"\[(\d+)\]", isi)]
pertama = []
for n in nomor:
    if n not in pertama:
        pertama.append(n)
print("sitasi unik:", sorted(set(nomor)))
print("monoton naik:", pertama == sorted(pertama), "| maks:", max(nomor), "| jumlah kemunculan:", len(nomor))
entri_dp = re.findall(r"^\[(\d+)\]", dp, flags=re.M)
print("entri DP:", len(entri_dp), "| urut:", entri_dp == sorted(entri_dp, key=int))

# 2) Persamaan bernomor
nomor_rumus = re.findall(r"\((\d+\.\d+)\)\s*$", tubuh, flags=re.M)
print("persamaan bernomor:", len(nomor_rumus), nomor_rumus)

# 3) Gambar dan tabel
gam = re.findall(r"^Gambar (\d+\.\d+)", tubuh, flags=re.M)
tab = re.findall(r"^Tabel (\d+\.\d+)", tubuh, flags=re.M)
print("keterangan Gambar:", gam)
print("keterangan Tabel:", tab)

# 4) Penanda PERLU
perlu_data = re.findall(r"\[PERLU DATA:[^\]]*\]", tubuh)
perlu_valid = re.findall(r"\[PERLU VALIDASI:[^\]]*\]", tubuh)
perlu_ilus = re.findall(r"\[PERLU ILUSTRASI:[^\]]*\]", tubuh)
print("PERLU DATA:", len(perlu_data), "| PERLU VALIDASI:", len(perlu_valid), "| PERLU ILUSTRASI:", len(perlu_ilus))

# 5) Pola terlarang
larangan = {
    "'bila'": len(re.findall(r"\bbila\b", isi)),
    "em dash": isi.count("\u2014"),
    "en dash prosa (di luar DP)": isi.count("\u2013"),
    "'di mana' relatif": len(re.findall(r"\bdi mana\b", isi)),
    "'yang mana'": len(re.findall(r"yang mana", isi)),
    "penyangkalan antisipatif (bukan berarti/melainkan)": len(re.findall(r"bukan berarti|bukan sekadar|melainkan", isi)),
    "'Konsekuensinya' pembuka": len(re.findall(r"^Konsekuensinya", isi, flags=re.M)),
    "'Sedangkan' pembuka": len(re.findall(r"^Sedangkan", isi, flags=re.M)),
    "'Adapun'": len(re.findall(r"\bAdapun\b", isi)),
    "konjungsi berpasangan (meskipun...tetapi)": len(re.findall(r"[Mm]eskipun[^.]*tetapi", isi)),
    "'merupakan'": len(re.findall(r"\bmerupakan\b", isi)),
    "'tersebut'": len(re.findall(r"\btersebut\b", isi)),
}
for k, v in larangan.items():
    print(f"  {k}: {v}")

# 6) Kalimat: panjang rata-rata pada prosa (abaikan tabel/rumus/mermaid/blok)
baris = []
skip = False
for ln in isi.split("\n"):
    t = ln.strip()
    if t.startswith("```"):
        skip = not skip
        continue
    if skip or t.startswith("|") or t.startswith("#") or t.startswith(">") or re.match(r"^\d+\.\s", t) or t.startswith("Gambar ") or t.startswith("Tabel "):
        continue
    if t:
        baris.append(t)
teks_prosa = " ".join(baris)
kalimat = [k.strip() for k in re.split(r"[.!?]+(?:\s|$)", teks_prosa) if len(k.strip()) > 2]
panjang = [len(k.split()) for k in kalimat]
if panjang:
    import statistics as st
    print(f"kalimat prosa: {len(kalimat)} | rerata: {st.mean(panjang):.1f} kata | stdev: {st.stdev(panjang):.1f}")
    print(f"  kalimat >=28 kata: {sum(1 for p in panjang if p >= 28) / len(panjang) * 100:.1f}% | <=10 kata: {sum(1 for p in panjang if p <= 10) / len(panjang) * 100:.1f}%")

# 7) Triplet "X, Y, dan Z" kandidat
trip = re.findall(r"(\b\w+, \b\w+, dan \b\w+\b)", isi)
print("kandidat triplet koma:", len(trip))
for t in trip[:15]:
    print("   ", t)
