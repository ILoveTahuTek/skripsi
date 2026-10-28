#!/usr/bin/env python3
"""QA ekspor akhir: posisi & lebar cetak tiap gambar di PDF + spot-check teks."""
import fitz, re, sys

PDF = sys.argv[1] if len(sys.argv) > 1 else '/home/z/my-project/download/translator-sibi-docx/Pratinjau-Proposal-Penerjemah-Dua-Arah-SIBI.pdf'
doc = fitz.open(PDF)
print(f'halaman: {len(doc)}')

found = {}
for pno in range(len(doc)):
    page = doc[pno]
    text = page.get_text()
    for m in re.finditer(r'Gambar 3\.(\d) [A-Z]', text):
        n = f'3.{m.group(1)}'
        cap_y = m.start(1) and None
        # posisi y caption via search_for
        hits = page.search_for(f'Gambar 3.{m.group(1)} ')
        if not hits: continue
        cy = min(h.y0 for h in hits)
        imgs = page.get_images(full=True)
        cands = []
        for x in imgs:
            for r in page.get_image_rects(x[0]):
                if r.y1 <= cy + 5:  # gambar di atas caption
                    cands.append(r)
        if cands:
            r = max(cands, key=lambda q: q.width)
            w_cm = r.width / 72 * 2.54
            h_cm = r.height / 72 * 2.54
            found.setdefault(n, (pno + 1, w_cm, h_cm))
for n in sorted(found):
    p, w, h = found[n]
    status = 'OK' if 13.5 <= w <= 14.05 and h <= 20.7 else 'PERIKSA'
    print(f'Gambar {n}: hal {p:2}, lebar cetak {w:.1f} cm x {h:.1f} cm  {status}')

# spot-check teks
full = re.sub(r'\s+', ' ', '\n'.join(doc[i].get_text() for i in range(len(doc))))
cek = [
    ('caption 3.1 jalur lolos', 'jalur gagal dirinci pada Gambar 3.2'),
    ('caption 3.2 remediasi', 'Jalur gagal dan remediasi gerbang keputusan'),
    ('caption 3.3 distilasi I', 'tahap data: perekaman tersinkron'),
    ('caption 3.4 distilasi II', 'tahap pelatihan: dataset murid'),
    ('caption 3.5 arsitektur', 'Rantai kiri = arah 1'),
    ('caption 3.8 evaluasi', 'Alur evaluasi: pembagian data'),
    ('WIFI_PS_NONE di prosa', 'WIFI_PS_NONE'),
    ('rujukan 3.2 di prosa 3.2', 'dirinci pada Gambar 3.2'),
    ('rujukan 3.3/3.4 di 3.2.3', 'ditunjukkan pada Gambar 3.3'),
    ('rujukan 3.8 di 3.8', 'ditunjukkan pada Gambar 3.8'),
    ('arah1/2/guru rujukan 3.5', 'ditunjukkan pada Gambar 3.5'),
    ('topologi rujukan 3.6', 'ditunjukkan pada Gambar 3.6'),
    ('inferensi rujukan 3.7', 'ditunjukkan pada Gambar 3.7'),
    ('PERLU DATA masih ada', 'PERLU DATA'),
]
gagal = 0
for nama, frasa in cek:
    ok = frasa in full
    gagal += 0 if ok else 1
    print(f'  [{"OK" if ok else "GAGAL"}] {nama}')
# caption lama yang harus hilang
for frasa in ['Rantai lengkap dari *dataset* hingga pengemasan', 'Gambar 3.6 Alur dataset, pelatihan guru–murid']:
    ok = frasa not in full
    gagal += 0 if ok else 1
    print(f'  [{"OK" if ok else "GAGAL"}] teks lama hilang: {frasa[:50]}')
sys.exit(1 if gagal else 0)
