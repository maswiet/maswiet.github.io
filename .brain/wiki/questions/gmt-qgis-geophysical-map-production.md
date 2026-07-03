---
title: "GMT vs QGIS for Geophysical Map Production"
type: question
status: active
created: 2026-07-03
updated: 2026-07-03
sources:
  - "[[wiki/sources/user-map-production-requirements-2026-07-03]]"
tags:
  - gmt
  - qgis
  - geophysical-mapping
---

# GMT vs QGIS for Geophysical Map Production

## Question

For the user's recurring geophysical analysis maps, when should GMT/PyGMT be preferred, when should QGIS be preferred, and when is a hybrid workflow better?

## Current Answer

Needs review after ingesting the referenced GMT, PyGMT, and QGIS sources. The initial requirement suggests GMT should remain the scientific reproducibility baseline, while QGIS may be valuable for GIS layer management, interactive inspection, and polished layout work.

## Links

- Source: [[wiki/sources/user-map-production-requirements-2026-07-03]]
- Concept: [[wiki/concepts/publication-quality-geophysical-mapping]]
- Synthesis: [[wiki/syntheses/geophysical-map-production-toolchain]]

## Open Questions

- Should scripts be the default deliverable, or is a saved QGIS project acceptable for some outputs?
- Which tasks are most frequent: static publication figures, report maps, field maps, batch map generation, or visual QA of spatial layers?
- How much Python integration is needed for analysis-to-map automation?
