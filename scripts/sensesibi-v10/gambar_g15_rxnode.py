#!/usr/bin/env python3
"""Gambar 3.4 (v15, revisi 2): skema 3D node penerima — tata letak "exploded stack".

Revisi dari versi 1 (label kanan bertumpuk): komponen disebar vertikal sebagai
tumpukan berurai dengan ruang label lega di kiri dan kanan; sumbu dimatikan.
Komponen mengikuti Tabel 3.1 dan Tabel 3.3. Skema isometrik; tidak berskala.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

plt.rcParams["font.sans-serif"] = ["DejaVu Sans"]
plt.rcParams["axes.unicode_minus"] = False

OUT = "/home/z/my-project/download/sensesibi-v10/assets-v15/gambar-3.4.png"

fig = plt.figure(figsize=(8.6, 6.6), dpi=230, constrained_layout=True)
ax = fig.add_subplot(111, projection="3d")

# ---------- util ----------
def cuboid(cx, cy, cz, dx, dy, dz, color, alpha=1.0, ec="#1f2937", lw=0.8):
    x0, x1 = cx - dx / 2, cx + dx / 2
    y0, y1 = cy - dy / 2, cy + dy / 2
    z0, z1 = cz - dz / 2, cz + dz / 2
    pts = [
        [(x0, y0, z0), (x1, y0, z0), (x1, y1, z0), (x0, y1, z0)],
        [(x0, y0, z1), (x1, y0, z1), (x1, y1, z1), (x0, y1, z1)],
        [(x0, y0, z0), (x1, y0, z0), (x1, y0, z1), (x0, y0, z1)],
        [(x0, y1, z0), (x1, y1, z0), (x1, y1, z1), (x0, y1, z1)],
        [(x0, y0, z0), (x0, y1, z0), (x0, y1, z1), (x0, y0, z1)],
        [(x1, y0, z0), (x1, y1, z0), (x1, y1, z1), (x1, y0, z1)],
    ]
    ax.add_collection3d(Poly3DCollection(pts, facecolors=color, edgecolors=ec,
                                         linewidths=lw, alpha=alpha))
    return (cx, cy, cz)

def cyl_x(cx, cy, cz, r, h, color, alpha=1.0):
    """Silinder sumbu-x (menonjol ke +x), dengan tutup ujung."""
    u = np.linspace(0, 2 * np.pi, 40)
    X = np.linspace(cx, cx + h, 8)
    U, XX = np.meshgrid(u, X)
    ax.plot_surface(XX, cy + r * np.cos(U), cz + r * np.sin(U),
                    color=color, alpha=alpha, linewidth=0)
    v = np.linspace(0, np.pi, 24)
    w = np.linspace(0, r, 12)
    V, W = np.meshgrid(v, w)
    ax.plot_surface(np.full_like(V, cx + h), cy + W * np.cos(V),
                    cz + W * np.sin(V), color=color, alpha=alpha, linewidth=0)

def disc_z(cx, cy, cz, r, h, color, alpha=1.0):
    """Silinder sumbu-z (piringan horizontal)."""
    u = np.linspace(0, 2 * np.pi, 40)
    Z = np.linspace(cz, cz + h, 6)
    U, ZZ = np.meshgrid(u, Z)
    ax.plot_surface(cx + r * np.cos(U), cy + r * np.sin(U), ZZ,
                    color=color, alpha=alpha, linewidth=0)

# ---------- tumpukan berurai (z makin tinggi makin atas) ----------
L, W = 11.0, 7.0            # dimensi enclosure (cm, skematis)
# 1) enclosure dasar (bawah) dengan dinding tembus pandang
cuboid(0, 0, 0.0, L, W, 0.35, "#e5e7eb", alpha=0.95, ec="#9aa2ad")
cuboid(0, -W / 2 + 0.15, 1.1, L, 0.3, 1.9, "#d3d7de", alpha=0.30, ec="#9aa2ad", lw=0.5)
cuboid(-L / 2 + 0.15, 0, 1.1, 0.3, W, 1.9, "#d3d7de", alpha=0.30, ec="#9aa2ad", lw=0.5)
cuboid(L / 2 - 0.15, 0, 1.1, 0.3, W, 1.9, "#d3d7de", alpha=0.30, ec="#9aa2ad", lw=0.5)
enc = (0, -W / 2, 1.0)
# port USB-C pada dinding kiri
usb = cuboid(-L / 2 - 0.25, 0, 1.1, 0.55, 1.2, 0.4, "#374151", ec="#111827")

# 2) baterai (lapis kedua, terurai ke atas-kiri)
batt = cuboid(-1.3, 0, 3.6, 8.6, 5.4, 1.0, "#3b6ea5", ec="#274c77")

# 3) modul ESP32-S3 (lapis ketiga, terurai lebih tinggi)
board = cuboid(1.6, 0, 6.2, 7.4, 2.7, 0.38, "#2f7d4f", ec="#1e5631")
cuboid(3.4, 0, 6.2, 1.7, 1.7, 0.44, "#c6c9ce", ec="#6b7280")    # pelindung logam
cuboid(-1.6, 0, 6.2, 0.85, 1.5, 0.46, "#111827", ec="#111827")  # area antena PCB

# 4) layar (paling atas, panel menghadap depan-atas)
scr = cuboid(1.0, 1.15, 8.8, 5.0, 0.3, 3.0, "#111827", ec="#000000")

# 5) antarmuka muka depan (menempel dinding depan enclosure)
disc_z(-2.9, W / 2 + 0.55, 1.25, 1.15, 0.6, "#4b5563")          # speaker
cuboid(2.9, W / 2 + 0.2, 1.3, 0.7, 0.5, 0.7, "#111827", ec="#000000")  # mikrofon

# 6) rotary encoder + tombol pada dinding kanan
cyl_x(L / 2 - 0.1, -0.6, 1.35, 0.68, 1.25, "#6b7280")
cyl_x(L / 2 - 0.1, -0.6, 1.35, 0.32, 1.65, "#9aa2ad")
cuboid(L / 2 + 0.1, 1.9, 1.9, 0.55, 0.95, 0.6, "#dc2626", ec="#7f1d1d")

# ---------- label (kiri dan kanan, z berjenjang agar tak bertumpuk) ----------
F = 14.5
def lab(p, tpos, text, ha="left"):
    ax.plot([p[0], tpos[0]], [p[1], tpos[1]], [p[2], tpos[2]],
            color="#4b5563", lw=0.85, ls=":")
    ax.text(tpos[0], tpos[1], tpos[2], text, fontsize=F, ha=ha, va="center",
            color="#111827")

# kolom kiri (atas ke bawah)
lab(scr, (-10.6, 6.4, 9.6), "Layar\n(OLED/TFT)", ha="right")
lab(board, (-11.2, -5.2, 6.9), "Modul ESP32-S3\n(Wi-Fi 2,4 GHz,\nantena PCB)", ha="right")
lab(batt, (-11.0, -6.0, 2.6), "Baterai Li-Po +\nBMS 1S + TP4056", ha="right")
lab(usb, (-11.6, 0.6, 0.2), "Port USB-C", ha="right")
# kolom kanan (atas ke bawah)
lab((L / 2, -0.6, 1.35), (11.6, 1.4, 4.6), "Rotary encoder\nEC11 + tombol")
lab((L / 2, 1.9, 1.9), (11.6, 3.6, 7.4), "Tombol tekan-\nuntuk-bicara")
lab((-2.9, W / 2, 1.3), (9.6, 7.6, 2.2), "Pengeras suara\n+ DAC MAX98357A")
lab((2.9, W / 2, 1.3), (10.6, 6.4, -0.8), "Mikrofon\nINMP441")
lab(enc, (-6.0, -5.8, -1.6), "Enclosure cetak 3D (PLA/ABS)", ha="right")

# ---------- bingkai dan tampilan ----------
ax.set_xlim(-13.5, 13.5)
ax.set_ylim(-9.5, 10.0)
ax.set_zlim(-3.0, 11.0)
ax.set_box_aspect((2.5, 1.55, 1.05))
ax.set_axis_off()
ax.view_init(elev=17, azim=-58)
ax.set_proj_type("ortho")

fig.savefig(OUT, facecolor="white")
print("OK", OUT)
