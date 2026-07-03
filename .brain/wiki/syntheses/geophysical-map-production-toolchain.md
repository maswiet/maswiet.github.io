---
title: "Geophysical Map Production Toolchain"
type: synthesis
status: seed
created: 2026-07-03
updated: 2026-07-03
sources:
  - "[[wiki/sources/user-map-production-requirements-2026-07-03]]"
tags:
  - geophysical-mapping
  - gmt
  - pygmt
  - qgis
---

# Geophysical Map Production Toolchain

## Summary

The user's target workflow is recurring production of high-quality geophysical maps. The initial toolchain question is not simply "GMT or QGIS"; it is how to combine reproducible scientific plotting, shaded topography/bathymetry, cartographic layout, and reusable map standards.

## Current Working Model

- GMT/PyGMT is likely strongest for reproducible scripted figures, batch production, and geophysics-native map conventions.
- QGIS is likely strongest for GIS data exploration, layer styling, layout design, and interactive cartographic editing.
- A mixed workflow may be useful: prepare or inspect layers in QGIS, produce reproducible analysis maps in GMT/PyGMT, and use QGIS when atlas/layout/report workflows dominate.

## Links

- Source: [[wiki/sources/user-map-production-requirements-2026-07-03]]
- Concept: [[wiki/concepts/publication-quality-geophysical-mapping]]
- Question: [[wiki/questions/gmt-qgis-geophysical-map-production]]

## Open Questions

- What map templates should be standardized first: regional overview, local study area, station map, seismicity map, cross-section index map, or bathymetry/topography base map?
- Should the user's default map assets be organized as GMT scripts, PyGMT notebooks, QGIS project templates, or all three?
