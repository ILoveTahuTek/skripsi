"""Pemeriksa invarian: bandingkan teks hasil sunting dengan sumber.

Pakai:  python cek.py <sumber> <hasil>
Invarian (dilaporkan per bagian bila dilanggar):
  heading, blok mermaid, baris tabel, caption gambar, penanda [PERLU ...],
  multiset sitasi [n] per subbab, multiset angka per subbab, Daftar Pustaka verbatim.
Baris judul (baris 1) dan sel "Judul" tabel identitas dikecualikan karena judul sengaja diganti.
"""
import re, sys
from collections import Counter

def bagian(t):
    """Pecah per heading ## atau # (kunci = teks heading)."""
    out, kunci, buf = {}, "_awal", []
    for ln in t.splitlines():
        if re.match(r"^#{1,3} ", ln):
            out.setdefault(kunci, []).extend(buf); buf = []; kunci = ln.strip()
        else:
            buf.append(ln)
    out.setdefault(kunci, []).extend(buf)
    return {k: "\n".join(v) for k, v in out.items()}

def strip_judul(t):
    ls = t.splitlines()
    ls = [l for i, l in enumerate(ls) if i != 0 and not l.startswith("| Judul |")]
    return "\n".join(ls)

def cek(src, dst):
    a, b = strip_judul(src), strip_judul(dst)
    err = []
    h = lambda t: [l.strip() for l in t.splitlines() if re.match(r"^#{1,3} ", l)]
    if h(a) != h(b): err.append(f"heading berubah: {set(h(a)) ^ set(h(b))}")
    mm = lambda t: re.findall(r"```mermaid.*?```", t, re.S)
    if mm(a) != mm(b): err.append(f"blok mermaid berubah ({len(mm(a))} vs {len(mm(b))})")
    tb = lambda t: [l.rstrip() for l in t.splitlines() if l.startswith("|")]
    if tb(a) != tb(b):
        d = [x for x in tb(a) if x not in tb(b)][:3]
        err.append(f"baris tabel berubah, mis.: {d}")
    cap = lambda t: [l.strip() for l in t.splitlines() if re.match(r"^(Gambar|Tabel) \d\.\d+", l)]
    if cap(a) != cap(b): err.append(f"caption berubah: {[x for x in cap(a) if x not in cap(b)][:3]}")
    pk = lambda t: re.findall(r"\[PERLU [A-Z]+: [^\]]*\]", t)
    if pk(a) != pk(b): err.append(f"penanda berubah: hilang {[x for x in pk(a) if x not in pk(b)]}, baru {[x for x in pk(b) if x not in pk(a)]}")
    dp = lambda t: t[t.find("# DAFTAR PUSTAKA"):] if "# DAFTAR PUSTAKA" in t else ""
    if dp(a) != dp(b): err.append("Daftar Pustaka berubah")
    ba, bb = bagian(a), bagian(b)
    for k in ba:
        if k not in bb: continue
        sa, sb = Counter(re.findall(r"\[\d+\]", ba[k])), Counter(re.findall(r"\[\d+\]", bb[k]))
        if sa != sb: err.append(f"{k}: sitasi berubah, hilang {dict(sa - sb)}, baru {dict(sb - sa)}")
        num = lambda t: Counter(re.findall(r"\d+(?:[.,]\d+)*", re.sub(r"\[\d+\]", "", t)))
        na, nb = num(ba[k]), num(bb[k])
        if na != nb: err.append(f"{k}: angka berubah, hilang {dict(na - nb)}, baru {dict(nb - na)}")
    return err

if __name__ == "__main__":
    src = open(sys.argv[1], encoding="utf-8").read()
    dst = open(sys.argv[2], encoding="utf-8").read()
    e = cek(src, dst)
    print("LOLOS" if not e else "GAGAL\n- " + "\n- ".join(e))
    sys.exit(1 if e else 0)
