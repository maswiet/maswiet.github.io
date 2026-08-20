#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gempa Flores 2026 — waveform GE.MMRI (Maumere) dari GEOFON.
Diadaptasi dari Pak_Beck/New2/load.py (workflow Lombok 2018).

- Ambil waveform + response (StationXML) dari FDSN GEOFON
- Pilih set 3-komponen terbaik: HH > BH (velocity), HN > HL (accel)
- Hapus response -> VEL (m/s) & ACC (m/s^2)
- Plot 3C velocity + spektrogram vertikal, PGV & PGA teranotasi
- Simpan PNG untuk slide 7
"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import gridspec
from obspy import UTCDateTime
from obspy.clients.fdsn import Client
from obspy.geodetics import gps2dist_azimuth

# ---- event (USGS) ----
OT   = UTCDateTime("2026-08-14T21:58:21")   # 15 Agu 2026 05:58:21 WITA
EVLA, EVLO, EVDP, MAG = -8.310, 121.352, 10.0, 7.7
NET, STA = "GE", "MMRI"
STLA, STLO = -8.6357, 122.2376

T_PRE, T_POST = 60, 480
OUTDIR = "assets"
OUTPNG = os.path.join(OUTDIR, "waveform_mmri_flores2026.png")

# elegant-minimalist palette
C_TEXT="#1F1F1B"; C_MUT="#5F625C"; C_ACC="#8A2D1F"; C_SUP="#2F5D62"; C_PAPER="#FFFFFF"

os.makedirs(OUTDIR, exist_ok=True)
cli = Client(base_url="https://geofon.gfz.de", timeout=120)

t1, t2 = OT - T_PRE, OT + T_POST
print(f"Fetching {NET}.{STA} {t1} .. {t2}")
st = cli.get_waveforms(NET, STA, "*", "BH?,HH?,HN?,HL?", t1, t2, attach_response=False)
inv = cli.get_stations(network=NET, station=STA, location="*",
                       channel="BH?,HH?,HN?,HL?", starttime=t1, endtime=t2, level="response")
st.merge(method=1, fill_value="interpolate")
print("Channels returned:")
for tr in st:
    print(f"  {tr.id}  fs={tr.stats.sampling_rate:g}Hz  npts={tr.stats.npts}  max|a|={np.max(np.abs(tr.data)):.3g}")

dist_m, az, baz = gps2dist_azimuth(EVLA, EVLO, STLA, STLO)
dist_km = dist_m/1000.0
print(f"Δ = {dist_km:.1f} km, az = {az:.0f}°")

def pick3c(stream, prefixes):
    for p in prefixes:
        z = stream.select(channel=p+"Z"); n = stream.select(channel=p+"N"); e = stream.select(channel=p+"E")
        if len(z) and len(n) and len(e):
            return p, z[0].copy(), n[0].copy(), e[0].copy()
    return None, None, None, None

# ---- velocity (broadband) ----
vp, vz, vn, ve = pick3c(st, ["HH", "BH"])
# ---- acceleration (strong motion) ----
ap, az_, an, ae = pick3c(st, ["HN", "HL"])

def prep(tr, inv, output, pre_filt):
    tr = tr.copy()
    tr.detrend("linear"); tr.taper(0.05)
    tr.remove_response(inventory=inv, output=output, pre_filt=pre_filt, water_level=60)
    return tr

# process velocity -> cm/s
pf_v = [0.01, 0.02, 20, 25]
VZ = prep(vz, inv, "VEL", pf_v); VN = prep(vn, inv, "VEL", pf_v); VE = prep(ve, inv, "VEL", pf_v)
for tr in (VZ, VN, VE): tr.data *= 100.0  # m/s -> cm/s
pgv = max(np.max(np.abs(tr.data)) for tr in (VZ, VN, VE))
print(f"Velocity set = {vp}?, PGV = {pgv:.2f} cm/s")

# process acceleration -> g
pga_g = None; acc_label = None
if ap is not None:
    pf_a = [0.05, 0.1, 40, 45]
    AZ = prep(az_, inv, "ACC", pf_a); AN = prep(an, inv, "ACC", pf_a); AE = prep(ae, inv, "ACC", pf_a)
    pga = max(np.max(np.abs(tr.data)) for tr in (AZ, AN, AE))  # m/s^2
    pga_g = pga/9.81
    acc_label = ap
    print(f"Accel set = {ap}?, PGA = {pga:.3f} m/s^2 = {pga_g:.3f} g")
else:
    print("No accelerometer channel; PGA omitted.")

# ---- figure ----
t = VZ.times()  # seconds from window start
p_from_ot = T_PRE  # OT located at T_PRE seconds into window

fig = plt.figure(figsize=(10.5, 7.6), dpi=170)
fig.patch.set_facecolor(C_PAPER)
gs = gridspec.GridSpec(4, 1, height_ratios=[1, 1, 1, 1.25], hspace=0.32)

comps = [("Z (vertikal)", VZ), ("N (utara)", VN), ("E (timur)", VE)]
for k, (lab, tr) in enumerate(comps):
    ax = fig.add_subplot(gs[k])
    ax.plot(t, tr.data, color=C_TEXT, lw=0.5)
    ax.axvline(p_from_ot, color=C_ACC, lw=1.1, ls="--")
    pk = np.max(np.abs(tr.data))
    ax.set_ylabel(f"{lab}\ncm/s", fontsize=9, color=C_MUT)
    ax.text(0.995, 0.90, f"puncak {pk:.2f} cm/s", transform=ax.transAxes,
            ha="right", va="top", fontsize=8, color=C_MUT)
    ax.set_xlim(t[0], t[-1]); ax.grid(True, color="#E7E2D8", lw=0.6)
    ax.tick_params(labelsize=8, colors=C_MUT)
    if k == 0:
        ax.text(p_from_ot+3, 0.82*ax.get_ylim()[1], "waktu asal", color=C_ACC, fontsize=8)
    ax.set_xticklabels([])
    for s in ax.spines.values(): s.set_color("#D8D2C5")

# spectrogram of vertical
axs = fig.add_subplot(gs[3])
axs.specgram(VZ.data, Fs=VZ.stats.sampling_rate, NFFT=256, noverlap=200, cmap="magma")
axs.axvline(p_from_ot, color="#FFFFFF", lw=1.0, ls="--", alpha=0.8)
axs.set_ylim(0, min(20, VZ.stats.sampling_rate/2))
axs.set_ylabel("Frekuensi\nHz", fontsize=9, color=C_MUT)
axs.set_xlabel("Waktu sejak awal jendela (detik)", fontsize=9, color=C_MUT)
axs.tick_params(labelsize=8, colors=C_MUT)
for s in axs.spines.values(): s.set_color("#D8D2C5")

# title + annotations
sub = f"Δ ≈ {dist_km:.0f} km dari episenter   ·   sensor {vp} (kecepatan)"
if pga_g is not None:
    sub += f"   ·   PGA ≈ {pga_g:.2f} g ({acc_label})"
fig.suptitle(f"GE.MMRI Maumere — Gempa Flores  M{MAG}  (15 Agu 2026, 05:58 WITA)",
             x=0.5, y=0.985, fontsize=13, fontweight="bold", color=C_TEXT)
fig.text(0.5, 0.945, sub, ha="center", fontsize=9.5, color=C_SUP)
fig.text(0.5, 0.012, f"PGV ≈ {pgv:.1f} cm/s   ·   data: GEOFON (GFZ)   ·   ObsPy (adaptasi load.py)",
         ha="center", fontsize=8.5, color=C_MUT)

plt.savefig(OUTPNG, dpi=170, bbox_inches="tight", facecolor=C_PAPER)
print("Saved", OUTPNG)
