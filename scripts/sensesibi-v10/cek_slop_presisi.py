#!/usr/bin/env python3
"""Pemeriksa presisi slop utk Proposal SenseSIBI v10 (humanizer-id, Mode Akademik Ketat).
Hanya melaporkan kecocokan riil dalam jendela kalimat, bukan regex baris penuh."""
import re, sys

F = "/home/z/my-project/download/sensesibi-v10/Proposal-SenseSIBI-v10.md"
teks = open(F, encoding="utf-8").read()
baris = teks.split("\n")

def cari(nama, pola, jendela=90, flags=0):
    print(f"\n### {nama}")
    n = 0
    for i, b in enumerate(baris, 1):
        if b.startswith("|") or b.startswith("["):  # skip tabel DP & lampiran diff
            continue
        for m in re.finditer(pola, b, flags):
            s = max(0, m.start() - 40)
            print(f"  L{i}: ...{b[s:m.end()+50]}...")
            n += 1
    if n == 0:
        print("  (bersih)")

# 1. Koma terlarang sebelum konjungsi intrakalimat (sehingga/karena/agar) di BELAKANG induk
cari("Koma sebelum 'sehingga'", r",\s+sehingga")
cari("Koma sebelum 'karena' (anak kalimat di belakang)", r"\w,\s+karena\s")
# 2. Korelatif: tidak ... melainkan (harus 'tetapi'); bukan ... tetapi/namun (harus 'melainkan')
cari("'tidak ... melainkan'", r"tidak[^.;]{5,140},\s*melainkan")
cari("'bukan ... tetapi'", r"bukan[^.;]{5,120},\s*tetapi")
cari("'bukan ... namun'", r"bukan[^.;]{5,120},\s*namun")
# 3. antara X dengan Y (riil, jendela sempit)
cari("'antara X dengan Y'", r"antara\s+\S+[^,.;]{0,40}\s+dengan")
cari("'antara ... hingga/sampai'", r"antara\s+[^,.;]{1,40}\s+(hingga|sampai)")
# 4. meskipun/walaupun ... tetapi/namun (dalam satu klausa)
cari("'meskipun ... tetapi/namun'", r"[Mm]eskipun[^.]{5,200}\b(tetapi|namun)\b")
# 5. Verba ringan
cari("Verba ringan: melakukan <nomina>", r"melakukan (validasi|segmentasi|pengukuran|analisis|pengujian|implementasi|optimalisasi|pengolahan|penyelidikan|pemeriksaan|perancangan|pembangunan)")
cari("Verba ringan: memberikan <nomina>", r"memberikan (pengaruh|bantuan|kontribusi|dukungan|masukan)")
cari("Verba ringan: mengalami <nomina>", r"mengalami (peningkatan|penurunan|perubahan|perbaikan)")
cari("Verba ringan: melaksanakan <nomina>", r"melaksanakan (pengujian|pelaksanaan|penelitian|kegiatan)")
# 6. Pembuka paragraf klise/konjungsi mekanis
cari("Pembuka paragraf konjungsi mekanis", r"^(Selain itu|Lebih lanjut|Oleh karena itu|Di sisi lain|Dengan demikian|Selanjutnya|Sementara itu|Di samping itu|Adapun|Pertanyaannya|Gagasannya|Lebih jauh lagi|Tak hanya itu)\b")
cari("Pembuka klise era digital", r"(era digital|di dunia yang serba|tak terbantahkan|sebagai kesimpulan|secara keseluruhan)")
# 7. Kalke klise
cari("Kalke klise (menyelami/merajut/lanskap/hiruk)", r"\b(menyelami|merajut|lanskap|hiruk pikuk|peta jalan|menyelami lebih dalam)\b")
cari("Antisipatif 'bukan berarti'", r"bukan berarti")
cari("Utopis penutup", r"(membawa dampak|mengubah wajah|revolusi|masa depan yang lebih baik|hari esok)")
# 8. 'adalah merupakan' & 'merupakan salah satu'
cari("'adalah merupakan'", r"adalah merupakan")
cari("'merupakan salah satu'", r"merupakan salah satu")
# 9. 'terdiri dari' (baku: terdiri atas)
cari("'terdiri dari'", r"terdiri dari")
# 10. 'agar supaya', 'demi untuk', 'dimana' penghubung
cari("'agar supaya/demi untuk'", r"(agar supaya|demi untuk|kalau seandainya|seperti misalnya)")
cari("'dimana' penghubung (bukan kata tanya)", r"\b(dimana|di mana)\b[^?]{0,60}(yang|menyimpan|memiliki|memungkinkan)")
# 11. di tahun/di era (harus 'pada')
cari("'di tahun/di hari/di era'", r"\bdi (tahun|hari|era|bulan)\b")
# 12. Methodology vs metode
cari("'metodologi' (non-judul)", r"metodologi")
# 13. 'kemampuan untuk', 'upaya untuk' pleonasme ringan
cari("'hal tersebut/ yang mana hal'", r"(hal tersebut|yang mana hal|dalam rangka untuk)")
# 14. Pemisah deiksis semu utk tabel/gambar
cari("Deiksis semu 'tabel/grafik di bawah/di atas'", r"(tabel|grafik|gambar|bagan|diagram) (di bawah ini|di atas|berikut)")
# 15. Penjamakan ganda
cari("Penjamakan ganda", r"(para|beberapa|berbagai|semua) \w+-\w{3,}")
# 16. 'berdasarkan pada'
cari("'berdasarkan pada'", r"berdasarkan pada")
# 17. Koma sebelum 'dan' antara dua klausa penuh (sering AI)
cari("'semakin ... semakin'", r"semakin[^.]{2,60}semakin")
# 18. 'sangat penting' & pujian tanpa bukti
cari("Pujian tanpa bukti", r"\b(sangat penting|sangat krusial|amat penting|krusial)\b")
# 19. 'dari pada' salah
cari("'dari pada' (harus daripada)", r"dari pada")
# 20. 'banyak digunakan/ banyak dipakai' vs 'banyak yang' — cek ragam
cari("'disebabkan karena'", r"disebabkan karena")
cari("'dan lain sebagainya'", r"dan lain sebagainya")
print("\n=== SELESAI ===")
