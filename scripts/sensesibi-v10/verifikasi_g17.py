#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Verifikasi menyeluruh v17: struktur DOCX, konten kunci, sapuan QC sempro-mepet."""
import re
from pathlib import Path
from docx import Document

V = Path("/home/z/my-project/download/sensesibi-v10")
DOCX = V / "Proposal-SenseSIBI-Studi-Kelayakan-v17.docx"
MD = V / "Proposal-SenseSIBI-v17.md"

doc = Document(str(DOCX))
h1 = [p for p in doc.paragraphs if p.style.name == "Heading 1"]
h2 = [p for p in doc.paragraphs if p.style.name == "Heading 2"]
h3 = [p for p in doc.paragraphs if p.style.name == "Heading 3"]
teks = "\n".join(p.text for p in doc.paragraphs)
tabel = doc.tables
print(f"H1: {len(h1)} | H2: {len(h2)} | H3: {len(h3)} | tabel: {len(tabel)} | paragraf: {len(doc.paragraphs)}")

# 1) judul sampul & H1
import zipfile
with zipfile.ZipFile(DOCX) as z:
    cover = z.read("word/document.xml").decode("utf-8")
ok1 = "PEMROSESAN SERVER" in cover and "CLOUD PROCESSING" not in re.sub(r"\| 20 \|.*?keputusan akhiran judul[^<]*", "", cover[:200000])
print("Sampul memakai PEMROSESAN SERVER:", "PEMROSESAN SERVER" in cover)

# 2) konten kunci v17
kunci = [
    ("Persamaan 2.15′ (prima)", "(2.15′)" in teks),
    ("Θtrain di tubuh", "Θtrain" in teks.replace("train", "train")),
    ("kontrak masukan (B, 8)", "(B, 8)" in teks),
    ("gerbang G0b", "G0b" in teks),
    ("probe linear", "probe linear" in teks),
    ("T = 16 langkah", "16 langkah per segmen" in teks),
    ("jendela bergulir H = 0,25", "H = 0,25 detik" in teks),
    ("supervisi label protokol (2.9)", "kartu pemandu" in teks),
    ("PERLU VALIDASI kelas J/Z WPC", "kelas J dan Z pada model juara WPC" in teks),
    ("PERLU VALIDASI normalisasi masukan", "parameter normalisasi masukan pada artefak checkpoint" in teks),
    ("deployment Pilihan 1", "Pilihan 1" in teks),
    ("Tabel 3.7 baris 19 deployment", "Pilihan 1: klasifikator saja" in teks),
    ("Tabel 3.7 baris 20 akhiran judul", "PEMROSESAN SERVER atau CLOUD PROCESSING" in teks),
    ("TTFA", "time-to-first-audio" in teks),
    ("F1 makro 0,45 di G1", "F1 makro sekurang-kurangnya 0,45" in teks),
    ("beban perekaman 780/65/97", "780 repetisi" in teks and "97 menit" in teks),
    ("Delta-CSI koefisien kompleks", "koefisien kanal kompleks" in teks),
    ("varian amplitudo d|H|", "d|H|" in teks),
    ("batas klaim populasi", "indikasi ketahanan awal" in teks),
    ("uji kegunaan framing", "uji kelayakan skala kecil" in teks),
    ("D3 server lokal utama", "jalur utama luring" in teks),
    ("speaker DAC I2S dialirkan", "audio dialirkan" in teks),
    ("Batasan no. 11", "11." in teks and "satu konfigurasi perangkat" in teks),
    ("keadaan tersembunyi per langkah", "keadaan tersembunyi per langkah" in teks),
    ("ringkasan beratensi", "ringkasan beratensi" in teks),
]
gagal = [nama for nama, ok in kunci if not ok]
for nama, ok in kunci:
    if not ok:
        print("  HILANG:", nama)
print(f"Konten kunci: {len(kunci) - len(gagal)}/{len(kunci)} ada")

# 3) sapuan QC sempro-mepet pada teks tubuh (tanpa daftar pustaka dan log)
tubuh = MD.read_text(encoding="utf-8")
tubuh = tubuh[:tubuh.index("<!-- ===== AKHIR NASKAH")]
tubuh_isi = tubuh[tubuh.index("# BAB I "):]

cek = {
    "'bila' di tubuh (harus 0)": len(re.findall(r"\bbila\b", tubuh_isi)),
    "em/en dash prosa (—)": tubuh_isi.count("—"),
    "'adalah merupakan'": tubuh_isi.count("adalah merupakan"),
    "'di mana'/'yang mana' penghubung": len(re.findall(r"(?<!ke )di mana|yang mana", tubuh_isi)),
    "'hal ini'": len(re.findall(r"\bhal ini\b", tubuh_isi, re.I)),
    "'Di era'/'Seiring'/'Tidak dapat dipungkiri'": len(re.findall(r"Di era|Seiring|Tidak dapat dipungkiri", tubuh_isi)),
    "'Perlu diingat'/'Mari kita'": len(re.findall(r"Perlu diingat|Mari kita", tubuh_isi)),
    "'terbukti' (audit klaim)": len(re.findall(r"\bterbukti\b", tubuh_isi)),
    "'sangat' (audit klaim)": len(re.findall(r"\bsangat\b", tubuh_isi)),
    "'signifikan'": len(re.findall(r"\bsignifikan\b", tubuh_isi)),
    "'krusial'/'inovatif'": len(re.findall(r"krusial|inovatif", tubuh_isi)),
    "placeholder bocor {{ }} TODO NaN XXX": len(re.findall(r"\{\{|\}\}|TODO|NaN\b|XXX", tubuh_isi)),
    "koma sebelum 'sehingga'": len(re.findall(r",\s*sehingga", tubuh_isi)),
    "'menggunakkan'/'di hadapi' typo": len(re.findall(r"menggunakkan|di hadapi|di tunjukkan", tubuh_isi)),
    "kata tak baku (analisa/praktek/sistim/aktifitas)": len(re.findall(r"\banalisa\b|\bpraktek\b|\bsistim\b|\baktifitas\b|\bresiko\b|\bobyek\b", tubuh_isi)),
}
for k, v in cek.items():
    print(f"  {k}: {v}")

# 4) sitasi & struktur tabel
nomor_sit = [int(x) for x in re.findall(r"\[(\d+)\]", tubuh_isi)]
print("sitasi maks:", max(nomor_sit), "| unik:", len(set(nomor_sit)))

# 5) jumlah baris tabel kunci
for t in tabel:
    header = " | ".join(c.text for c in t.rows[0].cells)[:70]
    if "Gerbang" in header or "Parameter" in header or "Aspek" in header:
        print(f"  tabel [{len(t.rows)} baris]: {header}")

print("\nSelesai.")
