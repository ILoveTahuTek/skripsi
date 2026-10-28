#!/usr/bin/env python3
"""Verifikasi paket bahan Claude — translator-sibi-bahan-claude.
Memeriksa: keberadaan berkas, salinan naskah identik, jumlah penanda/mermaid/rujukan,
judul terkunci, dan aturan-aturan kunci hadir di berkas poin."""
import hashlib
import re
import sys
from pathlib import Path

PAKET = Path("/home/z/my-project/download/translator-sibi-bahan-claude")
SUMBER_ASAL = Path("/home/z/my-project/download/translator-sibi-draft/Draft-Proposal-Translator-SIBI.md")
JUDUL = ("Purwarupa Penerjemah Dua Arah Isyarat SIBI Berbasis Wi-Fi Channel State "
         "Information pada Modul ESP32-S3 dengan Inferensi Tepi dan Pemrosesan Bahasa "
         "pada Server: Studi Kelayakan Kosakata Terbatas")

galat = []


def periksa(nama, kondisi, detail=""):
    status = "OK" if kondisi else "GALAT"
    print(f"[{status}] {nama}" + (f" — {detail}" if detail else ""))
    if not kondisi:
        galat.append(nama)


# 1. Keberadaan berkas
berkas_wajib = [
    "0-CARA-PAKAI.md", "1-PERAN-DAN-MISI.md", "2-KONTEKS-PROYEK.md",
    "3-STANDAR-BAHASA-DAN-KEJUJURAN.md", "4-ATURAN-DIAGRAM.md", "5-HAL-TERBUKA.md",
    "6-FORMAT-OUTPUT-FINAL.md", "naskah-sumber.md", "PROMPT-SATU-PESAN.md",
    "PROMPT-SATU-FILE-LENGKAP.md",
]
for b in berkas_wajib:
    periksa(f"berkas {b}", (PAKET / b).is_file() and (PAKET / b).stat().st_size > 500)

# 2. Salinan naskah identik dengan sumber
hash_salin = hashlib.sha256((PAKET / "naskah-sumber.md").read_bytes()).hexdigest()
hash_asal = hashlib.sha256(SUMBER_ASAL.read_bytes()).hexdigest()
periksa("naskah-sumber.md identik byte-per-byte dengan draft", hash_salin == hash_asal)

naskah = (PAKET / "naskah-sumber.md").read_text(encoding="utf-8")

# 3. Statistik naskah
baris = naskah.count("\n") + 1
kata = len(naskah.split())
periksa("jumlah baris naskah = 981", baris == 981, str(baris))
periksa("jumlah kata = 16.906 (toleransi ±10)", abs(kata - 16906) <= 10, str(kata))

# 4. Penanda PERLU DATA: 44 penanda + 1 penyebutan konvensi
raw = naskah.count("[PERLU DATA")
sebutan = naskah.count("[PERLU DATA: ...]")
penanda = raw - sebutan
periksa("penanda [PERLU DATA] = 44 (raw {} - sebutan {})", penanda == 44,
        f"penanda={penanda}, raw={raw}, sebutan={sebutan}")

# 5. Blok mermaid = 8; caption Gambar 3.1–3.8 urut
mermaid = len(re.findall(r"```mermaid", naskah))
periksa("blok mermaid = 8", mermaid == 8, str(mermaid))
caption = re.findall(r"^Gambar 3\.(\d) ", naskah, flags=re.M)
periksa("caption Gambar 3.1–3.8 urut", caption == list("12345678"), ",".join(caption))

# 6. Judul terkunci di baris pertama naskah + tabel identitas
periksa("judul terkunci di baris 1 naskah", naskah.splitlines()[0] == f"# {JUDUL}")
periksa("judul di tabel identitas", JUDUL in naskah)

# 7. Daftar Pustaka 80 entri
dp = re.findall(r"^\[(\d+)\] ", naskah, flags=re.M)
periksa("Daftar Pustaka [1]–[80] lengkap", dp == [str(i) for i in range(1, 81)],
        f"jumlah={len(dp)}")

# 8. Aturan kunci hadir di berkas poin
cek_aturan = {
    "0-CARA-PAKAI.md": ["44", "Mermaid", "DOCX"],
    "1-PERAN-DAN-MISI.md": ["whitelist", "blacklist", "naskah-sumber.md", "Minimal-intervensi"],
    "2-KONTEKS-PROYEK.md": [JUDUL, "distilasi guru–murid", "YOLO26-Pose", "16.906"],
    "3-STANDAR-BAHASA-DAN-KEJUJURAN.md": ["EYD V", "96,4%", "80", "modul pemancar (TX)"],
    "4-ATURAN-DIAGRAM.md": ["3.1–3.6", "3.1–3.8", "JANGAN REDESAIN", "verbatim"],
    "5-HAL-TERBUKA.md": ["44", "Tabel 3.6", "27", "Konfirmasi pembimbing"],
    "6-FORMAT-OUTPUT-FINAL.md": ["AKHIR NASKAH", "Log Perubahan", "Daftar Temuan", "Pernyataan verifikasi"],
    "PROMPT-SATU-PESAN.md": [JUDUL, "## 1. Peran dan misi", "## 6. Format output",
                             "AKHIR NASKAH", "Mulailah sekarang", "3.1–3.8"],
}
for nama, kunci in cek_aturan.items():
    teks = (PAKET / nama).read_text(encoding="utf-8")
    for k in kunci:
        periksa(f"{nama} memuat: {k[:52]}", k in teks)

# 9. Varian satu file: prompt + naskah utuh tergabung, penanda jelas
satu_file = (PAKET / "PROMPT-SATU-FILE-LENGKAP.md").read_text(encoding="utf-8")
prompt_teks = (PAKET / "PROMPT-SATU-PESAN.md").read_text(encoding="utf-8").rstrip("\n")
periksa("satu-file memuat prompt satu-pesan UTUH", prompt_teks in satu_file)
periksa("satu-file memuat naskah sumber UTUH", naskah.rstrip("\n") in satu_file)
periksa("satu-file memuat penanda MULAI/SELESAI NASKAH SUMBER",
        "MULAI NASKAH SUMBER" in satu_file and "SELESAI NASKAH SUMBER" in satu_file)
periksa("satu-file memuat catatan pengiriman tanpa lampiran",
        "tanpa lampiran" in (PAKET / "0-CARA-PAKAI.md").read_text(encoding="utf-8"))

# 10. Tidak ada sisa salah ketik 'naskah-source'
sisa = [b.name for b in PAKET.glob("*.md") if "naskah-source" in b.read_text(encoding="utf-8")]
periksa("tidak ada 'naskah-source' tersisa", not sisa, ", ".join(sisa))

print()
if galat:
    print(f"TOTAL: {len(galat)} GALAT — paket BELUM layak kirim")
    sys.exit(1)
print("TOTAL: SEMUA LOLOS — paket layak dikirim ke Claude")
