<!-- afk-research:managed v1 -->
# Log

Append-only chronological record for the `.brain` second brain. Use headings in this format:

```markdown
## [YYYY-MM-DD] type | Title
```

Allowed types: `setup`, `ingest`, `query`, `lint`, `maintenance`, `export`, `import`, `schema`.

No activity entries yet. This vault is treated as an initial setup baseline.

## [2026-07-01] ingest | LinkedIn profile for Wiwit Suryanto

- Trigger: User requested ingest of `https://www.linkedin.com/in/wiwit-suryanto-20215a6/`.
- Files changed:
  - `.brain/raw/2026-07-01_wiwit-suryanto-linkedin/provenance.md`
  - `.brain/raw/2026-07-01_wiwit-suryanto-linkedin/headers.txt`
  - `.brain/raw/2026-07-01_wiwit-suryanto-linkedin/page.html`
  - `.brain/wiki/sources/linkedin-wiwit-suryanto-profile.md`
  - `.brain/wiki/entities/wiwit-suryanto.md`
  - `.brain/wiki/index.md`
  - `.brain/wiki/log.md`
- Key result: Captured the LinkedIn URL, recorded the HTTP 429/authwall limitation, and seeded a needs-review person entity.
- Follow-ups: Revisit the LinkedIn profile only if authenticated or otherwise accessible profile content is provided.

## [2026-07-01] ingest | UGM Academic Staff profile for Wiwit Suryanto

- Trigger: User requested ingest of `https://acadstaff.ugm.ac.id/wiwit`.
- Files changed:
  - `.brain/raw/2026-07-01_wiwit-suryanto-ugm-acadstaff/provenance.md`
  - `.brain/raw/2026-07-01_wiwit-suryanto-ugm-acadstaff/headers.txt`
  - `.brain/raw/2026-07-01_wiwit-suryanto-ugm-acadstaff/page.html`
  - `.brain/raw/2026-07-01_wiwit-suryanto-ugm-acadstaff/ajax-profile.html`
  - `.brain/raw/2026-07-01_wiwit-suryanto-ugm-acadstaff/ajax-profile-headers.txt`
  - `.brain/raw/2026-07-01_wiwit-suryanto-ugm-acadstaff/ajax-course.html`
  - `.brain/raw/2026-07-01_wiwit-suryanto-ugm-acadstaff/ajax-course-headers.txt`
  - `.brain/raw/2026-07-01_wiwit-suryanto-ugm-acadstaff/ajax-grant.html`
  - `.brain/raw/2026-07-01_wiwit-suryanto-ugm-acadstaff/ajax-grant-headers.txt`
  - `.brain/raw/2026-07-01_wiwit-suryanto-ugm-acadstaff/ajax-research.html`
  - `.brain/raw/2026-07-01_wiwit-suryanto-ugm-acadstaff/ajax-research-headers.txt`
  - `.brain/raw/2026-07-01_wiwit-suryanto-ugm-acadstaff/ajax-community.html`
  - `.brain/raw/2026-07-01_wiwit-suryanto-ugm-acadstaff/ajax-community-headers.txt`
  - `.brain/raw/2026-07-01_wiwit-suryanto-ugm-acadstaff/ajax-patent.html`
  - `.brain/raw/2026-07-01_wiwit-suryanto-ugm-acadstaff/ajax-patent-headers.txt`
  - `.brain/raw/2026-07-01_wiwit-suryanto-ugm-acadstaff/ajax-publish.html`
  - `.brain/raw/2026-07-01_wiwit-suryanto-ugm-acadstaff/ajax-publish-headers.txt`
  - `.brain/raw/2026-07-01_wiwit-suryanto-ugm-acadstaff/ajax-prototipe.html`
  - `.brain/raw/2026-07-01_wiwit-suryanto-ugm-acadstaff/ajax-prototipe-headers.txt`
  - `.brain/wiki/sources/ugm-acadstaff-wiwit-suryanto.md`
  - `.brain/wiki/entities/wiwit-suryanto.md`
  - `.brain/wiki/entities/universitas-gadjah-mada.md`
  - `.brain/wiki/concepts/seismology-and-seismic-exploration.md`
  - `.brain/wiki/claims/wiwit-suryanto-ugm-academic-profile.md`
  - `.brain/wiki/index.md`
  - `.brain/wiki/log.md`
- Key result: Captured the public UGM profile and tab data; updated Wiwit Suryanto as an active academic entity with UGM affiliation, geophysics/seismology expertise, education, courses, projects, and publication-list summary.
- Follow-ups: Check role currentness against an additional institutional source if vice-dean status matters; compare publication data with Google Scholar during the next ingest.

## [2026-07-01] ingest | Google Scholar profile for Wiwit Suryanto

- Trigger: User requested ingest of `https://scholar.google.com/citations?user=9lJKKt0AAAAJ&hl=en`.
- Files changed:
  - `.brain/raw/2026-07-01_wiwit-suryanto-google-scholar/provenance.md`
  - `.brain/raw/2026-07-01_wiwit-suryanto-google-scholar/headers.txt`
  - `.brain/raw/2026-07-01_wiwit-suryanto-google-scholar/page.html`
  - `.brain/raw/2026-07-01_wiwit-suryanto-google-scholar/list-works-headers.txt`
  - `.brain/raw/2026-07-01_wiwit-suryanto-google-scholar/list-works.html`
  - `.brain/wiki/sources/google-scholar-wiwit-suryanto-profile.md`
  - `.brain/wiki/sources/ugm-acadstaff-wiwit-suryanto.md`
  - `.brain/wiki/entities/wiwit-suryanto.md`
  - `.brain/wiki/entities/universitas-gadjah-mada.md`
  - `.brain/wiki/concepts/seismology-and-seismic-exploration.md`
  - `.brain/wiki/claims/wiwit-suryanto-google-scholar-profile-metrics.md`
  - `.brain/wiki/index.md`
  - `.brain/wiki/log.md`
- Key result: Captured Google Scholar profile metadata, dated citation metrics, top cited articles, and 100 list-works rows; cross-linked the source to Wiwit Suryanto, UGM, and the seismology/geophysics concept.
- Follow-ups: Refresh metrics before time-sensitive use; decide which publication source should be canonical if a polished CV or website page is generated.

## [2026-07-01] ingest | Project Industri FMIPA 2022-2025 workbook

- Trigger: User requested ingest of `/Users/maswiet/Downloads/Project_Industri_FMIPA_2022_2025.xlsx`.
- Files changed:
  - `.brain/raw/2026-07-01_project-industri-fmipa-2022-2025/Project_Industri_FMIPA_2022_2025.xlsx`
  - `.brain/raw/2026-07-01_project-industri-fmipa-2022-2025/provenance.md`
  - `.brain/wiki/sources/project-industri-fmipa-2022-2025.md`
  - `.brain/wiki/entities/fmipa-ugm.md`
  - `.brain/wiki/entities/universitas-gadjah-mada.md`
  - `.brain/wiki/concepts/industry-funded-applied-research-portfolio.md`
  - `.brain/wiki/concepts/seismology-and-seismic-exploration.md`
  - `.brain/wiki/claims/fmipa-ugm-industrial-project-portfolio-2022-2026.md`
  - `.brain/wiki/index.md`
  - `.brain/wiki/log.md`
- Key result: Captured the workbook and summarized 82 FMIPA UGM industrial/applied project rows dated 2022-2026, including collaborator patterns, funding-column totals, dominant applied geophysics themes, and source limitations.
- Follow-ups: Confirm the Funding column currency, the intended date range given 2026 rows in a 2022-2025 file, and which projects should be attributed directly to Wiwit Suryanto.

## [2026-07-01] ingest | LEAF 2026 FMIPA Experiment deck

- Trigger: User requested ingest of `/Users/maswiet/Downloads/LEAF_2026_Wiwit_Suryanto_v3_The_FMIPA_Experiment.pptx`.
- Files changed:
  - `.brain/raw/2026-07-01_leaf-2026-wiwit-suryanto-the-fmipa-experiment/LEAF_2026_Wiwit_Suryanto_v3_The_FMIPA_Experiment.pptx`
  - `.brain/raw/2026-07-01_leaf-2026-wiwit-suryanto-the-fmipa-experiment/provenance.md`
  - `.brain/wiki/sources/leaf-2026-wiwit-suryanto-the-fmipa-experiment.md`
  - `.brain/wiki/sources/project-industri-fmipa-2022-2025.md`
  - `.brain/wiki/entities/wiwit-suryanto.md`
  - `.brain/wiki/entities/fmipa-ugm.md`
  - `.brain/wiki/entities/universitas-gadjah-mada.md`
  - `.brain/wiki/entities/leaf-2026.md`
  - `.brain/wiki/concepts/research-management-kpi-experiment.md`
  - `.brain/wiki/concepts/industry-funded-applied-research-portfolio.md`
  - `.brain/wiki/concepts/seismology-and-seismic-exploration.md`
  - `.brain/wiki/claims/fmipa-research-management-kpi-experiment-2022-2026.md`
  - `.brain/wiki/syntheses/fmipa-experiment-portfolio-and-kpi-shift.md`
  - `.brain/wiki/index.md`
  - `.brain/wiki/log.md`
- Key result: Captured the LEAF 2026 deck and extracted the "FMIPA Experiment" narrative: a 2022-2026 research-management KPI shift toward industry funding, product adoption, and community impact, with publication output treated as a control.
- Follow-ups: Reconcile the deck's Rp 184 billion and annual trajectory figures against the workbook; validate the cited Scival FMIPA publication-output claim; confirm whether `v3` is the final LEAF 2026 deck.

## [2026-07-01] ingest | Life Balance As Lecturer PDF

- Trigger: User requested ingest of `/Users/maswiet/Library/Mobile Documents/com~apple~CloudDocs/Downloads/Life Balance As Lecturer.pdf`.
- Files changed:
  - `.brain/raw/2026-07-01_life-balance-as-lecturer/Life_Balance_As_Lecturer.pdf`
  - `.brain/raw/2026-07-01_life-balance-as-lecturer/provenance.md`
  - `.brain/wiki/sources/life-balance-as-lecturer-2023.md`
  - `.brain/wiki/entities/wiwit-suryanto.md`
  - `.brain/wiki/entities/fmipa-ugm.md`
  - `.brain/wiki/entities/universitas-gadjah-mada.md`
  - `.brain/wiki/concepts/lecturer-life-balance-through-tridharma.md`
  - `.brain/wiki/concepts/industry-funded-applied-research-portfolio.md`
  - `.brain/wiki/concepts/seismology-and-seismic-exploration.md`
  - `.brain/wiki/claims/wiwit-suryanto-tridharma-and-professional-service-roles-2023.md`
  - `.brain/wiki/sources/project-industri-fmipa-2022-2025.md`
  - `.brain/wiki/syntheses/fmipa-experiment-portfolio-and-kpi-shift.md`
  - `.brain/wiki/index.md`
  - `.brain/wiki/log.md`
- Key result: Captured the 2023 PDF deck and extracted a Tridharma-based lecturer-balance narrative linking teaching, impactful research, global/community service, professional roles, and 2022-2023 industrial contract portfolios.
- Follow-ups: Confirm the original audience/event for the deck, validate listed professional service roles against independent sources before public use, and reconcile the deck's USD industrial-contract totals with the later FMIPA project workbook.

## [2026-07-03] ingest | User geophysical map production requirements

- Trigger: User requested ingest of map-production context and related GMT/PyGMT/QGIS URLs.
- Files changed:
  - `.brain/raw/2026-07-03_user-map-production-requirements/source.md`
  - `.brain/wiki/sources/user-map-production-requirements-2026-07-03.md`
  - `.brain/wiki/concepts/publication-quality-geophysical-mapping.md`
  - `.brain/wiki/claims/user-requires-publication-quality-geophysical-maps.md`
  - `.brain/wiki/questions/gmt-qgis-geophysical-map-production.md`
  - `.brain/wiki/syntheses/geophysical-map-production-toolchain.md`
  - `.brain/wiki/index.md`
  - `.brain/wiki/log.md`
- Key result: Captured the user's durable requirement for recurring high-quality geophysical maps with shaded topography/bathymetry, legend, north indicator, and index map, and seeded the GMT/QGIS workflow question.
- Follow-ups: Ingest the referenced GMT, PyGMT, and QGIS sources to ground the toolchain synthesis in documentation.

## [2026-07-03] ingest | CUSeisTut GMT6 topographic map tutorial

- Trigger: User requested ingest of `https://cuseistut.readthedocs.io/en/latest/GMT6-1/index.html`.
- Files changed:
  - `.brain/raw/2026-07-03_cuseistut-gmt6-topographic-map/page.html`
  - `.brain/raw/2026-07-03_cuseistut-gmt6-topographic-map/headers.txt`
  - `.brain/raw/2026-07-03_cuseistut-gmt6-topographic-map/curl-metadata.txt`
  - `.brain/raw/2026-07-03_cuseistut-gmt6-topographic-map/provenance.md`
  - `.brain/wiki/sources/cuseistut-gmt6-topographic-map.md`
  - `.brain/wiki/entities/generic-mapping-tools.md`
  - `.brain/wiki/concepts/publication-quality-geophysical-mapping.md`
  - `.brain/wiki/claims/gmt-supports-reproducible-shaded-topographic-maps.md`
  - `.brain/wiki/questions/gmt-qgis-geophysical-map-production.md`
  - `.brain/wiki/syntheses/geophysical-map-production-toolchain.md`
  - `.brain/wiki/index.md`
  - `.brain/wiki/log.md`
- Key result: Captured a concrete GMT6 recipe for a shaded topographic geophysical map using relief CPT, `@earth_relief_01m`, intensity shading, coastlines, tectonic/station overlays, labels, inset map, and colorbar.
- Follow-ups: Adapt the GMT example into a reusable Indonesian regional-map template and decide which DEM/bathymetry resolution should be standardized.

## [2026-07-03] ingest | GMT Tutorials

- Trigger: User requested ingest of `https://gmt-tutorials.org/en/`.
- Files changed:
  - `.brain/raw/2026-07-03_gmt-tutorials/page.html`
  - `.brain/raw/2026-07-03_gmt-tutorials/headers.txt`
  - `.brain/raw/2026-07-03_gmt-tutorials/curl-metadata.txt`
  - `.brain/raw/2026-07-03_gmt-tutorials/provenance.md`
  - `.brain/wiki/sources/gmt-tutorials.md`
  - `.brain/wiki/entities/generic-mapping-tools.md`
  - `.brain/wiki/concepts/publication-quality-geophysical-mapping.md`
  - `.brain/wiki/claims/gmt-tutorials-provide-map-production-learning-path.md`
  - `.brain/wiki/questions/gmt-qgis-geophysical-map-production.md`
  - `.brain/wiki/syntheses/geophysical-map-production-toolchain.md`
  - `.brain/wiki/index.md`
  - `.brain/wiki/log.md`
- Key result: Captured a structured GMT/PyGMT learning resource covering topography coloring, layout, hillshade, map elements, CPT/colorbar editing, 3D maps, focal mechanisms, image draping, and PyGMT notebooks.
- Follow-ups: Ingest specific chapters later if a reusable house-style map template needs operational command details.

## [2026-07-03] ingest | PyGMT v0.1.0 overview

- Trigger: User requested ingest of `https://www.pygmt.org/v0.1.0/overview.html`.
- Files changed:
  - `.brain/raw/2026-07-03_pygmt-v0-1-0-overview/page.html`
  - `.brain/raw/2026-07-03_pygmt-v0-1-0-overview/headers.txt`
  - `.brain/raw/2026-07-03_pygmt-v0-1-0-overview/curl-metadata.txt`
  - `.brain/raw/2026-07-03_pygmt-v0-1-0-overview/provenance.md`
  - `.brain/wiki/sources/pygmt-v0-1-0-overview.md`
  - `.brain/wiki/entities/pygmt.md`
  - `.brain/wiki/entities/generic-mapping-tools.md`
  - `.brain/wiki/concepts/publication-quality-geophysical-mapping.md`
  - `.brain/wiki/claims/pygmt-connects-python-analysis-to-gmt-quality-maps.md`
  - `.brain/wiki/questions/gmt-qgis-geophysical-map-production.md`
  - `.brain/wiki/syntheses/geophysical-map-production-toolchain.md`
  - `.brain/wiki/index.md`
  - `.brain/wiki/log.md`
- Key result: Captured PyGMT as a Python wrapper around GMT for spatial processing and high-quality static map output, while marking the page as old versioned documentation that should be refreshed before API-level template work.
- Follow-ups: Ingest current PyGMT documentation before building reusable PyGMT map templates.

## [2026-07-03] ingest | QGIS homepage

- Trigger: User requested ingest of `https://www.qgis.org/`.
- Files changed:
  - `.brain/raw/2026-07-03_qgis-homepage/page.html`
  - `.brain/raw/2026-07-03_qgis-homepage/headers.txt`
  - `.brain/raw/2026-07-03_qgis-homepage/curl-metadata.txt`
  - `.brain/raw/2026-07-03_qgis-homepage/provenance.md`
  - `.brain/wiki/sources/qgis-homepage.md`
  - `.brain/wiki/entities/qgis.md`
  - `.brain/wiki/concepts/publication-quality-geophysical-mapping.md`
  - `.brain/wiki/claims/qgis-supports-professional-map-layout-and-gis-workflows.md`
  - `.brain/wiki/questions/gmt-qgis-geophysical-map-production.md`
  - `.brain/wiki/syntheses/geophysical-map-production-toolchain.md`
  - `.brain/wiki/outputs/geophysical-map-quality-checklist.md`
  - `.brain/wiki/index.md`
  - `.brain/wiki/log.md`
- Key result: Captured QGIS as the GIS/layout complement to GMT/PyGMT, especially for layer management, professional layout, atlases/reports, editing, analysis workflows, data-format support, interoperability, and publishing.
- Follow-ups: Ingest specific QGIS manual pages for print layout, atlas/report generation, hillshade/terrain analysis, layer styling, and processing models before building QGIS templates.
