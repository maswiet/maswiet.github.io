---
title: "User Map Production Requirements 2026-07-03"
type: source
status: active
created: 2026-07-03
updated: 2026-07-03
sources:
  - "[[raw/2026-07-03_user-map-production-requirements/source]]"
tags:
  - geophysical-mapping
  - cartography
  - requirements
---

# User Map Production Requirements 2026-07-03

## Summary

The user expects to frequently draw analysis results as geophysical maps and has a high quality bar for map output. Required map components include shaded topography and bathymetry, a legend, a north arrow, and an index/inset map. The user recognizes GMT as a geophysics standard while noting that QGIS is increasingly used.

## Key Points

- The primary workflow need is repeated production of high-quality analysis maps, not a one-off figure.
- Required visual elements include topographic/bathymetric shading, legend, north indicator, and an index map.
- GMT should be treated as the established baseline for geophysics-grade map production.
- QGIS should be evaluated as a practical alternative or complement, especially for cartographic layout and GIS layer handling.

## Links

- Raw capture: [[raw/2026-07-03_user-map-production-requirements/source]]
- Concept: [[wiki/concepts/publication-quality-geophysical-mapping]]
- Claim: [[wiki/claims/user-requires-publication-quality-geophysical-maps]]
- Question: [[wiki/questions/gmt-qgis-geophysical-map-production]]
- Synthesis: [[wiki/syntheses/geophysical-map-production-toolchain]]

## Open Questions

- Which output style should be canonical for the user's future maps: journal figure, report plate, slide figure, web map, or print map?
- Should GMT, PyGMT, QGIS, or a mixed workflow become the default production path?
- What datasets should be standardized for Indonesian topography, bathymetry, coastlines, faults, volcanoes, seismicity, and administrative boundaries?
