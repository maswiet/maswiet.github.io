---
title: "Google Scholar profile for Wiwit Suryanto raw capture"
type: raw-provenance
created: 2026-07-01
---

# Provenance

- Requested URL: https://scholar.google.com/citations?user=9lJKKt0AAAAJ&hl=en
- Final URL: https://scholar.google.com/citations?user=9lJKKt0AAAAJ&hl=en
- Retrieval date: 2026-07-01
- Capture method: `curl -L --compressed` with a desktop browser user agent.
- HTTP result: 200 OK for the main profile page.
- Captured files:
  - `headers.txt` - Main profile response headers.
  - `page.html` - Main Google Scholar profile HTML, including profile metadata, metrics, and articles 1-20 sorted by citation count.
  - `list-works-headers.txt` - Response headers for the public list-works request.
  - `list-works.html` - Public list-works request with `view_op=list_works&sortby=pubdate&pagesize=100`, showing articles 1-100.
- Access limitations: The profile was accessible, but the captured pages include "The system can't perform the operation now. Try again later." around the show-more flow. The raw capture should be treated as a dated partial snapshot, not a guaranteed full publication corpus.

