# Phase C — Final Customer Experience, Conversion & Production Polish Audit

**Status:** Production-polish pass over the merged Phase A + Phase B baseline. One concrete fix applied. This is deliberately not a redesign — per the phase brief, only genuine, material issues are fixed.
**Scope boundary respected:** no work started on Google Search Console, Google Ads, or `AXIS_SEARCH_INTELLIGENCE_MAP.md` — all explicitly deferred to the next phase.

## Method

- Fresh full-page screenshots of 31 representative pages (all 9 service pages, all 3 expansion + 2 core area pages, the areas hub, all 3 guides + hub, contractors, about, contact, quote, thank-you, gallery, home, and all 4 PPC landing pages) at desktop (1440px) and a realistic mobile width (375×812, iPhone-class — not a generic breakpoint), with a script-level check for horizontal overflow on every page.
- A structural audit across all 45 real pages (heading hierarchy, alt text, duplicate IDs, meta description length, form labels, CTA density).
- A cross-page trust-consistency check (phone number formats, the £5m insurance claim's exact page scope, JSON-LD validity, internal link graph).
- Manual visual review of every screenshot against the brief's four customer-journey personas and the "does this still feel AI-template-assembled" checklist.
- Two suspected visual bugs were investigated with direct Playwright verification (bounding boxes / computed styles) rather than judged from a screenshot alone — see §3.

## 1. What this audit found already working well (verified, not assumed)

- **Service pages are genuinely differentiated**, not templated copy with nouns swapped. Checked directly against `SERVICE_DETAIL` in `build_site.py`: pricing figures, "What's Included" checklist items, FAQ questions, and process-step count/wording all differ meaningfully between e.g. residential, commercial, and dismantling — commercial's pricing paragraph talks about programme/documentation requirements, dismantling's talks about third-party scaffold removal; these are not reworded duplicates.
- **Zero console/page errors and zero horizontal overflow** across all 31 pages × 2 viewports (62 checks) in the fresh screenshot pass.
- **Zero broken internal links, zero invalid JSON-LD, zero duplicate element IDs** across all 45 real pages (structural audit).
- **GA4 analytics loader is safe with no real measurement ID**: `GA4_MEASUREMENT_ID = None` in `build_site.py`; `main.js`'s loader (`if (!window.AXIS_GA4_ID || ...) return;`) correctly no-ops rather than attempting to load `gtag.js` with a null/placeholder ID. No ID was invented for this phase.
- **The £5m insurance claim's scope is unchanged and correctly isolated** to the 5 pages already tracked in `CLAIM_VERIFICATION.md` (London + the 4 LP pages) — confirmed by a precise grep for the actual claim phrase (not a naive "£5" substring match, which would have false-positived on every price range like "£500–£800" on the site).
- **Testimonial integrity check (from PR #29) still passes** and was not touched.
- **FAQ content reviewed for duplication**: the homepage's 8-question general FAQ (`FAQS`) and each service page's own FAQ are thematically related (both may touch on cost or licensing) but are separately worded, separately scoped, and never shown on the same page together — this is normal, appropriate FAQ design for a site with both a general and a service-specific FAQ layer, not the "duplication" the brief was concerned about.

## 2. The one concrete fix made in this phase

**Phone number format inconsistency on all 4 `/lp/*` PPC landing pages.** Every `tel:` link on these pages used the bare national format (`tel:01702820468`), while every other page on the site — generated via `nav()`/`footer()` — consistently uses the E.164 format (`tel:+441702820468`, from `NAP['phone_e164']`). Both formats work as phone links, but this was a real, measurable cross-page inconsistency, squarely inside this phase's explicit "phone number... consistency" check. Normalised all 13 occurrences across the 4 files to match the site-wide convention. Already committed and pushed ahead of this document (`e4ee29a`).

## 3. Two suspected issues investigated and ruled out (documented so they aren't re-flagged later)

1. **The guide page's 6-card "Jobs That Typically Require Scaffolding" grid** appeared, in a scaled-down screenshot, to leave a 6th card stranded at the left edge of its own row (a 5-then-1 layout). Checked directly via `getBoundingClientRect()` on the live page: the 6th card's centre (x=720) exactly matches the container's centre (720), confirming the grid's documented `justify-content:center` behaviour for an incomplete trailing row is working exactly as designed (see the design comment at `build_site.py`'s `.decision-grid` CSS). Not a bug — no change made.
2. **The `/lp/*` pages' fixed mobile bottom bar** ("Call Now / Get Free Quote") appeared, in a full-page screenshot, to float awkwardly mid-page rather than at the bottom. Checked directly via computed style + bounding rect at scroll position 0 and after scrolling 1500px: `position: fixed; bottom: 0px` in both cases, rect unchanged — it is genuinely, correctly pinned to the viewport bottom during real scrolling. The screenshot artifact is the same category of Playwright `fullPage`-capture behaviour for fixed-position elements documented in `PHASE_A_WEBSITE_AUDIT.md` §0. Not a bug — no change made. (This bar exists only on the 4 LP pages, which is an intentional, accepted PPC-landing-page pattern per the Phase A audit — stripped nav, persistent sticky CTA — not a site-wide consistency violation, since these pages are deliberately outside the main site chrome.)

## 4. Known, already-documented gap — not fabricated, not fixed here

4 of the 9 services (`emergency-scaffolding`, `dismantling-scaffolding`, `loading-bay-scaffolding`, `scaffold-supply-erection`) have zero real project photos tagged in `PROJECTS`, so their service pages have no "Related Projects" section — confirmed still the case by re-counting `service_slug` tags in `build_site.py`. This was already known from the Phase 6/Phase A audits. Per this phase's explicit "never invent projects" rule, nothing was fabricated to fill this gap. It remains an owner-input item: real photography of these 4 service types, when available, would let those pages gain the same evidence section the other 5 already have.

## 5. Genuine issues that cannot safely be fixed without owner input

- The £5m insurance figure (5 pages) remains OWNER VERIFICATION REQUIRED, unchanged.
- The 4 services without tagged project photos (§4) — needs real photography from the business, not invented content.
- TG20:21 / CDM / Section 169 claims on the London page — unchanged, out of scope, tracked since Phase 7.

## 6. Validation performed

- `python3 build_site.py` + `python3 scripts/seo_postprocess.py` — clean, no drift.
- `python3 scripts/check_testimonials.py` — passes (4 approved testimonials, `APPROVED_RATING=None`).
- CI validation script replica (verbatim from `.github/workflows/pages.yml`) — passed.
- Deterministic rebuild (sha256 comparison across 2 consecutive builds) — no drift.
- `node -c assets/js/main.js` — clean.
- Full screenshot audit: 31 pages × 2 viewports (desktop 1440px, mobile 375×812) — 0 console/page errors, 0 horizontal overflow.
- Structural audit: 0 duplicate IDs, 0 broken internal links, 0 invalid JSON-LD, 0 missing alt text, 0 heading-hierarchy skips across all 45 real pages.
- Mobile quote flow and mobile navigation spot-checked visually — thumb-sized buttons, no cramping, no overflow.

## 7. Confirmation

No Google Search Console work, no Google Ads work, and no `AXIS_SEARCH_INTELLIGENCE_MAP.md` work was started in this phase. The site is now ready to be judged as a finished baseline before that phase begins, whenever requested.
