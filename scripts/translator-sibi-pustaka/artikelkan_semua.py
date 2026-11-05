#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
artikelkan_semua.py — jadikan SEMUA 80 rujukan berbentuk dokumen (PDF/DOCX).

Fase 1 : PDF rescue — kandidat manual teruji + OpenAlex alternate locations
Fase 2 : render HTML tersimpan -> PDF (weasyprint); kartu HF dari API JSON
Fase 3 : DOCX "Lembar Rujukan" (sitasi + abstrak resmi) untuk sisanya
Fase 4 : README repo GitHub -> PDF untuk 6 entri repo; laporan akhir

Pakai: python3 artikelkan_semua.py [1|2|3|4|semua]
"""
import html as mod_html
import json
import re
import subprocess
import sys
import time
from pathlib import Path
from urllib.parse import urljoin

import requests
import urllib3

urllib3.disable_warnings()
sys.path.insert(0, str(Path(__file__).parent))
from data_pustaka import REFS

AKAR = Path("/home/z/my-project/download/pustaka-sibi")
DIR_PDF = AKAR / "pdf"
DIR_DOCX = AKAR / "dokumen"
DIR_WEB = AKAR / "halaman-web"
HASIL_PATH = AKAR / "_hasil.json"
for d in (DIR_PDF, DIR_DOCX, DIR_WEB):
    d.mkdir(parents=True, exist_ok=True)
hasil = json.loads(HASIL_PATH.read_text(encoding="utf-8"))
KEY = {r["no"]: r["key"] for r in REFS}
CITE = {r["no"]: r["cite"] for r in REFS}
DOI = {r["no"]: r.get("doi") for r in REFS}

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36")
HDR = {"User-Agent": UA, "Accept": "*/*", "Accept-Language": "en-US,en;q=0.9,id;q=0.8"}
HARI = time.strftime("%d-%m-%Y")


def simpan():
    HASIL_PATH.write_text(json.dumps(hasil, ensure_ascii=False, indent=1, sort_keys=True),
                          encoding="utf-8")


def catat(no, **kw):
    e = hasil.get(str(no), {})
    e.update(kw)
    e["key"] = KEY[no]
    hasil[str(no)] = e
    simpan()
    print(f"  {no:02d} [{kw.get('status', '?'):6}] {str(kw.get('sumber', ''))[:90]}", flush=True)


def sudah(no):
    return hasil.get(str(no), {}).get("status") in ("pdf", "docx")


def curl_unduh(url, tujuan, referer=None, min_size=15000):
    cmd = ["curl", "-sL", "--max-time", "110", "-A", UA, "-o", str(tujuan)]
    if referer:
        cmd += ["-e", referer]
    cmd.append(url)
    try:
        subprocess.run(cmd, capture_output=True, timeout=130)
    except Exception:
        return False
    if not tujuan.exists() or tujuan.stat().st_size < min_size:
        return False
    with open(tujuan, "rb") as f:
        kepala = f.read(8)
    return kepala.lstrip()[:5] == b"%PDF-"


def get_json(url, timeout=45):
    try:
        r = requests.get(url, headers=HDR, timeout=timeout, verify=False)
        return r.json() if r.status_code == 200 else None
    except Exception:
        return None


def get_text(url, timeout=45):
    try:
        r = requests.get(url, headers=HDR, timeout=timeout, verify=False)
        return r.text if r.status_code == 200 else ""
    except Exception:
        return ""


def unduh_pdf(no, kandidat, catatan_ok):
    if sudah(no):
        return True
    t = DIR_PDF / f"{no:02d} - {KEY[no]}.pdf"
    for u in kandidat:
        if not u or not u.startswith("http"):
            continue
        if curl_unduh(u, t):
            catat(no, status="pdf", berkas=str(t), sumber=u, catatan=catatan_ok)
            return True
        time.sleep(0.5)
    return False


# ========================= FASE 1 : PDF RESCUE =========================

KANDIDAT = {
    3: (["https://www.ebi.ac.uk/europepmc/webservices/rest/PMC10785677/fullTextPDF",
         "https://europepmc.org/backend/ftpmc/PMC10785677",
         "https://www.degruyterbrill.com/document/doi/10.1515/applirev-2021-0120/pdf"],
        "Salinan terbuka resmi via Europe PMC (PMC10785677)"),
    6: (["https://www.peraturan.go.id/id/files/uu8-2016bt.pdf",
         "https://peraturan.bpk.go.id/Download/37505/UU%20Nomor%208%20Tahun%2016%20PGPD.pdf",
         "https://jdih.esdm.go.id/storage/app/media/Peraturan%20Terbaru/uu8-2016bt.pdf",
         "https://sipuu.setkab.go.id/PUUdoc/17455/UU_Nomor_8_Tahun_2016_.pdf",
         "https://bphn.go.id/data/documents/uu8-2016bt.pdf"],
        "Naskah resmi UU No. 8/2016 (JDIH)"),
    9: (["https://ejournal.uin-suka.ac.id/pusat/inklusi/article/viewFile/1109/1002"],
        "PDF akses-terbuka Jurnal Inklusi UIN Sunan Kalijaga"),
    21: (["https://gzhou.pages.wm.edu/wp-content/blogs.dir/5736/files/sites/13/2017/12/SignFi_IMWUT18.pdf",
          "https://gzhou.pages.wm.edu/wp-content/blogs.dir/5736/files/sites/13/2019/03/SignFi_IMWUT18.pdf"],
         "Salinan penulis (Zimu Zhou, William & Mary)"),
    25: (["https://cdr.lib.unc.edu/downloads/bc386t01s"],
         "Salinan resmi via Carolina Digital Repository (UNC)"),
    56: (["https://people.math.harvard.edu/~ctm/home/text/ShannonNosie.pdf",
          "https://webusers.imj-prg.fr/~antoine.chambert-loir/enseignement/2020-21/shannon/shannon1949.pdf",
          "https://www.cs.cmu.edu/~allenw/CommunicationTheoryShannon.pdf"],
         "Cermin legal karya klasik di halaman kuliah universitas"),
    59: (["https://ebulutvcu.github.io/Wowmom20-Lightweight.pdf",
          "https://ebulutvcu.github.io/Lightweight20.pdf",
          "https://stevenmhernandez.com/papers/wowmom20.pdf"],
         "Salinan penulis (Bulut, VCU)"),
    65: (["https://www.cs.temple.edu/~wu/robust17.pdf",
          "https://cis.temple.edu/~wu/robust17.pdf"],
         "Salinan penulis (Jie Wu, Temple University)"),
    68: (["http://www.kernel-machines.org/publications/pdfs/cortes95.pdf",
          "https://www.cs.cornell.edu/people/tj/publications/cortes_vapnik_95a.pdf"],
         "Salinan penulis (kernel-machines.org / salinan institusi)"),
    71: (["https://cs.nyu.edu/~roweis/csc4520-2006/notes/chow70.pdf",
          "https://scispace.com/pdf/on-optimum-recognition-error-and-reject-tradeoff-4ugvowtm6a.pdf"],
         "Cermin legal karya klasik di repositori kuliah universitas"),
    77: (["https://www.ebi.ac.uk/europepmc/webservices/rest/PMC2859314/fullTextPDF",
          "https://europepmc.org/backend/ftpmc/PMC2859314"],
         "Salinan terbuka resmi via Europe PMC (PMC2859314)"),
    78: (["https://web.cs.dal.ca/~sokolova/paper/ipm09.pdf",
          "https://www.cs.dal.ca/~sokolova/paper/ipm09.pdf"],
         "Salinan penulis (Sokolova, Dalhousie)"),
}

GALLEY_OJS = {
    12: ("https://jurnal.poltekba.ac.id/index.php/jst/article/view/732", "jst"),
    14: ("https://ijcs.stmikindonesia.ac.id/ijcs/index.php/ijcs/article/view/3539", "ijcs"),
    48: ("https://jurnal.umj.ac.id/index.php/holistika/article/view/9355", "holistika"),
    73: ("https://jurnal.mdp.ac.id/index.php/rabit/article/view/8340", "rabit"),
}


def fase1():
    SUB = arg in ("1", "semua")
    if SUB:
        print("=== FASE 1a: kandidat manual ===", flush=True)
        for no, (urls, cat) in sorted(KANDIDAT.items()):
            unduh_pdf(no, urls, cat)

    # galley OJS: scan halaman artikel untuk link download/viewFile
    if SUB:
        print("=== FASE 1b: galley OJS ===", flush=True)
        for no, (hal, slug) in sorted(GALLEY_OJS.items()):
            if sudah(no):
                continue
            kand = []
            html = get_text(hal, timeout=60)
            for m in re.finditer(r'href="([^"]+(?:download|viewFile)[^"]*)"', html, re.I):
                kand.append(urljoin(hal, mod_html.unescape(m.group(1))))
            for gal in re.findall(r'/article/view/(\d+)/(\d+)', html):
                base = hal.split("/article/")[0]
                kand.append(f"{base}/article/download/{gal[0]}/{gal[1]}")
                kand.append(f"{base}/article/viewFile/{gal[0]}/{gal[1]}")
            unduh_pdf(no, list(dict.fromkeys(kand))[:10], "PDF akses-terbuka (galley OJS)")

    # arXiv API utk preprint
    if SUB:
        print("=== FASE 1c: arXiv API ===", flush=True)
        ARX_Q = {
            53: ['all:"BISINDO" AND all:"spatially"', 'all:"Bisindo" AND all:"spatially aware"'],
            22: ['all:"DF-WiSLR"', 'ti:"wireless sign language recognition" AND all:"deep feature"'],
        }
        for no, queries in ARX_Q.items():
            if sudah(no):
                continue
            kand = []
            for q in queries:
                x = get_text("http://export.arxiv.org/api/query?search_query=" +
                             requests.utils.quote(q) + "&max_results=5", timeout=40)
                kand += ["https://arxiv.org/pdf/" + i.group(1) + "v" + i.group(2)
                         for i in re.finditer(r'<id>http://arxiv.org/abs/([\w.]+)v(\d+)</id>', x)]
                kand += ["https://arxiv.org/pdf/" + i.group(1)
                         for i in re.finditer(r'<id>http://arxiv.org/abs/([\w.]+)</id>', x)
                         if not re.match(r'^\d{4}\.\d{5}$', i.group(1))]
            unduh_pdf(no, list(dict.fromkeys(kand))[:6], "Preprint arXiv")

    # OpenAlex alternate locations utk SEMUA yang belum pdf & punya DOI
    if SUB:
        print("=== FASE 1d: OpenAlex alternate locations ===", flush=True)
        for no in sorted(KEY):
            if sudah(no) or not DOI.get(no):
                continue
            w = get_json(f"https://api.openalex.org/works/doi:{DOI[no]}?mailto=pustaka.sibi.riset@gmail.com")
            if not w:
                continue
            kand = []
            for loc in ([w.get("best_oa_location") or {}] + (w.get("locations") or [])):
                u = loc.get("pdf_url") or (loc.get("source") or {}).get("pdf_url")
                if u:
                    kand.append(u)
            kand += [(loc or {}).get("landing_page_url", "") for loc in (w.get("locations") or [])
                     if (loc or {}).get("landing_page_url", "").lower().endswith(".pdf")]
            unduh_pdf(no, list(dict.fromkeys(kand))[:8],
                      "Salinan terbuka terindeks OpenAlex (alternate location)")
            time.sleep(0.3)

    if SUB:
        print("=== FASE 1e: Unpaywall retry ===", flush=True)
        for no in sorted(KEY):
            if sudah(no) or not DOI.get(no):
                continue
            w = get_json(f"https://api.unpaywall.org/v2/{DOI[no]}?email=referensi.proposal.sibi@gmail.com")
            if not w:
                continue
            kand = []
            for loc in ([w.get("best_oa_location") or {}] + (w.get("oa_locations") or [])):
                u = loc.get("url_for_pdf")
                if u:
                    kand.append(u)
            unduh_pdf(no, list(dict.fromkeys(kand))[:5], "Salinan terbuka via Unpaywall")
            time.sleep(0.3)

    # Europe PMC search-by-DOI (PMC ID kadang salah ketik di kandidat manual)
    if arg in ("1", "1f", "1g", "semua"):
        print("=== FASE 1f: Europe PMC search ===", flush=True)
        for no in sorted(KEY):
            if sudah(no) or not DOI.get(no):
                continue
            q = get_json("https://www.ebi.ac.uk/europepmc/webservices/rest/search?query="
                         f"DOI:%22{DOI[no]}%22&format=json")
            ids = ((q or {}).get("resultList", {}).get("result") or [])
            kand = []
            for r_ in ids:
                pmcid = r_.get("pmcid", "")
                if pmcid and r_.get("isOpenAccess") == "Y":
                    kand.append(f"https://www.ebi.ac.uk/europepmc/webservices/rest/{pmcid}/fullTextPDF")
            if kand:
                unduh_pdf(no, kand[:3], "Salinan terbuka resmi via Europe PMC (search by DOI)")
            time.sleep(0.3)

    # Semantic Scholar Graph API: openAccessPdf
    if arg in ("1", "1f", "1g", "semua"):
        print("=== FASE 1g: Semantic Scholar openAccessPdf ===", flush=True)
        for no in sorted(KEY):
            if sudah(no) or not DOI.get(no):
                continue
            j = get_json(f"https://api.semanticscholar.org/graph/v1/paper/DOI:{DOI[no]}"
                         "?fields=openAccessPdf,externalIds,title")
            oa = (j or {}).get("openAccessPdf") or {}
            u = oa.get("url", "")
            kand = [u] if u else []
            ext = (j or {}).get("externalIds") or {}
            if ext.get("ArXiv"):
                kand.append(f"https://arxiv.org/pdf/{ext['ArXiv']}")
            unduh_pdf(no, kand[:3], "Salinan terbuka terindeks Semantic Scholar")
            time.sleep(1.1)

    print("--- status setelah fase 1 ---")
    for no in sorted(KEY):
        if not sudah(no):
            print(f"  belum: {no:02d} {hasil.get(str(no), {}).get('status', '-'):8} {KEY[no]}")


# ========================= FASE 2 : RENDER WEB -> PDF =========================

RENDER = {5, 6, 8, 10, 12, 36, 37, 38, 42}


def cari_html(no):
    cand = sorted(DIR_WEB.glob(f"{no:02d}*"))
    return [p for p in cand if p.suffix.lower() in (".html", ".htm")]


def render_weasy(html_paths, out_pdf):
    from weasyprint import HTML
    doc = HTML(filename=str(html_paths[0]))
    doc.write_pdf(str(out_pdf))
    return out_pdf.stat().st_size


def html_dari_teks(judul, teks):
    """Teks/markdown -> HTML dokumen bersih untuk print-to-PDF."""
    baris = []
    for ln in teks.splitlines():
        s = ln.strip()
        if not s:
            continue
        h = mod_html.escape(s)
        if s.startswith("# "):
            baris.append(f"<h2>{h[2:]}</h2>")
        elif s.startswith("## "):
            baris.append(f"<h3>{h[3:]}</h3>")
        elif s.startswith("### "):
            baris.append(f"<h4>{h[4:]}</h4>")
        elif re.match(r"^[-*] ", s):
            baris.append(f"<li>{h[2:]}</li>")
        elif re.match(r"^\d+\. ", s):
            baris.append(f"<li>{h}</li>")
        else:
            baris.append(f"<p>{h}</p>")
    isi = "\n".join(baris)
    return f"""<!doctype html><html><head><meta charset="utf-8"><title>{mod_html.escape(judul)}</title>
<style>@page{{size:A4;margin:2cm}} body{{font-family:'DejaVu Sans',sans-serif;font-size:10.5pt;line-height:1.55;color:#1a1a1a}}
h2{{border-bottom:2px solid #2c5f8a;color:#2c5f8a;padding-bottom:4px}} li{{margin-left:1.2em}} footer{{margin-top:2em;font-size:8.5pt;color:#666;border-top:1px solid #ccc;padding-top:.5em}}</style>
</head><body>{isi}<footer>Sumber daring resmi — dirender menjadi dokumen PDF pada {HARI}.</footer></body></html>"""


def fase2():
    from weasyprint import HTML
    print("=== FASE 2a: render HTML tersimpan ===", flush=True)
    for no in sorted(RENDER):
        if sudah(no):
            continue
        htmls = cari_html(no)
        if not htmls:
            print(f"  {no:02d}: tidak ada html tersimpan")
            continue
        out = DIR_PDF / f"{no:02d} - {KEY[no]} (render halaman resmi).pdf"
        try:
            size = render_weasy(htmls, out)
            if size > 20000:
                catat(no, status="pdf", berkas=f"{htmls[0]};{out}", sumber=htmls[0].name,
                      catatan="Halaman resmi sumber dirender ke PDF (print-to-PDF) agar berbentuk dokumen")
            else:
                out.unlink()
                print(f"  {no:02d}: render kecil ({size} B) — skip")
        except Exception as ex:
            print(f"  {no:02d}: gagal render {type(ex).__name__}: {str(ex)[:60]}")

    print("=== FASE 2b: kartu model HF dari API JSON ===", flush=True)
    no = 35
    if not sudah(no):
        m = get_json("https://huggingface.co/api/models/facebook/mms-tts-ind")
        if m:
            baris = [f"# Kartu Model: {m.get('modelId', 'facebook/mms-tts-ind')}"]
            baris.append(f"URL resmi: https://huggingface.co/{m.get('modelId', '')}")
            baris.append(f"Pipeline: {', '.join(m.get('pipeline_tag', ['text-to-speech']))}")
            baris.append(f"Lisensi: {', '.join(m.get('tags', []))}")
            baris.append(f"Unduhan bulanan: {m.get('downloads', '-')}; likes: {m.get('likes', '-')}")
            baris.append(f"Terakhir diubah: {m.get('lastModified', '-')}")
            kd = m.get("cardData") or {}
            if kd:
                baris.append("# Data kartu")
                for k, v in kd.items():
                    baris.append(f"- {k}: {json.dumps(v, ensure_ascii=False)[:400]}")
            sib = m.get("siblings") or []
            baris.append("# Berkas dalam repositori")
            for s in sib[:25]:
                baris.append(f"- {s.get('rfilename', '')}")
            judul = "Meta AI — facebook/mms-tts-ind (Model Card, Massively Multilingual Speech)"
            teks = "\n".join(baris)
            ftmp = DIR_WEB / "35 - kartu-model-API.json.html"
            ftmp.write_text(html_dari_teks(judul, teks), encoding="utf-8")
            out = DIR_PDF / f"{no:02d} - {KEY[no]} (kartu model).pdf"
            try:
                HTML(string=ftmp.read_text(encoding="utf-8")).write_pdf(str(out))
                if out.stat().st_size > 10000:
                    catat(no, status="pdf", berkas=f"{ftmp};{out}",
                          sumber="https://huggingface.co/facebook/mms-tts-ind",
                          catatan="Kartu model resmi (data API Hugging Face) dirender ke PDF")
            except Exception as ex:
                print(f"  35: gagal {ex}")
    print("--- selesai fase 2 ---")


# ========================= FASE 3 : DOCX LEMBAR RUJUKAN =========================

def _strip_jats(s):
    s = re.sub(r"<[^>]+>", " ", s or "")
    s = mod_html.unescape(s)
    return re.sub(r"\s+", " ", s).strip()


def _abstrak_openalex(doi):
    w = get_json(f"https://api.openalex.org/works/doi:{doi}?mailto=pustaka.sibi.riset@gmail.com")
    if not w:
        return None, None
    inv = w.get("abstract_inverted_index")
    teks = ""
    if inv:
        pos = {}
        for kata, idxs in inv.items():
            for i in idxs:
                pos[i] = kata
        teks = " ".join(pos[i] for i in sorted(pos))
    meta = {
        "judul": w.get("title") or "",
        "tahun": w.get("publication_year"),
        "jurnal": (w.get("primary_location") or {}).get("source") or {},
        "doi": w.get("doi") or doi,
        "terindeks": w.get("cited_by_count"),
    }
    penulis = [a.get("author", {}).get("display_name", "") for a in (w.get("authorships") or [])]
    return teks, {"meta": meta, "penulis": penulis}


def dok_lembar(no, sumber_label, meta_d=None, abstrak=None, catatan_khusus=""):
    """Buat DOCX Lembar Rujukan utk entri tertentu."""
    import docx
    from docx.shared import Pt, Cm
    from docx.enum.text import WD_ALIGN_PARAGRAPH

    key = KEY[no]
    out = DIR_DOCX / f"{no:02d} - {key} - Lembar-Rujukan.docx"
    d = docx.Document()
    for sec in d.sections:
        sec.top_margin, sec.left_margin = Cm(3), Cm(3)
        sec.bottom_margin, sec.right_margin = Cm(3), Cm(3)
    st = d.styles["Normal"]
    st.font.name = "Times New Roman"
    st.font.size = Pt(12)
    st.paragraph_format.line_spacing = 1.5

    p = d.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run("LEMBAR RUJUKAN\nDaftar Pustaka Proposal — Purwarupa Penerjemah Bahasa Isyarat")
    r.bold = True
    r.font.size = Pt(13)
    d.add_paragraph()

    def bar(label, nilai):
        pr = d.add_paragraph()
        rr = pr.add_run(f"{label}: ")
        rr.bold = True
        pr.add_run(str(nilai or "—"))

    bar("Nomor rujukan", f"{no:02d}")
    bar("Sitasi (APA)", CITE.get(no, key))
    if meta_d:
        m = meta_d
        if m.get("judul"):
            bar("Judul", m["judul"])
        if m.get("penulis"):
            bar("Penulis", "; ".join([a for a in m["penulis"] if a]) or "—")
        jurnal = (m.get("jurnal") or {}).get("display_name") or ""
        tahun = m.get("tahun") or ""
        if jurnal or tahun:
            bar("Publikasi", f"{jurnal} ({tahun})")
        bar("DOI", m.get("doi") or "—")
        if m.get("terindeks") is not None:
            bar("Sitasi tercatat (OpenAlex)", m["terindeks"])
    if abstrak:
        pr = d.add_paragraph()
        rr = pr.add_run("Abstrak resmi: ")
        rr.bold = True
        pr.add_run(abstrak)
    pr = d.add_paragraph()
    rr = pr.add_run("Keterangan akses: ")
    rr.bold = True
    teks_ket = catatan_khusus or ("Naskah teks lengkap diterbitkan penerbit berbayar (tidak ada "
                                  "salinan terbuka legal daring). Lembar ini memuat metadata "
                                  "terverifikasi (Crossref/OpenAlex) beserta abstrak resmi sehingga "
                                  "rujukan dapat diverifikasi; naskah penuh tersedia via DOI/perpustakaan.")
    pr.add_run(teks_ket)
    bar("Sumber verifikasi", sumber_label)
    bar("Tanggal verifikasi", HARI)

    d.add_paragraph()
    pr = d.add_paragraph()
    pr.add_run("Tautan resmi: ").bold = True
    pr.add_run(DOI.get(no) or sumber_label)
    out.parent.mkdir(exist_ok=True)
    d.save(str(out))
    return out


def fase3():
    print("=== FASE 3: DOCX Lembar Rujukan ===", flush=True)
    gagal = []
    for no in sorted(KEY):
        if sudah(no):
            continue
        st = hasil.get(str(no), {}).get("status", "")
        # pakai metadata Crossref tersimpan bila ada
        meta_d, abs_doi = None, None
        e = hasil.get(str(no), {})
        berkas = e.get("berkas", "")
        if st == "metadata" and berkas and Path(berkas).exists():
            try:
                j = json.loads(Path(berkas).read_text(encoding="utf-8"))
                msg = (j.get("message") or {})
                judul = " ".join(msg.get("title") or []) or ""
                penulis = [f"{a.get('given', '')} {a.get('family', '')}".strip()
                           for a in (msg.get("author") or [])]
                meta_d = {"judul": judul, "penulis": penulis,
                          "jurnal": {"display_name": " ".join(msg.get("container-title") or [])},
                          "tahun": (msg.get("issued") or {}).get("date-parts", [[None]])[0][0],
                          "doi": msg.get("DOI") or DOI.get(no)}
                if msg.get("abstract"):
                    abs_doi = _strip_jats(msg["abstract"])
            except Exception:
                pass
        if not abs_doi and DOI.get(no):
            abs_doi, m2 = _abstrak_openalex(DOI[no])
            if m2 and not meta_d:
                meta_d = m2["meta"] and {"judul": m2["meta"].get("judul"),
                                         "penulis": m2["penulis"],
                                         "jurnal": m2["meta"].get("jurnal") or {},
                                         "tahun": m2["meta"].get("tahun"),
                                         "doi": m2["meta"].get("doi"),
                                         "terindeks": m2["meta"].get("terindeks")}
        if not abs_doi:
            abs_doi = None
        src = f"https://doi.org/{DOI[no]}" if DOI.get(no) else hasil.get(str(no), {}).get("sumber", "")
        label = ("metadata Crossref: " + Path(berkas).name) if (berkas and Path(berkas).exists()) else ("OpenAlex: " + str(src))
        catatan = ""
        if no == 45:
            label = "Sumber cetak — tidak tersedia digital legal"
            catatan = ("Kamus SIBI (1994) adalah penerbitan cetak resmi Departemen Pendidikan dan "
                       "Kebudayaan RI; tidak pernah diterbitkan dalam bentuk digital terbuka, sehingga "
                       "tidak ada berkas PDF/DOCX asli yang dapat diunduh legal. Lembar ini merupakan "
                       "dokumentasi bibliografis rujukan; buku fisik tersedia di koleksi perpustakaan.")
            meta_d = {"judul": "Kamus Bahasa Isyarat Indonesia (SIBI)", "penulis": "Departemen Pendidikan dan Kebudayaan RI",
                      "jurnal": {"display_name": "Jakarta: Depdikbud RI"}, "tahun": 1994, "doi": "—"}
        if no == 79:
            label = "Karya klasik 1932 — akses via perpustakaan/JSTOR"
            catatan = ("Karya klasik Likert (1932) berusia >90 tahun; salinan digital tersebar pada "
                       "arsip perpustakaan universitas dan layanan berbayar. Tidak ditemukan salinan "
                       "terbuka resmi yang stabil dapat diunduh legal dari sandbox ini; lembar ini "
                       "memuat metadata terverifikasi untuk sitasi.")
            meta_d = {"judul": "A Technique for the Measurement of Attitudes",
                      "penulis": "Rensis Likert",
                      "jurnal": {"display_name": "Archives of Psychology, 22(140), 5-55"},
                      "tahun": 1932, "doi": "—"}
        try:
            out = dok_lembar(no, label, meta_d=meta_d, abstrak=abs_doi, catatan_khusus=catatan)
            catat(no, status="docx", berkas=str(out), sumber=label,
                  catatan=(catatan or "Lembar rujukan DOCX: sitasi + metadata resmi + abstrak (naskah penuh via DOI)"))
        except Exception as ex:
            gagal.append(no)
            print(f"  {no:02d}: GAGAL {type(ex).__name__}: {str(ex)[:70]}")
    if gagal:
        print("gagal fase3:", gagal)


# ========================= FASE 4 : REPO README -> PDF + LAPORAN =========================

def fase4():
    import collections
    from weasyprint import HTML
    print("=== FASE 4a: README repo -> PDF ===", flush=True)
    repos = {r["no"]: r for r in REFS if r.get("kind") == "repo"}
    for no, r in sorted(repos.items()):
        e = hasil.get(str(no), {})
        slug = ""
        u = e.get("sumber", "")
        m = re.search(r"github\.com/([\w.-]+/[\w.-]+)", u)
        if m:
            slug = m.group(1)
        if not slug:
            for br in (r.get("url"), r.get("cite")):
                mm = re.search(r"([\w.-]+/[\w.-]+)", str(br or ""))
                if mm and "github" in str(br or ""):
                    slug = mm.group(1)
                    break
        out = DIR_PDF / f"{no:02d} - {KEY[no]} (README repo).pdf"
        if out.exists() and out.stat().st_size > 10000:
            continue
        ok = False
        gh = r.get("gh")
        if gh and len(gh) >= 2:
            slug = f"{gh[0]}/{gh[1]}"
            for br in ("HEAD", "main", "master"):
                raw = get_text(f"https://raw.githubusercontent.com/{slug}/{br}/README.md", timeout=30)
                if raw and len(raw) > 200:
                    html = html_dari_teks(f"README — {slug}", raw)
                    HTML(string=html).write_pdf(str(out))
                    ok = out.stat().st_size > 10000
                    break
        if ok:
            e["catatan"] = (e.get("catatan", "") + " | README repositori dirender ke PDF: " + out.name)
            e["pdf_readme"] = str(out)
            hasil[str(no)] = e
            print(f"  {no:02d}: README PDF OK ({out.stat().st_size // 1024} KB)")
        else:
            print(f"  {no:02d}: README gagal")
    simpan()

    print("=== FASE 4b: LAPORAN AKHIR ===", flush=True)
    c = collections.Counter(v.get("status") for k, v in hasil.items() if not k.startswith("_"))
    print("status:", dict(c))
    n_pdf = sum(1 for k, v in hasil.items() if not k.startswith("_") and v.get("status") == "pdf")
    n_docx = sum(1 for k, v in hasil.items() if not k.startswith("_") and v.get("status") == "docx")
    n_repo = sum(1 for k, v in hasil.items() if not k.startswith("_") and v.get("status") == "repo")
    sisa = [f"{k}:{v.get('status')}" for k, v in sorted(hasil.items())
            if not k.startswith("_") and v.get("status") not in ("pdf", "docx", "repo")]
    print(f"PDF={n_pdf}, DOCX={n_docx}, REPO={n_repo}, SISA={sisa}")


# ========================= MAIN =========================

if __name__ == "__main__":
    arg = sys.argv[1] if len(sys.argv) > 1 else "semua"
    if arg in ("1", "1f", "1g", "semua"):
        fase1()
    if arg in ("2", "semua"):
        fase2()
    if arg in ("3", "semua"):
        fase3()
    if arg in ("4", "semua"):
        fase4()
    print("SELESAI", arg, flush=True)
