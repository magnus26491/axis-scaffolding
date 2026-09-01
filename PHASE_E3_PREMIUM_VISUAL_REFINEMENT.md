# Phase E3 — Premium Visual System & Customer Experience Refinement

**Status: execution refinement only.** The information architecture established in Phase E is unchanged — this phase asks whether the site's execution looks as considered as that architecture now is, and fixes only what genuinely didn't.

## 1. Live-site audit summary

Crawled the live deployment (`https://www.axisscaffoldingessex.co.uk/`) first, before touching any code, per the brief's explicit instruction. Hit a real environment constraint doing it with a full browser: this session's outbound proxy closes the HTTPS tunnel to any external host after ~6 seconds mid-exchange (confirmed from the proxy's own diagnostics, and confirmed **not specific to this site** — `www.google.com` shows the identical failure pattern in the same window). A full Chromium page load holds the tunnel open longer than that, so live-browser screenshots failed outright; quick, single-request `curl` calls to the same host succeeded repeatedly and reliably.

Given that, live verification was done the way that constraint actually allows:
- `curl` against the live site for every priority page (homepage, gallery, 3 service pages, about, contractors) — headers, redirect behaviour, and full HTML fetched directly.
- Full-page **visual** audit run against a local rebuild instead, after first proving that rebuild is a faithful stand-in — see §2.

## 2. Repository vs. live comparison

Diffed live-fetched HTML against the local build byte-for-byte for `/services/residential-scaffolding/`, `/quote/`, `/about`, `/contractors/`, and `/gallery` — **all five were byte-identical**. The live `Last-Modified` header (01 Sep 2026 21:22:36 GMT) matches the Phase E deploy exactly; PRs #34 and #35 since then were both docs-only with zero generated-HTML changes, so the live site was already known to be current before this phase started. On that basis, the local rebuild was used for the full visual audit (§3) as a proven-equivalent substitute for a live browser crawl, not a guess.

Two things checked directly on the live site, both **clean**:
- **The "5.0 Google Reviews" claim you flagged from a search-engine crawl result does not exist anywhere in the current live HTML** — confirmed by fetching the live homepage directly and searching for every variant of that phrase. This is exactly the stale-external-index case the brief warned against "fixing" — nothing was touched, because the live source is already correct (Phase B already removed this claim; the crawl result you saw was a cached snapshot from before that).
- Phone links, canonical tag, and old-domain absence all correct on the live homepage.

One incidental, pre-existing technical observation (not a regression, not acted on — out of scope for this phase): GitHub Pages 301-redirects `/services`, `/quote`, and `/contractors` (no trailing slash) to their trailing-slash form, while `/about` and `/gallery` resolve directly at 200. This is because `about.html`/`gallery.html` legacy stub files exist at the root (serving those bare paths directly) while `services`/`quote`/`contractors` have no such stub, so GitHub Pages' standard directory-index redirect applies. Unrelated to any recent phase; flagged for completeness only.

## 3. Visual issues found (material, not manufactured)

Screenshotted the local rebuild — proven identical to live (§2) — across homepage, gallery, 3 service pages (one with photos, one without, one with only a single tagged photo), about, and a filtered gallery state, at both 1440px and 375px. Applying the brief's own test ("does this look like a premium scaffolding company with real work behind it?") surfaced three real, material issues, all inside the priority areas you named:

1. **Service pages had zero photography until the very bottom of the page.** `service_detail_body()` is six stacked text sections (Who Is This For → What's Included → Pricing → How It Works → FAQ) before a single image appears — exactly the "Hero → cards → cards → cards → CTA" pattern named in the brief. Real, genuine project photos exist for 5 of the 9 services and were being held back until "Related Projects," near the very end.
2. **The gallery's "Full Portfolio" section was a uniform wall of 13 identical cards.** The page's own "Featured Project" treatment above it is already good (large image, editorial caption) — the portfolio grid directly below it reverted straight back to a flat 3-column grid with no visual rhythm, undercutting the exact editorial quality the featured section had just established.
3. **The About page stopped short of its own stated arc.** It correctly opens on "real person" (Ashley's photo and story) and "real company" (CISRS, insurance, incorporation), but jumped straight from there to a generic "Areas We Work In" pill list — never completing "real work." The genuine project photography used everywhere else on the site wasn't used here at all.

## 4. What was intentionally left unchanged

- **Hero parallax and the homepage split-image parallax** (Phase E) — already correctly implemented, already reduced-motion-safe, already desktop-only. Re-verified, not rebuilt.
- **The quote wizard** — reviewed against the brief's own psychology test ("tell us about your job" vs. "complete an application"). It already reads that way: a visible step-progress indicator, a restrained glass-card treatment reserved specifically for this form (not overused site-wide), clear choice-cards with proper hover/checked/focus states, one primary CTA. No material issue found — **investigated, no change made**, rather than inventing a reason to touch it.
- **Global design-system consistency** (typography scale, spacing rhythm, button geometry, dark/light section rhythm, silver accent usage) — spot-checked across every screenshot taken this phase; found consistent. No sitewide token or component changes made.
- **The 4 services without tagged project photos** (emergency, dismantling, loading-bay, supply-erection) — confirmed still genuinely absent from `PROJECTS`. Per the brief's explicit instruction, no imagery was invented or borrowed from an unrelated service for these; their pages keep the plain-text "Who Is This For?" section rather than a fabricated split-grid.
- **Mobile navigation, header, footer** — reviewed in every mobile screenshot taken this phase, no issue found.

## 5–8. Exact changes made

All three are the same underlying move — **reuse existing, genuine photography earlier and with more visual weight, using patterns the site already has** (the split-grid already proven on the homepage's "For Builders & Roofers" section, and the same editorial-card language already established for the homepage's "Recent Projects" section in Phase E) rather than inventing a new visual language.

**Service pages** (`services/{residential,commercial,domestic,roof,temporary-roofing}`): the "Who Is This For?" section is now a split-grid — proposition text on one side, that service's own first tagged project photo on the other — for the 5 services that have one. This collapses "Hero → proposition → imagery → who it's for" into one composition instead of a wall of stacked text sections. The "Related Projects" section further down now shows the *remaining* tagged photos (not a repeat of the one just featured above) — confirmed directly in the generated output that no photo appears twice on the same page. The 4 services without tagged photos are unchanged (plain text, no fabricated imagery), and this was verified explicitly in the generated output, not assumed.

**Projects/gallery** (`/gallery`): the "Full Portfolio" grid now gets a periodic wide tile (every 5th card, `nth-child(5n+1)`) at a 16:9 aspect ratio, using `grid-auto-flow: dense` so the layout still packs cleanly under the existing category filter — verified directly by filtering to "Commercial" (2 items) and confirming no gaps or orphaned spans. Collapses back to a single column on mobile, matching the rest of the grid. A one-line, purely descriptive intro sentence was added under "The Full Portfolio" heading (no new claims).

**About page**: a new "Real Work, Not a Brochure" section sits between the founder story and "Areas We Work In," showing 3 genuine tagged project photos (Southend, Rayleigh, Leigh-on-Sea — deliberately different towns/categories than the ones already featured on the homepage and gallery) using the same editorial project-card treatment as the rest of the site. This completes the "real person → real company → real work → real standards" arc the brief described, which the page previously stopped short of.

## 9. Quote UX improvements

None made — see §4. Investigated against the brief's own criteria and found no material issue.

## 10. Mobile checks

All changed pages re-screenshotted at 375×812. The service-page split-grid collapses to a single column in the correct document order (proposition text, then photo) — this was checked twice: once via a screenshot that initially looked like the heading text was missing (it wasn't — a mis-cropped verification image on my end, corrected and re-confirmed both by direct `getBoundingClientRect()` inspection and a correctly-cropped screenshot showing the heading exactly where the DOM says it is). The gallery's wide-tile treatment correctly reverts to single-column on mobile (media query at 900px). No horizontal overflow, no console/page errors, on any changed page at mobile width.

## 11. Accessibility checks

- All new `<img>` tags carry descriptive `alt` text following the site's existing pattern (`"{label} in {location}, Essex — real Axis Scaffolding project photograph"`), correct `width`/`height` (no CLS), `loading="lazy"`, and responsive `srcset` via the same `_project_srcset()` helper already used everywhere else.
- Heading hierarchy re-verified on every changed page (`about/index.html`, `gallery/index.html`, all 5 changed service pages): h1 → h2 → h3, no skips.
- No new interactive elements were added (the new sections are photos and text only), so no new focus-state or keyboard-nav surface was introduced.

## 12. Performance checks

- No new JavaScript. No new library or animation code — the gallery grid change is CSS-only (`grid-auto-flow: dense` + `nth-child`), and the split-grid image reuses the site's existing responsive-image pipeline (same `srcset`, same lazy-loading, same file sizes already generated and in use elsewhere on the site for the same photos).
- Deterministic rebuild confirmed (sha256 identical across 2 consecutive builds) — no drift.

## 13. Trust / claim verification

- Zero new claims of any kind. Every new section either reuses existing copy verbatim (`who_for` text on service pages, unchanged) or adds only structurally descriptive text ("Every completed job, filterable by type," "A small sample of completed jobs — the same real photography featured across this site, no stock imagery") — no statistics, ratings, response-time claims, or credentials.
- The £5m insurance claim was not touched or referenced anywhere in this phase.
- `python3 scripts/check_testimonials.py` passes unchanged — no testimonial content was touched.
- Confirmed directly (§2) that the live site does not currently show the stale "5.0 Google Reviews" claim you flagged — nothing needed fixing there.

## 14. Build/test results

- `python3 build_site.py` + `python3 scripts/seo_postprocess.py` — clean.
- `python3 scripts/check_testimonials.py` — passes.
- CI validation script replica (verbatim from `.github/workflows/pages.yml`) — passed.
- `node -c assets/js/main.js` — clean (no JS changed this phase, checked anyway).
- Deterministic rebuild (sha256 across 2 consecutive builds) — identical output.
- Site-wide duplicate element-ID check — none found.
- Heading hierarchy re-verified on every changed page — no skips.
- Diff scope: 9 files changed (`build_site.py`, `assets/css/style.css`, `about/index.html`, `gallery/index.html`, and the 5 service pages with tagged photos) — nothing outside the areas this phase targeted.

## Summary table

| Area | Outcome |
|---|---|
| Live-site verification | **FIXED** nothing (nothing was broken) — confirmed live matches source, confirmed the "5.0 Google Reviews" claim is stale external indexing, not a live defect |
| Service pages — photography position | **FIXED** — real photo moved into an early split-grid for the 5 services that have one |
| Gallery — Full Portfolio grid rhythm | **FIXED** — periodic wide tile, verified stable under filtering |
| About page — "real work" gap | **FIXED** — new section bridges founder story to genuine project photos |
| Hero / homepage split-image parallax | **INVESTIGATED / NO CHANGE REQUIRED** — already correct |
| Quote wizard visual psychology | **INVESTIGATED / NO CHANGE REQUIRED** — already reads as "tell us about your job" |
| Global design-system consistency | **INVESTIGATED / NO CHANGE REQUIRED** — spot-checked, consistent |
| 4 services without tagged photos | **OWNER INPUT REQUIRED** — genuine photography is the only real fix; nothing invented |
| GitHub Pages trailing-slash redirect quirk | **OWNER INPUT REQUIRED** (low priority) — pre-existing, harmless, out of scope for this phase |
