---
title: "Geophysical Map Production Toolchain"
type: synthesis
status: active
created: 2026-07-03
updated: 2026-07-03
sources:
  - "[[wiki/sources/user-map-production-requirements-2026-07-03]]"
  - "[[wiki/sources/cuseistut-gmt6-topographic-map]]"
  - "[[wiki/sources/gmt-tutorials]]"
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

- GMT is currently the strongest evidenced baseline for reproducible scripted figures, batch production, and geophysics-native map conventions.
- QGIS is likely strongest for GIS data exploration, layer styling, layout design, and interactive cartographic editing.
- A mixed workflow may be useful: prepare or inspect layers in QGIS, produce reproducible analysis maps in GMT/PyGMT, and use QGIS when atlas/layout/report workflows dominate.

## Evidence So Far

- The user requires recurring high-quality maps with shaded topography/bathymetry, legend, north indicator, and index map.
- The CUSeisTut GMT6 example demonstrates the core GMT recipe for a shaded topographic map: region/projection, relief CPT, remote `earth_relief` grid, intensity shading, coastlines, contextual tectonic lines, stations, labels, inset map, and colorbar.
- GMT Tutorials broadens the map-production reference set to layout design, hillshade, map elements, CPT/colorbar editing, 3D maps, focal mechanisms, image draping, and PyGMT notebooks.

## Links

- Source: [[wiki/sources/user-map-production-requirements-2026-07-03]]
- Source: [[wiki/sources/cuseistut-gmt6-topographic-map]]
- Source: [[wiki/sources/gmt-tutorials]]
- Concept: [[wiki/concepts/publication-quality-geophysical-mapping]]
- Entity: [[wiki/entities/generic-mapping-tools]]
- Question: [[wiki/questions/gmt-qgis-geophysical-map-production]]

## Open Questions

- What map templates should be standardized first: regional overview, local study area, station map, seismicity map, cross-section index map, or bathymetry/topography base map?
- Should the user's default map assets be organized as GMT scripts, PyGMT notebooks, QGIS project templates, or all three?
