#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
perbaikan_akhir.py — perbaikan 4 kasus khusus pasca-gelombang-2 (replika Task 30):
  6  : UU 8/2016 via Wikisource (curl, JDIH/Wikimedia blok requests)  -> halaman
  74 : DOI benar 10.1109/TIME-E.2015.7389747 (tanda hubung)           -> metadata
  9  : PDF Mursita via Garuda download.garuda                         -> pdf
  54/57: MDPI via mdpi-res.com (curl)                                 -> pdf
Semua hasil ditulis ke _hasil.json (inkremental per langkah).
"""
import json
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from unduh_pustaka import DIR_PDF, DIR_WEB, HDR, get_url, pdf_ok
from data_pustaka import REFS

AKAR = DIR_PDF.parent
HASIL_PATH = AKAR / "_hasil.json"
hasil = json.loads(HASIL_PATH.read_text(encoding="utf-8"))
KEY = {r["no"]: r["key"] for r in REFS}


def catat(no, **kw):
    e = hasil.get(str(no), {})
    e.update(kw)
    e["key"] = KEY[no]
    hasil[str(no)] = e
    HASIL_PATH.write_text(json.dumps(hasil, ensure_ascii=False, indent=1, sort_keys=True),
                          encoding="utf-8")
    print(f"{no:02d} [{kw.get('status','?'):8}] {kw.get('sumber', kw.get('catatan',''))[:90]}", flush=True)


def curl(path, url, referer=None):
    cmd = ["curl", "-sL", "--max-time", "120", "-A",
           "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
           "(KHTML, like Gecko) Chrome/124.0 Safari/537.36",
           "-o", str(path)]
    if referer:
        cmd += ["-e", referer]
    cmd.append(url)
    subprocess.run(cmd, capture_output=True, timeout=150)
    return path.exists() and path.stat().st_size > 1500


# ---------- 6: UU 8/2016 via Wikisource ----------
if hasil.get("6", {}).get("status") not in ("halaman",):
    target = DIR_WEB / "06 - RI-2016-UU-8-Penyandang-Disabilitas.html"
    for u in ("https://id.wikisource.org/wiki/Undang-Undang_Republik_Indonesia_Nomor_8_Tahun_2016",
              "https://id.wikisource.org/wiki/Undang-Undang_Republik_Indonesia_Nomor_8_Tahun_2016?action=raw"):
        if curl(target, u):
            catat(6, status="halaman", berkas=str(target), sumber=u,
                  catatan="Teks lengkap UU 8/2016 via Wikisource (JDIH BPK memblokir akses otomatis)")
            break

# ---------- 74: DOI benar (tanda hubung) -> metadata Crossref ----------
if hasil.get("74", {}).get("status") not in ("pdf", "metadata"):
    import requests
    doi74 = "10.1109/TIME-E.2015.7389747"
    try:
        r = requests.get(f"https://api.crossref.org/works/{doi74}", headers=HDR, timeout=30)
        if r.status_code == 200:
            t = AKAR / "metadata" / "74 - Rakun-2015-HMM-SIBI-TIME-E-crossref.json"
            t.write_text(r.text, encoding="utf-8")
            judul = (r.json()["message"].get("title") or [""])[0]
            catat(74, status="metadata", berkas=str(t), sumber=f"https://doi.org/{doi74}",
                  catatan=f"Tidak ada salinan terbuka (IEEE); metadata Crossref disimpan — judul terverifikasi: {judul[:80]}")
        else:
            catat(74, catatan=f"Crossref {r.status_code} untuk DOI dash — coba varian lain")
    except Exception as e:
        catat(74, catatan=f"eksepsi {type(e).__name__}: {e}")

# ---------- 9: PDF Mursita via Garuda / OJS INKLUSI ----------
if hasil.get("9", {}).get("status") not in ("pdf",):
    kandidat = [
        "https://journal.uinjkt.ac.id/index.php/inklusi/article/download/2202/1002",
        "https://journal.uinjkt.ac.id/inklusi/article/download/2202/1002",
        "https://garuda.kemdiktisaintek.go.id/documents/view/1109",
    ]
    # Garuda scraper: cari tautan download sebenarnya
    b = get_url("https://garuda.kemdiktisaintek.go.id/documents?q=RESPON+TUNARUNGU+MURSITA",
                timeout=(15, 60))
    if b:
        import re, html as mh
        from urllib.parse import urljoin
        t = b[0].decode("utf-8", "ignore")
        for u in re.findall(r'href="([^"]+)"', t):
            u2 = urljoin("https://garuda.kemdiktisaintek.go.id/", mh.unescape(u))
            if "/documents/view/" in u2:
                bb = get_url(u2, timeout=(15, 60))
                if bb:
                    tt = bb[0].decode("utf-8", "ignore")
                    for u3 in re.findall(r'href="([^"]+)"', tt):
                        u3 = urljoin(u2, mh.unescape(u3))
                        if "download.garuda" in u3 or "/document/download/" in u3:
                            kandidat.insert(0, u3)
                            break
                break
    for u in kandidat:
        bb = get_url(u, timeout=(15, 90))
        if bb and pdf_ok(bb[0]):
            simpan = DIR_PDF / "09 - Mursita-2015-SIBI-BISINDO-INKLUSI.pdf"
            simpan.write_bytes(bb[0])
            catat(9, status="pdf", berkas=str(simpan), sumber=u,
                  catatan="PDF akses-terbuka via sumber resmi")
            break

# ---------- 54/57: MDPI via mdpi-res.com ----------
MDPI = {
    54: ("sensors", "24", "03414"),
    57: ("sensors", "20", "04025"),
}
for no, (jurnal, vol, art) in MDPI.items():
    if hasil.get(str(no), {}).get("status") == "pdf":
        continue
    target = DIR_PDF / f"{no:02d} - {KEY[no]}.pdf"
    ok = False
    for host in ("https://mdpi-res.com/d_attachment", "https://res.mdpi.com/d_attachment"):
        for suf in ("", "-v2", "-v3"):
            u = f"{host}/{jurnal}/{jurnal}-{vol}-{art}/article_deploy/{jurnal}-{vol}-{art}{suf}.pdf"
            if curl(target, u, referer="https://www.mdpi.com/") and \
               target.read_bytes()[:5].startswith(b"%PDF"):
                catat(no, status="pdf", berkas=str(target), sumber=u,
                      catatan="PDF akses-terbuka MDPI (mdpi-res.com)")
                ok = True
                break
        if ok:
            break

print("selesai perbaikan_akhir")
