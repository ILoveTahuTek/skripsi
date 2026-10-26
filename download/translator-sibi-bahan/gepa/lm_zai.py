# -*- coding: utf-8 -*-
"""LanguageModel kustom untuk GEPA: dibungkus CLI `z-ai chat` (glm-4-plus).

Mengikuti protokol LM gepa: __call__(prompt: str | list[dict]) -> str.
Prompt panjang (kandidat + umpan balik) dikirim sebagai argumen subprocess
tanpa shell sehingga bebas masalah kutipan.
"""

import json
import os
import subprocess
import tempfile
import time


class ZaiLM:
    def __init__(self, per_call_timeout=420, retries=3, verbose=True):
        self.per_call_timeout = per_call_timeout
        self.retries = retries
        self.verbose = verbose
        self.n_panggilan = 0

    def _kirim(self, system: str | None, user: str) -> str:
        fd, path = tempfile.mkstemp(suffix=".json")
        os.close(fd)
        try:
            cmd = ["z-ai", "chat", "--prompt", user, "-o", path]
            if system:
                cmd += ["--system", system]
            proc = subprocess.run(
                cmd, capture_output=True, text=True,
                timeout=self.per_call_timeout,
            )
            if proc.returncode != 0:
                raise RuntimeError(f"z-ai gagal: {proc.stderr[:300]}")
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)
            isi = data["choices"][0]["message"]["content"]
            if not isi or not isi.strip():
                raise RuntimeError("z-ai mengembalikan kosong")
            return isi
        finally:
            try:
                os.unlink(path)
            except OSError:
                pass

    def __call__(self, prompt) -> str:
        self.n_panggilan += 1
        if isinstance(prompt, list):
            system_bag = " ".join(
                m.get("content", "") for m in prompt
                if m.get("role") in ("system", "assistant")
            ).strip()
            user_bag = "\n\n".join(
                m.get("content", "") for m in prompt if m.get("role") == "user"
            ).strip()
            if not user_bag:
                user_bag = " ".join(
                    m.get("content", "") for m in prompt
                ).strip()
        else:
            system_bag, user_bag = None, str(prompt)
        kesalahan = None
        for attempt in range(1, self.retries + 1):
            try:
                out = self._kirim(system_bag or None, user_bag)
                if self.verbose:
                    print(f"[ZaiLM] panggilan #{self.n_panggilan} percobaan "
                          f"{attempt} OK ({len(out)} karakter)", flush=True)
                return out
            except Exception as e:  # noqa: BLE001
                kesalahan = e
                if self.verbose:
                    print(f"[ZaiLM] panggilan #{self.n_panggilan} percobaan "
                          f"{attempt} GAGAL: {e}", flush=True)
                time.sleep(5 * attempt)
        raise RuntimeError(f"ZaiLM gagal setelah {self.retries} percobaan: {kesalahan}")
