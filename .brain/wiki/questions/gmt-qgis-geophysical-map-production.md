---
title: "GMT vs QGIS for Geophysical Map Production"
type: question
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
  - gmt
  - qgis
  - geophysical-mapping
---

# GMT vs QGIS for Geophysical Map Production

## Question

For the user's recurring geophysical analysis maps, when should GMT/PyGMT be preferred, when should QGIS be preferred, and when is a hybrid workflow better?

## Current Answer

Use GMT or PyGMT as the default when the map must be regenerated from analysis products, batch-produced, or kept close to geophysics scripting conventions. Use QGIS when the work is dominated by GIS layer management, visual QA, digitizing/editing, professional layout, atlas/report production, format interoperability, or publishing. Use a hybrid workflow when QGIS is best for preparing/checking layers and GMT/PyGMT is best for final reproducible scientific figures, or when GMT/PyGMT produces core panels that QGIS assembles into report/atlas layouts.

This answer is strong enough as a tool-selection heuristic, but operational templates still need current PyGMT documentation and specific QGIS manual pages.

## Evidence So Far

- User requirement: recurring high-quality geophysical maps need shaded topography/bathymetry, legend, north indicator, and index map.
- CUSeisTut GMT6: scripted GMT can produce a layered topographic map with relief coloring, `@earth_relief_01m`, intensity shading, coastline overlays, station symbols, an inset map, labels, and a colorbar.
- GMT Tutorials: the learning path covers topography coloring, layout design, hillshade, map elements, CPT/colorbar editing, focal mechanisms, 3D maps, image draping, and PyGMT notebooks.
- PyGMT v0.1.0: PyGMT is framed as a Python wrapper for GMT with spatial processing and high-quality static vector map output, but the source is old and should not anchor current API choices.
- QGIS homepage: QGIS is positioned for cartographic design, professional layout, large-format print maps, atlases/reports, layer editing, analysis workflows, format support, interoperability, and publishing.

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
- Synthesis: [[wiki/syntheses/geophysical-map-production-toolchain]]
- Output: [[wiki/outputs/geophysical-map-quality-checklist]]

## Open Questions

- Should scripts be the default deliverable, or is a saved QGIS project acceptable for some outputs?
- Which tasks are most frequent: static publication figures, report maps, field maps, batch map generation, or visual QA of spatial layers?
- How much Python integration is needed for analysis-to-map automation?
- Which current PyGMT documentation should be ingested before building reusable PyGMT templates?
- Which QGIS documentation pages should be ingested before building reusable QGIS project/layout templates?
