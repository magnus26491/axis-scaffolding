# Phase E2 — Rayleigh URL / Intent Alignment: Decision + Minimal Implementation

**Status: decision phase, evidence-first.** Scoped to the single Rayleigh attribution question raised in E1. No paid-search work, no broad SEO changes, no new pages, no keyword stuffing, no changes to unrelated pages.

## 1. What E1 discovered (recap)

- `/areas/rayleigh`'s technical setup is completely correct: canonical (www, no trailing slash), in `sitemap.xml`, no `noindex`, 42 internal links pointing to it, unique title/meta, 47 genuine town-specific mentions. **Re-verified unchanged in this phase** (still true after the Phase E homepage reorder).
- 39 Rayleigh-modified queries rank position 1–8 with **5,542 total impressions** — re-confirmed exactly against `Queries.csv` in this phase — yet **1 click** across all 39 (0.018% CTR).
- `/areas/rayleigh` shows **zero rows at all** in `Pages.csv`, in both available pulls (Aug 26 and Sep 1), under any trailing-slash form.
- The homepage's own title (`Scaffolding Essex | Axis Scaffolding Ltd Rayleigh Team`), 23 on-page mentions of "Rayleigh", and `LocalBusiness` schema `addressLocality: "Rayleigh"` give it a real, legitimate topical overlap with the area page. E1 treated this as the leading hypothesis for where the impressions were landing, while flagging (§3, §6) an unresolved data-quality question: which GSC property generated these exports, and why `Pages.csv` sums to 42.6% more impressions than the confirmed site-wide total from `Countries.csv`/`Devices.csv`.

That last open question is what this phase resolves.

## 2. New finding this phase: the exports are scoped to the bare (non-canonical) host

Re-reading `Pages.csv` directly (not just checking for the Rayleigh page's absence, but every URL in the file) turns up something E1 didn't check: **every single one of the 46 rows in the Sep 1 pull, and all 42 in the Aug 26 pull, use the bare `https://axisscaffoldingessex.co.uk/...` host — zero `www.` URLs appear anywhere, in either pull.**

The site's mandated canonical host is `www` (enforced by the CI validation script, confirmed correct site-wide). So this export is either:
- pulled from a GSC **property scoped to the bare, non-canonical, redirect-source host**, or
- pulled from a domain property whose `Pages.csv` report is, for some reason, dominated by legacy bare-host URL entries.

Either way, this is a materially different — and better-evidenced — explanation than E1's leading hypothesis.

**Directly tested the bare-host redirect** (not assumed) for both the homepage and the Rayleigh page specifically, since a broken redirect on one but not the other could explain the asymmetry:

| URL requested | Result |
|---|---|
| `https://axisscaffoldingessex.co.uk/` | `301` → `https://www.axisscaffoldingessex.co.uk/` |
| `https://axisscaffoldingessex.co.uk/areas/rayleigh/` | `301` → `https://www.axisscaffoldingessex.co.uk/areas/rayleigh/` |

**Both redirect correctly and identically.** This rules out "the bare-host redirect is broken for Rayleigh specifically" — it isn't. Also directly tested the canonical (www) host for both trailing-slash forms of the Rayleigh page: `/areas/rayleigh` and `/areas/rayleigh/` both return `200` with no redirect between them (ordinary GitHub Pages directory-index behaviour — this is also why several *other* area pages appear as two separate split rows in `Pages.csv`, e.g. Basildon at 926 + 89 impressions, Brentwood at 744 + 282, Rochford at 631 + 83 — the trailing-slash and non-trailing-slash forms are being counted as different "pages" by whichever report generated this export. This split-counting is almost certainly what produces `Pages.csv`'s 42.6% excess over the true site-wide total flagged in E1 — not a parsing error on my part, and not unique to Rayleigh.)

**The important asymmetry**: Rayleigh doesn't appear as a *split* row like Basildon or Brentwood — it doesn't appear at **all**, under either form, in either pull. Every other area page has *some* bare-host history; Rayleigh has none.

## 3. Diagnosis

The homepage (`/`) is almost certainly the site's oldest, most heavily-linked URL — live since the very first deployment, long before the current `www`-canonical architecture existed. A URL can retain search-visible impressions under a legacy hostname for a long time after a redirect is correctly put in place, simply because Google continues to show previously-indexed result entries until it fully re-crawls and consolidates them — this is normal, well-documented post-migration behaviour, not a bug.

`/areas/rayleigh`, by contrast, is part of the site's *rebuilt* area-page architecture (see `SEO_TECHNICAL_AUDIT.md` §17, "/areas — investigated, then rebuilt"). If this page was built or substantially reworked *after* the `www` canonical + redirect architecture was already correct, Google would have had no reason to ever discover or index a bare-host version of it — it would only ever have crawled the canonical `www` URL. That page's real performance data would exist entirely under the `www` host, and would be **structurally invisible** to an export scoped to (or dominated by) the bare host — not because the page isn't ranking, but because this particular data pull cannot see it.

This does not overturn E1's homepage-title/schema finding — that overlap is real and could still be a contributing factor once true `www`-side data is available — but it is no longer the best-supported explanation. The property-scope explanation accounts for the *exact* pattern observed (older pages present, some split across trailing-slash forms; a newer page absent under every form) without requiring the homepage to be actively outranking the area page.

## 4. Chosen outcome: **D — Technical/measurement attribution issue**

The technical architecture (§1, re-verified) is correct. The apparent "zero impressions" is best explained by the exports being scoped to a host that structurally cannot report `/areas/rayleigh`'s real, `www`-side performance — not by a site defect, not by the homepage stealing rankings, and not by the area page being under-signalled. Per the explicit instruction for this phase: **the evidence supports a documented no-change decision, not a manufactured fix.**

This was weighed against the alternatives directly:
- **Outcome A (keep architecture, no explanation needed)** — rejected as the *primary* framing only because leaving the property-scope question undocumented would waste the genuine progress made this phase; but its practical consequence (no site change) is identical to D's.
- **Outcome B (strengthen the area page)** — not supported. Nothing in §1's re-verification shows the page under-signalled: correct canonical, sitemap, internal links, unique and substantial content. Adding more Rayleigh references would not fix a measurement artifact, and was explicitly ruled out by the brief regardless.
- **Outcome C (homepage should formally own primary Rayleigh intent)** — not adopted. There's no evidence the area page is actually losing to the homepage in real (www-side) search results; treating that as settled and demoting the area page's role would be acting on the weaker of two explanations.
- **Outcome E** — no other explanation found that fits the evidence as well.

## 5. Implementation: none

No site code, copy, canonical, sitemap, robots, schema, or internal-linking changes were made to `/areas/rayleigh`, the homepage, or any other page. Nothing about this diagnosis points to a defect in the current architecture, and the brief's own instruction is explicit: a documented no-change decision is an acceptable — and here, the correct — deliverable.

## 6. Validation performed

Since no site output changes, this is a verification pass, not a build-drift check:

- `python3 build_site.py` + `python3 scripts/seo_postprocess.py` — run to confirm a clean baseline; `git diff --stat` after both showed no changes to any generated file.
- `python3 scripts/check_testimonials.py` — passes (untouched).
- Re-ran the canonical/sitemap/robots/internal-link checks from E1 §1 directly against current `main` (post-Phase-E) rather than assuming they still held — all unchanged and correct.
- Directly tested (not assumed) the bare-host redirect for both `/` and `/areas/rayleigh/`, and the trailing-slash behaviour of the canonical host for `/areas/rayleigh` — see §2.
- Re-confirmed the 5,542-impression, 1-click Rayleigh query-cluster total directly against `Queries.csv` (matches the figure already in circulation).
- Confirmed `/areas/rayleigh` is absent from `Pages.csv` under every URL form, in both available pulls — not a one-off pull artifact.

## 7. Remaining owner/measurement dependency

This phase substantially narrows the explanation but cannot fully close it without live account access. One thing would settle it definitively, and it's a Search Console action, not a repo change:

1. **Confirm which GSC property generated these exports** (Search Console's property switcher shows this directly — a URL-prefix property for `https://axisscaffoldingessex.co.uk/` would explain the 100% bare-host pattern outright; a domain property would mean the bare-host dominance reflects genuine index history instead).
2. If a **separate `www`-scoped or domain property** exists (or can be added — domain properties are free and take only DNS verification), pull the same Pages/Queries report from it and check `/areas/rayleigh` there directly.
3. In the GSC UI (not the bulk CSV export), click into 2–3 top Rayleigh queries → their own "Pages" tab — this is the joined query→URL view no static export provides, and would show today's actual answer directly.
4. Run URL Inspection on `https://www.axisscaffoldingessex.co.uk/areas/rayleigh` — confirms indexed/eligible status independent of any Performance report.

None of these require a site code change to act on — they're the account owner's next step if a definitive answer (rather than a well-evidenced no-change decision) is wanted.

## 8. Confirmation

The £5m insurance claim and the 4 services without tagged project photos remain untouched. No Rayleigh keyword density was added anywhere. No new area pages, no paid-search work, no unrelated page changes.
