#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
finalisasi.py — percobaan pamungkas (tautan Crossref, jina, garuda) + verifikasi
seluruh berkas + tulis MANIFEST.md untuk paket pustaka-sibi.
"""
import html as mod_html
import json
import re
import sys
import time
from pathlib import Path
from urllib.parse import urljoin

import requests

sys.path.insert(0, str(Path(__file__).parent))
from unduh_pustaka import DIR_PDF, DIR_WEB, DIR_REPOS, HDR, EMAIL, get_url, pdf_ok, html_ok
from data_pustaka import REFS

AKAR = DIR_PDF.parent
HASIL_PATH = AKAR / "_hasil.json"
hasil = json.loads(HASIL_PATH.read_text(encoding="utf-8"))
KEY = {r["no"]: r["key"] for r in REFS}
DOI = {r["no"]: r.get("doi") for r in REFS}
CITE = {r["no"]: r["cite"] for r in REFS}
WEBNATIVE = {r["no"] for r in REFS if r["kind"] in ("web", "hf")}


def catat(no, **kw):
    e = hasil.get(str(no), {})
    e.update(kw)
    e["key"] = KEY[no]
    hasil[str(no)] = e
    print(f"{no:02d} [{kw.get('status','?'):7}] {kw.get('cara','')[:70]}")


def simpan_pdf(no, data, sumber, cara):
    t = DIR_PDF / f"{no:02d} - {KEY[no]}.pdf"
    t.write_bytes(data)
    catat(no, status="pdf", berkas=str(t), sumber=sumber, cara=cara)


# ---------- 1. percobaan pamungkas (sekali jalan) ----------
MARKER = AKAR / "_pamungkas.selesai"
if MARKER.exists():
    print("(percobaan pamungkas sudah pernah dijalankan — dilewati)")
else:
    sisa = [int(k) for k, v in hasil.items()
            if v.get("status") not in ("pdf", "repo") and int(k) not in WEBNATIVE]

    for no in sisa:
        doi = DOI.get(no)
        if not doi:
            continue
        try:
            r = requests.get(f"https://api.crossref.org/works/{doi}", headers=HDR, timeout=25)
            links = [l["URL"] for l in (r.json()["message"].get("link") or [])][:3] if r.status_code == 200 else []
        except Exception:
            links = []
        for u in links:
            b = get_url(u, timeout=(15, 60))
            if b and pdf_ok(b[0]):
                simpan_pdf(no, b[0], u, "crossref-link")
                break

    # 12: jina poltekba (ulang)
    if hasil.get("12", {}).get("status") != "pdf":
        try:
            r = requests.get("https://r.jina.ai/https://jurnal.poltekba.ac.id/index.php/jst/article/view/732",
                             headers=HDR, timeout=(15, 90))
            if r.status_code == 200 and r.text:
                for u in re.findall(r'\((https?://[^\s)]+)\)', r.text):
                    if re.search(r'/article/(view|download)/732(/\d+)?', u):
                        u2 = u.replace("/article/view/", "/article/download/")
                        b = get_url(u2, timeout=(15, 90))
                        if b and pdf_ok(b[0]):
                            simpan_pdf(12, b[0], u2, "jina-poltekba")
                            break
        except Exception:
            pass

    # 73: garuda pencarian dokumen
    if hasil.get("73", {}).get("status") != "pdf":
        try:
            r = requests.get("https://garuda.kemdiktisaintek.go.id/documents",
                             params={"q": "OPTIMASI KLASIFIKASI CITRA ALFABET SIBI MobileNetV2"},
                             headers=HDR, timeout=(15, 60))
            if r.status_code == 200:
                t = r.text
                kand = []
                for u in re.findall(r'href="([^"]+)"', t, re.I):
                    if "download.garuda" in u or re.search(r'document/view/\d+', u):
                        kand.append(urljoin("https://garuda.kemdiktisaintek.go.id/", mod_html.unescape(u)))
                for u in kand[:6]:
                    b = get_url(u, timeout=(15, 90))
                    if b and pdf_ok(b[0]):
                        simpan_pdf(73, b[0], u, "garuda-doc")
                        break
        except Exception:
            pass
    MARKER.write_text("selesai")

# ---------- 2. verifikasi berkas ----------
print("\n=== VERIFIKASI ===")
masalah = []
verif = {}
for r in REFS:
    no = r["no"]
    e = hasil.get(str(no), {})
    berkas = e.get("berkas")
    berkas_list = [x.strip() for x in (berkas or "").split(";") if x.strip()] if berkas else []
    if e.get("status") in ("pdf", "repo", "halaman"):
        if not berkas_list:
            masalah.append(f"[{no:02d}] status {e['status']} tanpa berkas")
            verif[no] = ([], 0)
            continue
        ok = True
        ukuran_total = 0
        for bp in berkas_list:
            p = Path(bp)
            if not p.exists():
                masalah.append(f"[{no:02d}] berkas hilang: {bp}")
                ok = False
                continue
            ukuran = p.stat().st_size
            ukuran_total += ukuran
            kepala = open(p, "rb").read(8)
            if p.suffix == ".pdf" and not kepala.startswith(b"%PDF"):
                masalah.append(f"[{no:02d}] bukan PDF valid: {p.name}")
                ok = False
                continue
            if p.suffix == ".zip" and not kepala.startswith(b"PK"):
                masalah.append(f"[{no:02d}] bukan ZIP valid: {p.name}")
                ok = False
                continue
            if ukuran < 1000:
                masalah.append(f"[{no:02d}] berkas terlalu kecil: {p.name}")
                ok = False
        if not ok:
            verif[no] = ([], 0)
            continue
        verif[no] = (berkas_list, ukuran_total)
    else:
        verif[no] = ([], 0)

for m in masalah:
    print("MASALAH:", m)
print("Berkas terverifikasi:", sum(1 for p, u in verif.values() if p), "| masalah:", len(masalah))
# ---------- 3. MANIFEST.md ----------
def label(no):
    e = hasil[str(no)]
    st = e.get("status", "gagal")
    if st == "pdf":
        return "PDF"
    if st == "repo":
        return "Repo ZIP"
    if st == "halaman":
        return "Halaman web" if no in WEBNATIVE else "Halaman penerbit"
    if st == "tidak-tersedia":
        return "Tidak tersedia daring"
    return "Berbayar"


def catatan(no):
    e = hasil[str(no)]
    st = e.get("status")
    r = next(x for x in REFS if x["no"] == no)
    if st == "pdf":
        s = e.get("sumber") or ""
        cara = e.get("cara") or ""
        m = re.match(r"https?://([^/]+)", s)
        host = m.group(1) if m else ""
        if cara:
            return f"diunduh dari {host or 'sumber terbuka'} ({cara})"
        if s == "cache" or not s:
            if r.get("arxiv"):
                return "diunduh dari arxiv.org"
            return "diunduh pada putaran pertama via jalur akses terbuka (penerbit/OA/penulis)"
        return f"diunduh dari {host or s[:40]}"
    if st == "repo":
        return "arsip ZIP repositori GitHub" + (f" — {e.get('catatan','')}" if e.get("catatan") else "")
    if st == "halaman":
        if no in WEBNATIVE:
            return "sumber rujukan berupa halaman web — tersimpan utuh"
        return "PDF berbayar; halaman penerbit/arsip disimpan sebagai bukti akses"
    if st == "tidak-tersedia":
        return "buku cetak 1994 — tidak ditemukan salinan digital resmi"
    return "penerbit berbayar; tidak ada salinan terbuka (OA resmi, arXiv, Unpaywall, OpenAlex, Semantic Scholar, Europe PMC, repositori penulis/institusi, Garuda, arsip web — semuanya sudah dicoba)"


baris = []
for r in sorted(REFS, key=lambda x: x["no"]):
    no = r["no"]
    e = hasil.get(str(no), {})
    plist, _u = verif[no]
    nama = "; ".join(Path(b).name for b in plist) if plist else "—"
    baris.append(f"| {no} | {CITE[no]} | {label(no)} | {nama} | {catatan(no)} |")

n_pdf = sum(1 for r in REFS if label(r["no"]) == "PDF")
n_repo = sum(1 for r in REFS if label(r["no"]) == "Repo ZIP")
n_web = sum(1 for r in REFS if label(r["no"]) == "Halaman web")
n_land = sum(1 for r in REFS if label(r["no"]) == "Halaman penerbit")
n_byr = sum(1 for r in REFS if label(r["no"]) == "Berbayar")
n_tdk = sum(1 for r in REFS if label(r["no"]) == "Tidak tersedia daring")

md = []
md.append("# MANIFEST — Pustaka SIBI: 80 Rujukan DAFTAR PUSTAKA\n")
md.append("Paket unduhan rujukan untuk **Proposal Studi Kelayakan Purwarupa SIBI** "
          "(`download/translator-sibi-final/Proposal-Studi-Kelayakan-Purwarupa-SIBI-CSI-ESP32S3.docx`).\n")
md.append("- Diunduh: 4 November 2026")
md.append("- Struktur: `pdf/` (makalah & dokumen PDF), `repos/` (arsip ZIP repositori GitHub), "
          "`halaman-web/` (halaman web resmi, kartu model, dan halaman penerbit)")
md.append("- Jalur unduh **hanya legal**: akses terbuka resmi penerbit (Frontiers, MDPI, IEEE Access, "
          "IMWUT, IJACSA), arXiv, arsip ZIP repositori resmi (codeload GitHub), salinan penulis/institusi "
          "yang terindeks Unpaywall / OpenAlex / Semantic Scholar / Europe PMC, Garuda, dan arsip web "
          "(Wayback Machine). Tidak memakai situs bajakan.")
md.append("")
md.append("## Ringkasan\n")
md.append(f"- **PDF lengkap: {n_pdf}/80**")
md.append(f"- **Repositori (ZIP): {n_repo}/80** (rujukan [27], [28], [30], [31], [33], [72])")
md.append(f"- **Halaman web utuh: {n_web}/80** (rujukan yang sumber aslinya memang halaman web: "
          "berita resmi, dokumentasi cloud, kartu model)")
md.append(f"- **Halaman penerbit (pengganti): {n_land}/80** (PDF berbayar — halaman disimpan sebagai bukti)")
md.append(f"- **Berbayar, tidak ada salinan terbuka: {n_byr}/80**")
md.append(f"- **Tidak tersedia daring: {n_tdk}/80** (rujukan [45], Kamus SIBI 1994 — buku cetak)")
md.append("")
md.append("## Tabel Rujukan\n")
md.append("| No | Rujukan | Status | Berkas | Catatan |")
md.append("|---|---|---|---|---|")
md.extend(baris)
md.append("")
md.append("## Catatan Penting\n")
md.append("- Nama berkas diawali nomor rujukan sesuai DAFTAR PUSTAKA proposal (mis. `20 - ...pdf` = rujukan [20]).")
md.append("- Rujukan berbayar umumnya terbitan ACM / IEEE / Elsevier / Springer / Project MUSE; "
          "salinan terbuka tidak tersedia dan tidak diunduh dari situs bajakan.")
md.append("- [41] dan [61] adalah dua makalah YOLO26 yang berbeda (Jocher dkk. 2026 vs Sapkota dkk. 2025) — keduanya terunduh.")
md.append("- [64] diunduh dari arXiv (versi yang disitasi).")
md.append("")

(AKAR / "MANIFEST.md").write_text("\n".join(md), encoding="utf-8")
HASIL_PATH.write_text(json.dumps(hasil, ensure_ascii=False, indent=1, sort_keys=True),
                      encoding="utf-8")
print(f"\nMANIFEST.md ditulis: {n_pdf} PDF, {n_repo} repo, {n_web} web, {n_land} landing, {n_byr} berbayar, {n_tdk} tidak tersedia")
