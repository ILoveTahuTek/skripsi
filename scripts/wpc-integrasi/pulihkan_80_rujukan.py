#!/usr/bin/env python3
"""Pulihkan 80 rujukan asli (permintaan pemilik, Task 37).
Strategi: draft-final.md dikembalikan ke backup pra-WPC (teks asli, sitasi [1]-[80]),
lalu 4 blok integrasi WPC (gelombang 1+2) dicangkok kembali dari draft 63-rujukan:
  A. kalimat 3.2.3 (T2): "memakai pipeline pelatihan YOLO26 ..."
  B. Tabel 3.2: 12 baris (baris 5 = repositori WPC)
  C. 3.4: klausa "kode dan data pelatihan ... diverifikasi kelengkapannya (Tabel 3.2)"
  D. 3.7.4 par.2: dirinci + mAP50 0,8944; sitasi Ultralytics [34]->[42] (penomoran asli)
Log Perubahan gelombang 1-2 disalin ulang, lalu log gelombang 3 (pemulihan) ditambahkan.
"""
from pathlib import Path
import re, sys

DIR = Path("/home/z/my-project/download/translator-sibi-final")
BACKUP = (DIR / "_kerja/draft-final.sebelum-wpc.md").read_text(encoding="utf-8")
KINI = (DIR / "draft-final.md").read_text(encoding="utf-8")
PENANDA = "<!-- ===== AKHIR NASKAH — DI BAWAH INI LOG, TIDAK DIKONVERSI KE DOCX ===== -->"

def paragraf(teks, awal):
    for line in teks.split("\n"):
        if line.startswith(awal):
            return line
    raise SystemExit(f"paragraf '{awal}...' tidak ditemukan")

def blok_tabel(teks, judul):
    m = re.search(re.escape(judul) + r"\n\n(?:\|[^\n]*\n)+", teks)
    if not m:
        raise SystemExit(f"tabel '{judul}' tidak ditemukan")
    return m.group(0)

hasil = BACKUP

# ---- Cangkok A: kalimat 3.2.3 ----
lama_a = ("Model guru YOLO26-Pose menjalani pelatihan lanjutan pada data visual SIBI "
          "di layanan server GPU Kaggle, lalu kualitas *keypoint*-nya dievaluasi sebelum dipakai (Subbab 3.7.4).")
baru_a = ("Model guru YOLO26-Pose menjalani pelatihan lanjutan pada data visual SIBI "
          "di layanan server GPU Kaggle memakai pipeline pelatihan YOLO26 yang telah terimplementasi "
          "pada repositori milik peneliti (Subbab 3.7.4), lalu kualitas *keypoint*-nya dievaluasi sebelum dipakai.")
assert lama_a in hasil, "A: kalimat asli tidak ditemukan"
hasil = hasil.replace(lama_a, baru_a)

# ---- Cangkok B: Tabel 3.2 (12 baris, baris 5 = WPC) ----
t_backup = blok_tabel(hasil, "Tabel 3.2 Perangkat lunak penelitian")
t_wpc = blok_tabel(KINI, "Tabel 3.2 Perangkat lunak penelitian")
assert "| 5 | Repositori pipeline pelatihan YOLO26 (WPC) milik peneliti |" in t_wpc
baris_data = lambda t: sum(1 for l in t.split("\n") if l.startswith("| ") and not l.startswith("| No.") and not l.startswith("|---"))
assert baris_data(t_backup) == 11, f"B: tabel backup {baris_data(t_backup)} baris data, harapan 11"
assert baris_data(t_wpc) == 12, f"B: tabel WPC {baris_data(t_wpc)} baris data, harapan 12"
hasil = hasil.replace(t_backup, t_wpc)

# ---- Cangkok C: klausa bahan penelitian 3.4 ----
lama_c = ("Bahan penelitian meliputi *dataset* CSI beserta deret pose guru hasil perekaman sendiri, "
          "lembar definisi isyarat,")
baru_c = ("Bahan penelitian meliputi *dataset* CSI beserta deret pose guru hasil perekaman sendiri, "
          "kode dan data pelatihan model guru YOLO26 dari repositori milik peneliti "
          "yang telah diverifikasi kelengkapannya (Tabel 3.2), lembar definisi isyarat,")
assert lama_c in hasil, "C: klausa asli tidak ditemukan"
hasil = hasil.replace(lama_c, baru_c)

# ---- Cangkok D: 3.7.4 par.2 (sitasi Ultralytics [34] -> [42]) ----
p_wpc = paragraf(KINI, "Guru menjalani pelatihan lanjutan")
p_wpc = p_wpc.replace("ekspor model Ultralytics [34]", "ekspor model Ultralytics [42]")
assert "0,8944" in p_wpc and "[42]" in p_wpc, "D: isi paragraf WPC tidak lengkap"
lama_d = paragraf(hasil, "Guru menjalani pelatihan lanjutan")
hasil = hasil.replace(lama_d, p_wpc)

# ---- Pisahkan badan naskah vs log: potong di kemunculan PERTAMA penanda/log ----
pos_tanda = hasil.find(PENANDA)
m_log = re.search(r"^## Log Perubahan", hasil, flags=re.M)
pos_log = m_log.start() if m_log else len(hasil)
potong = min(p for p in (pos_tanda, pos_log) if p != -1)
badan = hasil[:potong].rstrip("\n") + "\n\n" + PENANDA + "\n"

def log_dari(teks, judul):
    m = re.search(re.escape(judul) + r".*?(?=^## |\Z)", teks, flags=re.M | re.S)
    if not m:
        raise SystemExit(f"log '{judul}' tidak ditemukan")
    return m.group(0).rstrip("\n")

log_g1 = log_dari(KINI, "## Log Perubahan — Revisi 6 November 2026 (integrasi pipeline WPC")
log_g2 = log_dari(KINI, "## Log Perubahan — Revisi 6 November 2026, gelombang 2")

log_g3 = """## Log Perubahan — Revisi 6 November 2026, gelombang 3 (pemulihan 80 rujukan)

| Lokasi | Sebelum (gelombang 1-2) | Sesudah (gelombang 3) | Alasan |
|---|---|---|---|
| Seluruh naskah | Daftar Pustaka 63 entri (17 rujukan berbayar dihapus pada gelombang 1; sitasi yang rujukannya terhapus ditulis ulang; seluruh sitasi dinomori ulang [1]-[63]) | Daftar Pustaka dikembalikan ke 80 entri asli dengan penomoran asli [1]-[80]; seluruh kalimat asli tempat 17 rujukan tersebut dikutip dipulihkan apa adanya (Tabel 2.2 kembali 17 baris) | Permintaan pemilik 7 Nov 2026: proposal memakai 80 rujukan yang sama seperti sebelumnya |
| 3.2.3, Tabel 3.2, 3.4, 3.7.4 | (dipertahankan) | Integrasi pipeline WPC dari gelombang 1-2 dipertahankan utuh melalui pencangkokan 4 blok: kalimat 3.2.3, Tabel 3.2 baris 5, klausa bahan 3.4, dan paragraf 3.7.4 (sitasi Ultralytics disesuaikan [34]->[42] ke penomoran asli) | Rujukan dipulihkan tanpa membuang hasil audit repositori WPC |

Catatan: ke-17 rujukan yang dipulihkan adalah rujukan berbayar/cetak yang akses salinannya terbatas; seluruh dokumennya tetap tersedia pada paket ZIP 80 rujukan (Gofile)."""

hasil = badan.rstrip("\n") + "\n\n" + log_g1 + "\n\n" + log_g2 + "\n\n" + log_g3 + "\n"

# ---- Tulis draft-final.md ----
(DIR / "draft-final.md").write_text(hasil, encoding="utf-8")

# ---- Rebuild naskah-untuk-docx.md (badan saja, tanpa log) ----
naskah = hasil.partition(PENANDA)[0].rstrip("\n") + "\n"
(DIR / "_kerja/naskah-untuk-docx.md").write_text(naskah, encoding="utf-8")

# ---- Regenerasi daftar-pustaka.md tingkat atas ----
m = re.search(r"^# DAFTAR PUSTAKA.*?(?=^<!-- |\Z)", naskah, flags=re.M | re.S)
(DIR / "daftar-pustaka.md").write_text(m.group(0).rstrip("\n") + "\n", encoding="utf-8")

# ---- Verifikasi ----
dp = re.findall(r"^\[(\d+)\] ", naskah, flags=re.M)
angka = sorted(set(int(x) for x in dp))
sitasi = set(int(x) for x in re.findall(r"\[(\d+)\]", naskah.partition("# DAFTAR PUSTAKA")[0]))
print(f"DP: {len(dp)} entri, nomor {angka[0]}..{angka[-1]}, urut={angka == list(range(1, 81))}")
print(f"Sitasi balik: {len(sitasi & set(angka))}/80 dirujuk; menggantung={sorted(sitasi - set(angka))}; >80={sorted(set(angka) - sitasi - {0})[:5]}")
for frasa in ["Repositori pipeline pelatihan YOLO26 (WPC)", "diverifikasi kelengkapannya",
              "0,8944", "ekspor model Ultralytics [42]", "Mitchell dan Karchmer [1], [2]"]:
    print(("ADA " if frasa in naskah else "HILANG ") + frasa)
print("Baris naskah-untuk-docx:", naskah.count("\n"))
