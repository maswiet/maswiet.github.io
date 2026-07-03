---
title: "Publication-Quality Geophysical Mapping"
type: concept
status: seed
created: 2026-07-03
updated: 2026-07-03
sources:
  - "[[wiki/sources/user-map-production-requirements-2026-07-03]]"
tags:
  - geophysical-mapping
  - cartography
  - visualization
---

# Publication-Quality Geophysical Mapping

## Summary

Publication-quality geophysical mapping means turning analysis outputs into maps that are technically accurate, visually legible, reproducible, and complete enough for scientific communication. For the user's work, the baseline includes shaded topography and bathymetry, clear legends, a north indicator, and an index/inset map.

## Design Criteria

- Relief and bathymetry should support interpretation without overpowering analysis layers.
- Legends should explain color, symbol, line, and raster encodings without forcing readers to infer meanings.
- Index maps should communicate regional context and the exact study area.
- Map layout should be reproducible enough that later figures can reuse scale, typography, color, projection, and data-source decisions.
- Tool choice should balance geophysics norms, reproducibility, cartographic quality, and speed of iteration.

## Links

- Source: [[wiki/sources/user-map-production-requirements-2026-07-03]]
- Claim: [[wiki/claims/user-requires-publication-quality-geophysical-maps]]
- Question: [[wiki/questions/gmt-qgis-geophysical-map-production]]
- Synthesis: [[wiki/syntheses/geophysical-map-production-toolchain]]

## Open Questions

- What house style should define fonts, line weights, label hierarchy, scale bars, color palettes, and export formats?
- Which projections should be default for regional Indonesian maps and smaller local study areas?
- How should maps distinguish analysis layers from context layers such as DEM, bathymetry, faults, coastlines, stations, and seismicity?
