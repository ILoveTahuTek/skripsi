#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verifikasi_pustaka.py — Verifikasi akhir 80 rujukan + buat LAPORAN-PENGUNDUHAN.md.
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, "/home/z/my-project/scripts/translator-sibi-pustaka")
from data_pustaka import REFS

AKAR = Path("/home/z/my-project/download/pustaka-sibi")
HASIL = AKAR / "_hasil.json"
hasil = json.loads(HASIL.read_text(encoding="utf-8"))


def cek_berkas(path):
    p = Path(path)
    if not p.exists():
        return False, "berkas tidak ada"
    b = p.read_bytes()[:2048]
    if p.suffix == ".pdf":
        return len(b) > 0 and b.lstrip()[:5].startswith(b"%PDF"), ""
    if p.suffix == ".zip":
        return b[:2] == b"PK", ""
    if p.suffix == ".json":
        try:
            json.loads(p.read_text(encoding="utf-8"))
            return True, ""
        except Exception:
            return False, "JSON rusak"
    return p.stat().st_size > 1500, ""


baris = []
masalah = []
n = {}
for ref in REFS:
    no, key = ref["no"], ref["key"]
    h = hasil.get(str(no), {})
    st = h.get("status", "TIDAK ADA")
    n[st] = n.get(st, 0) + 1
    berkas = h.get("berkas", "")
    ok, pesan = ("-", "")
    if berkas:
        hasil_cek = [cek_berkas(b.strip()) for b in berkas.split(";") if b.strip()]
        ok = "OK" if all(o for o, _ in hasil_cek) else "RUSAK"
        pesan = "; ".join(pp for o, pp in hasil_cek if pp)
        if ok == "RUSAK":
            masalah.append(f"{no:02d}: {pesan}")
    sumber = h.get("sumber", h.get("catatan", ""))
    baris.append((no, key, ref["cite"], st, berkas, ok, sumber))

# tulis laporan
garis = []
garis.append("# Laporan Pengunduhan 80 Rujukan — Proposal SIBI-CSI-ESP32S3")
garis.append("")
garis.append(f"Tanggal: {json.loads(HASIL.read_text(encoding='utf-8')).get('_tanggal', '2026-11-04')}")
garis.append("")
garis.append("## Ringkasan")
garis.append("")
garis.append("| Status | Arti | Jumlah |")
garis.append("|---|---|---|")
arti = {
    "pdf": "Dokumen lengkap (PDF)",
    "repo": "Arsip repositori kode (ZIP GitHub)",
    "halaman": "Halaman sumber resmi tersimpan (HTML) — kartu model, dokumentasi, berita",
    "metadata": "Tidak ada salinan terbuka legal; metadata resmi penerbit (Crossref) tersimpan",
    "gagal": "Tidak tersedia digital — buku cetak murni (lihat catatan)",
}
for k in ("pdf", "repo", "halaman", "metadata", "gagal"):
    garis.append(f"| {k} | {arti[k]} | {n.get(k, 0)} |")
garis.append(f"| **total** | | **{len(baris)}** |")
garis.append("")
garis.append("Seluruh pengunduhan memakai jalur legal: arXiv, jurnal akses-terbuka "
             "(OJS kampus, Frontiers, MDPI, ACM OA), halaman lab penulis, JDIH/Wikisource, "
             "codeload GitHub, kartu model Hugging Face, dan API Unpaywall/OpenAlex/"
             "Semantic Scholar. Tidak memakai situs bajakan.")
garis.append("")
garis.append("## Rincian per Rujukan")
garis.append("")
garis.append("| No | Status | Berkas/SumBER |")
garis.append("|---|---|---|")
for no, key, cite, st, berkas, ok, sumber in baris:
    rel = str(berkas).replace(str(AKAR) + "/", "") if berkas else ""
    tanda = "" if ok in ("-", "OK") else f" ⚠️ {ok}"
    garis.append(f"| {no} | {st}{tanda} | {rel or sumber[:90]} |")
garis.append("")
garis.append("## Catatan Rujukan Berbayar/Tidak-Tersedia")
garis.append("")
for no, key, cite, st, berkas, ok, sumber in baris:
    if st in ("metadata", "gagal"):
        h = hasil[str(no)]
        cat = h.get("catatan", "")
        garis.append(f"- **[{no}]** {cite} — {cat}")

lap = AKAR / "LAPORAN-PENGUNDUHAN.md"
lap.write_text("\n".join(garis), encoding="utf-8")

print(f"Verifikasi: {len(baris)} rujukan")
print(f"Status: {n}")
print(f"Masalah: {masalah if masalah else 'tidak ada'}")
print(f"Laporan: {lap}")
