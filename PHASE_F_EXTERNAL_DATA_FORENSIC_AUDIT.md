# Phase F — External Data Forensic Audit

**Status: READ-ONLY. No code, content, metadata, schema, redirects, internal links, Google Ads, GSC, GA4, or campaign settings were changed while producing this report.**

This continues Phase F from the completed site-side forensic audit (guides isolation, expansion-area under-linking, indiscriminate service↔area graph, project-photo gaps, schema gaps, trailing-slash behaviour, emergency-journey weakness). This document reconciles those structural findings against the raw external exports and cross-checks each site-side claim directly against the repository before treating it as established.

Every conclusion below is labelled:
- **(A)** directly evidenced by an external data export
- **(B)** evidenced by repository or live-site inspection
- **(C)** inference — plausible, not provable from the data available
- **(D)** unknown / requires further data

## Data quality note read this first

The raw exports used are internally inconsistent with each other in ways that matter. This is documented in full in **Section L**, but the headline is: **roughly a third to a half of paid-search spend, and over half of organic clicks, cannot be attributed to any individually named query in the exports provided.** Every percentage in this report is computed only over the visible, named rows unless stated otherwise — it is not a full-account picture.

---

## A. Executive Evidence Summary

1. **(A)** GSC query-level data is heavily thresholded: the Queries export sums to 42 clicks / 40,144 impressions across 614 rows, while the same 12-month period's daily Chart export totals 100 clicks / 43,124 impressions. **58% of organic clicks in the period are not attributable to any individual query** GSC will disclose.
2. **(A)** The Ads Search Terms export shows the same pattern on the paid side: of the account's £4,182.06 all-time cost, only £1,821.73 (44%) sits on individually named search terms; £1,121.69 sits in an "Other search terms" bucket Google won't disclose by text, and a further ~£1,238 sits in campaign types not covered by this report at all (see A.7 below).
3. **(A)** A single broad-match keyword, **"scaffolding hire,"** accounts for **52.9% of all keyword-level cost (£1,466.31 of £2,770.47) and 61.5% of all keyword-level conversions (24 of 39)** — by a wide margin the most important single unit in the account. It carries a "Limited" delivery status due to a Quality Score flag ("low quality"), meaning its own delivery is being throttled by Google despite being the top performer.
4. **(A)** The previously-reported **"cost" negative-keyword finding is now directly confirmed**: a broad-match, campaign-level negative keyword literally `cost` exists on "Phone calls Campaign - Axis High Intent," alongside 8 further price/cost variants (`price`, `prices`, `cheap`, `cheapest`, `price list`, `scaffolding hire cost`, `scaffolding hire prices`, `cost of scaffolding london`). This is no longer an inference.
5. **(B)** A new conflict was found while testing negatives against the site's own service architecture: **`domestic` is a broad-match, campaign-level negative** on the same active campaign — colliding directly with the real "Domestic Scaffolding" service and with organic queries like "domestic scaffolding rayleigh" that rank at position 7.2. This looks like an unintended block of a real service line, not a deliberate exclusion — flagged, not changed.
6. **(A)** GSC's Pages export shows **21 of 29 canonical pages (72%) are being tracked as two separate rows** — trailing-slash and non-trailing-slash — covering 93.5% of all indexed impressions. **(B)** Live verification (direct HTTP requests, not a guess) shows the *current* site correctly 301-redirects the non-slash variant to the slash variant on every URL tested, and the build produces no page that exists as both a flat file and a directory index. **(C)** This is very likely index-consolidation lag from Google, not a live duplicate-content bug today — but it means every raw per-page number in the export understates true page performance by roughly 2× for most of the site, and this cannot be fully resolved without knowing exactly when the redirect was fixed relative to GSC's crawl history.
7. **(D → partially corrected, see Section N)** "Total: Account" (£4,182.06, 94 conversions) exceeds "Total: Search" (£3,002.21, 40 conversions) by £1,179.85 and **54 conversions**. **A live Campaigns-view pull (Section N) confirms the account has exactly two campaigns and both are Campaign type "Search"** — this rules out Performance Max, Display, Demand Gen, Video, and Shopping as the explanation. The gap itself is not closed; see Section N for the full reconciliation and what remains unresolved.
8. **(A)** London is, on the paid side, the single highest-spending location in the account (£826.60 combined across its two bid-adjustment rows, 216 clicks, 12 conversions) and the keyword `scaffolding london` is the second-largest keyword by spend (£681.95, 10 conversions). **(B)** Yet London receives exactly one inbound internal link on the entire site (from the `/areas` hub only) and is absent from the footer. Paid is already proving commercial demand for a page the site itself treats as an afterthought.
9. **(A)** Kent generates real, efficiently-converting paid demand (£134.23 spend, 3 conversions, ~£44.74 CPA across Maidstone/Chatham/ME-postcode rows) despite having **no page anywhere in the site's architecture** (not in `AREA_DATA`, not in `EXPANSION_AREA_DATA`).
10. **(A)** Dozens of hyper-specific town+service organic queries rank at position 1–4 (e.g. "industrial scaffolding companies rayleigh" pos 1.0/173 impr, "commercial scaffolding rayleigh" pos 1.4/546 impr, "specialist scaffolding rayleigh" pos 1.66/399 impr) yet return **zero clicks**. **(D)** Whether this is a genuine CTR failure, a snippet problem, or a GSC position-averaging artifact from a low, noisy sample cannot be determined from this export alone.
11. **(A)** The GA4 property (screenshots only, see Section H) recorded 3 sessions / 3 users over the reporting window, with no `generate_lead` or `phone_click` events firing at all — every event was a default auto-collected one. **(B)** Confirmed in code: GA4 only loads after explicit cookie-consent opt-in, and was only wired across the full site + PPC LPs two days before the report's end date. GA4 is not usable as a volume source yet.

---

## B. GSC Query Intelligence Table

**(A) Property/scope facts, directly from the export's own `Filters.csv`:**
- Search type: **Web**
- Date range: **Last 12 months** (rolling as of 2026-09-05; the daily Chart export shows real data starting 2026-04-22, effectively ~4.5 months of live signal, not 12)
- Rows returned: 614 queries, 50 raw page rows (29 after merging trailing-slash duplicates)
- Site-wide totals (Chart.csv, the only fully-reconciled total): **100 clicks, 43,124 impressions**
- Countries: 92 of 100 clicks from United Kingdom; the rest scattered (India, South Africa, US, Spain, Russia, Bahrain) — noise, not addressable demand
- Devices: Desktop 59 clicks / 25,308 impr, Mobile 40 / 15,950, Tablet 1 / 1,866
- **Search Appearance report is completely empty (0 rows)** — the property is not accruing any measured rich-result/enhancement appearances. This corroborates the "meaningful educational-content schema gap" finding directly from GSC's own data, not just repository inspection.

**Intent-cluster reconstruction (614 rows, summing to 42 clicks / 40,144 impressions — see data-quality note above for why this undercounts):**

| Category | Queries | Clicks | Impr. | CTR | Avg. position | % of visible clicks |
|---|--:|--:|--:|--:|--:|--:|
| Branded ("axis...") | 11 | 23 | 176 | 13.07% | 17.27 | 54.8% |
| Core generic scaffolding | 166 | 9 | 8,000 | 0.11% | 36.66 | 21.4% |
| Core-town/local (12 towns) | 173 | 7 | 17,763 | 0.04% | 25.15 | 16.7% |
| Hire/rental | 99 | 2 | 4,504 | 0.04% | 37.46 | 4.8% |
| Contractor/commercial/builder | 77 | 0 | 7,168 | 0.00% | 29.61 | 0.0% |
| Out-of-area/other town | 25 | 0 | 413 | 0.00% | 62.31 | 0.0% |
| Service-specific | 22 | 0 | 1,481 | 0.00% | 33.29 | 0.0% |
| Expansion town (London/Brentwood/Loughton) | 11 | 0 | 284 | 0.00% | 22.70 | 0.0% |
| Equipment/plant | 9 | 0 | 43 | 0.00% | 62.42 | 0.0% |
| Job-seeking/employment | 5 | 0 | 54 | 0.00% | 32.61 | 0.0% |
| Price/cost | 3 | 0 | 4 | 0.00% | 2.50 | 0.0% |
| Informational | 2 | 0 | 19 | 0.00% | 82.79 | 0.0% |
| Emergency | 1 | 0 | 201 | 0.00% | 6.65 | 0.0% |

**(A) Branded query anomaly:** "axis scaffolding" itself averages **position 4.1**, not position 1, across 119 impressions. A branded head term not holding position 1 is unusual and worth independent verification (possible brand confusion with another "Axis" business, a Knowledge Panel competing for the top slot, or genuine SERP volatility) — **(D)** not resolved here.

**(A) Rayleigh investigation (Section D specific ask) — full evidence, not a summary:**

40 distinct Rayleigh-qualified query variants were found, totalling 3,327 impressions and **exactly 3 clicks** ("scaffolding rayleigh" 2 clicks/777 impr, "scaffolding in rayleigh" 1 click/331 impr). The striking pattern is the position data on the zero-click rows:

| Query | Impr. | Position | Clicks |
|---|--:|--:|--:|
| industrial scaffolding companies rayleigh | 173 | **1.00** | 0 |
| commercial scaffolding rayleigh | 546 | **1.40** | 0 |
| specialist scaffolding rayleigh | 399 | **1.66** | 0 |
| rental scaffolding material rayleigh | 195 | **1.14** | 0 |
| temporary roofing scaffolding rayleigh | 190 | **1.73** | 0 |
| local scaffolders rayleigh | 189 | **1.97** | 0 |
| scaffolding firms rayleigh | 188 | **1.96** | 0 |
| scaffolders in rayleigh | 185 | **2.21** | 0 |
| scaffold contractors rayleigh | 192 | **1.99** | 0 |
| domestic scaffolding rayleigh | 342 | 7.20 | 0 |

**Determination of the previously-observed Rayleigh anomaly (Section E specific ask):** the evidence rules out several candidate explanations directly:
- **Not a property-scope issue (A):** the property is the correct domain, "Web" search type, and Rayleigh queries clearly appear in it.
- **Not "genuinely absent from the Pages report" (A):** `/areas/rayleigh` does not even rank in the top-50 Pages export at all, at any position — yet its queries rank #1–2. This means the impressions are almost certainly landing on a *different* page than `/areas/rayleigh` (most plausibly the homepage, since "Rayleigh" is the business's home-base town and appears heavily in on-page copy sitewide) — **(D) unconfirmed without a query×page cross-report**, which GSC's UI export does not provide in one file.
- **Possibly a canonical/URL-consolidation effect (C):** consistent with the site-wide trailing-slash finding in Section C below.
- **Possibly a reporting/position-averaging artifact (C):** a position of 1.0–2.0 on a low-volume long-tail query can reflect one or two lucky high-rank impressions averaged with the query's real, much lower typical rank; GSC's "average position" is not resistant to this at low volumes.
- **Genuinely unresolved (D):** distinguishing these requires either the GSC URL Inspection tool per query (not available in this export) or a live rank-tracking test, neither of which was run. **This should stay flagged as unresolved, not closed.**

**Other specific queries requested:**
- `scaffolding hire` (exact) — 9 impressions, 0 clicks, position 1.22.
- `scaffolding near me` (exact) — 12 impressions, 1 click, position 14.42.
- `scaffolding company near me` (exact) — 11 impressions, 1 click, position 21.09.
- `scaffold hire` (exact) — 1 impression.
None of these carry meaningful organic volume as literal exact strings; real "hire" demand (4,504 impressions) is almost entirely long-tail, town-qualified ("scaffolding hire rayleigh" 396 impr, "scaffolding hire benfleet" 286 impr, etc.), not the bare head term.
- **Emergency:** exactly one row — "emergency scaffolding essex," 201 impressions, position 6.65, **0 clicks**. This corroborates the "emergency organic journey is structurally weaker" finding directly from GSC (position 6–7 is a real, stable average across enough impressions to be meaningful, not a single-observation artifact) — **(A)**.
- **Price/cost:** essentially invisible organically — 3 rows total, 4 impressions combined ("cheap scaffolding near me," "scaffolding costs uk," "scaffolding quote"). Organic pricing intent is not being captured at all, and (per Section F below) it is also being blocked on the paid side.

**Expansion-town organic demand (London/Brentwood/Loughton) — Section D specific ask:**

| Query | Impr. | Position |
|---|--:|--:|
| scaffolding services loughton | 148 | 20.53 |
| scaffolding loughton | 54 | 20.35 |
| domestic scaffolding loughton | 20 | 22.25 |
| scaffolding company loughton | 16 | 23.81 |
| scaffoldingforextensions london | 7 | 45.71 |
| scaffolding north east london | 4 | 35.50 |

Real, if modest, organic demand exists for Loughton specifically (246 combined impressions across 6 query variants) at positions in the 20s — a page that is currently linked from exactly one place on the entire site.

---

## C. GSC Page Performance Table

**Trailing-slash finding, quantified (A):** merging each URL's slash/non-slash variants into one canonical row:

| Canonical URL | Role | # GSC row variants | Clicks | Impr. | Avg. position |
|---|---|--:|--:|--:|--:|
| `/` | HOME | 2 | 91 | 31,664 | 28.15 |
| `/services/domestic-scaffolding/` | SERVICE | 2 | 0 | 3,439 | 60.54 |
| `/about/` | ABOUT | 2 | 2 | 2,987 | 46.56 |
| `/areas/southend/` | AREA | 2 | 0 | 2,645 | 45.75 |
| `/services/temporary-roofing/` | SERVICE | 2 | 0 | 2,589 | 38.43 |
| `/areas/chelmsford/` | AREA | 1 | 0 | 2,528 | 51.09 |
| `/areas/benfleet/` | AREA | 2 | 0 | 1,863 | 41.99 |
| `/services/` | SERVICE-HUB | 2 | 0 | 1,776 | 83.66 |
| `/services/commercial-scaffolding/` | SERVICE | 2 | 0 | 1,571 | 68.80 |
| `/contact/` | CONTACT | 2 | 1 | 1,489 | 82.17 |
| `/areas/brentwood/` | AREA (expansion) | 2 | 0 | 1,219 | 48.38 |
| `/services/roof-scaffolding/` | SERVICE | 2 | 0 | 1,118 | 41.54 |
| `/areas/basildon/` | AREA | 2 | 1 | 1,028 | 50.34 |
| `/areas/rochford/` | AREA | 2 | 1 | 740 | 25.36 |
| `/areas/canvey-island/` | AREA | 1 | 2 | 705 | 40.58 |
| `/services/emergency-scaffolding/` | SERVICE | 2 | 0 | 641 | 61.50 |
| `/services/residential-scaffolding/` | SERVICE | 2 | 0 | 557 | 81.62 |
| `/areas/loughton/` | AREA (expansion) | 2 | 1 | 508 | 19.68 |
| `/areas/` | AREA-HUB | 1 | 0 | 328 | 72.27 |
| `/quote/` | QUOTE | 2 | 0 | 305 | 90.41 |
| `/services/scaffold-supply-erection/` | SERVICE | 1 | 0 | 292 | 49.04 |
| `/areas/london/` | AREA (expansion) | 2 | 2 | 121 | 33.21 |
| `/terms/` | OTHER | 1 | 0 | 54 | 58.17 |
| `/gallery/` | GALLERY | 2 | 0 | 51 | 71.24 |
| `/guides/do-i-need-scaffolding/` | GUIDE | 2 | 0 | 37 | 75.11 |
| `/guides/highway-licence-scaffolding/` | GUIDE | 1 | 0 | 19 | 7.53 |
| `/services/dismantling-scaffolding/` | SERVICE | 2 | 0 | 11 | 40.73 |
| `/guides/scaffolding-cost-essex/` | GUIDE | 1 | 0 | 2 | 6.00 |

**21 of 29 canonical pages (72%), covering 93.5% of impressions, are split across two GSC rows.** No `/contractors` page appears in the Pages export at all (0 recorded impressions in 12 months).

**Findings against the role classification:**
- **High impressions, effectively zero CTR, across nearly every non-homepage page role** — Service pages, Area pages, About, Contact and Quote all sit at 0.00%–0.11% CTR despite thousands of combined impressions. This is not one weak page; it is the pattern across the entire site outside the homepage and a handful of branded/near-branded queries.
- **Pages ranking well but receiving unexpectedly few clicks:** `/areas/loughton/` averages position 19.68–21.08 (respectable for a page linked from nowhere but the areas hub) yet only 1 click on 508 impressions.
- **Guides have the weakest visibility of any page family on the site:** the three guide pages combined pull 58 impressions and 0 clicks across 12 months. `guides/scaffolding-cost-essex/` — the page that should be answering the price/cost intent this report also finds is blocked on paid (Section F) and invisible organically (Section B) — has **2 impressions total**. This is the single clearest piece of external evidence for the "guides are structurally isolated" finding: it isn't just under-linked internally (B, repo-verified in Section I), it is functionally invisible to search.
- **`/contact` and `/about` carry meaningful impressions (1,489 and 2,987) but essentially no clicks** (1 and 2 respectively) despite ranking around position 46–82 — consistent with pages that exist mainly for direct/branded navigational traffic, not discovery.
- **No page is competing head-to-head for the same query cluster in a way this export can detect** — the split-URL problem (above) is the dominant confound; a true cannibalisation read is not reliable until that is resolved.

---

## D/E. Ads Search-Term Forensics + Keyword ⇄ Search-Term Reconciliation

**(A) Scope facts:** "All time" export, 3,954 data rows (3,950 after removing 4 built-in subtotal rows), spanning **two campaigns**: "Phone calls Campaign - Axis High Intent" (2,813 rows, currently active per the Location report) and "Axis Scaffolding | High Intent" (1,137 rows, currently paused — confirmed directly in the Keyword report, where every one of its keywords shows status reason "campaign paused"). Any category total below blends an active and a dead campaign; this is flagged, not silently merged away.

**Official subtotal rows, taken verbatim from the export (do not re-derive these):**

| Row | Clicks | Impr. | Cost | Conversions |
|---|--:|--:|--:|--:|
| Total: Search terms (named rows) | 408 | 13,743 | £1,821.73 | 25.00 |
| Total: Other search terms (Google-anonymised) | 290 | 8,989 | £1,121.69 | 14.00 |
| Total: Search (both campaigns, Search type) | 743 | 24,534 | £3,002.21 | 40.00 |
| Total: Account (all campaign types) | 3,449 | 165,286 | £4,182.06 | 94.00 |

38% of "Total: Search" cost sits in terms Google won't name individually. The gap between "Total: Search" and "Total: Account" (£1,179.85, 54 conversions) is entirely outside this report's visibility — see Section G.

**14-category classification of the 3,950 named search-term rows** (sums to the "Total: Search terms" row above, confirming the classification script itself is not the source of any discrepancy):

| Category | Terms | Clicks | Cost | Conv. | CPA | % Spend | % Conv. |
|---|--:|--:|--:|--:|--:|--:|--:|
| 1. Core local generic | 2,616 | 260 | £1,151.15 | 15.0 | £76.74 | 63.2% | 60.0% |
| 2. Named-town/local (core 12) | 74 | 35 | £212.20 | 2.0 | £106.10 | 11.6% | 8.0% |
| 11. Outside service area | 180 | 29 | £146.28 | 3.0 | £48.76 | 8.0% | 12.0% |
| 7. Hire/rental | 330 | 28 | £109.40 | 2.0 | £54.70 | 6.0% | 8.0% |
| 14. Other/genuinely unclear | 293 | 12 | £77.10 | 1.0 | £77.10 | 4.2% | 4.0% |
| 8. Competitor/brand | 94 | 21 | £59.85 | 0.0 | — | 3.3% | 0.0% |
| 2b. Named-town (expansion: London/Brentwood/Loughton) | 117 | 13 | £46.41 | 1.0 | £46.41 | 2.5% | 4.0% |
| 6. Price/cost | 138 | 6 | £9.18 | 0.0 | — | 0.5% | 0.0% |
| 5. Emergency | 2 | 2 | £6.83 | 1.0 | £6.83 | 0.4% | 4.0% |
| 13. Irrelevant | 3 | 1 | £2.23 | 0.0 | — | 0.1% | 0.0% |
| 9. Equipment/plant | 61 | 1 | £1.10 | 0.0 | — | 0.1% | 0.0% |
| 3. Service-specific | 23 | 0 | £0.00 | 0.0 | — | 0.0% | 0.0% |
| 4. Contractor/builder/commercial | 16 | 0 | £0.00 | 0.0 | — | 0.0% | 0.0% |
| 12. Informational | 3 | 0 | £0.00 | 0.0 | — | 0.0% | 0.0% |
| **10. Job-seeking/employment** | **0** | **0** | **£0.00** | — | — | **0.0%** | — |

**Job-seeking/employment shows literally zero named-term spend** — the only category with no rows at all. Cross-referenced against Section F, this is a genuine negative-list success story, not a gap: an extensive job/careers/recruitment negative list is in place at both campaign and ad-group level and appears to be working exactly as intended.

**The single most important reconciliation finding in this report — the "scaffolding hire" keyword vs. its apparent search-term footprint:**

At the keyword level (Keywords export, 93 rows, £2,770.47 total cost, 39 conversions):

| Keyword | Match | Status | Clicks | Cost | Conv. |
|---|---|---|--:|--:|--:|
| **scaffolding hire** | Broad | Limited (low quality) | 311 | **£1,466.31** | **24.00** |
| scaffolding london | Broad | Eligible | 134 | £681.95 | 10.00 |
| scaffold hire | Broad | Not eligible (campaign paused) | 58 | £139.12 | 3.00 |
| [scaffold firms near me] | Exact | Limited | 27 | £121.95 | 1.00 |
| "scaffolding near me" | Phrase | Limited | 8 | £44.04 | 1.00 |

`scaffolding hire` alone is **52.9% of all keyword-level cost and 61.5% of all keyword-level conversions.** `scaffolding hire` + `scaffold hire` + `scaffolding london` together account for 82.6% of keyword-level cost.

Yet in the search-term text classification above, the entire "Hire/rental" category (every named term literally containing "hire" or "rent") sums to only **£109.40** — 7.5% of what the `scaffolding hire` keyword alone spent. **This is a direct, unreconciled conflict, and it is flagged rather than smoothed over:**

- **(D) Cannot be fully verified:** the Search Terms export provided has no "matched keyword" column, so there is no way to confirm from this data alone which literal queries actually triggered the `scaffolding hire` keyword.
- **(C) Most likely explanation:** Google's broad-match delivery for `scaffolding hire` is matching on modern semantic/behavioural signals, not literal substring containment — meaning most of the traffic it wins does **not** contain the word "hire" in the literal query text at all. This is consistent with "1. Core local generic" being by far the largest text-classified category (63.2% of spend, bare terms like "scaffolding," "scaffolders near me," "total access scaffolding") — plausibly much of that spend is actually being won by the `scaffolding hire` keyword's broad match, not a literal "generic" keyword.
- **This cannot be stated as fact.** A keyword-level report broken out by matched search term (available in the Ads UI as a drill-down, not exported here) is required to close this gap. **Flag for future data pull, not a conclusion to act on.**

**Answering the specific instruction — "determine whether the previous observation that broad 'scaffolding hire' consumed substantial keyword-level spend is still supported by the raw data":** **Yes — confirmed, and stronger than a prior summary would suggest.** It is not merely "substantial," it is the single dominant line item in the account, responsible for a majority of both cost and conversions, while simultaneously being throttled by a Quality Score flag.

**"scaffolding" and "scaffolding near me" as literal keywords:** no keyword row exists for the bare word "scaffolding" on its own — the closest exact-match equivalents are `[scaffolding near me]` (Exact, Paused, £13.51/2 clicks) and `"scaffolding near me"` (Phrase, Limited, £44.04/1 conv) plus a broad `scaffolding near me` (Paused, £43.09/0 conv on one campaign and £12.02/0 conv duplicated on the other, paused, no conversions on either instance). The broad match version of this exact phrase has never converted in this data; only the phrase-match version has.

**Competitor keywords:** none appear in the Keywords export at all — competitor names only show up as search terms (see Section F), not as active/paused keywords the account is bidding on. No evidence of deliberate competitor-conquesting keyword strategy.

**Terms with real conversions worth naming exactly** (from the visible search-terms rows, excluding subtotal rows): `scaffolding near me` (£73.39/1 conv), `scaffolding southend` (£58.38/1), `dale hire witham` (£23.35/1), `jacks scaffolding tunbridge wells` (£30.19/1), `billericay scaffolding` (£27.85/1), `murphy scaffolding` (£20.77/1), `markone hire basildon` (£13.80/1), `scaffolding norwich` (£17.85/1), `coventry scaffolding` (£13.70/1), `street scaffolding` (£15.62/1), `emergency scaffolding` (£6.83/1), `scaffolding` (bare, £81.70/1 and separately £4.77/1 on the other campaign), `essex scaffolding` (£6.70/1), `scaffolding company witham` (£8.78/1), `scaffolding leigh on sea` (£3.29/1), `scaffold poles for sale near me` (£9.24/1), `scaffolding agency london` (£6.45/1), `scaffolding grantham` (£5.76/1), `speedy erith` (£12.17/1), `mr scaffolding services` (£5.55/1), `morgans scaffolding` (£3.02/1), `scaffolding companies romford` (£1.04/1), `scaffolding companies braintree` (£2.47/1).

Notably several of these converting terms sit geographically **well outside any current or expansion service area** (Norwich, Coventry, Tunbridge Wells, Witham, Grantham, Erith) — real paying leads are apparently being won from locations the site has no architecture for and Ads has no dedicated targeting for. This deserves attention in a decision phase but is not acted on here.

---

## F. Negative-Keyword Conflict Report

**(A) Full inventory, from the current negative-keyword export (429 unique negative keywords):**

| Level | Count | Match type | Count |
|---|--:|---|--:|
| Campaign | 410 | Broad | 315 |
| Ad group | 20 | Exact | 77 |
| — | — | Phrase | 38 |

Two campaigns each carry a nearly-independent negative list; **61 negative-keyword texts are duplicated verbatim across both campaigns** (e.g. `[scaffolding certification]`, `[scaffolding insurance]`, `take apart`, `careers`, `diy`). This is redundant maintenance overhead — not a conflict, but worth noting under data quality: the two lists are not shared/synced, so future edits risk drifting apart.

**Previously-unverifiable "cost" finding — now confirmed (A):** the single-word broad-match negative `cost` exists at campaign level on "Phone calls Campaign - Axis High Intent," alongside `price`, `prices`, `price list`, `cheap`, `cheapest`, `scaffolding hire cost`, `scaffolding hire prices`, and `cost of scaffolding london`. Combined with the price/cost search-term category showing only £9.18 of spend and zero conversions across 138 terms (Section D), and the pricing guide page having 2 organic impressions in 12 months (Section C), **all three channels — paid, organic, and content — are independently near-silent on pricing intent**, which is either a deliberate low-intent filter or an unintended triple-block. Not resolved here; flagged for the decision phase.

**New conflict found — real high-intent term likely blocked (B, cross-referenced against the repository):**

`domestic` is a broad-match, campaign-level negative on the account's only currently active campaign. Broad-match negatives block any query containing that word. The business runs a named "Domestic Scaffolding" service (`build_site.py` SERVICES list, slug `domestic-scaffolding`), and organic data in this same report shows "domestic scaffolding rayleigh" (342 impr, position 7.2), "domestic scaffolding essex" (649 impr), and a dozen other domestic+town combinations with real search volume. There is no keyword in the current Keywords export targeting "domestic scaffolding" positively that would need this negative to disambiguate it from something else. **This looks like an accidental block of a real service line — flagged, not changed, pending confirmation of intent.**

**Other broad-match negatives worth a second look (lower confidence, listed for the decision phase, not acted on):**
- `home` — would block "home scaffolding southend" (54 organic impressions, a real query pattern found in GSC data).
- `free` — would block "free scaffolding quote"-style queries, which mirror the site's own stated CTA language ("Free quotes — call...").
- `scaffold` (bare, singular) — empirically does **not** appear to be blocking "scaffolding" (plural) queries, since the same campaign shows genuine spend on many "scaffolding ..." search terms; Google's broad-negative matching is evidently not treating them as close variants here. Flagged as ambiguous, not broken.

**Legitimate blocks confirmed working as intended (A) — for balance, not everything found here is a problem:**
- Job-seeking terms are covered extensively at *both* campaign level (`job`, `jobs`, `career`, `careers`, `vacancies`, `apprentice`, `apprenticeship`, `salary`, `wages`, `recruitment`) *and* ad-group level (`"jobs"`, `"recruitment"`, `"apprenticeship"`, `"labourer"`, `"training"`, `"health and safety"`, `"cis"`, `"hse"`, `"inspector"`, `"certification"`). This fully explains the zero-spend Job-seeking/employment category found in Section D.
- Equipment/plant negatives (`plant hire`, `scaffold tower`, `mobile tower`, `rolling tower`, `tower hire`) correspond directly to the near-zero Equipment/plant search-term spend (£1.10 across 61 terms).

**Leakage — terms that should arguably be excluded but are not yet (A, direct from `Added/Excluded` column):**
- Out-of-area: `scaffolding romford` (£16.81, None), `scaffolding chatham` (£7.19, None), `kent scaffolding companies` (£6.16, None), `trad safety systems barking` (£5.60, None), `scaffolders colchester` (£2.19, None), `scaffolding dartford` (£1.91 + £1.64, both None), `enfield scaffolding` (£1.50, None) — £146.28 total across 180 out-of-area terms, most not yet excluded.
- Residual competitor leakage: `speedy hire stansted` (£1.44, None), `aes scaffolding` (£1.15, None), `rotamead essex` (£1.07, None) — small (~£3.66 combined) but real, on terms whose base form (`speedy hire`, `aes scaffolding`, `rotamead`) is already excluded — these are un-caught variants.

**Note on classification vs. business reality:** `billericay scaffolding` was initially bucketed as "outside service area" by geography (Billericay is not in `AREA_DATA` or `EXPANSION_AREA_DATA`), but the repository's own Basildon area-page copy explicitly names Billericay as part of that area's informal coverage ("surrounding areas including Laindon, Pitsea, Billericay"). It converted once (£27.85/1 conv) and is already marked `Added` (promoted toward a keyword). This is exactly the kind of case Section 6 flags: **a location can be commercially real and already informally served without having formal site architecture** — the gap is in the site's structure, not necessarily in the term's relevance.

---

## G. Location Performance Report

**(A) Full picture, 126 rows, £2,863.08 total cost, 37 conversions** (this total is ~£182 different from the Search-Terms-derived "Total: Search" figure of £3,002.21 in Section D and ~£93 different from the Keywords-export total of £2,770.47 — a small, unexplained residual gap between all three exports, flagged rather than smoothed over; plausibly different pull timestamps or minor campaign-type scope differences between reports).

| Bucket | Locations | Clicks | Impr. | Cost | Conv. |
|---|--:|--:|--:|--:|--:|
| Core Essex town/county | 7 | 316 | 8,777 | £1,271.54 | 11.0 |
| Expansion town (London/Brentwood/Loughton) | 4 | 216 | 7,618 | £826.60 | 12.0 |
| Kent | 7 | 20 | 986 | £134.23 | 3.0 |
| Other/unclassified (scattered UK postcodes/towns) | 108 | 123 | 4,440 | £630.71 | 11.0 |

**London is the single top-spending location bucket by row, not just by aggregate:** `London, England, United Kingdom` with a +20% bid adjustment alone spends £699.69 for 12 conversions (£58.31 CPA); a second `London` row with no bid adjustment adds £126.91/0 conversions. Combined, London beats every individual Essex row.

**Unresolved location-data structure issue (D):** `Essex, England, United Kingdom` appears as **three separate rows** with three different bid adjustments (+20%, −20%, and none), summing to £1,199.96 and 10 conversions. Whether these represent three genuinely distinct targeting criteria (e.g. different location-targeting types — "presence" vs. "presence or interest" — stacked with device or audience modifiers) or a reporting artifact cannot be determined from a location-performance export alone; it would need the account's actual location-targeting settings, which are out of scope for a read-only data audit and were not inspected.

**Kent (Section 6 specific ask) — demand exists and is commercially meaningful (A):** £134.23 spend, 3 conversions, ~£44.74 CPA (a genuinely competitive CPA relative to the rest of the account) across Maidstone, Chatham, and several Kent postcode districts (ME1, ME9, ME3, ME19, ME20, TN15). **The site has zero architecture for Kent** — no `AREA_DATA`, no `EXPANSION_AREA_DATA` entry, no page. This is real, converting, currently-unserved demand.

**Long tail of scattered UK postcodes (108 rows, £630.71, 11 conversions) is not trivial in aggregate** (22% of location-report cost) but each individual row is thin (mostly 1–9 clicks). **Per the instruction not to assume a location deserves a page merely because it appears once**, none of these are recommended as new pages here — they are surfaced as a pattern (spend is diffusing into a very long, low-precision tail) for the decision phase, not as individual candidates.

**Cross-reference against site architecture:** of the "Expansion town" bucket's 4 rows (London ×2, and presumably Brentwood/Loughton individually — the two smaller expansion towns did not surface with nonzero cost in the top rows extracted and are not confirmed as separately spending here), only London has verified nonzero spend in the printed evidence above. Brentwood and Loughton's location-report rows were not found with cost/conversions in this pass — **(D) their true paid performance by location is not confirmed either way** and should not be assumed to mirror London's.

---

## H. GA4 Attribution / Conversion Report

**(D) No raw GA4 export/report file was provided or is available in this session.** The only GA4 evidence available is four dashboard screenshots (Events report and Traffic Acquisition report, both "Last 28 days: 8 Aug – 4 Sept 2026"), reviewed earlier in this conversation:

- **Events:** 42 total events, 3 users, 3 sessions. Every event is a default auto-collected type (`page_view` 16, `user_engagement` 15, `scroll` 5, `first_visit` 3, `session_start` 3). **No `generate_lead` or `phone_click` event fired even once** in the window shown.
- **Traffic acquisition:** 3 sessions total — 1 Direct, 1 Organic Search, 1 Organic Social. No paid channel appears in this breakdown at all.

**(B) Root cause, confirmed directly in `build_site.py`:** GA4 only loads client-side after explicit cookie-consent opt-in (`loadGA4()` gated behind `categories.analytics`, lines ~2444–2470) — until a visitor clicks Accept, nothing fires, not even `page_view`. **(B)** Git history shows GA4 was only wired across the full site and PPC landing pages by the Phase E5A commit on 2026-09-03, two days before this report's window ends — most of the 28-day window had no tracking code live at all. **(B)** No Google Ads conversion tag (`AW-...`) exists anywhere in the repository; the Ads-reported conversions are independent of the website's tracking entirely (most likely call-forwarding tracked at the phone-number level by Google Ads directly).

**Can current measurement distinguish organic/paid/direct/branded/local-generic/emergency/contractor leads? No — not yet, and not for a structural reason that will resolve itself with more time alone.** Two separate, compounding gaps:
1. **Volume gap (temporal):** insufficient days of live tracking so far.
2. **Coverage gap (structural, ongoing):** consent-gating means GA4 will *permanently* undercount paid-search sessions specifically, because PPC landing-page visitors who bounce before a consent decision (the majority of paid click-through behaviour) are invisible to GA4 by design. This is not something that improves with time — it is the GDPR-compliant tradeoff the current architecture made.

**Attribution blind spots (D):** whether GA4, once populated, would even be able to separate emergency leads from general residential leads, or contractor/commercial leads from homeowner leads, cannot be assessed — the custom event parameters (`generate_lead` with `event_label: form.dataset.formName`) exist in code but have never fired in the data available, so their actual output shape is unverified in production.

**No GA4 events or configuration were created or changed while producing this section.**

---

## I. Query → Page → Conversion Master Matrix

This is evidence-led and deliberately not exhaustive — it covers the clusters with real evidence weight from Sections B–G, not all 614 GSC queries or 3,950 search terms.

| Intent cluster | Location | Organic page (current) | Paid landing page | Current CTA | Evidence | Performance | Gap |
|---|---|---|---|---|---|---|---|
| Core generic ("scaffolding," "scaffolders near me") | Any | Homepage (inferred, B/D) | Homepage/PPC LP (unconfirmed which) | Call/quote form | A: 63.2% of named paid spend, 60% of conversions; A: 8,000 organic impr, 0.11% CTR | Best-converting cluster in the account | Organic CTR near-zero despite volume (C: possible snippet issue) |
| "scaffolding hire" (broad) | Any | Not a dedicated page (B: no hire-specific page exists) | Unconfirmed — no LP audit for keyword-to-LP mapping in this pass | Presumed generic quote CTA | A: 52.9% of keyword spend, 61.5% of conversions | Dominant single keyword, "Limited" by Quality Score | D: cannot confirm which LP it sends to, or whether a dedicated hire-intent page/ad group would relieve the quality flag |
| Town + service (Rayleigh, Benfleet, etc.) | Core 12 | `/areas/<town>/` (B) | Unconfirmed | Area-page quote CTA | A: position 1–4 on dozens of variants, 0 clicks; A: only £212.20/2 conv at keyword-town level | Excellent rank, near-zero realised organic value | D: CTR failure vs. reporting artifact unresolved (Section B) |
| London | Expansion | `/areas/london/` (B: 1 inbound link only) | Unconfirmed | Same generic template as core towns | A: £826.60 spend, 12 conversions (top-spending location); A: `scaffolding london` keyword £681.95/10 conv; A: 121 impr/2 clicks organic | Proven commercial demand, thin site treatment | B: structurally under-linked relative to its proven value |
| Kent (any town) | Out-of-footprint | No page (B) | No dedicated targeting confirmed | N/A | A: £134.23 spend, 3 conversions, £44.74 CPA | Real, efficient, currently unserved | G: not enough evidence yet — one geography, thin sample |
| Emergency | Essex-wide | `/services/emergency-scaffolding/` (B) | Presumed emergency LP (built in an earlier phase, not re-verified here) | Call CTA | A: 1 organic query, pos 6.65, 0 clicks, 201 impr; A: 2 paid search-term rows only, 1 conversion | Organic essentially absent; paid too thin to conclude | D: paid emergency performance under-sampled in this export |
| Price/cost | Any | `/guides/scaffolding-cost-essex/` (B) | N/A — actively negative-keyworded out (F) | N/A | A: 2 organic impressions/12mo; A: £9.18 paid spend/0 conv; A: `cost` is a broad negative | Triple-blocked across all three channels | Flagged for decision phase — cannot tell if deliberate |
| Guides (all three) | N/A | `/guides/*` (B: only reachable via one generic sitewide link + the hub) | N/A | "Read Guide" | A: 58 combined organic impressions, 0 clicks across all three guides | Effectively invisible | B: structurally isolated, now also confirmed externally invisible |
| Domestic scaffolding | Any | `/services/domestic-scaffolding/` | Blocked from the active campaign (F: `domestic` broad negative) | N/A | A: 649–3,439 impr (merged) organic, 0 clicks; B: real negative-keyword conflict found | Real service, real organic demand, actively excluded from paid | Flagged, not changed (F) |

---

## J. True Content/Page Gap Report

Classified per the requested taxonomy — **no page is proposed to be created, deleted, or modified.**

- **`/guides/*` (all three):** **D — improve internal linking (repository-confirmed) and re-evaluate discoverability once linked**, not F. The pages are not wrong or missing; they are unreachable in practice. Before concluding a *new* guide is needed, the existing three should get a fair test under real internal linking and, for the cost guide specifically, a fair test without the paid-side blanket block.
- **Cost/pricing intent:** **A — existing page is correct, improve relevance/authority is premature; the immediate issue is distribution, not content.** The guide exists and is reasonably scoped; it has simply never had a real chance to be found (Sections B, F). G — not enough evidence yet on whether its content itself needs work, because it's never been tested with traffic.
- **Emergency intent:** **D — improve internal linking / C — improve conversion pathway**, tentatively. The service page exists; the organic signal (one query, 0 clicks, position 6–7) is too thin to diagnose precisely without more data, but a position outside the top 5 for a single-word-intent query like "emergency scaffolding essex" is at minimum a linking/authority question, not a missing-page question.
- **Contractor/commercial intent:** **G — not enough evidence yet.** 77 organic queries generate 7,168 impressions and 0 clicks; 16 paid search terms generate £0 spend. This cluster needs its own dedicated pull (a `/contractors` page exists per the sitemap but recorded 0 impressions in the GSC Pages export in 12 months) before any page-role conclusion is safe.
- **Named towns (core 12):** **B — existing pages are correct, improve internal linking and CTR**, not F. The pages exist, rank respectably in places, and the gap is entirely in click realisation (Section B) and, per the site-side audit, in the indiscriminate service↔area graph diluting relevance per town.
- **London specifically:** **E is not applicable (the landing target itself is arguably fine) — this is squarely B: improve internal linking.** The commercial case (Section G) is unusually strong for a page currently treated as a footnote.
- **Kent:** **G — not enough evidence yet for a new page.** One geography, £134 spend, 3 conversions is real but thin; do not build a page from this alone. Worth a dedicated Kent-demand pull (GSC + Ads, Kent-specific) before this graduates past G.
- **Service-specific long-tail (chimney scaffold, extension scaffold, render scaffold, etc.):** **G.** 22–23 organic/paid rows each with negligible volume in this export — not enough to classify.

---

## K. Prioritised Opportunity Roadmap

**No implementation is proposed here — this ranks where the next decision-phase should look first, by evidence weight, not by search volume.**

### Tier 1 — strong evidence, high commercial value, ready for a decision-phase review
1. **`scaffolding hire` keyword's Quality Score / "Limited" status.** It is over half the account's conversions and is being throttled. Directly evidenced, unambiguous, highest leverage in the whole dataset.
2. **`domestic` broad-match negative keyword.** Directly evidenced conflict against a real, named service with confirmed organic demand. Cheap to verify, potentially meaningful to fix.
3. **London internal linking vs. proven paid value.** Direct evidence on both sides (repo: 1 inbound link; Ads: top-spending location, second-largest keyword). One of the clearest evidence-to-action lines in this whole audit.
4. **Guides' total lack of distribution.** Now confirmed externally (2–37 impressions per guide in 12 months) as well as structurally (repo). Low page count, low implementation complexity, previously-established high plausible value.
5. **The account-level £1,179.85 / 54-conversion blind spot (Section G).** Not a website or SEO question at all — it's a "what campaign type is this and why isn't it in any export we have" question, and it's more than half the account's conversions. Should be resolved before any other Ads decision is made, because it may change every percentage in this report's Ads sections.

### Tier 2 — promising, needs validation before acting
6. Kent as a potential coverage/page candidate — real and efficient, but one geography and a thin sample.
7. Out-of-footprint converting terms (Norwich, Coventry, Tunbridge Wells, Witham, Grantham, Erith) — real conversions, unclear whether coincidence, referral, or a genuine adjacent-market signal.
8. Price/cost triple-block — plausibly intentional (low historical quality), plausibly an accident; needs a decision-maker's judgement call, not more data.
9. Rayleigh's position-1 / zero-click pattern — worth a live rank-check and a look at whether these impressions are landing on the homepage instead of the area page, before concluding anything about CTR or content.
10. The out-of-area and residual-competitor paid leakage identified in Section F (~£150 combined) — small in isolation, mechanical to fix, low risk.

### Tier 3 — speculative, do not act yet
11. Emergency organic weakness — real but built on a single query row; needs its own dedicated pull.
12. Contractor/commercial intent — 0 clicks/0 spend on real volume; too undiagnosed to prioritise yet.
13. The long tail of 108 scattered UK-postcode location rows — a pattern, not yet an actionable list of candidates.
14. Service-specific long-tail queries (chimney, render, extension) — negligible volume in this export; not enough signal.

---

## L. Data Quality / Unknown Items

This section is not a footnote — several items here materially limit what can be claimed anywhere above.

1. **GSC query-level anonymisation:** 58% of the 12-month click total is not attributable to any named query (Chart total 100 clicks vs. Queries-export total 42). This is Google's standard behaviour for low-volume/potentially-identifying queries, not a configuration error, but it means the entire intent-cluster table in Section B is built on well under half the real click volume.
2. **Ads search-term anonymisation, the same pattern on the paid side:** 38% of "Total: Search" cost (£1,121.69 of £3,002.21) sits in "Other search terms," undisclosed by text.
3. **The account-type blind spot:** £1,179.85 and 54 conversions exist in "Total: Account" with no corresponding campaign-type breakdown available in any export provided. This is the single largest unresolved gap in this report.
4. **Two campaigns, one "All time" export, no per-period breakdown:** the Search Terms and Keywords exports blend an active campaign and a paused one under a single "All time" label with no way to separate by date in the files provided. Any earlier reference to "the campaign" without naming which of the two is now ambiguous and should be re-stated precisely going forward.
5. **Trailing-slash dual-indexation (Section C)** inflates apparent page-count and dilutes per-page metrics for 72% of pages; a query×page cross-tab (not available as a single GSC UI export) would be needed to fully unwind it.
6. **No "matched keyword" column in the Search Terms export** — the Section D/E keyword-to-term reconciliation gap (`scaffolding hire` £1,466 vs. text-matched "Hire/rental" £109) cannot be closed without a differently-configured pull.
7. **No GA4 raw export**, only four screenshots covering Events and Traffic Acquisition for one 28-day window. Landing-page-level, source/medium-level, and conversion-event-level GA4 data were not available and are not represented anywhere in this report.
8. **Location-report totals do not reconcile exactly with Search-Terms or Keywords totals** (£2,863.08 vs. £3,002.21 vs. £2,770.47) — a residual gap of roughly £90–£230 depending on which pair is compared, unexplained.
9. **The triple "Essex" row in the Location report** (three different bid adjustments under one location name) is not explained by any export available and was not resolved.
10. **Two identical uploads of the negative-keyword export were provided this session** (byte-for-byte identical) and were reconciled against the existing working copy with zero differences — noted for completeness, not a forensic finding.
11. **Playwright/browser-based live verification of the site was not usable this session** (a proxy/tunnel issue blocked headless Chromium specifically; plain HTTPS requests worked normally). Live-site claims in this report (redirect behaviour, canonical tags) are based on direct HTTP requests, not a full rendered-browser crawl.

---

## M. "Do Not Change Yet" List

Explicitly frozen pending the external-data-informed decision phase, or pending information this audit could not obtain:

- **Do not touch the `scaffolding hire` keyword, its bid, or its Quality Score inputs** until the account-level blind spot (L.3) and the keyword↔search-term reconciliation gap (L.6) are resolved — changing the account's best performer without knowing what else is happening in the other 54 conversions is premature.
- **Do not remove or edit the `domestic` (or `home`/`free`) negative keywords** — flagged as a likely-unintended conflict, but "likely" is not "confirmed intent," and a decision-maker should confirm before any negative list is touched.
- **Do not build a Kent page, or any page for the scattered long-tail locations in Section G**, on the strength of this data alone — real but thin.
- **Do not conclude the Rayleigh position-1/zero-click pattern is a CTR or content problem** — the property-scope, canonical, and reporting-artifact explanations were not fully separable from this export set.
- **Do not resolve the Price/Cost triple-block either way** (leave the `cost`/`price` negatives, the guide page, and its lack of paid targeting exactly as they are) until a decision-maker confirms whether the original exclusion was deliberate.
- **Do not act on the account-vs-Search conversion gap by assumption** — the Campaigns-by-type pull (Section N) has narrowed but not closed it; one further read-only check (re-pulling with Removed campaigns included) is identified and should happen before any budget or attribution conclusion is drawn from it.
- **Do not change the site's cookie-consent/GA4-loading architecture** on the basis of the low GA4 session count — that count is expected under the current, deliberate consent design, not a bug.
- **No code, content, schema, redirects, internal links, Google Ads settings, GSC settings, or GA4 configuration were changed in the process of producing this report**, consistent with the stop condition this phase was scoped to.

---

## N. Final Reconciliation — Campaigns-by-Type Pass — CLOSED

**Status: this pass is now closed by the account owner's decision, not because the gap is explained. It narrowed the account-level discrepancy and yielded one new, decision-relevant conclusion (on `scaffolding hire`), but did not fully close the original gap, and the account owner has chosen not to pursue the one remaining check (Ad state → Removed) further at this time. PR #43 remains in draft. No implementation follows from this section.**

### Source and scope

Unlike the five raw CSV exports used in Sections A–M, this pass is based on a **live Campaigns-view screen capture** provided directly in chat, not a downloaded file. This is a materially different kind of evidence and is treated with more caution:

- **View:** Google Ads Campaigns table, account "Axis Scaffolding Essex" (MJ AdSystems), captured twice in succession (the second capture showed 22,604 impressions vs. 22,602 in the first — a 2-impression drift consistent with a few minutes of real-world accrual, everything else identical).
- **Filter shown:** `Ad state is Enabled, Disabled`. This explicitly **excludes any Removed (deleted) campaign** — that exclusion is itself part of the reconciliation below, not an oversight in reading it.
- **Date range: confirmed by the account owner as "All time."** This closes the one open question from the first pass of this section. **(A)** Every figure below is therefore treated as a genuine all-time total for the two campaigns shown, not a possible shorter-window artifact.
- Two campaigns are shown, both **Campaign type: Search**. No Performance Max, Display, Demand Gen, Video, Shopping, or Local campaign appears anywhere in this view.

### Totals as provided (A — directly evidenced, transcribed exactly, no re-derivation)

| Campaign | Status | Type | Clicks | Impr. | CTR | Avg. CPC | Cost | Impr. (Top) % | Impr. (Abs. Top) % | Conversions | Conv. value | Cost/conv. | Conv. rate |
|---|---|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Phone calls Campaign - Axis High Intent | Enabled | Search | 560 | 18,438 | 3.04% | £4.75 | £2,659.14 | 21.25% | 51.41% | 36.00 | 0 | £73.86 | 6.43% |
| Axis Scaffolding \| High Intent | Paused | Search | 134 | 4,164 | 3.22% | £2.01 | £269.62 | 18.06% | 54.64% | 3.00 | 0 | £89.87 | 2.24% |
| **Total** | — | — | **694** | **22,602** | 3.07% | £4.22 | **£2,928.76** | 20.66% | 52.01% | **39.00** | **0** | £75.10 | 5.62% |

**Conv. value = 0 for both campaigns.** No conversion-value/revenue tracking is configured at the account level. This is an independent cross-confirmation of the GA4 screenshot finding in Section H, which also showed £0.00 total revenue — two unrelated sources agreeing on the same underlying fact.

### Reconciliation arithmetic — three separate comparisons, none silently merged

**1. Campaigns total vs. "Total: Search" (Search Terms export, pulled 2026-09-05, labelled "All time"):**

| | Clicks | Cost | Conversions |
|---|--:|--:|--:|
| Total: Search (Search Terms export) | 743 | £3,002.21 | 40.00 |
| Campaigns view total (this pass, confirmed All time) | 694 | £2,928.76 | 39.00 |
| **Difference** | **−49** | **−£73.45** | **−1.00** |

With the date range now confirmed as "All time" on both sides, **the earlier "shorter window" explanation for this gap is ruled out.** Two genuinely all-time pulls of what should be the same underlying figure disagree by 49 clicks, £73.45, and 1 conversion. **(D)** This small gap is now itself unexplained — plausible mundane causes (a few minutes of accrual between when the CSV export was generated on 2026-09-05 and when this live view was captured later in this conversation; minor rounding in how the Search Terms export computes its own subtotal row) remain the leading candidates, but none is confirmed. It is minor in absolute terms and does not change any conclusion in this report, but per instruction it is not smoothed over.

**2. Campaigns total vs. "Total: Account" (Search Terms export, same file, same "All time" label):**

| | Clicks | Cost | Conversions |
|---|--:|--:|--:|
| Total: Account (Search Terms export) | 3,449 | £4,182.06 | 94.00 |
| Campaigns view total (this pass) | 694 | £2,928.76 | 39.00 |
| **Difference** | **2,755** | **£1,253.30** | **55.00** |

This is the core discrepancy this pass was commissioned to close. **It is not closed.** What this pass does establish directly:

- **(A) Ruled out with high confidence:** items 2–7 on the requested checklist (Performance Max, Display, Demand Gen, Video, Shopping, "other campaign types") — the account has exactly two campaigns and both are Search. If a third, Removed campaign existed, it would not appear in this "Enabled, Disabled" view, so this rules out *additional currently-active or paused* campaign types, not necessarily historical ones (see below).
- **(A) Also now ruled out:** item 11, date-range differences. The account owner has confirmed this Campaigns view is scoped to All time, the same label as the Search Terms export. Two genuinely all-time totals still disagree by £1,253.30 and 55 conversions, so a scope mismatch is no longer an available explanation for this specific gap — which sharpens, rather than weakens, the case for a structural cause.
- **(C) Now the single leading candidate** — item 8/14 on the requested checklist (reporting-scope difference / "other identifiable reporting mechanism"): a **removed/deleted campaign** that existed earlier in the account's history. "Total: Account" in a search-terms export is a lifetime rollup that is not filtered by current campaign status; a campaign that was deleted (not merely paused) would still count toward that lifetime figure but would be invisible to an "Enabled, Disabled" Campaigns-view filter. This mechanism would fully explain both the missing campaign-type coverage and the missing conversions in one stroke — but it is **not confirmed**, only the best-fitting hypothesis against the evidence actually available, and it is now the *only* candidate from the original checklist that hasn't been either ruled out or left unaddressed.
- **The one further read-only check that would resolve this, unambiguously, without touching anything:** re-open the same Campaigns view (All time is already confirmed) and change the **Ad state filter to include Removed** alongside Enabled and Disabled. If a third campaign appears with roughly 2,755 clicks / £1,253.30 / 55 conversions, the gap is explained. If no third campaign appears and the two existing campaigns' all-time totals still fall short of "Total: Account," the gap remains genuinely unexplained and would need Google Ads support-level investigation (e.g. a historical account merge, an MCC-level rollup artifact, or a conversion-action change that retroactively affected reporting) — outside what any export-based audit can resolve.

**This gap is preserved as unresolved, per instruction, not assumed closed.**

**3. Campaigns total vs. Keywords export (93 rows, summed independently in Section D/E, no official "Total:" row of its own to cross-check against):**

| | Clicks | Cost | Conversions |
|---|--:|--:|--:|
| Keywords export (summed) | 632 | £2,770.47 | 39.00 |
| Campaigns view total (this pass) | 694 | £2,928.76 | 39.00 |
| **Difference** | **+62** | **+£158.29** | **0.00** |

**Conversions match exactly (39 = 39).** This is the most reassuring reconciliation point in this entire pass: every conversion recorded at the campaign level is also accounted for at the keyword level, with no residual "unattributed conversions" gap between the two. Clicks and cost each carry a small (~9%/5%) residual gap, most plausibly the same short-window/pull-timing effect noted in comparison 1 above — **(C)**, not confirmed.

### Answering the four specific sub-questions on `scaffolding hire`

> A. Does the £1,466.31 / 52.9%-of-keyword-spend figure represent genuine campaign-level spend?

**(A) Yes, with high confidence, and slightly strengthened by this pass.** £1,466.31 is 50.1% of this pass's own campaign-level total cost (£2,928.76) — closely in line with the 52.9%-of-keyword-level-cost figure already reported. The small residual gap between keyword-level and campaign-level totals (comparison 3 above, £158.29) is not large enough to materially change this conclusion either way.

> B. Is the 61.5% conversion share genuinely attributable to that keyword?

**(A) Yes — this sub-question is now more confidently answered than before this pass.** Because campaign-level conversions (39.00) match keyword-level conversions (39.00) **exactly**, there is no room for a large pool of campaign-level conversions sitting outside named keywords that could be silently diluting or inflating `scaffolding hire`'s apparent 61.5% share (24 of 39). The share is real, at both levels of the account's own reporting.

> C. Does the search-term report's export/matching limitation prevent full attribution to that keyword?

**(A) Yes — unchanged by this pass, and this pass does not and cannot resolve it.** This pass adds no search-term-level data. The original finding stands exactly as reported in Section D/E: the Search Terms export has no "matched keyword" column, so the £1,466.31-vs-£109.40 mismatch between `scaffolding hire`'s keyword-level spend and the text-matched "Hire/rental" search-term category remains open, and the most likely explanation (broad-match semantic expansion capturing queries that don't literally contain "hire") remains an inference, not a fact.

> D. Does the relationship remain unresolved?

**Partially.** The *conversion* side of the `scaffolding hire` finding (sub-question B) is now well-supported by cross-level agreement. The *spend* side (sub-question A) is supported but carries a small unexplained residual. The *search-term attribution mechanism* (sub-question C) remains genuinely unresolved and requires an export this audit does not have access to.

### Does the 54/55-conversion discrepancy affect any other finding already in this report?

- **`scaffolding hire` (Section D/E):** No material effect — addressed directly above; if anything, this pass increases confidence in the conversion-share finding.
- **London (Section A.8, G):** No effect. London's figures come from the Location report, which is a separate export from the account/Search totals question; nothing in this pass touches location-level data.
- **Kent (Section A.9, G):** No effect, same reason.
- **Competitor traffic (Section F):** Not addressed by this pass — campaign-level totals do not break out competitor-term spend; that reconciliation still rests entirely on the Search Terms export's own text classification (Section D), unchanged.
- **Local generic traffic (Section D, category 1):** Not addressed by this pass for the same reason — no campaign-level breakdown by search-term category exists in what was provided.
- **The trailing-slash finding (Section C), the `domestic`/`cost` negative-keyword findings (Section F), and the GA4 findings (Section H):** No effect — all independent of the account-level Ads accounting question.

### What remains unknown, stated exactly (per instruction, not smoothed over)

- The **date range is confirmed as All time** (account owner, this section) — no longer an open question.
- A **small, separately unexplained gap (49 clicks / £73.45 / 1 conversion)** exists between this all-time Campaigns total and the Search Terms export's own all-time "Total: Search" row. Minor, not investigated further, not affecting any conclusion.
- The **£1,253.30 / 55-conversion gap between the Campaigns-view total and "Total: Account"** is **not closed and is not being pursued further at this time** — the account owner has chosen to stop this reconciliation pass here rather than run the one remaining check (Ad state → Removed). It is documented as genuinely unresolved, not as resolved-by-inference and not as dismissed.
- **What additional check would close it, if revisited later:** the same Campaigns view (All time already confirmed), re-pulled with the Ad state filter expanded to include Removed. If that still does not reconcile, a request to Google Ads support or an MCC-level account history review would be the next step — beyond what any further CSV export or UI view can resolve alone.
- **Conversion value / revenue tracking (£0 across both campaigns, and £0.00 in the GA4 screenshots):** noted as a fact in this section, explicitly **not investigated further at the account owner's direction.** This is not evidence that revenue tracking is broken, misconfigured, or unimportant — it is simply out of scope for this forensic pass. It is not added to Section K's opportunity roadmap and should not be treated as prioritised or de-prioritised by its absence there.

**No conclusion in Sections A–M is withdrawn as a result of this pass, apart from the specific "other campaign type" phrasing in A.7, which is corrected above. This reconciliation pass is now closed.** PR #43 remains in draft; the audit (Sections A–N) is complete and ready for review as one evidence package, per the account owner's stated plan. No decision or implementation phase has begun.
