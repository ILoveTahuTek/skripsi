#!/usr/bin/env python3
"""Perbarui kamus REF pada _nomori-sitasi.py: isi 4 entri berpenanda + tambah 28 rujukan terverifikasi."""
import pathlib
import re
import sys

P = pathlib.Path("/home/z/my-project/materials/sempro/dpj4-sibi-csi/_nomori-sitasi.py")
src = P.read_text(encoding="utf-8")

FIX = [
    (
        ' "ruview": \'ruvnet, "RuView," GitHub repository. [Online]. Available: '
        'https://github.com/ruvnet/RuView [PERLU DATA: tanggal akses dan versi/commit yang dipakai]\',',
        ' "ruview": \'ruvnet, "RuView," GitHub repository. [Online]. Available: '
        'https://github.com/ruvnet/RuView, commit fefb0f9, diakses 24 Okt. 2026.\',',
    ),
    (
        ' "brin2026": \'Badan Riset dan Inovasi Nasional, "BRIN dorong penguatan ekosistem '
        'bahasa isyarat, BISINDO dominan digunakan penyandang tuli," 26 Agu. 2026. [Online]. '
        'Available: https://brin.go.id/news/130095 [PERLU DATA: tanggal akses]\',',
        ' "brin2026": \'Badan Riset dan Inovasi Nasional, "BRIN dorong penguatan ekosistem '
        'bahasa isyarat, BISINDO dominan digunakan penyandang tuli," 26 Agu. 2026. [Online]. '
        'Available: https://brin.go.id/news/130095, diakses 24 Okt. 2026.\',',
    ),
    (
        ' "kemenkopmk2025": \'Kementerian Koordinator Bidang Pembangunan Manusia dan Kebudayaan, '
        '"Kemenko PMK bergerak bersama wujudkan selaras bahasa isyarat," 3 Okt. 2025. [Online]. '
        'Available: [PERLU RUJUKAN: URL lengkap rilis di kemenkopmk.go.id dan tanggal akses]\',',
        ' "kemenkopmk2025": \'Kementerian Koordinator Bidang Pembangunan Manusia dan Kebudayaan, '
        '"Kemenko PMK bergerak bersama wujudkan selaras bahasa isyarat," 3 Okt. 2025. [Online]. '
        'Available: '
        'https://www.kemenkopmk.go.id/kemenko-pmk-bergerak-bersama-wujudkan-selaras-bahasa-isyarat, '
        'diakses 24 Okt. 2026.\',',
    ),
    (
        ' "kamussibi": \'[PERLU RUJUKAN: data terbitan resmi Kamus Sistem Isyarat Bahasa '
        'Indonesia (penerbit, tahun, edisi)]\',',
        ' "kamussibi": \'Departemen Pendidikan dan Kebudayaan, *Kamus Sistem Isyarat Bahasa '
        'Indonesia* (edisi pertama). Jakarta, Indonesia: Departemen Pendidikan dan Kebudayaan, '
        "1994.',",
    ),
]

# 28 rujukan baru (DOI terverifikasi Crossref, 24 Okt. 2026). Semua nilai berupa satu string
# berkutip tunggal; apostrof internal di-escape.
NEW = {
    "sigrist2013": 'R. Sigrist, G. Rauter, R. Riener, and P. Wolf, "Augmented visual, auditory, haptic, and multimodal feedback in motor learning: A review," *Psychonomic Bulletin & Review*, vol. 20, no. 1, pp. 21\u201353, 2013, doi: 10.3758/s13423-012-0333-8.',
    "intecom2024": 'B. I. Rodhiyah and S. Wulandari, "Aplikasi berbasis mobile sebagai sarana pembelajaran dasar bahasa isyarat," *INTECOMS: Journal of Information Technology and Computer Science*, vol. 7, no. 1, pp. 58\u201363, 2024, doi: 10.31539/intecoms.v7i1.8326.',
    "technomedia2022": 'R. Fatmawati, R. Asmara, Y. R. Prayogi, and R. Y. Hakkun, "Aplikasi pembelajaran sistem isyarat bahasa Indonesia (SIBI) berbasis voice menggunakan OpenSIBI," *Technomedia Journal*, vol. 7, no. 1, pp. 22\u201339, 2022, doi: 10.33050/tmj.v7i1.1690.',
    "zikky2019": 'M. Zikky and Z. F. Akbar, "Kamus sistem isyarat bahasa Indonesia (KASIBI) dengan voice recognition sebagai pendukung belajar bahasa isyarat berbasis Android," *Jurnal Sains Terapan*, vol. 5, no. 2, 2019, doi: 10.32487/jst.v5i2.732.',
    "dbesti2026": 'R. A. Maulana, A. R. Adriansyah, and Z. Imaduddin, "Integrasi model deep learning pada pengembangan aplikasi Android pendeteksi bahasa isyarat SIBI menggunakan Jetpack Compose," *DBESTI: Journal of Digital Business and Technology Innovation*, vol. 3, no. 1, pp. 78\u201385, 2026, doi: 10.54914/dbesti.v3i1.2081.',
    "audhi2024": 'S. As Satillah, K. Khotimah, N. N. Muslihah, R. Rahmayanti, W. Mirip, Y. D. Suryani, and L. D. A. Pagarwati, "Ragam bahasa anak tunarungu dengan SIBI di SLB N Ogan Ilir," *Jurnal Anak Usia Dini Holistik Integratif (AUDHI)*, vol. 7, no. 1, pp. 31\u201343, 2024, doi: 10.36722/jaudhi.v7i1.2876.',
    "kamussibidigital": 'Lembaga Penelitian dan Pengembangan Sistem Isyarat Bahasa Indonesia, "Kamus SIBI Digital," Direktorat Pendidikan Masyarakat dan Pendidikan Khusus, Kementerian Pendidikan dan Kebudayaan RI, 2020. [Online]. Available: https://pkplk.kemendikdasmen.go.id/sibi, diakses 24 Okt. 2026.',
    "ong2005": 'S. C. W. Ong and S. Ranganath, "Automatic sign language analysis: A survey and the future beyond lexical meaning," *IEEE Transactions on Pattern Analysis and Machine Intelligence*, vol. 27, no. 6, pp. 873\u2013891, 2005, doi: 10.1109/TPAMI.2005.112.',
    "mlmsign2024": 'A. Sadeghzadeh, A. F. M. Shahen Shah, and M. B. Islam, "MLMSign: Multi-lingual multi-modal illumination-invariant sign language recognition," *Intelligent Systems with Applications*, vol. 22, Art. no. 200384, 2024, doi: 10.1016/j.iswa.2024.200384.',
    "stokoe2005": 'W. C. Stokoe, "Sign language structure: An outline of the visual communication systems of the American deaf," *Journal of Deaf Studies and Deaf Education*, vol. 10, no. 1, pp. 3\u201337, 2005, doi: 10.1093/deafed/eni001 (cetak ulang monograf 1960).',
    "nugraheni2023": 'A. S. Nugraheni, A. P. Husain, and H. Unayah, "Optimalisasi penggunaan bahasa isyarat dengan SIBI dan BISINDO pada mahasiswa difabel tunarungu di Prodi PGMI UIN Sunan Kalijaga," *Jurnal Holistika*, vol. 5, no. 1, pp. 28\u201333, 2023, doi: 10.24853/holistika.5.1.28-33.',
    "malika2025": 'M. Malika and Berlianti, "Penggunaan bahasa isyarat SIBI dan BISINDO untuk siswa tuli di Sekolah Luar Biasa Negeri Pembina Medan," *Concept: Journal of Social Humanities and Education*, vol. 4, no. 3, pp. 78\u201387, 2025, doi: 10.55606/concept.v4i3.2178.',
    "hassan2026": 'S. Hassan, L. Nourian, C. de Lacerda Pataca, M. Olson, T. D\'aurio, K. Agarwal, S. M. N. Asad, G. W. Tigwell, and M. Huenerfauth, "ASL educators\' perspectives on AI for enhancing student learning in American Sign Language education," in *Proc. 2026 CHI Conf. Human Factors in Computing Systems (CHI)*, 2026, pp. 1\u201320, doi: 10.1145/3772318.3791928.',
    "sagawa2002": 'H. Sagawa and M. Takeuchi, "A teaching system of Japanese sign language using sign language recognition and generation methods," in *Proc. 10th ACM Int. Conf. Multimedia*, 2002, pp. 137\u2013145, doi: 10.1145/641007.641035.',
    "daniel2024": 'C. A. Daniel, N. M. Liam, Y. Habchi, and S. Basnet, "Enhancing language learning with real-time sign language recognition and feedback," in *Proc. 2024 IEEE MIT Undergraduate Research Technology Conf. (URTC)*, 2024, pp. 1\u20135, doi: 10.1109/URTC65039.2024.10937578.',
    "zajonc1965": 'R. B. Zajonc, "Social facilitation," *Science*, vol. 149, no. 3681, pp. 269\u2013274, 1965, doi: 10.1126/science.149.3681.269.',
    "bailenson2021": 'J. N. Bailenson, "Nonverbal overload: A theoretical argument for the causes of Zoom fatigue," *Technology, Mind, and Behavior*, vol. 2, no. 1, 2021, doi: 10.1037/tmb0000030.',
    "nyquist1928": 'H. Nyquist, "Certain topics in telegraph transmission theory," *Transactions of the American Institute of Electrical Engineers*, vol. 47, no. 2, pp. 617\u2013644, 1928, doi: 10.1109/T-AIEE.1928.5055024.',
    "shannon1949": 'C. E. Shannon, "Communication in the presence of noise," *Proceedings of the IRE*, vol. 37, no. 1, pp. 10\u201321, 1949, doi: 10.1109/JRPROC.1949.232969.',
    "zheng2023": 'C. Zheng *et al.*, "Deep learning-based human pose estimation: A survey," *ACM Computing Surveys*, vol. 56, no. 1, pp. 1\u201337, 2023, doi: 10.1145/3603618.',
    "cortes1995": 'C. Cortes and V. Vapnik, "Support-vector networks," *Machine Learning*, vol. 20, no. 3, pp. 273\u2013297, 1995, doi: 10.1007/BF00994018.',
    "kiranyaz2021": 'S. Kiranyaz, O. Avci, O. Abdeljaber, T. Ince, M. Gabbouj, and D. J. Inman, "1D convolutional neural networks and applications: A survey," *Mechanical Systems and Signal Processing*, vol. 151, Art. no. 107398, 2021, doi: 10.1016/j.ymssp.2020.107398.',
    "chow1970": 'C. K. Chow, "On optimum recognition error and reject tradeoff," *IEEE Transactions on Information Theory*, vol. 16, no. 1, pp. 41\u201346, 1970, doi: 10.1109/TIT.1970.1054406.',
    "bowen2009": 'D. J. Bowen, M. Kreuter, B. Spring, L. Cofta-Woerpel, L. Linnan, D. Weiner, S. Bakken, C. P. Kaplan, L. Squiers, C. Fabrizio, and M. Fernandez, "How we design feasibility studies," *American Journal of Preventive Medicine*, vol. 36, no. 5, pp. 452\u2013457, 2009, doi: 10.1016/j.amepre.2009.02.002.',
    "sokolova2009": 'M. Sokolova and G. Lapalme, "A systematic analysis of performance measures for classification tasks," *Information Processing & Management*, vol. 45, no. 4, pp. 427\u2013437, 2009, doi: 10.1016/j.ipm.2009.03.002.',
    "likert1932": 'R. Likert, "A technique for the measurement of attitudes," *Archives of Psychology*, no. 140, pp. 5\u201355, 1932.',
    "soekarta2024": 'R. Soekarta, S. Aras, R. Rezki, and N. K. D. P. Ainun, "Sistem deteksi simbol isyarat pada SIBI (Sistem Isyarat Bahasa Indonesia) menggunakan Mediapipe berbasis Android," *Insect (Informatics and Security): Jurnal Teknik Informatika*, vol. 10, no. 2, pp. 90\u2013100, 2024, doi: 10.33506/insect.v10i2.4079.',
    "mountrakis2011": 'G. Mountrakis, J. Im, and C. Ogole, "Support vector machines in remote sensing: A review," *ISPRS Journal of Photogrammetry and Remote Sensing*, vol. 66, no. 3, pp. 247\u2013259, 2011, doi: 10.1016/j.isprsjprs.2010.11.001.',
}


def main():
    global src
    for i, (old, new) in enumerate(FIX, 1):
        n = src.count(old)
        if n != 1:
            print(f"GAGAL perbaikan #{i}: kemunculan = {n}")
            sys.exit(1)
        src = src.replace(old, new)
    m = re.search(r"^REF = \{\n(.*?)^\}\n", src, re.S | re.M)
    if not m:
        print("Blok REF tidak ditemukan")
        sys.exit(1)
    blok = m.group(0)
    tambahan = "\n # --- rujukan baru (terverifikasi Crossref, 24 Okt. 2026) ---\n"
    tambahan += "\n".join(f' "{k}": {v!r},' for k, v in NEW.items())
    tambahan += "\n}\n"
    src = src.replace(blok, blok[:-2] + tambahan, 1)
    P.write_text(src, encoding="utf-8")
    # validasi: eksekusi definisi REF saja
    ns: dict = {}
    code = src.split("KEY = re.compile")[0]
    exec(compile(code, str(P), "exec"), ns)  # noqa: S102 - validasi internal
    ref = ns["REF"]
    print(f"[ok] REF kini {len(ref)} entri (sebelumnya 44).")
    print(f"    entri berpenanda tersisa: {[k for k, v in ref.items() if '[PERLU' in v]}")


if __name__ == "__main__":
    main()
