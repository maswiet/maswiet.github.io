"""
Aktivitas 1 — Turunan fungsi delta = sepasang gaya (couple)
Seismologi Kuantitatif, Bab 3 (Aki & Richards, 2002)

Tujuan:
  1. Melihat bahwa fungsi Gauss yang makin sempit mendekati fungsi delta.
  2. Melihat bahwa turunan fungsi delta berbentuk dua "paku" berlawanan arah
     yang berdempetan, seperti dipol listrik atau sepasang gaya (couple).
  3. Membuktikan secara numerik bahwa "momen" turunan delta selalu -1,
     berapa pun lebar Gauss-nya. Momen inilah yang kelak menjadi M0.

Cara menjalankan:
  python3 aktivitas1_turunan_delta.py
"""

import numpy as np
import matplotlib.pyplot as plt

# ---------------------------------------------------------------
# 1. Fungsi Gauss ternormalisasi (luasnya = 1) sebagai pendekatan delta
# ---------------------------------------------------------------
def gauss(x, sigma):
    """Pendekatan fungsi delta: Gauss dengan luas 1 dan lebar sigma."""
    return np.exp(-x**2 / (2 * sigma**2)) / (sigma * np.sqrt(2 * np.pi))


def turunan_gauss(x, sigma):
    """Turunan analitik Gauss terhadap x: pendekatan d(delta)/dx."""
    return -x / sigma**2 * gauss(x, sigma)


x = np.linspace(-1, 1, 4001)
dx = x[1] - x[0]
daftar_sigma = [0.20, 0.10, 0.05]   # makin kecil = makin mirip delta

# ---------------------------------------------------------------
# 2. Cek numerik: luas delta = 1 dan momen turunannya = -1
#    Luas   : integral  delta(x) dx          = 1   (satu gaya satuan)
#    Momen  : integral  x * d(delta)/dx dx   = -1  (lengan x gaya)
#    Hasil kedua tidak bergantung pada sigma: sepasang gaya yang makin
#    rapat tetapi makin kuat mempertahankan momen yang sama.
# ---------------------------------------------------------------
print("=" * 60)
print(f"{'sigma':>8} | {'luas Gauss':>12} | {'total gaya':>12} | {'momen':>10}")
print("-" * 60)
for s in daftar_sigma:
    luas = np.sum(gauss(x, s)) * dx
    total_gaya = np.sum(turunan_gauss(x, s)) * dx          # harus ~0
    momen = np.sum(x * turunan_gauss(x, s)) * dx           # harus ~ -1
    print(f"{s:8.2f} | {luas:12.4f} | {total_gaya:12.2e} | {momen:10.4f}")
print("=" * 60)
print("Kesimpulan: total gaya = 0, tetapi momennya tetap = -1.")
print("Turunan delta adalah sepasang gaya berlawanan: sebuah couple.\n")

# ---------------------------------------------------------------
# 3. Gambar
# ---------------------------------------------------------------
fig, ax = plt.subplots(1, 3, figsize=(15, 4.5))

# (a) Gauss makin sempit -> delta
for s in daftar_sigma:
    ax[0].plot(x, gauss(x, s), label=f"σ = {s}")
ax[0].set_title("(a) Gauss makin sempit → fungsi delta δ(x)")
ax[0].set_xlabel("x")
ax[0].legend()
ax[0].grid(alpha=0.3)

# (b) Turunannya -> dua paku berlawanan
for s in daftar_sigma:
    ax[1].plot(x, turunan_gauss(x, s), label=f"σ = {s}")
ax[1].axhline(0, color="k", lw=0.8)
ax[1].set_title("(b) Turunannya → dua 'paku' berlawanan, dδ/dx")
ax[1].set_xlabel("x")
ax[1].legend()
ax[1].grid(alpha=0.3)

# (c) Tafsiran fisis: beda hingga [δ(x+ε) - δ(x-ε)] / 2ε = dua gaya titik
eps = 0.15
ax[2].axhline(0, color="k", lw=0.8)
ax[2].annotate("", xy=(-eps, 1.0), xytext=(-eps, 0),
               arrowprops=dict(arrowstyle="-|>", color="tab:red", lw=2.5))
ax[2].annotate("", xy=(eps, -1.0), xytext=(eps, 0),
               arrowprops=dict(arrowstyle="-|>", color="tab:blue", lw=2.5))
ax[2].text(-eps, 1.08, "+F", ha="center", color="tab:red", fontsize=12)
ax[2].text(eps, -1.2, "−F", ha="center", color="tab:blue", fontsize=12)
ax[2].annotate("", xy=(eps, 0.25), xytext=(-eps, 0.25),
               arrowprops=dict(arrowstyle="<->", color="gray"))
ax[2].text(0, 0.32, "lengan 2ε", ha="center", color="gray")
ax[2].set_xlim(-0.6, 0.6)
ax[2].set_ylim(-1.5, 1.5)
ax[2].set_title("(c) Tafsiran fisis: sepasang gaya (couple)\n"
                "F × 2ε tetap, meskipun ε → 0")
ax[2].set_xlabel("x")
ax[2].set_yticks([])

plt.suptitle("Aktivitas 1: turunan fungsi delta = sepasang gaya", fontsize=13)
plt.tight_layout()
plt.savefig("aktivitas1_turunan_delta.png", dpi=150)
print("Gambar disimpan: aktivitas1_turunan_delta.png")
plt.show()

# ---------------------------------------------------------------
# Pertanyaan diskusi:
#  1. Mengapa total gaya (kolom ke-3) nol, tetapi momennya tidak?
#  2. Apa yang terjadi pada tinggi puncak (b) jika sigma diperkecil?
#     Mengapa momennya tetap -1?
#  3. Hubungkan dengan pers. (3.11): f1 = -mu [u1] d(delta)/d(eta3).
#     Ke arah mana gaya di atas sesar, dan ke arah mana di bawahnya?
# ---------------------------------------------------------------
