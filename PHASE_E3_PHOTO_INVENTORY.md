# Phase E3 — New Photograph Inventory & Disposition

**Companion to `PHASE_E3_PREMIUM_VISUAL_REFINEMENT.md`.** Covers the 3 additional photographs supplied directly in this conversation.

**Update**: the owner has since confirmed directly that all three photographs came from Ashley, the founder. That resolves the one question this document couldn't answer on its own — **authenticity is now owner-confirmed for all three.** It does not resolve the separate, still-open question of which town, which service, or (for photo 1) which company's job each one shows — that's genuinely different information, and this revision keeps the two apart rather than treating the first as evidence for the second.

## Executive summary

- **Authenticity: OWNER CONFIRMED** for all three — genuine Axis Scaffolding photography, per the founder directly.
- **Project / location / service metadata: still not established** for any of the three, and still not invented for any of them.
- **Revised publication decision**: all three are now published — on `/gallery` only, in a new "Recently Added" section, using **only** the confirmed fact (genuine Axis work) and no fabricated town, service, or client relationship. Full disposition and exactly what's still needed per photo is in §2.

## 1. Technical inventory & duplicate check (unchanged from the original pass)

| # | Dimensions | Format | File size | EXIF |
|---|---|---|---|---|
| 1 | 1536×2048 | JPEG | 521 KB | None (stripped) |
| 2 | 1536×2048 | JPEG | 529 KB | None (stripped) |
| 3 | 1536×2048 | JPEG | 474 KB | None (stripped) |

Compared against a contact sheet of all 14 existing `PROJECTS` photos directly — no exact or near duplicates. Genuinely new material. All three processed into the site's existing image pipeline as `project-15`/`16`/`17.webp` with the same `-480w`/`-768w`/`-1080w` responsive variants every other project photo has (same WEBP quality=85 conversion `generate_media_assets()` already uses for `project-1`–`7`; `project-8`–`14` were themselves committed the same way, without a `generate_media_assets()` step, so this matches existing precedent exactly).

## 2. Individual disposition (revised)

### Photo 1 — end-of-terrace brick house, "The Old Bakery" — now `project-15`

**Objectively visible**: two-storey brick terraced house, "The Old Bakery" door plate, scaffold to roof height, and a banner mounted on the scaffold reading "TUDOR ROOFING SPECIALISTS LTD" with a phone number and web address.

**Authenticity**: confirmed (owner). **Publication**: **PUBLISHED — GALLERY (supporting, untagged).** The Tudor Roofing sign is treated exactly as the owner directed: a genuine detail of a genuine photograph, not evidence of who the client was or what service this represents. No caption or alt text makes any claim about Tudor Roofing, a client relationship, or a service category. **Still required**: town, service category, and (only if the owner wants it recorded) the nature of the trade relationship visible in the shot.

### Photo 2 — large detached house, cream gable, integral garage — now `project-16`

**Objectively visible**: detached house, cream weatherboard/render gable, integral double garage, scaffold along the rear/side elevation, ladder, debris-chute rig. No signage of any kind.

**Authenticity**: confirmed (owner). **Publication**: **PUBLISHED — GALLERY (supporting, untagged).** **Still required**: town and service category — nothing in the photo itself supplies either.

### Photo 3 — 1930s semi-detached house, full scaffold wrap — now `project-17`

**Objectively visible**: semi-detached house, bay windows, full-height scaffold with netting, a van in the left foreground with visible "AXIS"-reading livery.

**Authenticity**: confirmed (owner) — the visible van livery is consistent with, though no longer needed to establish, that confirmation. **Publication**: **PUBLISHED — GALLERY (supporting, untagged).** **Still required**: town and service category.

## 3. What each photo still needs to move from "supporting, untagged" to a full `PROJECTS` entry

Unchanged questions, now purely about metadata rather than authenticity:

1. **Photo 1 / `project-15`**: which town? Which service category?
2. **Photo 2 / `project-16`**: which town? Which service category?
3. **Photo 3 / `project-17`**: which town? Which service category?

The moment any one is answered, that photo moves from `UNTAGGED_PHOTOS` into `PROJECTS` in `build_site.py` with a real `area_slug`/`service_slug`/`location` — no other code changes needed, the responsive images already exist, `project_card()` already knows how to render a fully-tagged entry with its area/service links and lightbox behaviour.

## 4. What was actually built this round

Rather than a second one-off workaround, this reuses the site's own image pipeline exactly as-is and adds one small, clearly-scoped piece to `build_site.py`:

- A new `UNTAGGED_PHOTOS` list (just slug + dimensions — no fabricated fields) sitting next to `PROJECTS`.
- A new `untagged_photo_card()` renderer — deliberately **not** `project_card()`: no area link, no service link, no category-filter tagging, no lightbox wiring. Each photo links directly to its own full-size image (opens in a new tab, `rel="noopener noreferrer"` + `aria-label`, matching the site's existing external-link pattern).
- A new "Recently Added" section on `/gallery` only, below the fully-tagged "Full Portfolio" grid, with its own honest intro line ("...haven't been matched to a specific town or service page yet, so they're shown here on their own rather than under a guessed location") and a plain per-photo caption ("Genuine Axis Scaffolding work — full project details to follow.").
- New CSS (`.untagged-photo-grid`/`.untagged-photo`) matching the site's existing flat, photography-first card treatment — no new visual language introduced.

**Deliberately not done**: the homepage, service pages, and About page are unchanged — per the owner's explicit instruction not to force all three onto the homepage, and because none of the three has a confirmed service relationship that would make it the right choice for a specific service page's early split-grid. The `PROJECTS`/`project_card()` data model itself was **not** redesigned — the owner separately flagged a longer-term "Verified Axis Work, with optional Project/Location/Service" model as worth considering later, once more founder-supplied photos without full metadata become a recurring pattern, but asked explicitly not to build that now. This round used the smallest addition that avoids fabricating anything, not a schema change.

## 5. Everything else from `PHASE_E3_PREMIUM_VISUAL_REFINEMENT.md` stands unchanged

The service-page split-grid photography, the gallery's editorial wide-tile treatment on the Full Portfolio grid, and the About page's "Real Work, Not a Brochure" section — all delivered earlier in this same PR — are unaffected by this photo addition and remain as validated and documented there.
