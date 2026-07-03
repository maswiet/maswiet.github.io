---
title: "Geophysical Map Quality Checklist"
type: output
status: seed
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
  - checklist
  - gmt
  - pygmt
  - qgis
---

# Geophysical Map Quality Checklist

Use this as a seed checklist before building reusable GMT, PyGMT, or QGIS templates.

## Data And Projection

- Define map purpose, audience, output size, and export format.
- Record projection, region bounds, coordinate reference system, grid resolution, and vertical datum when known.
- Record DEM/bathymetry source, coastline source, and any faults, trenches, stations, seismicity, or administrative layers.

## Base Map

- Use shaded topography and bathymetry when relief context helps interpretation.
- Choose color palettes that preserve land/sea meaning and do not obscure analysis layers.
- Keep relief shading subordinate to the scientific signal.
- Add coastlines, borders, trenches/faults, stations, and other context layers only when they explain the analysis.

## Required Map Elements

- Include a clear legend or symbol key for analysis layers.
- Include a colorbar for continuous raster or elevation/bathymetry encodings.
- Include an index/inset map for regional context when the study area is not immediately obvious.
- Include a north indicator when orientation is not obvious from graticules/projection.
- Include scale information when distance interpretation matters and the projection/extent supports it.

## Layout And Legibility

- Establish visual hierarchy: analysis data first, context second, decoration last.
- Check label placement, font size, line weight, symbol size, and contrast at final export size.
- Keep map frame, graticule, tick labels, title, legend, colorbar, and inset aligned and uncluttered.

## Reproducibility

- Prefer GMT or PyGMT when the figure must be regenerated from analysis outputs.
- Prefer QGIS when GIS layer preparation, visual QA, atlas/report layouts, or complex data-format handling dominate.
- Preserve scripts, notebooks, QGIS project files, style files, data paths, and export settings with the figure.

## Open Template Decisions

- Standard DEM/bathymetry datasets for Indonesian regional and local maps.
- Default projections for national, regional, and local study areas.
- House style for fonts, line weights, color palettes, station symbols, fault/trench styling, scale bars, north indicators, and inset maps.
