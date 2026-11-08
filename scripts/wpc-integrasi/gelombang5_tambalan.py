#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tambalan gelombang 5: paragraf purwarupa 1.1 (2-3 modul -> sepasang)."""
from pathlib import Path

DRAFT = Path("/home/z/my-project/download/translator-sibi-final/draft-final.md")
teks = DRAFT.read_text(encoding="utf-8")

LAMA = ("Purwarupa yang dirancang terdiri atas 2\u20133 modul ESP32-S3 yang portabel dan direncanakan memiliki layar, "
        "baterai, *speaker*, mikrofon, tombol tekan-untuk-bicara, dan rotary encoder volume. Pada arah pertama, "
        "modul pemancar dan modul penerima mengapit zona isyarat. Modul penerima menangkap CSI, mengenali isyarat "
        "melalui model murid yang berjalan pada perangkat,")
BARU = ("Purwarupa yang dirancang terdiri atas sepasang modul ESP32-S3 yang portabel; node pemancar dan node penerima "
        "mengapit zona isyarat, sedangkan node penerima sekaligus memuat antarmuka pengguna berupa layar, baterai, "
        "*speaker*, mikrofon, tombol tekan-untuk-bicara, dan rotary encoder volume. Pada arah pertama, node penerima "
        "menangkap CSI dari paket *beacon* ESP-NOW yang dipancarkan node pemancar, mengenali isyarat melalui model "
        "murid yang berjalan pada perangkat,")

c = teks.count(LAMA)
assert c == 1, c
teks = teks.replace(LAMA, BARU)
DRAFT.write_text(teks, encoding="utf-8")

# verifikasi ulang sisa
t2 = DRAFT.read_text(encoding="utf-8")
akar = t2.find("AKHIR NASKAH")
tubuh = t2[:akar]
for frasa in ["2\u20133 modul", "dua hingga tiga modul", "17 keypoint COCO", "YOLO26-Pose"]:
    print(f"  {frasa!r} di tubuh naskah: {'MASIH ADA!' if frasa in tubuh else 'bersih'}")
print("tambalan selesai")
