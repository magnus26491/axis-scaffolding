# Google Ads and Search Console: what the data says and what to do

Data used: Google Ads search keyword, search terms and negative keyword reports (1 May to 31 October 2026); Search Console queries (3 to 30 October 2026) and coverage (29 October 2026). Figures below are from those exports. Anything I could not see is marked as a question for the owner.

## 1. Headline numbers

| | Ads, last 6 months | Change on the 6 months before |
|---|---|---|
| Spend | £1,430.56 | down £635.70 |
| Clicks | 313 (CTR 3.35%, average CPC £4.57) | down 176 |
| Impressions | 9,353 | down 6,864 |
| Phone calls | 71 (about £20 per call) | down 12 |
| Conversions | 21 (£68.12 each, 6.71% conversion rate) | down 6 |

Organic search over the last 28 days produced 5 clicks, 3 of them for the brand name. So almost all current enquiries come from Ads, and Ads volume has fallen by about a third.

## 2. Google Ads: what is working and what is not

| Keyword | Spend | Share of spend | Conversions | Cost per conversion |
|---|---|---|---|---|
| scaffolding hire (broad) | £770.06 | 54% | 11 | £70 |
| scaffolding london (broad) | £318.37 | 22% | 4 | £80 |
| [scaffold firms near me] | £100.99 | 7% | 1 | £101 |
| [scaffolding colchester] | £59.23 | 4% | 1 | £59 |
| "scaffolding near me" | £43.47 | 3% | 3 | £14.50 |
| [southend scaffolding] | £21.71 | 1.5% | 1 | £21.70 |
| Everything else | about £117 | 8% | 0 | none |

Findings:

1. **Two broad-match keywords carry the account.** "scaffolding hire" and "scaffolding london" are 76% of spend and 71% of conversions. That is fragile, and "scaffolding hire" is flagged "low quality" by Google.
2. **A third of the budget is invisible.** 132 of 313 clicks (£494) came from "other search terms" Google does not show, so they cannot be checked.
3. **Some conversions look unqualified.** Of the 13 conversions attributed to named search terms, 5 were for towns outside the core area (Colchester, Witham, Maldon) or for competitor names (Curtis, Morgans). Counting a call as a conversion does not mean it was a job.
4. **71 calls but 21 conversions.** Either the call-length threshold is high, or only some calls are tracked. Calls tapped from the website, WhatsApp messages and quote forms are not counted at all.
5. **One campaign, one ad group, one landing page set.** All keywords share one ad group, so ads and pages cannot match what people searched. That is a main reason for "low quality" flags.
6. **Conflicts.** The keyword "scaffolding kent" is enabled while "scaffolding kent" and "kent scaffolding" are negative keywords, and it still spent £18.62. The "domestic" negative flagged earlier is now gone (good). Negatives for "dismantling", "remove", "take down", "construction" and "chimney scaffold hire" block work Axis actually does.
7. **Good news.** "scaffolding near me" phrase match converts at 37.5% (3 of 8 clicks, £14.50 each) and [southend scaffolding] at £21.70. The samples are small but worth scaling.

### Actions, in order

1. **Know what a conversion is worth** (owner): average job value, the share of calls that become jobs, and which of the 21 conversions were real. Log every call for four weeks. Without this nobody can set a sensible budget.
2. **Fix measurement.** Import the website events that already exist (phone tap, WhatsApp tap, quote form) into Google Ads as conversions, set the call-length threshold deliberately, and remove the old broken call conversion.
3. **Split the single ad group**, each group with its own landing page:

| Ad group | Example keywords (phrase/exact) | Landing page |
|---|---|---|
| Near me | scaffolding near me, scaffolders near me | Home |
| Towns | scaffolding [town], scaffolders [town] for Rayleigh, Southend, Benfleet, Basildon, Chelmsford, Wickford, Hockley, Hadleigh, Leigh, Canvey, Rochford, Thundersley | /areas/[town]/ |
| Solar | solar panel scaffolding [town] | /services/solar-panel-scaffolding/ |
| Roof and chimney | roof scaffolding, chimney scaffolding, roof replacement scaffolding | the matching job page |
| Emergency | emergency scaffolding essex | /services/emergency-scaffolding/ |
| Commercial | commercial scaffolding [town] | /services/commercial-scaffolding/ |
| Hire (erected) | scaffolding hire [town] | /guides/scaffolding-hire-essex/ |
| London | scaffolding london | /areas/london/ (own campaign and budget) |

4. **Tame "scaffolding hire".** Move it to phrase match with town names, point it at the hire guide, and write ads that say the scaffold is erected, inspected and dismantled for the customer. That filters out people who want to rent poles to put up themselves, and lifts relevance.
5. **Keep London separate.** £80 per conversion is a bit above the account average. Run it as its own campaign with a capped budget and decide using job value.
6. **Scale the winners** ("scaffolding near me", [southend scaffolding]) with higher bids once the tracking in step 2 is in.
7. **Trim.** Pause "scaffolding kent". Pause [scaffolding colchester] and related Colchester terms unless Axis works there. Add the competitor names seen in the search terms as negatives. Set location targeting to "people in" the area, not "people interested in" it.
8. **Review the conflicting negatives** (dismantling, remove, construction, chimney scaffold hire) and remove those blocking services Axis offers.
9. **Use the new pages in the ads.** Sitelinks to the job pages (solar, chimney, roof replacement), callouts (CISRS-qualified, £10m insured, 5.0 from 31 Google reviews), a call asset, a location asset, and an ad schedule that matches when the phone is answered.
10. **Re-enable the paused town keywords** (Benfleet, Billericay and others) once each points at its own town page.

## 3. Website: what the Search Console queries show

Demand that already exists (impressions in 28 days; almost all at 0 clicks):

- **Towns:** Basildon 195, Southend 166, Rayleigh 168, Benfleet 90, Wickford 65.
- **Commercial and industrial:** "commercial scaffolding southend" 154, "...rayleigh" 128, "...essex" 123, "commercial scaffolding specialists" 126, "industrial scaffolding southend" 68.
- **Domestic and residential:** "domestic scaffolding essex" 123, "...southend" 92, "residential scaffolding southend" 74.
- **Hire, as customers phrase it:** "scaffolding hire rayleigh" 101, "scaffolding hire" 53, "scaffolding hire benfleet" 47, "scaffolding hire in essex" 45.
- **Job-specific:** "custom scaffolding essex" 135, "temporary roofing scaffolding rayleigh" 32, "solar panel scaffolding rayleigh" 32, "emergency scaffolding essex" 42, "chimney scaffolding essex" 28.
- **Questions:** "how to tell if you need scaffolding" 45, "scaffolding types essex" 59, "cheap scaffolding essex" 39, "scaffolding prices essex" 16, "scaffold inspection essex" 17.
- **Places we have no page for:** Westcliff-on-Sea (22), Shoebury (21), Laindon (21), Hawkwell (18), Maldon (48), Grays (53), Ongar, Epping, Burnham-on-Crouch, Billericay, Pitsea.

### Done in this change

| Change | Targets |
|---|---|
| Every town page now lists all ten jobs with the town in the link text ("Commercial and industrial scaffolding in Southend-on-Sea") | the town + job queries above, and internal links to every job page |
| New guide "Types of Scaffolding" | "scaffolding types essex" |
| Cost guide title now "Scaffolding Prices in Essex: 2026 Cost Guide" | "scaffolding prices / cheap scaffolding essex" |
| "Do I need scaffolding" retitled "How to Tell If You Need Scaffolding" | "how to tell if you need scaffolding" |

Earlier changes already cover hire, solar, chimney, emergency, inspection and the Residential & Domestic merge.

### Needs the owner

1. Which of these places does Axis actually serve: Westcliff-on-Sea, Shoebury, Laindon, Hawkwell, Pitsea, Billericay, Maldon, Grays, Colchester? Pages are added only for places confirmed, with no invented local detail.
2. "custom scaffolding essex" (135) and "scaffold design and planning" suggest demand for bespoke scaffold designs. The commercial page says "TG20 or bespoke design". Is that accurate and available for a page of its own?
3. Does Axis take emergency calls out of hours? ("24 hour scaffolding essex" has searches; the site makes no 24-hour claim.)
4. Fresh Search Console exports **including the Position column** (Performance, Export) so the page-one and page-three queries can be told apart.

## 4. Why this works as one plan

The same pages feed both channels. A page that matches the search (a town page for a town search, the solar page for a solar search) ranks better, converts better, and lifts Google's Ads quality score, which lowers cost per click. That is why the order is: tracking first, then structure, then spend.

## 5. Search Console export, 16 months to 1 November 2026

| Measure | Value |
|---|---|
| Clicks / impressions | 139 / 61.4k (UK: 128 clicks) |
| Brand query "axis scaffolding" | 32 clicks, 21% CTR, but average position 4.0 (it should be 1) |
| Impressions by position | 1-3: 6.3k · 4-10: 8.0k · 11-20: 3.7k · 21-50: 32.5k · 51+: 7.5k |
| Devices | desktop 83 clicks, mobile 54, tablet 2 (similar CTR) |
| Host Google shows | non-www 72.6k impressions, www 16.5k, **http://www 2.9k** |

Findings:

1. **HTTPS is not enforced.** `http://www.axisscaffoldingessex.co.uk/` answers 200 (checked 1 November 2026) and Google is showing it, at position 2.26 with 2,942 impressions. Enforcing HTTPS in GitHub Pages settings is a one-click fix.
2. **Google still shows the non-www address** for most impressions. The bare host redirects correctly to www, and the canonical fix on 29 October points everything at www, so this should consolidate over the coming weeks. Nothing more to do in code.
3. **Rayleigh ranks 1 to 3 for dozens of long, odd queries and gets almost no clicks** ("rental scaffolding material rayleigh" 1.1, "industrial scaffolding companies rayleigh" 1.07). Most of this looks like automated or tool-generated search traffic, not customers. Do not chase it. Only "scaffolding rayleigh" (3 clicks at position 3.6) is real demand.
4. **The real opportunity is pages 2 to 4.** 69% of impressions are at position 21 or lower: "scaffolding essex" 2,525 impressions at 31, "commercial scaffolding essex" 963 at 32, "domestic scaffolding essex" 911 at 26, "scaffolding southend" 899 at 35, "scaffolders benfleet" 574 at 24.
5. **Close to page one:** "temporary roofing benfleet" (10.1), "scaffolding for roofing contractors essex" (10.6), "commercial scaffolding rochford" (11.4), "temporary roofing essex" (12.2), "specialist scaffolding in wickford" (12.6), "scaffolding rochford" (13.1, 200 impressions), "scaffolding canvey island" (16.1, 312 impressions). Small boosts (links, reviews, a sharper page) can tip these onto page one.
6. **Best-ranking pages are the smaller towns** (Loughton 19-20, Rochford 24, Wickford 27, gallery 21). The big ones (Southend 43, Chelmsford 50, Brentwood 42-44) need authority, not rewording.

## 6. Owner answers (1 November 2026) and what they change

- **Coverage:** Axis works everywhere in Essex. Pages added for Westcliff-on-Sea, Shoebury, Laindon, Pitsea, Hawkwell, Billericay, Maldon, Colchester and Grays. Colchester and Maldon are therefore **in area**: keep those Ads keywords (and their conversions) rather than pausing them. Scaffold licences for these towns come from Essex Highways, Southend-on-Sea City Council (Westcliff, Shoebury) or Thurrock Council (Grays).
- **Value of a lead:** about £1,000 per job and, conservatively, 1 in 2 calls becomes a job, so a call is worth about £500 of revenue. Current cost is about £20 per call and £68 per counted conversion. Even if only the 21 counted conversions were real, that is roughly 10 jobs (about £10,500) from £1,430 of spend, around 7 pounds of revenue per pound spent. The limit on growth is volume, not cost: impressions fell 42% and clicks 36% on the previous period.
- **What that means for Ads:** raise the daily budget and bids rather than trimming. A sensible ceiling for a counted conversion is £150 to £200 until margin is known (the owner should confirm margin per job). Judge by cost per job won, using the call log.
- **Bespoke design:** available for specialised jobs only. The commercial page and commercial guide now say so; standard jobs are not described as bespoke.
- **Emergencies:** emergency calls are taken out of hours. Stated on the emergency page and the emergency guide. The site still makes no "24-hour" claim.
- **Case studies:** details to follow from Ashley (town, work done, photo, customer quote), then one page per job.
