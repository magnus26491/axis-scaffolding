# Axis Search Intelligence Map

**Status: analysis only. No site code, Google Ads, or Google Search Console changes were made to produce this document.**
Phase D of the roadmap — the first phase to use the real GSC/Ads exports supplied earlier and set aside since. This document is the evidence base for Phase E (evidence-based website improvements) and Phase F (Search Console / Ads optimisation) — it does not itself implement anything.

## 0. Data sources and honest limitations

| Source | Window | Rows |
|---|---|---|
| GSC Performance — Queries.csv | Aug 26 – Sep 1, 2026 (latest pull) | 571 queries |
| GSC Performance — Pages.csv | Aug 26 – Sep 1, 2026 | 45 pages |
| GSC Performance — Queries/Pages.csv | Jul 26 – Aug 26, 2026 (earlier pull, used only to confirm patterns hold across time) | — |
| Ads Search terms report | Aug 1 – Sep 1, 2026 | 251 terms (all under one ad group) |
| Ads Search keyword report | Jul 27 – Aug 25, 2026 | 93 configured keywords |
| Ads Location report | Aug 1 – Sep 1, 2026 | 126 locations |
| Ads Negative keyword report | All time | 429 entries |

**Limitation stated plainly**: GSC's standard export gives Top Queries and Top Pages as two *separate* marginal tables, not a joined query-by-page table. Where this document says a query's "Intended page" is `/areas/rayleigh`, that means *the page that should answer this query given the current site architecture* — not a confirmed record of which URL Google actually displays. Where I can prove non-attribution (a town's dedicated page has zero recorded impressions despite large query volume for that town), I say so explicitly and treat it as strong circumstantial evidence, not certainty. The Ads spend total in this window (~£300 across the two overlapping Aug reports) is small — geographic/keyword conversion-rate conclusions below are kept directional, not treated as statistically solid on an n of 1–2 conversions.

## 1. Organic map — Query → Page → Intent → Opportunity → Action

Full 572-row classified table delivered separately as `axis_organic_queries_mapped.csv`. Top 35 by impression volume:

| Query | Clicks | Impr. | CTR% | Pos | Intent | Intended page | Opportunity |
|---|---|---|---|---|---|---|---|
| scaffolding essex | 1 | 1461 | 0.07 | 30.1 | Homeowner/Local | `/` | Buried position, real demand |
| domestic scaffolding essex | 0 | 526 | 0.0 | 30.0 | Homeowner/Local | `/services/domestic-scaffolding` | Mid-table |
| commercial scaffolding essex | 0 | 521 | 0.0 | 34.0 | Trade/Commercial | `/services/commercial-scaffolding` | Buried position, real demand |
| scaffolding rayleigh | 1 | 488 | 0.2 | 4.2 | Homeowner/Local | `/areas/rayleigh` | Top-10 position, very low CTR |
| scaffolding southend | 1 | 481 | 0.21 | 28.6 | Homeowner/Local | `/areas/southend` | Mid-table |
| scaffolding in essex | 0 | 435 | 0.0 | 25.2 | Homeowner/Local | `/` | Mid-table |
| scaffolding chelmsford | 0 | 396 | 0.0 | 47.6 | Homeowner/Local | `/areas/chelmsford` | Buried position, real demand |
| commercial scaffolding rayleigh | 0 | 371 | 0.0 | 1.4 | Trade/Commercial | `/areas/rayleigh` | Top-10 position, zero clicks |
| scaffolders rayleigh | 0 | 345 | 0.0 | 3.1 | Homeowner/Local | `/areas/rayleigh` | Top-10 position, zero clicks |
| scaffolders essex | 0 | 327 | 0.0 | 39.1 | Homeowner/Local | `/` | Buried position, real demand |
| scaffolders benfleet | 0 | 321 | 0.0 | 20.3 | Homeowner/Local | `/areas/benfleet` | Mid-table |
| industrial scaffolding southend | 0 | 291 | 0.0 | 30.2 | Trade/Commercial | `/areas/southend` | Buried position, real demand |
| specialist scaffolding rayleigh | 0 | 278 | 0.0 | 1.6 | Homeowner/Local | `/areas/rayleigh` | Top-10 position, zero clicks |
| scaffolding hire rayleigh | 0 | 266 | 0.0 | 4.1 | Homeowner/Local | `/areas/rayleigh` | Top-10 position, zero clicks |
| commercial scaffolding chelmsford | 0 | 266 | 0.0 | 45.5 | Trade/Commercial | `/areas/chelmsford` | Buried position, real demand |
| scaffolding benfleet | 0 | 256 | 0.0 | 18.6 | Homeowner/Local | `/areas/benfleet` | Mid-table |
| scaffold hire essex | 0 | 253 | 0.0 | 70.3 | Homeowner/Local | `/` | Buried position, real demand |
| scaffolding basildon | 1 | 241 | 0.41 | 45.8 | Homeowner/Local | `/areas/basildon` | Buried position, real demand |
| scaffolding company essex | 0 | 240 | 0.0 | 37.3 | Homeowner/Local | `/` | Buried position, real demand |
| scaffolding in rayleigh | 0 | 233 | 0.0 | 2.0 | Homeowner/Local | `/areas/rayleigh` | Top-10 position, zero clicks |
| scaffolding brentwood | 0 | 232 | 0.0 | 39.8 | Homeowner/Local | `/areas/brentwood` | Buried position, real demand |
| scaffolding company rayleigh | 0 | 228 | 0.0 | 2.0 | Homeowner/Local | `/areas/rayleigh` | Top-10 position, zero clicks |
| domestic scaffolding rayleigh | 0 | 223 | 0.0 | 8.0 | Homeowner/Local | `/areas/rayleigh` | Top-10 position, zero clicks |
| residential scaffolding essex | 0 | 207 | 0.0 | 28.2 | Homeowner/Local | `/services/residential-scaffolding` | Mid-table |
| scaffolding company southend | 0 | 204 | 0.0 | 32.7 | Homeowner/Local | `/areas/southend` | Buried position, real demand |
| scaffolding services essex | 0 | 202 | 0.0 | 44.1 | Homeowner/Local | `/` | Buried position, real demand |
| scaffolding company benfleet | 0 | 201 | 0.0 | 26.0 | Homeowner/Local | `/areas/benfleet` | Mid-table |
| scaffolding hire benfleet | 0 | 198 | 0.0 | 37.3 | Homeowner/Local | `/areas/benfleet` | Buried position, real demand |
| commercial scaffolding southend | 0 | 195 | 0.0 | 27.9 | Trade/Commercial | `/areas/southend` | Mid-table |
| scaffolding wickford | 0 | 193 | 0.0 | 23.5 | Homeowner/Local | `/areas/wickford` | Mid-table |
| emergency scaffolding essex | 0 | 189 | 0.0 | 6.8 | Emergency | `/services/emergency-scaffolding` | Top-10 position, zero clicks |
| scaffolding rochford | 1 | 188 | 0.53 | 13.4 | Homeowner/Local | `/areas/rochford` | Mid-table |
| industrial scaffolding essex | 0 | 185 | 0.0 | 62.1 | Trade/Commercial | `/services/commercial-scaffolding` | Buried position, real demand |
| domestic scaffolding chelmsford | 0 | 183 | 0.0 | 37.0 | Homeowner/Local | `/areas/chelmsford` | Buried position, real demand |
| scaffolding in southend | 0 | 175 | 0.0 | 32.4 | Homeowner/Local | `/areas/southend` | Buried position, real demand |

### Opportunity distribution across all 572 queries

| Opportunity | Queries | Total impressions |
|---|---|---|
| Buried position, real demand (pos > 30, impr ≥ 50) | 85 | 11,069 |
| Mid-table | 195 | 12,318 |
| Top-10 position, zero clicks | 46 | 5,871 |
| Low volume (< 15 impr) | 244 | 966 |
| Top-10 position, very low CTR | 1 | 488 |
| Working (clicks > 0, CTR ≥ 2%) | 1 | 88 |

Two structurally different problems, not one:

- **"Buried position, real demand" (85 queries, 11,069 impressions)** — the page genuinely doesn't rank. This is Essex-wide generic queries, Chelmsford, Southend, Basildon, Brentwood. Fixing this needs real content depth and authority-building (Phase E territory), not a quick technical fix.
- **"Top-10 position, zero clicks" (46 queries, 5,871 impressions)** — the opposite problem: the site (or something) already ranks well, but nobody clicks. This cluster is dominated almost entirely by one town.

### The Rayleigh anomaly — confirmed with harder evidence than the earlier session had

Every Rayleigh-modified query ranks at position 1–8 (`commercial scaffolding rayleigh` at **1.4**, `specialist scaffolding rayleigh` at **1.6**, `scaffolding in rayleigh` at **2.0**) yet generates almost zero clicks. Total Rayleigh-query impressions this window: **5,542** — the single largest town cluster in the data, ahead of Benfleet (3,728) and Southend (3,626).

Checked directly against `Pages.csv`: **`/areas/rayleigh` does not appear anywhere in the Pages report** — not truncated, the full 45-row export was read in full. A page cannot register thousands of query impressions across dozens of distinct Rayleigh-phrase queries while itself showing zero recorded impressions, unless those impressions are being attributed to a *different* URL (almost certainly the homepage, which is the only other page with the scale of impressions to absorb this: 23,740 in this window alone).

This is not the same shape of problem as every other town. Compare the top queries for Benfleet, Southend, Chelmsford, and Basildon — all sit at position 18–70, a normal "not ranking well yet" pattern. Rayleigh is the only town where the position is excellent and the click-through is broken anyway. Two testable explanations, not resolved here:

1. **Cannibalisation** — Google is showing the homepage for these queries, and its title/snippet ("Scaffolding in Essex for Homes, Roofers, Builders & Commercial Projects") reads as generic against a query as specific as "scaffolding company rayleigh", so users skip past it even at position 1–8.
2. **Rank-tracking / bot traffic** — some portion of these impressions may not be real human searchers at all.

Both were flagged as hypotheses in the earlier session; this pull adds the decisive piece of evidence (zero page-level attribution, re-confirmed on the freshest data) that narrows it toward hypothesis 1. Phase E should resolve this properly (a manual incognito SERP check for 2–3 of these exact phrases, or GSC's URL Inspection tool, settles it definitively) before acting — not guess.

### Secondary top-10-zero-click case

`emergency scaffolding essex` — position 6.8, 189 impressions, 0 clicks. Smaller than the Rayleigh cluster but the same shape: good position, no clicks. Worth the same kind of manual SERP check, lower priority than Rayleigh given the volume gap.

## 2. Paid map — Search Term → Keyword → Campaign → Landing Page → Cost → Conversion → Intent → Action

**Structural finding first**: the account runs a single campaign ("Phone calls Campaign - Axis High Intent") with a single ad group ("Axis-Scaffolding Ltd | Scaffolding Solutions | Essex UK") — all 251 classified search terms and all 93 configured keywords sit under that one ad group. Every keyword's **Final URL field is blank** — meaning there is no keyword-to-landing-page segmentation at all; every click currently lands on whatever the campaign's single default destination is. There is no "Landing Page" column to report per keyword because none is configured — that absence is itself the finding.

### Top spend keywords (from the configured Search Keyword report, Jul 27 – Aug 25)

| Keyword | Match type | Status | Cost | Clicks | Conversions | Read |
|---|---|---|---|---|---|---|
| scaffolding hire | Broad match | Limited | £119.05 | 29 | 0 | Broad match on "hire" is pulling in DIY/plant-hire searchers, not supply-and-erect customers — the single biggest cost driver in the account with zero return |
| scaffolding london | Broad match | Eligible | £72.97 | 15 | 1 | The account's one clearly-attributed conversion. Real evidence the London expansion tier (unified into the current site in Phase B) has genuine commercial value, not just an architectural nice-to-have |
| [scaffold firms near me] | Exact match | Limited | £33.75 | 7 | 0 | Core local intent, exact match, zero conversions — worth watching, not yet enough volume to condemn |
| [scaffolding chelmsford] | Exact match | Limited | £29.52 | 5 | 0 | Matches the organic finding — Chelmsford has real demand and no traction yet, paid or organic |
| "scaffolding near me" | Phrase match | Limited | £23.08 | 4 | 1 | Second conversion source |
| [scaffolding colchester] | Exact match | Limited | £13.34 | 4 | 0 | Colchester is outside the declared 12-town core area and the 3-town expansion tier — spend leaking to an undeclared area |

### Search-terms classification totals (251 terms, Aug 1 – Sep 1)

| Classification | Terms | Cost | Conversions |
|---|---|---|---|
| Core local service intent | 52 | £129.14 | 1 |
| Possible competitor brand name | 125 | £37.56 | 0 |
| Outside core service area | 26 | £15.91 | 0 |
| Generic — ambiguous | 2 | £24.63 | 0 |
| Unclassified | 22 | £0.65 | 0 |
| Expansion-tier area | 12 | £0.00 | 0 |
| Equipment/plant-hire intent | 10 | £0.00 | 0 |
| Already excluded | 2 | £0.00 | 0 |

"Possible competitor brand name" is the largest single bucket by term count (125 of 251 — half) but the classifier itself flags this tier as **not certain** (pattern-matched on "`<name> scaffolding`" with no generic qualifier — could genuinely be brand-name competitor searches, or could be a real local business name pattern this classifier can't distinguish). Needs a human read of the actual list before any negative-keyword action, not an automated exclusion.

### Geographic spend (Location report, Aug 1 – Sep 1, 126 locations, £301.45 total, 1 conversion)

74.8% of spend (£225.63) sits on locations with zero recorded conversions — but with only 1 total conversion in the window, that ratio isn't statistically meaningful on its own. What *is* meaningful, because it corroborates the search-terms finding independently: real spend is landing on postcodes and towns outside the declared area — Chatham, Maidstone, DA1/DA2 (Kent), South Ockendon and Grays (Thurrock), CM postcodes beyond Chelmsford. Two independent Ads reports (search terms and locations) point at the same out-of-area leakage, which is stronger evidence than either alone.

## 3. Combined map — Intent → Best Page → Supporting Guide → Real Project → Local Area → CTA

Cross-checked against the real `PROJECTS` and `AREA_DATA` tagging in `build_site.py` — not assumed.

| Intent | Best page | Supporting guide | Real project evidence? | CTA |
|---|---|---|---|---|
| Homeowner, core town (Rayleigh, Benfleet, Chelmsford, Southend, Basildon…) | `/areas/{town}` | `/guides/scaffolding-cost-essex` | Yes for 11 of 12 core towns (Hockley has none tagged) | Embedded quote form on the area page |
| Homeowner, general/no town given | `/services/residential-scaffolding` or `/services/domestic-scaffolding` | `/guides/do-i-need-scaffolding` | Yes — 5 residential + 2 domestic tagged | Quote form |
| Trade/Commercial | `/services/commercial-scaffolding` or `/contractors` | `/guides/highway-licence-scaffolding` (CDM/licence-adjacent) | Yes — 3 tagged commercial projects | Trade enquiry / quote |
| Emergency | `/services/emergency-scaffolding` | None — speed matters more than research content for this intent | **No tagged projects** (known gap, not fabricated) | Phone number, primary |
| Info/Research (cost, licence, "do I need") | The matching `/guides/*` page | Cross-links to the other 2 guides | N/A | Guide's own quote CTA |
| Brand ("axis scaffolding") | `/` | N/A | N/A | Quote |
| Expansion tier (London, Brentwood, Loughton) | `/areas/{town}` (unified into current V2 system in Phase B) | `/guides/scaffolding-cost-essex` | **No tagged projects** — honestly links to `/gallery` instead, per Phase B | Embedded quote form (same as core towns since Phase B) |
| Equipment/plant-hire ("scaffolding hire", tower/ladder searches) | **Not a target for any page** | — | — | Recommend as a negative-keyword candidate in Phase F, not a landing-page fix |
| Out-of-area (Colchester, Maidstone, Chatham, Kent postcodes, Dartford) | **Not a target under the current declared service area** | — | — | Same — a Phase F negative-keyword/geo-targeting decision, not a content decision |

Two real content/evidence gaps this table surfaces on its own, independent of the search data: **Hockley** (a real core-tier town) and **emergency-scaffolding** (a real, high-intent service) both lack tagged project photos. Both were already known from earlier phases — repeated here because the search-intelligence lens confirms they're not just administrative gaps, they're gaps in exactly the areas/services generating real search demand.

## 4. Priority order for Phase E (not actioned here)

1. **Resolve the Rayleigh attribution question with a direct check** (manual SERP / URL Inspection) before deciding what, if anything, to change — this is the single largest organic opportunity in the data (5,542 impressions) and the cheapest to verify.
2. **Chelmsford, Southend, Basildon, Brentwood organic depth** — these are "buried position, real demand" towns with thousands of combined impressions and genuinely poor rankings. This is real content/authority work, not a quick fix.
3. **The "scaffolding hire" broad-match keyword** — £119 of the ~£300 window spend with zero conversions, almost certainly wrong-intent traffic. A Phase F decision (tighten match type or add negatives), not a website change.
4. **Out-of-area paid leakage** (Colchester, Kent postcodes, Thurrock) — corroborated by two independent Ads reports. A Phase F geo-targeting/negative-keyword decision.
5. **"Possible competitor brand name" bucket (125 terms)** — needs a human read before any exclusion action; the classifier itself isn't confident here.

## 5. Confirmation

**£5m insurance claim**: unchanged, still OWNER VERIFICATION REQUIRED, not propagated. **4 services without tagged project photos**: unchanged, still a genuine content gap requiring real photography, nothing invented. No Google Ads settings were changed. No Google Search Console settings were changed. No site code was changed. This document is evidence, not action.
