# Phase E1 — Rayleigh Attribution Investigation

**Status: diagnosis only. No site code, Google Ads, or Search Console changes.** Answers the specific question list raised on review of Phase D, working through everything answerable from static exports and source code before recommending what only the account owner's live GSC access can resolve.

## Summary of conclusion

Three real, independent things are true at once, and none of them alone fully proves cannibalisation — together they make it the leading explanation, but it is not yet certain:

1. `/areas/rayleigh`'s on-site technical setup is completely correct — this rules out a site-side bug as the cause.
2. The homepage's own title, copy, and schema strongly and legitimately signal "Rayleigh" — a real, checkable mechanism for why Google might prefer the homepage over the dedicated page.
3. The GSC export data itself has an internal inconsistency I cannot resolve without live access — so confidence should stay at "strong hypothesis," not "proven."

## 1. Is this a site-side technical problem? — No, ruled out

Checked directly against the live repository, not assumed:

| Check | Result |
|---|---|
| Canonical tag | `<link rel="canonical" href="https://www.axisscaffoldingessex.co.uk/areas/rayleigh">` — correct www host, correct no-trailing-slash form, matches the site's own canonical strategy exactly |
| `noindex` present? | No |
| In `sitemap.xml`? | Yes — `<url><loc>.../areas/rayleigh</loc>...</url>` present |
| Internal links pointing to it | 42 files link to `/areas/rayleigh` (footer's "Areas We Cover" appears on every page) |
| Title | `Scaffolding in Rayleigh | Axis Scaffolding Essex` — unique, town-specific |
| Meta description | Unique, town-specific, mentions Rayleigh, CISRS, phone number |
| Content | 47 mentions of "Rayleigh" in genuinely town-specific prose (housing stock, typical projects, site access — not templated filler) |

**Conclusion: there is no canonical error, no noindex, no sitemap omission, no orphan-page problem, no thin/duplicate content.** If Google isn't selecting this page, it isn't because the page is technically broken or hard to find.

## 2. Does the homepage genuinely compete with it on the same topic? — Yes, confirmed

This is the strongest concrete finding in this investigation. Checked directly against source:

- Homepage `<title>`: **`Scaffolding Essex | Axis Scaffolding Ltd Rayleigh Team`** — the word "Rayleigh" is in the homepage's own title tag.
- "Rayleigh" appears **23 times** on the homepage itself (vs. 47 on the dedicated page — fewer, but still substantial, and concentrated in exactly the kind of prominent positions — title, hero trust row, footer — that carry the most weight).
- The homepage's `LocalBusiness` schema declares `"addressLocality": "Rayleigh"` — Google's structured-data understanding of *this business's registered location* is anchored to the homepage, not the area page.

**This gives a completely mundane, non-bug explanation for the anomaly**: for a query like "scaffolding company rayleigh", Google has two genuinely relevant candidates from the same site — a page that says "this is our page about the town of Rayleigh" and a page that says "this is the company, and it is registered/based in Rayleigh." Google may be treating the homepage as the more authoritative match for "local business in Rayleigh" intent, even though the area page is more topically specific. This is self-competition by design (the homepage legitimately needs to say where the business is based), not a technical defect — which changes what kind of fix would even make sense, if one turns out to be needed.

## 3. Data-quality check on the GSC export itself — a real, unresolved inconsistency found

Prompted directly by the review's question about date-range/property/dimension discrepancies. Checked three ways:

- **`Filters.csv` from both pulls**: `Search type: Web`, `Date: Last 3 months` — no unusual filter applied. **Correction to the Phase D document**: I had described the window as "Aug 26 – Sep 1, 2026" (inferring it from the export folder's pull date); it is actually a rolling 3-month window as of that pull date. This also means the "two pulls a week apart show the same pattern" claim from the earlier session is weaker evidence than stated — two 3-month rolling windows 6 days apart overlap by roughly 97% of their date range, so they are not independent confirmations, just two snapshots of almost the same underlying data.
- **Internal consistency of the marginal totals**: `Countries.csv` and `Devices.csv` both sum to exactly **33,335** impressions (as they should — two different breakdowns of the same grand total must agree, and they do). `Queries.csv` sums to 30,800 — about 7.6% lower, which is normal and expected (GSC deliberately omits very-low-volume/anonymised queries from the Top Queries export for privacy). **`Pages.csv` sums to 47,542 — 42.6% *higher* than the confirmed true total.** Verified independently with both Python and `awk` to rule out a parsing bug on my end; the number is real. I cannot explain this from a static CSV export — it does not match any GSC behaviour I can verify without live access to the account.
- **Practical effect on the Rayleigh finding**: this inconsistency doesn't invalidate the finding that `/areas/rayleigh` is absent from Pages.csv (its absence is a fact regardless of what the file's total should be), but it does mean I cannot fully rule out that Pages.csv itself is an incomplete or malformed export in some way I can't detect from outside the account. This is exactly the kind of check that needed a second pair of eyes with live access — flagged, not resolved.

## 4. External, corroborating checks (weak evidence — caveated clearly)

Using web search from this environment (US-based backend, not a logged-in UK Google session — treat as weak, directional corroboration only, not a substitute for the account owner's own SERP check):

- A `site:axisscaffoldingessex.co.uk rayleigh` search did **not** return `/areas/rayleigh/` among its top results — it returned the homepage, `/areas/london/`, `/areas/loughton/`, and two service pages instead. Consistent with (not proof of) the homepage/other pages being preferred over the area page for Rayleigh-flavoured queries.
- A search for "scaffolding company rayleigh axis scaffolding" surfaced a **genuine, unexpected finding**: the business's own old domain, `axisscaffolding.co.uk` (already known and documented in `SEO_TECHNICAL_AUDIT.md` §9 as external, unmanaged infrastructure), still has old, now-**dead** deep pages indexed somewhere — `www.axisscaffolding.co.uk/scaffolding-areas` and `.../residential-scaffolding` both returned live search results but are now **404 Not Found** when fetched directly. The domain root (`https://www.axisscaffolding.co.uk/`) does correctly 301-redirect to `https://axisscaffoldingessex.co.uk/`, confirmed directly — so the migration is *partially* working (root redirects), but old deep pages are neither live nor redirecting, just gone, while still apparently findable via search. This is a separate, real technical issue from the Rayleigh GSC anomaly — not necessarily its cause — but worth recording since it's new evidence about the old-domain migration §9 already flagged as unresolved external infrastructure.

## 5. Direct answers to the review's question list

| Question | Answer |
|---|---|
| Why are Rayleigh queries ranking strongly while `/areas/rayleigh` shows zero impressions? | Leading hypothesis: the homepage's own title/schema is a genuine topical competitor for "Rayleigh" queries (§2). Not proven — see below for what would prove it. |
| Which actual URL is receiving those impressions? | Cannot be determined from a static Pages/Queries export (they're separate marginal tables, not joined). Circumstantial evidence points to the homepage (§2, §4) but this needs the account owner's GSC UI, which lets you click a query and see its "Pages" tab filtered to just that query — that is the joined data I don't have. |
| Homepage, another area page, a service page, or unexpected URL? | Most likely the homepage, based on §2's evidence. Not the old domain (§4 confirms the old domain's root correctly redirects, so it shouldn't be absorbing new-domain GSC-recorded impressions — though see the caveat on old dead pages there). |
| Canonical/internal-link/sitemap/page-topic relationships? | Canonical, internal links, and sitemap are all correct (§1). Page-topic relationship is the real finding — the homepage and the area page legitimately overlap on "Rayleigh" (§2). |
| Is `/areas/rayleigh` indexed and eligible but not selected? | Consistent with the evidence (correct technical setup + absent from a live `site:` search's visible results), but "indexed but not selected for this specific query" is exactly what GSC's own URL Inspection tool is built to confirm definitively — the account owner should run it directly on `/areas/rayleigh` and on 2–3 of the top Rayleigh queries. |
| Dimension/date-range/property discrepancy? | Date range corrected (§3, rolling 3 months not 1 week). Filters are clean. A real, unexplained 43% total-impression discrepancy exists specifically in Pages.csv (§3) — needs the account owner to check directly in the live GSC property (and confirm which property — domain vs. URL-prefix, www vs. bare-host — generated this export, which isn't recorded in the CSV itself). |
| Is the visibility being attributed to another URL? | Best available answer: probably, and most likely the homepage — but "probably" is the honest ceiling of what a static export can prove. |

## 6. What would settle this definitively (for the account owner, not this repo)

1. In the live GSC UI: click through the query "scaffolding company rayleigh" (or similar) → its own "Pages" tab. This shows exactly which URL(s) earned those impressions — the one piece of data no static export provides.
2. Run URL Inspection on `https://www.axisscaffoldingessex.co.uk/areas/rayleigh` directly — confirms indexed/eligible status definitively.
3. A logged-out, UK-located, incognito search for 2–3 of the top Rayleigh phrases, to see today's actual SERP (today's result won't exactly match the 3-month historical window, but it's a real, current data point this repo's tools can't produce reliably).
4. Re-confirm which GSC property (domain property covering all hostname/protocol variants, vs. a URL-prefix property scoped to one exact hostname) was used to generate the exports already supplied — this determines whether `www` and non-`www` traffic are even being counted together.

## 7. What this investigation deliberately did not do

No changes were made to `/areas/rayleigh`, the homepage, internal linking, schema, or any other page. Per the explicit instruction, that decision waits until the questions in §6 are answered by the account owner. The £5m insurance claim and the 4 services without tagged project photos remain untouched.
