---
title: "Generic Mapping Tools"
type: entity
status: active
created: 2026-07-03
updated: 2026-07-03
sources:
  - "[[wiki/sources/cuseistut-gmt6-topographic-map]]"
tags:
  - gmt
  - mapping-software
  - geophysical-mapping
---

# Generic Mapping Tools

## Summary

Generic Mapping Tools (GMT) is an open-source command-line mapping and plotting toolchain used in Earth-science contexts. In the user's mapping workflow, GMT is a strong candidate for reproducible, scripted, geophysics-style figures with relief grids, coastlines, symbols, annotations, insets, and colorbars.

## Relevance To User Workflow

- Supports scripted map production, which helps make recurring analysis maps reproducible.
- Provides direct access to GMT remote relief datasets such as `@earth_relief_01m`.
- Supports layered map construction through commands such as `basemap`, `makecpt`, `grdimage`, `coast`, `plot`, `text`, `inset`, and `colorbar`.

## Links

- Source: [[wiki/sources/cuseistut-gmt6-topographic-map]]
- Concept: [[wiki/concepts/publication-quality-geophysical-mapping]]
- Claim: [[wiki/claims/gmt-supports-reproducible-shaded-topographic-maps]]
- Question: [[wiki/questions/gmt-qgis-geophysical-map-production]]

## Open Questions

- Which GMT version and install path should be standardized for the user's machine and collaborators?
- Which GMT theme/defaults should define the user's house style?
