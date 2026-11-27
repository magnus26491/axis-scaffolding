from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SITE = "https://www.axisscaffoldingessex.co.uk"

AREA_LINKS = {
    "Benfleet": "benfleet",
    "Canvey Island": "canvey-island",
    "Rayleigh": "rayleigh",
    "Southend-on-Sea": "southend",
    "Basildon": "basildon",
    "Chelmsford": "chelmsford",
    "Wickford": "wickford",
    "Hadleigh": "hadleigh",
    "Leigh-on-Sea": "leigh-on-sea",
    "Thundersley": "thundersley",
    "Hockley": "hockley",
    "Rochford": "rochford",
}

OLD_SITE = "https://axisscaffolding.co.uk"

# Only slugs whose legacy flat filename DIFFERS from the canonical folder
# slug belong here. GitHub Pages resolves a request for "/areas/X" by
# checking for a sibling "areas/X.html" file *before* "areas/X/index.html" —
# so a legacy stub named identically to its own target creates a same-URL
# redirect loop that permanently shadows the real page (confirmed live:
# brentwood/loughton/london/basildon/canvey-island/chelmsford/rayleigh/
# southend were all stuck redirecting to themselves until this was fixed).
# clacton/bromley are safe because they redirect to a different path (the
# /areas hub — there is no areas/clacton/ or areas/bromley/ folder).
LEGACY_AREA_TARGETS = {
    "clacton": "/areas",
    "bromley": "/areas",
}

LEGACY_SERVICE_TARGETS = {
    "services/residential.html": "/services/residential-scaffolding",
    "services/commercial.html": "/services/commercial-scaffolding",
    "services/supply-erection.html": "/services/scaffold-supply-erection",
    "services/dismantling.html": "/services/dismantling-scaffolding",
    "services/loading-bays.html": "/services/loading-bay-scaffolding",
    "services/temporary-roofs.html": "/services/temporary-roofing",
    # Domestic merged into Residential & Domestic (one page, one URL).
    "services/domestic-scaffolding/index.html": "/services/residential-scaffolding",
}

# This is the single source of truth for every legacy redirect stub — the
# generated .html files, the _redirects file, and (via normalise_legacy_
# redirect_page's noindex,follow meta) the indexation signal for all of
# them. build_site.py used to also write these with an inferior template
# (no noindex meta) that this script's normalise_legacy_redirect_page()
# only partially overwrote, silently leaving some stubs without the
# noindex directive. build_site.py no longer writes them at all.
#
# about.html/gallery.html/contact.html are deliberately NOT here (see the
# LEGACY_AREA_TARGETS comment above for why): their legacy filename is
# identical to their own canonical target, which on GitHub Pages creates a
# same-URL redirect loop that permanently shadows /about, /gallery and
# /contact — confirmed broken live. privacy.html/terms.html/cookies.html
# are safe because their legacy filename differs from the canonical slug.
LEGACY_TOP_TARGETS = {
    "privacy.html": "/privacy-policy",
    "terms.html": "/terms-and-conditions",
    "cookies.html": "/cookie-policy",
}


# GitHub Pages serves every folder page at "/x/" and 301-redirects "/x" to it.
# Canonical URLs, sitemap URLs and internal links therefore use the trailing-
# slash form, so none of them points at a URL that itself redirects.
_ABS_URL = re.compile(
    r"(" + re.escape(SITE) + r"/[A-Za-z0-9_\-/]*[A-Za-z0-9_\-])(?=[\"'<\s#?,)\\])"
)
_REL_HREF = re.compile(r"(href=[\"'])(/[A-Za-z0-9_\-/]*[A-Za-z0-9_\-])(?=[#?\"'])")


def add_trailing_slashes(text: str) -> str:
    text = _ABS_URL.sub(r"\1/", text)
    return _REL_HREF.sub(r"\1\2/", text)


def clean_metadata(html: str) -> str:
    html = re.sub(r'\s*<meta name="google-site-verification" content="REPLACE_WITH_GSC_CODE">', "", html)
    html = re.sub(r'\s*<meta name="revisit-after" content="30 days">', "", html)
    return html


def fix_area_page(html: str) -> str:
    html = html.replace('href="/#areas-covered"', 'href="/areas"')
    html = html.replace(f'href="{SITE}/#areas-covered"', f'href="{SITE}/areas"')
    return html


def fix_homepage(html: str) -> str:
    for name, slug in AREA_LINKS.items():
        html = html.replace(f'href="/contact">{name}</a>', f'href="/areas/{slug}">{name}</a>')
    return html


def _slash(target: str) -> str:
    return target if target.endswith("/") else target + "/"


def normalise_legacy_redirect_page(path: Path, target: str) -> None:
    target = _slash(target)
    target_url = SITE + target
    html = f'''<!doctype html>
<html lang="en-GB">
<head>
  <meta charset="utf-8">
  <meta http-equiv="refresh" content="0;url={target}">
  <link rel="canonical" href="{target_url}">
  <meta name="robots" content="noindex,follow">
  <title>Redirecting to Axis Scaffolding</title>
</head>
<body>
  <p>Redirecting to <a href="{target}">{target}</a></p>
  <script>window.location.replace({target!r});</script>
</body>
</html>
'''
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(html, encoding="utf-8")


def write_redirects() -> None:
    lines = [
        f"{OLD_SITE}/* {SITE}/:splat 301!",
        f"https://www.axisscaffolding.co.uk/* {SITE}/:splat 301!",
    ]
    lines.extend(f"/{src} {_slash(target)} 301" for src, target in LEGACY_TOP_TARGETS.items())
    lines.extend(
        f"/{src.removesuffix('/index.html')} {_slash(target)} 301" for src, target in LEGACY_SERVICE_TARGETS.items()
    )
    lines.extend(
        f"/areas/{slug}.html {_slash(target)} 301"
        for slug, target in LEGACY_AREA_TARGETS.items()
    )
    (ROOT / "_redirects").write_text("\n".join(lines) + "\n", encoding="utf-8")


def _page_lastmod(url: str) -> str:
    """Date the page's HTML last changed: today if the working copy differs from the last
    commit (or is new), otherwise the date of the last commit that touched it. Runs after
    the build and the normalisation above, so an unchanged page keeps its old date."""
    import datetime
    import subprocess
    rel = url.removeprefix(SITE).strip("/")
    rel = f"{rel}/index.html" if rel else "index.html"
    if not (ROOT / rel).exists():
        return ""
    def git(*args: str) -> subprocess.CompletedProcess:
        return subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True, timeout=30)
    tracked = git("ls-files", "--error-unmatch", "--", rel).returncode == 0
    if not tracked or git("diff", "--quiet", "HEAD", "--", rel).returncode != 0:
        return datetime.date.today().isoformat()
    return git("log", "-1", "--format=%cs", "--", rel).stdout.strip()


def update_sitemap() -> None:
    path = ROOT / "sitemap.xml"
    if not path.exists():
        return
    xml = add_trailing_slashes(path.read_text(encoding="utf-8"))

    def refresh(match: re.Match) -> str:
        block = match.group(0)
        loc = re.search(r"<loc>(.*?)</loc>", block).group(1)
        lastmod = _page_lastmod(loc)
        block = re.sub(r"<lastmod>.*?</lastmod>", "", block)
        if lastmod:
            block = block.replace("</loc>", f"</loc><lastmod>{lastmod}</lastmod>", 1)
        return block

    xml = re.sub(r"<url>.*?</url>", refresh, xml)
    path.write_text(xml, encoding="utf-8")


def main() -> None:
    for html_path in ROOT.rglob("*.html"):
        if any(part in {".git", "node_modules"} for part in html_path.parts):
            continue
        html = html_path.read_text(encoding="utf-8", errors="ignore")
        html = clean_metadata(html)
        if html_path == ROOT / "index.html":
            html = fix_homepage(html)
        if len(html_path.parts) >= 3 and html_path.parts[-3] == "areas" and html_path.name == "index.html":
            html = fix_area_page(html)
        html = add_trailing_slashes(html)
        html_path.write_text(html, encoding="utf-8")

    llms = ROOT / "llms.txt"
    if llms.exists():
        llms.write_text(add_trailing_slashes(llms.read_text(encoding="utf-8")), encoding="utf-8")

    for slug, target in LEGACY_AREA_TARGETS.items():
        normalise_legacy_redirect_page(ROOT / "areas" / f"{slug}.html", target)

    for source, target in LEGACY_SERVICE_TARGETS.items():
        normalise_legacy_redirect_page(ROOT / source, target)

    for source, target in LEGACY_TOP_TARGETS.items():
        normalise_legacy_redirect_page(ROOT / source, target)

    write_redirects()
    update_sitemap()
    print("SEO post-processing completed.")


if __name__ == "__main__":
    main()
