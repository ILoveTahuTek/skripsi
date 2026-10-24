#!/usr/bin/env python3
"""Evaluator rubric untuk skill proposal-writing dan dokumen DPJ.

Mode:
  --skill <dir>        Nilai kandidat skill (SKILL.md + references/ terasembel)
  --doc <path>         Nilai dokumen DPJ hasil generate (teks polos)

Output: skor float 0..1 + JSON feedback (aturan gagal + saran). Deterministik.
Sumber rubrik: 05-analisis-korpus/rubric.json (D1-D6, berbobot).
"""
import argparse, json, os, re, sys

RUBRIC_WEIGHTS = {"D1": 0.20, "D2": 0.20, "D3": 0.15, "D4": 0.15, "D5": 0.15, "D6": 0.15}

REF_FILES = [
    "references/00-output-language.md", "references/01-scope.md",
    "references/02-structure.md", "references/03-language-patterns.md",
    "references/04-citations.md", "references/05-format-mechanics.md",
    "references/06-ejaan-naskah-id.md", "references/07-claim-discipline.md",
    "references/08-gepa-loop.md", "references/09-workflow.md",
]

def read(p):
    try:
        with open(p, encoding="utf-8") as f:
            return f.read()
    except OSError:
        return ""

def parse_frontmatter(text):
    if not text.startswith("---"):
        return None
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.S)
    return m.group(1) if m else None

def cover_ratio(text, terms):
    if not terms:
        return 1.0, []
    norm = re.sub(r"\s+", " ", text)  # istilah tidak boleh gagal hanya karena line-wrap
    # istilah dipakai sebagai regex apa adanya (alternasi '|' diperbolehkan);
    # semua term di file ini memang dirancang sebagai pola, bukan string polos
    hit = [t for t in terms if re.search(t, norm, re.I)]
    miss = [t for t in terms if t not in hit]
    return len(hit) / len(terms), miss

# ---- dimensi: term wajib per dimensi (assembled = body + semua referensi) ----
DIM_TERMS = {
    "D1": ["Latar Belakang", "Rumusan Masalah", "Tujuan Penelitian", "Batasan Masalah",
           "Manfaat Penelitian", "Penelitian Terdahulu", "DAFTAR PUSTAKA", "Metode",
           "jadwal", "Manfaat Teoretis", "Bagi Peneliti", "konsisten"],
    "D2": ["Bagaimana", "bertujuan untuk", "ruang lingkup yang jelas", "tidak membahas",
           "Berdasarkan uraian tersebut", "Manfaat Praktis", "Berdasarkan latar belakang",
           "merancang", "Tahap pertama"],
    "D3": ["APA", "hanging indent", "doi", "menjelaskan", "menunjukkan", "Crossref", "verifikasi"],
    "D4": ["memengaruhi", "koma", "Gambar", "Tabel", "kapital", "Paragraf"],
    "D5": ["studi kelayakan", "stub", "Delta-CSI", "go/no-go", "risiko", "mitigasi",
           "PCK@20", "klasifikasi gestur"],
    "D6": ["alternatif", "semester", "biaya", "sampul", "placeholder", "Rupiah"],
}

def score_skill(skill_dir):
    """Nilai kandidat skill: format + proses + pointer + cakupan rubrik.

    Cakupan tiap dimensi = 0.6*rasio_di_BODY(SKILL.md) + 0.4*rasio_assembled
    (SKILL.md + referensi) — vocab inti harus hidup di lapisan routing, bukan
    hanya tersembunyi di referensi.
    """
    body = read(os.path.join(skill_dir, "SKILL.md"))
    refs = {r: read(os.path.join(skill_dir, r)) for r in REF_FILES}
    assembled = body + "\n" + "\n".join(refs.values())
    failed, coverage = [], {}

    # --- format gate ---
    fm = parse_frontmatter(body)
    if fm is None:
        failed.append({"check": "frontmatter", "suggestion": "SKILL.md harus diawali blok frontmatter '---' lengkap."})
    else:
        if not re.search(r"^name:\s*proposal-writing", fm, re.M):
            failed.append({"check": "frontmatter name", "suggestion": "name: proposal-writing wajib ada dan tepat."})
        desc = re.search(r"description:\s*(.+(?:\n\s+.+)*)", fm)
        dtext = desc.group(1) if desc else ""
        if len(dtext) < 200:
            failed.append({"check": "description panjang", "suggestion": "description harus >200 char agar memicu routing yang andal."})
        triggers = ["proposal", "pengajuan judul", "DPJ", "tugas akhir", "skripsi"]
        n_trig = sum(1 for t in triggers if t.lower() in dtext.lower())
        if n_trig < 3:
            failed.append({"check": "trigger description", "suggestion": f"description hanya memuat {n_trig}/5 trigger (proposal, pengajuan judul, DPJ, tugas akhir, skripsi). Tambahkan trigger yang kurang."})

    # --- steps + completion criteria ---
    steps = re.findall(r"^### (.+)$", body, re.M)
    n_steps = len([s for s in steps if not s.startswith("Penggunaan")])
    if n_steps < 5:
        failed.append({"check": "jumlah langkah", "suggestion": f"Proses hanya {n_steps} langkah; minimal 5 langkah berurutan."})
    n_done = len(re.findall(r"Selesai bila|Done when", body))
    if n_done < max(4, n_steps - 1):
        failed.append({"check": "kriteria selesai", "suggestion": f"Hanya {n_done} langkah punya 'Selesai bila'/'Done when'; tiap langkah proses wajib punya kriteria selesai eksplisit."})

    # --- pointers ke referensi ---
    for r in REF_FILES + ["scripts/evaluator.py"]:
        base = os.path.basename(r)
        if base not in body:
            failed.append({"check": f"pointer {base}", "suggestion": f"SKILL.md harus menunjuk {r} dengan namanya (context pointer)."})
        if not refs.get(r if r in refs else "", "").strip() and base != "evaluator.py":
            failed.append({"check": f"file {base}", "suggestion": f"File referensi {r} hilang/kosong."})

    # --- cakupan dimensi (body 60% + assembled 40%) ---
    for dim, terms in DIM_TERMS.items():
        a_ratio, _ = cover_ratio(assembled, terms)
        b_ratio, b_miss = cover_ratio(body, terms)
        ratio = 0.6 * b_ratio + 0.4 * a_ratio
        coverage[dim] = round(ratio, 3)
        if ratio < 0.999:
            failed.append({"check": f"cakupan {dim} (body {b_ratio:.2f}/assembled {a_ratio:.2f})",
                           "suggestion": f"Vocab inti belum ada di SKILL.md: {', '.join(b_miss)} — masukkan ringkas di langkah terkait (detail boleh tetap di referensi)."})

    # --- traceability + mekanika skill ---
    if not re.search(r"korpus", assembled, re.I) or not re.search(r"TRSE|Universitas Negeri Malang", assembled):
        failed.append({"check": "traceability korpus", "suggestion": "Sebutkan sumber pola (korpus TRSE Universitas Negeri Malang) untuk traceability."})
    n_body = body.count("\n")
    if n_body > 160:
        failed.append({"check": "panjang SKILL.md", "suggestion": f"Body {n_body} baris > 160 — geser detail ke references (progressive disclosure)."})
    if "memengaruhi" not in assembled:
        failed.append({"check": "ejaan PUEBI", "suggestion": "Referensi bahasa wajib memuat aturan 'memengaruhi' (bukan mempengaruhi)."})

    wsum = sum(RUBRIC_WEIGHTS[d] * coverage[d] for d in RUBRIC_WEIGHTS)
    hard_fails = [f for f in failed if not f["check"].startswith("cakupan")]
    gate = max(0.70, 1.0 - 0.06 * len(hard_fails)) if hard_fails else 1.0
    score = min(1.0, wsum * gate)
    return round(score, 4), {"score": round(score, 4), "coverage": coverage,
                             "steps": n_steps, "selesai_bila": n_done,
                             "failed": failed, "n_failed": len(failed)}

# ---------------- mode dokumen DPJ ----------------
# Format DPJ bernomor (1. Latar Belakang ... 10. Daftar Referensi) memakai
# alternasi agar setara dengan format BAB penuh (Pendahuluan/KAJIAN PUSTAKA dst).
DOC_TERMS = {
    "D1": ["Latar Belakang", "Rumusan Masalah", "Tujuan Penelitian", "Batasan Masalah",
           "Manfaat Penelitian", "Penelitian Terdahulu", "DAFTAR PUSTAKA|Daftar Referensi",
           "KAJIAN PUSTAKA|TINJAUAN PUSTAKA", "METODE PENELITIAN|METODOLOGI PENELITIAN"],
    "D2": ["Bagaimana", "bertujuan untuk", "tidak membahas",
           "Berdasarkan uraian tersebut", "Berdasarkan latar belakang"],
    "D3": ["doi.org", r"\(\d{4}\)", "et al|dkk"],
    "D4": ["memengaruhi|mempengaruhi"],
    "D5": ["studi kelayakan", "Delta-CSI|go/no-go"],
    "D6": ["Jadwal", "biaya|Biaya", "Alternatif|alternatif"],
}
DOC_FORBID = [r"saya\s+(akan|akan)", r"\bKami\b", r"mempengaruhi", r"End of Report", r"HALAMAN SAMPUL"]

def score_doc(path):
    text = read(path)
    failed, coverage = [], {}
    for dim, terms in DOC_TERMS.items():
        ratio, miss = cover_ratio(text, terms)
        coverage[dim] = round(ratio, 3)
        if ratio < 1.0:
            failed.append({"check": f"D{dim[1]}: istilah hilang", "suggestion": ", ".join(miss)})
    for pat in DOC_FORBID:
        if re.search(pat, text):
            failed.append({"check": f"pola terlarang: {pat}", "suggestion": "hapus/ganti sesuai rubrik D4."})
    wsum = sum(RUBRIC_WEIGHTS[d] * min(coverage[d], 1.0) for d in RUBRIC_WEIGHTS)
    pen = 0.05 * len([f for f in failed if "terlarang" in f["check"]])
    score = max(0.0, wsum - pen)
    return round(score, 4), {"score": round(score, 4), "coverage": coverage, "failed": failed}

def main():
    ap = argparse.ArgumentParser()
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--skill", help="direktori kandidat skill")
    g.add_argument("--doc", help="path teks dokumen DPJ")
    ap.add_argument("--json-out", help="simpan hasil ke file JSON")
    a = ap.parse_args()
    if a.skill:
        score, info = score_skill(a.skill)
    else:
        score, info = score_doc(a.doc)
    out = json.dumps(info, ensure_ascii=False, indent=1)
    print(out)
    if a.json_out:
        with open(a.json_out, "w", encoding="utf-8") as f:
            f.write(out)
    sys.exit(0 if score >= 0.8 else 1)

if __name__ == "__main__":
    main()
