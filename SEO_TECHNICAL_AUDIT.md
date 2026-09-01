# Axis Scaffolding — SEO / AEO / GEO Technical Audit

Durable reference document for Phase 7 (SEO + Local SEO + AEO + GEO
Architecture). Like `ALIGNMENT_SYSTEM.md` and `CLAIM_VERIFICATION.md`, this
is not a published page — it's the working forensic record that gates
future search-architecture decisions. Method: every finding below was
produced by directly reading the generated HTML/sitemap/robots output
(regenerated fresh via `python3 build_site.py && python3
scripts/seo_postprocess.py`) and the generator source, not assumed or
recalled from memory.

**Status: Step 1 (technical/on-page audit) complete, including the /areas
and /guides architecture decisions (§17–19) and the indexability-vs-
search-worthiness classification (§20). Steps 2–5 (query mapping, CTR
diagnosis, service/search-intent prioritisation) are explicitly blocked on
real Search Console and Google Ads exports — see §13. Nothing in those
sections has been guessed.**

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

---

## Round 2 — /areas and /guides architecture, indexability vs search-worthiness

Follow-up to the owner's explicit steer: the `/areas` (6-of-12 areas) and
`/guides` (no hub) gaps flagged in §7a needed a deliberate IA decision,
not a blind patch — and every page needs a crawlability-vs-usefulness
distinction, not just an indexable/not-indexable one.

## 17. /areas — investigated, then rebuilt

Before deciding, inspected the actual page, not just its content:

- `/areas` is **not in primary site navigation** anywhere (`nav()`
  produces Home/Services/For Builders/Projects/About/Contact — no
  "Areas" item).
- The **footer's own "Areas We Cover" section, present on every page,
  was providing zero navigational value** — it rendered `AREAS[:8]` as
  plain `<li>` text with no `<a href>` at all, truncated to 8 of the 12
  real areas. The actual area-discovery mechanism for the site is the
  homepage's own `area_pills()` section (all 12, real links) — the
  footer was decorative dead text, not a genuine second discovery path.
- Reading the hand-authored `areas/index.html` file in full revealed it
  was a **frozen snapshot of an older site-chrome template**: its header
  nav is missing "For Builders" and "Projects" (uses "Gallery" instead),
  its cookie consent bar is the old inline-styled version rather than
  the current `cookie_ui()` output, and its markup includes a
  `mobile-cta-bar` component that **no longer exists anywhere in the
  current generator** (confirmed: the CSS rules for `.mobile-cta-bar`
  are themselves dead code — nothing in `build_site.py` emits that
  markup any more). This is a materially bigger problem than "6 areas
  missing" — the whole page was drifting from the live design system,
  the same class of risk the redirect-stub consolidation (§8) already
  fixed for a different set of pages.

**Decision**: yes, `/areas` should be a genuine hub for all 12 real
`AREA_DATA` areas — the evidence supports it (12 real, substantive area
pages already exist; the only things missing were complete links and
current chrome, not missing content). Implemented by **migrating
`areas/index.html` into `build_site.py`** rather than hand-patching the
stale file — it now always reflects `AREA_DATA` and the live
`nav()`/`footer()`/`cookie_ui()`, so it can't drift again. Kept
deliberately concise per instruction: hero, the full 12-area pill grid
(`area_pills()`, already used elsewhere — no new component), a one-line
cross-link to `/services`, and the standard CTA banner. No new visual
elements.

**Also fixed as part of the same evidence**: the sitewide footer's
"Areas We Cover" now renders real links to all 12 areas instead of 8
unlinked names. This touches every page on the site and is the single
highest-value internal-linking fix this phase — area-page inbound link
counts more than doubled on the pages that were weakest (e.g.
`/areas/basildon` went from 18 to 40 inbound links after the footer fix
regenerated, since the footer appears everywhere).

**Deliberately not resolved in this pass**: London/Brentwood/Loughton
are not included in the rebuilt `/areas` hub. They carry a different
evidence tier (several claims flagged `OWNER VERIFICATION REQUIRED` in
`CLAIM_VERIFICATION.md` — the £5m insurance figure, TG20:21, CDM,
Section 169) and conflating them with the 12 verified core areas as
equal-tier entries would overstate their status. They remain reachable
via their own pages and breadcrumbs; whether/how to present them
alongside the core 12 is still an open decision, not silently made
either way.

## 18. /guides — investigated, then rebuilt

Evaluated the 3 guides for topical coherence before deciding — did not
build a hub merely because 3 pages exist:

- "Do I Need Scaffolding for My Project?" (earliest decision stage)
- "How Much Does Scaffolding Cost in Essex?" (pricing stage)
- "Does Scaffolding on a Pavement Need a Licence?" (logistics/compliance)

These are three genuinely distinct, substantive questions that form a
real pre-purchase customer journey — not an arbitrary set. Confirmed
zero cross-links between them and zero links from any service page,
the homepage, or `/services` to any of them before this fix — they were
reachable only by direct URL or sitemap crawl.

**Decision**: yes, a real hub is justified. Implemented:
- `GUIDES` list (slug/title/one-line summary) added to `build_site.py`.
- `/guides` index page (generated, not hand-authored): 3 cards using the
  existing `.service-card` pattern, no new visual elements.
- `related_guides_section()` — each guide now cross-links to the other
  two ("Related Guides").
- Each guide's "Guides" breadcrumb (previously an unlinked plain-text
  fix from §7/§14 item 5, since `/guides` didn't exist yet) now links to
  the real hub.
- One contextual inbound link each from the homepage FAQ section and
  the `/services` FAQ section ("Read our full guides" / "Not sure what
  you need? Read our scaffolding guides") — natural placements, not
  links added purely to raise a count.
- `/guides` added to `sitemap.xml`.

## 19. Cookie policy — fixed

Confirmed the gap was real: the footer's "Cookie Settings" button only
reopens the consent bar (accept/reject/manage categories) — it does not
show the actual policy text, and the consent bar itself links only to
`/privacy-policy`. `/cookie-policy` (the full policy document) had
exactly one inbound link sitewide before this fix: its own breadcrumb
(a self-link, which doesn't count). Fixed by adding a real `Cookie
Policy` link to the footer legal row, alongside the existing `Cookie
Settings` button (kept, since it serves a different purpose — managing
consent, not reading the policy), `Privacy Policy`, and `Terms &
Conditions`.

## 20. Technically indexable vs. search-worthy

Per the instruction not to assume every `index,follow` page belongs in
the sitemap or deserves organic priority. Classification for all 45 real
pages (44 → 45 after adding `/guides`) plus the 22 redirect stubs as one
group:

| Category | Pages | Technically indexable? | Search-worthy? | Why |
|---|---|---|---|---|
| **CORE INDEXABLE** | Homepage, `/services` + 9 service pages, `/areas` + 12 area pages, `/guides` + 3 guides, `/gallery`, `/about`, `/contractors` | Yes | Yes | Primary entity, service, location and informational content — the pages the whole architecture exists to rank |
| **SUPPORTING INDEXABLE** | `/services/dismantling-scaffolding`, `/services/loading-bay-scaffolding`, `/services/scaffold-supply-erection` (real services, but zero project-photo evidence per PR #25's audit table); `/areas/london`, `/areas/brentwood`, `/areas/loughton` (real content, but carrying unresolved owner-verification claims) | Yes | Qualified yes — real and legitimate, but weaker trust/evidence than the CORE tier until the gaps close | Genuinely useful, not thin, but shouldn't be assumed equally search-ready as the fully-evidenced core |
| **UTILITY** | `/contact`, `/quote`, `/404` | Yes (except 404, no canonical) | Low — necessary for users and conversion, not realistic organic search targets in their own right | Conversion/utility role, not content role |
| **PPC** | `/lp/emergency-scaffolding-essex`, `/lp/scaffolding-rayleigh`, `/lp/scaffolding-southend`, `/lp/temporary-roofing-essex` | No (`noindex,nofollow`) | No — deliberately paid-only | Correct as-is |
| **MIGRATION / REDIRECT** | All 22 legacy stub `.html` files | No (`noindex,follow`, meta-refresh) | No | Transitional only — see §8 |
| **LEGAL** | `/privacy-policy`, `/terms-and-conditions`, `/cookie-policy` | Technically yes (no noindex meta) but deliberately excluded from `sitemap.xml` | No — nobody searches for a scaffolding company's cookie policy | Correct as-is; the CI validation script enforces their sitemap exclusion |
| **DUPLICATE / CONSOLIDATION CANDIDATE** | None found | — | — | Residential vs. Domestic Scaffolding was checked in an earlier phase and confirmed genuinely distinct, not a duplicate pair |

No page was reclassified or reindexed based on this table alone — it's
diagnostic, feeding into (not pre-empting) the eventual GSC-informed
priority work.

## 21. Page-purpose test (representative sample)

Applied "why does this page exist / who is it for / what should they do
next" to the pages this round's fixes touched most:

- **`/areas`**: exists so a visitor who isn't sure whether Axis covers
  their town can check in one place, and so search/AI systems have one
  clear "coverage" page to point to rather than inferring it from 12
  separate pages. Next action: pick an area or go to Services/Quote.
  Evidence: the same real `AREA_DATA` used everywhere else — no
  fabricated coverage claims.
- **`/guides`**: exists for a visitor still deciding whether/how much/
  what's legally required, before they're ready to request a quote.
  Next action: read the relevant guide, then quote/call. Evidence: each
  guide already cites real regulations (Work at Height Regulations 2005,
  Highways Act 1980 s.169) and Axis's own process — not generic filler.
- **`/cookie-policy`**: exists for compliance and for the small number
  of visitors who want the full policy text rather than the consent
  banner's summary. Not meant to attract search traffic — correctly
  excluded from the sitemap, now just reachable.

## 22. Validation evidence (round 2)

- Full CI validation script — passes.
- Deterministic rebuild — verified after every change this round.
- `node -c assets/js/main.js` — OK.
- Zero duplicate element IDs on `/areas`, `/guides`, all 3 guide pages,
  homepage, `/services`.
- Internal-link graph re-run after all fixes: the `/guides` and
  `/cookie-policy` orphan findings from §7 are resolved (both now have
  real inbound links); the one broken-link finding (`/guides`) is
  resolved; the only remaining zero-inbound real pages are the ones
  expected to have none (404, the 4 PPC landing pages, `/thank-you`).
- Browser screenshots of `/areas` and `/guides` at 1440px and 390px,
  plus a guide page's new "Related Guides" section — all render using
  the existing design system with no new visual components, consistent
  header/footer, and no console errors beyond the known sandbox
  font-CDN noise.

---

## Round 3 — hub-integration audit (approved architecture, final check before stopping)

Re-verified the /areas and /guides hubs end-to-end rather than assuming
round 2's implementation was already perfect. Found and fixed one real
remaining defect; everything else checked out.

### 23. /areas hub verification

- `/areas` → all 12 real area pages: **12 links, zero duplicates**, all
  no-trailing-slash, verified by direct extraction.
- Every one of the 12 generator-built area pages' breadcrumb links back
  to `/areas` correctly. `areas/london/index.html`'s breadcrumb did
  not: `<a href="/areas/"> Areas Served</a>` — trailing slash plus a
  stray leading space inside the link text, missed by round 1's fix
  (which only touched the page's canonical/og/hreflang/schema URLs, not
  this separate relative link in the visible breadcrumb markup). **Fixed**
  this round: `<a href="/areas">Areas Served</a>`.
- No nearby-area links pointing to `/contact` as a substitute (the
  `/contact` matches found are legitimate nav/footer "Contact"/"Contact
  us" links, verified by inspecting each match, not area-name
  substitutions — the PR #25 fix holds).
- No stray anchor fragments beyond the standard `#main-content`
  skip-link (accessibility feature, present on every page, not a defect).
- No inconsistent URL forms remain: a sweep for any internal
  `href="/.../"` (trailing slash) across every area and guide page
  returned zero matches after the fix above.
- Area pages → services: full `services_grouped_section()` present on
  every generator-built area page (verified on Rayleigh: 10 service
  links). Area pages → quote: present (verified: 2 quote links each).
- **Area pages → real projects: genuinely missing.** `PROJECTS` already
  carries `area_slug` tagging 14 real projects across 11 of the 12
  areas (only Hockley has none) — the same kind of relationship PR #25
  already surfaced on service pages ("Related Projects" filtered by
  `service_slug`). No area page currently renders any project evidence
  at all. This is a real, data-backed gap, not a fabrication risk (the
  data already exists) — **flagged, not implemented**, per the
  instruction to stop technical implementation after this audit.

### 24. /guides hub verification

- `/guides` → all 3 real guides: verified, matches `GUIDES`.
- Every guide's breadcrumb links back to `/guides` — verified on all 3.
- Related-guide links: exactly 2 per guide (the other 2), verified —
  not a forced block, genuinely the full relevant set since there are
  only 3 guides total.
- Guide → quote CTA: present on all 3 (2–3 buttons each, existing CTA
  pattern).
- **Guide → service: currently only the generic footer's full 9-service
  list, not a deliberate, contextual link to the one or two services
  each guide is actually about** (e.g. the licence guide could
  reasonably link to `/services/residential-scaffolding` and
  `/services/roof-scaffolding` specifically, where highway licences
  come up most). Not a broken relationship — the footer link technically
  exists — but not the "genuinely relevant" targeted relationship the
  brief asked for either. **Flagged, not implemented** — the guide body
  copy would need a considered, specific edit per guide, not a
  mechanical addition.

### 25. Page-purpose roles (added to the classification)

Extending §20's table with explicit hub/child roles, as requested:

| Page | Role |
|---|---|
| `/areas` | **LOCAL NAVIGATION HUB** — lets a visitor or crawler discover every genuine service area from one place |
| `/areas/[area]` (12 pages) | **LOCAL SERVICE / LOCATION PAGE** — answers "does Axis cover my town, and what would a job here look like" |
| `/guides` | **KNOWLEDGE HUB** — the entry point for pre-purchase questions, not a sales page |
| `/guides/[guide]` (3 pages) | **INFORMATION / AEO RESOURCE** — a single, extractable answer to one real question |

`/areas/london`, `/areas/brentwood`, `/areas/loughton` remain classified
as SUPPORTING INDEXABLE local/location pages (§20) — real content, but a
different evidence tier, deliberately outside the LOCAL NAVIGATION HUB
role until their unresolved claims are confirmed.

### 26. Navigation — confirmed unchanged

Verified `nav()` still reads exactly Home / Services / For Builders /
Projects / About / Contact / phone / Get a Free Quote — **Guides was not
added to primary navigation**, per instruction. Discoverability for both
hubs comes from: `/areas` via the sitewide footer (all 12 areas, fixed
this phase) and the homepage's own area-pills section; `/guides` via the
homepage FAQ section, the `/services` FAQ section, and each guide's own
cross-links — contextual placement, not header real estate.

### 27. Human UX test

- **Can a homeowner find their local area easily?** Yes — from the
  footer (every page, all 12 real areas, now linked) or the homepage's
  dedicated area-pills section, in one click either way.
- **Can a customer find answers before contacting Axis?** Yes — `/guides`
  is reachable from the homepage FAQ and `/services` FAQ, and each
  guide cross-links the other two, so a visitor who lands on one finds
  the rest without hunting.
- **Can they move naturally from answer → service → location → real
  project → quote?** Answer → service: yes (guide body links to all
  services via the footer, though not the specific one — see §24).
  Service → location: yes (every service page has an "Areas We Cover"
  section, from PR #25). Location → real project: **no** — this is the
  one missing link in the chain (§23's finding). Location → quote: yes
  (every area page has a CTA). **Specific missing relationship
  identified**: area → project. Everything else in the chain holds.

### 28. Final technical audit — status

| Item | Status |
|---|---|
| Full URL inventory | Complete (§1) |
| Canonical audit | Complete (§2, §17, §23) |
| Sitemap audit | Complete (§6, §17–18) |
| Robots audit | Complete (§5) |
| Schema audit | Complete (§4, §23–24) — `/areas` and `/guides` carry only `LocalBusiness` + `BreadcrumbList`, matching every other generated page, no unnecessary types added |
| Breadcrumb audit | Complete (§7, §17, §23–24) — one remaining defect (London's `/areas/` breadcrumb link) found and fixed this round |
| Indexability audit | Complete (§5, §20) |
| Page-purpose classification | Complete (§20, §25) |
| Internal-link graph | Complete (§7, §22) — re-run this round: zero broken links, only expected orphans remain (404, 4 PPC pages, thank-you) |
| Service/area/project/guide relationship graph | Complete — one confirmed real gap (area→project, §23), one confirmed weak relationship (guide→specific-service, §24), both flagged not implemented |
| Fabricated-content scan | Complete (§4, §12) — one fabrication found and removed (AggregateRating), nothing else found |
| Unsupported-claim scan | Complete — see `CLAIM_VERIFICATION.md`, unchanged in scope this phase beyond the AggregateRating entry |

## 29. Final report — divided per instruction

**A. FIXED** (this phase, all committed and pushed to PR #26):
Fabricated `AggregateRating` removed; canonical/og/hreflang/breadcrumb-
schema trailing-slash consistency on 4 hand-authored area pages (round 1)
plus London's remaining breadcrumb link (round 3); `/areas` and `/guides`
added to sitemap; Twitter card copy-paste bug; broken `/guides`
breadcrumb link; legacy-redirect-stub generator consolidation (11 of 22
stubs gained missing `noindex,follow`); sitewide footer area list (8
unlinked names → 12 real links); `/areas` migrated from a stale
hand-authored file into the generator; `/guides` hub built from scratch;
cookie-policy footer link added.

**B. VERIFIED** (checked, found correct, no change needed):
Primary navigation unchanged, Guides correctly kept out of it; `/areas`
and `/guides` schema matches visible breadcrumbs exactly; no duplicate
or dead links in either hub; no inconsistent trailing-slash URLs remain
anywhere in the area/guide family; sitemap URLs all canonical, WWW,
correct trailing-slash convention, no redirects included; CI validation,
deterministic rebuild, `node -c`, duplicate-ID checks all pass.

**C. OWNER VERIFICATION REQUIRED** (unchanged from `CLAIM_VERIFICATION.md`,
not touched this phase): £5m insurance figure, TG20:21 compliance,
CDM regulations experience, Section 169 citation specificity — all
confined to the London page, all flagged before this phase began.

**D. GSC DATA REQUIRED**: query-level Search Console export (3 months,
`Query, Page, Clicks, Impressions, CTR, Position`) — not yet supplied.

**E. ADS DATA REQUIRED**: Google Ads Search Terms export (~30 days
matching the £316.36 spend reference, `Search term, Campaign, Ad group,
Impressions, Clicks, CTR, Cost, Conversions, Cost/conv, Conversion
value`) — not yet supplied.

**F. DEFERRED TO NEXT PHASE** (real, evidence-based, deliberately not
implemented — decisions or content work beyond this audit's scope):
- Area pages → real project evidence (§23) — 14 real `area_slug`-tagged
  projects exist and are unused on area pages.
- Guide → specific-service contextual links (§24) — currently only the
  generic footer list.
- Whether/how London/Brentwood/Loughton should relate to the `/areas`
  hub (§17).
- `areas/index.html`'s `ScaffoldingContractor` schema type vs.
  `LocalBusiness`/`HomeAndConstructionBusiness` used elsewhere.
- London page's missing Twitter card.
- All GSC/Ads-dependent work: query→page→intent mapping, CTR diagnosis,
  homepage-cannibalisation analysis, service/location prioritisation,
  Ads search-term classification.

**Phase 7 technical implementation stops here**, per instruction. No
further speculative SEO changes will be made against this audit; the
next work is the GSC/Ads-informed matrix once the two exports arrive.
