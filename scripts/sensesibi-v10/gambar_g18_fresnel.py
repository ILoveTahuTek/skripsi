#!/usr/bin/env python3
"""Gambar 2.1 (v18): ilustrasi 3D zona Fresnel pertama — perbaikan ISS-27.

Perubahan dari v15/v16: seluruh anotasi diberi kotak latar putih (bbox) agar
tidak bertumpuk dengan elipsoid/siluet; label node TX/RX di tepi kiri-atas dan
kanan-atas; label zona Fresnel dan tangan pengisyarat dipisah sisi; penanda
jarak antarmodul di bawah garis pandang.
Fisika: r1 = sqrt(lam * d1 * d2 / (d1 + d2)) = sqrt(0,125*0,5*0,5) = 0,1768 m.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

plt.rcParams["font.sans-serif"] = ["DejaVu Sans"]
plt.rcParams["axes.unicode_minus"] = False

OUT = "/home/z/my-project/download/sensesibi-v10/assets-v18/gambar-2.1.png"

D = 1.0            # jarak baku antarmodul (m)
H = 1.2            # tinggi dada (m)
LAM = 0.125        # panjang gelombang 2,4 GHz (m)
R1 = np.sqrt(LAM * (D / 2) * (D / 2) / D)  # 0,1768 m
MID = (D / 2, 0.0, H)

fig = plt.figure(figsize=(8.6, 6.0), dpi=240, constrained_layout=True)
ax = fig.add_subplot(111, projection="3d")

# ---- lantai ----
gx, gy = np.meshgrid(np.linspace(-0.32, 1.32, 6), np.linspace(-0.62, 0.68, 6))
ax.plot_surface(gx, gy, np.zeros_like(gx), color="#d9dde3", alpha=0.35, linewidth=0)
ax.plot_wireframe(gx, gy, np.zeros_like(gx), color="#b9bfc9", alpha=0.4, lw=0.35)

# ---- elipsoid zona Fresnel pertama ----
u = np.linspace(0, 2 * np.pi, 72)
v = np.linspace(0, np.pi, 48)
U, V = np.meshgrid(u, v)
EX = MID[0] + (D / 2) * np.sin(V) * np.cos(U)
EY = MID[1] + R1 * np.sin(V) * np.sin(U)
EZ = MID[2] + R1 * np.cos(V)
ax.plot_surface(EX, EY, EZ, color="#2b7a9e", alpha=0.13, linewidth=0)
ax.plot_wireframe(EX, EY, EZ, color="#2b7a9e", alpha=0.5, lw=0.45,
                  rstride=10, cstride=18)

# ---- garis pandang TX-RX ----
ax.plot([0, D], [0, 0], [H, H], color="#333333", lw=1.1, ls=(0, (5, 3)))

# ---- modul ----
def cuboid(cx, cy, cz, dx, dy, dz, color, alpha=1.0):
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
    ax.add_collection3d(Poly3DCollection(pts, facecolors=color, edgecolors="#1c2733",
                                         linewidths=0.7, alpha=alpha))

ax.plot([0, 0], [0, 0], [0, H - 0.025], color="#7b8794", lw=2.2, solid_capstyle="round")
ax.plot([D, D], [0, 0], [0, H - 0.025], color="#7b8794", lw=2.2, solid_capstyle="round")
cuboid(0.0, 0.0, H + 0.006, 0.085, 0.038, 0.016, "#0e7490")   # node TX
cuboid(D, 0.0, H + 0.006, 0.085, 0.038, 0.016, "#1e3a8a")     # node RX

# ---- pengisyarat skematis ----
PXY = 0.34
bodyc = "#6b7280"
ax.plot([0.5 - 0.045, 0.5 - 0.045], [PXY, PXY], [0, 0.55], color=bodyc, lw=5.5, solid_capstyle="round")
ax.plot([0.5 + 0.045, 0.5 + 0.045], [PXY, PXY], [0, 0.55], color=bodyc, lw=5.5, solid_capstyle="round")
ax.plot([0.5, 0.5], [PXY, PXY], [0.52, 1.04], color=bodyc, lw=13, solid_capstyle="round")
uh, vh = np.meshgrid(np.linspace(0, 2 * np.pi, 28), np.linspace(0, np.pi, 18))
ax.plot_surface(0.5 + 0.075 * np.sin(vh) * np.cos(uh),
                PXY + 0.075 * np.sin(vh) * np.sin(uh),
                1.15 + 0.082 * np.cos(vh), color=bodyc, alpha=0.95, linewidth=0)
ax.plot([0.5, 0.5, 0.5], [PXY - 0.06, 0.16, 0.03], [0.99, 1.06, H],
        color=bodyc, lw=4.2, solid_capstyle="round")
ut, vt = np.meshgrid(np.linspace(0, 2 * np.pi, 22), np.linspace(0, np.pi, 14))
ax.plot_surface(0.5 + 0.042 * np.sin(vt) * np.cos(ut),
                0.02 + 0.042 * np.sin(vt) * np.sin(ut),
                H + 0.045 * np.cos(vt), color="#374151", alpha=1.0, linewidth=0)

# ---- garis ukur radius r1 di titik tengah ----
ax.plot([0.5, 0.5], [-R1, R1], [H, H], color="#111827", lw=1.3)
ax.plot([0.5, 0.5], [-R1, -R1], [H - 0.012, H + 0.012], color="#111827", lw=1.3)
ax.plot([0.5, 0.5], [R1, R1], [H - 0.012, H + 0.012], color="#111827", lw=1.3)

# ---- anotasi: proyeksikan jangkar ke koordinat figur, gambar di lapisan 2D ----
from mpl_toolkits.mplot3d import proj3d
import matplotlib.lines as mlines

F = 14.5
fig.canvas.draw()  # pastikan transform final

def proyeksi_frac(x, y, z):
    x2, y2, _ = proj3d.proj_transform(x, y, z, ax.get_proj())
    dx, dy = ax.transData.transform((x2, y2))
    return fig.transFigure.inverted().transform((dx, dy))

def label_2d(fx, fy, text, jangkar, ha="left", va="center", color="#111827", fs=F):
    tx, ty = fig.transFigure.inverted().transform(
        fig.transFigure.transform((fx, fy)))
    ax_frac = proyeksi_frac(*jangkar)
    fig.lines.append(mlines.Line2D([ax_frac[0], fx], [ax_frac[1], fy],
                     transform=fig.transFigure, color="#4b5563", lw=0.9,
                     ls=":", zorder=5))
    fig.text(fx, fy, text, fontsize=fs, ha=ha, va=va, color=color,
             bbox=dict(facecolor="white", alpha=0.9, edgecolor="none", pad=2.5),
             zorder=10)

H2 = 1.2
label_2d(0.015, 0.925, "Node TX\n(ESP32-S3)", (0.0, 0.0, H2 + 0.02), ha="left")
label_2d(0.985, 0.925, "Node RX\n(ESP32-S3)", (1.0, 0.0, H2 + 0.02), ha="right")
label_2d(0.015, 0.565, "zona Fresnel pertama\n(radius $r_1$ \≈ 18 cm)", (0.5, -0.1768 * 0.75, H2 - 0.10), ha="left")
label_2d(0.960, 0.60, "tangan\npengisyarat", (0.5, 0.03, H2 + 0.06), ha="right")
label_2d(0.5, 0.035, "jarak antarmodul d = 1 m", (0.5, 0.0, 0.0), ha="center")

# ---- bingkai dan tampilan ----
ax.set_xlim(-0.35, 1.35)
ax.set_ylim(-0.75, 0.85)
ax.set_zlim(-0.10, 1.95)
ax.set_box_aspect((1.35, 1.15, 1.45))
ax.set_axis_off()
ax.view_init(elev=16, azim=-62)
ax.set_proj_type("ortho")

fig.savefig(OUT, facecolor="white")
print("OK", OUT)
