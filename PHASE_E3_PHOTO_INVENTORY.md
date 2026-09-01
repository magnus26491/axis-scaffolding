# Phase E3 — New Photograph Inventory & Disposition

**Companion to `PHASE_E3_PREMIUM_VISUAL_REFINEMENT.md`.** Covers the 3 additional photographs supplied directly in this conversation. No image files were provided with filenames, EXIF, or written captions — everything below is either objectively visible in the photograph itself or explicitly marked as requiring owner confirmation. Nothing was inferred from appearance and presented as fact.

## Executive summary

All three photographs are genuine scaffolding photographs, correctly exposed, full resolution, no technical defects — and **none of them can be safely published into the gallery, homepage, service pages, or About page in this round**, because none carry the minimum information the site's actual data model requires (a specific location, a specific service category, and confidence that the job shown is genuinely Axis's own work) without inventing it. This is a real, evidence-based outcome, not a shortfall — see §5 for exactly what would unlock each one.

## 1. Technical inventory

| # | Dimensions | Format | File size | EXIF | Orientation |
|---|---|---|---|---|---|
| 1 | 1536×2048 | JPEG | 521 KB | None (stripped) | Portrait |
| 2 | 1536×2048 | JPEG | 529 KB | None (stripped) | Portrait |
| 3 | 1536×2048 | JPEG | 474 KB | None (stripped) | Portrait |

All three are consistent, full-resolution phone-camera output — no corruption, no unusable thumbnails, no quality issue that would rule any of them out on technical grounds alone. No EXIF survived (likely stripped by the upload pipeline before reaching this session), which removes what would otherwise have been the single most useful source of genuine location/timestamp data — this is the main reason §5's questions can't be answered from the files themselves.

## 2. Duplicate / near-duplicate check against the existing 14-photo library

Built a visual contact sheet of all 14 existing `PROJECTS` photos (`project-1.webp` through `project-14.webp`) and compared each of the 3 new photographs against it directly. **No exact or near duplicates found** — different buildings, different scaffold configurations, different streets in every case. These are genuinely new photographic material, not re-crops or repeats of anything already in the library.

One useful pattern did emerge from that comparison, relevant to §3 and §5: **6 of the 14 existing verified photos show a scaffold-mounted "AXIS SCAFFOLDING LTD" banner** (`project-3`, `project-6`, `project-7`, `project-9`, `project-11`, `project-12`) — this appears to be the site's own established convention for how a live Axis job is marked on-site. None of the 3 new photographs show that same banner. This doesn't mean they aren't genuine Axis jobs — plenty of real jobs won't have the banner up in every shot — but it's one less independent confirmation signal than the existing library typically has, which is part of why §5 asks directly rather than assuming.

## 3. Individual disposition

### Photo 1 — end-of-terrace brick house, "The Old Bakery"

**What's objectively visible**: a two-storey brick terraced house with a door plate reading "The Old Bakery," scaffold to roof height along the front elevation on yellow base plates, a grey car (registration visible) and a white van parked in the foreground. **A large banner is mounted on the scaffold itself reading "TUDOR ROOFING SPECIALISTS LTD" with a phone number and web address** — a different company's advertising signage, prominently placed on the job.

**Disposition: HOLD — OWNER INFORMATION REQUIRED.** This is the one photo in the set that needs more than just "which town" before it could ever be considered for publication. A branded competitor/trade-partner sign on a scaffold most plausibly means one of two genuine, unremarkable trade scenarios — Axis erected the scaffold as a subcontractor for Tudor Roofing's job, or this photo isn't an Axis job at all — and I cannot tell which from the image. Publishing this as "Axis project photography" without knowing which is true would risk misrepresenting whose work it shows, so it's held rather than guessed at either way.

### Photo 2 — large detached house, cream gable, integral garage

**What's objectively visible**: a two-storey detached house, cream weatherboard/render upper gable over a red-brick lower storey, an integral double garage, scaffold along the rear/side elevation, a ladder resting against it, a coiled rope-and-pulley debris-chute rig, block-paved driveway. **No signage, branding, or any other identifying mark is visible anywhere in the frame.**

**Disposition: HOLD — OWNER INFORMATION REQUIRED.** Nothing in the photo itself confirms location, service type, or that this is an Axis job specifically (no banner, no branded vehicle, nothing). Genuinely good, usable photography once that information exists.

### Photo 3 — 1930s semi-detached house, full scaffold wrap

**What's objectively visible**: a rendered semi-detached house with bay windows and a dark composite front door (partial house number visible but not fully legible), scaffold wrapping the full height with netting/boarding at the top, and — in the left foreground — **a white van whose visible livery reads "AXIS" with a partial phone number beneath it.**

**Disposition: HOLD — OWNER INFORMATION REQUIRED**, but the most promising of the three. A visibly Axis-liveried van in frame is a real, positive signal (stronger than photos 1 and 2), though on its own it confirms a vehicle was present, not that this specific scaffold is the job it was there for, and — same as the other two — there's no location or service-type information to attach to it yet.

## 4. Verified relationships established this round

**None.** No project, service, or location relationship met the bar for "genuinely supported by Axis source information" (per the brief's own rule) for any of the three photographs. Nothing was tagged, nothing was guessed.

## 5. What would unlock each photo — specific, answerable questions

1. **Photo 1**: Was Axis the scaffolding contractor on this job (i.e., erected/supplied the scaffold for Tudor Roofing Specialists' roofing work), or is this photo not an Axis job? If it is an Axis job — which town, and which service category (most likely residential or temporary-roofing, but only if confirmed)?
2. **Photo 2**: Which town/area was this job in? What service category — residential, roof, or something else?
3. **Photo 3**: Confirm this is a genuine Axis job (the van livery strongly suggests yes). Which town, and which service category?

Any one of these answered turns a held photo into a publishable one on the next pass — no code changes are needed to add a photo once its `PROJECTS` entry (location, category, service_slug, area_slug, label, description) can be filled in with real information; the generator (`build_site.py`) already handles everything else automatically.

## 6. Gallery / homepage / service-page / About changes this round

**None.** Per §3, no photograph could be published without inventing metadata the site's own architecture requires (every `PROJECTS` entry links to a specific `/areas/{town}` and `/services/{slug}` page — a fabricated town or service would create a broken or misleading link, not just a mislabeled caption). This is a genuine, evidence-based "no visual change" outcome, consistent with the same discipline Phase C established: investigated and left unchanged is a correct result, not a shortfall to be papered over.

The three photographs remain available in this conversation's upload store, unused, ready to fold into the existing `PROJECTS` list in `build_site.py` the moment real location/service/relationship information exists for any of them — at that point they'd follow the same `_project_srcset()` responsive-image pipeline as every other photo on the site, no new system needed.

## 7. Everything else from `PHASE_E3_PREMIUM_VISUAL_REFINEMENT.md` stands unchanged

The service-page split-grid photography, the gallery's editorial wide-tile treatment, and the About page's "Real Work, Not a Brochure" section — all already delivered in this same PR — are unaffected by this photo review and remain as validated and documented there. This file adds the photo-inventory record; it doesn't revise any prior finding in that document.
