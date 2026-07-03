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
  - "[[wiki/sources/pygmt-v0-1-0-overview]]"
  - "[[wiki/sources/qgis-homepage]]"
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
- PyGMT is a promising Python bridge for reproducible GMT-style outputs, especially when analysis products already live in Python.
- QGIS is strongest for GIS layer management, editing, visual QA, layout design, atlas/report maps, data-format interoperability, and publishing workflows.
- A mixed workflow may be useful: prepare or inspect layers in QGIS, produce reproducible analysis maps in GMT/PyGMT, and use QGIS when atlas/layout/report workflows dominate.

## Evidence So Far

- The user requires recurring high-quality maps with shaded topography/bathymetry, legend, north indicator, and index map.
- The CUSeisTut GMT6 example demonstrates the core GMT recipe for a shaded topographic map: region/projection, relief CPT, remote `earth_relief` grid, intensity shading, coastlines, contextual tectonic lines, stations, labels, inset map, and colorbar.
- GMT Tutorials broadens the map-production reference set to layout design, hillshade, map elements, CPT/colorbar editing, 3D maps, focal mechanisms, image draping, and PyGMT notebooks.
- The PyGMT v0.1.0 overview supports PyGMT's role as a Python wrapper around GMT for spatial processing and high-quality static map output, but needs a current-docs refresh before API-level use.
- The QGIS homepage supports QGIS's role in professional map layout, large-format print maps, atlases/reports, editing/digitizing, analysis workflows, broad data-format support, standards/interoperability, and publishing.

## Practical Decision Rule

- Use GMT when the priority is geophysics-standard, scriptable, static scientific maps and repeatable batch output.
- Use PyGMT when the priority is connecting Python analysis products to GMT-style static maps.
- Use QGIS when the priority is GIS layer preparation, cartographic layout, print/report/atlas output, data interoperability, or interactive QA.
- Use hybrid workflows when the map needs both strong GIS preparation/layout and reproducible scientific plotting.

## Links

- Source: [[wiki/sources/user-map-production-requirements-2026-07-03]]
- Source: [[wiki/sources/cuseistut-gmt6-topographic-map]]
- Source: [[wiki/sources/gmt-tutorials]]
- Source: [[wiki/sources/pygmt-v0-1-0-overview]]
- Source: [[wiki/sources/qgis-homepage]]
- Concept: [[wiki/concepts/publication-quality-geophysical-mapping]]
- Entity: [[wiki/entities/generic-mapping-tools]]
- Entity: [[wiki/entities/pygmt]]
- Entity: [[wiki/entities/qgis]]
- Question: [[wiki/questions/gmt-qgis-geophysical-map-production]]
- Output: [[wiki/outputs/geophysical-map-quality-checklist]]

## Open Questions

- What map templates should be standardized first: regional overview, local study area, station map, seismicity map, cross-section index map, or bathymetry/topography base map?
- Should the user's default map assets be organized as GMT scripts, PyGMT notebooks, QGIS project templates, or all three?
- Which current PyGMT release and examples should be treated as canonical?
- Which QGIS manual pages should be treated as canonical for layout, atlas, hillshade, and processing models?
