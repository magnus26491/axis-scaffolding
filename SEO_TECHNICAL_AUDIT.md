# Axis Scaffolding — SEO / AEO / GEO Technical Audit

Durable reference document for Phase 7 (SEO + Local SEO + AEO + GEO
Architecture). Like `ALIGNMENT_SYSTEM.md` and `CLAIM_VERIFICATION.md`, this
is not a published page — it's the working forensic record that gates
future search-architecture decisions. Method: every finding below was
produced by directly reading the generated HTML/sitemap/robots output
(regenerated fresh via `python3 build_site.py && python3
scripts/seo_postprocess.py`) and the generator source, not assumed or
recalled from memory.

**Status: Step 1 (technical/on-page audit) substantially complete. Steps 2–5
(query mapping, CTR diagnosis, service/search-intent prioritisation) are
explicitly blocked on real Search Console and Google Ads exports — see
§13. Nothing in those sections has been guessed.**

---

## 1. URL inventory summary

66 HTML files on this branch: **44 real (indexable-intent) pages**, **22
legacy redirect stubs**. 35 URLs in `sitemap.xml`.

Real page breakdown:
- 1 homepage
- 9 service pages + 1 services index
- 12 area pages (generator-built, `AREA_DATA`) + 3 hand-authored area pages
  (London, Brentwood, Loughton) + 1 areas hub (`/areas`, hand-authored)
- 3 guides
- 4 `/lp/*` PPC landing pages (intentionally `noindex,nofollow`)
- About, Contact, Quote, Gallery, Contractors, Cookie Policy, Privacy
  Policy, Terms & Conditions, Thank You, 404

Four pages in the "real" set are **hand-authored, outside `build_site.py`
entirely**: `areas/index.html`, `areas/london/index.html`,
`areas/brentwood/index.html`, `areas/loughton/index.html`. Everything else
is generated. This matters for every finding below that touches those four
— they don't get the generator's consistency guarantees for free, and
every fix to them this phase was a manual, individually-verified edit.

## 2. Canonical audit

**Before this phase**: the 4 hand-authored pages each declared a
self-referencing canonical (and, on 3 of them, `og:url`/`hreflang`/
breadcrumb-schema `item`) with a trailing slash (`/areas/london/`), while
every one of the 12 generator-built area pages, the sitemap, and every
internal link sitewide referenced them without one (`/areas/london`). A
page's own declared canonical disagreeing with the URL form used
everywhere else that points to it is exactly the kind of combined
canonicalisation signal conflict Google's documentation warns can cause it
to select a different canonical than the one declared.

**Fixed this phase**: all 4 pages' canonical/og:url/hreflang/breadcrumb-
schema URLs now use the no-trailing-slash form, matching the site's
established convention (only the homepage itself is the trailing-slash
exception, per the CI validation script).

**Confirmed clean elsewhere**: every generator-built page's canonical is
self-referencing and uses the WWW host consistently; the bare (non-www)
hostname never appears as an outgoing URL anywhere (a dedicated CI check
enforces this).

## 3. Metadata audit

- Every real page has a `<title>` and meta description.
- **Fixed**: `areas/index.html`'s `twitter:title`/`twitter:description`
  were copy-pasted from the About page and described the wrong page
  entirely ("About Axis Scaffolding Essex | Essex Scaffolders Team" on the
  Areas hub). Corrected to match the page's own `og:title`/description.
- `areas/london/index.html` has no `twitter:title`/`twitter:description`
  at all (brentwood/loughton both have them). Not fabricated here — flagged
  as a minor, low-priority gap rather than invented.
- Title lengths (`title_len` column, full inventory in the audit script
  output) are broadly reasonable; none were rewritten this phase per the
  brief's instruction to sequence title/meta review *after* the
  intent/page map exists (§26 of the brief), not before.

## 4. Schema (JSON-LD) audit

Full type inventory per page was generated and reviewed. Headline finding,
already acted on:

- **`areas/london/index.html` carried a fabricated `AggregateRating`**
  (`ratingValue: "5.0"`, `reviewCount: "47"`) on its `LocalBusiness` block.
  A sitewide `grep` for `AggregateRating`/`aggregateRating`/`ratingValue`/
  `reviewCount`/`review` confirmed this was the **only** occurrence in the
  repository — removed entirely, not replaced with any other figure.
  Logged in `CLAIM_VERIFICATION.md`. Google's own guidance restricts
  `review`/`aggregateRating` on `LocalBusiness` markup to sites reviewing
  *other* local businesses, not self-serving reviews of the business
  itself — genuine testimonials remain as visible page content sitewide,
  never as structured data.
- `areas/index.html` carries its own `ScaffoldingContractor` schema block
  (distinct from the `LocalBusiness`/`HomeAndConstructionBusiness` type
  used elsewhere) — a real, valid schema.org type, not necessarily wrong,
  but worth deciding whether the site should standardise on one business
  entity type across all pages carrying business schema (currently: mostly
  `LocalBusiness`/`HomeAndConstructionBusiness`, this one page uses
  `ScaffoldingContractor`). Flagged, not changed — an entity-consistency
  decision, not a clear bug.
- `BreadcrumbList` schema is present and correct on every real page that
  has a visible breadcrumb, now including the 3 guide pages' corrected
  "Guides" crumb (see §7).
- `FAQPage` schema exists on the homepage, `/services`, and each of the
  3 hand-authored area pages (London/Brentwood/Loughton) — all sourced
  from real, visible on-page FAQ content, not schema-only invented Q&A.
- No schema was added this phase beyond what was already valid and
  representing visible content, per the brief's explicit instruction not
  to add schema types merely because they exist in schema.org.

## 5. Indexability / robots meta audit

All 22 legacy redirect stubs are now uniformly `noindex,follow` (see §8 —
this was a real, confirmed gap before this phase's fix). All `/lp/*`
landing pages are `noindex,nofollow` (correct — paid-only, not meant to
rank organically). `/thank-you` is `noindex,nofollow` (correct — form
confirmation page). All 44 real pages otherwise carry no restrictive
robots meta (implicitly indexable) except the above.

## 6. Sitemap audit

**Fixed**: `/areas` (the hub/index page) was missing from `sitemap.xml`
despite being a real, `index,follow` page that every area page and the
hand-authored London/Brentwood/Loughton pages link back to. Added.

`sitemap.xml` correctly excludes: all 22 redirect stubs, all 4 `/lp/*`
pages, `/thank-you`, and the 3 noindex legal pages (privacy policy, terms,
cookie policy) — verified by the CI validation script's own noindex-in-
sitemap check, which passes.

Sitemap URL form is consistent (no trailing slash except the homepage
itself) — this was the actual point of the canonical fix in §2, since
`scripts/seo_postprocess.py`'s `update_sitemap()` already strips trailing
slashes from any URL it adds, so the sitemap entries for London/Brentwood/
Loughton were always correct; only the pages' own self-declared canonical
disagreed with them.

## 7. Internal-link graph

Built by extracting every internal `<a href>` from every real page and
resolving in/out degree. Full counts captured in this phase's audit
script output (not reproduced in full here — summary below).

**Orphans (real pages with zero inbound internal links from other real
pages) — 10 found, classified:**

| Page | Classification | Action |
|---|---|---|
| `/404.html` | Expected — error page, never linked | None needed |
| `/thank-you` | Expected — only reached via form submission redirect | None needed |
| `/lp/emergency-scaffolding-essex`, `/lp/scaffolding-rayleigh`, `/lp/scaffolding-southend`, `/lp/temporary-roofing-essex` | Expected — PPC-only pages, deliberately not linked from organic navigation | None needed |
| `/guides/do-i-need-scaffolding`, `/guides/highway-licence-scaffolding`, `/guides/scaffolding-cost-essex` | **Real gap.** Three genuine, non-fabricated guide pages with zero inbound links from anywhere else on the site — only reachable via direct URL or sitemap crawl | Flagged, not fixed — see §7a |
| `/cookie-policy` | **Real gap.** Only one `href="/cookie-policy"` exists sitewide, and it's the page's own breadcrumb (self-link, doesn't count). The footer uses a JS "Cookie Settings" `<button>` that opens a preferences modal, not a link to the standalone page | Flagged — low severity, content is largely duplicated in the consent banner, but the standalone page is otherwise unreachable by navigation |

**Broken internal links: one found and fixed.** All 3 guide pages'
breadcrumbs linked to `/guides`, which doesn't exist as a page (`ls
guides/` shows only the 3 individual guide subdirectories — no index).
This was a live, visible 404 in every guide page's breadcrumb and a
misleading `BreadcrumbList` schema entry citing a non-existent URL. Fixed
by making `breadcrumb_nav()`/`breadcrumb_schema()` render an unlinked crumb
level (no `<a>`, no schema `item`) when no real hub page exists yet — not
by inventing a `/guides` index page. Whether a real `/guides` hub should be
built is a content/IA decision, not a technical one; flagged in §7a.

**Weakly-linked pages**: London/Brentwood/Loughton each have only 3
inbound internal links (their own breadcrumb self-references aside), versus
15–24 for the 12 generator-built area pages. `/areas/index.html`
itself only links out to 6 of the 12 real areas plus London — it omits
Wickford, Hadleigh, Leigh-on-Sea, Thundersley, Hockley, Rochford, and
Brentwood/Loughton entirely from its own "areas we cover" list, despite
all of them being real pages. Flagged — see §7a.

### 7a. Flagged internal-linking decisions (not acted on — ambiguous, per the brief's own rule)

- **Should a real `/guides` index page be built?** Three genuine guides
  exist with no hub and no cross-linking between them. Building one is a
  content/IA decision (what intro copy, what order, whether it belongs in
  main nav) that goes beyond a technical fix.
- **Should `/areas/index.html` link to all 12 real areas (plus
  Brentwood/Loughton)?** It currently lists only 6. This looks like an
  omission rather than a deliberate curation, but changing which areas
  appear on the site's primary "areas we cover" page is a visible content
  decision worth confirming rather than silently rewriting.
- **Should `/cookie-policy` gain a real inbound link** (e.g. from the
  footer, alongside or instead of the JS preferences button), or is the
  JS-only path intentional?

## 8. Redirect / migration architecture audit

Two real, now-fixed generator bugs (see git history on this branch for
full detail — commits fixing "fabricated AggregateRating" and
"consolidate legacy redirect stubs"):

1. `build_site.py` and `scripts/seo_postprocess.py` **independently**
   generated the legacy redirect stub `.html` files and `_redirects`, with
   `seo_postprocess.py` (which always runs second) only partially
   overwriting `build_site.py`'s output. Net effect: 11 of 22 legacy
   stubs (`about.html`, `gallery.html`, `contact.html`, `privacy.html`,
   `terms.html`, `cookies.html`, and 5 of 10 legacy area stubs) were
   missing the `noindex,follow` meta tag that the other 11 correctly had —
   relying solely on a meta-refresh redirect and canonical tag to stay out
   of the index. Consolidated into `scripts/seo_postprocess.py` as the
   single source of truth; `build_site.py`'s duplicate generator removed
   entirely (not left as dead code). Verified self-sufficient: deleting
   all 22 stub files plus `_redirects` and rerunning the pipeline
   regenerates every one of them, byte-for-byte correct, from nothing.
2. **`_redirects` is Netlify-syntax and does not function on GitHub
   Pages** (this repo deploys via `actions/deploy-pages`, which serves
   static files as-is — it does not process a `_redirects` file). The
   file is still generated and now internally complete/consistent, but it
   has **no actual effect on the deployed site**. The real, functioning
   redirect mechanism for every legacy URL is the per-file client-side
   `<meta http-equiv="refresh">` + `window.location.replace()` plus the
   page's own `<link rel="canonical">` pointing at the real target. This
   is weaker than a server-side 301 (client-side redirects require the
   page to load and execute JS before redirecting, and carry a slightly
   different signal to crawlers) but it is what is actually live. Do not
   assume `_redirects` is doing anything on production — documenting this
   gap rather than pretending it's solved, per the brief's own instruction
   for the domain-migration section.

## 9. Old-domain migration (external infrastructure — unchanged this phase)

`axisscaffolding.co.uk` deep-link redirect behaviour is an **external
infrastructure limitation outside this repository** — confirmed
unchanged, not re-investigated this phase since nothing in the repo can
affect it. The canonical, correct architecture remains:

- Live site: `https://www.axisscaffoldingessex.co.uk/`
- `CNAME` correctly declares the WWW host (verified by CI)
- Old-domain wildcard rules exist in `_redirects` (see §8 — non-functional
  on this host) for any request that does reach GitHub Pages

Per Google's own site-migration guidance, this requires monitoring in
Search Console over time once the exports exist (§13) — watching both
properties' indexing/crawl errors and confirming the new sitemap is
submitted and being crawled. That's a Search Console action for the
owner, not a repository change.

## 10. AEO question inventory (existing content only — no new content written)

Existing FAQ sources, all real and already live:
- Homepage FAQ (general)
- `/services` FAQ (general)
- Each of the 9 service pages: service-specific FAQs + 1–3 curated general
  questions (PR #25's work — kept as-is, praised by the owner as correct)
- 3 guide pages (each is itself a long-form answer to one question: "How
  much does scaffolding cost in Essex?", "Do I need scaffolding?", "Do I
  need a highway licence?")
- London/Brentwood/Loughton hand-authored `FAQPage` schema (3 questions
  each)

All of these already follow a reasonable question → direct answer →
supporting detail shape informally. None were rewritten this phase — per
the brief, AEO answer-quality work (testing each answer as if extracted
alone) is scoped as a later step in this same phase, and it should be
informed by which questions actually drive impressions/clicks once the
GSC export exists, not reordered speculatively now.

## 11. GEO opportunity inventory (existing relationships only)

Real, verifiable relationships already in the data model (no invented
ones): `PROJECTS` entries carry both `service_slug` and `area` fields, so
service↔project and area↔project relationships already exist wherever a
real project photo exists. Confirmed gap (already surfaced in PR #25's
audit table, unchanged this phase): **4 of 9 services — Loading Bay,
Supply & Erection, Emergency, Dismantling — have zero tagged project
photos**, so their service pages cannot show real first-party evidence for
that specific service. This remains an owner-information gap (real job
photos needed), not something to fabricate around.

## 12. Claim verification summary

See `CLAIM_VERIFICATION.md` for the full three-tier table. This phase's
only addition: the fabricated `AggregateRating` (§4), now logged under
**DO NOT USE**. No other claims were touched, added, or propagated this
phase.

## 13. GSC / Ads data — explicitly required, not fabricated

**GSC DATA REQUIRED** — query-level Search Console export (`Query, Page,
Clicks, Impressions, CTR, Position`, 3-month window) not yet supplied.
Nothing in §14–16 below or in any future query-mapping/CTR/prioritisation
work has been started or guessed.

**ADS SEARCH-TERM DATA REQUIRED** — Google Ads Search Terms export
(`Search term, Campaign, Ad group, Match type, Impressions, Clicks, CTR,
Cost, Conversions, Cost/conv.`, matching the ~30-day window of the
£316.36-spend reference) not yet supplied.

Blocked until the exports arrive: query → page → intent mapping, CTR
diagnosis, homepage cannibalisation analysis, GSC/Ads-informed service or
location prioritisation, and the P0/P1/P2 opportunity matrix.

## 14. Fixes implemented this phase

1. Removed fabricated `AggregateRating` from `areas/london/index.html`;
   logged in `CLAIM_VERIFICATION.md`.
2. Fixed canonical/og:url/hreflang/breadcrumb-schema trailing-slash
   mismatch on `areas/london`, `areas/brentwood`, `areas/loughton`,
   `areas/index.html` — now consistent with the sitemap and every internal
   link that references them.
3. Added `/areas` to `sitemap.xml` (was missing entirely).
4. Fixed `areas/index.html`'s `twitter:title`/`twitter:description`,
   which described the About page.
5. Fixed the broken `/guides` breadcrumb link (and matching misleading
   `BreadcrumbList` schema entry) on all 3 guide pages — rendered as
   plain text rather than a dead link, without creating a new page.
6. Consolidated the two independent, disagreeing legacy-redirect-stub
   generators into one (`scripts/seo_postprocess.py`), fixing a real
   `noindex,follow` gap on 11 of 22 legacy stub pages and a missing-entries
   gap in `_redirects`. Removed the now-fully-redundant duplicate
   generator from `build_site.py` rather than leaving dead code.

Every fix above was individually validated: full CI script, deterministic
rebuild (double- and triple-checked across this phase), zero duplicate
element IDs, valid JSON-LD, `node -c` on `main.js`, and a browser check of
the affected pages with no console errors beyond the pre-existing sandbox
font-CDN connection-reset noise present on every page regardless of what
changed.

## 15. Fixes deferred / flagged (not acted on — decisions, not bugs)

See §7a (guides hub, areas-index area list, cookie-policy linking), §4
(schema entity-type consistency), §3 (London page missing Twitter card).
None of these were silently decided — each is a real, evidence-based
finding put to the owner rather than resolved unilaterally, per the
brief's explicit "when something is ambiguous, do not silently choose"
rule.

## 16. Validation evidence (this phase, cumulative)

- Full CI validation script (verbatim from `.github/workflows/pages.yml`)
  — passes on the final state.
- Deterministic rebuild — verified repeatedly across every commit this
  phase, including a from-nothing regeneration test (deleted all 22
  legacy stub files + `_redirects`, confirmed exact recreation).
- `node -c assets/js/main.js` — OK.
- Zero duplicate element IDs across every page touched this phase.
- All touched JSON-LD blocks parse as valid JSON.
- Browser smoke test of the guide breadcrumb fix and the London area page
  post-canonical-fix — both render correctly, console errors limited to
  the known sandbox font-CDN noise.
