<!-- afk-research:managed v1 -->
# Index

This is the content map for the `.brain` second brain. Read this file before answering from or editing the wiki. Update it on every ingest and every durable query that changes the vault.

Last updated: 2026-07-01

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

- [[wiki/sources/linkedin-wiwit-suryanto-profile]] - Access-limited LinkedIn profile capture for Wiwit Suryanto.
- [[wiki/sources/ugm-acadstaff-wiwit-suryanto]] - Public UGM Academic Staff profile with affiliation, expertise, education, projects, courses, and publication-list data.
- [[wiki/sources/google-scholar-wiwit-suryanto-profile]] - Google Scholar profile with UGM affiliation, topic labels, dated citation metrics, and article-list captures.

## Concepts

- [[wiki/concepts/seismology-and-seismic-exploration]] - Research area tied to Wiwit Suryanto's UGM and Google Scholar profiles, including earthquake hazard, passive seismic uses, volcanology, and microearthquake monitoring.

## Entities

- [[wiki/entities/wiwit-suryanto]] - UGM academic profile entity focused on geophysics, seismology, volcanology, seismic exploration, and earthquake hazard topics.
- [[wiki/entities/universitas-gadjah-mada]] - Institution linked to Wiwit Suryanto through UGM Academic Staff and Google Scholar profile evidence.

## Claims

- [[wiki/claims/wiwit-suryanto-ugm-academic-profile]] - UGM Academic Staff profile evidence for Wiwit Suryanto's affiliation and expertise.
- [[wiki/claims/wiwit-suryanto-google-scholar-profile-metrics]] - Dated Google Scholar profile and citation-metrics snapshot for Wiwit Suryanto.

## Questions

- No durable question pages yet.

## Syntheses

- No synthesis pages yet.

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
