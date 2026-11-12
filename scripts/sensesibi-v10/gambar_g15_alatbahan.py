#!/usr/bin/env python3
"""Gambar 3.2 (v15): grid foto 3x3 sembilan perangkat keras (baris 1-9 Tabel 3.1).

Foto diambil dari hasil pencarian gambar daring (imgsearch/*.json, layanan
image-search); tiap sel diberi label huruf sesuai baris Tabel 3.1 dan sumber
foto. Jika satu foto gagal diunduh, kandidat berikutnya dipakai; jika semua
gagal, sel diganti kotak abu-abu berlabel (placeholder).
"""
import io
import json
import urllib.request
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

plt.rcParams["font.sans-serif"] = ["DejaVu Sans"]
plt.rcParams["axes.unicode_minus"] = False

BASE = Path("/home/z/my-project/scripts/sensesibi-v10/imgsearch")
OUT = Path("/home/z/my-project/download/sensesibi-v10/assets-v15/gambar-3.2.png")

KOMPONEN = [
    ("01-esp32s3", "a. Modul ESP32-S3"),
    ("02-layar", "b. Layar OLED/TFT"),
    ("03-encoder", "c. Rotary encoder EC11"),
    ("04-speaker", "d. Pengeras suara + DAC"),
    ("05-mikrofon", "e. Mikrofon INMP441"),
    ("06-baterai", "f. Baterai Li-Po + TP4056"),
    ("07-laptop", "g. Laptop"),
    ("08-ponsel", "h. Ponsel pintar"),
    ("09-router", "i. Access point"),
]

def ambil_foto(stem):
    """Kembalikan (array gambar persegi, sumber) dari hasil pencarian; None jika gagal."""
    berkas = BASE / f"{stem}.json"
    if not berkas.exists():
        return None
    try:
        data = json.loads(berkas.read_text(encoding="utf-8"))
    except Exception:
        return None
    for r in data.get("results", []):
        url = r.get("original_url", "")
        if not url:
            continue
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=60) as resp:
                raw = resp.read()
            im = Image.open(io.BytesIO(raw)).convert("RGB")
            w, h = im.size
            s = min(w, h)
            im = im.crop(((w - s) // 2, (h - s) // 2, (w + s) // 2, (h + s) // 2))
            im = im.resize((560, 560), Image.LANCZOS)
            return np.asarray(im), (r.get("source") or "daring")
        except Exception:
            continue
    return None

fig, axes = plt.subplots(3, 3, figsize=(9.0, 10.1), dpi=210, constrained_layout=True)
ok_n = 0
for ax, (stem, label) in zip(axes.flat, KOMPONEN):
    hasil = ambil_foto(stem)
    if hasil is not None:
        arr, sumber = hasil
        ax.imshow(arr)
        ok_n += 1
    else:
        ax.imshow(np.full((560, 560, 3), 235, dtype=np.uint8))
        ax.text(0.5, 0.5, "[foto belum tersedia]", transform=ax.transAxes,
                ha="center", va="center", fontsize=15, color="#6b7280")
        sumber = "placeholder"
    ax.set_axis_off()
    ax.text(0.5, -0.055, label, transform=ax.transAxes, ha="center",
            va="top", fontsize=16, color="#111827", fontweight="bold")
    ax.text(0.5, -0.155, f"foto: {sumber}", transform=ax.transAxes, ha="center",
            va="top", fontsize=12, color="#6b7280")

fig.savefig(OUT, facecolor="white")
print("OK", OUT, "foto berhasil:", ok_n, "dari", len(KOMPONEN))
