#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Probe keterjangkauan rujukan ambigu — validasi URL kandidat PDF (%PDF, >15KB)."""
import concurrent.futures as cf
import subprocess
import tempfile
from pathlib import Path

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36")

# no -> daftar URL kandidat (berurutan, cukup satu yang berhasil)
KANDIDAT = {
    7:  ["https://www.frontiersin.org/journals/education/articles/10.3389/feduc.2023.1121597/pdf"],
    11: ["https://jurnal.uhamka.ac.id/index.php/audhi/article/view/2876",
         "https://journal.uhamka.ac.id/index.php/audhi/article/view/2876",
         "https://doi.org/10.36722/jaudhi.v7i1.2876"],
    12: ["https://jurnal.poltekba.ac.id/index.php/jst/article/view/732",
         "https://jurnal.poltekba.ac.id/index.php/jst/article/download/732/pdf"],
    13: ["https://ejournal.umbmi.ac.id/index.php/technomedia/article/view/1690",
         "https://ejournal.nusacc.org/index.php/technomedia/article/view/1690",
         "https://doi.org/10.33050/tmj.v7i1.1690"],
    16: ["https://insect.sbvuzi.ac.id/index.php/insect/article/view/4079",
         "https://doi.org/10.33506/insect.v10i2.4079"],
    17: ["https://jurnal.dbesti.org/index.php/dbesti/article/view/2081",
         "https://ejournal.papistand.or.id/index.php/dbesti/article/view/2081",
         "https://doi.org/10.54914/dbesti.v3i1.2081"],
    19: ["https://tmb.apaopen.org/pub/nonverbal-overload/download/pdf"],
    21: ["https://gzhou.pages.wm.edu/wp-content/blogs.dir/5736/files/sites/13/2017/12/SignFi_IMWUT18.pdf",
         "https://gzhou.pages.wm.edu/wp-content/blogs.dir/5736/files/sites/13/2019/03/SignFi_IMWUT18.pdf"],
    22: ["https://expert.taylors.edu.my/file/rems/publication/109291_8483_1.pdf"],
    25: ["https://www.eecs.umich.edu/~mns/keystroke.pdf",
         "http://web.eecs.umich.edu/~mns/keystroke.pdf"],
    40: ["https://tns.thss.tsinghua.edu.cn/publications/2021/widar30.pdf",
         "https://tns.thss.tsinghua.edu.cn/~zhangy/publication/pdf/widar30.pdf"],
    49: ["https://ejournal.papandayan.ac.id/index.php/concept/article/view/2178",
         "https://doi.org/10.55606/concept.v4i3.2178"],
    50: ["https://jurnal.poltekpos.ac.id/index.php/intecoms/article/view/8326",
         "https://doi.org/10.31539/intecoms.v7i1.8326"],
    52: ["https://thesai.org/Downloads/Volume16No10/Paper_94-BISINDO_Recognition_Using_3D_CNN_and_LSTM.pdf",
         "https://thesai.org/Downloads/Volume16No9/Paper_94-BISINDO_Recognition_Using_3D_CNN_and_LSTM.pdf"],
    59: ["https://ebulutvcu.github.io/Wowmom20-Lightweight.pdf",
         "https://ebulutvcu.github.io/Lightweight20.pdf",
         "https://stevenmhernandez.com/papers/wowmom20.pdf"],
    63: ["https://openaccess.thecvf.com/content_ICCV_2019/papers/Wang_Person-in-WiFi_Fine-Grained_Person_Pose_Estimation_With_WiFi_ICCV_2019_paper.pdf",
         "https://arxiv.org/pdf/1904.07870"],
    68: ["http://www.kernel-machines.org/publications/pdfs/cortes95.pdf",
         "https://www.cs.cornell.edu/people/tj/publications/cortes_vapnik_95a.pdf",
         "https://link.springer.com/content/pdf/10.1007/BF00994018.pdf"],
    71: ["https://cs.nyu.edu/~roweis/csc4520-2006/notes/chow70.pdf",
         "https://scispace.com/pdf/on-optimum-recognition-error-and-reject-tradeoff-4ugvowtm6a.pdf"],
    73: ["https://jurnal.mdp.ac.id/index.php/rabit/article/view/8340",
         "https://jurnal.univrab.ac.id/index.php/rabit/article/view/8340",
         "https://jurnal.mdp.ac.id/index.php/rabit/article/download/8340/3439"],
    9:  ["https://ejournal.uin-suka.ac.id/pusat/inklusi/article/viewFile/1109/1002"],
    14: ["https://www.ijcs.net/archive/vol12/issue6/3539.pdf",
         "https://ijcs.stmikindonesia.ac.id/ijcs/index.php/ijcs/article/download/3539/298"],
    15: ["https://thesai.org/Downloads/Volume12No10/Paper_46-Indonesia_Sign_Language_Recognition_using_Convolutional_Neural_Network.pdf"],
    48: ["https://jurnal.umj.ac.id/index.php/holistika/article/download/9355/5468",
         "https://jurnal.umj.ac.id/index.php/holistika/article/view/9355"],
    26: ["https://ieeexplore.ieee.org/ielx7/6287639/8274985/09724225.pdf",
         "https://pmc.ncbi.nlm.nih.gov/articles/PMC9830631/pdf/"],
    3:  ["https://www.ebi.ac.uk/europepmc/webservices/rest/PMC10785677/fullTextPDF"],
    77: ["https://www.ebi.ac.uk/europepmc/webservices/rest/PMC2859314/fullTextPDF"],
    55: ["https://bayes.wustl.edu/etj/articles/nyquist.pdf"],
    56: ["https://webusers.imj-prg.fr/~antoine.chambert-loir/enseignement/2020-21/shannon/shannon1949.pdf",
         "https://people.math.harvard.edu/~ctm/home/text/ShannonNosie.pdf"],
    65: ["https://cis.temple.edu/~wu/robust17.pdf",
         "https://www.cs.temple.edu/~wu/robust17.pdf"],
    69: ["http://www.aboutgis.com/pdfs/mountrakis2011.pdf",
         "https://www.aboutgis.com/pdfs/mountrakis2011.pdf"],
    78: ["https://web.cs.dal.ca/~sokolova/paper/ipm09.pdf"],
    79: ["https://archive.org/download/likert-1932/Likert_1932.pdf"],
    6:  ["https://jdih.esdm.go.id/storage/app/media/Peraturan%20Terbaru/uu8-2016bt.pdf",
         "https://peraturan.bpk.go.id/Download/37505/UU%20Nomor%208%20Tahun%2016%20PGPD.pdf"],
}


def cek(url):
    """Unduh 200KB pertama; kembalikan (ok_pdf, ukuran, catatan)."""
    with tempfile.NamedTemporaryFile(delete=False, suffix=".bin") as f:
        tmp = f.name
    try:
        r = subprocess.run(
            ["curl", "-sL", "--max-time", "45", "-A", UA, "--range", "0-204799",
             "-o", tmp, "-w", "%{http_code}|%{size_download}|%{url_effective}", url],
            capture_output=True, timeout=60)
        info = r.stdout.decode(errors="ignore")
        code = info.split("|")[0] if info else "0"
        size = Path(tmp).stat().st_size
        head = open(tmp, "rb").read(5)
        ok = head == b"%PDF-" and size > 15000
        return ok, size, f"HTTP {code}, head={head!r}"
    except Exception as ex:
        return False, 0, f"ERR {type(ex).__name__}"
    finally:
        Path(tmp).unlink(missing_ok=True)


hasil = {}
futures = {}
with cf.ThreadPoolExecutor(max_workers=8) as ex:
    for no, urls in KANDIDAT.items():
        for u in urls:
            fut = ex.submit(cek, u)
            futures[fut] = (no, u)

for fut in cf.as_completed(futures):
    no, u = futures[fut]
    ok, size, note = fut.result()
    prev = hasil.get(no)
    if ok or prev is None:
        hasil[no] = (ok, size, u, note)

print(f"{'no':>3} {'status':<8} {'ukuran':>9}  url")
for no in sorted(hasil):
    ok, size, u, note = hasil[no]
    print(f"{no:>3} {'PDF-OK' if ok else 'GAGAL':<8} {size:>9}  {u[:90]}")
    print(f"    > {note}")
