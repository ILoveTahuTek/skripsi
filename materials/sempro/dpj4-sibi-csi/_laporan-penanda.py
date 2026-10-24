"""Buat laporan-penanda.md: semua [PERLU DATA: …] / [PERLU RUJUKAN: …] yang masih tersisa di naskah.

Pemakaian (dari folder ini):  python _laporan-penanda.py
Jalankan ulang setiap kali ada penanda yang diisi; laporan selalu mencerminkan isi berkas saat itu.
"""
import re, pathlib, datetime

D = pathlib.Path(__file__).parent
FILES = ["bab1-pendahuluan.md", "bab2-kajian-pustaka.md", "bab3-metodologi.md", "daftar-pustaka.md"]
MARK = re.compile(r"\[PERLU (DATA|RUJUKAN): ([^\]]+)\]")
ODD = re.compile(r"\[(?:PERLU(?! (?:DATA|RUJUKAN):)[^\]]*|@[^\]]+)\]")  # penanda tak baku atau kunci sitasi tersisa

# (kategori, kata kunci) — dicocokkan berurutan, huruf kecil
RULES = [
    ("Pembimbing (ambang & kebijakan)", ["pembimbing", "ambang g", "batas latensi", "batas kesesuaian", "lembaga atau komisi", "token apresiasi"]),
    ("Peneliti (perangkat & platform)", ["esp32 yang dipakai", "spesifikasi laptop", "adr", "laju pencuplikan", "laju sampling", "jarak antarnode",
                                         "tanggal akses", "commit", "bulan dan tahun", "biometrik"]),
    ("Mitra, validator, lapangan", ["mitra", "isyarat sibi terpilih", "pengisyarat dan lokasi", "kriteria kompetensi", "rekrutmen", "sesi perekaman",
                                    "setiap ruang", "kamus sibi", "kandidat isyarat", "proporsi kosakata"]),
    ("Data literatur & kondisi lapangan", ["signfi", "bahasa isyarat yang dikenali", "sibi atau bisindo", "sesuai rujukan", "orientasi pembelajaran",
                                           "penelusuran literatur", "di indonesia", "aplikasi atau video", "kursus", "kebutuhan belajar"]),
]
PRIORITAS = ["laju pencuplikan", "laju sampling", "nama sekolah", "isyarat sibi terpilih", "ambang g2", "ambang g3", "lembaga atau komisi", "varian esp32"]


def kategori(jenis, teks):
    if jenis == "RUJUKAN":
        return "Pustaka (rujukan yang perlu dicari)"
    t = teks.lower()
    for nama, kunci in RULES:
        if any(k in t for k in kunci):
            return nama
    return "Keputusan rancangan (peneliti + pembimbing)"


items, aneh = [], []
for f in FILES:
    p = D / f
    if not p.exists():
        continue
    sub = "—"
    for no, baris in enumerate(p.read_text(encoding="utf-8").splitlines(), 1):
        if baris.startswith("#"):
            sub = baris.lstrip("# ").strip()
        lokasi = sub + (" (tabel)" if baris.lstrip().startswith("|") else "")
        for jenis, teks in MARK.findall(baris):
            items.append(dict(berkas=f, baris=no, lokasi=lokasi, jenis=jenis, teks=teks.strip(),
                              kat=kategori(jenis, teks), prio=any(k in teks.lower() for k in PRIORITAS)))
        for m in ODD.findall(baris):
            aneh.append(f"`{f}:{no}` — `{m}`")

total = sum((D / f).read_text(encoding="utf-8").count("[PERLU") for f in FILES if (D / f).exists())
assert len(items) + sum("[PERLU" in a for a in aneh) == total, "ada penanda [PERLU …] yang terpotong baris; satukan dalam satu baris"

unik = {}
for it in items:
    k = (it["jenis"], it["teks"])
    unik.setdefault(k, {**it, "tempat": []})["tempat"].append(f"{it['berkas'].split('-')[0].replace('daftar','DP').upper()}:{it['baris']}")

out = [
    "# Laporan Penanda yang Masih Placeholder",
    "",
    f"Dibuat otomatis oleh `_laporan-penanda.py` pada {datetime.date.today():%d-%m-%Y}. Jalankan ulang setelah mengisi penanda.",
    "",
    f"**Total:** {len(items)} kemunculan, {len(unik)} penanda unik "
    f"({sum(1 for k in unik if k[0] == 'DATA')} PERLU DATA, {sum(1 for k in unik if k[0] == 'RUJUKAN')} PERLU RUJUKAN).",
    "",
    "## Ringkasan per berkas",
    "",
    "| Berkas | PERLU DATA | PERLU RUJUKAN |",
    "|---|---|---|",
]
for f in FILES:
    d = sum(1 for i in items if i["berkas"] == f and i["jenis"] == "DATA")
    r = sum(1 for i in items if i["berkas"] == f and i["jenis"] == "RUJUKAN")
    out.append(f"| `{f}` | {d} | {r} |")

prio = [u for u in unik.values() if u["prio"]]
if prio:
    out += ["", "## Prioritas (menentukan kelayakan rancangan)", ""]
    out += [f"- [ ] {u['teks']} — {', '.join(u['tempat'])}" for u in prio]

urutan = ["Pembimbing (ambang & kebijakan)", "Peneliti (perangkat & platform)", "Mitra, validator, lapangan",
          "Keputusan rancangan (peneliti + pembimbing)", "Data literatur & kondisi lapangan", "Pustaka (rujukan yang perlu dicari)"]
for kat in urutan:
    grup = [u for u in unik.values() if u["kat"] == kat]
    if not grup:
        continue
    out += ["", f"## {kat} ({len(grup)})", "", "| Status | Penanda | Jenis | Lokasi (berkas:baris) | Subbab pertama |", "|---|---|---|---|---|"]
    for u in grup:
        out.append(f"| ☐ | {u['teks']} | {u['jenis']} | {', '.join(u['tempat'])} | {u['lokasi']} |")

out += ["", "## Pemeriksaan format", ""]
out += aneh if aneh else ["Tidak ada penanda tak baku atau kunci sitasi `[@…]` yang tertinggal."]
out += ["", "Kode lokasi: BAB1/BAB2/BAB3 = berkas bab, DP = daftar pustaka. Nomor baris mengacu ke berkas bernomor (bukan `_berkunci/`)."]

(D / "laporan-penanda.md").write_text("\n".join(out) + "\n", encoding="utf-8")
print(f"laporan-penanda.md: {len(items)} kemunculan, {len(unik)} unik, {len(aneh)} format tak baku")
