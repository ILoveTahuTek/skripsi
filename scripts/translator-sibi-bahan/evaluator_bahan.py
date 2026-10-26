# -*- coding: utf-8 -*-
"""Evaluator hibrida untuk dossier bahan Translator SIBI (dipakai GEPA).

Skor = (fraksi komponen bersih cek objektif) x (rata-rata juri LLM / 10).
Cek objektif: jangkar fakta, klaim terlarang bertuas-negasi, penanda
[PERLU DATA], panjang minimal. Juri: rubrik lima dimensi via z-ai (glm-4-plus).
Umpan balik rich: masalah objektif + kritik juri per bagian, dirutekan ke
komponen terkait lewat kunci {komponen}_specific_info.
"""

import json
import re
import tempfile
import os
import subprocess

from jangkar import periksa_komponen, KOMPONEN_UTAMA
from bagian_tetap import rakit

SYSTEM_JURI = (
    "Anda juru ketat dokumen bahan penulisan proposal skripsi Indonesia. "
    "Anda menilai KUALITAS sebagai bahan kerja penulis naskah, bukan kebenaran hasil penelitian. "
    "Nilai dengan keras tetapi adil: 9-10 hanya untuk kualitas luar biasa, 7-8 baik, "
    "5-6 cukup, 3-4 lemah, 0-2 buruk. Keluarkan HANYA JSON sah tanpa kalimat lain."
)

RUBRIK = """Nilai delapan seksi mudah-sunting dokumen berikut (seksi 0, 1, 2, 8, 9, 10, 11, 12) pada lima dimensi, masing-masing 0-10 satu desimal:

D1 kesesuaian-topik: seluruh bagian konsisten dengan visi produk — purwarupa penerjemah DUA ARAH berbasis 2-3 modul ESP32-S3; inferensi pengenalan di perangkat; TTS/ASR di server lokal laptop; kamera dan YOLO26 hanya jalur pelabelan riset; produk akhir tanpa kamera; tidak ada sisa kerangka lama "alat latihan satu arah" sebagai muara; server lokal vs cloud jarak jauh dibedakan.
D2 kegunaan-bahan: cukup konkret dan kaya untuk menulis dan membela proposal — bata kalimat siap pakai, fakta dengan rujukan [n], arah kerja jelas, tidak ada bagian melompong atau generik.
D3 bahasa-baku: bahasa Indonesia baku (EYD V), kalimat efektif, bebas pola tulisan mesin (pembuka kosmik, penghubung ritual, pleonasme), istilah konsisten.
D4 disiplin-klaim: klaim sebanding bukti; janji teknis dibingkai hipotesis/gerbang; batas MVP (5-8 isyarat terisolasi, bukan kalimat, tanpa jari/wajah) konsisten di mana-mana.
D5 koherensi-antarbagian: istilah dan angka konsisten antarseksi; tidak ada kontradiksi antara ringkasan, masalah, konsep, kit, dan antisipasi sidang.

Seksi 3-7 dan 13 (bank fakta, bank rujukan, perangkat, tabel gerbang-risiko, lampiran) adalah REFERENSI TETAP: jangan dinilai, gunakan sebagai pembanding kebenaran angka.

Kembalikan JSON dengan bentuk persis:
{"D1": angka, "D2": angka, "D3": angka, "D4": angka, "D5": angka, "komentar_umum": "dua-tiga kalimat kritik tersukses", "komentar_per_bagian": {"ringkasan": "satu-dua kalimat kritik konkret", "arah_latar": "...", "peta_masalah": "...", "konsep_alat": "...", "kit_bab1": "...", "kit_bab23": "...", "sidang": "...", "keputusan": "..."}}

Kritik harus menyebut kalimat/bagian spesifik yang bisa diperbaiki, bukan pujian umum.

DOKUMEN YANG DINILAI:
"""


def _panggil_zai(system: str, user: str, timeout=420, retries=2):
    fd, path = tempfile.mkstemp(suffix=".json")
    os.close(fd)
    try:
        cmd = ["z-ai", "chat", "--prompt", user, "-o", path]
        if system:
            cmd += ["--system", system]
        proc = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
        if proc.returncode != 0:
            raise RuntimeError(f"z-ai gagal: {proc.stderr[:200]}")
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)["choices"][0]["message"]["content"]
    finally:
        try:
            os.unlink(path)
        except OSError:
            pass


def _parse_json_juri(teks: str):
    if not teks:
        return None
    a, b = teks.find("{"), teks.rfind("}")
    if a >= 0 and b > a:
        try:
            return json.loads(teks[a:b + 1])
        except json.JSONDecodeError:
            pass
    # fallback: ekstrak per kunci
    out = {}
    for kunci in ("D1", "D2", "D3", "D4", "D5"):
        m = re.search(rf'"{kunci}"\s*:\s*([0-9]+(?:\.[0-9]+)?)', teks)
        if m:
            out[kunci] = float(m.group(1))
    m = re.search(r'"komentar_umum"\s*:\s*"([^"]{10,})"', teks)
    if m:
        out["komentar_umum"] = m.group(1)
    return out or None


def panggil_juri(dokumen: str):
    """Panggil juri LLM; kembalikan dict atau None bila gagal."""
    try:
        mentah = _panggil_zai(SYSTEM_JURI, RUBRIK + dokumen)
    except Exception as e:  # noqa: BLE001
        return {"error": str(e)[:200]}
    return _parse_json_juri(mentah)


def evaluate(candidate):
    """Evaluator GEPA: kandidat dict 8 komponen -> (skor, info)."""
    try:
        return _evaluate_dalam(candidate)
    except Exception as e:  # noqa: BLE001
        return 0.0, {"error": f"evaluator gagal: {e!r}"[:300]}


def _evaluate_dalam(candidate):
    # --- Cek objektif per komponen ---
    hasil = {}
    masalah_semua = []
    for nama in KOMPONEN_UTAMA:
        teks = candidate.get(nama, "")
        h = periksa_komponen(nama, teks)
        hasil[nama] = h
        for m in h["masalah"]:
            masalah_semua.append(m)
    n_bersih = sum(1 for h in hasil.values() if not h["masalah"])
    skor_objektif = n_bersih / len(KOMPONEN_UTAMA)

    # --- Juri LLM atas dokumen terakit ---
    dokumen = rakit(candidate)
    juri = panggil_juri(dokumen)

    nilai_d = []
    for d in ("D1", "D2", "D3", "D4", "D5"):
        v = (juri or {}).get(d)
        if isinstance(v, (int, float)) and 0 <= float(v) <= 10:
            nilai_d.append(min(10.0, float(v)))
    if len(nilai_d) == 5:
        skor_juri = sum(nilai_d) / 5 / 10.0
        juri_ok = True
    else:
        skor_juri = 0.5  # netral bila juri gagal
        juri_ok = False

    skor = round(skor_objektif * skor_juri, 4)

    # --- Umpan balik rich (dibaca LM refleksi) ---
    info = {
        "skor_total": skor,
        "skor_objektif": round(skor_objektif, 3),
        "komponen_bersih": f"{n_bersih}/{len(KOMPONEN_UTAMA)}",
        "nilai_juri": {d: (juri or {}).get(d) for d in ("D1", "D2", "D3", "D4", "D5")},
        "komentar_juri_umum": (juri or {}).get("komentar_umum", ""),
        "juri_ok": juri_ok,
        "masalah_objektif": masalah_semua[:40],
    }
    if not juri_ok:
        info["peringatan_juri"] = (
            "Keluaran juri tidak terbaca; pastikan JSON sah. "
            "Skor juri dinetralkan 0,5 pada evaluasi ini."
        )
    komentar_per = (juri or {}).get("komentar_per_bagian", {}) or {}
    for nama in KOMPONEN_UTAMA:
        info[f"{nama}_specific_info"] = {
            "masalah_bagian_ini": hasil[nama]["masalah"],
            "jangkar_hilang": hasil[nama]["jangkar_hilang"],
            "komentar_juri": komentar_per.get(nama, ""),
        }
    return skor, info
