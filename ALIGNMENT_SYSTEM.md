# Axis Scaffolding — Global Layout & Alignment System

Produced as part of V2.1 (Global Layout & Alignment audit), across two
rounds. This is a durable reference, not a published page — it exists so
every future PR can check its own work against the same standard, per
the standing rule:

> Every subsequent PR should ask: "Did this change introduce any visual
> drift against the global grid?" That belongs in the V2 definition of
> done.

## Round 1 → Round 2: why this document changed shape

Round 1 fixed the reported bug (the hero trust row wasn't centred) and
generalised the fix: card grids that don't divide evenly were converted
from CSS Grid to a centred flexbox, so a leftover row centres itself
instead of sticking to the left edge with dead space.

Round 1 review correctly rejected that as the finish line. Centred is
not the same as composed: 5 decision cards rendering as 4 in a full row
plus 1 alone underneath, or 9 services as 4 + 4 + 1, is mathematically
centred and still reads as a broken layout to a human — the lone item
looks like an accident, not a decision. "Flexbox centres whatever's
left over" was a general-purpose fallback, not a design.

Round 2 replaces that organic reflow with **explicit, deliberate
per-breakpoint compositions** for the two flagged components — the
system is described below in "Explicit composition rules", which is now
the authoritative reference for how these components behave. It also
fixes an independent bug the stricter verification in this round
surfaced (a `<figure>` element's unreset browser-default margin), and
gives the "Not Sure" decision card a distinct visual identity so its
position in the layout reads as intentional rather than "the leftover
card."

## The system, in one paragraph

One content container (`.container`, `width:min(1160px, calc(100% -
2rem))`, widening to 1280px above 1440px) — verified in Round 2 via
`getBoundingClientRect`, not just source reading, that the decision,
services, builder (`.split-grid`) and projects sections all resolve to
byte-identical container edges (see "Container system audit" below).
One section-rhythm token (`--space-2xl`, 4.5rem, driving `.section`
padding). One spacing scale (`--space-3xs` through `--space-3xl`) for
new or touched rules. The two homepage card grids with a known, fixed
item count (5 decision cards, 9 services) now use **explicit
per-breakpoint column compositions** — see below — rather than letting
flexbox decide organically. The gallery's 14-project grid, which is
reused by pages with other item counts too, keeps the more general
centred-flexbox fallback from Round 1, with a documented rationale for
why (its "real" fix — a featured photo + editorial layout — already
exists, unmerged, in Phase 3).

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

### 2. Card grids with uneven row counts left orphan rows stuck to the left edge (Round 1) → replaced with deliberate compositions (Round 2)

**Components**: `.decision-grid` (5 cards on the homepage), `.services-grid` /
`.service-listing` (9 cards), `.projects-grid` (14 cards on the gallery
page).

**Root cause**: all three used CSS Grid with a fixed
`grid-template-columns:repeat(N,1fr)`, changed per breakpoint via media
queries (5 → 3 → 1 for decisions; 3 → 2 for services/projects). `1fr`
tracks always fill 100% of the row, so when the item count doesn't
divide evenly by the column count — 5÷3, 9÷2, 14÷3 all leave a
remainder — the last row's item(s) occupy the first N columns and the
remaining track(s) sit empty. The item is mathematically "in the grid"
but visually left-stuck with dead space to its right.

**Round 1 fix (superseded for decisions/services)**: converted all
three to `display:flex; flex-wrap:wrap; justify-content:center` with an
organic `flex-basis`/`max-width` per card that reflowed to roughly
5/3/1 or 3/2/1 columns depending on how many happened to fit at a given
width. This centred the leftover row instead of left-sticking it, but
the *exact* split wasn't deliberately chosen — at 1024px the decision
grid organically produced 4+1, and the services grid 4+4+1, which is
centred but still reads as an accident, not a decision.

**Round 2 fix**: for the two components with one fixed, known count
(decisions = 5, services = 9 — see "Explicit composition rules" below),
card width is now an exact **percentage of the row** (e.g.
`calc(20% - 1rem)` for 5 columns), set explicitly per breakpoint tier
via `min-width` media queries, with `flex-grow:0; flex-shrink:0`. A full
row's cards always sum to exactly 100% and sit flush with the container
edges (matching every other section); only a genuinely short trailing
row is narrower than 100% and gets centred. This replaced the two
Round-1 organic-reflow rules for `.decision-card` and `.service-card`
with deterministic ones — the exact column count at each breakpoint is
now a decision, not whatever happens to fit.

`.projects-grid` (14 items on the gallery page, but reused by the
homepage's 6-item preview and potentially other counts) keeps the
Round-1 percentage-based centred-flexbox approach rather than a
component-specific composition — see "Not done" below for why a richer
featured/editorial treatment wasn't built here.

**Verified**: rendered-DOM row grouping (grouped card bounding boxes by
`top` position) confirmed the expected per-row counts at
320/375/390/430/768/1024/1280/1440px, zero horizontal overflow at any
width, and — critically, per the Round 2 review — **row-edge
verification**: for every full row, the row's own left/right edges were
checked against the container's left/right edges and confirmed
`flush=true` (within 2px) at every breakpoint; only the intentionally
short trailing row is `flush=false` (narrower, centred). Screenshots at
each breakpoint confirm the decision grid renders as 5 (desktop) / 3+2,
centred (tablet) / 1-per-row (mobile), and the services grid as
3×3×3 (desktop+tablet) / 1-per-row (mobile) — no orphan card at any
breakpoint for either component.

### 2b. `<figure>` element's unreset default margin (found during Round 2 verification)

**Component**: `.project-item` (the `<figure>` wrapping each project
photo in `.projects-grid`).

**Root cause**: `<figure>` carries a browser default UA-stylesheet
margin (`1em 40px`) that was never reset. This predates this PR — it
was already present under the original CSS Grid version of the
component — but Round 1's fixed-percentage flex-basis (`flex-shrink:0`)
made it newly visible as a real bug rather than a cosmetic gutter: the
un-reset 80px of margin-left+right per card meant 3 cards' declared
widths summed to fractionally more than the row's available width,
which a `flex-shrink:0` row can't compress, so the row wrapped after 2
cards instead of 3 — reintroducing the exact "row doesn't reach the
container edge" problem this whole system exists to fix. Caught by the
Round 2 discipline of checking row-edge flushness via
`getBoundingClientRect`, not by trusting that "the CSS looks right."

**Fix**: `.project-item { margin:0; }`.

**Verified**: re-measured `.project-item` bounding boxes on the gallery
page — 3 cards now span exactly `[80,1360]`, matching the container
edges exactly, both for the first (full) row and confirmed via an
element-scoped screenshot (a full-page `page.screenshot()` had an
unrelated headless-Chromium paint-timing artifact on the same page —
documented so it isn't mistaken for a second bug — but
`getComputedStyle`/`getBoundingClientRect` plus a `grid.screenshot()`
scoped to just the grid element both independently confirmed correct,
flush 3-column rendering).

## Explicit composition rules (per component, per breakpoint)

Requested directly: these are decisions, not accidents of flexbox math.
Breakpoint bands follow the site's own existing convention (the
mobile nav already switches at 768px), not an arbitrary new scale.

| Component | Mobile (≤768px) | Tablet (769–1024px) | Desktop (≥1025px) |
|---|---|---|---|
| **DecisionGrid** (homepage, 5 cards: Homeowner / Builder·Roofer / Commercial / Emergency / Not Sure) | 1 column | 3 columns → **3 + 2**, the pair centred | 5 columns → one full row |
| **ServiceGrid** (`.services-grid` + `.service-listing`, always 9 cards) | 1 column | 3 columns → **3 + 3 + 3** | 3 columns → **3 + 3 + 3** (same as tablet — see note) |
| **ProjectGrid** (`.projects-grid`, homepage preview = 6, gallery = 14) | 1 column | 3 columns, centred-flexbox fallback (not a fixed composition — item count varies by page) | same |

**Why ServiceGrid stays 3 columns from tablet through desktop, not 2 on
tablet:** 9 services in a 2-column tablet tier is 4 + 4 + 1 — the exact
orphan problem this system exists to prevent. Three columns all the way
down to 769px was evaluated against the "readability" criterion in the
request and judged acceptable (short summaries, already proven at a
similar ~220px card width by the decision grid) — a deliberate choice,
not an oversight.

**Other pages reusing `.decision-grid`** (guide/service pages with 3,
4, or 6 cards, not the homepage's 5) get the same percentage-based
system and therefore the same edge-flush-on-full-rows behaviour, but
the specific breakpoints above were tuned for 5 — they're a genuine
improvement for those other counts (full rows now reach the container
edge, which the original single global `repeat(5,1fr)` rule did not
guarantee for a 4-count or 6-count page) without being a bespoke,
verified-orphan-free composition for every count. A future pass could
add count-specific modifier classes for those pages if they need the
same pixel-perfect treatment; not done here to keep this PR's diff
focused on the two components actually flagged.

### "Not Sure" card — deliberate differentiation, styling only

Requested: the fifth decision card should read as a different kind of
option (an open catch-all), not "whichever card is left over." Added
`.decision-card-open` (dashed border, slightly darker fill) to the "Not
Sure" card only — visible in every composition (a full 5-across row on
desktop, or the trailing pair on tablet) as a deliberately different
treatment, not just a position.

The request's illustrative copy change ("Not Sure? / Tell us what
you're having done.") was **not** applied — this PR's own scope rule
(no content changes) takes precedence, and the copy suggestion was
framed as an example ("I'd perhaps...") rather than a requirement. The
geometry and visual distinction both work without it; happy to make the
one-line copy change separately if still wanted.

## Container system audit

Requested: verify whether the decision/services/builder/projects
sections actually share one page-width system, since they *looked*
slightly different in width in the reviewed screenshots.

**Method**: `getBoundingClientRect()` on each section's `.container`
element at 1440px width (not source reading — the point of this audit
is to catch the gap between "same CSS" and "same rendered result").

**Result**: all four containers resolve to the identical box —
`left:80, right:1360, width:1280` — confirming there is **no real
container-width inconsistency**; all four sections already use the same
`.container` primitive. Three tiers (STANDARD / WIDE / FULL-BLEED) were
not introduced, because the audit found no case of an actual arbitrary
width to consolidate.

**What was actually causing the perceived inconsistency**: the
Round-1 organic-reflow fix, when a row of cards didn't happen to fill
the container's full width, pulled that row's *visible edges* inward
via `justify-content:center` — e.g. the decision grid's first card sat
at `left:130` against a `left:80` container (a 50px inset), while the
services grid — whose organic row happened to nearly fill the
container — sat flush. Different sections were rendering their content
at different insets from the *same* container, which is exactly what
reads as "some sections feel more compressed." This is fixed by the
Round 2 percentage-based composition (fix 2 above): a full row's cards
now always sum to exactly 100% of the container width, so every
section's content is flush with the same container edge unless a row is
deliberately short (and centred) by design.

## Hero composition axis — re-verified

Requested: confirm `h1` → subhead → CTA row → trust rail share one
optical axis, not just that each is independently centred.

**Method**: measured each row's *content* center-x (not the row box's
center, which is meaningless for a full-width flex row — the visible
badges/buttons within it), via `getBoundingClientRect` on each row's
children, at 1440px viewport.

**Result**: `h1` center = 720, subhead (`p`) center = 720, CTA row
content center = 720, trust row content center = 720 — identical to the
viewport's own center (720). All four elements share one exact
optical axis; the trust rail is not "an independent flex row that
happens to also be centred," it measurably lines up with everything
above it.

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

- **Project grid featured/editorial composition.** The request
  explicitly asked for the gallery's 14 photos to be evaluated for a
  featured-item + editorial-grid treatment rather than a uniform
  matrix, rather than forced into one column count. That richer
  composition **already exists**, built for Phase 3 (unmerged PR #21 —
  a featured card, editorial grid weighting, and an accessible
  lightbox, all built on the same `PROJECTS` data). Rebuilding it here
  would duplicate that work and conflict with it at merge time. This PR
  instead applies the same edge-flush, centred-trailing-row treatment
  used for decisions/services to the *current* simple grid (including
  fixing the `<figure>` margin bug above), so the pre-Phase-3 state
  isn't left with an undeliberate composition while the two PRs are
  sequenced — see "Merge-order dependency" below.
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
- **"Not Sure" copy change** — deliberately not applied; see the
  "Not Sure" section above.

## Merge-order dependency (flagged by the user, tracked here)

PR #24 is based on plain `main`, per the "don't stack unmerged
branches" rule — so it does **not** include Phase 3's image pipeline
(PR #21, unmerged), which is where `images/gallery-project-{8..14}.webp`
actually get created. Merging PR #24 in isolation would not *reintroduce*
that gap (it's already present on `main` today, PR #24 doesn't touch
it), but it also wouldn't *fix* it. Recommended merge order, matching
the sequencing given directly:

1. **PR #24** (this one) — composition system.
2. **PR #22** — quote experience.
3. **PR #23** — trust/customer journey (includes the claim-verification
   work and the homepage section reorder).
4. **PR #21** (Phase 3 — projects/image pipeline) whenever it's ready;
   at that point the gallery's featured/editorial redesign is the right
   place to revisit `.projects-grid`'s composition properly, rather than
   the interim edge-flush fix in this PR.
5. Then SEO/AEO/GEO architecture work.

Not acted on automatically — this is a sequencing note for the owner to
confirm, not a merge this session performs.

## Regression-check rule (new standing process, effective immediately)

Per instruction, alignment QA is no longer a one-time pass. **Every PR
from this point forward should be able to answer, before merge:** did
this change introduce any visual drift against the grid/spacing system
above? Concretely:
- New or changed sections use `.container` (or a narrower measure
  centered inside it) — no new arbitrary container widths. Verify with
  `getBoundingClientRect`, not by re-reading the CSS — Round 2 found a
  real gap between "uses `.container`" and "renders flush with it."
- New repeated spacing/gap/padding values pull from the `--space-*`
  scale rather than introducing a new literal.
- A card/item grid with a **known, fixed item count** gets an explicit
  per-breakpoint column composition (percentage-based `flex-basis`,
  `flex-grow:0; flex-shrink:0`, set via `min-width` media queries) —
  worked out deliberately for that count, the way the "Explicit
  composition rules" table above does for decisions/services. Never
  ship "whatever fits" as the final answer for a fixed-count component.
- A grid whose item count **varies by page** (like `.projects-grid`)
  can reasonably use the more general centred-flexbox fallback, but
  check it doesn't produce an orphan-of-1 on any page that reuses it
  where a deliberate composition would be cheap to add instead.
- Any new/edited `<figure>`, `<blockquote>`, or other element that
  carries a browser default margin/padding gets it reset explicitly —
  don't assume "no margin was declared" means "no margin is applied."
- A screenshot check at, minimum, 390px and 1440px for any touched
  section, including once with `prefers-reduced-motion: reduce`; for a
  new fixed-count grid, also check the tablet tier(s) where its specific
  count could produce an orphan.
- The final test from the original request is a good one to keep
  asking: could you draw invisible vertical lines through the page and
  see one consistent grid? Does every repeated component look
  intentionally composed, or does something look like an accidental
  leftover?

## Verification (Round 1 + Round 2)

- Full CI validation script: **PASS** (re-run after Round 2's changes)
- Rebuild-from-clean determinism check: identical file hashes across two
  consecutive builds after each round; only `build_site.py` (source),
  `assets/css/style.css` (generated CSS) and `index.html` (the "Not
  Sure" card's new class attribute) changed — no unexpected HTML drift
- `node -c assets/js/main.js`: valid (JS untouched by this PR)
- Zero horizontal overflow (`scrollWidth - clientWidth === 0`) confirmed
  at all eight requested breakpoints — 320/375/390/430/768/1024/1280/1440
- Rendered-DOM verification (Playwright, real Chromium — not source
  reading):
  - `getComputedStyle`/`getBoundingClientRect` on `.hero-trust-badges`
    and its siblings confirms one shared optical axis (center-x = 720 =
    viewport center, for `h1`, subhead, CTA row, and trust row alike) at
    1440px
  - Card-grid row grouping by bounding-box position confirms the exact
    composition table above at every breakpoint: decision grid 5 / 3+2
    / 1, services grid 3×3×3 / 3×3×3 / 1
  - Row-edge flushness check: every full row's own left/right edges
    matched the container's edges within 2px; the intentionally short
    trailing rows (decision tablet's 2-card row) did not, confirming
    they're centred by design rather than accidentally inset
  - Container audit: `.container` elements in the decision, services,
    builder, and projects sections resolve to byte-identical boxes
  - The `<figure>` margin bug (2b above) was caught by this level of
    verification, not by reading the CSS
- Screenshots reviewed at 320/375/390/430/768/1024/1280/1440px:
  homepage hero, decision grid (every breakpoint, including the 3+2
  tablet composition and the "Not Sure" card's distinct styling),
  services grid (every breakpoint, including the full 3×3×3), gallery
  projects grid (1440/375, plus an element-scoped screenshot to work
  around a headless-Chromium full-page screenshot paint-timing
  artifact — documented above so it isn't mistaken for a layout bug),
  homepage's 6-project preview grid, footer, pricing, FAQ, and
  `prefers-reduced-motion: reduce` renders of both the hero and the
  decision grid (identical to the motion-enabled versions)
