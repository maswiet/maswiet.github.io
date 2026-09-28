"""
Aktivitas 2 — Rotasi tensor momen: double couple = dipol P dan T
Seismologi Kuantitatif, Bab 3 (Aki & Richards, 2002), Soal 3.4

Tujuan:
  1. Membangun tensor momen dari normal bidang sesar dan arah slip,
     m_pq = mu (nu_p [u_q] + nu_q [u_p])            (pers. 3.22)
  2. Memutar tensor 45 derajat dan melihat bahwa double couple
     menjadi diag(M0, 0, -M0): sepasang dipol T (tarikan) dan P (tekanan).
  3. Menemukan sumbu P dan T lewat nilai eigen dan vektor eigen.
  4. Membuktikan bahwa bidang sesar dan bidang bantu memberi M yang sama.
  5. Melihat pola radiasi gelombang P (4 cuping) dari tensor M.

Cara menjalankan:
  python3 aktivitas2_rotasi_tensor.py
"""

import numpy as np
import matplotlib.pyplot as plt

np.set_printoptions(precision=3, suppress=True)

M0 = 1.0   # momen seismik (satuan bebas); coba ganti nilainya


def cetak(judul, M):
    print(f"\n{judul}")
    print(M)


# ---------------------------------------------------------------
# 1. Tensor momen dari normal (nu) dan arah slip (d)
# ---------------------------------------------------------------
def tensor_momen(nu, d, M0=1.0):
    """M_pq = M0 (nu_p d_q + nu_q d_p), nu dan d vektor satuan."""
    nu = np.asarray(nu, float) / np.linalg.norm(nu)
    d = np.asarray(d, float) / np.linalg.norm(d)
    return M0 * (np.outer(nu, d) + np.outer(d, nu))


# Sesar pada bidang xi3 = 0 (normal ke arah 3), slip ke arah 1 (Gbr. 3.2)
nu = [0, 0, 1]
slip = [1, 0, 0]
M = tensor_momen(nu, slip, M0)
cetak("Tensor momen sesar (normal = sumbu 3, slip = sumbu 1), pers. 3.25:", M)


# ---------------------------------------------------------------
# 2. Rotasi terhadap sumbu 2:  M' = R M R^T
# ---------------------------------------------------------------
def rotasi_sumbu2(theta_derajat):
    t = np.radians(theta_derajat)
    c, s = np.cos(t), np.sin(t)
    return np.array([[c, 0, s],
                     [0, 1, 0],
                     [-s, 0, c]])


R = rotasi_sumbu2(45)
M_rot = R @ M @ R.T
cetak("Setelah diputar 45° terhadap sumbu 2 (Soal 3.4):", M_rot)
print("→ Diagonal: satu dipol +M0 (tarikan) dan satu dipol -M0 (tekanan).")

# Bagaimana komponen berubah untuk setiap sudut?
sudut = np.linspace(0, 180, 361)
M11, M33, M13 = [], [], []
for th in sudut:
    Mr = rotasi_sumbu2(th) @ M @ rotasi_sumbu2(th).T
    M11.append(Mr[0, 0]); M33.append(Mr[2, 2]); M13.append(Mr[0, 2])


# ---------------------------------------------------------------
# 3. Sumbu P dan T dari nilai eigen
# ---------------------------------------------------------------
nilai, vektor = np.linalg.eigh(M)       # nilai eigen terurut naik
# Tanda vektor eigen bebas (v dan -v sama-sama benar); agar mudah dibaca,
# buat komponen pertama yang tidak nol bernilai positif.
for k in range(3):
    v = vektor[:, k]
    if v[np.argmax(np.abs(v) > 1e-9)] < 0:
        vektor[:, k] = -v
P = vektor[:, 0]    # nilai eigen terkecil (-M0) -> sumbu P (tekanan)
B = vektor[:, 1]    # nilai eigen nol         -> sumbu B (null)
T = vektor[:, 2]    # nilai eigen terbesar (+M0) -> sumbu T (tarikan)
print("\nNilai eigen:", nilai)
print("Sumbu T (tarikan):", T)
print("Sumbu P (tekanan):", P)
print("Sumbu B (null)   :", B)
sudut_PT = np.degrees(np.arccos(abs(P @ np.array(nu, float))))
print(f"Sudut antara sumbu P dan normal sesar: {sudut_PT:.1f}°")


# ---------------------------------------------------------------
# 4. Bidang sesar vs bidang bantu: tukar normal dan slip
# ---------------------------------------------------------------
M_bantu = tensor_momen(slip, nu, M0)
cetak("Tensor momen bidang bantu (normal = sumbu 1, slip = sumbu 3):", M_bantu)
print("Sama dengan M semula?", np.allclose(M, M_bantu))
print("→ Dari sumber titik, bidang sesar dan bidang bantu tidak bisa dibedakan.")


# ---------------------------------------------------------------
# 5. Contoh sumber lain (Bagian 8 bahan belajar)
# ---------------------------------------------------------------
lam, mu = 1.0, 1.0                       # benda Poisson: lambda = mu
M_tarik = np.diag([lam, lam, lam + 2 * mu])
M_ledak = (lam + 2 / 3 * mu) * np.eye(3)
cetak("Rekah tarik (λ = μ, [u3]A = 1), rasio 1 : 1 : 3:", M_tarik)
cetak("Ledakan isotropik (ΔV = 1):", M_ledak)
for nama, Mx in [("double couple", M), ("rekah tarik", M_tarik), ("ledakan", M_ledak)]:
    print(f"  trace M ({nama:13s}) = {np.trace(Mx):.3f}"
          "   (trace ≠ 0 berarti ada perubahan volume)")


# ---------------------------------------------------------------
# 6. Gambar
# ---------------------------------------------------------------
fig = plt.figure(figsize=(15, 4.8))

# (a) Komponen M terhadap sudut rotasi
ax1 = fig.add_subplot(1, 3, 1)
ax1.plot(sudut, M13, label="M₁₃ (couple)")
ax1.plot(sudut, M11, label="M₁₁ (dipol)")
ax1.plot(sudut, M33, label="M₃₃ (dipol)")
ax1.axvline(45, color="gray", ls="--")
ax1.text(49, 0.08, "45°: M₁₃ = 0,\nhanya dipol", fontsize=9)
ax1.set_xlabel("sudut rotasi terhadap sumbu 2 (°)")
ax1.set_ylabel("komponen / M0")
ax1.set_title("(a) Komponen tensor saat sumbu diputar")
ax1.legend(fontsize=9, loc="upper center", bbox_to_anchor=(0.5, -0.18), ncol=3)
ax1.grid(alpha=0.3)


def gambar_gaya(ax, pasangan, judul):
    """pasangan: daftar (titik_pangkal, vektor_gaya, warna) di bidang 1-3."""
    ax.axhline(0, color="k", ls="--", lw=1)          # bidang sesar
    for (x0, z0), (fx, fz), warna in pasangan:
        ax.annotate("", xy=(x0 + fx, z0 + fz), xytext=(x0, z0),
                    arrowprops=dict(arrowstyle="-|>", color=warna, lw=2.5))
    ax.set_xlim(-1.6, 1.6); ax.set_ylim(-1.6, 1.6)
    ax.set_aspect("equal")
    ax.set_xlabel("sumbu 1"); ax.set_ylabel("sumbu 3")
    ax.set_title(judul)


# (b) Sistem gaya: double couple dan dipol P-T yang setara
ax2 = fig.add_subplot(1, 3, 2)
a, L = 0.25, 0.9
dc = [((-L / 2, a), (L, 0), "tab:blue"), ((L / 2, -a), (-L, 0), "tab:blue"),
      ((a, -L / 2), (0, L), "tab:orange"), ((-a, L / 2), (0, -L), "tab:orange")]
gambar_gaya(ax2, dc, "(b) Double couple (biru + oranye)\n"
                     "dan sumbu T, P setara (garis tipis)")
r = 1.4
t_dir = T[[0, 2]] / np.linalg.norm(T[[0, 2]])
p_dir = P[[0, 2]] / np.linalg.norm(P[[0, 2]])
for arah, label, warna in [(t_dir, "T", "tab:green"), (p_dir, "P", "tab:red")]:
    ax2.plot([-r * arah[0], r * arah[0]], [-r * arah[1], r * arah[1]],
             color=warna, lw=1, ls=":")
    ax2.text(1.12 * r * arah[0], 1.12 * r * arah[1], label,
             color=warna, fontsize=13, ha="center", va="center")

# (c) Pola radiasi P di bidang 1-3: A(phi) = gamma . M . gamma
ax3 = fig.add_subplot(1, 3, 3, projection="polar")
phi = np.linspace(0, 2 * np.pi, 721)
gamma = np.stack([np.cos(phi), np.zeros_like(phi), np.sin(phi)])  # arah pengamat
A = np.einsum("ik,ij,jk->k", gamma, M, gamma)                      # = M0 sin(2 phi)
ax3.fill_between(phi, 0, np.where(A > 0, A, 0), color="tab:green", alpha=0.5,
                 label="kompresi (+, gerak awal menjauh)")
ax3.fill_between(phi, 0, np.where(A < 0, -A, 0), color="tab:red", alpha=0.5,
                 label="dilatasi (−, gerak awal mendekat)")
ax3.set_title("(c) Pola radiasi P di bidang 1–3\n"
              "sudut dari sumbu 1 ke sumbu 3", fontsize=10)
ax3.set_yticks([])
ax3.legend(loc="lower center", bbox_to_anchor=(0.5, -0.32), fontsize=8)

plt.suptitle("Aktivitas 2: rotasi tensor momen, double couple = dipol T dan P",
             fontsize=13)
plt.tight_layout()
plt.savefig("aktivitas2_rotasi_tensor.png", dpi=150)
print("\nGambar disimpan: aktivitas2_rotasi_tensor.png")
plt.show()

# ---------------------------------------------------------------
# Pertanyaan diskusi:
#  1. Pada sudut berapa lagi M13 bernilai nol? Apa artinya?
#  2. Di (c), di arah mana amplitudo P nol? Bandingkan dengan arah
#     bidang sesar dan bidang bantu. Mengapa keduanya disebut bidang nodal?
#  3. Ubah slip = [1, 0, 1] (sesar miring). Apakah M masih double couple?
#     Petunjuk: periksa nilai eigennya. Mengapa hasilnya aneh?
#     (slip harus sejajar bidang sesar!)
#  4. Ganti M dengan M_tarik atau M_ledak di bagian (c). Bagaimana
#     pola radiasinya berubah?
# ---------------------------------------------------------------
