---
title: "GMT Supports Reproducible Shaded Topographic Maps"
type: claim
status: active
created: 2026-07-03
updated: 2026-07-03
sources:
  - "[[wiki/sources/cuseistut-gmt6-topographic-map]]"
tags:
  - gmt
  - reproducibility
  - topography
---

# GMT Supports Reproducible Shaded Topographic Maps

## Claim

GMT can support reproducible geophysical topographic map production through scripted layered commands for map frame, relief palette, shaded raster rendering, coastlines, insets, symbols, annotations, and colorbar legends.

## Evidence

- The CUSeisTut example uses a shell script with `gmt begin` and `gmt end` to generate a map output.
- It builds a relief CPT, renders `@earth_relief_01m` with intensity shading, and overlays coastlines, trench data, station symbols, labels, an inset map, and a colorbar.
- The tutorial explicitly presents scripting as the better approach for very complex figures because the figure can be rerun and refined.

## Links

- Source: [[wiki/sources/cuseistut-gmt6-topographic-map]]
- Entity: [[wiki/entities/generic-mapping-tools]]
- Concept: [[wiki/concepts/publication-quality-geophysical-mapping]]
- Synthesis: [[wiki/syntheses/geophysical-map-production-toolchain]]
