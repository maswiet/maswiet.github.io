# Academic Site Pages

## Request

Create Design Samples for all core pages of the academic site (homepage/landing,
publications, research portfolio, teaching/lectures) using the elegant-minimalist
Design System.

## Design System

- Name: Elegant minimalist
- Path: `.design/design-system/elegant-minimalist`

The system's tokens, layout model, and prose guidance are the source of truth.
This sample applies them; it does not introduce new design decisions.

## Generated Files

| File | Description |
|------|-------------|
| `index.html` | Homepage / landing — identity rail, hero statement, selected-research highlights, research-availability callout. |
| `research.html` | Research portfolio — bordered editorial research entries (role, period, collaborators, abstract, outputs) grouped by active/recent. |
| `publications.html` | Publications — citation-forward rows with year, bold self-author, italic venue, and DOI/PDF/Data links, plus topic filter tags. |
| `teaching.html` | Teaching / lectures — office-hours callout, course groups with lecture rows, and a weekly schedule table. |
| `styles.css` | Shared stylesheet. All colors, typography, spacing, and radius values are transcribed directly from `DESIGN.md` tokens (CSS custom properties). |

All four pages share the same editorial two-column layout: a sticky identity rail
(name, affiliation, primary nav, contact) plus a wider main reading column capped
near the 760px content width, inside the 1180px site width.

## How the Design System is applied

- **Colors:** warm paper `#F8F6F1` page, white surfaces, deep charcoal text,
  volcanic-red `#8A2D1F` accent used sparingly (active nav, one primary button,
  links, publication year, focus rings). Mineral teal `#2F5D62` used only for
  quiet support cues (eyebrows, callout border) so it never competes with the
  accent for calls to action.
- **Typography:** Source Serif 4 for headlines, ledes, and long-form voice;
  Inter for nav, labels, metadata, tables, and utility text. Fixed type levels,
  `0px` letter-spacing.
- **Layout & spacing:** 4/8px rhythm, `96px` between major sections, editorial
  rail + reading column rather than a dashboard/card grid.
- **Elevation & shapes:** flat hierarchy via borders, whitespace, and tonal
  `surface-muted` bands; no shadows on content modules; square/`4px`/`6px`
  radii with `full` pills reserved for tags.
- **Accessibility:** active navigation carries a non-color cue (left border +
  weight on desktop, bottom border on mobile); links underline on hover; visible
  focus outlines; charcoal-on-paper text meets WCAG AA.

## Open / Run

These are standalone static files. Either:

- Open `index.html` directly in a browser (navigation between the four pages
  works via relative links), or
- Serve the folder and browse `http://localhost:4599/`:

  ```sh
  python3 -m http.server 4599 \
    --directory .design/design-system/elegant-minimalist/outputs/academic-site-pages
  ```

Fonts load from Google Fonts; with no network the pages fall back to Georgia /
system sans, preserving layout and hierarchy.

A ready-to-use preview config was added at `.claude/launch.json`
(server name `design-sample-academic-pages`).

## Verification

Rendered and visually checked with the Launch preview (Chromium) at 1280px
desktop and 375px mobile:

- **Homepage** — rail, hero, highlights, and callout render as intended; accent
  used only on active nav, primary button, and links. ✓
- **Publications** — citation rows scan cleanly; year in accent, self-author
  bold, venue italic. ✓
- **Research** — bordered research entries with meta, tags, abstract, and
  outputs divider. ✓
- **Teaching** — office-hours callout (teal rule), course groups, lecture rows,
  and schedule table. ✓
- **Responsive** — at 375px all pages collapse to a single column and the nav
  becomes a horizontal row with an underline active cue; display type scales
  from 56px → 40px. ✓

## Gaps / Notes

- **Illustrative content.** Names of co-authors, titles, DOIs, course codes,
  venues, room numbers, and dates are plausible placeholders for demonstration,
  not verified bibliographic or scheduling data. Replace with real content
  before any production use.
- **Links** (CV, DOI, PDF, ORCID, Scholar, slides) are `#` placeholders.
- No live-site source code was modified. The only file created outside the
  sample folder is `.claude/launch.json` (a local preview convenience).
- Static preview images were not saved to the folder; verification was performed
  live via the preview tool and is summarized above.

## Metadata

- Created: 2026-07-01T00:00:00Z
