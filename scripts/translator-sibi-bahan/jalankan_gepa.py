# -*- coding: utf-8 -*-
"""Pelari optimisasi GEPA untuk dossier bahan Translator SIBI.

Mode: single-task (tanpa dataset/valset), kandidat = dict 8 komponen,
backend gepa, LM refleksi = ZaiLM (z-ai chat, glm-4-plus), evaluator =
evaluator_bahan.evaluate (hibrida objektif x juri LLM).

Jalankan:  nohup python3 jalankan_gepa.py > runs/run.log 2>&1 &
"""

import json
import os
import sys
import time

_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _DIR)
os.chdir(_DIR)

from lm_zai import ZaiLM
import benih_komponen as b1
import benih_lanjutan as b2
from bagian_tetap import rakit
from evaluator_bahan import evaluate

from gepa.optimize_anything import (
    optimize_anything, GEPAConfig, EngineConfig, ReflectionConfig,
)
from gepa.utils.stop_condition import TimeoutStopCondition

RUNS = os.path.join(_DIR, "runs")
os.makedirs(RUNS, exist_ok=True)

SEED = {
    "ringkasan": b1.RINGKASAN,
    "arah_latar": b1.ARAH_LATAR,
    "peta_masalah": b1.PETA_MASALAH,
    "konsep_alat": b1.KONSEP_ALAT,
    "kit_bab1": b2.KIT_BAB1,
    "kit_bab23": b2.KIT_BAB23,
    "sidang": b2.SIDANG,
    "keputusan": b2.KEPUTUSAN,
}

TEMPLATE_REFLEKSI = """Kamu menyunting SATU bagian dossier bahan penulisan proposal skripsi berbahasa Indonesia. Topik riset: purwarupa penerjemah dua arah isyarat SIBI berbasis Wi-Fi CSI pada 2-3 modul ESP32-S3 (inferensi pengenalan di perangkat; TTS/ASR Bahasa Indonesia di server lokal laptop; kamera dan model pose YOLO26 hanya pada jalur pelabelan riset; produk akhir tanpa kamera).

NILAI BAGIAN SAAT INI:
```
<curr_param>
```

UMPAN BALIK EVALUATOR (skor, masalah objektif, kritik juri):
```
<side_info>
```

Tulis ulang bagian itu supaya lebih baik. Aturan mutlak:
1. Pertahankan SEMUA fakta dan angka apa adanya: angka persen, jumlah, satuan, nomor rujukan [n], nama sistem (SignFi, WiSign, WiKey, KASIBI, OpenSIBI, MMS-TTS-ind, faster-whisper, Kokoro, YOLO26, RuView), istilah teknis. Jangan menambah fakta atau angka baru.
2. Kembalikan jangkar yang hilang (daftarnya ada di umpan balik) dengan memakai kata yang sama.
3. Pertahankan semua penanda [PERLU DATA: ...] beserta maknanya.
4. Bahasa Indonesia baku EYD V: tanpa "di era digital", "tidak dapat dipungkiri", "perlu diingat", "hal ini" berlebihan, "di mana/yang mana" sebagai penghubung, tanpa pleonasme ("adalah merupakan", "agar supaya"); kata baku: risiko, praktik, analisis, aktivitas, sistem; "di-" serangkai untuk verba pasif.
5. Jangan tulis klaim terlarang tanpa negasi: penerjemah kalimat penuh, penerjemahan kontinu, pengenalan isyarat kontinu, mengenali bentuk jari/konfigurasi jari/ekspresi wajah dari CSI, menggantikan juru bahasa, meningkatkan empati sebagai hasil, janji angka akurasi/latensi. Bila topik itu perlu disebut, selalu dengan "bukan", "tidak", atau "di luar cakupan".
6. Bentuk keluaran identik: markdown dengan kepala ###, daftar bernomor/berbutir, tabel apa adanya; panjang minimal sama dengan aslinya (boleh lebih panjang bila menambah kejelasan, tidak boleh mengerdilkan).
7. Jawab kritik juri pada umpan balik dengan perbaikan nyata, bukan menambah kata formal.

Keluaran: HANYA teks bagian baru di dalam satu blok ``` ... ``` tanpa kalimat pembuka atau penjelasan.
"""


def main():
    tanda_waktu = time.strftime("%Y%m%d-%H%M%S")
    run_dir = os.path.join(RUNS, f"gepa-{tanda_waktu}")
    os.makedirs(run_dir, exist_ok=True)

    print(f"[RUN] mulai {tanda_waktu}; run_dir={run_dir}", flush=True)

    config = GEPAConfig(
        engine=EngineConfig(
            run_dir=run_dir,
            seed=2610,
            max_metric_calls=48,
            max_candidate_proposals=14,
            raise_on_exception=False,
            parallel=False,
            use_cloudpickle=True,
            display_progress_bar=False,
        ),
        reflection=ReflectionConfig(
            reflection_lm=ZaiLM(),
            reflection_prompt_template=TEMPLATE_REFLEKSI,
            module_selector="round_robin",
            reflection_minibatch_size=1,
        ),
        stop_callbacks=[TimeoutStopCondition(3000)],
    )

    hasil = optimize_anything(
        SEED,
        evaluator=evaluate,
        config=config,
    )

    print(f"[RUN] selesai", flush=True)

    # gepa 0.1.4: GEPAResult tidak memuat best_score/best_candidate;
    # yang terbaik = indeks skor agregat valset tertinggi.
    skor_list = list(hasil.val_aggregate_scores)
    idx_terbaik = max(range(len(skor_list)), key=lambda i: skor_list[i])
    terbaik = hasil.candidates[idx_terbaik]
    print(f"[RUN] best idx={idx_terbaik} skor={skor_list[idx_terbaik]}", flush=True)
    if isinstance(terbaik, dict):
        with open(os.path.join(run_dir, "kandidat_terbaik.json"), "w", encoding="utf-8") as f:
            json.dump(terbaik, f, ensure_ascii=False, indent=1)
        with open(os.path.join(run_dir, "dossier_terbaik.md"), "w", encoding="utf-8") as f:
            f.write(rakit(terbaik))
    ringkas = {
        "best_idx": idx_terbaik,
        "best_score": skor_list[idx_terbaik],
        "semua_skor": skor_list,
        "total_metric_calls": getattr(hasil, "total_metric_calls", None),
        "waktu": tanda_waktu,
    }
    with open(os.path.join(run_dir, "ringkasan.json"), "w", encoding="utf-8") as f:
        json.dump(ringkas, f, ensure_ascii=False, indent=1)
    print(f"[RUN] artefak tersimpan di {run_dir}", flush=True)


if __name__ == "__main__":
    main()
