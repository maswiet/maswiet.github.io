---
title: "PyGMT"
type: entity
status: active
created: 2026-07-03
updated: 2026-07-03
sources:
  - "[[wiki/sources/pygmt-v0-1-0-overview]]"
  - "[[wiki/sources/gmt-tutorials]]"
tags:
  - pygmt
  - python
  - gmt
  - mapping-software
---

# PyGMT

## Summary

PyGMT is a Python interface to GMT. For the user's map-production workflow, it is relevant as a possible bridge between Python-based geophysical analysis and GMT-style publication-quality static maps.

## Relevance To User Workflow

- Useful when the analysis pipeline is already in Python and the map should remain scriptable and reproducible.
- Potentially reduces friction compared with shell-only GMT for users who already manage arrays, tables, gridded data, and analysis outputs in Python.
- Should be checked against current documentation before operational use because the captured overview is for `v0.1.0`.

## Links

- Source: [[wiki/sources/pygmt-v0-1-0-overview]]
- Source: [[wiki/sources/gmt-tutorials]]
- Entity: [[wiki/entities/generic-mapping-tools]]
- Concept: [[wiki/concepts/publication-quality-geophysical-mapping]]
- Claim: [[wiki/claims/pygmt-connects-python-analysis-to-gmt-quality-maps]]
- Question: [[wiki/questions/gmt-qgis-geophysical-map-production]]

## Open Questions

- Should future map examples be implemented in PyGMT first, GMT shell first, or both?
- Which current PyGMT install path is most reliable for the user's environment?
