"""Testimonial & rating-claim integrity check — permanent QA safeguard.

Why this exists: during Phase B (Trust, Consistency & Customer-Journey
Integration) six fabricated or altered customer testimonials were found on
hand-authored PPC landing pages (/lp/*) — near-verbatim copies of real
reviews from build_site.py's TESTIMONIALS list, with the customer's name
and/or a location changed, plus two wholly invented quotes and two
unsourced "Rated 5.0 on Google" claims. See CLAIM_VERIFICATION.md's Phase B
section for the full record. That was found by a one-off manual read —
this script is the permanent safeguard against it happening again,
silently, in either a hand-authored page or a future generator change.

It checks every real HTML page (generated and hand-authored) against
build_site.py's TESTIMONIALS list, the single approved source, and fails
with a non-zero exit code if it finds:

  1. Quoted testimonial-shaped text with no matching approved entry.
  2. Testimonial text that matches an approved entry but is attributed to
     the wrong name.
  3. A location or other descriptor appended to a name that isn't the
     approved entry's platform label (i.e. a fabricated location).
  4. Any "Rated X on Google" / star-rating-out-of-N statement, or any
     schema.org ratingValue / reviewCount / AggregateRating key, anywhere
     on the site — unless build_site.py's APPROVED_RATING is set (it is
     None by default, since no such claim is currently approved anywhere).

This is deliberately a lightweight, pattern-based check against the two
testimonial-display patterns that actually exist in this codebase today —
not a semantic/plagiarism detector. If a third display pattern is ever
introduced (a new component, a new hand-authored page style), extend
GENERATED_CARD_RE / INLINE_QUOTE_RE below to match it, or this check will
silently miss it.

Run manually with `python3 scripts/check_testimonials.py`. Wired into CI
as a required step in .github/workflows/pages.yml.
"""

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from build_site import TESTIMONIALS, APPROVED_RATING  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent

APPROVED_BY_TEXT = {t["text"]: t for t in TESTIMONIALS}


def real_html_files():
    """Yield (relative_path, content) for every real page — excludes
    legacy http-equiv=refresh redirect stubs, which carry no content."""
    for html in sorted(ROOT.rglob("*.html")):
        rel = html.relative_to(ROOT)
        if ".git" in rel.parts:
            continue
        content = html.read_text(encoding="utf-8", errors="ignore")
        if 'http-equiv="refresh"' in content:
            continue
        yield rel, content


# Pattern 1: the generated `.testimonial-card` markup — testimonials() in
# build_site.py. Should always match an approved entry exactly since it's
# rendered directly from TESTIMONIALS; checked anyway as a regression guard
# against a future hand-edit of the generated output or template drift.
GENERATED_CARD_RE = re.compile(
    r'<blockquote class="review-text">\s*"(?P<text>.*?)"\s*</blockquote>.*?'
    r'<span class="reviewer-name">(?P<name>[^<]+)</span>.*?'
    r'<span class="review-source">\s*(?:<img[^>]*>)?\s*(?P<platform>[^<]+?)\s*</span>',
    re.S,
)

# Pattern 2: the hand-authored /lp/* "glass-card" pattern — a quoted
# paragraph immediately followed by a "– Name, Platform" attribution
# paragraph. This is the exact pattern the 6 fabricated testimonials used.
INLINE_QUOTE_RE = re.compile(
    r'<p[^>]*>\s*"(?P<text>[^"]{15,400})"\s*</p>\s*'
    r'<p[^>]*>\s*[–—-]\s*(?P<attribution>[^<]{2,80}?)\s*</p>',
    re.S,
)


def _clean(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip()


def check_generated_cards(rel, content, errors):
    for m in GENERATED_CARD_RE.finditer(content):
        text = _clean(m.group("text"))
        name = _clean(m.group("name"))
        platform = _clean(m.group("platform"))
        approved = APPROVED_BY_TEXT.get(text)
        if approved is None:
            errors.append(f"{rel}: generated testimonial card text has no matching approved entry: \"{text[:80]}\"")
            continue
        if name != approved["name"]:
            errors.append(f"{rel}: generated testimonial card attributes {text[:40]!r}... to {name!r}, approved name is {approved['name']!r}")
        if platform != approved["platform"]:
            errors.append(f"{rel}: generated testimonial card shows platform {platform!r}, approved platform is {approved['platform']!r}")


def check_inline_quotes(rel, content, errors):
    for m in INLINE_QUOTE_RE.finditer(content):
        text = _clean(m.group("text"))
        attribution = _clean(m.group("attribution"))
        approved = APPROVED_BY_TEXT.get(text)
        if approved is None:
            # Only flag if it looks like a genuine testimonial attribution
            # (a capitalised name-like lead-in) to avoid false positives on
            # unrelated quoted strings elsewhere on a page.
            if re.match(r"^[A-Z][a-zA-Z'.\s]{1,40}(,|$)", attribution):
                errors.append(f"{rel}: quoted testimonial text has no matching approved source: \"{text[:80]}\"")
            continue
        attributed_name = attribution.split(",")[0].strip()
        if attributed_name != approved["name"]:
            errors.append(f"{rel}: testimonial text matches {approved['name']!r} but is attributed to {attributed_name!r}")
        if "," in attribution:
            suffix = attribution.split(",", 1)[1].strip()
            if suffix and suffix != approved["platform"]:
                errors.append(
                    f"{rel}: testimonial for {approved['name']!r} has an unapproved location/suffix {suffix!r} "
                    f"(approved platform label: {approved['platform']!r})"
                )


# Deliberately narrow: only the exact fabricated-pattern class actually
# found ("Rated 5.0 on Google") and schema.org aggregate-rating keys. Does
# NOT match the legitimate per-review "5 out of 5 stars" aria-label or
# visible "★★★★★" glyphs that every real, approved testimonial card uses —
# a broader "N stars"/"N out of 5" pattern would false-positive on those.
RATING_CLAIM_RE = re.compile(
    r"Rated\s+[\d.]+\s+on\s+Google"
    r'|"ratingValue"'
    r'|"reviewCount"'
    r'|"AggregateRating"'
    r'|"aggregateRating"',
    re.I,
)


def check_rating_claims(rel, content, errors):
    for m in RATING_CLAIM_RE.finditer(content):
        snippet = m.group(0)
        if APPROVED_RATING is None:
            errors.append(f"{rel}: unsupported rating/review-count claim found: {snippet!r} (APPROVED_RATING is not set)")
        else:
            errors.append(f"{rel}: rating/review-count claim found: {snippet!r} — verify it matches APPROVED_RATING and update this check if so")


def main() -> int:
    errors: list[str] = []
    for rel, content in real_html_files():
        check_generated_cards(rel, content, errors)
        check_inline_quotes(rel, content, errors)
        check_rating_claims(rel, content, errors)

    if errors:
        print(f"Testimonial/rating integrity check FAILED ({len(errors)} issue(s)):")
        for e in errors:
            print(f"  - {e}")
        return 1

    print(
        f"Testimonial/rating integrity check passed "
        f"({len(TESTIMONIALS)} approved testimonials, APPROVED_RATING={APPROVED_RATING!r})."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
