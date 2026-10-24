#!/usr/bin/env python3
"""Susun markdown terpadu: blok judul+identitas + BAB I + BAB II + BAB III + Daftar Pustaka.
Konten bab digabung VERBATIM dari materi (tanpa perubahan teks)."""
import re, pathlib

SRC = pathlib.Path('/home/z/my-project/materials/sempro/dpj4-sibi-csi')
OUT = pathlib.Path('/home/z/my-project/download/sempro-dpj4-sibi-csi/Proposal-Sempro-DPJ4-SIBI-CSI.md')

bab1 = (SRC / 'bab1-pendahuluan.md').read_text(encoding='utf-8').strip()
bab2 = (SRC / 'bab2-kajian-pustaka.md').read_text(encoding='utf-8').strip()
bab3 = (SRC / 'bab3-metodologi.md').read_text(encoding='utf-8').strip()
dp   = (SRC / 'daftar-pustaka.md').read_text(encoding='utf-8').strip()

def strip_h1(text):
    """Buang baris H1 (judul bab akan dipisah dengan pemisah sendiri)."""
    lines = text.split('\n')
    assert lines[0].startswith('# '), lines[0]
    return '\n'.join(lines[1:]).strip()

header = """# Alat Pembelajaran Isyarat SIBI Tanpa Kamera Berbasis Wi-Fi Channel State Information pada ESP32: Studi Kelayakan Umpan Balik Latihan bagi Pembelajar Pendengar

**PROPOSAL PENELITIAN**

| Identitas | Keterangan |
|---|---|
| Judul | Alat Pembelajaran Isyarat SIBI Tanpa Kamera Berbasis Wi-Fi *Channel State Information* pada ESP32: Studi Kelayakan Umpan Balik Latihan bagi Pembelajar Pendengar |
| Jenis dokumen | Proposal penelitian (seminar proposal), BAB I–III + Daftar Pustaka |
| Disusun oleh | [PERLU DATA: nama penulis] |
| NIM | [PERLU DATA: NIM penulis] |
| Program studi | [PERLU DATA: program studi] |
| Universitas | [PERLU DATA: nama universitas] |
| Pembimbing | [PERLU DATA: nama pembimbing, bila sudah ditetapkan] |
| Tahun | [PERLU DATA: tahun penyusunan] |

> Catatan pengemasan: dokumen ini disusun dari materi `sempro/dpj4-sibi-csi` (23 Oktober 2026; penanda diisi dari sumber terverifikasi pada 24 Oktober 2026). Penanda `[PERLU DATA: ...]` yang tersisa berupa keputusan bersama pembimbing, data pribadi, atau parameter rancangan yang memang ditetapkan kemudian; daftar lengkapnya ada pada `laporan-penanda.md`. Diagram Gambar 3.1 dan 3.2 tersimpan sebagai berkas PNG pada `assets/`.

---

"""

parts = [header]
for bab in (bab1, bab2, bab3):
    parts.append(bab + '\n\n---\n\n')
parts.append(dp + '\n')

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(''.join(parts), encoding='utf-8')

# Verifikasi: teks bab harus identik verbatim
combined = OUT.read_text(encoding='utf-8')
for name, bab in [('bab1', bab1), ('bab2', bab2), ('bab3', bab3), ('dp', dp)]:
    body = strip_h1(bab)
    print(f"{name}: verbatim={'OK' if body in combined else 'GAGAL'} ({len(body)} chars)")
print("Total:", len(combined), "chars")
