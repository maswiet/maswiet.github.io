---
version: alpha
name: "Elegant minimalist"
description: "A restrained personal academic website system for research, teaching, and professional credibility."
colors:
  page: "#F8F6F1"
  surface: "#FFFFFF"
  surface-muted: "#F1EEE7"
  text: "#1F1F1B"
  text-muted: "#5F625C"
  border: "#D8D2C5"
  accent: "#8A2D1F"
  accent-hover: "#6F2117"
  on-accent: "#FFFFFF"
  support: "#2F5D62"
typography:
  display:
    fontFamily: Source Serif 4
    fontSize: 56px
    fontWeight: 600
    lineHeight: 1.05
    letterSpacing: 0px
  headline-lg:
    fontFamily: Source Serif 4
    fontSize: 40px
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: 0px
  headline-md:
    fontFamily: Source Serif 4
    fontSize: 30px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0px
  title-md:
    fontFamily: Inter
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0px
  body-lg:
    fontFamily: Source Serif 4
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1.65
    letterSpacing: 0px
  body-md:
    fontFamily: Source Serif 4
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.7
    letterSpacing: 0px
  body-sm:
    fontFamily: Inter
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0px
  label-lg:
    fontFamily: Inter
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0px
  label-md:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0px
  label-sm:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0px
  caption:
    fontFamily: Inter
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0px
rounded:
  none: 0px
  sm: 4px
  md: 6px
  full: 9999px
spacing:
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 32px
  xxl: 48px
  section: 96px
  mobile-margin: 20px
  page-margin: 32px
  rail-width: 260px
  content-width: 760px
  site-width: 1180px
components:
  nav-link:
    textColor: "{colors.text-muted}"
    typography: "{typography.label-md}"
    padding: 8px
  nav-link-active:
    textColor: "{colors.accent}"
    typography: "{typography.label-md}"
    padding: 8px
  button-primary:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-accent}"
    typography: "{typography.label-lg}"
    rounded: "{rounded.sm}"
    padding: "12px 16px"
  button-primary-hover:
    backgroundColor: "{colors.accent-hover}"
    textColor: "{colors.on-accent}"
  button-secondary:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.text}"
    typography: "{typography.label-lg}"
    rounded: "{rounded.sm}"
    padding: "12px 16px"
  research-entry:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.text}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 24px
  lecture-row:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.text}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: "16px 0px"
  tag:
    backgroundColor: "{colors.surface-muted}"
    textColor: "{colors.text-muted}"
    typography: "{typography.label-sm}"
    rounded: "{rounded.full}"
    padding: "4px 8px"
  callout:
    backgroundColor: "{colors.surface-muted}"
    textColor: "{colors.text}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 24px
---

## Overview

Elegant minimalist is the Design System for Wiwit Suryanto's personal academic website. The site should support personal branding, research portfolio material, and lecture-related content for the Geophysics UGM context.

The visual language should feel restrained, credible, and refined rather than promotional. It should help visitors quickly understand Wiwit's academic identity, research focus, and teaching role without overwhelming the content.

Audience priority is academic peers and potential research collaborators first, Geophysics UGM students second, and broader personal-brand visitors third. The design should therefore lead with evidence, clarity, and intellectual calm, while keeping lecture material discoverable and approachable.

The platform baseline is desktop-first credibility with fully responsive mobile support. Interfaces must meet WCAG AA contrast for normal text, preserve comfortable reading for long-form academic material, avoid tiny footnote-like UI, and never rely on color alone to communicate meaning.

## Colors

The palette uses warm paper neutrals, deep charcoal text, and one restrained geophysics-inspired interactive accent. It should feel academic, calm, and editorial, not decorative or promotional.

- **Page (#F8F6F1):** A warm paper background for the full site, used to soften long reading sessions without drifting into a beige-heavy theme.
- **Surface (#FFFFFF):** A clean content surface for articles, research summaries, lecture blocks, and navigation areas.
- **Surface Muted (#F1EEE7):** A subtle tonal layer for secondary bands, callouts, and quiet metadata groupings.
- **Text (#1F1F1B):** Deep charcoal for primary text, headings, and essential interface copy.
- **Text Muted (#5F625C):** Reserved for dates, captions, affiliations, abstracts, and secondary labels.
- **Border (#D8D2C5):** A soft stone divider for rules, cards, tables, and input outlines.
- **Accent (#8A2D1F):** A deep volcanic red used sparingly for links, active navigation, focused states, and the single primary action on a page.
- **Accent Hover (#6F2117):** The stronger interaction state for accent elements.
- **On Accent (#FFFFFF):** Text or icon color placed on accent fills.
- **Support (#2F5D62):** A mineral teal support color for diagrams, badges, or informational highlights. It should not compete with the accent for calls to action.

All text and interactive color pairings must meet WCAG AA contrast. Color must be paired with text, iconography, underline, border, or layout treatment whenever it communicates state or meaning.

## Typography

Typography uses **Source Serif 4** for the academic voice and **Inter** for interface clarity. Source Serif 4 should carry headlines, research introductions, abstracts, essays, and long-form lecture notes. Inter should carry navigation, buttons, metadata, labels, compact lists, tables, and utility text.

The system should feel like a careful academic publication translated into a modern website. Use fixed typography levels rather than viewport-scaled text. Keep letter spacing at `0px`; elegance should come from proportion, whitespace, and font choice rather than tight tracking.

- **Display:** Large first-viewport identity statements and major page openings.
- **Headline Large:** Section headers for research, teaching, publications, and profile pages.
- **Headline Medium:** Subsection headers and article headings.
- **Title Medium:** Card titles, lecture titles, publication names, and compact page modules.
- **Body Large:** Introductory paragraphs and page summaries that need editorial presence.
- **Body Medium:** Default long-form reading text.
- **Body Small:** Dense supporting copy, tables, lists, and short descriptions.
- **Labels:** Navigation, actions, filters, metadata labels, and form text.
- **Caption:** Dates, affiliations, figure captions, and source notes.

## Layout & Spacing

The layout uses an editorial two-column model on desktop: a narrow identity rail for name, affiliation, primary navigation, and contact context, paired with a wider main column for research, teaching, publications, and writing. On mobile, the layout collapses to a single column with navigation at the top.

The desktop site width should max out at `1180px`, with a `260px` rail and a main content column that keeps long-form reading near `760px`. The design should feel spacious and scholarly, not dashboard-like. Avoid dense card grids as the default composition; use lists, section bands, excerpts, and measured whitespace to make academic content scan well.

Spacing follows a restrained 4px/8px-based rhythm. Use `96px` between major page sections on desktop, `48px` for large internal groupings, `24px` to `32px` inside content modules, and `16px` or less only for tightly related labels, metadata, and controls.

## Elevation & Depth

Hierarchy is mostly flat. Use whitespace, typography, borders, and tonal background layers to separate content instead of defaulting to shadows.

Normal content modules, research entries, lecture lists, publication groups, and profile sections should sit flat on `surface` or `page` with `border` dividers when needed. The `surface-muted` color may be used for quiet section bands or callouts.

Shadows are reserved for temporary overlays such as menus, popovers, and modals. When used, they must be extremely subtle: soft, low-opacity, and secondary to the border treatment.

## Shapes

The shape language is mostly square and softly corrected. Page structure, dividers, section bands, and large editorial regions should use `0px` radius. Buttons, inputs, and small controls use `4px`. Content modules may use `6px` when a contained treatment is needed. Fully rounded shapes are only for small pills, tags, avatars, or compact status markers.

Icons should be simple line icons with consistent optical stroke weight. Avoid playful blobs, oversized rounded containers, and heavily rounded card systems; the site should feel precise, scholarly, and composed.

## Components

Components should be text-led academic components, not decorative marketing blocks. They should rely on typography, borders, spacing, and restrained color to make research and teaching content easy to scan.

- **Navigation:** Use understated Inter labels. Default links use muted text; active links use the accent and should also have a non-color cue such as underline, border, or position.
- **Buttons:** Use primary buttons sparingly for the most important action on a page, such as contacting Wiwit or opening a curriculum vitae. Secondary buttons remain white with a border and charcoal text.
- **Research Entries:** Present research projects as bordered editorial entries with clear title, role, timeframe, collaborators, short abstract, and related outputs. Avoid image-heavy project cards unless the visual evidence is genuinely useful.
- **Publication Entries:** Use citation-forward rows or blocks. Title, authorship, venue, year, and links should be easy to scan. The visual weight should privilege the publication title and year.
- **Lecture Rows:** Treat lectures and course material as ordered rows or sectioned lists, optimized for repeat access by students.
- **Tags:** Use small rounded pills only for metadata such as topic, method, course, year, or research area. Tags must stay secondary and should not dominate the layout.
- **Callouts:** Use quiet tonal callouts for important academic context, office-hour notes, research availability, or selected teaching guidance.
- **Tables:** Use minimal borders, generous row spacing, and Inter body text for datasets, schedules, reading lists, or publication metadata.
- **Forms:** Keep labels visible, inputs square-cornered, focus states clear, and errors explicit in text as well as color.

## Do's and Don'ts

- Do lead with academic credibility, research evidence, and clear affiliation.
- Do use the accent only for active navigation, important links, focus states, or one primary action per view.
- Do keep long-form research and lecture text readable with generous line height and content width.
- Do use borders, whitespace, and typography before adding visual decoration.
- Do make lecture material easy for students to find without making the whole site feel like a course portal.
- Don't use oversized marketing hero cards, decorative gradients, or ornamental backgrounds.
- Don't build dense card grids as the default research or publication layout.
- Don't use shadows for ordinary content modules.
- Don't rely on color alone for state, hierarchy, or meaning.
- Don't let personal branding become self-promotional; the tone should remain calm, precise, and academically credible.
