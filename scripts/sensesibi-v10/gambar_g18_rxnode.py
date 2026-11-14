#!/usr/bin/env python3
"""Gambar 3.4 (v18): skema 3D node penerima — perbaikan ISS-27.

Perubahan dari v15/v16: seluruh anotasi diberi kotak latar putih dan digeser
lebih keluar (kolom kiri/kanan lebih lebar) sehingga label tidak bertumpuk
dengan dinding enclosure abu-abu maupun satu sama lain; garis penunjuk (callout)
dipertahankan. Skema isometrik konseptual; tidak berskala.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

plt.rcParams["font.sans-serif"] = ["DejaVu Sans"]
plt.rcParams["axes.unicode_minus"] = False

OUT = "/home/z/my-project/download/sensesibi-v10/assets-v18/gambar-3.4.png"

fig = plt.figure(figsize=(9.2, 6.9), dpi=230, constrained_layout=True)
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
    u = np.linspace(0, 2 * np.pi, 40)
    Z = np.linspace(cz, cz + h, 6)
    U, ZZ = np.meshgrid(u, Z)
    ax.plot_surface(cx + r * np.cos(U), cy + r * np.sin(U), ZZ,
                    color=color, alpha=alpha, linewidth=0)

# ---------- tumpukan berurai ----------
L, W = 11.0, 7.0            # dimensi enclosure (cm, skematis)
cuboid(0, 0, 0.0, L, W, 0.35, "#e5e7eb", alpha=0.95, ec="#9aa2ad")
cuboid(0, -W / 2 + 0.15, 1.1, L, 0.3, 1.9, "#d3d7de", alpha=0.30, ec="#9aa2ad", lw=0.5)
cuboid(-L / 2 + 0.15, 0, 1.1, 0.3, W, 1.9, "#d3d7de", alpha=0.30, ec="#9aa2ad", lw=0.5)
cuboid(L / 2 - 0.15, 0, 1.1, 0.3, W, 1.9, "#d3d7de", alpha=0.30, ec="#9aa2ad", lw=0.5)
enc = (0, -W / 2, 1.0)
usb = cuboid(-L / 2 - 0.25, 0, 1.1, 0.55, 1.2, 0.4, "#374151", ec="#111827")
batt = cuboid(-1.3, 0, 3.6, 8.6, 5.4, 1.0, "#3b6ea5", ec="#274c77")
board = cuboid(1.6, 0, 6.2, 7.4, 2.7, 0.38, "#2f7d4f", ec="#1e5631")
cuboid(3.4, 0, 6.2, 1.7, 1.7, 0.44, "#c6c9ce", ec="#6b7280")    # pelindung logam
cuboid(-1.6, 0, 6.2, 0.85, 1.5, 0.46, "#111827", ec="#111827")  # area antena PCB
scr = cuboid(1.0, 1.15, 8.8, 5.0, 0.3, 3.0, "#111827", ec="#000000")
disc_z(-2.9, W / 2 + 0.55, 1.25, 1.15, 0.6, "#4b5563")          # speaker
cuboid(2.9, W / 2 + 0.2, 1.3, 0.7, 0.5, 0.7, "#111827", ec="#000000")  # mikrofon
cyl_x(L / 2 - 0.1, -0.6, 1.35, 0.68, 1.25, "#6b7280")
cyl_x(L / 2 - 0.1, -0.6, 1.35, 0.32, 1.65, "#9aa2ad")
cuboid(L / 2 + 0.1, 1.9, 1.9, 0.55, 0.95, 0.6, "#dc2626", ec="#7f1d1d")

# ---------- label: callout + kotak putih, z berjenjang ----------
F = 14.5
BBOX = dict(facecolor="white", alpha=0.9, edgecolor="none", pad=2.5)

def lab(p, tpos, text, ha="left"):
    ax.plot([p[0], tpos[0]], [p[1], tpos[1]], [p[2], tpos[2]],
            color="#4b5563", lw=0.85, ls=":")
    ax.text(tpos[0], tpos[1], tpos[2], text, fontsize=F, ha=ha, va="center",
            color="#111827", bbox=BBOX, zorder=10)

# kolom kiri (atas ke bawah) — digeser lebih keluar
lab(scr, (-13.4, 7.4, 10.4), "Layar\n(OLED/TFT)", ha="right")
lab(board, (-13.8, -6.2, 7.6), "Modul ESP32-S3\n(Wi-Fi 2,4 GHz,\nantena PCB)", ha="right")
lab(batt, (-13.4, -7.0, 2.6), "Baterai Li-Po +\nBMS 1S + TP4056", ha="right")
lab(usb, (-14.2, 0.8, -0.4), "Port USB-C", ha="right")
# kolom kanan (atas ke bawah) — digeser lebih keluar
lab((L / 2, -0.6, 1.35), (14.0, -2.4, 5.2), "Rotary encoder\nEC11 + tombol")
lab((L / 2, 1.9, 1.9), (14.0, 1.0, 8.6), "Tombol tekan-\nuntuk-bicara")
lab((-2.9, W / 2, 1.3), (12.4, 9.6, 3.2), "Pengeras suara\n+ DAC MAX98357A")
lab((2.9, W / 2, 1.3), (13.2, 8.4, -1.2), "Mikrofon\nINMP441")
lab(enc, (-8.0, -7.4, -2.2), "Enclosure cetak 3D (PLA/ABS)", ha="right")

# ---------- bingkai dan tampilan ----------
ax.set_xlim(-16.0, 16.0)
ax.set_ylim(-11.0, 11.5)
ax.set_zlim(-3.6, 11.6)
ax.set_box_aspect((2.7, 1.85, 1.25))
ax.set_axis_off()
ax.view_init(elev=17, azim=-58)
ax.set_proj_type("ortho")

fig.savefig(OUT, facecolor="white")
print("OK", OUT)
