# Axis Scaffolding: traffic, clicks and impressions plan

Written 29 October 2026. Evidence: Search Console performance (12 months to mid-October 2026), the earlier search-intelligence work in `AXIS_SEARCH_INTELLIGENCE_MAP.md`, and a review of how ranking scaffolders and local-SEO research handle the same problems. Nothing here promises a ranking; it lists what is worth doing, what is already done in this change, and what only the owner can do.

## 1. What the data says

| Measure (12 months) | Value | Read |
|---|---|---|
| Total clicks | 139 | Very low for the demand |
| Total impressions | 61.3k | The site is shown a lot |
| Average CTR | 0.2% | Almost nobody who sees the site clicks it |
| Average position | 28.5 | Page 3: most impressions are on results nobody scrolls to |

Two separate problems, from the query map (Aug-Sep pull, 571 queries):

1. **Visibility.** Generic and town queries sit at positions 20 to 70 ("scaffolding essex" 30, "scaffolding chelmsford" 47, "scaffold hire essex" 70, "scaffolding company essex" 37). Fixing this needs more useful content, internal links and outside signals.
2. **Click-through.** Some queries rank 1 to 8 with no clicks ("scaffolding rayleigh" 4.2, "scaffolders rayleigh" 3.1, "scaffolding hire rayleigh" 4.1, "emergency scaffolding essex" 6.8). Some of that is likely rank-tracking traffic, but weak titles and snippets are a real, cheap thing to fix.

## 2. Done in this change

| Action | Why |
|---|---|
| Area page titles and descriptions rewritten ("Scaffolding in X – Local Scaffolders | Axis"; description carries CISRS, insured, 5.0 from 31 Google reviews, phone number) | Click-through on queries already ranking |
| Homepage title now "Scaffolding Company in Rayleigh & Essex" | Matches "scaffolding company rayleigh / essex" queries |
| Six new guides: scaffolding hire, choosing a company, how long scaffolding stays up, commercial and industrial scaffolding, emergency/storm damage, safe scaffold checklist | Targets queries with impressions and no good page ("scaffold hire essex" 253 at position 70, "scaffolding hire rayleigh/benfleet" 266/198, "industrial scaffolding" 291/185, "emergency scaffolding essex" 189) |
| Every guide has a visible FAQ with matching FAQ markup, a "why call Axis" block and cited sources | Answer-engine and AI-search eligibility; Google says AI features use the same helpful-content and structured-data signals as normal search |
| Homepage now links three guides; each guide links the next three, plus service and area pages | Internal links pass relevance and help crawling |
| Guides added to sitemap and `llms.txt` | Discovery |

Only facts already on the site or verified against HSE, Essex Highways, Southend council and CISRS pages are used. Commercial pages carry no prices.

## 3. Only the owner can do these (highest impact first)

1. **Google Business Profile.** In independent local-SEO surveys the primary category, then proximity, then keywords in the profile name, are the top map-pack factors, and review signals have grown in importance. Check: primary category is the scaffolding one; every service is listed with a description; the website link is the www address; hours match the website (currently a known conflict); upload 2 to 3 real project photos a week; post weekly; answer every review.
2. **Reviews.** Ask every customer for a Google review the day the scaffold comes down, with the profile link texted to them. Reply to all of them. This feeds map results and click-through.
3. **Citations and directories.** Same name, address, phone and hours everywhere: Checkatrade, TrustATrader, MyBuilder, Bark, Yell, FreeIndex, Thomson Local, Bing Places, Apple Business Connect, Nextdoor. Directory profiles are also real backlinks.
4. **Accreditations.** Competitors cite CHAS, Safecontractor and NASC or Scaffolding Association membership. These earn trust and a profile link. Apply only if Axis qualifies, and tell us before we mention any on the site.
5. **Backlinks from real relationships.** Ask the roofers, builders and solar installers Axis already works with for a "trusted trades" link; offer local clubs a sponsor link; send finished jobs with photos (with the customer's permission) to the Southend and Rayleigh local news sites; join the local chamber of commerce.
6. **Search Console.** Submit the sitemap again after this deploys; use URL inspection and "request indexing" on the six new guides and the Residential & Domestic page; export queries and pages monthly (the last export we have is from early September).
7. **Google Ads.** Remove "domestic" as a negative keyword; tighten "scaffolding hire" from broad to phrase; fix the lead conversion. Paid clicks also teach us which wording converts.

## 4. Worth doing next (needs your input)

- **Project case-study pages.** One page per real job (town, what was built, how long, photo, customer quote). Needs the job details from you; these are what top local firms use to rank for "scaffolding in [town]".
- **A short video** of an erection or a site walk-through, for the profile and the site.
- **Town-by-service pages** (for example "chimney scaffolding in Benfleet") only where each page can carry genuinely different local detail. Thin copies would hurt.
- **Two new guides a month** from the questions customers ask on calls.

## 5. How to measure

Track monthly in Search Console: impressions, clicks, CTR and average position for the queries named above, plus calls and WhatsApp messages. Titles and descriptions typically need a few weeks to be re-crawled; new pages need longer. Judge success on clicks and enquiries, not impressions.

## 6. Indexing finding (Search Console coverage export, 29 October 2026)

Of about 129 URLs Google knows, 41 are indexed and 88 are not. The biggest buckets: 49 "Page with redirect", 13 "Alternative page with proper canonical tag", 20 "Discovered, currently not indexed", 4 "noindex" (intended: legal pages, thank-you, landing pages), 3 "Crawled, currently not indexed", 1 "404".

Cause of the first two: GitHub Pages serves every page at the trailing-slash URL and 301-redirects the bare URL to it, but the site's canonical tags, sitemap and internal links all used the bare URL. Google was told to index a URL that itself redirects, and the page it landed on said the redirecting URL was canonical. Fixed by making canonicals, sitemap, `llms.txt`, redirect stubs and internal links use the trailing-slash form, so every URL points at itself.

After deploy: resubmit the sitemap, then in Search Console open Pages and click "Validate fix" on the redirect and canonical rows. Expect weeks, not days, for the counts to settle. The 20 "discovered, not indexed" pages are mostly new and low-authority-site crawl delay; links, reviews and the actions in section 3 are what move those.
