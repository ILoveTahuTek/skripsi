#!/usr/bin/env python3
"""Verifikasi versi ringkas: (1) sitasi 1..93 urut dan DP cocok;
(2) angka kunci tidak ada yang baru/diubah dibanding naskah asli."""
import re
from pathlib import Path

BASE = Path("/home/z/my-project/download/sensesibi-v10")
ringkas = (BASE / "Proposal-SenseSIBI-v10-ringkas.md").read_text(encoding="utf-8")
asli = (BASE / "Proposal-SenseSIBI-v10.md").read_text(encoding="utf-8")

mark = "<!-- ===== AKHIR NASKAH"
i_r = ringkas.index(mark); i_a = asli.index(mark)
dp_r = ringkas[ringkas.index("# DAFTAR PUSTAKA"):i_r]
dp_a = asli[asli.index("# DAFTAR PUSTAKA"):i_a]
body_r = ringkas[:ringkas.index("# DAFTAR PUSTAKA")]
body_a = asli[:asli.index("# DAFTAR PUSTAKA")]

# 1) sitasi
cit = [int(m) for m in re.findall(r"\[(\d{1,3})\]", body_r)]
unik = list(dict.fromkeys(cit))
print(f"Sitasi tubuh: total {len(cit)}, unik {len(unik)}, urut-kemunculan benar: {unik == sorted(unik)}")
print(f"Nomor unik berurutan 1..{len(unik)}: {unik == list(range(1, len(unik)+1))}")

# entri DP dan kecocokan konten terhadap DP asli (urutkan asli berdasar isi)
ent_a = {}
for m in re.finditer(r"^\[(\d{1,3})\] (.+)$", dp_a, re.M):
    ent_a[m.group(2).strip()] = int(m.group(1))
ent_r = {}
for m in re.finditer(r"^\[(\d{1,3})\] (.+)$", dp_r, re.M):
    ent_r[int(m.group(1))] = m.group(2).strip()
print(f"DP ringkas: {len(ent_r)} entri")
salah = [n for n, teks in ent_r.items() if teks not in ent_a]
teks_sama = all(teks in ent_a for teks in ent_r.values())
print("Semua entri DP ringkas identik dengan entri DP asli:", teks_sama)
if salah:
    print("  entri tak dikenal:", salah[:3])

# 2) angka: kumpulkan token numerik & persen dari tubuh ringkas; cek ada di asli
def toks(t):
    # buang nomor subbab/tabel/gambar/sitasi/minggu/gerbang/GATE (di-whitelist)
    t = re.sub(r"\[\d{1,3}\]", " ", t)
    t = re.sub(r"(?:Subbab|Tabel|Gambar)\s+\d+(?:\.\d+)*", " ", t)
    t = re.sub(r"\bM(?:1[0-4]?|[1-9])\b", " ", t)
    t = re.sub(r"\bG[0-4]\b", " ", t)
    t = re.sub(r"\bT[0-5]\b", " ", t)
    t = re.sub(r"\b(?:ADR-\d+|GPIO ?\d+|IEEE 802\.11|TKT/TRL|CC-BY-NC|id-ID|802\.11b/g/n)\b", " ", t)
    t = t.replace("*Kamus SIBI*", " ")
    out = set()
    for m in re.finditer(r"\d+(?:[.,]\d+)*(?:\s?%)?", t):
        out.add(m.group(0).replace(" ", ""))
    return out

ta, tr = toks(body_a), toks(body_r)
baru = sorted(tr - ta)
print(f"Token numerik ringkas: {len(tr)}; tidak ada di naskah asli: {len(baru)}")
if baru:
    print("  TOKEN BARU:", baru[:20])

# 3) penanda PERLU
perlu_r = re.findall(r"\[PERLU (?:DATA|RUJUKAN|ILUSTRASI):[^\]]*\]", body_r)
perlu_a = re.findall(r"\[PERLU (?:DATA|RUJUKAN|ILUSTRASI):[^\]]*\]", body_a)
print(f"Penanda PERLU ringkas: {len(perlu_r)} (asli tubuh: {len(perlu_a)})")
hilang = [p for p in set(perlu_a) - set(perlu_r) if not any(p[:30] in q for q in perlu_r)]
print("Penanda asli yang hilang total:", len(hilang))
for h in hilang[:5]:
    print("   -", h[:80])

# 4) cermin rumusan-tujuan
rum = re.search(r"## 1\.2.*?\n\n(.*?)\n\n## 1\.3", body_r, re.S).group(1)
tuj = re.search(r"## 1\.3.*?\n\n(.*?)\n\n## 1\.4", body_r, re.S).group(1)
n_rum = len(re.findall(r"^\d+\.", rum, re.M))
n_tuj = len(re.findall(r"^\d+\.", tuj, re.M))
print(f"Cermin rumusan ({n_rum}) - tujuan ({n_tuj}): {'OK' if n_rum == n_tuj else 'BEDA!'}")
