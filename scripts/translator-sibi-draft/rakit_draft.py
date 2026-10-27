#!/usr/bin/env python3
# rakit_draft.py — Rakit dokumen utuh + verifikasi menyeluruh draft proposal
# Sumber: download/translator-sibi-draft/{bab1,bab2,bab3,daftar-pustaka}.md
import re, sys, os

BASE = '/home/z/my-project/download/translator-sibi-draft'
OUT = os.path.join(BASE, 'Draft-Proposal-Translator-SIBI.md')

HEADER = """# Purwarupa Penerjemah Dua Arah Isyarat SIBI Berbasis Wi-Fi Channel State Information pada Modul ESP32-S3 dengan Inferensi Tepi dan Pemrosesan Bahasa pada Server: Studi Kelayakan Kosakata Terbatas

**PROPOSAL PENELITIAN**

| Identitas | Keterangan |
|---|---|
| Judul | Purwarupa Penerjemah Dua Arah Isyarat SIBI Berbasis Wi-Fi *Channel State Information* pada Modul ESP32-S3 dengan Inferensi Tepi dan Pemrosesan Bahasa pada Server: Studi Kelayakan Kosakata Terbatas |
| Jenis dokumen | Proposal penelitian (seminar proposal), BAB I–III + Daftar Pustaka |
| Disusun oleh | [PERLU DATA: nama penulis] |
| NIM | [PERLU DATA: NIM penulis] |
| Program studi | [PERLU DATA: program studi] |
| Universitas | [PERLU DATA: nama universitas] |
| Pembimbing | [PERLU DATA: nama pembimbing, bila sudah ditetapkan] |
| Tahun | [PERLU DATA: tahun penyusunan] |

> Catatan penyusunan: draft utuh ini disusun dari dossier bahan `Bahan-Proposal-Translator-SIBI.md` (26 Oktober 2026) dan proposal revisi terverifikasi, dengan struktur serta register korpus sempro-mepet, kaidah bahasa naskah-id (EYD V), dan optimasi kata berjenjang GEPA pada kalimat kritis. Metodologi utama naskah adalah distilasi guru–murid: YOLO26-Pose sebagai guru kamera yang mensupervisi pelatihan murid CSI untuk inferensi tepi pada ESP32-S3. Naskah memuat diagram hanya pada BAB III (Gambar 3.1–3.6) yang tersimpan sebagai berkas Mermaid pada folder `diagram/`; berkas diagram BAB I–II (G1.1, G1.2, G2.1–G2.3) tetap tersimpan pada folder yang sama sebagai konteks bacaan dan tidak dimuat di naskah. Penanda `[PERLU DATA: ...]` menandai keputusan yang menunggu pemilik penelitian, pembimbing, atau hasil tahap sebelumnya.

---

"""

def read(name):
    with open(os.path.join(BASE, name), encoding='utf-8') as f:
        return f.read().strip() + '\n'

parts = [HEADER, read('bab1-pendahuluan.md'), '', read('bab2-kajian-pustaka.md'), '',
         read('bab3-metodologi.md'), '', '---', '', read('daftar-pustaka.md')]
doc = '\n'.join(parts)
with open(OUT, 'w', encoding='utf-8') as f:
    f.write(doc)

# ============ VERIFIKASI ============
body = parts[1] + '\n' + parts[3] + '\n' + parts[5]  # bab 1-3 saja (tanpa header & DP)
full = doc
errors, warns, oks = [], [], []

def ok(msg): oks.append(msg)
def err(msg): errors.append(msg)
def warn(msg): warns.append(msg)

# 1. Daftar Pustaka 1..80
dp = re.findall(r'^\[(\d+)\] ', read('daftar-pustaka.md'), re.M)
dp_nums = [int(x) for x in dp]
if dp_nums == list(range(1, 81)):
    ok('Daftar Pustaka lengkap 1..80')
else:
    err(f'DP tidak lengkap/urut: {len(dp_nums)} entri, rentang {min(dp_nums) if dp_nums else "-"}..{max(dp_nums) if dp_nums else "-"}')

# 2. Sitasi dalam tubuh
cites = set()
for m in re.finditer(r'\[(\d+)\]', body):
    cites.add(int(m.group(1)))
# rentang [14]-[17] dsb: tangkap angka di dalam "[a], [b]" dan "[a]-[b]"
for m in re.finditer(r'\[(\d+)\]-\[(\d+)\]', body):
    a, b = int(m.group(1)), int(m.group(2))
    for n in range(a, b+1): cites.add(n)
    # hapus bentuk rentang agar tidak dihitung ganda sebagai dua situs sah — tetap sah
missing_cite = [n for n in cites if n < 1 or n > 80]
if missing_cite: err(f'Sitasi di luar 1..80: {sorted(missing_cite)}')
else: ok(f'Semua sitasi tubuh dalam 1..80 ({len(cites)} nomor unik)')
uncited = [n for n in dp_nums if n not in cites]
if uncited: err(f'Entri DP tak pernah dikutip: {uncited}')
else: ok('Seluruh 80 entri DP dikutip minimal sekali')

# 3. Blok mermaid + caption gambar (revisi 26 Okt 2026: diagram BAB I-II dikeluarkan dari naskah,
#    berkas .mmd tetap di folder diagram/ sebagai konteks. Revisi sesi 2 (26 Okt 2026): metodologi
#    utama = distilasi guru-murid; BAB III memuat Gambar 3.1-3.6 (G3.2 baru: alur teacher-student).
EXP_CAPS = ['3.1', '3.2', '3.3', '3.4', '3.5', '3.6']
n_mmd = len(re.findall(r'```mermaid', body))
caps = re.findall(r'^Gambar (\d+\.\d+) ', body, re.M)
if n_mmd == 6: ok('6 blok mermaid pada tubuh (BAB III saja)')
else: err(f'Blok mermaid = {n_mmd}, harusnya 6')
if caps == EXP_CAPS: ok('6 caption Gambar 3.1-3.6 urut')
else: err(f'Caption Gambar = {len(caps)}: {caps} (harusnya {EXP_CAPS})')
# setiap Gambar X.Y dirujuk di prosa (di luar caption)
for g in caps:
    n_ref = len(re.findall(rf'Gambar {re.escape(g)}\b', body)) - 1  # -1 = caption sendiri
    if n_ref >= 1: pass
    else: err(f'Gambar {g} tidak dirujuk prosa')
if caps: ok('Semua gambar dirujuk prosa minimal sekali')

# 4. Tabel dirujuk
tab_caps = re.findall(r'^Tabel (\d+\.\d+) ', body, re.M)
expected_tabs = ['2.1','2.2','3.1','3.2','3.3','3.4','3.5','3.6','3.7']
for t in expected_tabs:
    if t not in tab_caps: err(f'Tabel {t} tidak memiliki caption')
    n_ref = len(re.findall(rf'Tabel {re.escape(t)}\b', body)) - 1
    if n_ref < 1: err(f'Tabel {t} tidak dirujuk prosa')
if not [e for e in errors if 'Tabel' in e]: ok(f'Semua {len(expected_tabs)} tabel berkaption & dirujuk prosa')

# 5. Penanda
n_data = len(re.findall(r'\[PERLU DATA: [^\]]+\]', full))
n_ruj = len(re.findall(r'\[PERLU RUJUKAN: [^\]]+\]', full))
ok(f'Penanda PERLU DATA = {n_data}, PERLU RUJUKAN = {n_ruj}')
if n_ruj > 0: warn('Ada PERLU RUJUKAN tersisa — periksa manual')

# 6. Cermin rumusan <-> tujuan (3:3, verba pertama) — cakupan hanya seksi 1.2-1.3
sec_12_13 = body.split('## 1.2 Rumusan Masalah')[1].split('## 1.4')[0]
n_rum = len(re.findall(r'^\d+\. Bagaimana', sec_12_13, re.M))
n_tuj = len(re.findall(r'^\d+\. (Merancang|Mengukur|Menguji)', sec_12_13, re.M))
if n_rum == 3 and n_tuj == 3: ok('Rumusan (3 butir) <-> Tujuan (3 butir) cermin 1:1')
else: err(f'Rumusan={n_rum}, Tujuan={n_tuj} — harus 3:3')

# 7. Pola terlarang / K-level
pat_forbidden = [
    (r'adalah merupakan', 'adalah merupakan (pleonasma)'),
    (r'agar supaya', 'agar supaya'),
    (r'memainkan peran', 'memainkan peran'),
    (r'\bdi mana\b', 'di mana sebagai penghubung'),
    (r'\byang mana\b', 'yang mana sebagai penghubung'),
    (r'menggunakkan', 'salah ketik menggunakkan'),
    (r'Di era ', 'pembuka kosmik Di era'),
    (r'Seiring perkembangan', 'pembuka kosmik Seiring'),
    (r'Tidak dapat dipungkiri', 'empty assertive'),
    (r'Perlu diingat', 'lecture voice'),
    (r'Mari kita', 'lecture voice'),
    (r'\bmemeringkas\b', 'salah ketik memeringkas'),
    (r'\bantarmodu\b(?!l)', 'salah ketik antarmodu'),
    (r'\bbermutru\b', 'salah ketip bermutru'),
    (r'\bpenolangan\b', 'salah ketik penolangan'),
    (r'\bmemerikan\b', 'salah ketik memerikan'),
    (r'\bmenelusari\b', 'salah ketik menelusari'),
    (r'revisi sebelumnya', 'meta-bahasa revisi tertinggal'),
    (r'Proposal-Revisi', 'referensi internal tertinggal'),
    (r'\bdari hasil .* menunjukkan', 'subjek hilang'),
    (r'[A-Za-z0-9] +(,|\.|;|:)', 'spasi sebelum tanda baca'),
    (r'\S\(', 'tanpa spasi sebelum kurung buka'),
]
# prose tubuh tanpa blok kode & tanpa DP (judul karya di DP verbatim, tak boleh disentuh)
prose_lines, _in = [], False
for line in body.split('\n'):
    if line.strip().startswith('```'):
        _in = not _in; prose_lines.append(''); continue
    prose_lines.append('' if _in else line)
prose_txt = '\n'.join(prose_lines)
for pat, name in pat_forbidden:
    hits = re.findall(pat, prose_txt)
    if hits:
        sample = [m.group(0)[:50] for m in re.finditer(pat, prose_txt)][:3]
        err(f'Pola terlarang "{name}": {len(hits)} kemunculan — contoh: {sample}')
if not [e for e in errors if 'Pola terlarang' in e]: ok('Bebas pola terlarang K/AI yang diperiksa')

# 8. Panjang kalimat prosa (>40 kata) — heuristik, abaikan baris tabel/list/kode/caption
def is_enumeration(sent, line=''):
    return (sent.count(',') >= 4) or (':' in sent and sent.count(',') >= 3) or line.startswith('**BAB')
long_sents = []
in_code = False
for line in body.split('\n'):
    if line.strip().startswith('```'):
        in_code = not in_code; continue
    if in_code: continue
    s = line.strip()
    if not s or s.startswith('|') or s.startswith('#') or s.startswith('>') or re.match(r'^\d+\.', s) or s.startswith('Gambar') or s.startswith('Tabel') or s.startswith('-'):
        continue
    for sent in re.split(r'(?<=[.;]) ', s):
        words = len(re.findall(r'\S+', sent))
        limit = 45 if is_enumeration(sent, s) else 40
        if words > limit:
            long_sents.append((words, sent[:90]))
if long_sents:
    warn(f'{len(long_sents)} kalimat prosa >40 kata (periksa pecah manual):')
    for w, s in long_sents[:12]: warn(f'   {w} kata: {s}...')
else: ok('Tidak ada kalimat prosa >40 kata')

# 9. Struktur bab lengkap
need = {
 'BAB I': ['1.1 Latar Belakang','1.2 Rumusan Masalah','1.3 Tujuan Penelitian','1.4 Batasan Masalah','1.5 Manfaat Penelitian','1.6 Sistematika Penulisan'],
 'BAB II': ['2.1 Bahasa Isyarat','2.2 Kebutuhan Komunikasi','2.3 Wi-Fi Channel State Information','2.4 Modul ESP32-S3','2.5 Estimasi Pose','2.6 Pengenalan Isyarat dan Gestur','2.7 TTS dan ASR','2.8 Pemetaan Teks','2.9 Komunikasi Modul','2.10 Evaluasi Kelayakan','2.11 Penelitian Terdahulu'],
 'BAB III': ['3.1 Desain Penelitian','3.2 Tahapan Penelitian','3.3 Waktu dan Lokasi','3.4 Alat dan Bahan','3.5 Perancangan Sistem','3.6 Protokol Perekaman','3.7 Pengolahan Sinyal','3.8 Skenario Pengujian','3.9 Jadwal','3.10 Parameter','3.11 Risiko'],
}
for bab, subs in need.items():
    for sub in subs:
        if sub not in body: err(f'Struktur kurang: {bab} — {sub}')
if not [e for e in errors if 'Struktur kurang' in e]: ok('Struktur BAB I-III lengkap (6+11+11 subbab)')

# 10. Akronim pertama-pakai: TTS/ASR tak boleh muncul di prosa BAB I (MMS-TTS-ind = nama model, dikecualikan)
bab1_lines, _in, bab1_prose = body.split('# BAB II')[0].split('\n'), False, []
for line in bab1_lines:
    if line.strip().startswith('```'):
        _in = not _in; continue
    if not _in: bab1_prose.append(line)
for ab in ['TTS', 'ASR']:
    hits = [l for l in bab1_prose if re.search(rf'(?<!MMS-)(?<![-\w]){ab}\b(?!-ind)', l) and not l.strip().startswith('|')]
    if hits:
        warn(f'Akronim {ab} muncul di prosa BAB I: {hits[:2]}')
    else:
        ok(f'Akronim {ab} tidak muncul di prosa BAB I (didefinisikan di 2.7)')

print('='*64)
print(f'DOKUMEN UTUH: {OUT}')
print(f'  {len(doc.splitlines())} baris, {len(doc.split())} kata, {len(dp)} entri DP')
print('='*64)
for o in oks: print(f'  [OK]   {o}')
for w in warns: print(f'  [WARN] {w}')
for e in errors: print(f'  [ERR]  {e}')
print('='*64)
print(f'RESULT: {"LOLOS" if not errors else "GAGAL"} — {len(oks)} ok, {len(warns)} warn, {len(errors)} err')
sys.exit(1 if errors else 0)
