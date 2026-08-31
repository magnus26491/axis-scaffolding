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
entirely, not replaced with any other figure. Genuine testimonials remain
displayed as visible page content (not structured data) sitewide — see
Phase 7's schema audit for the full `review`/`aggregateRating` scan
confirming this was the only occurrence in the repository.

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
| **£5 million public liability insurance (specific figure)** | `areas/london/index.html` only (3 occurrences: FAQ schema, USP list, second FAQ) | "We are fully insured with £5 million public liability cover" | **Owner confirmation required** | **Yes — high priority.** No other page states a figure; if the real figure is different, this is a live legal/financial claim being made publicly | Do not state a specific figure anywhere else until confirmed. If confirmed accurate, extend to the general "fully insured" claim sitewide for consistency; if not, correct or remove from the London page |
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
