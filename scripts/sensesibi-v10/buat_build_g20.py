#!/usr/bin/env python3
# Derive build_docx_g20.sh from build_docx_g19.sh (rename paths, update metadata).
from pathlib import Path

scr = Path("/home/z/my-project/scripts/sensesibi-v10")
s = (scr / "build_docx_g19.sh").read_text(encoding="utf-8")

s = s.replace("_kerja-g19", "_kerja-g20")
s = s.replace("assets-v19", "assets-v20")
s = s.replace("parsed-g19", "parsed-g20")
s = s.replace("Proposal-SenseSIBI-v19.md", "Proposal-SenseSIBI-v20.md")
s = s.replace("parse_md_g19", "parse_md_g20")
s = s.replace("generate_docx_g19", "generate_docx_g20")
s = s.replace("Proposal-SenseSIBI-Studi-Kelayakan-v19", "Proposal-SenseSIBI-Studi-Kelayakan-v20")
s = s.replace('cek = "v19.docx" in s', 'cek = "v20.docx" in s')
s = s.replace('assert "parsed-g19.json" in s', 'assert "parsed-g20.json" in s')
s = s.replace('assert "assets-v19" in cek_p and "parsed-g19.json" in cek_p',
              'assert "assets-v20" in cek_p and "parsed-g20.json" in cek_p')
s = s.replace('print("JS g19 siap', 'print("JS g20 siap')
s = s.replace('naskah-untuk-docx.md:', 'naskah-g20-untuk-docx.md:')

# deskripsi dokumen
import re
lama_desc = re.search(r"description: 'Proposal[^']*'", s).group(0)
baru_desc = ("description: 'Proposal v20 disiplin penanda terbuka atas v19 (ledger 25 isu "
             "koreksi baseline kebenaran v17): tebakan belum diuji dikembalikan [PERLU DATA] "
             "(protokol audio PCM 16 kHz, regulator 500-800 mA, kapasitas baterai, pre-cache 26 "
             "klip menjadi opsi G3); pelengkapan verifikasi pinout Tabel 3.3 (strapping, USB, "
             "ADC1, konflik periferal, revisi papan), audit T0 (buffer, paket hilang, RSSI, fase), "
             "repetisi terpakai per kelas/sesi, penyelarasan keypoint, uji pilot pose dan J/Z, "
             "kerangka BOM tanpa angka tebakan; keputusan kondisional Pilihan 1 (Tabel 3.7 no. 19) "
             "dan MMS-TTS-ind (no. 17) tetap menunggu konfirmasi; skill sempro-mepet'")
s = s.replace(lama_desc, baru_desc, 1)
s = s.replace("# Bangun DOCX+PDF v19 (gelombang 18): revisi verifikasi sumber primer (ISS-01..ISS-30).",
              "# Bangun DOCX+PDF v20 (gelombang 20): disiplin penanda terbuka + pelengkapan audit T0,\n# pinout, repetisi, kerangka BOM; keputusan kondisional dijaga.")
s = s.replace("patch generate g19 gagal", "patch generate g20 gagal")

(scr / "build_docx_g20.sh").write_text(s, encoding="utf-8")
print("build_docx_g20.sh dibuat:", len(s), "karakter")
