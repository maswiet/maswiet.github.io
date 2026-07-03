---
title: "Publication-Quality Geophysical Mapping"
type: concept
status: active
created: 2026-07-03
updated: 2026-07-03
sources:
  - "[[wiki/sources/user-map-production-requirements-2026-07-03]]"
  - "[[wiki/sources/cuseistut-gmt6-topographic-map]]"
  - "[[wiki/sources/gmt-tutorials]]"
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

## GMT Pattern

The CUSeisTut GMT6 example provides a practical baseline for a publication-style geophysical base map: define region and projection, create a relief CPT, render GMT remote relief with intensity shading, add coastlines and tectonic/context layers, place an inset/index map, plot analysis or station symbols, annotate features, and add a labeled colorbar.

## Learning Path

GMT Tutorials expands the operational reference set beyond one map: topography coloring, layout design, hillshade, map elements, CPT/colorbar editing, focal mechanisms, 3D maps, and image draping are all candidates for future map-template standards.

## Links

- Source: [[wiki/sources/user-map-production-requirements-2026-07-03]]
- Source: [[wiki/sources/cuseistut-gmt6-topographic-map]]
- Source: [[wiki/sources/gmt-tutorials]]
- Entity: [[wiki/entities/generic-mapping-tools]]
- Claim: [[wiki/claims/user-requires-publication-quality-geophysical-maps]]
- Claim: [[wiki/claims/gmt-supports-reproducible-shaded-topographic-maps]]
- Claim: [[wiki/claims/gmt-tutorials-provide-map-production-learning-path]]
- Question: [[wiki/questions/gmt-qgis-geophysical-map-production]]
- Synthesis: [[wiki/syntheses/geophysical-map-production-toolchain]]

## Open Questions

- What house style should define fonts, line weights, label hierarchy, scale bars, color palettes, and export formats?
- Which projections should be default for regional Indonesian maps and smaller local study areas?
- How should maps distinguish analysis layers from context layers such as DEM, bathymetry, faults, coastlines, stations, and seismicity?
- Which GMT elements are mandatory in the reusable template and which are study-specific?
- Which GMT Tutorials chapters should be converted first into local templates?
