#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Probe putaran 2 — URL terkurasi benar + resolver galley OJS + verifikasi judul."""
import concurrent.futures as cf
import re
import subprocess
import tempfile
from pathlib import Path

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36")

PDF_URL = {
    3:  ["https://europepmc.org/articles/PMC10785677?pdf=render",
         "https://europepmc.org/backend/ftpmc/PMC10785677",
         "https://www.degruyterbrill.com/document/doi/10.1515/applirev-2021-0120/pdf"],
    6:  ["https://www.peraturan.go.id/id/files/uu8-2016bt.pdf",
         "https://jdih.esdm.go.id/storage/app/media/Peraturan%20Terbaru/uu8-2016bt.pdf"],
    19: ["https://vhil.stanford.edu/sites/g/files/sbiybj29011/files/media/file/bailenson-apa-nonverbal-overload.pdf"],
    20: ["https://gzhou.pages.wm.edu/wp-content/blogs.dir/5736/files/sites/13/2017/12/WiFiSenseSurvey_CSUR19.pdf"],
    21: ["https://gzhou.pages.wm.edu/wp-content/blogs.dir/5736/files/sites/13/2017/12/SignFi_IMWUT18.pdf",
         "https://gzhou.pages.wm.edu/wp-content/blogs.dir/5736/files/sites/13/2019/03/SignFi_IMWUT18.pdf"],
    22: ["https://expert.taylors.edu.my/file/rems/publication/109291_8483_1.pdf",
         "https://web.archive.org/web/2024id_/https://expert.taylors.edu.my/file/rems/publication/109291_8483_1.pdf"],
    26: ["https://europepmc.org/articles/PMC9830631?pdf=render",
         "https://pmc.ncbi.nlm.nih.gov/articles/PMC9830631/pdf/"],
    40: ["https://tns.thss.tsinghua.edu.cn/widar3.0/data/TPAMI_Widar3.0_paper.pdf"],
    55: ["http://web.archive.org/web/2021id_/https://bayes.wustl.edu/etj/articles/nyquist.pdf"],
    65: ["https://cis.temple.edu/~wu/robust17.pdf",
         "https://web.archive.org/web/2023id_/https://www.cs.temple.edu/~wu/robust17.pdf"],
    68: ["http://www.kernel-machines.org/publications/pdfs/cortes95.pdf",
         "https://www.cs.cornell.edu/people/tj/publications/cortes_vapnik_95a.pdf",
         "https://web.archive.org/web/2020id_/http://www.kernel-machines.org/publications/pdfs/cortes95.pdf"],
    69: ["http://www.aboutgis.com/pdfs/mountrakis2011.pdf"],
    71: ["https://web.archive.org/web/2020id_/https://cs.nyu.edu/~roweis/csc4520-2006/notes/chow70.pdf"],
    73: ["https://jurnal.mdp.ac.id/index.php/rabit/article/download/8340/4101",
         "https://jurnal.mdp.ac.id/index.php/rabit/article/download/8340/3439"],
    76: ["https://vipl.ict.ac.cn/research/sign/hylw/202205/W020220524841131372266.pdf"],
    77: ["https://europepmc.org/articles/PMC2859314?pdf=render",
         "https://europepmc.org/backend/ftpmc/PMC2859314"],
    78: ["https://web.archive.org/web/2023id_/https://web.cs.dal.ca/~sokolova/paper/ipm09.pdf",
         "https://web.cs.dal.ca/~sokolova/paper/ipm09.pdf"],
    63: ["https://arxiv.org/pdf/1904.07870"],
    15: ["https://thesai.org/Downloads/Volume12No10/Paper_46-Indonesia_Sign_Language_Recognition_using_Convolutional_Neural_Network.pdf",
         "https://thesai.org/paper/12/46.pdf"],
    52: ["https://thesai.org/Downloads/Volume16No10/Paper_94-BISINDO_Recognition_Using_3D_CNN_and_LSTM.pdf"],
}

# OJS: unduh landing, cari tautan galley, unduh galley
OJS_LANDING = {
    11: ["https://doi.org/10.36722/jaudhi.v7i1.2876"],
    12: ["https://jurnal.poltekba.ac.id/index.php/jst/article/view/732"],
    13: ["https://doi.org/10.33050/tmj.v7i1.1690"],
    16: ["https://doi.org/10.33506/insect.v10i2.4079"],
    17: ["https://doi.org/10.54914/dbesti.v3i1.2081"],
    49: ["https://doi.org/10.55606/concept.v4i3.2178"],
    50: ["https://doi.org/10.31539/intecoms.v7i1.8326"],
}

GALLEY_RE = re.compile(
    r'href="([^"]*?/article/(?:viewFile|download)/[^"]+|[^"]*?/galley/\d+/download/[^"]+)"', re.I)


def curl(url, timeout=50, referer=None):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".bin") as f:
        tmp = f.name
    cmd = ["curl", "-sL", "--max-time", str(timeout), "-A", UA,
           "-o", tmp, "-w", "%{http_code}|%{url_effective}"]
    if referer:
        cmd += ["-e", referer]
    cmd.append(url)
    try:
        r = subprocess.run(cmd, capture_output=True, timeout=timeout + 15)
        code = r.stdout.decode(errors="ignore").split("|")[0]
        data = Path(tmp).read_bytes()
        return code, data, r.stdout.decode(errors="ignore")
    except Exception:
        return "0", b"", ""
    finally:
        Path(tmp).unlink(missing_ok=True)


def cek_pdf(url, referer=None):
    code, data, info = curl(url, referer=referer)
    ok = data[:5] == b"%PDF-" and len(data) > 15000
    return ok, len(data), f"HTTP {code}", data


def cek_ojs(landing):
    code, html, info = curl(landing)
    if code != "200" or b"<html" not in html[:3000].lower():
        return False, 0, f"landing HTTP {code} ({len(html)}B)"
    m = GALLEY_RE.findall(html.decode(errors="ignore"))
    if not m:
        return False, len(html), f"landing ok, galley tidak ditemukan; final={info.split('|')[-1][:70]}"
    # coba hingga 3 kandidat galley
    for g in m[:3]:
        ok, size, note, _ = cek_pdf(g, referer=landing)
        if ok:
            return True, size, f"galley {g[:80]}"
    return False, 0, f"galley ada ({len(m)}) tapi PDF gagal: {m[0][:70]}"


hasil = {}
with cf.ThreadPoolExecutor(max_workers=7) as ex:
    futs = {}
    for no, urls in PDF_URL.items():
        for u in urls:
            futs[ex.submit(cek_pdf, u)] = (no, u, "pdf")
    for no, urls in OJS_LANDING.items():
        futs[ex.submit(cek_ojs, urls[0])] = (no, urls[0], "ojs")
    for fut in cf.as_completed(futs):
        no, u, jenis = futs[fut]
        ok, size, note = fut.result()[:3]
        prev = hasil.get(no)
        if ok or prev is None:
            hasil[no] = (ok, size, note, u)
        elif not prev[0]:
            hasil[no] = prev  # pertahankan hasil pertama gagal

print(f"{'no':>3} {'status':<8} {'ukuran':>9}  catatan")
for no in sorted(hasil):
    ok, size, note, u = hasil[no]
    print(f"{no:>3} {'PDF-OK' if ok else 'GAGAL':<8} {size:>9}  {note}")

# verifikasi judul #63 (arXiv 1904.07870)
code, data, _ = curl("https://arxiv.org/abs/1904.07870")
m = re.search(r'<title>(.*?)</title>', data.decode(errors="ignore"), re.S)
print("\n#63 verifikasi judul arXiv 1904.07870:", (m.group(1).strip()[:110] if m else "gagal ambil"))
