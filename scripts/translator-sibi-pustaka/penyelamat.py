#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
penyelamat.py — Putaran 3: penyelamatan rujukan yang masih gagal.
Strategi: kandidat URL spesifik (hasil riset), backend Europe PMC, Wayback Machine
(untuk PDF ACM/IEEEXplore yang diblokir bot), scrape repositori institusi (UvA, MIT,
UNIST), wayback-scrape OJS yang memblokir, dan arsip.org untuk buku klasik.
Memperbarui _hasil.json di tempat.
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
from unduh_pustaka import DIR_PDF, DIR_WEB, HDR, EMAIL, get_url, pdf_ok, html_ok, pdf_kepala
from data_pustaka import REFS

KEY = {r["no"]: r["key"] for r in REFS}
DOI = {r["no"]: r.get("doi") for r in REFS}
AKAR = DIR_PDF.parent
HASIL_PATH = AKAR / "_hasil.json"

# ---------- helper ----------

def muat_hasil():
    return json.loads(HASIL_PATH.read_text(encoding="utf-8")) if HASIL_PATH.exists() else {}


def catat(hasil, no, **kw):
    e = hasil.get(str(no), {})
    e.update(kw)
    e["key"] = KEY[no]
    hasil[str(no)] = e
    print(f"{no:02d} [{kw.get('status', '?'):7}] {kw.get('cara', kw.get('catatan', ''))[:70]}")


def wayback(u):
    try:
        r = requests.get("http://archive.org/wayback/available",
                         params={"url": u}, headers=HDR, timeout=20)
        j = r.json().get("archived_snapshots", {}).get("closest", {})
        if j.get("available") and j.get("timestamp"):
            return f"https://web.archive.org/web/{j['timestamp']}id_/{u}"
    except Exception:
        pass
    return None


def simpan_pdf(hasil, no, data, sumber, cara):
    tujuan = DIR_PDF / f"{no:02d} - {KEY[no]}.pdf"
    tujuan.write_bytes(data)
    catat(hasil, no, status="pdf", berkas=str(tujuan), sumber=sumber, cara=cara)
    return True


def coba(hasil, no, urls, cara="langsung", wb=True):
    """Coba daftar URL; tiap URL: langsung → wayback. Berhasil = simpan PDF."""
    for u in urls:
        if not u:
            continue
        b = get_url(u, timeout=(15, 180))
        if b and pdf_ok(b[0]):
            return simpan_pdf(hasil, no, b[0], u, cara)
        if wb:
            w = wayback(u)
            if w:
                b = get_url(w, timeout=(15, 180))
                if b and pdf_ok(b[0]):
                    return simpan_pdf(hasil, no, b[0], w, cara + "+wayback")
    return False


def kandidat_landing(landing):
    try:
        r = requests.get(landing, headers=HDR, timeout=(15, 90), allow_redirects=True)
    except Exception:
        return []
    if r.status_code != 200:
        return []
    t = r.text or ""
    kand = []
    m = re.search(r'citation_pdf_url[^>]*content=["\']([^"\']+)["\']', t, re.I)
    if m:
        kand.append(mod_html.unescape(m.group(1)))
    for u in re.findall(r'href=["\']([^"\']+)["\']', t, re.I):
        u2 = mod_html.unescape(u)
        if re.search(r'(\.pdf|bitstream|viewFile|/article/download/|/download/)', u2, re.I):
            if u2.startswith("//"):
                u2 = "https:" + u2
            elif not u2.startswith("http"):
                u2 = urljoin(r.url, u2)
            kand.append(u2)
    out = []
    for u in kand:
        if u not in out:
            out.append(u)
    return out[:10]


def scrape_wayback(hasil, no, landing, max_kand=6):
    """Wayback → halaman OJS → ekstrak tautan PDF/galley → unduh (asli atau wayback)."""
    w = wayback(landing)
    if not w:
        return False
    b = get_url(w, timeout=(15, 120))
    if not b:
        return False
    t = b[0].decode("utf-8", "ignore")
    asal = re.match(r"https?://[^/]+", landing).group(0)
    kand = []
    for u in re.findall(r'href=["\']([^"\']+)["\']', t, re.I):
        u2 = mod_html.unescape(u)
        if re.search(r'(\.pdf|viewFile|/article/(view|download)/\d+(/\d+)?)', u2, re.I):
            if u2.startswith("//"):
                u2 = "https:" + u2
            elif u2.startswith("/"):
                u2 = asal + u2
            elif "web.archive.org" in u2:
                m = re.search(r"/web/[^/]+/(https?://.+)", u2)
                if m:
                    u2 = m.group(1)
            # galley view → download
            u3 = u2.replace("/article/view/", "/article/download/")
            for v in (u3, u2):
                if v not in kand:
                    kand.append(v)
    for u in kand[:max_kand]:
        if coba(hasil, no, [u], "wayback-scrape", wb=False):
            return True
        if coba(hasil, no, [u], "wayback-scrape", wb=True):
            return True
    return False


def upw_lokasi(doi):
    try:
        r = requests.get(f"https://api.unpaywall.org/v2/{doi}",
                         params={"email": EMAIL}, headers=HDR, timeout=25)
        j = r.json()
        pdfs = [l["url_for_pdf"] for l in (j.get("oa_locations") or []) if l.get("url_for_pdf")]
        lands = [l["url"] for l in (j.get("oa_locations") or [])
                 if l.get("url") and not l.get("url_for_pdf")]
        return pdfs, lands
    except Exception:
        return [], []


def sudah_pdf(hasil, no):
    e = hasil.get(str(no), {})
    return e.get("status") == "pdf" and Path(e.get("berkas", "/x")).exists()

# ---------- playbook ----------

LANGSUNG = {
    3:  ["https://europepmc.org/backend/ftpmc/PMC10785677"],
    6:  ["https://peraturan.bpk.go.id/Download/26352/UU%20Nomor%208%20Tahun%202016.pdf"],
    19: ["https://tmb.apaopen.org/pub/nonverbal-overload/download/pdf"],
    26: ["https://europepmc.org/backend/ftpmc/PMC9830631"],
    40: ["https://tns.thss.tsinghua.edu.cn/widar3.0/data/TPAMI_Widar3.0_paper.pdf"],
    48: ["https://pdfs.semanticscholar.org/d806/3cf27f9bb3682b674b5697451a3b15a2c3d8.pdf"],
    54: ["https://europepmc.org/backend/ftpmc/PMC11175107",
         "https://res.mdpi.com/d_attachment/sensors/sensors-24-03414/article_deploy/sensors-24-03414.pdf",
         "https://mdpi-res.com/d_attachment/sensors/sensors-24-03414/article_deploy/sensors-24-03414.pdf"],
    55: ["https://bayes.wustl.edu/Manual/CertainTopicsInTelegraphTransmissionTheory.pdf"],
    56: ["https://webusers.imj-prg.fr/~antoine.chambert-loir/enseignement/2020-21/shannon/shannon1949.pdf"],
    57: ["https://europepmc.org/backend/ftpmc/PMC7412096",
         "https://res.mdpi.com/d_attachment/sensors/sensors-20-04025/article_deploy/sensors-20-04025.pdf",
         "https://mdpi-res.com/d_attachment/sensors/sensors-20-04025/article_deploy/sensors-20-04025.pdf"],
    59: ["https://ieeexplore.ieee.org/iel7/9210704/9217631/09217780.pdf"],
    68: ["https://link.springer.com/content/pdf/10.1007/BF00994018.pdf"],
    71: ["https://scispace.com/pdf/on-optimum-recognition-error-and-reject-tradeoff-4ugvowtm6a.pdf"],
    77: ["https://europepmc.org/backend/ftpmc/PMC2859314"],
}

ACM_WAYBACK = {
    20: "https://dl.acm.org/doi/pdf/10.1145/3310194",
    21: "https://dl.acm.org/doi/pdf/10.1145/3191755",
    24: "https://dl.acm.org/doi/pdf/10.1145/3377553",
    25: "https://dl.acm.org/doi/pdf/10.1145/2789168.2790109",
    39: "https://dl.acm.org/doi/pdf/10.1145/3570325",
    44: "https://dl.acm.org/doi/pdf/10.1145/3663547.3759693",
    65: "https://dl.acm.org/doi/pdf/10.1145/3097620.3097624",
    76: "https://dl.acm.org/doi/pdf/10.1145/641007.641035",
}

OJS_WAYBACK = {
    9:  "https://ejournal.uin-suka.ac.id/pusat/inklusi/article/view/2202",
    48: "https://jurnal.umj.ac.id/index.php/holistika/article/view/9355",
    73: "https://jurnal.univrab.ac.id/index.php/rabit/article/view/8340",
}


def main():
    hasil = muat_hasil()

    # 1) kandidat langsung
    for no, urls in LANGSUNG.items():
        if sudah_pdf(hasil, no):
            continue
        if not coba(hasil, no, urls, "langsung"):
            catat(hasil, no, status="masih-gagal", cara=f"langsung x{len(urls)}")

    # 2) ACM via wayback
    for no, u in ACM_WAYBACK.items():
        if sudah_pdf(hasil, no):
            continue
        w = wayback(u)
        if w:
            if not coba(hasil, no, [u], "acm", wb=True):
                catat(hasil, no, status="masih-gagal", cara="acm-wayback")
        else:
            catat(hasil, no, status="masih-gagal", cara="acm-wayback (tanpa snapshot)")

    # 3) OJS terblokir via wayback-scrape
    for no, landing in OJS_WAYBACK.items():
        if sudah_pdf(hasil, no):
            continue
        if not scrape_wayback(hasil, no, landing):
            catat(hasil, no, status="masih-gagal", cara="ojs-wayback")

    # 4) repositori institusi (green OA) — scrape landing
    for no, doi in [(4, DOI[4]), (69, DOI[69])]:
        if sudah_pdf(hasil, no):
            continue
        _, lands = upw_lokasi(doi)
        kand = []
        for l in lands:
            kand += kandidat_landing(l)
        if kand:
            if not coba(hasil, no, kand[:8], "repo-institusi"):
                catat(hasil, no, status="masih-gagal", cara="repo-institusi")
        else:
            catat(hasil, no, status="masih-gagal", cara="repo-institusi (landing kosong)")

    # 5) MIT DSpace utk Chow 1970 (jika SciSpace gagal)
    if not sudah_pdf(hasil, 71):
        kand = kandidat_landing(
            "https://dspace.mit.edu/entities/publication/3d09633b-df6a-4051-8915-66bb2ae5b236")
        if kand:
            coba(hasil, 71, kand[:8], "mit-dspace")
        if not sudah_pdf(hasil, 71):
            kand2 = kandidat_landing("http://hdl.handle.net/1721.1/6177")
            if kand2:
                coba(hasil, 71, kand2[:8], "mit-handle")

    # 6) 12 JST poltekba: scrape + transform view→download
    if not sudah_pdf(hasil, 12):
        kand = kandidat_landing("https://jurnal.poltekba.ac.id/index.php/jst/article/view/732")
        kand = [u.replace("/article/view/", "/article/download/") for u in kand] + kand
        coba(hasil, 12, kand[:8], "ojs-transform")

    # 7) arsip.org: Likert 1932
    if not sudah_pdf(hasil, 79):
        try:
            r = requests.get("https://archive.org/metadata/likert-1932", headers=HDR, timeout=30)
            files = (r.json() or {}).get("files") or []
            pdfs = [f["name"] for f in files if (f.get("name") or "").lower().endswith(".pdf")]
            if pdfs:
                coba(hasil, 79, [f"https://archive.org/download/likert-1932/{mod_html.quote(pdfs[0])}"],
                     "archive.org")
            else:
                catat(hasil, 79, status="masih-gagal", cara="archive.org (tanpa PDF)")
        except Exception:
            catat(hasil, 79, status="masih-gagal", cara="archive.org (galat)")

    # 8) arsip.org: Kamus SIBI 1994 (pencarian)
    if not sudah_pdf(hasil, 45):
        try:
            r = requests.get("https://archive.org/advancedsearch.php",
                             params={"q": 'title:("Kamus Sistem Isyarat Bahasa Indonesia")',
                                     "fl[]": "identifier,title", "rows": 5, "output": "json"},
                             headers=HDR, timeout=30)
            docs = (r.json().get("response", {}).get("docs")) or []
            if docs:
                ident = docs[0]["identifier"]
                r2 = requests.get(f"https://archive.org/metadata/{ident}", headers=HDR, timeout=30)
                files = (r2.json() or {}).get("files") or []
                pdfs = [f["name"] for f in files if (f.get("name") or "").lower().endswith(".pdf")]
                if pdfs:
                    coba(hasil, 45, [f"https://archive.org/download/{ident}/{mod_html.quote(pdfs[0])}"],
                         "archive.org")
                else:
                    catat(hasil, 45, status="tidak-tersedia", cara="archive.org: item tanpa PDF")
            else:
                catat(hasil, 45, status="tidak-tersedia",
                      cara="buku cetak 1994 — tidak terdigitalisasi")
        except Exception:
            catat(hasil, 45, status="tidak-tersedia", cara="pencarian arsip galat")

    # 9) BRIN 8: wayback halaman
    if hasil.get("8", {}).get("status") != "halaman":
        for u in ("https://brin.go.id/news/130095", "https://brin.go.id/news/130095/"):
            w = wayback(u)
            if w:
                b = get_url(w, timeout=(15, 120))
                if b and (html_ok(b[0]) or pdf_ok(b[0])):
                    p = DIR_WEB / "08 - BRIN-2026-Ekosistem-Bahasa-Isyarat" + (".pdf" if pdf_ok(b[0]) else ".html")
                    p.write_bytes(b[0])
                    catat(hasil, 8, status="halaman", berkas=str(p), sumber=w, cara="wayback")
                    break

    HASIL_PATH.write_text(json.dumps(hasil, ensure_ascii=False, indent=1, sort_keys=True),
                          encoding="utf-8")
    n = {}
    for v in hasil.values():
        n[v.get("status", "?")] = n.get(v.get("status", "?"), 0) + 1
    print("\n=== RINGKASAN PENYELAMAT ===")
    for k in sorted(n):
        print(f"{k:16}: {n[k]}")
    print(f"total            : {len(hasil)}/80")


if __name__ == "__main__":
    main()
