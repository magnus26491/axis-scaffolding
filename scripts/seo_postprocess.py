from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SITE = "https://axisscaffoldingessex.co.uk"

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

LEGACY_AREA_TARGETS = {
    "brentwood": "/areas/brentwood",
    "loughton": "/areas/loughton",
    "london": "/areas/london",
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
}


def clean_metadata(html: str) -> str:
    html = re.sub(r'\s*<meta name="google-site-verification" content="REPLACE_WITH_GSC_CODE">', "", html)
    html = re.sub(r'\s*<meta name="revisit-after" content="30 days">', "", html)
    return html


def fix_area_page(html: str) -> str:
    # The parent breadcrumb must resolve to a real Areas page, not a homepage fragment.
    html = html.replace('href="/#areas-covered"', 'href="/areas"')
    html = html.replace(f'href="{SITE}/#areas-covered"', f'href="{SITE}/areas"')
    return html


def fix_homepage(html: str) -> str:
    # Turn the area pills into genuine internal links instead of sending every visitor to Contact.
    for name, slug in AREA_LINKS.items():
        html = html.replace(f'href="/contact">{name}</a>', f'href="/areas/{slug}">{name}</a>')
    return html


def normalise_legacy_area_page(path: Path, target: str) -> None:
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


def normalise_legacy_service_file(path: Path, target: str) -> None:
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
        f"https://axisscaffolding.co.uk/* {SITE}/:splat 301!",
        f"https://www.axisscaffolding.co.uk/* {SITE}/:splat 301!",
        "/about.html /about 301",
        "/gallery.html /gallery 301",
        "/contact.html /contact 301",
        "/privacy.html /privacy-policy 301",
        "/terms.html /terms-and-conditions 301",
        "/cookies.html /cookie-policy 301",
    ]
    lines.extend(f"/{src} {target} 301" for src, target in LEGACY_SERVICE_TARGETS.items())
    lines.extend([
        "/areas/clacton /areas 301",
        "/areas/bromley /areas 301",
    ])
    (ROOT / "_redirects").write_text("\n".join(lines) + "\n", encoding="utf-8")


def update_sitemap() -> None:
    path = ROOT / "sitemap.xml"
    if not path.exists():
        return
    xml = path.read_text(encoding="utf-8")
    # Keep the generator's deliberate non-trailing-slash canonical strategy consistent.
    xml = re.sub(r"(<loc>" + re.escape(SITE) + r"/[^<]*?)/</loc>", r"\1</loc>", xml)
    xml = xml.replace("<loc>" + SITE + "/</loc>", "<loc>" + SITE + "/</loc>")

    existing = set(re.findall(r"<loc>(.*?)</loc>", xml))
    additions = []
    for slug in ("brentwood", "loughton", "london"):
        url = f"{SITE}/areas/{slug}"
        if url not in existing and (ROOT / "areas" / slug / "index.html").exists():
            additions.append(
                f"  <url><loc>{url}</loc><lastmod>2026-08-26</lastmod><changefreq>monthly</changefreq><priority>0.7</priority></url>"
            )
    if additions:
        xml = xml.replace("</urlset>", "\n" + "\n".join(additions) + "\n</urlset>")
    path.write_text(xml, encoding="utf-8")


def main() -> None:
    for html_path in ROOT.rglob("*.html"):
        # Do not alter generated third-party/vendor files if any are added later.
        if any(part in {".git", "node_modules"} for part in html_path.parts):
            continue
        html = html_path.read_text(encoding="utf-8", errors="ignore")
        html = clean_metadata(html)
        if html_path == ROOT / "index.html":
            html = fix_homepage(html)
        if html_path.parts[-2:-1] == ("areas",):
            html = fix_area_page(html)
        html_path.write_text(html, encoding="utf-8")

    for slug, target in LEGACY_AREA_TARGETS.items():
        normalise_legacy_area_page(ROOT / "areas" / f"{slug}.html", target)

    for source, target in LEGACY_SERVICE_TARGETS.items():
        normalise_legacy_service_file(ROOT / source, target)

    write_redirects()
    update_sitemap()
    print("SEO post-processing completed.")


if __name__ == "__main__":
    main()
