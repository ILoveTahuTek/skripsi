# T17-R1 — Riset Teknologi TTS & ASR yang Mendukung Bahasa Indonesia
**Konteks proyek**: penerjemah dua arah isyarat SIBI; server lokal laptop RTX 3070 8GB + opsi cloud.

- **Task ID**: T17-R1 (percobaan ke-2; percobaan ke-1 gagal karena kehabisan waktu)
- **Tanggal riset**: 2026-10-25
- **Metode**: inspeksi langsung URL resmi via `curl` (alat WebSearch tidak tersedia di sesi ini). arXiv API terblokir sesuai instruksi → halaman `arxiv.org/abs/2212.04356` dan cermin ar5iv dipakai.
- **Label klaim**: [DIVERIFIKASI] = URL diinspeksi langsung, angka terbaca sendiri; [CUPILIKAN] = diverifikasi + kutipan teks; [TIDAK DITEMUKAN] = tidak berhasil ditemukan/diakses; [TIDAK DIVERIFIKASI] = klaim umum beredar tetapi sumber resmi gagal diakses.
- **Status dokumen**: TTS selesai; ASR diperbarui bertahap di bawah.

---

## 1. Kokoro TTS (hexgrad/Kokoro-82M)

| # | Klaim | Status | Bukti (URL diinspeksi langsung) |
|---|-------|--------|----------------------------------|
| 1.1 | Bahasa yang didukung v1.0: **American English, British English, Japanese, Mandarin Chinese, Spanish, French, Hindi, Italian, Brazilian Portuguese** (8 bahasa, 54 voice) | [CUPILIKAN] | https://huggingface.co/hexgrad/Kokoro-82M/blob/main/VOICES.md — daftar voice berbendera hanya 9 kategori di atas (11F/9M en-US, 4F/4M en-GB, 4F/1M ja, 4F/4M zh, 1F/2M es, 1F fr, 2F/2M hi, 1F/1M it, 1F/2M pt-BR) |
| 1.2 | **Bahasa Indonesia TIDAK didukung Kokoro v1.0** — jawaban tegas: TIDAK | [DIVERIFIKASI] | `grep -ic indones` pada VOICES.md → 0 kecocokan; README model card tidak memuat "Indonesian"; kutipan README: "Support for non-English languages may be absent or thin due to weak G2P and/or lack of training data" |
| 1.3 | Lisensi: **Apache-2.0** (bobot model) | [CUPILIKAN] | https://huggingface.co/hexgrad/Kokoro-82M — API HF: `"license:apache-2.0"`; README: "open-weight TTS model with 82 million parameters ... With Apache-licensed weights" |
| 1.4 | Ukuran: **82 juta parameter**; v1.0 rilis 2025-01-27 | [CUPILIKAN] | README: "Kokoro is an open-weight TTS model with 82 million parameters"; tabel versi: v1.0 \| 2025 Jan 27 \| 8 & 54 (bahasa & voice) |
| 1.5 | Varian **kokoro-onnx** (thewh1teagle): runtime ONNX, lisensi MIT, ukuran ~300 MB (kuantisasi int8 ~80 MB), bahasa mengikuti VOICES.md Kokoro → **Indonesia juga TIDAK didukung** | [CUPILIKAN] | https://github.com/thewh1teagle/kokoro-onnx (README, HTTP 200): "Lightweight: ~300MB (quantized: ~80MB)", "See the latest voices and languages in Kokoro-82M/VOICES.md", "License: kokoro-onnx: MIT" |
| 1.6 | (Konteks harga API pihak ketiga, bukan self-host): layanan Kokoro over API < US$1 per 1 juta karakter (per April 2025) | [CUPILIKAN] | README Kokoro: "the market rate of Kokoro served over API is under $1 per million characters of text input" |
| 1.7 | Latensi Kokoro: angka RTF/RFT resmi di model card | [TIDAK DITEMUKAN] | grep `RFT/RTF/realtime/real-time` pada README tidak menghasilkan tabel angka |

**Kesimpulan 1**: Kokoro (termasuk varian ONNX) TIDAK dapat dipakai untuk keluaran suara Bahasa Indonesia. Hanya relevan bila proyek butuh voice Inggris.

## 2. TTS pengganti yang mendukung Bahasa Indonesia

### 2a. facebook/mms-tts-id (HuggingFace)
- Repo `facebook/mms-tts-id` → API HF merespons `{"error":"Invalid username or password."}` (41 byte) — repo dengan id persis itu **tidak dapat diakses/tidak terverifikasi**. [DIVERIFIKASI kegagalan akses]
- Pencarian API HF `?search=mms-tts-id` mengembalikan **`facebook/mms-tts-idd`** → kandidat repo MMS-TTS untuk Bahasa Indonesia yang benar adalah kode bahasa **`idd`**, bukan `id`. [DIVERIFIKASI via https://huggingface.co/api/models?search=mms-tts-id&limit=10]
- Detail (lisensi, isi model card) → **diperbarui pada ronde ASR di bawah**.

### 2b. Google Cloud Text-to-Speech (voice `id-ID`)
- Voice yang terdaftar untuk Indonesian (Indonesia) di halaman voices resmi: **id-ID-Chirp3-HD-*** (≥25 voice: Achernar, Achird, Algenib, Algieba, Alnilam, Aoede, Autonoe, Callirrhoe, Charon, Despina, Enceladus, Erinome, Fenrir, Gacrux, Iapetus, Kore, Laomedeia, Leda, Orus, Puck, Pulcherrima, Rasalgethi, Sadachbia, Sadaltager, Schedar, …), serta keluarga **id-ID-Standard** dan **id-ID-Wavenet**. [DIVERIFIKASI] https://cloud.google.com/text-to-speech/docs/voices
- Harga per karakter (halaman pricing resmi, tier "0 to 1 million characters"): **US$4 per 1 juta karakter (Standard)**; **US$16 per 1 juta (WaveNet/Neural2)**; **US$30 per 1 juta (Chirp 3: HD)**; terlihat juga US$60 dan US$160 per 1 juta karakter (pemetaan label voice untuk kedua angka ini belum terbaca — lengkapan di bawah). [DIVERIFIKASI] https://cloud.google.com/text-to-speech/pricing
- Tingkat gratis bulanan TTS Google: **TIDAK DITEMUKAN** pada halaman pricing yang diinspeksi (yang terlihat hanya kredit pelanggan baru/kampanye "Start free"). [TIDAK DITEMUKAN]

### 2c. Azure AI Speech (voice `id-ID`)
- Voice Indonesia pada halaman dukungan bahasa resmi: **id-ID-ArdiNeural, id-ID-GadisNeural** (plus voice non-neural lama: id-ID-Ardi, id-ID-Cahya, id-ID-Gadis, id-ID-Sari). Bahasa "Indonesian (Indonesia)" tercantum untuk STT & TTS. [DIVERIFIKASI] https://learn.microsoft.com/en-us/azure/ai-services/speech-service/language-support?tabs=stt-tts
- Tingkat gratis F0 (halaman pricing resmi): **"0.5 million characters free per month"** (TTS, tier Free F0); **"Real-time Transcription: 5 audio hours free per month"** (STT, Free F0; catatan: "Free audio hours for speech to text is shared between Standard and Custom"). [CUPILIKAN] https://azure.microsoft.com/en-us/pricing/details/cognitive-services/speech-services/
- Harga berbayar per unit: halaman pricing merender angka "$-" (dinamis/JS) dan API `pricing.azure.com` gagal tersambung (HTTP 000) → **[TIDAK DIVERIFIKASI]** pada sesi ini.

### 2d. Coqui XTTS-v2 (coqui/XTTS-v2)
- Bahasa yang didukung — kutipan penuh README: "XTTS-v2 supports 17 languages: English (en), Spanish (es), French (fr), German (de), Italian (it), Portuguese (pt), Polish (pl), Turkish (tr), Russian (ru), Dutch (nl), Czech (cs), Arabic (ar), Chinese (zh-cn), Japanese (ja), Hungarian (hu), Korean (ko) Hindi (hi)". **Bahasa Indonesia TIDAK termasuk** (grep "indones" = 0 pada model card). [CUPILIKAN] https://huggingface.co/coqui/XTTS-v2
- Lisensi: **Coqui Public Model License (CPML)** — tag HF `license: other`, `license_name: coqui-public-model-license`, tautan https://coqui.ai/cpml (lisensi kustom, bukan OSI; risiko: Coiri perusahaan Coqui telah berhenti beroperasi — status lisensi/tautan perlu dicek tim hukum). [DIVERIFIKASI]
- Fitur: voice cloning lintas bahasa dari klip 6 detik; "Supports 17 languages", "Cross-language voice cloning". [CUPILIKAN]

### 2e. Piper (rhasspy/piper)
- Daftar voice resmi **VOICES.md** (HTTP 200) TIDAK memuat satu pun voice `id_ID`/Indonesian (grep "indones|id_ID" = 0). [DIVERIFIKASI] https://raw.githubusercontent.com/rhasspy/piper/master/VOICES.md
- Halaman contoh suara resmi https://rhasspy.github.io/piper-samples/ (HTTP 200) juga TIDAK memuat "indones". [DIVERIFIKASI]
- **Kesimpulan: Piper tidak menyediakan voice Bahasa Indonesia resmi.**

### 2f. Model TTS komunitas Indonesia di HuggingFace
Hasil pencarian API HF (query "indonesian tts" / "tts indonesia" / "vits indonesia"):
- `Wikidepia/indonesian-tts` — 42 unduhan/bulan [DIVERIFIKASI] https://huggingface.co/api/models/Wikidepia/indonesian-tts
- `datasetsANDmodels/indonesian-tts` — 27 unduhan/bulan [DIVERIFIKASI] https://huggingface.co/api/models/datasetsANDmodels/indonesian-tts
- Kandidat lain yang muncul: `anak10thn/pocket-tts-indonesian`, `nayerim/speecht5-indonesian-tts`, `winabadi/tts-indonesia`, `arifteguhr/tts-indonesia-v1`, `grandhigh/Chatterbox-TTS-Indonesian`, `mazrba/Chatterbox-TTS-Indonesian-gguf`, `alkhrzmy/qwen3-tts-0.6b-indonesian`. [DIVERIFIKASI daftar]
- Catatan: kolom lisensi kedua model utama tidak tercantum di API HF (→ [TIDAK DITEMUKAN]); volume unduhan sangat kecil → risiko kualitas & pemeliharaan tinggi.

---

## 3. ASR (Speech-to-Text) Bahasa Indonesia

> **[MENUNGGU RONDE 3 — bagian ini diisi setelah fetch Whisper/faster-whisper/MMS/wav2vec2/Vosk/Google STT/arXiv]**

## 4. Latensi terdokumentasi resmi

> **[MENUNGGU — diisi bersama bagian 3]**

## 5. Matriks putusan akhir

> **[MENUNGGU — diisi setelah semua klaim lengkap]**

<!-- LANJUTAN: ASR -->
