---
title: "CUSeisTut GMT6 Topographic Map"
type: source
status: active
created: 2026-07-03
updated: 2026-07-03
sources:
  - "[[raw/2026-07-03_cuseistut-gmt6-topographic-map/provenance]]"
tags:
  - gmt
  - topography
  - geophysical-mapping
  - tutorial
---

# CUSeisTut GMT6 Topographic Map

## Summary

This CUSeisTut page is a beginner-facing GMT 6 tutorial for creating a topographic map. It is directly relevant to the user's map standard because it demonstrates a scripted GMT workflow with relief coloring, GMT remote topography data, intensity shading, coastline overlays, an inset/index map, station symbols, text labels, and a colorbar.

## Key Points

- The tutorial frames GMT as a widely used open-source mapping tool across Earth, ocean, and planetary sciences.
- It emphasizes shell-scripted GMT workflows for complex figures because scripts are easy to rerun and refine.
- The topographic-map example uses a Mercator regional frame over the Banda Arc, a relief CPT, `grdimage` on `@earth_relief_01m`, and `-I+` intensity for shaded relief.
- The example includes map context elements that matter for the user's standard: coastlines, trench line, station symbols, labels, an inset map, and a colorbar labeled for topography.
- It is useful as a concrete GMT baseline, but it does not cover north arrows, scale bars, QGIS layout workflows, or modern PyGMT equivalents.

## Evidence Extracted

- `gmt makecpt -Crelief ...` is used to build the topography/bathymetry color palette.
- `gmt grdimage @earth_relief_01m ... -I+` is used for relief rendering and intensity shading.
- `gmt inset begin ...` and `gmt inset end` are used for regional context.
- `gmt colorbar ... -By+l"Topo (m)"` is used for the elevation legend.

## Links

- Raw provenance: [[raw/2026-07-03_cuseistut-gmt6-topographic-map/provenance]]
- Raw HTML: [[raw/2026-07-03_cuseistut-gmt6-topographic-map/page]]
- Entity: [[wiki/entities/generic-mapping-tools]]
- Concept: [[wiki/concepts/publication-quality-geophysical-mapping]]
- Claim: [[wiki/claims/gmt-supports-reproducible-shaded-topographic-maps]]
- Question: [[wiki/questions/gmt-qgis-geophysical-map-production]]
- Synthesis: [[wiki/syntheses/geophysical-map-production-toolchain]]

## Open Questions

- Which GMT map elements should become the user's default template: inset map, scale bar, north arrow, colorbar, station symbols, fault/trench overlays, and grid annotations?
- Should the house style use `@earth_relief_01m` by default, or should higher-resolution local DEM/bathymetry grids be standardized for Indonesian study areas?
- How should the GMT example be adapted into a reusable regional map template for the user's analysis outputs?
