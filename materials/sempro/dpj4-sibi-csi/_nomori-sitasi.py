"""Ganti kunci [@kunci] di bab1-3 menjadi nomor IEEE berurut kemunculan pertama, lalu tulis daftar-pustaka.md."""
import re, sys, pathlib

D = pathlib.Path(sys.argv[1])
if D.resolve().name == "_berkunci":
    sys.exit("Jangan jalankan di _berkunci/: salin dulu ketiga bab ke folder lain.")
FILES = ["bab1-pendahuluan.md", "bab2-kajian-pustaka.md", "bab3-metodologi.md"]

REF = {
 "rodriguez2023": 'P. A. Rodríguez-Correa, A. Valencia-Arias, O. N. Patiño-Toro, Y. Oblitas Díaz, and R. Teodori De la Puente, "Benefits and development of assistive technologies for Deaf people\'s communication: A systematic review," *Frontiers in Education*, vol. 8, Art. no. 1121597, 2023, doi: 10.3389/feduc.2023.1121597.',
 "sanjaya2023": 'S. A. Sanjaya and H. F. Ilone, "BISINDO sign language recognition: A systematic literature review of deep learning techniques for image processing," *Indonesian Journal of Computer Science*, vol. 12, no. 6, 2023, doi: 10.33022/ijcs.v12i6.3539.',
 "dwijayanti2021": 'S. Dwijayanti, Hermawati, S. I. Taqiyyah, H. Hikmarika, and B. Y. Suprapto, "Indonesia sign language recognition using convolutional neural network," *International Journal of Advanced Computer Science and Applications*, vol. 12, no. 10, 2021, doi: 10.14569/IJACSA.2021.0121046.',
 "ma2019survey": 'Y. Ma, G. Zhou, and S. Wang, "WiFi sensing with channel state information: A survey," *ACM Computing Surveys*, vol. 52, no. 3, pp. 1–36, 2019, doi: 10.1145/3310194.',
 "hernandez2020": 'S. M. Hernandez and E. Bulut, "Lightweight and standalone IoT based WiFi sensing for active repositioning and mobility," in *Proc. 2020 IEEE 21st Int. Symp. "A World of Wireless, Mobile and Multimedia Networks" (WoWMoM)*, 2020, pp. 277–286, doi: 10.1109/WoWMoM49955.2020.00056.',
 "signfi2018": 'Y. Ma, G. Zhou, S. Wang, H. Zhao, and W. Jung, "SignFi: Sign language recognition using WiFi," *Proceedings of the ACM on Interactive, Mobile, Wearable and Ubiquitous Technologies*, vol. 2, no. 1, pp. 1–21, 2018, doi: 10.1145/3191755.',
 "baldeo2024": 'J. M. E. G. Baldeo, J. A. P. Canlas, K. D. C. Clata, D. C. C. Flores, J. J. D. Surot, and J. M. R. Reyes, "Filipino sign language recognition using Wi-Fi channel state information," in *Proc. TENCON 2024 – 2024 IEEE Region 10 Conf.*, 2024, pp. 1026–1029, doi: 10.1109/TENCON61640.2024.10903008.',
 "shang2017": 'J. Shang and J. Wu, "A robust sign language recognition system with multiple Wi-Fi devices," in *Proc. Workshop on Mobility in the Evolving Internet Architecture (MobiArch)*, 2017, pp. 19–24, doi: 10.1145/3097620.3097624.',
 "ahmed2020": 'H. F. Thariq Ahmed, H. Ahmad, K. Narasingamurthi, H. Harkat, and S. K. Phang, "DF-WiSLR: Device-free Wi-Fi-based sign language recognition," *Pervasive and Mobile Computing*, vol. 69, Art. no. 101289, 2020, doi: 10.1016/j.pmcj.2020.101289.',
 "ahmed2021": 'H. F. Thariq Ahmed, H. Ahmad, S. K. Phang, H. Harkat, and K. Narasingamurthi, "Wi-Fi CSI based human sign language recognition using LSTM network," in *Proc. 2021 IEEE Int. Conf. Industry 4.0, Artificial Intelligence, and Communications Technology (IAICT)*, 2021, pp. 51–57, doi: 10.1109/IAICT52856.2021.9532548.',
 "widar2021": 'Y. Zhang, Y. Zheng, K. Qian, G. Zhang, Y. Liu, C. Wu, and Z. Yang, "Widar3.0: Zero-effort cross-domain gesture recognition with Wi-Fi," *IEEE Transactions on Pattern Analysis and Machine Intelligence*, vol. 44, no. 11, pp. 8671–8685, 2022, doi: 10.1109/TPAMI.2021.3105387.',
 "chen2023": 'C. Chen, G. Zhou, and Y. Lin, "Cross-domain WiFi sensing with channel state information: A survey," *ACM Computing Surveys*, vol. 55, no. 11, pp. 1–37, 2023, doi: 10.1145/3570325.',
 "hao2020": 'Z. Hao, Y. Duan, X. Dang, Y. Liu, and D. Zhang, "Wi-SL: Contactless fine-grained gesture recognition uses channel state information," *Sensors*, vol. 20, no. 14, Art. no. 4025, 2020, doi: 10.3390/s20144025.',
 "sruthi2024": 'P. Sruthi, S. Satapathy, and S. K. Udgata, "HandFi: WiFi sensing based hand gesture recognition using channel state information," *Procedia Computer Science*, vol. 235, pp. 426–435, 2024, doi: 10.1016/j.procs.2024.04.042.',
 "cai2024": 'Z. Cai, Z. Li, Z. Chen, H. Zhuo, L. Zheng, X. Wu, and Y. Liu, "Device-free wireless sensing for gesture recognition based on complementary CSI amplitude and phase," *Sensors*, vol. 24, no. 11, Art. no. 3414, 2024, doi: 10.3390/s24113414.',
 "qin2023": 'Y. Qin, S. Pan, W. Zhou, D. Pan, and Z. Li, "WiASL: American Sign Language writing recognition system using commercial WiFi devices," *Measurement*, vol. 218, Art. no. 113125, 2023, doi: 10.1016/j.measurement.2023.113125.',
 "kindy2025": 'G. O. Kindy, G. Leonali, and H. Lucky, "Word-level BISINDO: A novel video Indonesian sign language dataset and baseline methods," *Procedia Computer Science*, vol. 269, pp. 249–258, 2025, doi: 10.1016/j.procs.2025.08.277.',
 "wiguna2025": 'K. L. Wiguna and Rojali, "Sentence-level Indonesian sign language (BISINDO) recognition using 3D CNN-LSTM and 3D CNN-BiLSTM models," *International Journal of Advanced Computer Science and Applications*, vol. 16, no. 9, 2025, doi: 10.14569/IJACSA.2025.0160941.',
 "sebastian2025": 'C. Sebastian, J. Limanza, L. Laurentia, J. Harefa, and K. Jingga, "Indonesian sign language (BISINDO) recognition using spatially aware body gesture recognition," *Procedia Computer Science*, vol. 269, pp. 1002–1011, 2025, doi: 10.1016/j.procs.2025.09.042.',
 "personinwifi2019": 'F. Wang, S. Zhou, S. Panev, J. Han, and D. Huang, "Person-in-WiFi: Fine-grained person perception using WiFi," in *Proc. IEEE/CVF Int. Conf. Computer Vision (ICCV)*, 2019, pp. 5451–5460, doi: 10.1109/ICCV.2019.00555.',
 "densepose2023": 'J. Geng, D. Huang, and F. De la Torre, "DensePose from WiFi," arXiv:2301.00250, 2023, doi: 10.48550/arXiv.2301.00250.',
 "mediapipe2019": 'C. Lugaresi *et al.*, "MediaPipe: A framework for building perception pipelines," arXiv:1906.08172, 2019, doi: 10.48550/arXiv.1906.08172.',
 "blazepose2020": 'V. Bazarevsky, I. Grishchenko, K. Raveendran, T. Zhu, F. Zhang, and M. Grundmann, "BlazePose: On-device real-time body pose tracking," arXiv:2006.10204, 2020, doi: 10.48550/arXiv.2006.10204.',
 "mphands2020": 'F. Zhang *et al.*, "MediaPipe Hands: On-device real-time hand tracking," arXiv:2006.10214, 2020, doi: 10.48550/arXiv.2006.10214.',
 "kim2023": 'J.-W. Kim, J.-Y. Choi, E.-J. Ha, and J.-H. Choi, "Human pose estimation using MediaPipe Pose and optimization method based on a humanoid model," *Applied Sciences*, vol. 13, no. 4, Art. no. 2700, 2023, doi: 10.3390/app13042700.',
 "chadha2021": 'S. Chadha, K. Kamenov, and A. Cieza, "The world report on hearing, 2021," *Bulletin of the World Health Organization*, vol. 99, no. 4, pp. 242–242A, 2021, doi: 10.2471/BLT.21.285643.',
 "mitchell2004": 'R. E. Mitchell and M. A. Karchmer, "Chasing the mythical ten percent: Parental hearing status of deaf and hard of hearing students in the United States," *Sign Language Studies*, vol. 4, no. 2, pp. 138–163, 2004, doi: 10.1353/sls.2004.0005.',
 "mitchell2005": 'R. E. Mitchell and M. A. Karchmer, "Parental hearing status and signing among deaf and hard of hearing students," *Sign Language Studies*, vol. 5, no. 2, pp. 231–244, 2005, doi: 10.1353/sls.2005.0004.',
 "lieberman2022": 'A. M. Lieberman, J. Mitchiner, and E. Pontecorvo, "Hearing parents learning American Sign Language with their deaf children: A mixed-methods survey," *Applied Linguistics Review*, vol. 15, no. 1, pp. 309–333, 2022, doi: 10.1515/applirev-2021-0120.',
 "ritmeester2025": 'J. Ritmeester, B. Sümer, M. Boonstra, M. de Meulder, B. van der Aa, and F. Roelofsen, "Navigating sign language learning: Insights from hearing parents of deaf and hard-of-hearing children," *Journal of Deaf Studies and Deaf Education*, vol. 31, no. 1, pp. 85–103, 2025, doi: 10.1093/jdsade/enaf059.',
 "ruview": 'ruvnet, "RuView," GitHub repository. [Online]. Available: https://github.com/ruvnet/RuView [PERLU DATA: tanggal akses dan versi/commit yang dipakai]',
 "brin2026": 'Badan Riset dan Inovasi Nasional, "BRIN dorong penguatan ekosistem bahasa isyarat, BISINDO dominan digunakan penyandang tuli," 26 Agu. 2026. [Online]. Available: https://brin.go.id/news/130095 [PERLU DATA: tanggal akses]',
 "kemenkopmk2025": 'Kementerian Koordinator Bidang Pembangunan Manusia dan Kebudayaan, "Kemenko PMK bergerak bersama wujudkan selaras bahasa isyarat," 3 Okt. 2025. [Online]. Available: [PERLU RUJUKAN: URL lengkap rilis di kemenkopmk.go.id dan tanggal akses]',
 "uu8_2016": 'Republik Indonesia, *Undang-Undang Nomor 8 Tahun 2016 tentang Penyandang Disabilitas*. Jakarta, Indonesia, 2016.',
 "kamussibi": '[PERLU RUJUKAN: data terbitan resmi Kamus Sistem Isyarat Bahasa Indonesia (penerbit, tahun, edisi)]',
}

KEY = re.compile(r"\[@([A-Za-z0-9_]+)\]")
order, texts = [], {}
for f in FILES:
    t = (D / f).read_text(encoding="utf-8")
    if re.search(r"\[\d+\]", t):  # sudah bernomor: lanjut berarti daftar pustaka tertimpa kosong atau nomor bertabrakan
        sys.exit(f"{f} sudah bernomor; pakai salinan dari _berkunci/.")
    texts[f] = t
    for k in KEY.findall(t):
        if k not in order:
            order.append(k)
unknown = [k for k in order if k not in REF]
if unknown:
    sys.exit(f"Kunci tidak dikenal: {unknown}")
num = {k: i + 1 for i, k in enumerate(order)}

def merge(m):
    # gabungkan rangkaian kunci berurutan "[@a], [@b]" → "[1], [2]" (IEEE tetap per nomor)
    return f"[{num[m.group(1)]}]"

for f, t in texts.items():
    (D / f).write_text(KEY.sub(merge, t), encoding="utf-8")

lines = ["# DAFTAR PUSTAKA", ""]
lines += [f"[{num[k]}] {REF[k]}" + "\n" for k in order]
(D / "daftar-pustaka.md").write_text("\n".join(lines), encoding="utf-8")
print(f"{len(order)} rujukan dipakai; tidak dipakai: {sorted(set(REF) - set(order))}")

# padatkan rangkaian nomor berurutan (≥3) menjadi rentang IEEE, mis. [3], [4], [5] → [3]–[5]
RUN = re.compile(r"\[(\d+)\](?:, \[\d+\])+")
def comp(m):
    ns = [int(x) for x in re.findall(r"\d+", m.group(0))]
    out, i = [], 0
    while i < len(ns):
        j = i
        while j + 1 < len(ns) and ns[j + 1] == ns[j] + 1:
            j += 1
        out.append(f"[{ns[i]}]–[{ns[j]}]" if j - i >= 2 else ", ".join(f"[{n}]" for n in ns[i:j + 1]))
        i = j + 1
    return ", ".join(out)
for f in FILES:
    p = D / f
    p.write_text(RUN.sub(comp, p.read_text(encoding="utf-8")), encoding="utf-8")
    assert "[@" not in p.read_text(encoding="utf-8"), f"kunci tersisa di {f} (salah ketik, mis. spasi di dalam kurung)"
