#!/usr/bin/env python3
"""Gambar 2.1 (v15, revisi 2): ilustrasi 3D zona Fresnel pertama pada tautan baku 1 meter.

Revisi: sumbu dimatikan (ilustrasi skematis; skala dibawa label "jarak baku 1 m",
"r1 = 18 cm", "setinggi dada"), label node dijauhkan dari elipsoid.
Fisika: r1 = sqrt(lam * d1 * d2 / (d1 + d2)) = sqrt(0,125*0,5*0,5) = 0,1768 m.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

plt.rcParams["font.sans-serif"] = ["DejaVu Sans"]
plt.rcParams["axes.unicode_minus"] = False

OUT = "/home/z/my-project/download/sensesibi-v10/assets-v15/gambar-2.1.png"

D = 1.0            # jarak baku antarmodul (m)
H = 1.2            # tinggi dada (m)
LAM = 0.125        # panjang gelombang 2,4 GHz (m)
R1 = np.sqrt(LAM * (D / 2) * (D / 2) / D)  # 0,1768 m
MID = (D / 2, 0.0, H)

fig = plt.figure(figsize=(8.2, 5.8), dpi=240, constrained_layout=True)
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

# ---- modul (kuboid kecil di atas tiang) ----
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

# ---- pengisyarat skematis (di belakang sumbu tautan) ----
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

# ---- anotasi (tanpa sumbu; skala dibawa label) ----
F = 15
def leader(x, y, z, tx_, ty_, tz_, text, ha="left"):
    ax.plot([x, tx_], [y, ty_], [z, tz_], color="#4b5563", lw=0.8, ls=":")
    ax.text(tx_, ty_, tz_, text, fontsize=F, ha=ha, va="center", color="#111827")

leader(0.0, 0.0, H + 0.02, -0.34, -0.18, H + 0.34, "Node TX\n(ESP32-S3)")
leader(D, 0.0, H + 0.02, 1.36, -0.18, H + 0.34, "Node RX\n(ESP32-S3)", ha="right")
leader(0.5, 0.03, H + 0.045, 0.78, 0.30, H + 0.40, "tangan pengisyarat")
leader(0.5, R1 * 0.7, H + 0.02, -0.16, 0.34, H + 0.48,
       "zona Fresnel pertama\n(radius $r_1$)")
ax.text(0.5, -0.175, H + 0.055, "jarak baku 1 m", fontsize=F, ha="center", color="#111827")
ax.text(0.255, -0.085, H + 0.04, "$d_1$", fontsize=F, ha="center", color="#111827")
ax.text(0.745, -0.085, H + 0.04, "$d_2$", fontsize=F, ha="center", color="#111827")
ax.text(0.60, -0.075, H - 0.085, "$r_1 \\approx 18$ cm", fontsize=14, ha="left", color="#111827")
ax.text(0.0, 0.0, 0.62, "setinggi dada\n$\\pm$1,2 m", fontsize=13.5, ha="center", color="#4b5563")

# ---- bingkai dan tampilan (tanpa sumbu) ----
ax.set_xlim(-0.5, 1.5)
ax.set_ylim(-0.72, 0.78)
ax.set_zlim(-0.05, 1.78)
ax.set_box_aspect((1.5, 1.1, 1.15))
ax.set_axis_off()
ax.view_init(elev=16, azim=-62)
ax.set_proj_type("ortho")

fig.savefig(OUT, facecolor="white")
print("OK", OUT)
