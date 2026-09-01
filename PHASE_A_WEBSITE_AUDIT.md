# Phase A — Final Website Experience Audit

**Status:** Read-only inventory. No site code was changed to produce this document.
**Scope:** Full re-audit of `main` after PR #25 (service/journey architecture) and PR #26 (SEO/AEO/GEO architecture) both merged.
**Method:** CI validation replica + determinism check; static structural audit across all 45 real pages; internal-link graph check; full-page desktop (1440px) and mobile (390px) screenshots across 17 representative page types, plus reduced-motion screenshots on 2 pages; manual visual review of every screenshot.

This is the prerequisite inventory for the roadmap's next PR ("Trust + customer journeys + service refinement"). Per the roadmap, nothing here was changed — findings are reported for review before Phase B work begins.

---

## 0. Screenshot methodology note (read this before the findings below)

Two things showed up repeatedly in the first screenshot pass and turned out to be **test-capture artifacts, not site bugs**. Documenting them here so they aren't mistaken for real defects, and so future audits don't re-chase them:

1. **Cookie-consent banner "overlapping" mid-page content.** The banner is `position: fixed; bottom: 0`. Playwright's `fullPage` screenshot bakes fixed-position elements in at the coordinates they occupy in the *original, unexpanded* viewport, not the true document position — so in the first pass it appeared to float over the Pricing section on every service page. Confirmed by dismissing the banner (`localStorage` consent) before capture: the smudge and the "cut-off" pricing text both disappeared completely, with no other change. Not a real bug — a real visitor scrolling sees the banner correctly pinned to their actual viewport bottom.
2. **A faint white smudge at viewport-centre on first load.** This is `#mouse-glow`, a decorative radial-gradient `<div>` that follows the cursor (`assets/js/main.js` "WHITE MOUSE GLOW" block). Its JS defaults `mouseX/mouseY` to `innerWidth/2, innerHeight/2` until the first real `mousemove` fires — headless Playwright never fires one, so it sits dead-centre of the original viewport, which is exactly where the smudge appeared. Confirmed by reading the source, not by inspection alone. Not a bug — it's inert, working-as-designed decor that a real cursor moves away from immediately.
3. **A one-time `ERR_CONNECTION_RESET` console entry on every page except `/thank-you/`.** Isolated by checking which pages load the Google Fonts stylesheet (`<link href="https://fonts.googleapis.com/css2?...">`) — every page that has it shows the error, `/thank-you/` (the only page without it) doesn't. This is the sandbox's outbound network proxy dropping the external font request; it is a test-environment limitation, not a site defect. Real browsers on real networks fetch Google Fonts normally.
4. **The very first screenshot pass showed several project photos as solid black boxes** on the homepage and `/gallery/`. Root-caused (not assumed) via a targeted script checking `naturalWidth`/`complete` on the actual `<img>` elements: the images use native `loading="lazy"`, and Playwright's `fullPage` composite renders below-the-fold lazy images as black if the page is never scrolled first. Confirmed fixed once a scroll-through step was added before capture. Separately, the very first full run (before switching from Python's single-threaded `http.server` to a concurrent Node `http-server`) also produced real, network-level image load failures under concurrent asset requests — that was a local-server concurrency limit, not a site bug either; switching test servers resolved it. All screenshots referenced below are from the corrected, clean run.

All findings from §1 onward are real, verified against source or rendered output — not artifacts.

---

## 1. Sitewide structural findings (all 45 real pages)

Static HTML audit (`H1` count, heading hierarchy inside `<main>`, image `alt`, duplicate IDs, meta description length, phone/quote CTA presence, form label association) across every real page (redirect stubs excluded):

| Finding | Pages affected | Detail |
|---|---|---|
| Meta description too long (>160 chars) | `/areas` (191), `/areas/london` (162), `/gallery` (165), `/guides/highway-licence-scaffolding` (168), `/guides/scaffolding-cost-essex` (179) | Google typically truncates around 155–160 chars on desktop; these will clip mid-sentence in search results. |
| Heading hierarchy skip | `/guides` | Jumps from `<h1>` straight to `<h3>` (no `<h2>` on the page) — the three guide-card titles are marked up a level too deep. |
| Form input without an associated `<label for>` | `/quote` | The photo-upload input (`Photos (optional)`) has a `<legend>` for context but no direct `<label for="qw-photos">` — a screen-reader user tabbing to that specific control won't get its name announced. |
| Everything else (H1 count, alt text, duplicate IDs, phone/quote CTA presence) | — | Clean across all 45 pages. No missing alt text, no duplicate IDs, no page without a phone or quote CTA. |

These are all small, mechanical fixes — flagged for Phase B, not fixed now per the read-only instruction.

---

## 2. Major finding: the three expansion-tier area pages are running a stale template

`/areas/london/`, `/areas/brentwood/`, `/areas/loughton/` are hand-authored (not generated by `build_site.py`, unlike the 12 core area pages) and have not been kept in sync with several rounds of site evolution. Verified directly against source, not just visually:

| Element | Core area pages (e.g. `/areas/rayleigh/`) | Expansion pages (London/Brentwood/Loughton) |
|---|---|---|
| Header nav | Home · Services · **For Builders** · **Projects** · About · Contact · **01702 820468** · Get a Free Quote | Home · Services · **Gallery** · About · Contact · Get a Free Quote — missing "For Builders", missing the phone number, and still uses the pre-rename "Gallery" label/link instead of "Projects" |
| On-page quote form | Full embedded "Request a Free Quote — [Town]" form | **No `<form>` on the page at all** — the only way to convert is the header/CTA-banner buttons, which route to the generic `/quote` flow with no location context carried over |
| Breadcrumb label | "Home > Areas" | "Home > **Areas Served**" (stale label, predates the `/areas` hub's breadcrumb wording) |
| Footer "Areas We Cover" | All 12 core towns, each linked | **Only 9 entries** (Benfleet, Canvey Island, Rayleigh, Southend-on-Sea, Basildon, Chelmsford, Brentwood, Loughton, London) — missing Wickford, Hadleigh, Leigh-on-Sea, Thundersley, Hockley, Rochford. This is the *pre-fix* footer, from before this session's footer-link fix (`build_site.py`'s `footer()` now iterates the full `AREA_DATA`) — confirming these three pages were never touched by that fix because they sit outside the generator. |
| Visual design | Card-based decision grid, service cards, area pills, dark-theme component system | Plain `<ul>` bullet lists for "Why Choose Axis" and "Areas We Cover", no cards, no pills — visually a different, older design language |
| Footer credit | None | **"Website by MJ AdSystems Ltd"** with a logo — appears only on these 3 pages, nowhere else on the site |

**Why this matters:** these are exactly the pages a London/Brentwood/Loughton searcher lands on. Right now that visitor gets a visibly older, less trustworthy-looking page, has no on-page way to submit a quote request for their specific town, and the page under-represents the company's actual coverage in its own footer. This is a bigger conversion and consistency risk than any single copy or schema issue and should be a leading candidate for Phase B, not treated as a stale expansion tier to leave alone. (This is separate from — and additional to — the already-tracked "unresolved trust claims on the London page" line in `CLAIM_VERIFICATION.md`; that entry covers content claims, not template staleness.)

---

## 3. New claim-verification findings — the 4 PPC landing pages (`/lp/*`)

`CLAIM_VERIFICATION.md`'s existing tiering only ever assessed `/areas/london/`. Reading the four hand-authored landing pages (`emergency-scaffolding-essex`, `scaffolding-rayleigh`, `scaffolding-southend`, `temporary-roofing-essex` — used for paid-search traffic, not linked from primary nav) surfaced claims that tier never covered.

Note on structure first, so it isn't mistaken for a defect: all 4 pages deliberately strip the header down to just a logo (linking home) with no site nav — a standard PPC/CRO pattern to minimize exit points on paid traffic, confirmed by reading the markup. That part is intentional and fine. The claims below are not:

1. **"£5 million public liability coverage" appears on all 4 pages.** Previously only tracked as appearing on the London page. Same OWNER VERIFICATION REQUIRED status applies — needs to be added to `CLAIM_VERIFICATION.md` explicitly for these 4 pages, not just London.
2. **`/lp/emergency-scaffolding-essex/` claims "24/7 Availability… We're Ready 24/7."** This directly contradicts the phrasing used everywhere else on the site ("we aim to attend site or arrange erection as quickly as operatives are available" — see the real `/services/emergency-scaffolding/` FAQ). The roadmap's Phase F instructions explicitly say **"Do not invent response times."** This reads as an invented, unverified availability claim and is the strongest single candidate for removal or rewrite in Phase B/F.
3. **`/lp/scaffolding-southend/` contains a customer testimonial** — *"Emergency call-out within hours when we had storm damage. Ashley was brilliant…" — Robert P., Southend, 5 stars* — **that does not exist anywhere in the site's real `testimonials()` data model** in `build_site.py`. Verified by direct grep; no "Robert P." or matching quote exists. This matches the exact fabrication pattern the earlier session found and removed on the London area page (the fake `AggregateRating` / case studies). It should be treated the same way: DO NOT USE until either the real testimonial is sourced or it's removed.

These findings need to be folded into `CLAIM_VERIFICATION.md` in Phase B before any further work touches the `/lp/*` pages.

---

## 4. Per-page-type visual/UX audit (desktop 1440 + mobile 390, reduced motion where noted)

Grouped by template family since sibling pages (all core area pages, all service pages) share one generator template and behave identically once one is checked.

| Page / template | Purpose | Primary user | Primary CTA | Trust signals | Content quality | UX / visual / mobile / a11y notes |
|---|---|---|---|---|---|---|
| **Home `/`** | Convert cold traffic; route by job type | Homeowner or builder, first visit | "Get a Free Quote" (nav + hero) | CISRS badge, 10+ yrs, £5m insurance line, testimonials, real project photos | Strong — decision grid routes by audience, real photography, FAQ | Clean at both breakpoints and under reduced motion (checked side-by-side — layout identical, only animation suppressed, as intended). No issues found. |
| **Services index `/services`** | Route to the right service page | Any visitor unsure which service | "View Service →" per card | Grouped by audience (Home & Property / Commercial & Trade / Specialist) | Good — the 3-group card taxonomy from PR #25 reads clearly at both breakpoints | Clean. |
| **Service detail (residential/emergency/loading-bay checked)** | Convert a specific-intent visitor | Homeowner/builder who knows their need | "Request a Quote" / phone | Pricing ranges, "How It Works" steps, area pills, CISRS mention | Good, consistent template | `/services/emergency-scaffolding/` and `/services/loading-bay-scaffolding/` have **no "Related Projects" section** — no project photos are tagged to those services yet (matches the "4 of 9 services have zero tagged project photos" gap already flagged in PR #25's audit). Not a bug, a content gap: worth prioritising real photos for these two before Phase B ships, since every other service page uses real photography as a trust signal and these two visibly don't. |
| **Gallery/Projects `/gallery`** | Prove real work exists | Skeptical visitor comparing suppliers | "Get a Free Quote" | 14 real, geotagged photos, category filter | Strong — explicitly "no stock imagery" | Clean at both breakpoints once the concurrency artifact (§0) is excluded. |
| **Areas hub `/areas`** | Route to a specific town page | Visitor checking coverage | "View All Services" / phone | All 12 towns, real pills | Clean, simple | Clean. |
| **Core area pages (Rayleigh, Hockley checked)** | Convert a local searcher | Homeowner/builder in that specific town | Embedded quote form | Local housing-stock detail, access notes, nearby-areas cross-links | Strong — genuinely town-specific copy, not templated filler | Clean at both breakpoints. |
| **Expansion area pages (London checked; Brentwood/Loughton confirmed by source to match)** | Convert a London/Brentwood/Loughton searcher | Same as above but outside core area | Header/CTA-banner buttons only | £5m insurance, CISRS, review count claim | Text itself is reasonably well-written | **See §2 — major template-staleness finding.** This is the worst-performing page family on UX/trust/mobile-consistency grounds of anything audited. |
| **Guides hub `/guides` + guide detail** | Answer pre-purchase questions, build AEO trust | Early-stage researcher | "Request a Free Quote" / "Read Guide" | Real Essex pricing ranges, plain-English structure | Good | `/guides` has the heading-hierarchy skip noted in §1; otherwise clean. |
| **Contractors `/contractors`** | Convert trade/B2B visitors | Builder, roofer, developer | "Send an Enquiry" / phone | RAMS, CISRS, trade-account framing | Good, distinct value prop from homeowner pages | Clean. |
| **About `/about`** | Humanise the brand, found trust | Any visitor doing due diligence | "Get a Free Quote" | Ashley's real photo, testimonial quote, company number | Founder identity intact and correctly preserved | Clean. Minor: large empty vertical space below the photo on desktop where the copy block is shorter than the image — cosmetic only. |
| **Contact `/contact`** | Low-friction contact | Visitor ready to reach out | Quote form | Phone, email, address, company number | Clean, direct | The left "Contact Us" info card is visibly shorter than the form card beside it, leaving a large empty block on desktop — minor visual balance issue, not a functional one. |
| **Quote `/quote`** (6-step wizard) | Structured lead capture | Visitor ready to convert | "Continue" / "Get My Free Quote" | Step count shown, response-time promise | Well-structured, low-pressure step 1 | Missing-label finding from §1 (step 5, photo upload) is the one real accessibility gap. Mobile stacking of the 11 project-type buttons is clean and thumb-friendly. |
| **Thank-you `/thank-you`** | Confirm submission, prevent drop-off | Just-converted visitor | "Back to Home" / "View Our Services" | 24-hour response promise | Simple, clear | Clean. Only page without the Google Fonts request (uses system fonts) — not a defect, just worth knowing before treating "no font request" as unusual. |

---

## 5. What Phase A deliberately did not touch

- Google Search Console and Google Ads data: untouched, exactly as instructed. No query-level, CTR, or spend analysis performed or referenced in this document.
- No site code, copy, schema, or CSS was modified as part of producing this audit.
- The `/lp/*` findings (§3) are reported, not fixed — the fabricated testimonial and the "24/7" claim are both real problems, but fixing them is content/trust work that belongs to Phase B (or Phase F, per the roadmap's own phase split), not this inventory step.
- The expansion-tier template staleness (§2) is reported, not fixed, for the same reason — it's a real, sizeable piece of work (rebuild 3 pages onto the current template + embedded quote forms), not a one-line patch.

---

## 6. Suggested priority order for Phase B, based on this audit

1. **Expansion-tier area pages (§2)** — highest combined impact: trust, conversion (no quote form), and consistency, and it's currently costing paid/organic traffic on 3 real, live URLs.
2. **`/lp/*` claim fixes (§3)** — the fabricated testimonial and unverified "24/7" claim are direct violations of the project's own no-fabrication rule and should be fast to fix.
3. **Mechanical fixes from §1** — meta description lengths, `/guides` heading skip, `/quote` label — all small, low-risk, high-clarity wins.
4. **Real photography for emergency/loading-bay service pages** — closes the "Related Projects" gap noted in the service-detail row of §4.
