# Diskusi Publik — Respons Tanggap Darurat Gempa Flores 2026

Slide deck untuk Wiwit Suryanto sebagai narasumber di **Diskusi Publik PSBA UGM**
(daring, 21 Agustus 2026), dari sudut pandang **seismologi/geofisika**.

## Isi

| File | Keterangan |
|------|-----------|
| `deck.html` | Dek presentasi 9 slide (gaya *elegant-minimalist*). Presentasikan di browser: **F** layar penuh, **←/→** atau klik untuk navigasi, **P** cetak PDF. |
| `deck.pdf` | Ekspor PDF 9 halaman 16:9 (Chrome headless). Siap di-*share screen*. |
| `Diskusi_Publik_Gempa_Flores_2026_Wiwit_Suryanto.pptx` | Versi PowerPoint editable (python-pptx). |
| `assets/w01_seismisitas_indonesia.png` | Peta seismisitas Indonesia (katalog BMKG 1998–2024), dari repo Kuliah_Seismologi. Pembuka. |
| `assets/waveform_mmri_flores2026.png` | Waveform 3-komponen + spektrogram GE.MMRI (Maumere), gempa Flores 2026. |
| `make_waveform_mmri.py` | Skrip ObsPy penarik & pemplot waveform GEOFON (adaptasi `Pak_Beck/New2/load.py`). |
| `build_pptx.py` | Skrip pembangun PPTX. |

## Alur slide

1. Pembuka — "Indonesia adalah rumah gempa" (peta seismisitas)
2. Peta penuh — 217.801 gempa
3. Zoom Flores — titik ini bagian dari denyut kegempaan nasional
4. Fakta gempa (Mw 7,7; 15 Agu 2026)
5. Analog FBAT: 1992 Flores → 2018 Lombok → 2026 Flores
6. Sejarah pra-instrumen (katalog Wichmann): Solor 1648, laut utara Flores 1837, Nanga Rama 1855, Ende 1868
7. Peta gempa historis NTT (katalog Wichmann) — sebaran kejadian hingga 1877
8. 72 jam pertama — peran seismologi
9. Waveform GE.MMRI — PGA 0,14 g, PGV 1,9 cm/s, Δ104 km
10. Susulan (Omori) & pesan evakuasi mandiri
11. Penutup — pemantauan Indonesia timur & sensor biaya rendah

## Data & sumber

- **Parameter gempa:** USGS Mw 7,7 (GFZ Mw 7,61), 2026-08-14T21:58:21 UTC, kedalaman 10 km,
  episenter 8,31°S 121,35°E, sesar naik busur-belakang Flores. Dampak/susulan dari BMKG.
  Data korban masih berkembang — verifikasi ulang angka menjelang acara.
- **Waveform:** stasiun GEOFON **GE.MMRI** (broadband BH* + akselerometer HN*), diambil via FDSN
  `https://geofon.gfz.de`. Terukur: Δ 104 km (az 110°), PGV ≈ 1,9 cm/s, PGA ≈ 0,14 g.
- **Analog Lombok 2018:** katalog & analisis di `~/Work/DATA/Pak_Beck` (GCMT thrust, b-value, ISC→Mw).

## Reproduksi

```sh
# waveform (butuh obspy + akses jaringan ke GEOFON)
python3 make_waveform_mmri.py
# pptx
python3 build_pptx.py
# pdf (butuh Google Chrome; jalankan server dulu)
python3 -m http.server 4600 --directory . &
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless=new \
  --no-pdf-header-footer --print-to-pdf=deck.pdf http://localhost:4600/deck.html
```

## Verifikasi

- `deck.html` & `deck.pdf` — diverifikasi visual (opener, peta, zoom Flores, fakta, waveform). ✓
- `waveform_mmri_flores2026.png` — dari data GEOFON asli, diperiksa visual. ✓
- **PPTX belum dirender-verifikasi** (LibreOffice tidak tersedia di mesin ini); dibangun dengan
  python-pptx yang andal. Buka sekali di PowerPoint/Keynote untuk memastikan tata letak.

## Catatan

- Font: Source Serif 4 + Inter (Google Fonts di HTML; PowerPoint menyubstitusi bila font tak terpasang).
- Angka dampak bersifat sementara (data BMKG berkembang).
