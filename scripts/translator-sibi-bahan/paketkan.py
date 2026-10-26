# -*- coding: utf-8 -*-
"""Pengemasan akhir: rakit kandidat terbaik -> dossier final + jejak GEPA.

Pemakaian: python3 paketkan.py [run_dir]
Bila run_dir tidak diberikan atau kandidat terbaik gagal cek jangkar,
dossier dirakit dari benih (yang telah lolos seluruh cek).
"""

import json
import os
import shutil
import subprocess
import sys

_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _DIR)

import benih_komponen as b1
import benih_lanjutan as b2
from bagian_tetap import rakit
from jangkar import periksa_komponen, KOMPONEN_UTAMA

TUJUAN = "/home/z/my-project/download/translator-sibi-bahan"
PERIKSA = "/home/z/my-project/skills-arsip/naskah-id/scripts/periksa.py"

SEED = {
    "ringkasan": b1.RINGKASAN, "arah_latar": b1.ARAH_LATAR,
    "peta_masalah": b1.PETA_MASALAH, "konsep_alat": b1.KONSEP_ALAT,
    "kit_bab1": b2.KIT_BAB1, "kit_bab23": b2.KIT_BAB23,
    "sidang": b2.SIDANG, "keputusan": b2.KEPUTUSAN,
}


def muat_kandidat(run_dir):
    if not run_dir:
        return None, "run_dir tidak diberikan"
    path = os.path.join(run_dir, "kandidat_terbaik.json")
    if not os.path.exists(path):
        return None, f"{path} tidak ada"
    with open(path, encoding="utf-8") as f:
        kandidat = json.load(f)
    if not isinstance(kandidat, dict) or set(kandidat) != set(KOMPONEN_UTAMA):
        return None, "struktur kandidat tidak lengkap"
    masalah = []
    for nama in KOMPONEN_UTAMA:
        masalah.extend(periksa_komponen(nama, kandidat[nama])["masalah"])
    if masalah:
        return None, "kandidat terbaik melanggar kontrak: " + "; ".join(masalah)[:300]
    identik = all(kandidat[n] == SEED[n] for n in KOMPONEN_UTAMA)
    return kandidat, ("identik dengan benih" if identik else "mutasi diterima")


def main():
    run_dir = sys.argv[1] if len(sys.argv) > 1 else None
    kandidat, status = muat_kandidat(run_dir)
    if kandidat is None:
        print(f"[PAKET] kandidat terbaik TIDAK dipakai ({status}); memakai benih.")
        kandidat, status = SEED, "benih (lolos cek)"
    print(f"[PAKET] sumber dossier: {status}")

    os.makedirs(TUJUAN, exist_ok=True)
    dokumen = rakit(kandidat)
    path_doc = os.path.join(TUJUAN, "Bahan-Proposal-Translator-SIBI.md")
    with open(path_doc, "w", encoding="utf-8") as f:
        f.write(dokumen)
    print(f"[PAKET] dossier: {path_doc} ({len(dokumen)} karakter, {dokumen.count(chr(10))} baris)")

    # Verifikasi ulang seluruh kontrak pada dokumen final
    total_masalah = 0
    for nama in KOMPONEN_UTAMA:
        h = periksa_komponen(nama, kandidat[nama])
        total_masalah += len(h["masalah"])
    print(f"[PAKET] cek objektif final: {total_masalah} masalah")

    # Jejak GEPA
    jejak = os.path.join(TUJUAN, "gepa")
    os.makedirs(jejak, exist_ok=True)
    for berkas in ("evaluator_bahan.py", "jangkar.py", "jalankan_gepa.py",
                   "lm_zai.py", "benih_komponen.py", "benih_lanjutan.py",
                   "bagian_tetap.py"):
        shutil.copy2(os.path.join(_DIR, berkas), os.path.join(jejak, berkas))
    if run_dir:
        for nama in ("ringkasan.json", "kandidat_terbaik.json", "run_log.txt",
                     "candidates.json"):
            sumber = os.path.join(run_dir, nama)
            if os.path.exists(sumber):
                shutil.copy2(sumber, os.path.join(jejak, nama))
        log_sumber = "/home/z/my-project/scripts/translator-sibi-bahan/runs/run.log"
        if os.path.exists(log_sumber):
            shutil.copy2(log_sumber, os.path.join(jejak, "run.log"))
    print(f"[PAKET] jejak GEPA: {jejak}")

    # Lint naskah-id (petunjuk, bukan putusan)
    if os.path.exists(PERIKSA):
        proc = subprocess.run(
            ["python3", PERIKSA, path_doc], capture_output=True, text=True, timeout=120
        )
        print("[PAKET] lint periksa.py:")
        print(proc.stdout[:3000] or proc.stderr[:1000])

    # Statistik penanda
    n_penanda = dokumen.count("[PERLU DATA")
    print(f"[PAKET] penanda [PERLU DATA] pada dokumen final: {n_penanda}")


if __name__ == "__main__":
    main()
