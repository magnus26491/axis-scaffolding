# Axis Paid Search Restructure — Phase F

**Status: evidence-led specification, not a live account change.** This session has no Google Ads account access, no Google Ads API/MCP tool, and no way to read or write the live account. Everything below is built from the four real exports already supplied (Search keyword report, Search terms report, Location report, Negative keyword report) plus the live website architecture. Section 0 states exactly what that does and doesn't let this phase do, before anything else.

## 0. What this phase could and couldn't do — read this first

**Could do, from the four real exports (re-examined in full, not just the columns Phase D used):**
- Full keyword-level inventory: both campaigns, every keyword, match type, status, Final URL — §1.
- Full 251-term search-term reclassification into the requested 8-category taxonomy — §2.
- Full 126-location geographic breakdown — §3.
- Full 430-row negative-keyword audit, including catching an existing negative that conflicts with the site's own content — §9.
- A proposed campaign/ad-group/landing-page architecture built only from what the data actually supports — §6–8.
- Draft ad copy using only claims already `VERIFIED`/`Established` in `CLAIM_VERIFICATION.md` — §8.

**Could not do — genuinely missing, not guessed at:**
- **Bidding strategy, budgets, ad schedules, audience settings, and the actual location-targeting mode** (Presence vs. "Presence or interest") — none of these appear in any of the four exports. §11 and §13 are built on inference from performance data, flagged everywhere they are.
- **Existing ad copy** — no Ads/RSA report was supplied, so §8 audits nothing; it proposes new copy for the recommended structure instead, clearly labelled as proposed, not implemented.
- **Conversion-action configuration** (which action is primary, whether GA4 imports are wired in, call-duration thresholds) — the reports show a `Conversions` count, not what's behind it. §12 documents this gap rather than guessing.
- **Live implementation.** There is no Google Ads config file in this repository — restructuring the account itself has to happen in the Google Ads UI, by whoever holds account access. This PR is the specification for that work, matching the pattern of the diagnosis-only PRs earlier in this project (E1, E2): a documented, evidence-backed plan, not a claim of changes made.

## 1. Current account structure (Phase 1 — forensic audit, from real data)

Two campaigns exist, not one — Phase D's map only surfaced the active one, because the search-terms report it used only covers that campaign:

| Campaign | Status | Ad group | Keywords | Negatives attached |
|---|---|---|---|---|
| **Phone calls Campaign - Axis High Intent** | Active | Axis-Scaffolding Ltd \| Scaffolding Solutions \| Essex UK | 57 | 341 |
| **Axis Scaffolding \| High Intent** | **Paused** (every keyword's status reason includes "campaign paused") | Ad group 2 | 36 | 89 |

**The paused campaign is a real duplicate-structure finding.** Its 36 keywords cover much of the same ground as the active one (`scaffold hire`, `scaffolding near me`, `scaffolding company`, `scaffolding london`, `domestic scaffolding`, `residential scaffolding`, `emergency scaffolding`, plus several tower/mobile-scaffold-hire terms) and it carries its own 89 negative keywords, sitting dormant. It has zero spend, clicks or impressions in every export — consistent with genuinely being paused, not a live source of hidden spend. It's covered as an architecture decision in §6, not treated as urgent.

**Active campaign, keyword-level (57 keywords):**
- 38 Paused, 19 Enabled.
- Of the 19 Enabled: 9 `Eligible`, 10 `Limited` (mostly `low quality`).
- Match type split: 25 Phrase, 20 Exact, 12 Broad.
- **Every single keyword's Final URL field is blank** — zero segmentation, confirming Phase D's original finding still holds exactly.
- Only 8 keywords have any recorded spend at all; the other 49 are dormant (paused or enabled-but-never-served).

**Total spend, active campaign, keyword report window (27 Jul – 25 Aug):** £316.35 / 68 clicks / 2 conversions.

## 2. Search-term re-classification (Phase 2 — re-checked against current data, 8-category taxonomy)

251 search terms (search-terms report, 1 Aug – 1 Sep), reclassified into the requested taxonomy rather than reusing Phase D's own five-bucket scheme:

| Category | Terms | Cost | Clicks | Conversions | Impr. |
|---|---|---|---|---|---|
| Core local service | 52 | £110.35 | 19 | 0 | 247 |
| Competitor (brand-name pattern) | 139 | £43.53 | 10 | 0 | 263 |
| Ambiguous (generic, no town/qualifier) | 7 | £43.42 | 8 | **1** | 234 |
| Expansion geography — out-of-area/undeclared | 17 | £10.59 | 3 | 0 | 55 |
| Other (unclassifiable from the term alone) | 20 | £0.00 | 0 | 0 | 26 |
| Expansion geography — London/Brentwood/Loughton | 11 | £0.00 | 0 | 0 | 29 |
| Equipment / plant hire | 5 | £0.00 | 0 | 0 | 5 |
| Employment / job-seeker | 0 | — | — | — | — |
| Irrelevant | 0 | — | — | — | — |

Total: 251 terms, £207.89, 40 clicks, 1 conversion (this window; the keyword report's slightly earlier, overlapping window shows a second conversion — see §2c).

**a. Competitor is the largest bucket by term count (139/251, 55%) but the smallest meaningful cost driver (£43.53, 21% of spend).** The pattern is consistent and specific: short opaque initialisms (`abs scaffolding`, `acs scaffolding`, `ags scaffolding`) and surname-style names (`curtis scaffolding`, `cooks scaffolding`, `brisko scaffolding`, `eco scaffolding`, `absolute scaffolding`) — exactly the naming convention of real, independent UK scaffolding firms, not a generic-phrase false positive. This is a firmer read than Phase D's "not certain — needs a human read" caveat, but the underlying list (now in `axis_paid_search_terms_classified_v2.csv`, delivered alongside this PR) is still worth a human skim before wholesale negative-matching, per §9.

**b. Ambiguous is small (7 terms) but holds the account's only recorded conversion in this window** — `scaffolding near me` (£15.42, 3 clicks, 1 conversion), plus `scaffolding` (£24.63, 4 clicks, 0) and `scaffolders near me` (£3.37, 1 click, 0). This is exactly the category the brief warned against mishandling: these are not noise to be negative-matched away, they're the account's best-performing terms per click. Protected explicitly in §9.

**c. Two conversions total, not one, across the two overlapping windows examined.** The keyword report (27 Jul – 25 Aug) shows conversions on both `scaffolding london` (broad match, £72.97, 15 clicks, 1 conv.) and `scaffolding near me` (phrase match, £23.08, 4 clicks, 1 conv.) — 2 total. The later search-terms window (1 Aug – 1 Sep) only captures the `scaffolding near me` one, because the London conversion most likely landed before 1 Aug. This refines, not overturns, the London finding from Phase D and the brief: London still has one real, attributed conversion, and it is not the account's only one — "near me" has an equally real, independently-attributed conversion. Both are treated as evidence in §8 and §9; London gets a dedicated section because of the brief's explicit interest in it, not because it's the stronger of the two.

**d. One live account development since Phase D**: `scaffolding london` shows in the more recent search-terms report as `Match type: Exact match (close variant)`, `Added: Added` — someone (a person or Google's own keyword-promotion feature) has already promoted it from a broad-match discovery into its own exact-match keyword, with zero fresh activity recorded since. Worth knowing before treating §8's London recommendation as a green-field decision — it's already partly in motion.

## 3. Geographic structure (Phase 3)

Location report, 126 rows, £301.45 total spend, 1 conversion (window: 1 Aug – 1 Sep):

| Bucket | Locations | Cost | Clicks | Conv. |
|---|---|---|---|---|
| **CORE** (declared service towns + "Essex" generic) | 7 | £181.11 | 44 | 1 |
| **Unclassified / other UK locations** | 106 | £102.28 | 21 | 0 |
| **Out-of-area** (Kent postcodes, Colchester, Thurrock, etc.) | 9 | £18.06 | 3 | 0 |
| **Expansion (London/Brentwood/Loughton)** | 4 | £0.00 | 0 | 0 |

The "Essex, England" location appears **twice** as separate rows (£87.57 + £75.82) — Google Ads' Presence-vs-interest location reporting can split a single geographic target into more than one row depending on match reason; this isn't a data error, just worth knowing when reading raw exports directly.

**Real out-of-area leakage, corroborating §2's search-term finding independently:** CM11, DA1, DA2, ME3, ME9, ME19 (Kent postcodes), Grays, South Ockendon (Thurrock), Chatham, Maidstone — £18.06 in this window alone, on locations with zero recorded conversions. Two independent reports (search terms and locations) agreeing is stronger evidence than either alone, same conclusion as Phase D reached, now re-confirmed against the same data rather than assumed still true.

**A geography note worth surfacing plainly**: `Essex` and each core town cost more than the entire out-of-area bucket, and still convert at roughly the account's overall (very low) rate — the leakage is real but it is not the dominant cost driver. Fixing it is worth doing (§9, §11) because it's cheap and unambiguous, not because it's where most of the money is going.

### CORE / EXPANSION / EXCLUDE

- **CORE GEO** (target, no change): the 12 declared core towns already in `AREA_DATA` — Rayleigh, Benfleet, Canvey Island, Southend, Basildon, Chelmsford, Wickford, Hadleigh, Leigh-on-Sea, Thundersley, Hockley, Rochford — plus "Essex" as a generic county target.
- **EXPANSION GEO** (target, controlled): London, Brentwood, Loughton — the site's already-built `EXPANSION_AREA_DATA` tier (Phase B). No new geography invented for this phase.
- **EXCLUDE GEO**: the specific out-of-area locations observed spending — Colchester, Maldon, Braintree, the Kent postcodes above, Thurrock/Grays/South Ockendon, Maidstone, Chatham. Not a blanket "exclude everywhere outside Essex" — only the places the data actually shows spend landing.

### Presence vs. "Presence or interest" — flagged, not silently assumed

This session cannot read the account's actual location-targeting setting — it isn't in any export. But the existing negative-keyword list already contains exact-match entries for `birmingham`, `bristol`, `cardiff`, `cornwall`, `coventry`, `cambridge`, `bournemouth` (§9) — someone already had to manually block these city names, which is itself indirect evidence that the account has been showing (or nearly showing) ads to people merely *interested in* those places rather than *present in* Essex/London — the exact failure mode Google's own Presence-targeting documentation describes "Presence or interest" as permitting. **Recommendation**: confirm the current setting, and if it is "Presence or interest," switch Core and Expansion geo to **Presence** only — a company that physically attends a job site should be targeting people who are actually there or regularly there, not merely people mentioning the area. This is a setting change, not a keyword change, and needs the account owner to action it directly.

## 4–5. (see §6–8 — architecture, landing pages, and ads are combined below since the data supports one coherent structure, not independent decisions per phase)

## 6. Proposed campaign / ad-group architecture (Phase 4)

The brief is explicit: the smallest sensible structure, not dozens of tiny ad groups. At ~£300/month total spend and 2 recorded conversions across two overlapping months, the data does not support a large structure — it supports three ad groups, and a clear "not yet" on a fourth.

**Recommendation: keep one active campaign** (`Phone calls Campaign - Axis High Intent` — it holds all the real performance and conversion history) **restructured into 3 ad groups.** Leave the paused `Axis Scaffolding | High Intent` campaign paused rather than reactivating it as a second live campaign: reactivating it now would split an already-thin budget and conversion signal across two campaigns competing on largely the same terms, with no data justifying the split. If its more distinctive terms (tower/mobile-scaffold-hire — genuinely different intent, see §9) are wanted at all, they belong as negatives, not as a second campaign.

| Ad group | Core terms (from real data) | Match type | Final URL |
|---|---|---|---|
| **A — Core Local, Generic** | `scaffolding near me`, `scaffolders near me`, `scaffolding company near me`, `scaffolding`, `scaffolders`, `scaffolding company`, `scaffolding hire` *(tightened — see §9)*, `local scaffolding companies` | Phrase/Exact (see §9 on why not Broad) | `/` (homepage) — the correct router for a query with no named town or service, and per E1/E2 already confirmed to legitimately carry strong local-authority signal |
| **B — Core Local, Named Town** | Exact-match keyword per declared town: `[scaffolding rayleigh]`, `[scaffolding chelmsford]`, `[scaffolding southend]`, `[scaffolding basildon]`, `[scaffolding benfleet]`, etc. — 12 keywords, one per `AREA_DATA` town | Exact match | **Keyword-level** Final URL override per town: `/areas/{town-slug}` — an ad-group-level default can't do this, each keyword needs its own destination |
| **C — Trade & Commercial** | `commercial scaffolding`, `scaffolding for builders`/`contractors`, `scaffolding company essex` (trade-flavoured) | Phrase/Exact | `/contractors` |
| *(not created)* — Specialist (emergency, loading bay, temporary roofing, dismantling) | — | — | **Not justified yet** — zero real spend/clicks on any of these terms in either campaign's live data (the only emergency-scaffolding keyword with any history is Paused, on the paused campaign, £0). Revisit if genuine volume appears; don't pre-build structure for demand that hasn't shown up. |

**London** is deliberately its own decision in §8, not folded into Ad group A or C.

## 7. Landing-page alignment (Phase 5)

| Ad group / intent | Final URL | Why |
|---|---|---|
| A — Core Local, Generic | `/` | No town or service named in the query; homepage is the only page built to route a fully generic local-intent visitor |
| B — Core Local, Named Town | `/areas/{town}` per keyword | Exact match, already-built page, already the organic-intent destination in the Phase D combined map |
| C — Trade & Commercial | `/contractors` | Existing page built specifically for the trade/contractor audience; `/services/commercial-scaffolding` is the fallback if a future ad group wants service-specificity over audience-specificity |
| London (§8) | `/areas/london` | Already unified into the current site architecture in Phase B; no new page needed |
| Cost/price-intent queries *(currently blocked — see §9)* | `/guides/scaffolding-cost-essex` | **Landing page already exists and is correctly built for this intent** — the gap isn't a missing page, it's an existing negative keyword blocking the traffic before it can reach it |

No `LANDING PAGE GAP` was found for any ad group this data supports building. Every proposed destination already exists in the current V2 site architecture — nothing new was created for this phase, per the explicit instruction.

## 8. London (Phase 8)

Evidence: one attributed conversion on `scaffolding london` (broad match, £72.97, 15 clicks — see §2c for the full, corrected picture including the second, non-London conversion), £0 recorded spend on the *location* "London" itself in the more recent window (§3 — the conversion is query-attributed, not visitor-location-attributed; these are different signals and shouldn't be conflated), and `/areas/london` already exists as a real, Phase-B-built destination.

**Recommendation: controlled testing within the existing architecture, not a dedicated campaign.** One conversion is a real, worth-protecting signal — not proof of a scalable market. Concretely:
- A small, separate ad group (not folded into Ad group A) with London-specific terms already showing in the data: `scaffolding london`, `scaffolding london` close variants, `scaffolding hire london`, `scaffolding in london`.
- Exact/phrase match only — London is exactly the kind of geography where broad match risks pulling in the "biggest scaffolding companies in london" and "boss scaffolding london" (competitor-name) terms already visible in the same data (§2).
- Final URL: `/areas/london`.
- No budget increase beyond what the existing account already spends — the brief's own caution applies directly: one conversion does not justify aggressive expansion, and the London page itself carries no fabricated case-study content (confirmed unchanged from Phase B).

## 9. Negative-keyword strategy (Phase 7)

**a. The account already has a real, fairly disciplined negative list** — 355 unique negatives across 430 rows, not a blank slate. Genuine existing coverage: 37 employment/training terms (`jobs`, `careers`, `apprenticeship`, `cscs`, `training`…), 33 equipment/purchase terms (`scaffolding for sale`, `scaffolding equipment`, `buy scaffolding`, `used scaffolding`…), and city-level exclusions for places clearly outside the service area (`birmingham`, `bristol`, `cardiff`, `cornwall`, `coventry`, `cambridge`, `bournemouth`). This existing work is sound and shouldn't be touched.

**b. One existing negative directly conflicts with the site's own content — the most concrete, highest-confidence finding in this phase.** `cost` is a **campaign-level, Broad match** negative on the active campaign. A broad-match negative blocks any query containing that word, in any position — meaning the account is currently structurally unable to show ads for `scaffolding cost essex`, `how much does scaffolding cost`, or any other cost-intent phrasing, ever, regardless of keyword bids. The site has a real, dedicated page built for exactly this intent — `/guides/scaffolding-cost-essex` — already identified in the Phase D combined map as the correct destination for cost/price research intent. This is why no cost-intent term appears anywhere in 251 rows of search-terms data: it can't, it's blocked before Google ever logs it as a matched term. **Recommend removing the broad-match `cost` negative** (or narrowing it to an exact-match negative on genuinely irrelevant phrasings like `cost of scaffolding license exam`, if any such need is later identified) so this ad group can actually reach the audience its own landing page was built for.

**c. A second, lower-confidence flag on the same pattern**: `construction` and `construction companies` are also campaign-level Broad negatives. Axis's own declared customer base explicitly includes trade/contractor/commercial customers (the whole `/contractors` page, the "Commercial & Trade" service group, the homepage's own three customer routes as of the Phase E reorder). A broad match on `construction` could plausibly block genuine queries like "scaffolding for construction companies." This is less clear-cut than `cost` — "construction companies" as a search phrase could equally mean someone looking *for* a construction company, not scaffolding *for* one — so this is flagged for the owner's judgement rather than a confident recommend-removal, unlike `cost`.

**d. One exact-match negative worth a specific, careful flag**: `[leigh scaffolding]`. "Leigh" is very close to Leigh-on-Sea, a real declared core town (`AREA_DATA`). This is an *exact* match, so it only blocks that literal phrase — not "leigh-on-sea scaffolding" — which limits the blast radius, but it could still be either (a) correctly excluding a real competitor plausibly named "Leigh Scaffolding" (consistent with the many similarly-patterned real company names already in the list, e.g. `[m r scaffolding]`, `[new era scaffolding]`), or (b) accidentally blocking a genuine, if unusually-phrased, Leigh-on-Sea search. Cannot be resolved from this data alone — flagged for the owner to check rather than guessed at either way.

**e. Protected — do not negative-match**, per the brief's explicit list and confirmed as the account's actual best-performing terms in §2: `scaffolding near me`, `scaffolders near me`, `scaffolding company`, `scaffolding hire` (tighten match type, don't exclude — see f), `domestic scaffolding`, `commercial scaffolding`, `roofing scaffolding`, `temporary roofing`, and every declared core-town query. None of these currently appear as negatives anywhere in the account (checked directly) — nothing to undo here, just confirmed clean.

**f. `scaffolding hire` is not a negative-keyword problem — it's a match-type problem.** It's the single largest cost driver (£119.05, 29 clicks, 0 conversions in the keyword report window) as a **Broad match** keyword. Broad match on "hire" is what's pulling in tower-hire/plant-hire/equipment-rental searchers — exactly the intent already well-covered by the account's own equipment negatives elsewhere. Recommend **tightening to Phrase match** (`"scaffolding hire"`) rather than adding it to negatives, which would throw away real core-intent traffic along with the DIY/plant-hire noise.

**g. Proposed new additions**, each with a documented reason, none touching the protected list above:
| Negative | Match type | Reason |
|---|---|---|
| `scaffold tower hire` | Phrase | Equipment/plant-hire — already excluded in spirit (§9a) but this specific phrasing isn't yet in the list and shows real search volume in the paused campaign's own keyword set |
| `mobile scaffold hire` | Phrase | Same as above |
| `portable scaffold hire` | Phrase | Same as above |
| `colchester`, `maldon`, `braintree` | Phrase, per §3's out-of-area list | Corroborated by both the search-terms and location reports independently |
| Kent postcode prefixes actually observed (`DA1`, `DA2`, `ME3`, `ME9`, `ME19`) | — | These are better handled as **location exclusions** (§3), not keyword negatives — postcode-shaped negative keywords are fragile and don't generalise; flagged here only so the recommendation isn't lost between sections |

## 10. Ads (Phase 6) — proposed copy for the new structure, not an audit of existing ads

No existing ad copy was supplied in any export, so there is nothing to audit — this is draft copy for the 3 recommended ad groups, using only claims already `VERIFIED`/`Established` in `CLAIM_VERIFICATION.md`. **Not implemented; for review before use.**

**Ad group A — Core Local, Generic** (destination: `/`)
- Headlines: "Axis Scaffolding Ltd", "CISRS-Qualified Scaffolders", "Scaffolding Across South Essex", "Fully Insured & Founder-Led", "10+ Years' Experience", "Free, No-Obligation Quotes"
- Description: "Founder-led scaffolding team based in Rayleigh. CISRS-qualified, fully insured. We aim to respond to enquiries the same working day."

**Ad group B — Core Local, Named Town** (destination: `/areas/{town}`, one RSA per town recommended over one generic RSA with `{LOCATION}` insertion, given the small keyword count makes this manageable)
- Headlines: "Scaffolding in {Town}", "Local {Town} Scaffolders", "CISRS-Qualified Team", "Fully Insured Scaffolding"
- Description: "Axis Scaffolding Ltd — CISRS-qualified, fully insured scaffolders serving {Town} and South Essex. Free quotes."

**Ad group C — Trade & Commercial** (destination: `/contractors`)
- Headlines: "Scaffolding for Builders", "Trade & Contractor Scaffolding", "RAMS Available on Request", "CISRS-Qualified Operatives", "Programme-Led Erection & Strike"
- Description: "A scaffolder that turns up when agreed. RAMS available on request. CISRS-qualified team serving South Essex contractors."

None of these use the £5m insurance figure (still `OWNER VERIFICATION REQUIRED`), invented ratings, invented response-time guarantees, or invented statistics — every claim traces to an `Established` row in `CLAIM_VERIFICATION.md`. Per current RSA guidance, each group has several genuinely distinct headline/description assets rather than near-duplicates, and nothing is recommended for pinning — there's no strategic reason here to force a specific headline into a fixed position, and pinning would reduce Google's ability to test combinations on an account with this little data to begin with.

## 11. Budget / bidding assessment (Phase 9)

**Cannot see the account's actual current bidding strategy or budget** — not in any export. What the data does support:

- Real spend across the reports examined: ~£300–£320/month, depending on window.
- Real conversions: 2, across two overlapping ~4-week windows (§2c). That is not enough volume for automated bidding strategies that optimise toward a target CPA or conversion volume to have a meaningful signal to learn from — Google's own guidance on Smart Bidding is explicit that conversion volume matters for how well these strategies can optimise.
- **Recommendation, conditional on the actual current strategy (unverifiable from here)**: if the account is currently on a conversion-volume-dependent automated strategy (Target CPA, Maximize Conversions), document the risk that 2 conversions/month is too thin a signal for it to optimise reliably, and consider a manual or Maximize Clicks approach until the restructured account (§6–9) has accumulated more conversion history to bid against. If it's already on manual bidding, no change is implied by this data.
- **No budget increase is recommended.** The brief is explicit on this and the data doesn't contradict it — fix the structural issues first (blank Final URLs, the `cost` negative, out-of-area leakage, the broad-match `scaffolding hire`) and let a cleaner account earn a larger budget on its own evidence, not the other way round.

## 12. Conversion tracking audit (Phase 10)

- The reports show a `Conversions` column and `Cost / conv.` — this is **whatever the account currently counts as a conversion action**, and this session has no visibility into what that action actually is (a phone-call action with what duration threshold, a form-submission action, an imported GA4 event, or some combination as primary vs. secondary).
- The website's own event infrastructure (`phone_click`, `quote_start`, `generate_lead`, `quote_error` — confirmed present in `main.js` from earlier phases) is ready to feed Ads conversions, but **GA4 itself remains unconfigured** (`GA4_MEASUREMENT_ID = None` in `build_site.py`, confirmed unchanged) — so if Ads conversions are currently sourced from an imported GA4 event, they cannot actually be flowing correctly, since there's no live GA4 property to import from. If they're sourced from Ads' own native call-tracking instead, that's a separate, valid path and this note doesn't apply.
- **This is a real gap that needs the account owner's direct look at Google Ads → Goals → Conversions**, not something resolvable from CSV exports. No conversion action was assumed correct or incorrect here — flagged, not guessed at.

## 13. Implementation rule (Phase 11) — specification, not execution

Every change recommended above is summarised here as BEFORE → PROPOSED → WHY, for whoever executes it in the Ads UI:

| Change | Before | Proposed | Evidence |
|---|---|---|---|
| Campaign structure | 1 active + 1 paused (duplicate-ish) campaign | Keep 1 active campaign, leave the second paused (don't reactivate without new evidence) | §1, §6 |
| Ad groups | 1 (active campaign) | 3: Core Local Generic / Core Local Named-Town / Trade & Commercial | §6 |
| `scaffolding hire` match type | Broad | Phrase | §9f — largest zero-conversion cost driver under Broad |
| Final URLs | Blank on all 93 keywords | Set per ad group / per town keyword (§7) | §1, §7 |
| `cost` negative | Campaign-level Broad | **Remove** | §9b — blocks the site's own cost-intent landing page |
| `construction` / `construction companies` negatives | Campaign-level Broad | Owner review, not auto-removed | §9c |
| `[leigh scaffolding]` negative | Exact, campaign-level | Owner review, not auto-removed | §9d |
| Out-of-area locations (Colchester, Kent postcodes, Thurrock towns, Maidstone) | Targeted, no exclusion found | Add as location exclusions | §3, §9g |
| Location targeting mode | Unknown — not visible in any export | If "Presence or interest," switch to "Presence" | §3 |
| London | No dedicated grouping | Small, exact/phrase-only ad group → `/areas/london`, no budget increase | §8 |
| Ad copy | Unknown — no export supplied | 3 draft RSA sets provided, unimplemented | §10 |
| Bidding strategy / budget | Unknown | No change recommended; document thin-data risk if on automated bidding | §11 |

**Nothing here was executed.** No live Google Ads write access exists in this session.

## 14. Measurement plan (Phase 12)

Once the above is actually applied in the Ads UI, track by ad group and landing page (not just account-wide): impressions, clicks, CTR, CPC, cost, conversions, CPA, and geography — cut consistently by the new ad-group structure (A/B/C/London) so the account owner can see whether Ad group B's per-town Final URLs actually convert better than the old single blank-URL setup, whether removing the `cost` negative surfaces real cost-intent volume, and whether the London test's single conversion repeats or was a one-off. **Primary business outcome is qualified scaffolding enquiries, not CTR** — a high-CTR, zero-conversion ad group (exactly what `scaffolding hire` under Broad match already demonstrated) is not success.

## 15. Rollback notes (Phase 13)

No live changes were made, so there's nothing to roll back from this PR itself. For whoever does execute this in the Ads UI: Google Ads retains full change history natively (Tools → Change history) for every account-side edit, which is the real rollback mechanism — this document doesn't need to duplicate it. The one explicit caution: removing the `cost` negative (§9b) is the highest-leverage, lowest-risk change on this list (a landing page already exists for the traffic it would unblock) and is a reasonable first move to make in isolation, watching results, before touching match types or geography.

## 16. Remaining owner decisions

1. Confirm the actual current location-targeting mode (Presence vs. "Presence or interest") — not visible in any export.
2. Confirm current bidding strategy and budget — needed to judge §11 properly.
3. Confirm what Ads currently counts as a conversion action, and whether it's genuinely wired up (§12).
4. Review `construction`/`construction companies` and `[leigh scaffolding]` negatives directly (§9c, §9d) — flagged, not auto-changed.
5. Decide whether the paused `Axis Scaffolding | High Intent` campaign should be deleted outright or left paused as-is (§1, §6) — no data forces either choice.
6. Execute the BEFORE/PROPOSED table (§13) in the Google Ads UI — this repository has no mechanism to do it directly.

## 17. Confirmation

No website code, copy, or architecture was changed in this phase. No Google Search Console settings were touched. No SEO work was done. The £5m insurance claim was not used anywhere in the proposed ad copy and remains `OWNER VERIFICATION REQUIRED`. No fake projects, testimonials, ratings, response-time guarantees, or statistics were introduced anywhere in this document. No budget increase is recommended.
