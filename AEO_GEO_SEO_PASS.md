# AEO / GEO / SEO pass (Oct 2026)

What this pass changed and why, plus the off-site items the codebase can't do.
Everything on-page is generated from `build_site.py`, so markup can't drift from
visible content.

## Done in code
- **FAQPage markup on all 9 service pages** (they already showed FAQs, but had no markup) and on the
  12 core area pages. Markup is generated from the same function that renders the visible accordion
  (`service_faqs()`, `area_faqs()`), so they always match. Area-page answers reuse wording the site already
  publishes (cost / speed / licence); only the question names the town.
- **Answer-first line** at the top of every core area page.
- **Service schema** on each service page (provider = the business `@id`, areaServed, serviceType).
- **Article schema** on the three guides; **AboutPage / ContactPage / CollectionPage** types on
  /about, /contact (and /quote) and /gallery; **WebSite** + **WebPage** nodes on every page.
- **LocalBusiness enriched:** all 12 core towns + Brentwood, Loughton, London in `areaServed`;
  `hasOfferCatalog` (9 services), `knowsAbout`, `contactPoint` (phone and WhatsApp), Companies House
  `identifier`, logo, image, description. No AggregateRating (self-serving reviews aren't eligible).
- **Explicit robots meta** allowing large snippets / image previews (eligibility for rich results and AI
  summaries).
- **robots.txt** names the AI search / assistant crawlers (OAI-SearchBot, ChatGPT-User, GPTBot, ClaudeBot,
  Claude-SearchBot, Claude-User, PerplexityBot, Google-Extended, Applebot-Extended, ...). Remove an entry to opt out.
- **/llms.txt**: machine-readable summary (facts, services, areas, guides, contact). Generated from the same
  constants as the site, including the approved rating.
- **sitemap `<lastmod>`** now comes from git history (real change dates; CI checks out full history).
  Omitted rather than invented when unknown.
- **Two titles over 60 characters** shortened (/contractors, /guides/do-i-need-scaffolding).
- **Google Fonts stylesheet** no longer blocks first render (preload + onload swap, `<noscript>` fallback).
- Footer links to the `/guides` hub from every page.

## Needs the owner (off-site; the biggest remaining levers)
- Google Business Profile: website link (still the old domain), opening hours (profile says 24 hours, the
  site says Mon–Fri 07:00–18:00 — the site's hours schema stays as is until confirmed), services, categories,
  photos and regular posts.
- Keep asking for Google reviews (review count is shown from `APPROVED_RATING`; update it when it changes).
- Consistent NAP citations: Bark, Yell, Checkatrade, Trustpilot, Facebook, Instagram, LinkedIn (send the URL to add to `sameAs`).
- Local links: roofers, builders, plasterers/renderers and suppliers the business works with.
- Search Console: submit the sitemap, then watch /areas/rayleigh vs the homepage for Rayleigh queries.

## Deliberately not done
- No invented dates, ratings, awards, memberships (e.g. NASC) or local detail for new towns.
- No new area pages: they need genuine local detail from the business (South Woodham Ferrers is a good next one).
