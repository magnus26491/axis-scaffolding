# Axis Scaffolding — Global Layout & Alignment System

Produced as part of V2.1 (Global Layout & Alignment audit). This is a
durable reference, not a published page — it exists so every future PR
can check its own work against the same standard, per the standing rule:

> Every subsequent PR should ask: "Did this change introduce any visual
> drift against the global grid?" That belongs in the V2 definition of
> done.

## The system, in one paragraph

One content container (`.container`, `width:min(1160px, calc(100% - 2rem))`,
widening to 1280px above 1440px). One section-rhythm token
(`--space-2xl`, 4.5rem, driving `.section` padding). One spacing scale
(`--space-3xs` through `--space-3xl`) for new or touched rules. Card
grids that don't reliably divide evenly (5 decision cards, 9 services,
14 gallery projects) use `display:flex; flex-wrap:wrap; justify-content:
center` with a `flex-basis`/`max-width` per card, not CSS Grid's
`repeat(N,1fr)` — so a leftover last row centers itself instead of
sticking to the left edge with dead space on the right. Everything else
in the stylesheet was audited against this system and left alone where
it was already consistent (see "Reviewed, no change needed" below) —
this was a targeted fix of confirmed root causes, not a full rewrite.

## Issues found and fixed

### 1. Hero trust/spec badge row not centered (the reported issue)

**Component**: `.hero-trust-badges` (homepage hero — CISRS Qualified /
Fully Insured / 10+ Years' Experience / Free Quotes).

**Root cause**: every other row in the hero (`h1`, `p`, `.hero-cta-row`)
is an explicitly centred flex/text-align element. `.hero-trust-badges`
was also `display:flex; flex-wrap:wrap`, but had no `justify-content` —
which defaults to `flex-start`. So the badges were left-aligned inside a
full-width row sitting under a centred headline and CTA row above it.
That's what read as "not one balanced, centred group" — it wasn't a
per-badge spacing problem, it was a missing group-level property.

**Fix**: `justify-content:center` added to the row (one property, group
level, not per-badge margins). Gap and top-margin now use
`--space-2xs`/`--space-md` instead of restated literals.

**Verified**: `getComputedStyle(...).justifyContent === 'center'` at
390/768/1024/1440px, plus visual screenshots at each width and with
`prefers-reduced-motion: reduce` (alignment is identical — nothing here
depends on animation).

### 2. Card grids with uneven row counts left orphan rows stuck to the left edge

**Components**: `.decision-grid` (5 cards), `.services-grid` /
`.service-listing` (9 cards), `.projects-grid` (14 cards on the gallery
page).

**Root cause**: all three used CSS Grid with a fixed
`grid-template-columns:repeat(N,1fr)`, changed per breakpoint via media
queries (5 → 3 → 1 for decisions; 3 → 2 for services/projects). `1fr`
tracks always fill 100% of the row, so when the item count doesn't
divide evenly by the column count — 5÷3, 9÷2, 14÷3 all leave a
remainder — the last row's item(s) occupy the first N columns and the
remaining track(s) sit empty. The item is mathematically "in the grid"
but visually left-stuck with dead space to its right. This is a
systemic pattern, not a one-off: it affects every page reusing these
three shared classes, including five other `.decision-grid` instances on
guide/service pages that aren't the homepage.

**Fix**: converted all three to `display:flex; flex-wrap:wrap;
justify-content:center` with a `flex-basis`/`max-width` per card
(tuned to reproduce the same ~5/3/1, ~3/2/1 per-row density the grid
version had at each breakpoint). Flexbox centers a partial last line by
default — no per-breakpoint column-count overrides needed any more, so
the two `.decision-grid` media-query rules were removed as redundant.

**Verified**: rendered-DOM row grouping (grouped card bounding boxes by
`top` position) confirmed the expected per-row counts at 390/768/1024/
1440px, zero horizontal overflow at any width, and screenshots at each
breakpoint show the orphan row (the 5th decision card, the 9th service
card, the trailing 2-project row on the gallery page) centered under
the grid above it instead of pinned left.

### 3. No shared spacing scale

**Root cause**: the stylesheet's literal spacing values were already a
reasonably disciplined soft rhythm (0.25rem-ish increments — no genuine
17px/23px/29px chaos), but they were restated as literals everywhere,
including the single highest-leverage value in the file: `.section`'s
vertical padding, which controls the dark/light/dark/light rhythm on
every page.

**Fix**: added a documented `--space-3xs` … `--space-3xl` scale to
`:root`, mapped onto values already in use (not new numbers). Applied it
to `.section` padding and to the components touched by fixes 1 and 2
above. Left already-consistent component-specific values (`.btn`
padding, `.service-card` padding, etc.) as literals rather than
retrofitting the whole ~2,900-line stylesheet in one pass — see "Not
done" below for why, and the regression-check rule this doc sets up for
catching drift going forward instead.

## Reviewed, confirmed already correct — no change needed

- **`.btn`** base class already sets `display:inline-flex;
  align-items:center; justify-content:center; border:2px solid
  transparent` — buttons of different variants (filled/outline) already
  share one height and baseline; the always-reserved 2px border prevents
  the classic "outline button is a couple of pixels shorter" bug.
- **`.split-grid`** (text/image sections — "Why Builders & Homeowners
  Choose Axis") already has `align-items:center`, vertically centring
  text against the image as required.
- **Footer** (`.footer-grid`, 4 columns) — reviewed via screenshot;
  column widths, heading baseline, and link alignment are already
  structurally balanced.
- **FAQ accordion** (`.faq-wrap`, max-width:900px) — question/answer
  text and the accordion control share one consistent left/right edge
  and indentation; open vs. collapsed items don't shift width.
- **Pricing block** — heading, indicative-price answer box, factor list
  and CTA all share the container's left edge; no drift.
- **Areas pills** (`.area-pills`) — left-aligned by design (the section
  heading and intro are also left-aligned here, not centred), so this is
  consistent, not asymmetric-by-accident.
- **Icon sizing** — icons differ in size between components by design
  (44px decision icons vs. 40px service icons vs. 36px footer-social
  circles vs. 40px process-step numerals), reflecting each component's
  own visual hierarchy. Each component is internally consistent; this is
  the "controlled asymmetry, not everything identical" the brief asked
  for, not drift.

## Intentional asymmetry retained (not a bug)

- `.hero h1` is capped at `max-width:980px` for line-length, while
  `.hero-cta-row` and `.hero-trust-badges` span the full container width
  with their *content* centered inside — all three still share the same
  horizontal center axis, they just have different box widths. This
  reads as one composition because the axis is shared, not because every
  box is the same width.
- Narrower inner measures (`.faq-wrap` 900px, `.connect-inner` 800px)
  nested inside the outer 1160/1280px `.container`, centered via
  `margin:0 auto` — a deliberate reading-measure narrowing, symmetric
  around the same center axis, not container drift.
- `.cta-banner-inner` uses `justify-content:space-between` (text left,
  button right) — an intentional two-side layout, not a centering bug.

## Not done in this PR (by design, per the "layout only" scope)

- **Full literal-value → token migration.** Only the highest-leverage,
  repeated values were tokenized (`.section` padding, the three grids'
  gap/basis). The remaining component-specific padding/gap values are
  already internally consistent (confirmed via audit) but still written
  as literals. Retrofitting all of them in one pass across a ~2,900-line
  generator would be a much larger, higher-risk change for a real-site
  generator with no visual diffing in CI; the regression-check rule
  below is the intended way to keep drift from creeping back in, rather
  than trying to eliminate every literal in one sitting.
- **`images/gallery-project-{8..14}.webp` are missing** (only `.jpg`
  originals exist on `main`), so the gallery page's last two project
  photos render broken on this branch. This is not a layout defect and
  not new — it's the same file-extension mismatch already found and
  fixed with a full image-reprocessing pipeline in the unmerged Phase 3
  PR (`#21`). Duplicating that fix here would be image-asset-pipeline
  work outside this PR's layout-only scope, and would fight PR #21 on
  merge. Left untouched; will resolve once #21 merges.
- **No SEO/AEO/GEO/content/analytics changes** — per instruction, this
  PR is layout/design-system only. Content questions raised while
  reading the templates (e.g. `/gallery`'s "from our Benfleet base"
  phrasing) were noticed but are out of scope here and already tracked
  as content-audit items from the trust-journeys phase (PR #23).

## Regression-check rule (new standing process, effective immediately)

Per instruction, alignment QA is no longer a one-time pass. **Every PR
from this point forward should be able to answer, before merge:** did
this change introduce any visual drift against the grid/spacing system
above? Concretely:
- New or changed sections use `.container` (or a narrower measure
  centered inside it) — no new arbitrary container widths.
- New repeated spacing/gap/padding values pull from the `--space-*`
  scale rather than introducing a new literal.
- Any new card/item grid with a variable or non-fixed item count uses
  the flex + `justify-content:center` + `flex-basis` pattern from fix 2
  above, not a bare `repeat(N,1fr)` CSS Grid.
- A screenshot check at 390px and 1440px (minimum) for any touched
  section, including once with `prefers-reduced-motion: reduce`.

## Verification (this PR)

- Full CI validation script: **PASS**
- Rebuild-from-clean determinism check: identical `assets/css/style.css`
  hash across two consecutive builds; only `build_site.py` (source) and
  `assets/css/style.css` (generated output) changed — no HTML drift,
  as expected for a CSS-only change
- `node -c assets/js/main.js`: valid (JS untouched by this PR)
- Zero horizontal overflow (`scrollWidth - clientWidth === 0`) at
  390/768/1024/1440px on the homepage
- Rendered-DOM verification (Playwright, real Chromium — not source
  reading): `getComputedStyle` on `.hero-trust-badges` confirms
  `justify-content:center` at every breakpoint; card-grid row grouping
  by bounding-box position confirms the expected per-row counts and that
  orphan rows center rather than left-stick
- Screenshots reviewed: homepage hero (1440/768/390, plus
  reduced-motion 1440), decision cards (768/1024, orphan-row case),
  services grid (1440, orphan-row case), gallery projects grid (1440,
  orphan-row case), footer, pricing, FAQ
