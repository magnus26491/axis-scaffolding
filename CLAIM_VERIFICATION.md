# Axis Scaffolding — Claim Verification Inventory

Produced as part of Phase 5 (Trust + Customer Journeys). This is a durable
reference document, not a published page — it exists to gate what gets
reused/expanded in future phases (per the "resolve factual gaps before
expanding them" sequencing).

**Method**: every claim below was found by directly grepping the actual
repository content (not assumed, not re-derived from memory of earlier
sessions). "Pages using claim" lists every file where the claim's key terms
appear, found via `grep -rl` across all generated and hand-authored HTML.

## Summary — the three-way control system

This is the reference classification for all future SEO/AEO/GEO/commercial
content work. "Established" below corresponds to **VERIFIED**.

**VERIFIED** — safe to use, extend, and feature prominently:
CISRS qualified team · fully insured (general claim, no figure) · 10+ years'
experience · founder-led / Ashley (name, photo, the one existing testimonial
that names him) · same-day quote/response (phrased as an aim) · RAMS
available on request · company name/legal name/address/phone/email/company
number · based in Rayleigh, serving South Essex and surrounding areas.

**OWNER VERIFICATION REQUIRED** — do not delete, do not propagate, do not
feature until confirmed: £5m public liability insurance figure · TG20:21
compliance (as a certification claim, not a design methodology) · CDM
regulations experience · Section 169 Highways Act citation · RAMS "provided
as standard" (vs. "available on request").

**DO NOT USE** — confirmed fabricated, already removed, must not be
recreated or referenced as a source: the three dated London project case
studies (Barking/Dagenham/Romford, invented Mar–May 2026 dates and
operational detail, zero corroborating evidence anywhere in the repository);
a fabricated `AggregateRating` schema block (`ratingValue: "5.0"`,
`reviewCount: "47"`) found on `areas/london/index.html`'s `LocalBusiness`
JSON-LD during the Phase 7 SEO/AEO/GEO audit — no review-platform
integration or 47 reviews exist anywhere else in the repository; removed
entirely, not replaced with any other figure; six fabricated or altered
customer testimonials found across three of the four `/lp/*` PPC landing
pages during the Phase B claim audit ("Robert P.", "Michael T.", "James M.",
"Sarah K." — either wholly invented or near-verbatim copies of real
`testimonials()` reviews with the name and location changed — plus two
unverifiable anonymous "Roofing Contractor, Basildon" / "Property Owner,
Chelmsford" quotes with no traceable source); a matching "Rated 5.0 on
Google" sitewide-rating claim on 2 of those pages, same fabrication class as
the `AggregateRating` finding, no review-platform integration anywhere in
the repository. Genuine testimonials remain displayed as visible page
content (not structured data) sitewide — see Phase 7's schema audit for the
full `review`/`aggregateRating` scan confirming the `AggregateRating` block
was the only structured-data occurrence in the repository, and the Phase B
section below for the full landing-page testimonial audit.

## How to read "Verified?" (detailed table below)

- **Established** — appears consistently across multiple independently-built
  pages/templates (i.e. it's load-bearing enough that it's presumably a real
  fact the business supplied at some point), OR is structurally guaranteed
  true (e.g. company number, since it's the literal registered number).
- **Owner confirmation required** — appears on one page only, is more
  specific than the same topic is described elsewhere, or has no
  corroborating evidence (photos, other pages, schema) anywhere else in the
  repository.
- **Removed (fabricated)** — content with no factual basis found anywhere;
  action already taken in this PR, documented below.

| Claim | Source page(s) | Source text | Verified? | Owner confirmation required? | Recommended wording |
|---|---|---|---|---|---|
| CISRS qualified team | 34 files across the whole site (homepage, every service page, contractor page, about, London page) | "CISRS Qualified" / "CISRS-qualified team" / "CISRS-certified" | **Established** | No — used consistently sitewide, treated as core fact throughout this project | Keep as-is |
| Fully insured | Homepage, contractor page, ~11 other pages | "Fully Insured" / "fully insured" / "public liability" | **Established** (as a general claim) | No, for the general claim | Keep as-is |
| **£5 million public liability insurance (specific figure)** | `areas/london/index.html` (3 occurrences: FAQ schema, USP list, second FAQ) **and all four `/lp/*` PPC landing pages** (1 occurrence each — scope extended in Phase B's landing-page audit; previously only the London page was tracked) | "We are fully insured with £5 million public liability cover" / "£5m public liability coverage" | **Owner confirmation required** | **Yes — high priority, now affecting 5 pages, not 1.** No other page states a figure; if the real figure is different, this is a live legal/financial claim being made publicly on all of them | Do not state a specific figure anywhere else until confirmed. If confirmed accurate, extend to the general "fully insured" claim sitewide for consistency; if not, correct or remove from all 5 pages |
| 10+ years' experience | Homepage ("10+ Years' Experience"), About page, London page ("over 10 years") | "10+ Years' Experience" / "over a decade" / "over 10 years" | **Established** | No — consistent across pages | Keep as-is |
| "Founder-led" / Ashley as founder | Homepage ("Founder-led local operation"), About page, one customer testimonial naming him | "Founder-led local operation", "Ashley and his team were professional throughout..." | **Established** (per explicit instruction: existing founder material is a trust asset, not a gap) | No | Keep as-is — already improved in presentation this phase, not rewritten |
| RAMS / method statements & risk assessments | Contractor page: "RAMS on Request"; commercial-scaffolding service: "available on request"; London page: **"provided as standard for all commercial and CDM-notifiable projects"** | See above | **Established** as "available on request"; **the London page's "provided as standard" framing is stronger and inconsistent with every other page** | **Yes** — which is accurate: on-request, or standard-for-commercial? | Align London page wording to "available on request" (matching every other page) unless the owner confirms RAMS really are standard-issue for every commercial job, in which case update the wording sitewide instead |
| TG20 / TG20:21 compliance | `services/commercial-scaffolding/index.html`: "Installation... to TG20 or bespoke design" (design methodology, not a compliance certification claim); `areas/london/index.html`: "confirming competence to TG20:21 standards" / "compliant with current HSE guidance and TG20:21 standards" (a specific dated standard, stated as a compliance guarantee) | See above | **Owner confirmation required** for the London page's stronger framing | **Yes** — "designed to TG20" (a design methodology scaffolders use) is a materially different claim from "TG20:21 compliant" (implying certified conformance to a specific standard edition) | Align to the commercial-scaffolding page's more measured "to TG20 or bespoke design" framing unless the stronger claim is confirmed accurate |
| CDM regulations experience | `areas/london/index.html` only: "experienced teams accustomed to working under CDM regulations" | See above | **Owner confirmation required** | **Yes** — not mentioned anywhere else in the site | Do not propagate to other pages until confirmed |
| Section 169 Highways Act licensing advice | `areas/london/index.html` only | "We advise on Section 169 Highways Act licences for any scaffold occupying London borough streets" | **Owner confirmation required** | **Yes** — a specific named legal provision not referenced anywhere else (other pages use generic "highway/pavement licence" language, never a section number) | Use the site's existing generic "highway/pavement licence" language instead, unless the specific citation is confirmed correct |
| Same-day quote / same-day response | Sitewide — homepage, most area pages, emergency service page, both `/lp/` landing pages | "Same-Day Quote Response", "same-day quote", "aim to respond... same working day" | **Established**, consistently phrased as an *aim*, not a guarantee, everywhere except... | No | Keep as-is |
| Emergency mobilisation "within hours" | `areas/london/index.html` only, inside the now-removed fabricated case study | "erected a make-safe scaffold within hours of the client's call" | **Removed (fabricated)** | N/A — removed | See below |
| **Three dated project case studies (Barking, Dagenham, Romford)** | `areas/london/index.html` only | "Victorian Terrace Roof Scaffold – Barking" (May 2026), "Commercial Cladding Scaffold – Dagenham" (Apr 2026), "Emergency Make-Safe Scaffold – Romford" (Mar 2026) | **Fabricated — confirmed, not just unverified** | N/A | **Removed in this PR.** No photos, no entry in the real Projects data (`PROJECTS`/`AREA_DATA`), specific invented dates and operational details with zero corroborating evidence anywhere in the repository. Replaced with an honest link to the real `/gallery` Projects page (genuine South Essex work), not a substitute fabrication |
| Brand name consistency | Sitewide | "Axis Scaffolding" (16×) / "Axis Scaffolding Ltd" (16×) on homepage alone; "Axis Scaffolding Essex" also used on London page and some area pages | **Established as intentional**, per this phase's brief: "Axis Scaffolding" / "Axis Scaffolding Essex" as customer-facing brand, "Axis Scaffolding Ltd" as the legal entity (schema, footer, legal text) | No | Keep as-is — matches the explicit instruction that these are deliberately different registers, not an inconsistency |
| Company number / address / phone / email | Sitewide, schema + footer | "15050136", "Arterial Road, Rayleigh, Essex, SS6 7XT", "01702 820468", "axis-scaffolding@outlook.com" | **Established** — structurally guaranteed (same values everywhere, checked as part of every prior phase's CI validation) | No | Keep as-is |
| "Benfleet team" (quote-page intro) | Was on `/quote` — already rewritten in PR #22 (unmerged) to "Prefer to talk? Call {phone} instead", no location claim | — | **Already resolved** | No | No action needed here; will land once PR #22 merges |
| "Benfleet" wording on the domestic-scaffolding *service* page | Checked directly — already reads "We are based in Rayleigh and regularly provide scaffolding in Benfleet, Canvey Island..." | — | **Already correct** | No | No action needed |
| **Fabricated `AggregateRating` schema (5.0 / 47 reviews)** | `areas/london/index.html` only, `LocalBusiness` JSON-LD block | `"aggregateRating": {"@type": "AggregateRating", "ratingValue": "5.0", "reviewCount": "47"}` | **Fabricated — confirmed, not just unverified** | N/A | **Removed in Phase 7.** No review-platform integration, no 47 reviews, no rating source anywhere else in the repository. A sitewide `grep` for `AggregateRating`/`aggregateRating`/`ratingValue`/`reviewCount`/`review` confirmed this was the only occurrence — not repeated on any other page. Genuine testimonials remain as visible page content, not structured data; Google's own guidance restricts `review`/`aggregateRating` on `LocalBusiness` markup to sites reviewing *other* local businesses, not self-serving reviews of the business itself, so no replacement figure was added |

## Action taken in this PR (Phase 5)

- Removed the three fabricated London project case studies (see above) and replaced with an honest link to the real Projects page.
- Did **not** alter the £5m insurance figure, TG20:21, CDM, or Section 169 claims on the London page — per instruction not to delete a claim merely because it's unverified elsewhere. They're flagged above for owner confirmation instead.
- Did **not** propagate any of the London-page-only claims (insurance figure, TG20:21, CDM, Section 169) to any other page in this PR.

## Action taken in Phase 7 (SEO/AEO/GEO architecture)

- Removed the fabricated `AggregateRating` block from `areas/london/index.html` (see table above). Sitewide schema scan confirms no other `review`/`aggregateRating` structured data exists anywhere in the repository.
- Insurance figure, TG20:21, CDM, and Section 169 claims on the London page remain untouched and still flagged below as owner-verification-required — not deleted, not propagated elsewhere.

## Phase B — PPC landing page (`/lp/*`) claim audit

Phase A's read-only audit flagged one example (the Southend testimonial) as a
sample finding. Auditing all four `/lp/*` pages against this document in
Phase B, as instructed, found the same fabrication pattern repeated across
three of the four pages, not just one. Documented in full below, per the
CLAIM / PAGE / SOURCE / STATUS / ACTION / OWNER INPUT NEEDED format.

| Claim | Page(s) | Source text found | Status | Action taken | Owner input needed |
|---|---|---|---|---|---|
| **"Robert P., Southend" testimonial** | `lp/scaffolding-southend/index.html` | "Emergency call-out within hours when we had storm damage. Ashley was brilliant and the scaffold made everything safe." — Robert P., Southend | **Fabricated — confirmed.** No matching name, quote, or storm-damage/emergency review exists anywhere in the real `testimonials()` data or elsewhere in the repository. | **Removed.** Replaced with two genuine, verbatim entries from the real `testimonials()` list (Jason R. and Hannah M.), correctly attributed, with the fabricated Southend-specific framing dropped rather than reused for an unrelated real review. | No — do not recreate. If a real Southend/storm-damage testimonial exists, it should be added to `testimonials()` first (so it's available sitewide, verifiable, and consistent) rather than written directly onto one landing page. |
| **"Michael T., Southend-on-Sea" testimonial** | `lp/scaffolding-southend/index.html` | "Quick, efficient and friendly... Highly recommend for any Southend project." — Michael T., Southend-on-Sea | **Fabricated — confirmed.** Near-verbatim copy of the real Jason R. review (`testimonials()`), with the name changed and a location sentence appended that doesn't appear in the source review. | **Removed**, replaced as above. | No |
| **"James M., Rayleigh" testimonial** | `lp/scaffolding-rayleigh/index.html` | "They turned up on time... Highly recommend for any Rayleigh project." — James M., Rayleigh | **Fabricated — confirmed.** Near-verbatim copy of the real Sally M. review, name changed, location sentence appended. | **Removed.** Replaced with genuine, verbatim Sally M. and Hannah M. entries from `testimonials()`, generic framing ("What Our Customers Say", no location claim). | No |
| **"Sarah K., Rayleigh" testimonial** | `lp/scaffolding-rayleigh/index.html` | "Ashley and his team were professional... for our Rayleigh home." — Sarah K., Rayleigh | **Fabricated — confirmed.** Altered copy of the real Hannah M. review (name changed, "our project" changed to "our Rayleigh home"). | **Removed**, replaced as above. | No |
| **"Roofing Contractor, Basildon" / "Property Owner, Chelmsford" testimonials** | `lp/temporary-roofing-essex/index.html` | "Axis Scaffolding provided an excellent temporary roof..." / "Professional service from start to finish..." | **Unverifiable.** Anonymous personas, no name to check, no matching entry anywhere in `testimonials()` or the rest of the repository — no authoritative source could be established. | **Removed**, replaced with genuine, verbatim Jason R. and Verified Customer entries from `testimonials()`. | No — if these are real reviews from a real contractor/homeowner, add them to `testimonials()` with a real name or an honestly-labelled "Verified Customer" attribution (as the site already does for one entry) so they're traceable, rather than an anonymous persona on one page. |
| **"Rated 5.0 on Google" (sitewide rating claim)** | `lp/scaffolding-rayleigh/index.html`, `lp/scaffolding-southend/index.html` | "⭐⭐⭐⭐⭐ Rated 5.0 on Google · CISRS Certified · Fully Insured" | **Fabricated — confirmed**, same class as the already-removed `AggregateRating` (5.0 / 47 reviews) schema finding from Phase 7. No Google review-platform integration or review count exists anywhere in the repository. | **Removed** the rating claim; kept "CISRS Certified · Fully Insured" (both established elsewhere). | If a real, current Google rating exists, add it as a genuine, sourced figure (ideally sitewide via `testimonials()`/schema, not ad hoc per landing page) rather than restoring this line as-is. |
| **24/7 availability** | `lp/emergency-scaffolding-essex/index.html` | Title tag "24/7 Response", H1 "Emergency Scaffolding Essex – 24/7 Response", H2 "Emergency Scaffolding – Available 24/7", H3 "24/7 Availability" / "We respond to emergencies day and night", CTA "Call 01702 820468 – We're Ready 24/7" | **Owner verification required — treated as unverified, not propagated.** Contradicts the phrasing used everywhere else on the site ("aim to attend site or arrange erection as quickly as operatives are available"), and no other page or data source establishes genuine 24-hour/day operation. | **Rewritten to neutral, non-invented language**, matching the site's established phrasing: title/H1/H2 changed to "Rapid Response", H3 changed to "Priority Response" / "We aim to attend site or arrange erection as quickly as operatives are available", CTA changed to "We Respond Fast". No new response-time promise invented. | Yes — if the business genuinely operates a 24-hour emergency line, that's a strong, usable trust signal, but it needs confirming before it goes back on any page, worded precisely (e.g. "24-hour emergency phone line" vs. "24/7 on-site attendance" are very different claims). |
| **£5m public liability insurance (specific figure)** | All four `/lp/*` pages (previously only tracked on `areas/london/index.html`) | "£5m public liability coverage" | **Owner verification required** (existing classification, scope extended to cover all 4 LP pages) | **Not changed.** Per explicit instruction: do not propagate this claim further, but do not delete it from existing source material merely because it's unverified. Left as-is on all 4 pages. | Yes — see the original entry above. If confirmed, this becomes a strong, reusable trust signal sitewide; if not, it needs correcting on all 5 pages that now carry it (4 LP pages + London). |

### Permanent QA safeguard: testimonial & rating-claim integrity check

The six fabricated/altered testimonials above were found by a one-off
manual read of the four `/lp/*` pages — nothing was automatically checking
for this before Phase B. That's too important to leave as a manual
discovery, so this phase added a permanent, build-blocking regression
check: `scripts/check_testimonials.py`.

**What it does**: `build_site.py` now defines `TESTIMONIALS` as a
module-level constant — the single approved source of every real
testimonial (previously this data lived only inside `testimonials()`'s
function body, duplicated in spirit but never in source, on the pages that
carried altered copies of it). `scripts/check_testimonials.py` scans every
real HTML page — generated and hand-authored alike — for testimonial-shaped
content and fails (non-zero exit) if it finds:

1. Quoted testimonial text with no matching entry in `TESTIMONIALS`.
2. Testimonial text that matches an approved entry but is attributed to a
   different name.
3. A location or descriptor appended to a name that isn't that entry's
   approved platform label (i.e. a fabricated location, the exact pattern
   used in 4 of the 6 fabrications above).
4. Any "Rated X on Google" statement or `ratingValue`/`reviewCount`/
   `AggregateRating` schema key found anywhere on the site, unless
   `build_site.py`'s `APPROVED_RATING` constant is set (it's `None` by
   default — no such claim is currently approved anywhere).

**What it does not do**: it isn't a semantic or plagiarism detector — it's
a lightweight, pattern-based check against the two testimonial-display
patterns that actually exist in this codebase (the generated
`.testimonial-card` markup, and the hand-authored `/lp/*` "glass-card"
pattern). Verified against a synthetic fabricated-content test during
Phase B: it correctly caught a wholly invented quote, a name
misattribution, a fabricated location suffix, and a fake rating claim,
with zero false positives against the real (clean) codebase. If a third
testimonial-display pattern is ever introduced, this check needs
extending or it will silently miss it — see the module docstring.

**Wired into CI**: `.github/workflows/pages.yml` runs
`python3 scripts/check_testimonials.py` as a required build step, right
after the SEO post-processor. A future PR that reintroduces a fabricated
or altered testimonial, or an unsupported rating claim, fails CI rather
than merging silently.

To add a genuine new testimonial: add it to `TESTIMONIALS` in
`build_site.py` first (with a real source), then use it — never write
testimonial text directly onto a page without a `TESTIMONIALS` entry
backing it.

### Action taken in Phase B (Trust, Consistency & Customer-Journey Integration)

- Removed 6 fabricated/altered customer testimonials across 3 of the 4 `/lp/*` pages (Southend ×2, Rayleigh ×2, Temporary Roofing ×2) and replaced them with genuine, verbatim entries from the real `testimonials()` data, with any location-specific framing that wasn't genuinely sourced dropped rather than carried over onto real reviews.
- Removed the unsourced "Rated 5.0 on Google" line from 2 pages (Rayleigh, Southend) — same fabrication class as the Phase 7 `AggregateRating` finding.
- Rewrote the "24/7" claim on the emergency landing page to neutral, non-invented language, matching the site's established response-time phrasing.
- Did **not** touch the £5m insurance figure on any page — left in place per instruction, classification unchanged (owner verification required), scope of the existing table row extended to note it now appears on 5 pages, not 1.
- Did **not** touch TG20:21, CDM, or Section 169 claims on the London page — out of this phase's named scope, already documented above, unchanged since Phase 7.
- Added a permanent, CI-enforced regression check (`scripts/check_testimonials.py`) so a future testimonial or rating-claim fabrication fails the build instead of requiring another manual discovery — see the section above for full detail.

## Owner Information Report

### Critical
- **Confirm the £5 million public liability insurance figure.** This is a live, specific financial/legal claim on a public page, stated nowhere else on the site. If accurate, it should probably be added consistently wherever "fully insured" appears (it's a strong trust signal); if inaccurate, it needs correcting immediately.
- **Confirm whether RAMS (method statements & risk assessments) are provided as standard for commercial/CDM-notifiable work, or available on request.** The site currently says both, on different pages.

### Important
- **Confirm TG20:21 compliance** (the specific standard edition) vs. the more measured "designed to TG20" framing used on the commercial-scaffolding page.
- **Confirm CDM regulation experience** as a claim — is this something the business can substantiate (e.g. specific commercial/principal-contractor work), and should it be featured more broadly if true?
- **Confirm the Section 169 Highways Act citation** for London borough pavement licensing — if accurate for London specifically, is the general (non-London) highway/pavement licence guidance elsewhere on the site citing the right equivalent provision for Essex/non-London councils?
- **Real London project evidence.** If Axis genuinely does regular East/NE London work, real photos and honest project records (matching the same standard used for the South Essex Projects page) would let a real London projects section be rebuilt properly, rather than leaving the removed section as just a link back to South Essex work.

### Optional
- A named surname or short bio line for Ashley, if the business wants to expand the About page beyond what the existing testimonial and photo establish (explicitly not done in this PR — flagged only).
- Customer/project counts, if the business tracks them and wants to use them as a trust signal (not currently used anywhere, and not invented here).
