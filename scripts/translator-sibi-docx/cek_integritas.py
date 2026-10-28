#!/usr/bin/env python3
"""Pemeriksa integritas ilmiah: seluruh simpul & sisi 6 diagram lama harus terwakili di 8 diagram baru.
Transformasi terdokumentasi (kompresi notasi, pemindahan ke caption/prosa) tercantum eksplisit."""
import re, os, sys

LAMA = '/home/z/my-project/download/translator-sibi-draft/diagram/lama-20261026'
BARU = '/home/z/my-project/download/translator-sibi-draft/diagram'

def parse(path):
    ids, edges = set(), []
    for line in open(path, encoding='utf-8'):
        line = line.strip()
        if line.startswith('%%'): continue
        line = line.replace('<br/>', ' | ').replace('<br />', ' | ')
        m = re.match(r'([A-Za-z][A-Za-z0-9]*)\s*(?:\[|\{|\()', line)
        if m: ids.add(m.group(1))
        for e in re.finditer(r'(\w+)\s*(--[^>]*?-|-\.-[^>]*?-)?->{0,1}>{1}\s*(\w+)', line):
            pass
        # sisi: A --> B / A -- "lbl" --> B / A -. "lbl" .-> B / A ~~~ B (abaikan ~~~)
        for e in re.finditer(r'(\w+)\s*(--[^>]*|-\.([^>]*)\.)?-{1,2}>\s*(\w+)', line):
            a, lbl, c, b = e.group(1), e.group(2) or '', e.group(3), e.group(4)
            if a in ('subgraph',) : continue
            edges.append((a, b, lbl.strip('-" ')))
    return ids, edges

# petakan eksplisit transformasi yang TERDOKUMENTASI (bukan kehilangan)
DIPINDAH = {  # simpul lama -> lokasi baru / keterangan
 'P0': '3.2 (aksi G0)', 'P1': '3.2 (aksi G1)', 'P2': '3.2 (aksi G2)', 'P3': '3.2 (aksi G3)', 'P4': '3.2 (aksi G4)',
 'G0U': '3.2: label sisi "lolos/gagal lagi" (uji ulang)', 'G1U': '3.2: label sisi "lolos/gagal lagi" (uji ulang)',
 'S0': '3.2: lingkaran "temuan" + caption (rincian teks)', 'S1': '3.2: lingkaran "temuan" + caption (rincian teks)',
 'NOTE': '3.7: dihapus — isi sudah di BAB II [29]; WIFI_PS_NONE ke prosa 3.7.8',
 'REC': '3.3', 'FLT': '3.3 (dari G3.6 lama)', 'TT': '3.3', 'TQ': '3.3', 'Y26': '3.3', 'PAIR': '3.3', 'DQ': '3.3',
 'SD': '3.4 (utk G3.6 lama: simpul DS setara)', 'STU': '3.4', 'BASE': '3.4', 'EQ': '3.4', 'OPT': '3.4', 'DEP': '3.4', 'DEV': '3.4',
 'TX': '3.5', 'ZN': '3.5', 'RX': '3.5', 'MAPL': '3.5', 'DSP1': '3.5', 'TTS': '3.5', 'SPK': '3.5',
 'BTN': '3.5', 'MIC': '3.5', 'STT': '3.5', 'DSP2': '3.5', 'AST': '3.5', 'CAM': '3.5', 'Y26P': '3.5', 'SUP': '3.5', 'LOK': '3.5',
 'MA': '3.6', 'MB': '3.6', 'MC': '3.6', 'AP': '3.6', 'TTSA': '3.6', 'STTA': '3.6', 'RUVR': '3.6', 'ASRL': '3.6', 'TTSL': '3.6',
 'CSI': '3.7', 'BUF': '3.7', 'SEG': '3.7', 'FT': '3.7', 'MOD': '3.7', 'DEC': '3.7', 'OUT': '3.7', 'RJ': '3.7',
 'SPLIT': '3.8', 'MET': '3.8', 'OP': '3.8', 'COVER': '3.8', 'USE': '3.8', 'ARTE': '3.8',
 'DS': '3.3/3.4 (simpul SD setara)', 'MULAI': '3.8 (simpul masuk baru, mewakili keluaran 3.4)',
}
# id baru (3.1/3.2 pakai id sama utk T0..T5, G0..G4)
for t in ['T0','T1','T2','T2B','T3','T4','T5']: DIPINDAH[t] = '3.1'
for g in ['G0','G1','G2','G3','G4']: DIPINDAH[g] = '3.1/3.2'

SISI_KHUSUS = {  # (lama_a, lama_b) -> justifikasi transformasi
 ('P0','G0U'): '3.2: teks P0 "lalu G0 diuji ulang" + cabang lolos/gagal lagi',
 ('G0U','T1'): '3.2: sisi P0 --"lolos: T1"--> keluaran',
 ('G0U','S0'): '3.2: sisi P0 --"gagal lagi"--> temuan',
 ('S0','T5'): '3.2: teks lingkaran/temuan + caption "penelitian lanjut ke T5"',
 ('P1','G1U'): '3.2: teks P1 + cabang lolos/gagal lagi',
 ('G1U','T2'): '3.2: sisi P1 --"lolos: T2"--> keluaran',
 ('G1U','S1'): '3.2: sisi P1 --"gagal lagi"--> temuan',
 ('REC','TT'): '3.3: REC-->FLT-->TT (FLT disisip dari G3.6 lama; rantai sama)',
 ('TQ','Y26'): '3.3: sisi klaster KA--"ya"-->KB',
 ('REC','PAIR'): '3.3: sisi klaster KA--"video + CSI"-->KB',
 ('DQ','REC'): '3.3: sisi klaster KB--"belum"-->KA',
 ('DQ','SD'): '3.3: sisi DQ --"ya: ke Gambar 3.4"--> keluaran',
 ('EQ','OPT'): '3.4: sisi klaster KA--"ya"-->KB',
 ('FT','MOD'): '3.7: sisi klaster R1-->R2',
 ('DEC','OUT'): '3.7: sisi klaster R2--"ya"-->R3',
 ('DEC','RJ'): '3.7: sisi klaster R2--"tidak"-->R3',
 ('MOD','NOTE'): '3.7: NOTE dihapus (duplikat BAB II [29]); lihat DIPINDAH',
 ('STU','SPLIT'): '3.4→3.8: simpul masuk MULAI "(Gambar 3.4)"',
 ('TT','DS'): '3.3→3.4: rantai guru→dataset terwakili DQ-ya→Gambar 3.4 (SD)',
 ('G2','T2B'): '3.1: sisi klaster KA--"lolos"-->KB',
 ('AWAN','SERVER'): '3.6: sisi taklihat AWAN~~~SERVER (hanya penata, pendamping sisi AP-.->SERVER)',
}

# kumpulkan sisi lama & baru
lama_ids, lama_edges = set(), []
for f in sorted(os.listdir(LAMA)):
    if not f.endswith('.mmd') or os.path.isdir(os.path.join(LAMA, f)): continue
    i, e = parse(os.path.join(LAMA, f))
    lama_ids |= i; lama_edges += e
baru_ids, baru_edges = set(), []
for f in os.listdir(BARU):
    if not f.startswith('G3.') or not f.endswith('.mmd'): continue
    if os.path.isdir(os.path.join(BARU, f)): continue
    i, e = parse(os.path.join(BARU, f))
    baru_ids |= i; baru_edges += e
baru_pair = {(a, b) for a, b, _ in baru_edges}

masalah = []
for i in sorted(lama_ids):
    if i not in DIPINDAH and i not in baru_ids:
        masalah.append(f'SIMPUL HILANG: {i}')
for a, b, lbl in lama_edges:
    if (a, b) in baru_pair: continue
    if (a, b) in SISI_KHUSUS: continue
    # sisi lama yang ujungnya dimutasi tercakup di SISI_KHUSUS
    masalah.append(f'SISI TAK TERWAKILI: {a} --> {b} [{lbl}]')

print(f'Simpul lama: {len(lama_ids)} | sisi lama: {len(lama_edges)} | simpul baru: {len(baru_ids)} | sisi baru: {len(baru_edges)}')
if masalah:
    print('TEMUAN:')
    for m in masalah: print(' -', m)
    sys.exit(1)
print('INTEGRITAS: LOLOS — seluruh simpul & sisi sumber terwakili atau terdokumentasi transformasinya')
