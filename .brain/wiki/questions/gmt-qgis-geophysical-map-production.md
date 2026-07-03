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
tags:
  - gmt
  - qgis
  - geophysical-mapping
---

# GMT vs QGIS for Geophysical Map Production

## Question

For the user's recurring geophysical analysis maps, when should GMT/PyGMT be preferred, when should QGIS be preferred, and when is a hybrid workflow better?

## Current Answer

Needs review after ingesting all referenced sources. The GMT sources strengthen the case for GMT as a reproducible scripted baseline for shaded topographic maps and as a learning path for layout, hillshade, colorbar, map elements, and PyGMT examples. The PyGMT v0.1.0 overview supports using Python as a bridge to GMT-quality static maps, but current PyGMT docs are needed before operational template decisions. QGIS still needs separate evidence before deciding the default or hybrid workflow.

## Evidence So Far

- User requirement: recurring high-quality geophysical maps need shaded topography/bathymetry, legend, north indicator, and index map.
- CUSeisTut GMT6: scripted GMT can produce a layered topographic map with relief coloring, `@earth_relief_01m`, intensity shading, coastline overlays, station symbols, an inset map, labels, and a colorbar.
- GMT Tutorials: the learning path covers topography coloring, layout design, hillshade, map elements, CPT/colorbar editing, focal mechanisms, 3D maps, image draping, and PyGMT notebooks.
- PyGMT v0.1.0: PyGMT is framed as a Python wrapper for GMT with spatial processing and high-quality static vector map output, but the source is old and should not anchor current API choices.

## Links

- Source: [[wiki/sources/user-map-production-requirements-2026-07-03]]
- Source: [[wiki/sources/cuseistut-gmt6-topographic-map]]
- Source: [[wiki/sources/gmt-tutorials]]
- Source: [[wiki/sources/pygmt-v0-1-0-overview]]
- Concept: [[wiki/concepts/publication-quality-geophysical-mapping]]
- Entity: [[wiki/entities/generic-mapping-tools]]
- Entity: [[wiki/entities/pygmt]]
- Synthesis: [[wiki/syntheses/geophysical-map-production-toolchain]]

## Open Questions

- Should scripts be the default deliverable, or is a saved QGIS project acceptable for some outputs?
- Which tasks are most frequent: static publication figures, report maps, field maps, batch map generation, or visual QA of spatial layers?
- How much Python integration is needed for analysis-to-map automation?
- Which current PyGMT documentation should be ingested before building reusable PyGMT templates?
