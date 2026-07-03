<!-- afk-research:managed v1 -->
# Index

This is the content map for the `.brain` second brain. Read this file before answering from or editing the wiki. Update it on every ingest and every durable query that changes the vault.

Last updated: 2026-07-03

## Start Here

- [[AGENTS|AGENTS.md]] - Operating schema for the LLM wiki agent.
- [[CLAUDE|CLAUDE.md]] - Claude-compatible pointer to the schema.
- [[wiki/log|log.md]] - Append-only chronological activity log.

## Folder Conventions

- `raw/` - Immutable source captures and provenance records.
- `wiki/` - All maintained knowledge and operating files.
- `wiki/index.md` - This content map.
- `wiki/log.md` - Append-only activity log.
- `wiki/sources/` - Source summaries and extracted takeaways.
- `wiki/concepts/` - Durable ideas and patterns.
- `wiki/entities/` - People, organizations, projects, datasets, and named things.
- `wiki/claims/` - Evidence-bearing claims worth tracking.
- `wiki/questions/` - Research questions and durable answers.
- `wiki/syntheses/` - Multi-source analysis and evolving theses.
- `wiki/outputs/` - Exportable artifacts and examples.
- `wiki/templates/` - Reusable page templates and workflow checklists.
- `wiki/inbox/` - Unprocessed material waiting for ingest.
- `wiki/scratch/` - Temporary agent work notes.
- `wiki/archive/` - Superseded or inactive material.

## Sources

- [[wiki/sources/user-map-production-requirements-2026-07-03]] - User-stated requirements for recurring high-quality geophysical maps with shaded topography/bathymetry, legend, north indicator, and index map.
- [[wiki/sources/cuseistut-gmt6-topographic-map]] - CUSeisTut GMT6 tutorial demonstrating a scripted shaded topographic map with relief CPT, `earth_relief`, inset map, station symbols, labels, and colorbar.
- [[wiki/sources/gmt-tutorials]] - Structured GMT/PyGMT learning resource covering topography coloring, layout, hillshade, map elements, CPT/colorbar editing, 3D maps, focal mechanisms, and image draping.
- [[wiki/sources/pygmt-v0-1-0-overview]] - Versioned PyGMT overview describing PyGMT as a Python wrapper for GMT and a route to high-quality static maps; API details need current-docs review.
- [[wiki/sources/linkedin-wiwit-suryanto-profile]] - Access-limited LinkedIn profile capture for Wiwit Suryanto.
- [[wiki/sources/ugm-acadstaff-wiwit-suryanto]] - Public UGM Academic Staff profile with affiliation, expertise, education, projects, courses, and publication-list data.
- [[wiki/sources/google-scholar-wiwit-suryanto-profile]] - Google Scholar profile with UGM affiliation, topic labels, dated citation metrics, and article-list captures.
- [[wiki/sources/life-balance-as-lecturer-2023]] - Local 2023 PDF deck framing lecturer balance through Tridharma, professional service, global engagement, and early industrial contract portfolios.
- [[wiki/sources/project-industri-fmipa-2022-2025]] - Local workbook listing FMIPA UGM industrial/applied project rows for 2022-2026, with funding values and collaborator names.
- [[wiki/sources/leaf-2026-wiwit-suryanto-the-fmipa-experiment]] - Local LEAF 2026 deck framing FMIPA UGM's 2022-2026 industry-collaboration shift as a research-management KPI experiment.

## Concepts

- [[wiki/concepts/publication-quality-geophysical-mapping]] - Working standard for complete, reproducible, high-quality geophysical maps and their required cartographic elements.
- [[wiki/concepts/seismology-and-seismic-exploration]] - Research area tied to Wiwit Suryanto's UGM and Google Scholar profiles, including earthquake hazard, passive seismic uses, volcanology, and microearthquake monitoring.
- [[wiki/concepts/lecturer-life-balance-through-tridharma]] - Academic-career concept seeded from the 2023 life-balance deck, linking teaching, research, service, global roles, and industry work.
- [[wiki/concepts/industry-funded-applied-research-portfolio]] - Pattern for university-industry applied research portfolios, seeded from the FMIPA UGM industrial project workbook.
- [[wiki/concepts/research-management-kpi-experiment]] - KPI-design concept from the LEAF 2026 deck, linking industry funding, product adoption, community impact, and publication-output control.

## Entities

- [[wiki/entities/generic-mapping-tools]] - Open-source command-line mapping toolchain tracked as the geophysics-style scripted baseline for reproducible map production.
- [[wiki/entities/pygmt]] - Python interface to GMT tracked as a possible analysis-to-map bridge for reproducible geophysical figures.
- [[wiki/entities/wiwit-suryanto]] - UGM academic profile entity focused on geophysics, seismology, volcanology, seismic exploration, and earthquake hazard topics.
- [[wiki/entities/universitas-gadjah-mada]] - Institution linked to Wiwit Suryanto through UGM Academic Staff and Google Scholar profile evidence.
- [[wiki/entities/fmipa-ugm]] - Faculty of Mathematics and Natural Sciences at UGM, linked to Wiwit Suryanto's UGM profile and the industrial project workbook.
- [[wiki/entities/leaf-2026]] - Event context named in the LEAF 2026 deck at Universitas Indonesia on 2026-07-08 to 2026-07-09.

## Claims

- [[wiki/claims/user-requires-publication-quality-geophysical-maps]] - User-stated requirement for frequent high-quality geophysical maps with shaded relief/bathymetry, legend, north indicator, and index map.
- [[wiki/claims/gmt-supports-reproducible-shaded-topographic-maps]] - CUSeisTut evidence that GMT can script shaded topographic maps with relief grids, insets, symbols, annotations, and colorbar legends.
- [[wiki/claims/gmt-tutorials-provide-map-production-learning-path]] - Evidence that GMT Tutorials offers a structured learning path for high-quality GMT/PyGMT map production.
- [[wiki/claims/pygmt-connects-python-analysis-to-gmt-quality-maps]] - Needs-review claim that PyGMT bridges Python analysis to GMT-quality static maps; current docs needed for API details.
- [[wiki/claims/wiwit-suryanto-ugm-academic-profile]] - UGM Academic Staff profile evidence for Wiwit Suryanto's affiliation and expertise.
- [[wiki/claims/wiwit-suryanto-google-scholar-profile-metrics]] - Dated Google Scholar profile and citation-metrics snapshot for Wiwit Suryanto.
- [[wiki/claims/wiwit-suryanto-tridharma-and-professional-service-roles-2023]] - Needs-review claim summarizing the 2023 life-balance deck's Tridharma framing and listed professional service roles.
- [[wiki/claims/fmipa-ugm-industrial-project-portfolio-2022-2026]] - Needs-review claim summarizing the FMIPA UGM industrial project portfolio rows, totals, dominant partner pattern, and uncertainty.
- [[wiki/claims/fmipa-research-management-kpi-experiment-2022-2026]] - Needs-review claim summarizing the LEAF 2026 deck's FMIPA research-management KPI experiment narrative.

## Questions

- [[wiki/questions/gmt-qgis-geophysical-map-production]] - Tracks when GMT/PyGMT, QGIS, or hybrid workflows should be used for the user's geophysical map production.

## Syntheses

- [[wiki/syntheses/geophysical-map-production-toolchain]] - Evolving synthesis for a reproducible, high-quality geophysical map production workflow across GMT, PyGMT, and QGIS.
- [[wiki/syntheses/fmipa-experiment-portfolio-and-kpi-shift]] - Cross-source synthesis connecting the LEAF 2026 narrative to the industrial project workbook and their numeric reconciliation issues.

## Outputs

- No output pages currently.

## Templates

- [[wiki/templates/source-page]] - Template for source summary pages.
- [[wiki/templates/concept-page]] - Template for concept pages.
- [[wiki/templates/entity-page]] - Template for entity pages.
- [[wiki/templates/ingest-checklist]] - Checklist for future ingest work.

## Open Threads

- Keep all second-brain work inside `.brain`, with content organized under only `raw/` and `wiki/`.
- Brain operations that change `.brain` must commit and push those `.brain` changes to the repository remote before reporting completion.
- Brain imports are non-destructive: imported knowledge enriches the current vault, while schema and operational-file collisions are preserved as provenance unless explicitly approved.
- Brain setup should also ensure generated export/import artifacts under `.outputs/` are ignored by Git.
- Confirm attribution before using the FMIPA industrial project workbook as evidence for Wiwit Suryanto personally; the workbook does not identify per-person roles.
- Reconcile the LEAF deck and FMIPA project workbook before using public-facing numbers for contract value, annual project counts, or geophysics-only 2025 totals.
- Validate professional service roles from the 2023 life-balance deck against independent sources before presenting them as externally confirmed.
- Define a reusable geophysical map house style covering projections, DEM/bathymetry sources, relief shading, color palettes, legends, north indicators, scale bars, and index maps.
- Refresh PyGMT evidence from current documentation before committing to API-level map templates.
