---
title: "Generic Mapping Tools"
type: entity
status: active
created: 2026-07-03
updated: 2026-07-03
sources:
  - "[[wiki/sources/cuseistut-gmt6-topographic-map]]"
  - "[[wiki/sources/gmt-tutorials]]"
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

## Learning Resources

- [[wiki/sources/cuseistut-gmt6-topographic-map]] provides a concrete topographic-map recipe.
- [[wiki/sources/gmt-tutorials]] provides a broader learning path for first maps, topography coloring, layout, hillshade, map elements, CPT/colorbar work, 3D maps, focal mechanisms, and PyGMT examples.

## Links

- Source: [[wiki/sources/cuseistut-gmt6-topographic-map]]
- Source: [[wiki/sources/gmt-tutorials]]
- Concept: [[wiki/concepts/publication-quality-geophysical-mapping]]
- Claim: [[wiki/claims/gmt-supports-reproducible-shaded-topographic-maps]]
- Claim: [[wiki/claims/gmt-tutorials-provide-map-production-learning-path]]
- Question: [[wiki/questions/gmt-qgis-geophysical-map-production]]

## Open Questions

- Which GMT version and install path should be standardized for the user's machine and collaborators?
- Which GMT theme/defaults should define the user's house style?
