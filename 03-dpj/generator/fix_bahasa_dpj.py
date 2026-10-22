#!/usr/bin/env python3
"""fix_bahasa_dpj.py — Sunting bahasa 4 proposal DPJ (skill naskah-id, level SUNTING).

Kontrak yang diikuti (naskah-id KONTRAK.md):
- TIDAK mengubah angka, hasil, nama, sitasi, dan urutan argumen.
- Hanya: ejaan (EYD V), kata baku (KBBI), tanda baca, susunan kalimat,
  perangkai, pleonasme, nominalisasi, dan kalke Inggris.
- Satu daftar perbaikan dipakai untuk markdown DAN modul konten JS agar
  DOCX hasil regenerasi tetap sinkron dengan markdown.

Setiap pasangan (old, new) dipakai dengan str.replace; jumlah kemunculan
yang berhasil diterapkan dilaporkan per berkas.
"""
import io
import os
import sys

MD_DIR = "/home/z/my-project/download/markdown"
JS_DIR = "/home/z/my-project/scripts"

MD_FILES = {
    "DPJ-1": f"{MD_DIR}/DPJ-1_Kandang-Broiler.md",
    "DPJ-2": f"{MD_DIR}/DPJ-2_Kelas-SLB.md",
    "DPJ-3": f"{MD_DIR}/DPJ-3_Asrama-SLB.md",
    "DPJ-4": f"{MD_DIR}/DPJ-4_Isyarat-SIBI-BISINDO.md",
}
JS_FILES = {
    "DPJ-1": f"{JS_DIR}/dpj_content_1_ayam.js",
    "DPJ-2": f"{JS_DIR}/dpj_content_2_kelas.js",
    "DPJ-3": f"{JS_DIR}/dpj_content_3_asrama.js",
    "DPJ-4": f"{JS_DIR}/dpj_content_4_isyarat.js",
}

# ============ Perbaikan GLOBAL (4 berkas) ============
GLOBAL = [
    # EJ-10 (K): koma sebelum "sehingga" saat anak kalimat mengikuti induk (EYD V, tanda koma kaidah 4)
    (", sehingga", " sehingga"),
    # Sitasi dalam teks: dkk. untuk et al. (sitasi.md; naskah Indonesia, sasaran kampus)
    ("et al.", "dkk."),
    # Kata depan "per" ditulis terpisah (EYD V)
    ("per-ekor", "per ekor"),
    ("per-individu", "per individu"),
    ("per-subcarrier", "per subcarrier"),
    ("per-gestur", "per gestur"),
    ("per-sesi", "per sesi"),
    ("per-penandatangan", "per penandatangan"),
    # Gabungan kata (EYD V)
    ("blok-waktu", "blok waktu"),
    # Perbandingan baku
    ("dibandingkan terhadap", "dibandingkan dengan"),
    # Mubazir "untuk" setelah "bertujuan" + verba langsung (kalimat-efektif.md)
    ("bertujuan untuk menguji", "bertujuan menguji"),
    # Kalimat penuntas daftar yang terpotong (tanpa "adalah")
    ("Rumusan masalah pada penelitian ini sebagai berikut.",
     "Rumusan masalah pada penelitian ini adalah sebagai berikut."),
    ("Adapun batasan masalah pada penelitian ini sebagai berikut.",
     "Adapun batasan masalah pada penelitian ini adalah sebagai berikut."),
    # Nama mata uang huruf kecil (KBBI: rupiah)
    ("dalam Rupiah", "dalam rupiah"),
    # Kalimat majemuk tak setara: pemisahan dua klausa yang ditaut koma
    (", terdapat juga beberapa celah masalah (gap) yang belum terselesaikan secara simultan",
     ". Masih terdapat beberapa celah masalah (gap) yang belum terselesaikan secara simultan"),
    # Pasif tanpa pelaku "oleh"
    ("direplikasi sekolah lain", "direplikasi oleh sekolah lain"),
]

# ============ Perbaikan per berkas ============
PER_FILE = {
    "DPJ-1": [
        # KB-01 (K): kata baku
        ("kontinyu", "kontinu"),
        # Kalke Inggris "small and numerous" -> bentuk Indonesia natural
        ("kawanan unggas kecil-kecil banyak", "kawanan unggas berbadan kecil dan berjumlah banyak"),
        ("unggas kecil-kecil banyak", "unggas berbadan kecil dan berjumlah banyak"),
        # Frasa "hal jujur" -> "catatan jujur" (sejajar berkas lain)
        ("Dua hal jujur perlu dicatat sejak awal.", "Dua catatan jujur perlu dicatat sejak awal."),
        # Pengulangan "ini ... ini"
        ("Pola pendekatan ini sejalan dengan kebutuhan penelitian ini:",
         "Pola pendekatan tersebut sejalan dengan kebutuhan penelitian ini:"),
        # EJ-05: bentuk terikat "anti-" serangkai
        ("(anti korosi amonia)", "(antikorosi amonia)"),
        # Kapitalisasi
        ("Kamera/WebCam sinkron", "Kamera/webcam sinkron"),
        # Kalimat >35 kata dipecah (KE)
        ("wajib diubah di firmware dan server, dan denyut jantung ayam (250 hingga 330 denyut per menit) tidak mungkin diukur tanpa desain ulang filter.",
         "wajib diubah di firmware dan server. Denyut jantung ayam (250 hingga 330 denyut per menit) bahkan tidak mungkin diukur tanpa desain ulang filter."),
        # Nominalisasi "melakukan dekoding" (kalimat-efektif.md)
        ("yang melakukan dekoding frame", "yang menangani dekoding frame"),
        # Verba tujuan konkret (bukan "Mengetahui")
        ("Mengetahui hasil pengujian control chart z-score adaptif",
         "Menguji control chart z-score adaptif"),
        # Pasif tanpa "oleh"
        ("direplikasi peternak dan peneliti lain", "direplikasi oleh peternak dan peneliti lain"),
        # "antar-hari" -> bentuk bebas yang natural
        ("validasi antar-hari", "validasi pada hari yang berbeda"),
    ],
    "DPJ-2": [
        # AI-14 (K): "di mana" penghubung -> "saat"
        ("di mana perhatian guru terbagi", "saat perhatian guru terbagi"),
        # Frasa tak lengkap
        ("dari populasi dewasa neurotipikal pada umumnya data latih",
         "dari populasi dewasa neurotipikal yang umumnya menjadi data latih"),
        # Kelengkapan predikat
        ("kemampuan deteksi jatuh realistis untuk dijanjikan",
         "kemampuan deteksi jatuh cukup realistis untuk dijanjikan"),
        # Luluh k: "mengkalibrasi" diragukan status KBBI -> istilah yang sudah dipakai naskah
        ("mengkalibrasi ulang parameter sensing Wi-Fi dari populasi dewasa ke populasi anak",
         "menyetel ulang parameter sensing Wi-Fi dari populasi dewasa ke populasi anak"),
        # Kalke "dewasa-ke-anak" -> bentuk frasa
        ("kalibrasi dewasa-ke-anak dijadikan kontribusi utama",
         "kalibrasi dari dewasa ke anak dijadikan kontribusi utama"),
        ("penyetelan parameter dewasa-ke-anak sebagai kontribusi kalibrasi",
         "penyetelan parameter dari nilai dewasa ke populasi anak sebagai kontribusi kalibrasi"),
        # Tanda hubung bentuk terikat (EJ-05)
        ("lintas-individu", "lintas individu"),
        ("antar-individu", "antarindividu"),
        ("antar-ruang", "antarruang"),
        # Satuan SI konsisten dengan tabel (ms)
        ("debouncing di bawah 200 milidetik", "debouncing di bawah 200 ms"),
        # Konsistensi istilah: ambang (bukan threshold)
        ("perbaikan threshold", "penyetelan ulang ambang"),
        ("mengkatalogkan", "mengelompokkan"),
    ],
    "DPJ-3": [
        # Kalke "kontak-less" -> padanan yang sudah hidup
        ("memantau tidur secara kontak-less", "memantau tidur tanpa kontak"),
        ("Wi-Sleep kontak-less via Wi-Fi", "Wi-Sleep tanpa kontak via Wi-Fi"),
        # "mendeploy"/"deployment" -> padanan
        ("mendeploy sistem sensing Wi-Fi", "menerapkan sistem sensing Wi-Fi"),
        ("yang menunjukkan pola deployment pada penghuni sensitif dapat dilakukan",
         "yang menunjukkan penerapan pada penghuni sensitif dapat dilakukan"),
        ("mendokumentasikan deployment sensing Wi-Fi", "mendokumentasikan penerapan sensing Wi-Fi"),
        # "berada di" + rentang angka
        ("berada di 18 hingga 25 napas per menit", "berada pada rentang 18 hingga 25 napas per menit"),
        # Frasa kabur
        ("ruang tidur anak adalah ruang paling sensitif dari alat-alat yang dipertimbangkan",
         "ruang tidur anak adalah konteks paling sensitif dari seluruh alat yang dipertimbangkan"),
        ("laju napas anak 18 hingga 25 napas per menit berada dekat batas atas band sehingga",
         "laju napas anak 18 hingga 25 napas per menit mendekati batas atas band sehingga"),
        # Kalke "terkunci di belakang" (locked behind)
        ("terkunci di belakang fitur kompilasi khusus", "hanya aktif bila dikompilasi dengan fitur khusus"),
        # EJ-05: "multi-" serangkai
        ("multi penghuni per kamar", "multipenghuni per kamar"),
        # Pasif tanpa "oleh"
        ("dapat dipakai ulang asrama lain", "dapat dipakai ulang oleh asrama lain"),
        ("direplikasi asrama lain", "direplikasi oleh asrama lain"),
        # Kalke "dewasa-ke-anak"
        ("diakhiri rekomendasi parameter dewasa-ke-anak", "diakhiri rekomendasi parameter dari dewasa ke anak"),
        ("rekomendasi parameter dewasa-ke-anak dan protokol izin berjenjang",
         "rekomendasi parameter dari dewasa ke anak dan protokol izin berjenjang"),
        # Verba tujuan konkret
        ("Mengetahui hasil pengujian deteksi anomali", "Menguji deteksi anomali"),
        # Kelengkapan keterangan
        ("konstanta filter diubah terdokumentasi di firmware dan server",
         "konstanta filter diubah secara terdokumentasi di firmware dan server"),
        ("ubah konstanta filter terdokumentasi", "ubah konstanta filter secara terdokumentasi"),
        # Konsistensi istilah
        ("perbaikan threshold", "penyetelan ulang ambang"),
        ("mengkatalogkan", "mengelompokkan"),
        # Nominalisasi
        ("pengasuh melakukan patroli berkala", "pengasuh berpatroli berkala"),
    ],
    "DPJ-4": [
        # Kalke Inggris dan kelengkapan predikat
        ("mengkatalogkan", "mengelompokkan"),
        ("dapat dilakukan perangkat murah seperti ESP32", "dapat dilakukan dengan perangkat murah seperti ESP32"),
        ("Literatur saat proposal ini disusun belum menemukan",
         "Pencarian literatur saat proposal ini disusun belum menemukan"),
        ("literatur yang tumbuh nyata-nyata berbasis visi", "literatur yang nyata-nyata tumbuh berbasis visi"),
        ("laptop pengolahan data menggunakan milik pribadi",
         "laptop pengolahan data memakai perangkat milik pribadi"),
        # Kapitalisasi nama diri
        ("karakteristik doppler gerak lengan", "karakteristik Doppler gerak lengan"),
        # EJ-05 dan bentuk terikat/hubung
        ("antar-ruang", "antarruang"),
        ("lintas-domain", "lintas domain"),
        ("lintas-person", "lintas penandatangan"),
        ("lintas-sesi", "lintas sesi"),
        ("dalam-sesi", "dalam sesi"),
        ("lintas-ruang", "lintas ruang"),
        ("pengenalan multi-penandatangan simultan", "pengenalan beberapa penandatangan secara simultan"),
        ("titik tidak-kembali", "titik tanpa jalan kembali"),
        ("keputusan lanjut-atau-berhenti", "keputusan untuk lanjut atau berhenti"),
        # Kata asing + imbuhan -> padanan (EYD V)
        ("entitas alert ter-update", "entitas alert diperbarui"),
        ("entropy", "entropi"),
        # Perbandingan baku
        ("lebih ringan dibanding kasus pemantauan anak", "lebih ringan dibandingkan dengan kasus pemantauan anak"),
        # Tata kalimat
        ("gestur yang berbeda artinya namun mirip geraknya", "gestur yang berbeda arti tetapi mirip geraknya"),
        ("atau alih ke judul cadangan", "atau beralih ke judul cadangan"),
        ("threshold energi gerak disetel per ruang", "ambang energi gerak disetel per ruang"),
        # Verba tujuan konkret
        ("Mengetahui hasil pengujian akurasi klasifikasi", "Menguji akurasi klasifikasi"),
    ],
}


def apply_fixes(text, fixes, label, report):
    for old, new in fixes:
        n = text.count(old)
        if n == 0:
            report.append(f"  [MISS] {label}: tidak ditemukan -> {old[:70]}")
            continue
        text = text.replace(old, new)
        report.append(f"  [{n}x] {label}: {old[:60]}...")
    return text


def main():
    report = []
    for key in MD_FILES:
        # Markdown
        with io.open(MD_FILES[key], encoding="utf-8") as fh:
            md = fh.read()
        md = apply_fixes(md, GLOBAL, f"{key}/md", report)
        md = apply_fixes(md, PER_FILE[key], f"{key}/md", report)
        with io.open(MD_FILES[key], "w", encoding="utf-8") as fh:
            fh.write(md)
        # JS
        with io.open(JS_FILES[key], encoding="utf-8") as fh:
            js = fh.read()
        js = apply_fixes(js, GLOBAL, f"{key}/js", report)
        js = apply_fixes(js, PER_FILE[key], f"{key}/js", report)
        with io.open(JS_FILES[key], "w", encoding="utf-8") as fh:
            fh.write(js)
        print(f"{key}: md+js diperbarui")

    print("\n==== LAPORAN APLIKASI ====")
    miss = [r for r in report if "[MISS]" in r]
    print("\n".join(report))
    print(f"\nTOTAL entri: {len(report)} | MISS: {len(miss)}")
    if miss:
        sys.exit(1)


if __name__ == "__main__":
    main()
