#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Renumber sitasi + pangkas DAFTAR PUSTAKA draft-final.md (revisi WPC).

HAPUS (17): rujukan paywall/cetak tanpa salinan legal gratis.
KEEP (63) -> nomor baru 1..63 mengikuti urutan lama.
Bagian log (setelah AKHIR NASKAH) tidak disentuh.
"""
import re
from pathlib import Path

P = Path('/home/z/my-project/download/translator-sibi-final/draft-final.md')
HAPUS = {1, 2, 4, 18, 22, 23, 24, 39, 43, 44, 45, 46, 66, 67, 71, 74, 75}

# peta nomor lama -> baru (urutan asli dipertahankan)
peta = {}
new = 0
for old in range(1, 81):
    if old in HAPUS:
        continue
    new += 1
    peta[old] = new
assert new == 63, new

teks = P.read_text(encoding='utf-8')
baris = teks.split('\n')
akar = next(i for i, l in enumerate(baris) if 'AKHIR NASKAH' in l)
dp_mulai = next(i for i, l in enumerate(baris) if l.startswith('# DAFTAR PUSTAKA'))

naskah = baris[:akar]
log = baris[akar:]

# 1) pisahkan entri DP, buang yang dihapus
kepala_dp = dp_mulai
isi_dp = []
dp_akhir = kepala_dp
for i in range(kepala_dp, akar):
    l = naskah[i]
    m = re.match(r'^\[(\d{1,2})\] ', l)
    if m:
        no = int(m.group(1))
        dp_akhir = i
        if no not in HAPUS:
            isi_dp.append(l)
    elif l.strip() == '' or l.startswith('<!--') or l.startswith('---'):
        continue
# baris di luar entri (mis. pemisah) dipertahankan apa adanya via rekonstruksi di bawah

# rekonstruksi blok naskah: kepala (0..dp_mulai) + DP baru + log
kepala = naskah[:dp_mulai]

# 2) renumber sitasi [n] di kepala (prosa naskah)
def renumber(t):
    def ganti(m):
        no = int(m.group(1))
        return '[' + str(peta[no]) + ']' if no in peta else m.group(0)
    return re.sub(r'\[(\d{1,2})\]', ganti, t)

kepala_baru = [renumber(l) for l in kepala]

# 3) renumber awalan entri DP
dp_baru = []
for l in isi_dp:
    m = re.match(r'^\[(\d{1,2})\] (.*)$', l)
    no, isi = int(m.group(1)), m.group(2)
    dp_baru.append(f'[{peta[no]}] {isi}')

# 4) rakit ulang
naskah_baru = kepala_baru + [
    '# DAFTAR PUSTAKA',
    '',
] + [f'{e}' if i % 1 == 0 else e for i, e in enumerate(dp_baru)]
# sisipkan baris kosong antarentri (format asli: entri dipisah baris kosong)
naskah_baru = kepala_baru + ['# DAFTAR PUSTAKA', '']
for e in dp_baru:
    naskah_baru.append(e)
    naskah_baru.append('')

hasil = naskah_baru + log
P.write_text('\n'.join(hasil), encoding='utf-8')

# 5) verifikasi
t2 = P.read_text(encoding='utf-8')
b2 = t2.split('\n')
akar2 = next(i for i, l in enumerate(b2) if 'AKHIR NASKAH' in l)
n2 = b2[:akar2]
dp2 = [l for l in n2 if re.match(r'^\[\d{1,2}\] ', l)]
print(f"entri DP sekarang: {len(dp2)}")
nomor = sorted(int(re.match(r'^\[(\d+)]', l).group(1)) for l in dp2)
print(f"nomor berurut 1..{nomor[-1]}: {nomor == list(range(1, 64))}")

# sitasi di prosa vs daftar DP
dp_mulai2 = next(i for i, l in enumerate(n2) if l.startswith('# DAFTAR PUSTAKA'))
prosa = '\n'.join(n2[:dp_mulai2])
sitasi = sorted(set(int(x) for x in re.findall(r'\[(\d{1,2})\]', prosa)))
print(f"rentang sitasi prosa: {sitasi[0]}..{sitasi[-1]}, jumlah unik {len(sitasi)}")
tak_dirujuk = [n for n in nomor if n not in sitasi]
dirujuk_tak_ada = [n for n in sitasi if n not in nomor]
print(f"entri DP tanpa sitasi: {tak_dirujuk}")
print(f"sitasi tanpa entri DP: {dirujuk_tak_ada}")
sisa_hapus = [int(m) for m in re.findall(r'\[(\d+)\]', prosa) if int(m) > 63]
print(f"sitasi > 63 di prosa (harus kosong): {sisa_hapus}")
# peta untuk laporan
print("\nPeta lama->baru (63):")
print(', '.join(f'{o}->{n}' for o, n in peta.items()))
