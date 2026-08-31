from __future__ import annotations

import json
from datetime import date
from pathlib import Path
from typing import Iterable

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).parent
SITE = "https://www.axisscaffoldingessex.co.uk"
# Bare (non-www) new-domain hostname. GitHub Pages (see CNAME) redirects this
# to SITE automatically at the edge — no application code needed for that
# hop. Kept only for the duplicate-host audit / CI checks below; never used
# to build an outgoing URL.
BARE_SITE = "https://axisscaffoldingessex.co.uk"
OLD_SITE = "https://axisscaffolding.co.uk"
OG_IMAGE_URL = f"{SITE}/public/og-image.jpg"
TODAY = date.today().isoformat()
CONTACT_EMAIL = 'axis-scaffolding@outlook.com'
FORM_ACTION = 'https://formsubmit.co/axis-scaffolding@outlook.com'
FORM_NEXT = 'https://www.axisscaffoldingessex.co.uk/thank-you'
# No verified GA4 property exists for this site yet. Leave unset (None) until a real
# measurement ID is provided — do not hard-code a placeholder or invented ID here.
# When set (e.g. "G-XXXXXXX"), analytics load only after the visitor grants consent.
GA4_MEASUREMENT_ID: str | None = None

NAP = {
    "name": "Axis Scaffolding Ltd",
    "address": "Arterial Road, Rayleigh, Essex, SS6 7XT",
    "phone": "01702 820468",
    "phone_e164": "+441702820468",
    "email": CONTACT_EMAIL,
    "company_no": "15050136",
}

FAQS = [
    (
        "How much does scaffolding cost in Essex?",
        "Residential scaffolding in Essex typically starts from around £300–£500 for smaller access jobs, rising to £1,500 or more for full roof scaffolds on larger properties. The final price depends on scaffold size, height, number of elevations, site access, duration and whether a highway licence is required. We provide clear, itemised quotations — call 01702 820468 or use the quote form for a no-obligation price.",
    ),
    (
        "How quickly can scaffolding be erected?",
        "Most standard South Essex domestic and commercial jobs are scheduled within 2–5 working days once a quote is approved. Emergency scaffolding for urgent structural or storm-damage situations is prioritised — call 01702 820468 directly for urgent access requirements.",
    ),
    (
        "Are you CISRS certified scaffolders?",
        "Yes. Axis Scaffolding Ltd is a fully qualified, CISRS-certified scaffolding company. CISRS (Construction Industry Scaffolders Record Scheme) is the industry standard qualification for scaffolders in the UK, demonstrating that our operatives are trained and assessed to national standards.",
    ),
    (
        "Do you need a licence to erect scaffolding on a pavement or road?",
        "Yes. Scaffolding that overhangs or occupies a public highway — including pavements — requires a licence under Section 169 of the Highways Act 1980. Axis Scaffolding can advise on the licence process and coordinate with the local authority on your behalf. Licence fees and timescales vary by area.",
    ),
    (
        "Do you cover residential and commercial scaffolding in Essex?",
        "Yes. We provide domestic and residential scaffolding for homeowners, roof scaffolding for roofers and contractors, and commercial scaffolding for builders, developers and property managers. We also provide temporary roofing and emergency access across South Essex.",
    ),
    (
        "What is the difference between residential and domestic scaffolding?",
        "At Axis Scaffolding, residential scaffolding typically refers to larger home projects — extensions, full roof replacements, multi-storey properties — while domestic scaffolding covers shorter-term access for occupied homes undertaking repairs, painting or chimney work. Both are handled by the same CISRS-qualified team. If you're unsure which applies, just describe your job and we'll advise.",
    ),
    (
        "Will scaffolding damage my driveway or garden?",
        "We take care to protect driveways, gardens and render when erecting scaffold. Base plates and boards are used to spread load and minimise ground contact. If you have a particular concern about your driveway surface or a specific access constraint, mention it when you request your quote so we can plan accordingly.",
    ),
    (
        "What areas do you cover in Essex?",
        "We are based in Rayleigh and regularly provide scaffolding in Benfleet, Canvey Island, Southend-on-Sea, Basildon, Chelmsford, Wickford, Hadleigh, Leigh-on-Sea, Thundersley, Hockley and Rochford. Contact us to confirm coverage for your specific location.",
    ),
]

SERVICES = [
    {
        "slug": "residential-scaffolding",
        "name": "Residential Scaffolding",
        "title": "Residential Scaffolding Essex | Axis Scaffolding Ltd",
        "desc": "Residential scaffolding in Essex for extensions, roof replacements and exterior works. CISRS-qualified team based in Rayleigh. Free quotes — call 01702 820468.",
        "summary": "Safe, tidy scaffold systems for extensions, full roof replacements, rendering and exterior home improvements across South Essex.",
        "who_for": "Homeowners undertaking extensions, roof replacements, chimney repairs, rendering and other major exterior works.",
    },
    {
        "slug": "commercial-scaffolding",
        "name": "Commercial Scaffolding",
        "title": "Commercial Scaffolding Essex | Axis Scaffolding Ltd",
        "desc": "Commercial scaffolding in Essex for builders, developers and contractors. RAMS available. CISRS-qualified team in Rayleigh. Call 01702 820468 for a fast quote.",
        "summary": "Planned scaffold packages for builders, contractors, offices, retail units, schools and commercial developments across Essex.",
        "who_for": "Builders, developers, principal contractors, property managers and commercial premises requiring planned scaffold access.",
    },
    {
        "slug": "domestic-scaffolding",
        "name": "Domestic Scaffolding",
        "title": "Domestic Scaffolding Essex | Axis Scaffolding Ltd",
        "desc": "Domestic scaffolding in Essex for occupied homes, repairs and short-term access. CISRS-qualified team in Rayleigh, South Essex. Free quotes — call 01702 820468.",
        "summary": "Short-term scaffold access for occupied homes needing repairs, painting, chimney work or maintenance across South Essex.",
        "who_for": "Homeowners requiring shorter-term scaffold access for repairs, maintenance, painting or chimney work on occupied properties.",
    },
    {
        "slug": "roof-scaffolding",
        "name": "Roof Scaffolding",
        "title": "Roof Scaffolding Essex | Axis Scaffolding Ltd",
        "desc": "Roof scaffolding in Essex for roofers, chimney repairs and roofline works. CISRS-qualified. Based in Rayleigh. Free quote — call 01702 820468.",
        "summary": "Specialist roof-level scaffold systems for chimney repairs, guttering, fascias and full roof replacements across South Essex.",
        "who_for": "Homeowners and roofing contractors needing safe, compliant roof access for repairs, replacement, chimneys or guttering.",
    },
    {
        "slug": "temporary-roofing",
        "name": "Temporary Roofing",
        "title": "Temporary Roofing Essex | Axis Scaffolding Ltd",
        "desc": "Temporary roofing in Essex to protect live projects from weather. Scaffold-supported structures for ongoing roof works. Rayleigh team — call 01702 820468.",
        "summary": "Weather-protected temporary roof structures that keep projects moving year-round, protecting exposed structures during active roof works.",
        "who_for": "Builders, roofers and homeowners needing weather protection over an exposed structure during roof replacement or significant repair work.",
    },
    {
        "slug": "emergency-scaffolding",
        "name": "Emergency Scaffolding",
        "title": "Emergency Scaffolding Essex | Axis Scaffolding Ltd",
        "desc": "Emergency scaffolding in Essex for storm damage, urgent access and safety works. Axis Scaffolding prioritises urgent enquiries — call 01702 820468 now.",
        "summary": "Rapid-response scaffold support for urgent structural issues, storm damage and emergency safety access across South Essex.",
        "who_for": "Anyone facing urgent structural access needs — storm-damaged roofs, emergency repairs, temporary protection after an incident.",
    },
    {
        "slug": "dismantling-scaffolding",
        "name": "Scaffold Dismantling",
        "title": "Scaffold Dismantling Essex | Axis Scaffolding Ltd",
        "desc": "Professional scaffold dismantling in Essex. Safe, efficient removal and tidy handover once your project is complete. Rayleigh team — call 01702 820468.",
        "summary": "Safe, efficient scaffold removal and tidy site handover once works are complete — completing the full scaffold lifecycle.",
        "who_for": "Anyone who needs an existing scaffold removed safely, including scaffolds erected by other companies.",
    },
    {
        "slug": "loading-bay-scaffolding",
        "name": "Loading Bay Scaffolding",
        "title": "Loading Bay Scaffolding Essex | Axis Scaffolding Ltd",
        "desc": "Loading bay scaffolding in Essex for commercial sites and contractors. Structured material access solutions. Rayleigh team — call 01702 820468.",
        "summary": "Scaffold-integrated loading bays for safe materials delivery and handling on commercial and residential construction sites.",
        "who_for": "Builders and contractors on sites requiring safe access for materials delivery, loading and unloading at height.",
    },
    {
        "slug": "scaffold-supply-erection",
        "name": "Scaffold Supply & Erection",
        "title": "Scaffold Supply and Erection Essex | Axis Scaffolding Ltd",
        "desc": "Scaffold supply and erection in Essex. Materials and installation from a single CISRS-qualified team in Rayleigh. Free quote — call 01702 820468.",
        "summary": "Complete scaffold supply and erection from a single contractor — materials, qualified labour and site coordination in one package.",
        "who_for": "Contractors and homeowners who need a complete, managed scaffold solution from a single point of contact.",
    },
]

AREAS = [
    "Benfleet",
    "Canvey Island",
    "Rayleigh",
    "Southend-on-Sea",
    "Basildon",
    "Chelmsford",
    "Wickford",
    "Hadleigh",
    "Leigh-on-Sea",
    "Thundersley",
    "Hockley",
    "Rochford",
]


def ensure_dirs() -> None:
    for rel in [
        "assets/css",
        "assets/js",
        "images",
        "public",
        "services",
        "gallery",
        "about",
        "contact",
        "quote",
        "privacy-policy",
        "terms-and-conditions",
        "cookie-policy",
        "guides",
        "contractors",
    ]:
        (ROOT / rel).mkdir(parents=True, exist_ok=True)


def write(path: str, content: str) -> None:
    target = ROOT / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(content.strip() + "\n", encoding="utf-8")


def local_business_schema() -> dict:
    return {
        "@context": "https://schema.org",
        "@type": "LocalBusiness",
        "@id": f"{SITE}/#business",
        "name": "Axis Scaffolding Ltd",
        "legalName": "AXIS SCAFFOLDING LTD",
        "url": SITE,
        "telephone": NAP["phone"],
        "email": NAP["email"],
        "address": {
            "@type": "PostalAddress",
            "streetAddress": "Arterial Road",
            "addressLocality": "Rayleigh",
            "addressRegion": "Essex",
            "postalCode": "SS6 7XT",
            "addressCountry": "GB",
        },
        "geo": {"@type": "GeoCoordinates", "latitude": 51.5868, "longitude": 0.6044},
        "areaServed": [
            {"@type": "City", "name": "Rayleigh"},
            {"@type": "City", "name": "Benfleet"},
            {"@type": "City", "name": "Canvey Island"},
            {"@type": "City", "name": "Southend-on-Sea"},
            {"@type": "City", "name": "Basildon"},
            {"@type": "City", "name": "Chelmsford"},
            {"@type": "AdministrativeArea", "name": "Essex"},
        ],
        "priceRange": "££",
        "openingHoursSpecification": [
            {
                "@type": "OpeningHoursSpecification",
                "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
                "opens": "07:00",
                "closes": "18:00",
            }
        ],
        "sameAs": [
            "https://www.facebook.com/Axisscaffoldingltd/",
            "https://www.instagram.com/axis_scaffoldingessex/",
        ],
    }


def breadcrumb_schema(items: Iterable[tuple[str, str]]) -> dict:
    return {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": name, "item": SITE + path}
            for i, (name, path) in enumerate(items)
        ],
    }


def faq_schema() -> dict:
    return {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {
                "@type": "Question",
                "name": q,
                "acceptedAnswer": {"@type": "Answer", "text": a},
            }
            for q, a in FAQS
        ],
    }


def head_tags(
    *,
    title: str,
    desc: str,
    path: str,
    breadcrumb_items: list[tuple[str, str]] | None = None,
    include_faq_schema: bool = False,
    preload_hero: bool = False,
) -> str:
    canonical = SITE + path
    schemas = [local_business_schema()]
    if breadcrumb_items:
        schemas.append(breadcrumb_schema(breadcrumb_items))
    if include_faq_schema:
        schemas.append(faq_schema())
    schema_tags = "\n".join(
        f'<script type="application/ld+json">{json.dumps(s, ensure_ascii=False)}</script>'
        for s in schemas
    )
    preload = '<link rel="preload" as="image" href="/images/hero-bg.webp">' if preload_hero else ""
    return f"""
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <meta name="author" content="Axis Scaffolding Ltd">
  <link rel="canonical" href="{canonical}">
  <link rel="alternate" hreflang="en-gb" href="{canonical}">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:image" content="{OG_IMAGE_URL}">
  <meta property="og:url" content="{canonical}">
  <meta property="og:type" content="website">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{title}">
  <meta name="twitter:description" content="{desc}">
  <meta name="twitter:image" content="{OG_IMAGE_URL}">
  <link rel="icon" href="/favicon.ico" sizes="any">
  <link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png">
  <link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Poppins:wght@500;600;700;800&display=swap" rel="stylesheet">
  {preload}
  <link rel="stylesheet" href="/assets/css/style.css">
  {schema_tags}
</head>
"""


def breadcrumb_nav(items: list[tuple[str, str]]) -> str:
    parts = []
    for idx, (name, path) in enumerate(items):
        if idx < len(items) - 1:
            parts.append(f'<a href="{path}">{name}</a>')
        else:
            parts.append(f"<span>{name}</span>")
    return '<nav class="breadcrumbs" aria-label="Breadcrumb">' + ' <span aria-hidden="true">&gt;</span> '.join(parts) + "</nav>"


def nav() -> str:
    return f"""
<header class="site-header" id="site-header">
  <div class="container nav-wrap">
    <a class="logo-wrap" href="/" aria-label="Axis Scaffolding Ltd homepage">
      <span class="logo-circle logo-circle-nav">
        <img src="/images/logo.webp" alt="Axis Scaffolding Ltd logo" width="64" height="64" loading="lazy" decoding="async">
      </span>
    </a>
    <a class="nav-phone-mobile" href="tel:{NAP['phone_e164']}" aria-label="Call Axis Scaffolding">{NAP['phone']}</a>
    <button class="menu-toggle" id="menu-toggle" aria-label="Toggle mobile menu" aria-controls="site-menu" aria-expanded="false">
      <span></span><span></span><span></span>
    </button>
    <nav class="site-nav" id="site-menu" aria-label="Primary navigation">
      <a href="/">Home</a>
      <a href="/services">Services</a>
      <a href="/contractors">For Builders</a>
      <a href="/gallery">Projects</a>
      <a href="/about">About</a>
      <a href="/contact">Contact</a>
      <a class="nav-phone-desktop" href="tel:{NAP['phone_e164']}">{NAP['phone']}</a>
      <a class="cta-pill" href="/quote">Get a Free Quote</a>
    </nav>
  </div>
</header>
"""


def footer() -> str:
    svc = "".join(f'<li><a href="/services/{s["slug"]}">{s["name"]}</a></li>' for s in SERVICES)
    area = "".join(f"<li>{a}</li>" for a in AREAS[:8])
    return f"""
<footer class="site-footer">
  <div class="container footer-grid">
    <section>
      <h2>Brand</h2>
      <span class="logo-circle logo-circle-footer">
        <img src="/images/logo.webp" alt="Axis Scaffolding Ltd logo" width="80" height="80" loading="lazy" decoding="async">
      </span>
      <p>Reliable scaffolding across Essex.</p>
      <div class="footer-social-links">
        <a href="https://www.facebook.com/Axisscaffoldingltd/" target="_blank" rel="noopener noreferrer" class="footer-social-link" aria-label="Follow Axis Scaffolding on Facebook">
          <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M22 12.06C22 6.5 17.52 2 12 2S2 6.5 2 12.06c0 5.02 3.66 9.18 8.44 9.94v-7.03H7.9v-2.9h2.54V9.84c0-2.52 1.49-3.92 3.77-3.92 1.09 0 2.23.2 2.23.2v2.47h-1.25c-1.24 0-1.62.77-1.62 1.56v1.87h2.75l-.44 2.9h-2.31V22c4.78-.76 8.44-4.92 8.44-9.94Z"/></svg>
        </a>
        <a href="https://www.instagram.com/axis_scaffoldingessex/" target="_blank" rel="noopener noreferrer" class="footer-social-link" aria-label="Follow Axis Scaffolding on Instagram">
          <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M7.75 2h8.5A5.76 5.76 0 0 1 22 7.75v8.5A5.76 5.76 0 0 1 16.25 22h-8.5A5.76 5.76 0 0 1 2 16.25v-8.5A5.76 5.76 0 0 1 7.75 2Zm0 1.8A3.95 3.95 0 0 0 3.8 7.75v8.5a3.95 3.95 0 0 0 3.95 3.95h8.5a3.95 3.95 0 0 0 3.95-3.95v-8.5a3.95 3.95 0 0 0-3.95-3.95h-8.5Zm8.9 1.35a1.2 1.2 0 1 1 0 2.4 1.2 1.2 0 0 1 0-2.4ZM12 7a5 5 0 1 1 0 10 5 5 0 0 1 0-10Zm0 1.8A3.2 3.2 0 1 0 12 15.2 3.2 3.2 0 0 0 12 8.8Z"/></svg>
        </a>
        <a href="https://maps.google.com/?q=Arterial+Road+Rayleigh+Essex+SS6+7XT" target="_blank" rel="noopener noreferrer" class="footer-social-link" aria-label="Find Axis Scaffolding on Google">
          <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2a7 7 0 0 1 7 7c0 5.03-7 13-7 13S5 14.03 5 9a7 7 0 0 1 7-7Zm0 3.1A3.9 3.9 0 1 0 12 12.9 3.9 3.9 0 0 0 12 5.1Z"/></svg>
        </a>
      </div>
    </section>
    <section><h2>Our Services</h2><ul>{svc}</ul></section>
    <section><h2>Areas We Cover</h2><ul>{area}</ul></section>
    <section>
      <h2>Contact Us</h2>
      <p>{NAP["name"]}</p>
      <p><a href="tel:{NAP["phone_e164"]}">{NAP["phone"]}</a></p>
      <p><a href="mailto:{NAP["email"]}">{NAP["email"]}</a></p>
      <p>{NAP["address"]}</p>
      <p>Company No: {NAP["company_no"]}</p>
      <p style="margin-top:0.5rem; font-size:0.85rem;">Mon–Fri 07:00–18:00</p>
    </section>
  </div>
  <div class="container footer-bottom">
    <hr>
    <p>AXIS SCAFFOLDING LTD is registered as a limited company in England and Wales under Company Number: 15050136.</p>
    <p>Registered Company Address: Arterial Road, Rayleigh, England, SS6 7XT</p>
    <p>© 2026. The content on this website is owned by us and our licensors. Do not copy any content (including images) without our consent.</p>
    <div class="footer-legal-links">
      <button id="axis-footer-cookie-btn" style="background:none; border:none; color:#6b7280; font-size:0.8rem; cursor:pointer; text-decoration:underline; padding:0;">Cookie Settings</button>
      <a href="/privacy-policy">Privacy Policy</a>
      <a href="/terms-and-conditions">Terms &amp; Conditions</a>
    </div>
  </div>
</footer>
"""


def cookie_ui() -> str:
    return """
<div id="axis-cookie-bar" class="cookie-bar">
  <p>
    We use cookies to improve your experience and analyse site traffic.
    By clicking <strong>Accept All</strong> you consent
    to our use of cookies.
    <a href="/privacy-policy">Read our Privacy Policy</a>
  </p>
  <div class="cookie-bar-actions">
    <button id="axis-cookie-accept" class="btn btn-primary">Accept All</button>
    <button id="axis-cookie-reject" class="btn btn-outline">Reject Non-Essential</button>
    <button id="axis-cookie-manage" class="btn-manage">Manage Preferences</button>
  </div>
</div>
"""


def moved_site_banner() -> str:
    return """
<div id="domain-move-banner" class="domain-move-banner" hidden>
  We've moved! Visit us at
  <a href="https://www.axisscaffoldingessex.co.uk" rel="canonical">www.axisscaffoldingessex.co.uk</a>
</div>
"""


def faq_accordion() -> str:
    parts = []
    for idx, (q, a) in enumerate(FAQS):
        parts.append(
            f"""
<div class="faq-item">
  <button class="faq-question" id="faq-button-{idx}" aria-expanded="{'true' if idx == 0 else 'false'}" aria-controls="faq-panel-{idx}">{q}</button>
  <div class="faq-answer" id="faq-panel-{idx}" role="region" aria-labelledby="faq-button-{idx}" {'style="display:block;"' if idx == 0 else ''}>
    <p>{a}</p>
  </div>
</div>
"""
        )
    return "".join(parts)


def quote_form(prefix: str, title: str) -> str:
    return f"""
<section class="quote-form-card">
  <h3>{title}</h3>
  <form class="axis-quote-form" data-form-name="{prefix}" action="{FORM_ACTION}" method="POST">
    <input type="hidden" name="_subject" value="New Scaffolding Quote Request — Axis Scaffolding Ltd">
    <input type="hidden" name="_replyto" value="{CONTACT_EMAIL}">
    <input type="hidden" name="_next" value="{FORM_NEXT}">
    <input type="hidden" name="_captcha" value="false">
    <input type="text" name="_honey" style="display:none" tabindex="-1" autocomplete="off">
    <p><label for="{prefix}-name">Full Name *</label><input id="{prefix}-name" name="fullName" autocomplete="name" required></p>
    <p><label for="{prefix}-phone">Phone Number *</label><input id="{prefix}-phone" name="phone" type="tel" autocomplete="tel" required></p>
    <p><label for="{prefix}-email">Email Address *</label><input id="{prefix}-email" name="email" type="email" autocomplete="email" required></p>
    <p><label for="{prefix}-postcode">Postcode *</label><input id="{prefix}-postcode" name="postcode" autocomplete="postal-code" required></p>
    <p><label for="{prefix}-type">Type of Scaffolding *</label>
      <select id="{prefix}-type" name="scaffoldingType" required>
        <option value="">Please select</option>
        <option>Residential — home extension, roof, rendering</option>
        <option>Commercial — site, office, retail, development</option>
        <option>Roof scaffolding — roofer access</option>
        <option>Temporary roofing</option>
        <option>Emergency</option>
        <option>Not sure — describe below</option>
      </select>
    </p>
    <p><label for="{prefix}-brief">Brief Description of Work *</label><textarea id="{prefix}-brief" name="briefDescription" required placeholder="e.g. Full roof replacement on a 3-bed semi in Rayleigh. Need scaffold for 2 weeks."></textarea></p>
    <p><label for="{prefix}-source">How did you hear about us?</label>
      <select id="{prefix}-source" name="source">
        <option value="">Please select</option><option>Google Search</option><option>Google Maps</option><option>Facebook</option><option>Instagram</option><option>Word of Mouth</option><option>Bark.com</option><option>Other</option>
      </select>
    </p>
    <button type="submit" class="btn btn-primary btn-full">Get My Free Quote</button>
    <p class="form-note" style="font-size:0.82rem; color:#6b7280; margin-top:0.5rem;">We aim to respond within one working day. For urgent enquiries call <a href="tel:{NAP['phone_e164']}">{NAP['phone']}</a>.</p>
    <p class="form-message" aria-live="polite"></p>
  </form>
</section>
"""


def render_page(
    *,
    title: str,
    desc: str,
    path: str,
    body: str,
    breadcrumb_items: list[tuple[str, str]] | None = None,
    include_faq_schema: bool = False,
    preload_hero: bool = False,
) -> str:
    return f"""<!doctype html>
<html lang="en-GB">
{head_tags(title=title, desc=desc, path=path, breadcrumb_items=breadcrumb_items, include_faq_schema=include_faq_schema, preload_hero=preload_hero)}
<body>
  <div id="mouse-glow" aria-hidden="true"></div>
  <a href="#main-content" class="sr-only focus:not-sr-only">Skip to main content</a>
  {nav()}
  {moved_site_banner()}
  <main id="main-content">{body}</main>
  {footer()}
  {cookie_ui()}
  <script>window.AXIS_GA4_ID = {json.dumps(GA4_MEASUREMENT_ID)};</script>
  <script src="/assets/js/main.js" defer></script>
</body>
</html>
"""


def generate_media_assets() -> None:
    src_logo = ROOT / "assets/images/logo.png"
    if not src_logo.exists():
        raise FileNotFoundError("Missing assets/images/logo.png")

    with Image.open(src_logo) as logo_img:
        logo_rgb = logo_img.convert("RGB")
        logo_rgb.save(ROOT / "images/logo.webp", format="WEBP", quality=90)
        logo_rgb.save(ROOT / "favicon.ico", sizes=[(16, 16), (32, 32), (48, 48)])
        logo_rgb.resize((32, 32)).save(ROOT / "favicon-32x32.png", format="PNG")
        logo_rgb.resize((180, 180)).save(ROOT / "apple-touch-icon.png", format="PNG")

    for idx in range(1, 8):
        src = ROOT / f"assets/images/job{idx}.jpg"
        if src.exists():
            with Image.open(src) as im:
                im.convert("RGB").save(ROOT / f"images/project-{idx}.webp", format="WEBP", quality=85)

    hero_src = ROOT / "assets/images/job1.jpg"
    if hero_src.exists():
        with Image.open(hero_src) as im:
            rgb = im.convert("RGB")
            orig_w, orig_h = rgb.size
            # Cap the largest variant at 1920w — the widest size any srcset entry
            # below claims. Previously hero-bg.webp was saved at the source image's
            # full native resolution (several thousand px, ~3.8MB) but declared as
            # "1920w" in the srcset, so a matching browser downloaded the full
            # multi-megabyte original believing it was ~1920px wide.
            HERO_MAX_W = 1920
            if orig_w > HERO_MAX_W:
                base_h = round(orig_h * HERO_MAX_W / orig_w)
                rgb = rgb.resize((HERO_MAX_W, base_h), Image.LANCZOS)
                orig_w, orig_h = rgb.size
            rgb.save(ROOT / "images/hero-bg.webp", format="WEBP", quality=85)
            for w in (480, 768, 1024, 1440):
                if orig_w >= w:
                    h = round(orig_h * w / orig_w)
                    rgb.resize((w, h), Image.LANCZOS).save(
                        ROOT / f"images/hero-bg-{w}w.webp", format="WEBP", quality=85
                    )

    for idx in range(8, 15):
        src = ROOT / f"assets/images/gallery-project-{idx}.jpg"
        if src.exists():
            with Image.open(src) as im:
                im.convert("RGB").save(ROOT / f"images/gallery-project-{idx}.webp", format="WEBP", quality=85)

    og = Image.new("RGB", (1200, 630), "#0d0d0d")
    draw = ImageDraw.Draw(og)
    with Image.open(src_logo) as logo:
        logo = logo.convert("RGB").resize((220, 220))
        mask = Image.new("L", (220, 220), 0)
        mask_draw = ImageDraw.Draw(mask)
        mask_draw.ellipse((0, 0, 219, 219), fill=255)
        og.paste(logo, (490, 120), mask)
        draw.ellipse((488, 118, 712, 342), outline="#c8cdd4", width=4)
    try:
        title_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 58)
        subtitle_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 36)
    except OSError:
        title_font = ImageFont.load_default()
        subtitle_font = ImageFont.load_default()
    draw.text((278, 388), "Axis Scaffolding Essex", fill="white", font=title_font)
    draw.text((282, 468), "Reliable Scaffolding Across Essex", fill="white", font=subtitle_font)
    og.save(ROOT / "public/og-image.jpg", format="JPEG", quality=92)


def generate_css() -> None:
    css = """
:root {
  --bg-base:          #000000;
  --bg-depth:         #0a0a0a;
  --glass-bg:         rgba(255, 255, 255, 0.05);
  --glass-border:     rgba(255, 255, 255, 0.12);
  --accent:           #c8cdd4;
  --accent-light:     #e8eaed;
  --accent-dark:      #8e949c;
  --accent-hover:     #b0b7bf;
  --accent-glow:      rgba(200, 205, 212, 0.12);
  --accent-gradient:  linear-gradient(135deg,
                        #e8eaed 0%,
                        #9ba3ab 40%,
                        #c8cdd4 60%,
                        #e2e5e8 100%);
  --text-primary:     #ffffff;
  --text-body:        #e5e7eb;
  --text-muted:       #9ca3af;
  --border-subtle:    rgba(255, 255, 255, 0.08);
  --border-glass:     rgba(255, 255, 255, 0.14);

  /* V2 semantic tokens — additive aliases over the palette above.
     Existing component CSS keeps using the names above unchanged;
     new V2 components (hex system, parallax hero) use these. */
  --bg:            var(--bg-base);
  --surface:       var(--bg-depth);
  --surface-2:     #151515;
  --surface-3:     #1c1c1c;
  --text:          var(--text-primary);
  --text-secondary: var(--text-body);
  --silver:        var(--accent);
  --silver-dark:   var(--accent-dark);
  --silver-light:  var(--accent-light);
  --border:        var(--border-subtle);
  --border-strong: var(--border-glass);

  /* V2.1 spacing scale — the deliberate rhythm tokens the layout/
     alignment audit introduces. Mapped onto values already in use
     across the stylesheet (not invented numbers), so applying them
     doesn't shift anything visually — it just gives the repeated,
     structural values (section rhythm, grid gaps) a shared name
     instead of being restated as literals everywhere. */
  --space-3xs: 0.25rem;
  --space-2xs: 0.5rem;
  --space-xs:  0.75rem;
  --space-sm:  1rem;
  --space-md:  1.5rem;
  --space-lg:  2rem;
  --space-xl:  3rem;
  --space-2xl: 4.5rem;
  --space-3xl: 6rem;

  /* V2 Phase 2 — spacing and type scale. Used by the refined nav, card,
     trust-rail and cookie-banner components below; existing components
     keep their original hand-tuned values untouched. Independent, named
     differently, from the --space-3xs..3xl scale above — both are kept,
     each still has real consumers. */
  --space-1: 0.25rem; --space-2: 0.5rem;  --space-3: 0.75rem;
  --space-4: 1rem;    --space-5: 1.25rem; --space-6: 1.5rem;
  --space-8: 2rem;    --space-10: 2.5rem; --space-12: 3rem;
  --text-xs: 0.8125rem; --text-sm: 0.875rem; --text-base: 1rem;
  --text-lg: 1.125rem;  --text-xl: 1.25rem; --text-2xl: 1.5rem;
}

*, *::before, *::after { box-sizing: border-box; }

html, body {
  margin: 0; padding: 0;
  background-color: #000000 !important;
  color: #d1d5db;
  font-family: 'Inter', system-ui, sans-serif;
  line-height: 1.6;
  overflow-x: hidden;
}

.skip-link {
  position: absolute; top: auto; left: -9999px; z-index: 9999;
  padding: 0.75rem 1.25rem; background: #000; color: #fff;
  font-size: 1rem; font-weight: 600; text-decoration: none;
  border-radius: 0 0 4px 0; transition: left 0s;
}
.skip-link:focus { left: 0; top: 0; }

h1,h2,h3,h4,h5,h6 {
  font-family: 'Poppins','Inter',sans-serif;
  color: #ffffff; margin: 0 0 1rem; line-height: 1.2;
  letter-spacing: -0.01em;
}
/* Deliberate type scale — previously every heading below h1 fell back to
   the browser's UA default size, so hierarchy was accidental rather than
   designed. */
h1 { font-size: clamp(2.25rem, 4.5vw, 3.25rem); font-weight: 700; }
h2 { font-size: clamp(1.65rem, 3vw, 2.15rem); font-weight: 700; }
h3 { font-size: 1.2rem; font-weight: 600; letter-spacing: -0.005em; }
h4 { font-size: 1.05rem; font-weight: 600; letter-spacing: 0; }
p { margin: 0 0 1rem; color: #e5e7eb; }
li, td { color: #e5e7eb; }
small, .muted { color: #9ca3af; }
a { color: inherit; }
img { max-width: 100%; display: block; }
.container { width: min(1160px, calc(100% - 2rem)); margin: 0 auto; }

/* ── MOUSE GLOW ── */
#mouse-glow {
  position: fixed; top: 0; left: 0;
  width: 240px; height: 240px; border-radius: 50%;
  background: radial-gradient(circle,
    rgba(255,255,255,0.09) 0%,
    rgba(255,255,255,0.04) 35%,
    rgba(255,255,255,0.01) 60%,
    transparent 75%);
  pointer-events: none; z-index: 9998;
  transform: translate(-50%, -50%);
  transition: opacity 0.3s ease; will-change: left, top;
}
@media (hover: none), (max-width: 768px) {
  #mouse-glow { display: none !important; }
}

/* ── ACCESSIBILITY ── */
.sr-only {
  position:absolute; width:1px; height:1px;
  padding:0; margin:-1px; overflow:hidden;
  clip:rect(0,0,0,0); border:0;
}
.focus\\:not-sr-only:focus {
  position:fixed; left:1rem; top:1rem;
  width:auto; height:auto; clip:auto; margin:0;
  padding:0.6rem 1rem; background:#fff; color:#000;
  z-index:3000; border-radius:0.5rem;
}
a:focus-visible,button:focus-visible,
input:focus-visible,select:focus-visible,
textarea:focus-visible {
  outline:3px solid var(--accent); outline-offset:2px;
}

/* ── NAVBAR ── */
.site-header {
  position: sticky; top: 0; z-index: 1000;
  background: rgba(0,0,0,0.5) !important;
  backdrop-filter: blur(20px) saturate(180%);
  -webkit-backdrop-filter: blur(20px) saturate(180%);
  border-bottom: 1px solid rgba(255,255,255,0.07);
  transition: background 0.3s ease, box-shadow 0.3s ease;
}
.site-header.scrolled {
  background: rgba(0,0,0,0.92) !important;
  box-shadow: 0 4px 24px rgba(0,0,0,0.6);
}
.nav-wrap {
  display: grid; grid-template-columns: auto 1fr auto;
  align-items: center; gap: 1rem; min-height: 88px;
}
.logo-circle {
  border-radius: 50%; overflow: hidden;
  display: inline-flex; align-items: center;
  justify-content: center; background: #ffffff;
}
.logo-circle-nav {
  width:64px; height:64px;
  border: 2px solid rgba(255,255,255,0.25); padding: 6px;
}
.logo-circle-footer {
  width:80px; height:80px;
  border: 2px solid rgba(255,255,255,0.2); padding: 8px;
}
.logo-circle img {
  width:100%; height:100%;
  object-fit: contain !important; object-position: center;
}
.site-nav {
  display:flex; justify-content:center;
  align-items:center; gap:1.2rem;
}
.site-nav a:not(.cta-pill) {
  position:relative; text-decoration:none; color:#ffffff;
  font-weight:600; font-size:var(--text-sm); transition:color 0.2s;
  padding-bottom:2px;
}
.site-nav a:not(.cta-pill)::after {
  content:''; position:absolute; left:0; right:100%; bottom:0;
  height:1px; background:var(--silver);
  transition:right 0.2s ease;
}
.site-nav a:not(.cta-pill):hover { color: #c8cdd4; }
.site-nav a:not(.cta-pill):hover::after,
.site-nav a:not(.cta-pill):focus-visible::after { right:0; }
.menu-toggle {
  display:none; width:48px; height:48px;
  border:1px solid rgba(255,255,255,0.4);
  background:rgba(255,255,255,0.1);
  border-radius:0.6rem;
  align-items:center; justify-content:center;
  gap:0.25rem; flex-direction:column; cursor: pointer;
}
.menu-toggle span { width:22px; height:2px; background:#fff; }

/* Nav phone links */
.nav-phone-desktop { font-weight:600; color:#c8cdd4 !important; font-size:0.95rem; }
.nav-phone-mobile { display:none; font-weight:700; color:#c8cdd4; font-size:0.85rem; text-decoration:none; }

/* ── BUTTONS ── */
.btn {
  text-decoration:none; border-radius:9999px;
  padding:0.75rem 1.25rem; font-weight:600;
  display:inline-flex; align-items:center;
  justify-content:center; border:2px solid transparent;
  cursor:pointer; transition: all 0.2s ease;
}
.btn-primary,
.cta-pill {
  position:relative; overflow:hidden;
  background: linear-gradient(135deg, #e8eaed 0%, #9ba3ab 40%, #c8cdd4 60%, #e2e5e8 100%) !important;
  color: #000000 !important; font-weight: 700 !important; border: none !important;
  box-shadow: inset 0 1px 0 rgba(255,255,255,0.4), 0 4px 15px rgba(200,205,212,0.15) !important;
}
.btn-primary::before,
.cta-pill::before {
  content:''; position:absolute; top:0; bottom:0; left:-60%; width:40%;
  background:linear-gradient(115deg, transparent, rgba(255,255,255,0.55), transparent);
  transform:skewX(-20deg) translateX(-20%);
  transition:transform 0.5s ease; pointer-events:none;
}
.btn-primary:hover,
.cta-pill:hover {
  background: linear-gradient(135deg, #ffffff 0%, #c8cdd4 40%, #e2e5e8 100%) !important;
  transform: translateY(-1px) !important;
}
.btn-primary:hover::before,
.cta-pill:hover::before { transform:skewX(-20deg) translateX(340%); }
@media (prefers-reduced-motion:reduce) {
  .btn-primary::before, .cta-pill::before { display:none; }
}
.btn-outline { border-color:#fff; color:#fff; background:transparent; }
.btn-outline:hover { background:rgba(255,255,255,0.1); }
.btn-outline-orange { border-color:var(--accent); color:var(--accent); background:transparent; }
.btn-dark { background:rgba(255,255,255,0.08); color:#fff; }
.btn-light { background:#fff; color:#000; }
.btn-full { width:100%; }
.hero-cta-row { display:flex; flex-wrap:wrap; gap:0.75rem; justify-content:center; }

.cta-pill {
  /* Colour/hover/sweep are on the shared .btn-primary,.cta-pill rules
     above — this just supplies the pill-specific box model, since
     .cta-pill is used standalone (not combined with .btn) in the nav. */
  padding: 0.65rem 1.4rem !important; border-radius: 9999px !important;
  text-decoration: none !important; display: inline-block !important;
}

/* ── HERO ── */
.hero {
  position:relative; min-height:100vh;
  display:flex; align-items:center;
  justify-content:center; color:#fff;
  overflow:hidden; background:#000000 !important;
}
.hero-media {
  position:absolute; top:-20%; left:0;
  width:100%; height:140%;
  object-fit:cover; object-position:center;
  will-change:transform; z-index:0;
}
.hero-overlay {
  position:absolute; inset:0;
  background:rgba(0,0,0,0.62) !important; z-index:1;
}
.hero-content { position:relative; z-index:3; text-align:center; }
.hero h1 {
  color:#fff; font-size:clamp(2.5rem,6vw,4rem);
  max-width:980px; margin-inline:auto;
}
.hero p { color:#fff; font-size:1.1rem; }
.hero-phone a { color:#fff; text-decoration:underline; font-weight:600; }

/* Hero trust rail — small structural "spec plate" tags rather than soft
   pills: flat corners, a thin silver top edge, hairline dividers between
   them, closer to an engineering nameplate than a marketing badge.
   (Design merged from Phase 2's premium redesign of this component.)

   display:inline-flex, not flex: a plain `flex` block still stretches
   to the full width of .hero-content and, with no justify-content, its
   flush-together spans sit left-aligned inside that oversized box — the
   exact "badges don't read as one balanced, centred group" bug the
   alignment audit fixed, just reintroduced by a different visual
   treatment of the same element. inline-flex sizes the whole plate to
   its content and lets it centre as a unit via the parent's
   text-align:center, the same way the plate's own bordered edge should
   only wrap its content, not the full hero width. */
.hero-trust-badges {
  display:inline-flex; flex-wrap:wrap; margin-top:1.75rem;
  border:1px solid rgba(255,255,255,0.18); border-radius:2px;
  overflow:hidden; backdrop-filter:blur(6px); -webkit-backdrop-filter:blur(6px);
}
.hero-trust-badges span {
  position:relative; background:rgba(0,0,0,0.35);
  border-top:2px solid var(--silver);
  border-left:1px solid rgba(255,255,255,0.14);
  color:#fff; font-size:var(--text-xs); font-weight:600;
  letter-spacing:0.03em; text-transform:uppercase;
  padding:0.5rem 0.9rem;
}
.hero-trust-badges span:first-child { border-left:none; }

/* ── HERO STRUCTURAL HEX LAYER + PARALLAX ──
   Axis's structural signature: a large, sparse hex mesh (steel-frame
   scale, not a dense tech-grid) sitting between the photo overlay and
   the hero content. Motion is transform-only (driven by JS setting CSS
   custom properties), so it never triggers layout/paint of anything
   else. Desktop pointer devices only — see generate_js(); everywhere
   else the layers are simply static. */
.hero-hex {
  position:absolute; inset:0; z-index:2; pointer-events:none;
  background-image:url('/assets/images/hex-grid.svg');
  background-repeat:repeat; background-size:208px 360px;
  opacity:0.12;
  transform:translateY(var(--hex-parallax-y, 0px));
}
.hero-media { transform:translateY(var(--hero-parallax-y, 0px)); }
@media (prefers-reduced-motion:reduce) {
  .hero-media, .hero-hex { transform:none !important; }
}

/* ── SECTIONS ── */
.section { padding:var(--space-2xl) 0; }
.section-light { background:#0a0a0a !important; }
.section-dark  { background:#000000 !important; }
.section-dark h2,.section-dark h3,.section-dark p { color:#ffffff; }
.section-intro { color:#9ca3af; margin-bottom:1.5rem; }

/* ── TRUST RAIL ── */
.trust-bar {
  background:var(--surface) !important;
  border-top:1px solid var(--border-strong);
  border-bottom:1px solid var(--border-strong);
  padding:var(--space-8) 0; overflow-x:auto;
}
.trust-items { display:flex; gap:0; justify-content:center; flex-wrap:wrap; }
.trust-item {
  display:flex; flex-direction:column; align-items:center; gap:var(--space-1);
  padding:0 var(--space-8); border-left:1px solid var(--border);
}
.trust-item:first-child { border-left:none; }
.trust-number,.trust-static { font-family:'Poppins',sans-serif; font-size:1.9rem; font-weight:700; color:#ffffff; letter-spacing:-0.02em; }
.trust-label { color:#9ca3af; font-size:var(--text-xs); text-align:center; text-transform:uppercase; letter-spacing:0.04em; }
@media (max-width:768px) {
  .trust-item { padding:0 var(--space-4); }
}

/* ── CARD SYSTEM ──
   Default surface is solid and architectural — a deliberate steel panel
   with a bright top edge, not glass. Heavy blur/saturate/brightness glass
   used to be applied to every card on the site; that's now reserved for
   .quote-form-card alone (the one genuine floating/input panel). Solid
   cards read as material, not as a translucent overlay effect. */
.service-card,
.testimonial-card,
.contact-card,
.social-card,
.decision-card {
  position: relative;
  background: var(--surface-2) !important;
  border: 1px solid var(--border) !important;
  border-top: 2px solid var(--border-strong) !important;
  border-radius: 10px !important;
  box-shadow: 0 1px 2px rgba(0,0,0,0.4), 0 8px 24px rgba(0,0,0,0.35) !important;
  transition: transform 0.2s ease, border-color 0.2s ease, box-shadow 0.2s ease !important;
}
.service-card:hover,
.testimonial-card:hover,
.social-card:hover,
.decision-card:hover {
  transform: translateY(-3px) !important;
  border-color: var(--silver) !important;
  box-shadow: 0 4px 8px rgba(0,0,0,0.45), 0 16px 36px rgba(0,0,0,0.4) !important;
}

/* Reserved glass — the quote form only. */
.glass-card,
.quote-form-card {
  position: relative; overflow: hidden;
  background: rgba(255,255,255,0.045) !important;
  border: 1px solid var(--border-strong) !important;
  backdrop-filter: blur(16px) saturate(160%) !important;
  -webkit-backdrop-filter: blur(16px) saturate(160%) !important;
  border-radius: 14px !important;
  box-shadow:
    0 4px 6px rgba(0,0,0,0.4),
    0 10px 40px rgba(0,0,0,0.5),
    inset 0 1px 0 rgba(255,255,255,0.10) !important;
}
.quote-form-card:hover { transform: none !important; }

/* ── SERVICES GRID ──
   Both .services-grid and .service-listing always render the same 9
   SERVICES entries, so — unlike .decision-grid, which is reused with
   varying counts — this can be a fully deliberate, zero-ambiguity
   composition rather than a general-purpose fallback:
     mobile           (≤768px):     1 column
     tablet + desktop (≥769px):     3 columns → 9 = 3 + 3 + 3, always
   A 2-column tablet tier was deliberately rejected: 9 services in 2
   columns is 4 + 4 + 1, the exact orphan-row problem this system
   exists to avoid. Percentage-based flex-basis (not a fixed px
   value) means a full row always sums to exactly 100% and sits flush
   with the container edges, matching every other section. */
.services-grid, .service-listing {
  display:flex; flex-wrap:wrap; justify-content:center; gap:1rem;
}
.services-grid .service-card, .service-listing .service-card {
  flex:0 0 100%;
}
@media (min-width:769px) {
  .services-grid .service-card, .service-listing .service-card {
    flex-basis:calc(33.333% - 0.667rem);
  }
}
.service-card { padding:1.5rem; }
.service-icon {
  width:40px; height:40px; border-radius:50%;
  background: linear-gradient(135deg, #c8cdd4, #8e949c) !important;
  margin-bottom:0.75rem;
}
.service-card h3, .service-card h2 { margin-bottom:0.6rem; }
.service-card a { color:#e5e7eb; font-weight:600; text-decoration:none; }
.service-card a:hover { color:#ffffff; }

/* ── SPLIT GRID ── */
.split-grid { display:grid; grid-template-columns:1fr 1fr; gap:2rem; align-items:center; }
.rounded-image { border-radius:1rem; }

/* ── USP LIST ── */
.usp-list { list-style:none; padding:0; margin:0 0 1.25rem; }
.usp-list li { margin-bottom:0.7rem; padding-left:1.5rem; position:relative; color:#d1d5db; }
.usp-list li::before {
  content:'✔'; position:absolute; left:0;
  background: linear-gradient(135deg, #e8eaed, #9ba3ab);
  -webkit-background-clip: text; -webkit-text-fill-color: transparent;
  background-clip: text;
}
@supports not (-webkit-background-clip: text) {
  .usp-list li::before { color:#c8cdd4 !important; -webkit-text-fill-color:unset !important; }
}
.about-blurb {
  background:rgba(255,255,255,0.04);
  border-left:4px solid rgba(255,255,255,0.18);
  padding:0.9rem; border-radius:0.75rem; color:#d1d5db;
}

/* ── PROJECTS GRID ──
   Interim composition fix only. The homepage's 6-project preview
   divides evenly into 3-column rows either way (6 = 3+3 desktop, 3+3
   tablet, 6×1 mobile — no orphan). The full gallery page's 14 items
   don't (14 = 3+3+3+3+2 at 3 columns), so this uses the same
   percentage-based system as the services grid — full rows flush
   with the container edges, a short trailing row centred rather than
   left-stuck.
   This is deliberately NOT the featured-item + editorial-grid
   treatment the gallery page's 14 photos would benefit from (a
   uniform matrix isn't the best composition for 14 real, unequal
   project photos) — that richer layout already exists, built for
   Phase 3 (unmerged PR #21, which adds a featured card + accessible
   lightbox on top of the same PROJECTS data). Rebuilding it here
   would duplicate that work and conflict with it on merge. This PR
   only makes the current simple grid's row composition deliberate;
   see ALIGNMENT_SYSTEM.md for the merge-order note. */
.projects-grid { display:flex; flex-wrap:wrap; justify-content:center; gap:1rem; }
.projects-grid .project-item { flex:0 0 100%; }
@media (min-width:769px) {
  .projects-grid .project-item { flex-basis:calc(33.333% - 0.667rem); }
}
/* .project-item is a <figure> — reset the browser's default figure
   margin (1em 40px). Left unset, that 40px-per-side margin doesn't
   collapse in a flex/grid row: it silently ate into each card's
   available width, which is what caused the fixed percentage basis
   above to overflow its row and wrap early instead of filling it
   edge-to-edge. Independent of, and pre-dating, this composition
   fix — the same default margin was already present under the
   original CSS Grid version of this component. */
.project-item { position:relative; overflow:hidden; border-radius:1rem; margin:0; }
.project-item img { width:100%; height:100%; object-fit:cover; }
.project-item figcaption {
  position:absolute; inset:auto 0 0 0; padding:0.8rem;
  background:linear-gradient(transparent,rgba(0,0,0,0.8));
  color:#fff; transform:translateY(100%); transition:transform 0.25s ease;
}
.project-item:hover figcaption { transform:translateY(0); }
.project-item figcaption span { display:block; font-weight:700; }
.project-item figcaption small { color:#f5f5f5; }
.centered { text-align:center; }

/* ── TESTIMONIALS ── */
.testimonial-carousel { overflow:hidden; }
.testimonial-track { display:flex; transition:transform 0.5s ease; }
.testimonial-card { min-width:100%; padding:1.75rem; }
.review-stars {
  color:#f5c518; font-size:1.3rem; letter-spacing:2px;
  margin-bottom:0.75rem; display:block;
}
.review-stars span { color:#f5c518 !important; display:inline-block; line-height:1; }
.review-text {
  color:#d1d5db; font-size:0.95rem; line-height:1.7;
  font-style:italic; margin:0 0 1.25rem; padding:0; border:none;
}
.reviewer-info { display:flex; align-items:center; justify-content:space-between; gap:0.5rem; flex-wrap:wrap; }
.reviewer-name { color:#ffffff; font-family:'Poppins',sans-serif; font-weight:600; font-size:0.9rem; }
.review-source { display:flex; align-items:center; gap:0.35rem; color:#6b7280; font-size:0.78rem; }
.review-source img { width:16px; height:16px; display:inline-block; }

/* ── AREA PILLS ── */
.area-pills { list-style:none; padding:0; margin:0; display:flex; flex-wrap:wrap; gap:0.6rem; }
.area-pills li { display:inline-flex; }
.area-pill-link {
  display:inline-block; padding:0.45rem 0.9rem;
  border:1px solid #c8cdd4 !important; color:#c8cdd4 !important;
  border-radius:9999px; text-decoration:none; font-weight:500;
}
.area-pill-link:hover {
  background: linear-gradient(135deg, #e8eaed, #c8cdd4) !important;
  color: #000000 !important; border-color:transparent !important;
}

/* ── FAQ ── */
.faq-wrap { max-width:900px; }
.faq-item {
  background:rgba(255,255,255,0.03) !important;
  border:1px solid rgba(255,255,255,0.08) !important;
  border-radius:12px; margin-bottom:0.75rem;
  overflow:hidden; transition:all 0.3s ease;
}
.faq-item.open {
  border-left:3px solid #c8cdd4 !important;
  background:rgba(200,205,212,0.04) !important;
}
.faq-question {
  width:100%; text-align:left; background:transparent; border:none;
  padding:1rem; font-size:1rem; font-weight:600; cursor:pointer;
  color:#ffffff !important;
}
.faq-answer { display:none; padding:0 1rem 1rem; color:#d1d5db !important; }

/* ── QUOTE FORM ── */
.quote-form-card { padding:1.5rem; }
.quote-form-card form p { margin-bottom:0.9rem; }
.quote-form-card label { display:block; margin-bottom:0.35rem; font-weight:600; color:#ffffff !important; }
.quote-form-card input,
.quote-form-card select,
.quote-form-card textarea {
  width:100%; background:rgba(255,255,255,0.06) !important;
  border:1px solid rgba(255,255,255,0.14) !important;
  border-radius:10px !important; color:#ffffff !important;
  padding:0.7rem 0.9rem !important; font:inherit !important;
  transition:border-color 0.2s ease !important;
}
.quote-form-card input:focus,
.quote-form-card select:focus,
.quote-form-card textarea:focus {
  border-color:rgba(255,255,255,0.45) !important; outline:none !important;
  background:rgba(255,255,255,0.09) !important;
}
.quote-form-card select option { background:#0a0a0a; color:#ffffff; }
.quote-form-card textarea { min-height:120px; }
.form-message { min-height:1.2rem; font-weight:600; color:#34d399; }

/* ── CTA BANNER ── */
.cta-banner {
  background:linear-gradient(135deg, #111314 0%, #1e2124 50%, #111314 100%) !important;
  border-top:1px solid rgba(200,205,212,0.2) !important;
  border-bottom:1px solid rgba(200,205,212,0.2) !important;
  padding:2.4rem 0;
}
.cta-banner h2, .cta-banner p { color:#ffffff !important; }
.cta-banner-inner { display:flex; align-items:center; justify-content:space-between; gap:1rem; flex-wrap:wrap; }

/* ── INNER PAGES ── */
.inner-hero { background:#0a0a0a !important; padding:8rem 0 3rem; }
.inner-hero h1 { margin-bottom:0.6rem; color:#ffffff; }
.breadcrumbs { font-size:0.92rem; color:#9ca3af; margin-bottom:1rem; }
.breadcrumbs a { color:#d1d5db; text-decoration:none; }
.two-col { display:grid; grid-template-columns:1fr 1fr; gap:1.5rem; }
.contact-card { padding:1.1rem; }

/* ── FOOTER ── */
.site-footer {
  background:rgba(255,255,255,0.03) !important;
  border-top:1px solid rgba(255,255,255,0.08) !important;
  color:#9ca3af; padding-top:3rem;
}
.site-footer h2 { color:#fff; font-size:1.1rem; margin-bottom:0.8rem; }
.footer-grid { display:grid; grid-template-columns:repeat(4,minmax(0,1fr)); gap:1.2rem; }
.site-footer ul { list-style:none; padding:0; margin:0; }
.site-footer li { margin-bottom:0.35rem; }
.site-footer a { color:#d1d5db; text-decoration:none; transition:color 0.2s; }
.site-footer a:hover { color:var(--accent); }
.footer-social-links { display:flex; gap:0.5rem; }
.footer-social-link {
  width:36px; height:36px; background:rgba(255,255,255,0.07);
  border:1px solid rgba(255,255,255,0.12); border-radius:50%;
  display:flex; align-items:center; justify-content:center;
  transition:background 0.2s, border-color 0.2s;
}
.footer-social-link:hover {
  background:rgba(200,205,212,0.15); border-color:rgba(255,255,255,0.28);
}
.footer-social-link svg {
  width:18px; height:18px; fill:#d1d5db; transition:fill 0.2s ease;
}
.footer-social-link:hover svg { fill:#c8cdd4; }
.footer-bottom {
  text-align:center; padding:1.2rem 0 2rem;
  border-top:1px solid rgba(255,255,255,0.06); margin-top:2rem;
}
.footer-bottom p { color:#6b7280; margin-bottom:0.65rem; }
.footer-legal-links { display:flex; justify-content:center; gap:1rem; flex-wrap:wrap; }
.text-button {
  border:none; background:none; color:#d1d5db;
  text-decoration:underline; cursor:pointer; font:inherit;
}

/* ── DOMAIN MOVE BANNER ── */
.domain-move-banner {
  background:rgba(255,255,255,0.05);
  border-bottom:1px solid rgba(255,255,255,0.1);
  color:#d1d5db; text-align:center;
  padding:0.75rem 1rem; font-weight:600;
}
.domain-move-banner a { color:#c8cdd4; text-decoration:underline; }

/* ── 404 ── */
.not-found-wrap {
  min-height:100vh; display:grid; place-content:center;
  gap:0.8rem; text-align:center; padding:2rem;
  background:#000000;
}

/* ── CONNECT / SOCIAL SECTION ── */
.connect-section {
  background:#000000; padding:5rem 2rem; text-align:center;
  border-top:1px solid rgba(255,255,255,0.07);
}
.connect-inner { max-width:800px; margin:0 auto; }
.connect-section h2 {
  font-family:'Poppins',sans-serif;
  font-size:clamp(1.8rem,3vw,2.4rem);
  font-weight:700; color:#ffffff; margin:0 0 1rem;
}
.connect-section p { color:#9ca3af; font-size:1rem; margin:0 0 2.5rem; }
.social-links { display:flex; justify-content:center; gap:1.5rem; flex-wrap:wrap; }
.social-card {
  display:flex; flex-direction:column; align-items:center; gap:0.5rem;
  padding:2rem 2.5rem; min-width:160px; text-decoration:none;
}
.social-card svg { width:36px; height:36px; fill:#ffffff; transition:transform 0.2s ease; }
.social-card:hover svg { transform: scale(1.1); }
.social-card span { color:#ffffff; font-family:'Poppins',sans-serif; font-weight:600; font-size:1rem; }
.social-card small { color:#6b7280; font-size:0.78rem; }

/* ── COOKIE BAR ── */
.cookie-bar {
  display:none; position:fixed; bottom:0; left:0; right:0; z-index:99999;
  background:var(--surface); border-top:2px solid var(--border-strong);
  padding:var(--space-4) var(--space-8); flex-wrap:wrap;
  align-items:center; justify-content:space-between; gap:var(--space-4);
}
.cookie-bar p { color:var(--text-secondary); font-size:var(--text-sm); max-width:600px; margin:0; }
.cookie-bar p strong { color:#fff; }
.cookie-bar p a { color:var(--silver); text-decoration:underline; }
.cookie-bar-actions { display:flex; flex-wrap:wrap; gap:var(--space-3); align-items:center; }
.cookie-bar-actions .btn-manage {
  background:none; border:none; color:var(--text-muted);
  font-size:var(--text-sm); cursor:pointer; text-decoration:underline; padding:0.5rem 0;
}
.cookie-prefs-panel {
  position:fixed; bottom:80px; left:0; right:0; z-index:99998;
  background:var(--surface); border-top:1px solid var(--border-strong);
  padding:var(--space-6) var(--space-8); font-size:var(--text-sm); color:var(--text-secondary);
}
.cookie-prefs-panel .cookie-prefs-title { color:#fff; font-weight:600; margin:0 0 var(--space-4); }
.cookie-prefs-panel .cookie-prefs-row {
  display:flex; justify-content:space-between; align-items:center;
  padding:var(--space-2) 0; border-bottom:1px solid var(--border);
}
.cookie-prefs-panel .cookie-prefs-row:last-of-type { border-bottom:none; }
.cookie-prefs-panel .btn-save-prefs {
  margin-top:var(--space-4); background:linear-gradient(135deg,#e8eaed,#c8cdd4);
  color:#000; border:none; border-radius:9999px; padding:0.5rem 1.5rem;
  font-weight:700; cursor:pointer;
}
@media (max-width:768px) {
  .cookie-bar { padding:var(--space-4); }
}

/* ── DECISION CARDS ──
   Explicit per-breakpoint composition, not organic reflow — a card's
   width is a defined FRACTION of the row (100%, 33.333%, 20%), so a
   full row always sums to exactly 100% and sits flush with the
   container edges (matching every other section on the page), and
   only a genuinely incomplete trailing row is narrower than 100% and
   gets centred by justify-content:center. This is deliberately
   designed for the 5-card homepage instance:
     mobile  (≤768px):        1 column
     tablet  (769–1024px):    3 columns  → 5 cards = 3 + 2, centred
     desktop (≥1025px):       5 columns  → 5 cards = one full row
   Other pages reuse .decision-grid with 3/4/6 cards; the same
   percentage system still applies (a full row always reaches the
   container edges; a short last row centres instead of sticking
   left) even though the exact column counts above were tuned for 5. */
.decision-section { padding-bottom:3rem; }
.decision-grid {
  display:flex; flex-wrap:wrap; justify-content:center;
  gap:1.25rem; margin-top:1.5rem;
}
.decision-card {
  /* Background/border/hover come from the shared card system above —
     this supplies layout (and, below, this component's explicit
     per-breakpoint composition) only. */
  flex:0 0 100%;
  padding:1.75rem 1.25rem 1.5rem;
  text-decoration:none; color:#ffffff;
  display:flex; flex-direction:column; gap:0.5rem;
}
@media (min-width:769px) {
  .decision-card { flex-basis:calc(33.333% - 0.834rem); }
}
@media (min-width:1025px) {
  .decision-card { flex-basis:calc(20% - 1rem); }
}
.decision-card-urgent {
  border-color:rgba(255,100,100,0.35) !important;
  border-top-color:rgba(255,120,120,0.6) !important;
  background:rgba(255,50,50,0.06) !important;
}
.decision-card-urgent:hover { border-color:rgba(255,120,120,0.55) !important; }
/* "Not Sure" is a deliberately different job (an open catch-all, not
   a category) — a subtly distinct treatment so its position in the
   layout (whatever row it lands on) reads as intentional rather than
   "the leftover card". Styling only; copy is unchanged in this PR. */
.decision-card-open {
  border-style:dashed !important;
  border-color:rgba(255,255,255,0.24) !important;
  background:rgba(255,255,255,0.02) !important;
}
.decision-card-open:hover { border-color:rgba(255,255,255,0.4) !important; }
.decision-icon { width:44px; height:44px; color:#c8cdd4; margin-bottom:0.25rem; }
.decision-icon svg { width:100%; height:100%; }
.decision-card h3 { font-size:1.1rem; margin:0; color:#ffffff; }
.decision-card p { font-size:0.9rem; color:#9ca3af; margin:0; }
.decision-link { font-size:0.85rem; font-weight:600; color:#c8cdd4; margin-top:auto; padding-top:0.5rem; }

/* ── PROCESS STEPS ── */
.process-steps {
  list-style:none; padding:0; margin:0;
  display:flex; flex-direction:column; gap:1.5rem;
}
.process-step { display:flex; gap:1.25rem; align-items:flex-start; }
.process-num {
  flex-shrink:0; width:2.5rem; height:2.5rem;
  background:linear-gradient(135deg,#e8eaed,#9ba3ab);
  color:#000; font-family:'Poppins',sans-serif;
  font-weight:700; font-size:1rem; border-radius:50%;
  display:flex; align-items:center; justify-content:center;
}
.process-step h3 { font-size:1.05rem; margin-bottom:0.25rem; color:#ffffff; }
.process-step p { color:#9ca3af; font-size:0.95rem; margin:0; }

/* ── USP EVIDENCE LIST ── */
.usp-evidence { list-style:none; padding:0; }
.usp-evidence li { margin-bottom:1rem; }
.usp-evidence strong { display:block; font-weight:700; margin-bottom:0.15rem; color:#ffffff; }
.usp-evidence span { font-size:0.92rem; color:#9ca3af; }

/* ── PRICING / DIRECT ANSWER ── */
.pricing-factors { color:#d1d5db; }
.pricing-factors li { margin-bottom:0.35rem; }
.direct-answer {
  font-size:1.05rem; font-weight:600; color:#ffffff;
  background:rgba(255,255,255,0.05);
  border-left:4px solid #c8cdd4;
  padding:0.75rem 1rem; border-radius:0 0.5rem 0.5rem 0;
  margin-bottom:1.25rem;
}

/* ── SCROLL REVEAL ── */
.reveal-up,.reveal-left,.reveal-right {
  opacity:0; transition:opacity 0.6s ease, transform 0.6s ease;
}
.reveal-up    { transform:translateY(30px); }
.reveal-left  { transform:translateX(-40px); }
.reveal-right { transform:translateX(40px); }
.reveal-up.is-visible,
.reveal-left.is-visible,
.reveal-right.is-visible { opacity:1; transform:none; }

/* ── MOBILE STICKY CTA BAR ── */
.mobile-cta-bar {
  display:none; position:fixed; bottom:0; left:0; right:0;
  z-index:9999; background:var(--surface-3); padding:0;
  padding-bottom:env(safe-area-inset-bottom);
  border-top:2px solid var(--border-strong);
  height:56px; box-shadow:0 -2px 10px rgba(0,0,0,0.4);
}
.mobile-cta-bar .cta-buttons { display:flex; height:100%; }
.mobile-cta-bar .btn-call,
.mobile-cta-bar .btn-quote {
  flex:1; display:flex; align-items:center; justify-content:center;
  gap:0.5rem; font-size:16px; font-weight:700;
  text-decoration:none; transition:background 0.2s ease;
}
/* Call keeps a distinct (desaturated, on-brand-darkened) green — a
   deliberate functional exception, not a decorative one: call vs. quote
   need to read as two different actions at a glance on the one sticky
   bar every mobile visitor sees on every page. */
.mobile-cta-bar .btn-call { background:#2f6b46; color:#ffffff; border-right:1px solid var(--border); }
.mobile-cta-bar .btn-quote { background:var(--silver); color:#000000; }
.mobile-cta-bar svg { width:18px; height:18px; }
@media (max-width:768px) { .mobile-cta-bar { display:flex; } }

/* ── RESPONSIVE ── */
@media (max-width:1024px) {
  .split-grid,.two-col { grid-template-columns:1fr; }
}
@media (max-width:768px) {
  .menu-toggle { display:inline-flex; }
  .nav-phone-mobile { display:inline-flex; align-items:center; }
  .nav-phone-desktop { display:none; }
  .site-nav {
    /* Deliberately not "inset:0 0 0 30%": .site-header has a
       backdrop-filter, which creates a new containing block for
       position:fixed descendants — bottom:0 would then resolve against
       the ~90px header instead of the viewport, leaving the drawer only
       as tall as the header. Explicit vh sizing sidesteps that (vh units
       are always viewport-relative regardless of containing block). */
    position:fixed; top:0; right:0; left:30%;
    height:100vh; height:100dvh; overflow-y:auto;
    background:var(--surface); border-left:1px solid var(--border-strong);
    padding:6rem var(--space-6) var(--space-6); display:flex;
    flex-direction:column; align-items:stretch; gap:0;
    transform:translateX(100%); transition:transform 0.3s ease;
  }
  .site-nav.open { transform:translateX(0); }
  .site-nav a:not(.cta-pill) {
    width:100%; padding:var(--space-4) 0;
    border-bottom:1px solid var(--border); font-size:var(--text-lg);
  }
  .site-nav a:not(.cta-pill)::after { display:none; }
  .site-nav .cta-pill, .site-nav .nav-phone-desktop { margin-top:var(--space-6); }
  .nav-wrap { grid-template-columns:auto auto; justify-content:space-between; }
  .footer-grid { grid-template-columns:1fr; }
  .hero-media { top:0 !important; height:100% !important; transform:none !important; }
}
@media (max-width:480px) {
  .social-card { width:100%; min-width:unset; }
}
@media (max-width:375px) {
  .container { width:calc(100% - 1rem); }
  .hero h1 { font-size:2.2rem; }
}
@media (max-width:320px) { .hero h1 { font-size:2rem; } }
@media (min-width:1440px) { .container { width:min(1280px,calc(100% - 3rem)); } }
@media (prefers-reduced-motion:reduce) {
  .reveal-up,.reveal-left,.reveal-right {
    opacity:1 !important; transform:none !important; transition:none !important;
  }
  *, *::before, *::after { animation:none !important; transition-duration:0.01ms !important; }
  #mouse-glow { display:none !important; }
}
"""
    write("assets/css/style.css", css)


def generate_js() -> None:
    js = """
(() => {
  const CONTACT_EMAIL = 'axis-scaffolding@outlook.com';
  const header = document.getElementById('site-header');
  const menuToggle = document.getElementById('menu-toggle');
  const siteMenu = document.getElementById('site-menu');
  const setHeaderState = () => {
    if (!header) return;
    header.classList.toggle('scrolled', window.scrollY > 12);
  };
  const currentHost = window.location.hostname.toLowerCase();
  if (currentHost === 'axisscaffolding.co.uk' || currentHost === 'www.axisscaffolding.co.uk') {
    const nextUrl = `https://www.axisscaffoldingessex.co.uk${window.location.pathname}${window.location.search}${window.location.hash}`;
    const moveBanner = document.getElementById('domain-move-banner');
    const canonicalTag = document.querySelector('link[rel="canonical"]');
    if (canonicalTag) canonicalTag.setAttribute('href', nextUrl);
    if (moveBanner) moveBanner.hidden = false;
    window.setTimeout(() => {
      window.location.replace(nextUrl);
    }, 2200);
  }
  setHeaderState();
  window.addEventListener('scroll', setHeaderState, { passive: true });

  // ── HERO PARALLAX ──
  // Cinematic and restrained by design: over a 500px scroll the hero photo
  // lags the page by ~100px and the hex layer by ~50px (0.2 / 0.1 of the
  // scroll delta). Transform-only, rAF-batched, desktop-pointer-only.
  (function heroParallax() {
    const hero = document.querySelector('.hero');
    const heroMedia = hero && hero.querySelector('.hero-media');
    const heroHex = hero && hero.querySelector('.hero-hex');
    if (!hero || !heroMedia || !heroHex) return;

    const HERO_RATIO = 0.2;
    const HEX_RATIO = 0.1;
    const canAnimate = () =>
      window.matchMedia('(min-width: 769px)').matches &&
      window.matchMedia('(hover: hover)').matches &&
      !window.matchMedia('(prefers-reduced-motion: reduce)').matches;

    let active = false;
    let ticking = false;

    function reset() {
      heroMedia.style.removeProperty('--hero-parallax-y');
      heroHex.style.removeProperty('--hex-parallax-y');
    }

    function update() {
      ticking = false;
      const rect = hero.getBoundingClientRect();
      if (rect.bottom < 0 || rect.top > window.innerHeight) return;
      const scrolled = Math.max(0, -rect.top);
      heroMedia.style.setProperty('--hero-parallax-y', (scrolled * HERO_RATIO) + 'px');
      heroHex.style.setProperty('--hex-parallax-y', (scrolled * HEX_RATIO) + 'px');
    }

    function onScroll() {
      if (!active || ticking) return;
      ticking = true;
      requestAnimationFrame(update);
    }

    function sync() {
      const should = canAnimate();
      if (should === active) return;
      active = should;
      if (active) {
        update();
      } else {
        reset();
      }
    }

    sync();
    window.addEventListener('scroll', onScroll, { passive: true });
    window.addEventListener('resize', sync, { passive: true });
  })();
  if (menuToggle && siteMenu) {
    menuToggle.addEventListener('click', () => {
      const open = siteMenu.classList.toggle('open');
      menuToggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  }

  document.querySelectorAll('.faq-question').forEach((button) => {
    button.addEventListener('click', () => {
      document.querySelectorAll('.faq-question').forEach((item) => {
        const panel = document.getElementById(item.getAttribute('aria-controls'));
        const open = item === button && item.getAttribute('aria-expanded') !== 'true';
        item.setAttribute('aria-expanded', open ? 'true' : 'false');
        if (panel) panel.style.display = open ? 'block' : 'none';
      });
    });
  });

  const track = document.getElementById('testimonial-track');
  const carousel = document.getElementById('testimonial-carousel');
  let idx = 0;
  let timer = null;
  const start = () => {
    if (!track || track.children.length <= 1) return;
    timer = window.setInterval(() => {
      idx = (idx + 1) % track.children.length;
      track.style.transform = `translateX(-${idx * 100}%)`;
    }, 4500);
  };
  const stop = () => {
    if (timer) clearInterval(timer);
    timer = null;
  };
  if (carousel) {
    carousel.addEventListener('mouseenter', stop);
    carousel.addEventListener('mouseleave', start);
  }
  start();

  // ── ANALYTICS (consent-gated, no-op until a real GA4 ID is configured) ──
  const CATEGORIES_KEY = 'axis_cookie_categories';
  function loadGA4() {
    if (!window.AXIS_GA4_ID || window.__axisGA4Loaded) return;
    window.__axisGA4Loaded = true;
    var s = document.createElement('script');
    s.src = 'https://www.googletagmanager.com/gtag/js?id=' + window.AXIS_GA4_ID;
    s.async = true;
    document.head.appendChild(s);
    window.dataLayer = window.dataLayer || [];
    window.gtag = function() { window.dataLayer.push(arguments); };
    window.gtag('js', new Date());
    window.gtag('config', window.AXIS_GA4_ID, { anonymize_ip: true });
  }
  function trackEvent(name, params) {
    if (typeof window.gtag === 'function') window.gtag('event', name, params || {});
  }
  function applyConsentCategories(categories) {
    localStorage.setItem(CATEGORIES_KEY, JSON.stringify(categories));
    if (categories.analytics) loadGA4();
  }
  (function restoreConsent() {
    try {
      const stored = JSON.parse(localStorage.getItem(CATEGORIES_KEY) || 'null');
      if (stored && stored.analytics) loadGA4();
    } catch (_err) { /* ignore malformed stored consent */ }
  })();
  document.querySelectorAll('a[href^="tel:"]').forEach((link) => {
    link.addEventListener('click', () => {
      trackEvent('phone_click', { event_category: 'Lead', link_url: link.getAttribute('href') });
    });
  });
  document.querySelectorAll('.axis-quote-form').forEach((form) => {
    let started = false;
    form.addEventListener('input', () => {
      if (started) return;
      started = true;
      trackEvent('quote_start', { event_category: 'Lead', event_label: form.dataset.formName || 'quote_form' });
    }, { once: false, capture: true });
  });
  // ── END ANALYTICS ──

  const CONSENT_KEY = 'axis_cookie_consent';
  var bar = document.getElementById('axis-cookie-bar');
  function showBar() {
    if (bar) bar.style.display = 'flex';
  }
  function hideBar() {
    if (bar) bar.style.display = 'none';
  }
  function setConsent(value) {
    localStorage.setItem(CONSENT_KEY, value);
    hideBar();
  }
  if (!localStorage.getItem(CONSENT_KEY)) {
    showBar();
  }
  var acceptBtn = document.getElementById('axis-cookie-accept');
  if (acceptBtn) {
    acceptBtn.addEventListener('click', function() {
      setConsent('accepted');
      applyConsentCategories({ analytics: true, marketing: true });
    });
  }
  var rejectBtn = document.getElementById('axis-cookie-reject');
  if (rejectBtn) {
    rejectBtn.addEventListener('click', function() {
      setConsent('rejected');
      applyConsentCategories({ analytics: false, marketing: false });
    });
  }
  var manageBtn = document.getElementById('axis-cookie-manage');
  if (manageBtn) {
    manageBtn.addEventListener('click', function() {
      var existing = document.getElementById('axis-cookie-prefs');
      if (existing) { existing.remove(); return; }
      var panel = document.createElement('div');
      panel.id = 'axis-cookie-prefs';
      panel.className = 'cookie-prefs-panel';
      panel.innerHTML = '<p class="cookie-prefs-title">Cookie Preferences</p>' +
        '<div>' +
        '<label class="cookie-prefs-row">' +
        '<span>Necessary <span style="color:#6b7280;font-size:0.75rem;">(always on)</span></span>' +
        '<input type="checkbox" checked disabled></label>' +
        '<label class="cookie-prefs-row">' +
        '<span>Analytics</span><input type="checkbox" id="axis-pref-analytics"></label>' +
        '<label class="cookie-prefs-row">' +
        '<span>Marketing</span><input type="checkbox" id="axis-pref-marketing"></label>' +
        '</div>' +
        '<button id="axis-pref-save" class="btn-save-prefs">Save Preferences</button>';
      document.body.appendChild(panel);
      var save = document.getElementById('axis-pref-save');
      if (save) {
        save.addEventListener('click', function() {
          var analyticsChecked = document.getElementById('axis-pref-analytics');
          var marketingChecked = document.getElementById('axis-pref-marketing');
          panel.remove();
          setConsent('custom');
          applyConsentCategories({
            analytics: !!(analyticsChecked && analyticsChecked.checked),
            marketing: !!(marketingChecked && marketingChecked.checked),
          });
        });
      }
    });
  }
  var footerBtn = document.getElementById('axis-footer-cookie-btn');
  if (footerBtn) {
    footerBtn.addEventListener('click', function() {
      localStorage.removeItem(CONSENT_KEY);
      localStorage.removeItem(CATEGORIES_KEY);
      showBar();
    });
  }

  document.querySelectorAll('.axis-quote-form').forEach((form) => {
    form.addEventListener('submit', async (event) => {
      const webhook = window.AXIS_QUOTE_WEBHOOK;

      // No webhook is configured: allow the form's native FormSubmit action to run.
      // The previous code prevented the native POST and then displayed a false success
      // message, which could silently discard every quote enquiry.
      if (!webhook) {
        trackEvent('generate_lead', { event_category: 'Lead', event_label: form.dataset.formName || 'quote_form' });
        return;
      }

      event.preventDefault();
      const message = form.querySelector('.form-message');
      const data = Object.fromEntries(new FormData(form).entries());
      const payload = { ...data, notification_email: CONTACT_EMAIL };
      let ok = false;

      try {
        const res = await fetch(webhook, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(payload),
        });
        ok = res.ok;
      } catch (_err) {
        ok = false;
      }

      if (message) {
        message.textContent = ok
          ? 'Thanks. Your quote request has been received. We will respond within one working day.'
          : 'There was a problem submitting your request. Please call 01702 820468 to reach us directly.';
      }

      if (ok) {
        trackEvent('generate_lead', { event_category: 'Lead', event_label: form.dataset.formName || 'quote_form' });
        form.reset();
        window.setTimeout(() => {
          window.location.assign('/thank-you');
        }, 250);
      } else {
        trackEvent('quote_error', { event_category: 'Lead', event_label: form.dataset.formName || 'quote_form' });
      }
    });
  });
})();

// ── WHITE MOUSE GLOW ──────────────────────
(function() {
  if (window.matchMedia('(hover: none)').matches) return;
  if (window.matchMedia('(max-width: 768px)').matches) return;

  var glow = document.getElementById('mouse-glow');
  if (!glow) return;

  var mouseX = window.innerWidth / 2;
  var mouseY = window.innerHeight / 2;
  var currentX = mouseX;
  var currentY = mouseY;

  function lerp(start, end, factor) {
    return start + (end - start) * factor;
  }

  function animate() {
    currentX = lerp(currentX, mouseX, 0.12);
    currentY = lerp(currentY, mouseY, 0.12);
    glow.style.left = currentX + 'px';
    glow.style.top  = currentY + 'px';
    requestAnimationFrame(animate);
  }

  document.addEventListener('mousemove', function(e) {
    mouseX = e.clientX;
    mouseY = e.clientY;
  }, { passive: true });

  animate();

  document.addEventListener('mouseleave', function() {
    glow.style.opacity = '0';
  });
  document.addEventListener('mouseenter', function() {
    glow.style.opacity = '1';
  });
})();
// ── END MOUSE GLOW ────────────────────────
"""
    write("assets/js/main.js", js)


PROJECT_ROWS = [
    ("project-1.webp",         "Residential Scaffolding",         "Benfleet",       "Full perimeter scaffold for roof replacement on a detached house."),
    ("project-2.webp",         "Commercial Scaffolding",          "Canvey Island",  "Multi-elevation access scaffold for a commercial refurbishment."),
    ("project-3.webp",         "Shopfront Access Scaffold",       "Rayleigh",       "Single-elevation scaffold for shopfront rendering and signage work."),
    ("project-4.webp",         "Temporary Roofing Scaffold",      "Southend-on-Sea","Scaffold with temporary roof cover to protect during roof replacement."),
    ("project-5.webp",         "Roof Scaffolding",                "Basildon",       "Roof-level scaffold for chimney repointing and ridge tile replacement."),
    ("project-6.webp",         "Domestic Scaffolding",            "Chelmsford",     "Rear-elevation scaffold for extension construction access."),
    ("project-7.webp",         "Residential Scaffolding",         "Wickford",       "Full scaffold erected for a complete re-roofing project."),
]

GALLERY_ROWS = PROJECT_ROWS + [
    ("gallery-project-8.webp",  "Roof Scaffolding",               "Hadleigh",       "Scaffold for roof and roofline replacement on a semi-detached property."),
    ("gallery-project-9.webp",  "Domestic Scaffolding",           "Leigh-on-Sea",   "Single-elevation domestic scaffold for fascia and soffit replacement."),
    ("gallery-project-10.webp", "Residential Scaffolding",        "Thundersley",    "Full perimeter scaffold for a complete exterior renovation project."),
    ("gallery-project-11.webp", "Commercial Scaffolding",         "Rayleigh",       "Commercial scaffold erected for building envelope maintenance works."),
    ("gallery-project-12.webp", "Render Scaffold",                "Benfleet",       "Scaffold providing full access for external render replacement."),
    ("gallery-project-13.webp", "Extension Scaffold",             "Chelmsford",     "Side and rear scaffold to support a two-storey extension build."),
    ("gallery-project-14.webp", "Roof Scaffolding",               "Rochford",       "Roof scaffold for full tile replacement and chimney repointing."),
]


def project_cards(full_gallery: bool = False) -> str:
    rows = GALLERY_ROWS if full_gallery else PROJECT_ROWS[:6]
    return "".join(
        f"""
<figure class="project-item">
  <img src="/images/{img}" alt="{label} — {location}, Essex" width="640" height="800" loading="lazy" decoding="async">
  <figcaption><span>{label}</span><small>{location} — {desc}</small></figcaption>
</figure>
"""
        for img, label, location, desc in rows
    )


def service_cards() -> str:
    return "".join(
        f"""
<article class="service-card">
  <div class="service-icon" aria-hidden="true"></div>
  <h3>{svc['name']}</h3>
  <p>{svc['summary']}</p>
  <a href="/services/{svc['slug']}">Learn More →</a>
</article>
"""
        for svc in SERVICES
    )


def service_list_cards() -> str:
    return "".join(
        f"""
<article class="service-card">
  <h2>{svc['name']}</h2>
  <p>{svc['summary']} We provide scaffolding Essex coverage from Benfleet and nearby towns. Get a free quote today.</p>
  <a href="/services/{svc['slug']}">Read more about {svc['name'].lower()}</a>
</article>
"""
        for svc in SERVICES
    )


def area_pills() -> str:
    return "".join(
        f'<li><a class="area-pill-link" href="/areas/{data["slug"]}">{name}</a></li>'
        for name, data in AREA_DATA.items()
    )


def testimonials() -> str:
    entries = [
        (
            "They turned up on time and completed the work efficiently. The tower was exactly as our builder requested.",
            "Sally M.",
            "/images/icons/google-badge.svg",
            "Google review",
            "Google Review",
        ),
        (
            "Ashley and his team were professional throughout: on time, polite and great value for our project.",
            "Hannah M.",
            "/images/icons/verified-badge.svg",
            "Verified review",
            "Verified Review",
        ),
        (
            "Quick, efficient and friendly. Great communication throughout and they met every requirement we had.",
            "Jason R.",
            "/images/icons/bark-badge.svg",
            "Bark.com review",
            "Bark.com Review",
        ),
        (
            "Very professional setup, clear communication and tidy dismantling at the end of works.",
            "Verified Customer",
            "/images/icons/bark-badge.svg",
            "Bark.com review",
            "Bark.com Review",
        ),
    ]
    return "".join(
        f"""
<div class="testimonial-card">
  <div class="review-stars" aria-label="5 out of 5 stars">
    <span aria-hidden="true">★★★★★</span>
  </div>
  <blockquote class="review-text">
    "{text}"
  </blockquote>
  <div class="reviewer-info">
    <span class="reviewer-name">{name}</span>
    <span class="review-source">
      <img src="{badge_icon}" alt="{badge_alt}" width="16" height="16">
      {platform}
    </span>
  </div>
</div>
"""
        for text, name, badge_icon, badge_alt, platform in entries
    )


def homepage() -> str:
    return f"""
<section class="hero" id="top">
  <img class="hero-media"
       src="/images/hero-bg.webp"
       srcset="/images/hero-bg-480w.webp 480w, /images/hero-bg-768w.webp 768w, /images/hero-bg-1024w.webp 1024w, /images/hero-bg-1440w.webp 1440w, /images/hero-bg.webp 1920w"
       sizes="100vw"
       alt="Scaffolding erected on a residential property in South Essex by Axis Scaffolding Ltd"
       width="1920" height="1280" loading="eager" fetchpriority="high" decoding="async">
  <div class="hero-overlay"></div>
  <div class="hero-hex" aria-hidden="true"></div>
  <div class="container hero-content">
    <h1>Scaffolding in Essex for Homes, Roofers, Builders &amp; Commercial Projects</h1>
    <p>Safe, fully qualified scaffolding across South Essex and surrounding areas. Free quotes. Fast response.</p>
    <div class="hero-cta-row">
      <a class="btn btn-primary btn-hero-call" href="tel:{NAP['phone_e164']}">Call {NAP['phone']}</a>
      <a class="btn btn-outline" href="/quote">Get a Free Quote</a>
    </div>
    <div class="hero-trust-badges" aria-label="Trust credentials">
      <span>CISRS Qualified</span>
      <span>Fully Insured</span>
      <span>10+ Years' Experience</span>
      <span>Free Quotes</span>
    </div>
  </div>
</section>

<section class="section section-light decision-section" aria-labelledby="decision-heading">
  <div class="container">
    <h2 id="decision-heading">What are you working on?</h2>
    <p class="section-intro">Pick the option closest to your project and we'll point you to the right place.</p>
    <div class="decision-grid">
      <a href="/services/residential-scaffolding" class="decision-card">
        <div class="decision-icon" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 9.5L12 3l9 6.5V20a1 1 0 01-1 1H4a1 1 0 01-1-1V9.5z"/><path d="M9 21V12h6v9"/></svg></div>
        <h3>Homeowner</h3>
        <p>Roofing &middot; rendering &middot; extensions &middot; chimneys</p>
        <span class="decision-link" aria-hidden="true">Find out more &rarr;</span>
      </a>
      <a href="/contractors" class="decision-card">
        <div class="decision-icon" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="7" width="20" height="14" rx="1"/><path d="M16 7V5a2 2 0 00-2-2h-4a2 2 0 00-2 2v2"/><line x1="12" y1="12" x2="12" y2="16"/><line x1="10" y1="14" x2="14" y2="14"/></svg></div>
        <h3>Builder / Roofer</h3>
        <p>Access scaffold &middot; trade support &middot; fast turnaround</p>
        <span class="decision-link" aria-hidden="true">For contractors &rarr;</span>
      </a>
      <a href="/contractors" class="decision-card">
        <div class="decision-icon" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="1"/><path d="M3 9h18M9 21V9"/></svg></div>
        <h3>Commercial</h3>
        <p>Sites &middot; offices &middot; retail &middot; schools &middot; developments</p>
        <span class="decision-link" aria-hidden="true">For contractors &rarr;</span>
      </a>
      <a href="/services/emergency-scaffolding" class="decision-card decision-card-urgent">
        <div class="decision-icon" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M10.29 3.86L1.82 18a2 2 0 001.71 3h16.94a2 2 0 001.71-3L13.71 3.86a2 2 0 00-3.42 0z"/><line x1="12" y1="9" x2="12" y2="13"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg></div>
        <h3>Emergency</h3>
        <p>Storm damage &middot; urgent access &middot; temporary protection</p>
        <span class="decision-link" aria-hidden="true">Call us now &rarr;</span>
      </a>
      <a href="/contact" class="decision-card decision-card-open">
        <div class="decision-icon" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M9.5 9a2.5 2.5 0 015 0c0 1.5-2.5 2-2.5 3.5"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg></div>
        <h3>Not Sure</h3>
        <p>Tell us what you're doing and we'll point you in the right direction.</p>
        <span class="decision-link" aria-hidden="true">Get in touch &rarr;</span>
      </a>
    </div>
  </div>
</section>

<section class="section" aria-labelledby="process-heading">
  <div class="container">
    <h2 id="process-heading">How It Works</h2>
    <p class="section-intro">From your first call to final dismantling — here is what to expect when you work with Axis Scaffolding.</p>
    <ol class="process-steps">
      <li class="process-step"><span class="process-num" aria-hidden="true">1</span><div><h3>Tell us about your project</h3><p>Call <a href="tel:{NAP['phone_e164']}">{NAP['phone']}</a> or complete the short quote form. Tell us what work you are having done, your address and when you need access.</p></div></li>
      <li class="process-step"><span class="process-num" aria-hidden="true">2</span><div><h3>We assess the requirements</h3><p>We establish property and site access, the right scaffold type, any access constraints and your timeline. We advise on highway licence requirements if relevant.</p></div></li>
      <li class="process-step"><span class="process-num" aria-hidden="true">3</span><div><h3>You receive a clear quote</h3><p>We aim to respond to all quote requests the same working day. Your quote is clear and no-obligation — no hidden extras.</p></div></li>
      <li class="process-step"><span class="process-num" aria-hidden="true">4</span><div><h3>We erect safely and on time</h3><p>Our CISRS-qualified team installs the agreed scaffold, working around your roofer, builder or site schedule.</p></div></li>
      <li class="process-step"><span class="process-num" aria-hidden="true">5</span><div><h3>We dismantle and leave you tidy</h3><p>Once your work is finished, we return promptly to dismantle and remove all scaffold. Tidy handover — no materials left on site.</p></div></li>
    </ol>
  </div>
</section>

<section class="section section-light" aria-labelledby="services-heading">
  <div class="container">
    <h2 id="services-heading">Our Scaffolding Services</h2>
    <div class="services-grid">{service_cards()}</div>
  </div>
</section>

<section class="section" aria-labelledby="why-axis-heading">
  <div class="container split-grid">
    <div>
      <img src="/images/project-7.webp" alt="Domestic scaffolding structure erected beside a home in Benfleet, Essex by Axis Scaffolding Ltd" width="640" height="800" loading="lazy" decoding="async" class="rounded-image">
    </div>
    <div>
      <h2 id="why-axis-heading">Why Builders &amp; Homeowners Choose Axis</h2>
      <ul class="usp-list usp-evidence">
        <li><strong>CISRS Qualified</strong><span>Our scaffolders hold current CISRS qualifications — the UK industry standard for trained scaffold professionals. Your installation is carried out to a recognised national standard.</span></li>
        <li><strong>Fully Insured</strong><span>Public liability insurance in place. Added protection for your property and project.</span></li>
        <li><strong>10+ Years' Experience</strong><span>Founder-led local operation with over a decade of scaffolding experience across residential and commercial work in South Essex.</span></li>
        <li><strong>Same-Day Quote Response</strong><span>We aim to respond to all quote requests within the same working day. Emergency enquiries are prioritised — call <a href="tel:{NAP['phone_e164']}">{NAP['phone']}</a>.</span></li>
        <li><strong>RAMS Available</strong><span>Risk assessments and method statements available for commercial sites and principal contractors requiring documentation.</span></li>
      </ul>
      <a class="btn btn-primary" href="/quote">Get a Free Quote</a>
    </div>
  </div>
</section>

<section class="section section-dark" aria-labelledby="projects-heading">
  <div class="container">
    <h2 id="projects-heading">Recent Projects</h2>
    <div class="projects-grid">{project_cards()}</div>
    <p class="centered"><a class="btn btn-outline-orange" href="/gallery">View All Projects &rarr;</a></p>
  </div>
</section>

<section class="section section-light" aria-labelledby="reviews-heading">
  <div class="container">
    <h2 id="reviews-heading">What Our Customers Say</h2>
    <div class="testimonial-carousel" id="testimonial-carousel" aria-live="polite">
      <div class="testimonial-track" id="testimonial-track">{testimonials()}</div>
    </div>
    <p class="centered review-source-note" style="font-size:0.85rem; color:#6b7280; margin-top:1rem;">Reviews sourced from Google, Bark.com and verified customers. <a href="https://maps.google.com/?q=Axis+Scaffolding+Rayleigh+Essex" target="_blank" rel="noopener noreferrer">Leave a Google review</a></p>
  </div>
</section>

<section class="section" id="areas-covered" aria-labelledby="areas-heading">
  <div class="container">
    <h2 id="areas-heading">Areas We Cover in Essex</h2>
    <p>Axis Scaffolding Ltd provides domestic, residential and commercial scaffolding in Rayleigh, Benfleet, Canvey Island, Southend-on-Sea, Basildon, Chelmsford, Wickford, Hadleigh, Leigh-on-Sea, Thundersley, Hockley and Rochford. Contact us to confirm coverage for your specific location.</p>
    <ul class="area-pills">{area_pills()}</ul>
  </div>
</section>

<section class="section section-light" aria-labelledby="pricing-heading">
  <div class="container">
    <h2 id="pricing-heading">How Much Does Scaffolding Cost in Essex?</h2>
    <p class="direct-answer">Residential scaffolding in Essex typically starts from around &pound;300&ndash;&pound;500 for smaller jobs, rising to &pound;1,500 or more for full roof scaffolds on larger properties.</p>
    <h3>What affects the price?</h3>
    <ul class="pricing-factors">
      <li>Scaffold height and the number of elevations required</li>
      <li>Footprint and overall scaffold size</li>
      <li>Site access — narrow driveways, close neighbours, restricted entry</li>
      <li>Whether a pavement or highway licence is required</li>
      <li>Duration of hire</li>
      <li>Temporary roofing requirement</li>
    </ul>
    <p>We provide free, no-obligation quotations. Call <a href="tel:{NAP['phone_e164']}">{NAP['phone']}</a> or complete the quote form below.</p>
  </div>
</section>

<section class="section" aria-labelledby="quote-heading">
  <div class="container">
    <h2 id="quote-heading">Get a Free Scaffolding Quote</h2>
    {quote_form("home", "Tell us about your project")}
  </div>
</section>

<section class="section section-light" aria-labelledby="faq-heading">
  <div class="container faq-wrap">
    <h2 id="faq-heading">Frequently Asked Questions</h2>
    {faq_accordion()}
  </div>
</section>

<section class="cta-banner">
  <div class="container cta-banner-inner">
    <div>
      <h2>Need Scaffolding in Essex?</h2>
      <p>Free quote &middot; Fast response &middot; CISRS qualified</p>
    </div>
    <div class="hero-cta-row">
      <a class="btn btn-light" href="tel:{NAP['phone_e164']}">{NAP['phone']}</a>
      <a class="btn btn-dark" href="/quote">Request a Quote</a>
    </div>
  </div>
</section>

<section class="connect-section">
  <div class="connect-inner">
    <h2>Connect With Us</h2>
    <p>Follow Axis Scaffolding for project updates, behind-the-scenes content and the latest news from our team across Essex.</p>
    <div class="social-links">
      <a href="https://www.facebook.com/Axisscaffoldingltd/" target="_blank" rel="noopener noreferrer" class="social-card" aria-label="Follow Axis Scaffolding on Facebook">
        <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M22 12.06C22 6.5 17.52 2 12 2S2 6.5 2 12.06c0 5.02 3.66 9.18 8.44 9.94v-7.03H7.9v-2.9h2.54V9.84c0-2.52 1.49-3.92 3.77-3.92 1.09 0 2.23.2 2.23.2v2.47h-1.25c-1.24 0-1.62.77-1.62 1.56v1.87h2.75l-.44 2.9h-2.31V22c4.78-.76 8.44-4.92 8.44-9.94Z"/></svg>
        <span>Facebook</span>
        <small>@Axisscaffoldingltd</small>
      </a>
      <a href="https://www.instagram.com/axis_scaffoldingessex/" target="_blank" rel="noopener noreferrer" class="social-card" aria-label="Follow Axis Scaffolding on Instagram">
        <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M7.75 2h8.5A5.76 5.76 0 0 1 22 7.75v8.5A5.76 5.76 0 0 1 16.25 22h-8.5A5.76 5.76 0 0 1 2 16.25v-8.5A5.76 5.76 0 0 1 7.75 2Zm0 1.8A3.95 3.95 0 0 0 3.8 7.75v8.5a3.95 3.95 0 0 0 3.95 3.95h8.5a3.95 3.95 0 0 0 3.95-3.95v-8.5a3.95 3.95 0 0 0-3.95-3.95h-8.5Zm8.9 1.35a1.2 1.2 0 1 1 0 2.4 1.2 1.2 0 0 1 0-2.4ZM12 7a5 5 0 1 1 0 10 5 5 0 0 1 0-10Zm0 1.8A3.2 3.2 0 1 0 12 15.2 3.2 3.2 0 0 0 12 8.8Z"/></svg>
        <span>Instagram</span>
        <small>@axis_scaffoldingessex</small>
      </a>
      <a href="https://maps.google.com/?q=Arterial+Road+Rayleigh+Essex+SS6+7XT" target="_blank" rel="noopener noreferrer" class="social-card" aria-label="Find Axis Scaffolding on Google">
        <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2a7 7 0 0 1 7 7c0 5.03-7 13-7 13S5 14.03 5 9a7 7 0 0 1 7-7Zm0 3.1A3.9 3.9 0 1 0 12 12.9 3.9 3.9 0 0 0 12 5.1Z"/></svg>
        <span>Google</span>
        <small>Leave us a review</small>
      </a>
    </div>
  </div>
</section>
"""


def inner_hero(path_items: list[tuple[str, str]], h1: str, intro: str) -> str:
    return f"""
<section class="inner-hero">
  <div class="container">
    {breadcrumb_nav(path_items)}
    <h1>{h1}</h1>
    <p>{intro}</p>
  </div>
</section>
"""


SERVICE_DETAIL: dict[str, dict] = {
    "residential-scaffolding": {
        "h1": "Residential Scaffolding in Essex",
        "who_for_detail": "Homeowners planning extensions, full roof replacements, rendering, chimney repairs or major exterior improvements on houses and flats across South Essex.",
        "whats_included": [
            "Site assessment and scaffold design tailored to your property",
            "Installation by CISRS-qualified operatives",
            "Scaffold boards, guardrails and toe boards for safe access",
            "Routine safety checks throughout the hire period",
            "Prompt dismantling and full site clearance on completion",
            "Highway licence application support where a pavement licence is required",
        ],
        "pricing": "Residential scaffolding in Essex typically starts from £300–£500 for smaller access jobs (chimney, single elevation) and rises to £1,200–£2,000+ for full four-elevation roof scaffolds on larger detached properties. Pricing depends on scaffold height, footprint, number of elevations, access constraints, duration and whether a highway licence is needed.",
        "process_steps": [
            ("Tell us about your project", "Call 01702 820468 or complete the quote form with your address, the work being done and your required dates."),
            ("We assess and quote", "We evaluate access, scaffold type, height and any licence requirements. You receive a clear, itemised quote — usually same day."),
            ("Scaffold is erected", "Our CISRS-qualified team erects to the agreed specification, coordinating with your roofer or builder."),
            ("Works proceed safely", "The scaffold is checked regularly. We can adjust if your project scope changes."),
            ("Dismantling and clear-up", "Once works are complete, we return promptly to dismantle and remove all scaffold materials."),
        ],
        "faqs": [
            ("How much does residential scaffolding cost in Essex?", "For most homes in South Essex, expect £300–£500 for a single-elevation access scaffold and £1,200–£2,000+ for a full roof scaffold on a larger property. We provide itemised, no-obligation quotes."),
            ("Do I need a licence for scaffolding on my driveway?", "A licence is only required if scaffold overhangs or occupies a public highway (road or pavement). Scaffold within your private property boundary does not require a licence. We advise on this when we quote."),
            ("How long does it take to erect residential scaffolding?", "Most standard residential scaffolds are erected in half a day to a full day depending on size. We aim to fit your builder or roofer's schedule."),
            ("Will you protect my driveway and garden?", "Yes. Base plates and scaffold boards are used to distribute load. If you have a block-paved or resin driveway, let us know when you enquire so we can plan appropriately."),
        ],
        "cta_label": "Need scaffolding for your home?",
    },
    "commercial-scaffolding": {
        "h1": "Commercial Scaffolding in Essex",
        "who_for_detail": "Builders, principal contractors, developers, property managers and commercial premises including offices, retail units, schools and industrial buildings requiring planned scaffold access.",
        "whats_included": [
            "Pre-contract site survey and scaffold design",
            "Risk assessments and method statements (RAMS) available on request",
            "Installation by CISRS-qualified operatives to TG20 or bespoke design",
            "Loading bay scaffold integration where materials handling is required",
            "Regular statutory inspections and handover certificates",
            "Long-term hire arrangements to match project programmes",
            "Site communication and coordination with principal contractors",
        ],
        "pricing": "Commercial scaffolding pricing depends on the scale and complexity of the project, duration, access constraints and documentation requirements. We quote competitively for both one-off commercial contracts and ongoing site relationships. Call 01702 820468 to discuss your project and receive a detailed quotation.",
        "process_steps": [
            ("Initial enquiry and site review", "Contact us with your project details, site address and programme. We carry out a site survey to understand access, scale and documentation requirements."),
            ("RAMS and quotation", "We provide risk assessments, method statements and a detailed quotation aligned to your programme."),
            ("Scaffold installation", "CISRS-qualified operatives erect to specification with full handover documentation and a scaffold inspection certificate."),
            ("Programme management", "We check the scaffold regularly and adapt to programme changes. Loading bays can be integrated at any stage."),
            ("Strike and clearance", "Scaffold is struck promptly once your programme allows, with full site clearance and waste removal."),
        ],
        "faqs": [
            ("Do you provide RAMS for commercial scaffolding?", "Yes. Risk assessments and method statements are available for all commercial projects. These can be tailored to your principal contractor's requirements."),
            ("Can you integrate a loading bay into the scaffold?", "Yes. Loading bays for safe materials handling can be incorporated into the scaffold design from the outset or added during the project."),
            ("Do you offer long-term scaffold hire for large developments?", "Yes. We work with developers and contractors on extended programmes. Long-term hire rates and dedicated account management are available — contact us to discuss."),
            ("Are you familiar with working on occupied commercial premises?", "Yes. We are experienced working on occupied retail units, offices and schools where phased access and minimal disruption are priorities."),
        ],
        "cta_label": "Need a scaffold package for your site?",
    },
    "domestic-scaffolding": {
        "h1": "Domestic Scaffolding in Essex",
        "who_for_detail": "Homeowners in occupied properties requiring short-term scaffold access for routine repairs, painting, chimney work, guttering replacement or fascia and soffit maintenance.",
        "whats_included": [
            "Site survey to confirm scaffold type and safe access route",
            "Installation by CISRS-qualified operatives",
            "Scaffold designed to minimise impact on the property and neighbours",
            "Safety checks throughout the hire period",
            "Prompt dismantling and removal on completion",
        ],
        "pricing": "Domestic scaffolding for shorter-term access jobs in Essex typically starts from around £300 for a simple single-elevation setup. Chimney scaffolds, two-elevation setups or scaffolds with difficult access will cost more. We provide clear, no-obligation quotes.",
        "process_steps": [
            ("Describe your job", "Call 01702 820468 or use the quote form. Tell us the property address, what work is being done and your required dates."),
            ("We assess and quote", "We confirm scaffold type, safe access and any constraints. You receive a clear quote — usually same day."),
            ("Installation", "Our team erects the scaffold efficiently, minimising disruption to you, your family and neighbours."),
            ("Work proceeds", "Your tradesperson completes the work with safe scaffold access throughout."),
            ("Dismantling", "We return promptly to dismantle and clear once your work is done."),
        ],
        "faqs": [
            ("What is domestic scaffolding?", "Domestic scaffolding refers to shorter-term access scaffold erected at an occupied home for maintenance, repair or cosmetic work. It typically covers one or two elevations for a limited hire period."),
            ("How quickly can you erect domestic scaffolding?", "Most domestic scaffolding jobs in South Essex can be scheduled within 2–5 working days of a quote being approved."),
            ("Do you notify neighbours before erecting scaffold?", "We recommend homeowners notify immediate neighbours before erection, particularly where scaffold is close to boundaries. We work tidily and efficiently to minimise any inconvenience."),
        ],
        "cta_label": "Need domestic scaffold access?",
    },
    "roof-scaffolding": {
        "h1": "Roof Scaffolding in Essex",
        "who_for_detail": "Homeowners and roofing contractors requiring safe scaffold access to pitched or flat roofs for repairs, replacement, chimney work, ridge tiles, guttering or fascia and soffit replacement.",
        "whats_included": [
            "Roof-level scaffold designed for safe access to pitched and flat roofs",
            "Ridge board and eaves-level platforms as required",
            "Full guardrails, toe boards and edge protection",
            "Installation by CISRS-qualified operatives",
            "Safety checks throughout the hire period",
            "Dismantling and site clearance on completion",
        ],
        "pricing": "Roof scaffolding in Essex typically starts from £400–£600 for a single-pitch access scaffold on a standard semi-detached property, rising to £1,000–£2,000+ for detached houses, hipped roofs or properties requiring access to multiple elevations. Chimney scaffolds are priced individually based on height and access.",
        "process_steps": [
            ("Tell us about the roof job", "Call us or complete the quote form with your address, roof type and the work being carried out. A site visit may be required for complex roofs."),
            ("Quotation", "We confirm the scaffold design, height, number of elevations and any special requirements. You receive a clear, itemised quote."),
            ("Erection", "Our CISRS-qualified operatives erect roof-level scaffold to your roofer's specification, coordinating access around your programme."),
            ("Roofer access", "Your roofing contractor works safely at roof level with full edge protection throughout."),
            ("Dismantling", "Once roofing works are complete, we dismantle and remove all scaffold promptly."),
        ],
        "faqs": [
            ("Do I need scaffold for a roof repair?", "For any work at eaves height or above, scaffold is the safest access method. Work at roof level without proper scaffold creates serious fall risk and is not compliant with HSE guidance. Ladders alone are not adequate for most roof repair jobs."),
            ("Can you scaffold around a chimney?", "Yes. We design and erect chimney scaffolds for repointing, chimney rebuilds, flaunching repair and lead flashing work. Height and access route are assessed at the site visit or from photographs where the job is straightforward."),
            ("How long does roof scaffolding take to erect?", "A standard semi-detached or terraced house roof scaffold can typically be erected in half a day. Larger or more complex setups take a full day or more."),
            ("Do you work with roofing contractors directly?", "Yes. Many roofing contractors in Essex use Axis Scaffolding regularly. If you are a roofer looking for a reliable scaffold supply partner, call us to discuss rates and turnaround times."),
        ],
        "cta_label": "Need roof scaffolding for your project?",
    },
    "temporary-roofing": {
        "h1": "Temporary Roofing in Essex",
        "who_for_detail": "Builders, roofers and homeowners who need to protect an exposed structure from weather while roof replacement or major repair work is underway — typically over winter months or during extended roofing programmes.",
        "whats_included": [
            "Scaffold-supported temporary roof structure over the exposed area",
            "Polycarbonate or sheeted roof panels for weather protection",
            "Full edge protection and safe working platform beneath the structure",
            "Installation by CISRS-qualified operatives",
            "Regular inspections throughout the hire period",
            "Dismantling and removal on completion",
        ],
        "pricing": "Temporary roofing pricing depends on the span, pitch and complexity of the structure required, the duration of protection needed and site access conditions. It is always quoted in conjunction with the underlying scaffold. Call 01702 820468 to discuss your project.",
        "process_steps": [
            ("Describe the project", "Tell us the building type, roof area to be covered, duration and the roofing programme. We assess whether a temporary roof is required."),
            ("Design and quotation", "We design the temporary roof structure in conjunction with the underlying scaffold and provide a combined quotation."),
            ("Installation", "The scaffold and temporary roof are erected together. Your roofer can begin work in a weather-protected environment."),
            ("Works proceed", "Roofing works continue without weather delay. Inspections ensure the structure remains safe throughout."),
            ("Strike", "Both the temporary roof and scaffold are struck and removed once works are complete."),
        ],
        "faqs": [
            ("What is a temporary roof used for?", "A temporary roof is a scaffold-supported weatherproof structure erected over a property where the existing roof has been removed or is substantially open to the elements. It allows roofing works to continue regardless of weather and protects the building and its contents."),
            ("How long can a temporary roof remain in place?", "Temporary roofs can remain in place for the full duration of a roofing project — weeks or months if needed. Regular inspections ensure the structure remains safe and wind-resistant throughout."),
            ("Is a temporary roof always necessary for roof replacement?", "Not always. For straightforward strip-and-re-tile jobs on smaller properties, works can often be completed quickly without temporary weatherproofing. For larger projects, complex roofs or where weather risk is significant, a temporary roof is advisable."),
        ],
        "cta_label": "Need temporary weatherproofing for your roof project?",
    },
    "emergency-scaffolding": {
        "h1": "Emergency Scaffolding in Essex",
        "who_for_detail": "Anyone facing an urgent structural access need — storm-damaged roofs, structural instability, post-incident protection or emergency access requirements that cannot wait for a standard scheduling window.",
        "whats_included": [
            "Priority response for urgent enquiries — call 01702 820468",
            "Rapid site assessment to determine the scaffold required",
            "Same-day or next-day erection where operatives are available",
            "Temporary propping, debris protection and access scaffold as required",
            "Safety checks throughout the emergency hire period",
            "Liaison with loss adjusters or insurers on request",
        ],
        "pricing": "Emergency scaffolding is priced on the specific requirements of each situation. Out-of-hours and same-day attendance may carry a premium. Call 01702 820468 immediately for urgent requirements — we will give you a clear indication of cost and availability.",
        "process_steps": [
            ("Call us immediately", "For emergency scaffolding in Essex, call 01702 820468 directly. Do not use the form for urgent requirements."),
            ("Rapid assessment", "We assess the situation over the phone and, where necessary, attend site to determine what scaffold is required."),
            ("Priority erection", "We prioritise emergency jobs in our scheduling. Same-day or next-day erection where operatives are available."),
            ("Safe access or protection established", "The emergency scaffold provides immediate safe access, temporary protection or structural stabilisation as required."),
            ("Follow-on works", "Once the immediate risk is addressed, we can discuss longer-term scaffold hire for remediation works."),
        ],
        "faqs": [
            ("How quickly can you respond to an emergency?", "We prioritise emergency calls and aim to attend site or arrange erection as quickly as operatives are available. Call 01702 820468 directly — do not rely on the contact form for urgent situations."),
            ("What counts as an emergency scaffolding situation?", "Storm-damaged roofs with exposed structures, partial roof collapse, structural instability following an incident, fire or flood damage requiring safe access, or any situation where delay creates ongoing risk to life or property."),
            ("Do you work with insurance companies on emergency scaffold?", "Yes. We can liaise with loss adjusters and provide documentation to support insurance claims where required."),
        ],
        "cta_label": "Emergency? Call us now:",
        "cta_is_phone": True,
    },
    "dismantling-scaffolding": {
        "h1": "Scaffold Dismantling in Essex",
        "who_for_detail": "Anyone who needs an existing scaffold safely removed and the site left clear — including scaffolds erected by other contractors, scaffolds where the original company is no longer available, and all Axis Scaffolding installations at completion.",
        "whats_included": [
            "Safe dismantling of any scaffold system by CISRS-qualified operatives",
            "Removal of all scaffold materials, boards and fittings",
            "Tidy handover with the site left clear",
            "Works coordinated around your completion programme",
            "We can dismantle scaffolds erected by other contractors",
        ],
        "pricing": "Dismantling costs depend on scaffold size, complexity and site access. For Axis Scaffolding installations, dismantling is included as part of the hire agreement. For third-party scaffold removal, we provide a separate quotation.",
        "process_steps": [
            ("Contact us with details", "Tell us the scaffold size, location and who originally erected it (if known). Photographs help us assess the job remotely."),
            ("Quotation", "We provide a dismantling-only quotation if the scaffold was erected by another contractor."),
            ("Scheduled dismantling", "We attend site on the agreed date and dismantle safely and efficiently."),
            ("Site clearance", "All materials are removed and the site is left tidy."),
        ],
        "faqs": [
            ("Can you dismantle scaffold erected by another company?", "Yes. We dismantle scaffolds erected by other contractors across South Essex. Provide us with details or photographs and we will quote accordingly."),
            ("What if I don't know who erected the scaffold?", "That is not a problem. We assess the scaffold on site and dismantle it safely regardless of origin."),
            ("How quickly can scaffold be dismantled?", "Most domestic scaffolds can be dismantled in half a day. Larger commercial scaffolds take longer. We work to fit your completion programme."),
        ],
        "cta_label": "Need scaffold removed?",
    },
    "loading-bay-scaffolding": {
        "h1": "Loading Bay Scaffolding in Essex",
        "who_for_detail": "Builders and contractors on commercial or residential construction sites who need a safe, structured platform for receiving and distributing materials at height — reducing manual handling risk and improving site efficiency.",
        "whats_included": [
            "Scaffold-integrated loading bay platform designed for your site",
            "Rated and tested for materials loading requirements",
            "Gates, edge protection and safe access routes",
            "Coordination with site logistics and delivery programme",
            "Regular safety inspections throughout the project",
            "Dismantling and removal on strike",
        ],
        "pricing": "Loading bay pricing depends on platform size, load rating, height and integration with the surrounding scaffold. It is normally quoted as part of the wider scaffold package. Call 01702 820468 to discuss your site requirements.",
        "process_steps": [
            ("Describe the site and delivery needs", "Tell us your site, the scaffold scope and what materials you need to receive and distribute at height."),
            ("Design and quotation", "We design a loading bay integrated into the overall scaffold specification and include it in the site quotation."),
            ("Installation", "The loading bay is erected as part of the scaffold, tested and handed over with a scaffold inspection certificate."),
            ("Materials handling", "Deliveries are received and distributed safely at the loading bay throughout the project."),
            ("Strike", "The loading bay and scaffold are dismantled and removed on programme completion."),
        ],
        "faqs": [
            ("What is a loading bay scaffold?", "A loading bay is a scaffold-supported platform with a rated capacity for receiving and distributing materials at height. It typically includes gates, edge protection and a clear access route from the delivery point."),
            ("How much weight can a loading bay scaffold take?", "Rated capacity depends on the design. We specify the load rating at the design stage based on your materials handling requirements."),
            ("Can a loading bay be added to an existing scaffold?", "Yes. Loading bays can be incorporated into an existing scaffold installation where the structure allows. Contact us to arrange a site assessment."),
        ],
        "cta_label": "Need a loading bay for your site?",
    },
    "scaffold-supply-erection": {
        "h1": "Scaffold Supply and Erection in Essex",
        "who_for_detail": "Contractors and homeowners who need a complete, managed scaffold solution from a single point of contact — materials supply, qualified labour and site coordination included.",
        "whats_included": [
            "Supply of all scaffold materials: standards, ledgers, boards, fittings",
            "Erection by CISRS-qualified operatives",
            "Site coordination and programme planning",
            "Scaffold inspection certificate on handover",
            "Regular safety checks throughout the hire period",
            "Dismantling, removal and tidy handover on completion",
        ],
        "pricing": "Full supply-and-erect pricing depends on scaffold scope, materials quantity, duration and site access. We provide transparent, itemised quotations covering materials and labour. Call 01702 820468 or complete the quote form.",
        "process_steps": [
            ("Tell us your requirements", "Describe the project, site address, scaffold scope and programme. We assess materials and labour requirements."),
            ("Itemised quotation", "You receive a quotation covering both materials supply and erection labour — one invoice, one point of contact."),
            ("Delivery and erection", "Materials are delivered to site and the scaffold is erected by our CISRS-qualified team on the agreed date."),
            ("Handover", "We provide a scaffold inspection certificate and handover documentation."),
            ("Strike and removal", "At programme completion, we dismantle, remove all materials and leave the site clear."),
        ],
        "faqs": [
            ("What is the difference between scaffold supply-and-erect and labour-only?", "Supply-and-erect means we provide both the scaffold materials and the qualified operatives to erect them. Labour-only means the client supplies materials and we provide the erection team. Most of our clients use supply-and-erect for simplicity."),
            ("Do you supply scaffold materials for self-erect projects?", "We do not generally supply materials for self-erection. Scaffold erection requires CISRS-qualified operatives for safety and insurance reasons."),
            ("How quickly can you mobilise for a supply-and-erect job?", "Most South Essex jobs can be scheduled within 3–7 working days of quote approval, subject to current workload."),
        ],
        "cta_label": "Need a complete scaffold supply and erection package?",
    },
}


def service_detail_body(service: dict) -> str:
    slug = service["slug"]
    detail = SERVICE_DETAIL.get(slug, {})
    path = [("Home", "/"), ("Services", "/services"), (service["name"], f"/services/{slug}")]

    h1 = detail.get("h1", f"{service['name']} in Essex")
    who_for = detail.get("who_for_detail", service.get("who_for", ""))
    whats_included = detail.get("whats_included", [])
    pricing_text = detail.get("pricing", "")
    process_steps = detail.get("process_steps", [])
    faqs = detail.get("faqs", [])
    cta_label = detail.get("cta_label", f"Need {service['name'].lower()}?")
    cta_is_phone = detail.get("cta_is_phone", False)

    included_html = "".join(f"<li>{item}</li>" for item in whats_included) if whats_included else ""
    steps_html = "".join(
        f'<li class="process-step"><span class="process-num" aria-hidden="true">{i+1}</span><div><h3>{title}</h3><p>{desc}</p></div></li>'
        for i, (title, desc) in enumerate(process_steps)
    )
    faq_html = "".join(
        f"""<div class="faq-item"><button class="faq-question" id="sfaq-btn-{idx}" aria-expanded="{'true' if idx==0 else 'false'}" aria-controls="sfaq-panel-{idx}">{q}</button><div class="faq-answer" id="sfaq-panel-{idx}" role="region" aria-labelledby="sfaq-btn-{idx}" {'style="display:block;"' if idx==0 else ''}><p>{a}</p></div></div>"""
        for idx, (q, a) in enumerate(faqs)
    )

    if cta_is_phone:
        cta_buttons = f'<a class="btn btn-primary" href="tel:{NAP["phone_e164"]}">{NAP["phone"]}</a><a class="btn btn-outline" href="/quote">Request a Quote</a>'
    else:
        cta_buttons = f'<a class="btn btn-light" href="tel:{NAP["phone_e164"]}">{NAP["phone"]}</a><a class="btn btn-dark" href="/quote">Request a Quote</a>'

    return (
        inner_hero(path, h1, f"{service['summary']} Free, no-obligation quotes — call {NAP['phone']} or complete the form below.")
        + f"""
<section class="section section-light">
  <div class="container">
    <h2>Who Is This For?</h2>
    <p>{who_for}</p>
  </div>
</section>
"""
        + (f"""
<section class="section">
  <div class="container">
    <h2>What&rsquo;s Included</h2>
    <ul class="usp-list">{included_html}</ul>
  </div>
</section>
""" if included_html else "")
        + (f"""
<section class="section section-light">
  <div class="container">
    <h2>Pricing</h2>
    <p class="direct-answer">{pricing_text}</p>
  </div>
</section>
""" if pricing_text else "")
        + (f"""
<section class="section">
  <div class="container">
    <h2>How It Works</h2>
    <ol class="process-steps">{steps_html}</ol>
  </div>
</section>
""" if steps_html else "")
        + (f"""
<section class="section section-light">
  <div class="container faq-wrap">
    <h2>Frequently Asked Questions</h2>
    {faq_html}
  </div>
</section>
""" if faq_html else "")
        + f"""
<section class="section">
  <div class="container faq-wrap">
    <h2>General FAQs</h2>
    {faq_accordion()}
  </div>
</section>
<section class="cta-banner">
  <div class="container cta-banner-inner">
    <div>
      <h2>{cta_label}</h2>
      <p>CISRS qualified &middot; Fully insured &middot; Free quotes &middot; South Essex</p>
    </div>
    <div class="hero-cta-row">{cta_buttons}</div>
  </div>
</section>
"""
    )


AREA_DATA: dict[str, dict] = {
    "Benfleet": {
        "slug": "benfleet",
        "postcode": "SS7",
        "desc": "Scaffolding in Benfleet, Essex — residential, roof and commercial access by Axis Scaffolding Ltd. CISRS qualified. Free quotes — call 01702 820468.",
        "intro": "Axis Scaffolding Ltd provides residential, commercial and roof scaffolding in Benfleet, SS7. Based in nearby Rayleigh, we cover Benfleet and surrounding villages including Thundersley, Hadleigh and Canvey Island.",
        "housing": "Benfleet is predominantly a residential area with a mix of 1930s–1970s semi-detached and detached homes along roads such as Kents Hill Road, Vicarage Hill and the estates around Cemetery Corner. Many of these properties are reaching an age where roof replacements, chimney repointing and full exterior renders are common projects — all of which require scaffold access.",
        "typical_projects": "Typical scaffolding jobs in Benfleet include full roof replacements on detached and semi-detached houses, chimney scaffold for repointing and rebuild, single-elevation scaffold for fascia, soffit and guttering replacement, rendering scaffold for properties with pebbledash or sand-and-cement renders, and extension scaffold for rear and side additions.",
        "access": "Most residential streets in Benfleet are standard residential width with adequate access for a scaffold lorry. Properties along Kents Hill Road and on the Benfleet Hill area can require additional planning due to the slope and narrower road widths. We assess access at the site visit or from photographs before committing.",
        "nearby": ["Thundersley", "Hadleigh", "Canvey Island", "Rayleigh", "Leigh-on-Sea"],
    },
    "Canvey Island": {
        "slug": "canvey-island",
        "postcode": "SS8",
        "desc": "Scaffolding in Canvey Island, Essex — domestic, residential and commercial by Axis Scaffolding Ltd. CISRS qualified. Free quotes — call 01702 820468.",
        "intro": "Axis Scaffolding Ltd provides scaffolding services across Canvey Island, SS8. We cover the whole island including the seafront, residential estates and commercial areas from our Rayleigh base.",
        "housing": "Canvey Island has a dense residential character with a high proportion of bungalows, semi-detached houses and some larger detached properties. The flat terrain and largely standard street widths make scaffold access straightforward in most areas. Properties along Furtherwick Road, Long Road and the seafront streets are typical of the housing stock we work on regularly.",
        "typical_projects": "Common scaffolding jobs on Canvey Island include bungalow roof scaffolding (often requiring full perimeter access at a lower working height), chimney scaffold, render scaffold for properties with older pebbledash or Tyrolean finishes, and domestic maintenance scaffold for fascia and guttering replacement. Commercial scaffolding on the High Street and retail parade areas is also undertaken.",
        "access": "Canvey Island is accessed across the bridge and causeway, which we factor into scheduling. Most residential streets have good lorry access. Some bungalow plots with rear extensions or conservatories require careful scaffold planning to allow access around the full perimeter.",
        "nearby": ["Benfleet", "Hadleigh", "South Benfleet", "Thundersley"],
    },
    "Rayleigh": {
        "slug": "rayleigh",
        "postcode": "SS6",
        "desc": "Scaffolding in Rayleigh, Essex — residential, commercial and roof access by Axis Scaffolding Ltd. Local, CISRS qualified. Free quotes — call 01702 820468.",
        "intro": "Axis Scaffolding Ltd is based in Rayleigh, SS6 — making us the most local scaffolding company available for residential and commercial projects in the town.",
        "housing": "Rayleigh has a varied housing stock from Victorian and Edwardian terraces in the town centre area to post-war semi-detached and detached houses across the residential estates of Downhall Park, Rawreth and London Road. The older housing stock in particular generates steady demand for roof replacement, chimney repair and rendering scaffold.",
        "typical_projects": "Being locally based, we undertake a high volume of work in Rayleigh itself — full roof scaffolding, extension scaffold, render scaffold, chimney access and domestic maintenance scaffold. Commercial scaffolding on the High Street and in the industrial areas around Arterial Road is also a regular part of our work.",
        "access": "As locals, we have detailed knowledge of access points, parking restrictions and narrow streets throughout Rayleigh. The High Street area and some older residential streets require early-morning access or prior arrangement with the council for scaffold on pavements.",
        "nearby": ["Wickford", "Hockley", "Rochford", "Benfleet", "Chelmsford"],
    },
    "Southend-on-Sea": {
        "slug": "southend",
        "postcode": "SS1–SS2",
        "desc": "Scaffolding in Southend-on-Sea, Essex — residential, commercial and emergency access by Axis Scaffolding Ltd. CISRS qualified. Free quotes — call 01702 820468.",
        "intro": "Axis Scaffolding Ltd provides scaffolding across Southend-on-Sea, covering SS1, SS2 and surrounding areas. We handle domestic repairs, full residential roof scaffolding and commercial projects across the borough.",
        "housing": "Southend has a diverse housing stock including Victorian and Edwardian terraces close to the seafront and town centre, 1930s and post-war semi-detached houses in Leigh, Thorpe Bay and Eastwood, and a significant number of purpose-built flats. The older housing stock along roads such as Hamlet Court Road, Eastern Esplanade and in the Westcliff area generates regular demand for roof and chimney scaffold.",
        "typical_projects": "Roof scaffold for terraced and semi-detached houses, chimney scaffold in the older parts of town, render scaffold for Victorian and Edwardian properties, flat-roof scaffold for commercial and mixed-use buildings, and emergency scaffolding for storm-damaged roofs following sea-facing weather events.",
        "access": "Southend has a mix of good and restricted access. Seafront and town centre locations may require highway licences where scaffold extends over pavements. We advise on licence requirements as part of the quoting process. Residential streets in Westcliff, Leigh and Thorpe Bay generally have good lorry access.",
        "nearby": ["Leigh-on-Sea", "Rochford", "Rayleigh", "Benfleet"],
    },
    "Basildon": {
        "slug": "basildon",
        "postcode": "SS13–SS16",
        "desc": "Scaffolding in Basildon, Essex — residential, commercial and roof access by Axis Scaffolding Ltd. CISRS qualified. Free quotes — call 01702 820468.",
        "intro": "Axis Scaffolding Ltd covers Basildon and the surrounding areas including Laindon, Pitsea, Billericay and Wickford. We provide residential, commercial and emergency scaffolding across the SS13–SS16 postcode area.",
        "housing": "Basildon's housing stock reflects its origins as a post-war new town — a large proportion of properties are 1950s–1970s semi-detached and terraced houses across the Fryerns, Kingswood, Lee Chapel and Vange areas. These properties are now of an age where full roof replacements, chimney repairs and window and render projects are commonplace.",
        "typical_projects": "Full roof scaffold on post-war semi-detached and terraced houses, chimney scaffold, render scaffold for 1960s and 1970s properties with original pebbledash, extension scaffold across residential estates, and commercial scaffolding on Basildon town centre and the business parks around the A127.",
        "access": "Basildon's planned street layout generally provides good lorry access across most residential areas. Some of the earlier estate roads with parking areas close to boundaries require careful positioning.",
        "nearby": ["Wickford", "Benfleet", "Rayleigh", "Chelmsford"],
    },
    "Chelmsford": {
        "slug": "chelmsford",
        "postcode": "CM1–CM3",
        "desc": "Scaffolding in Chelmsford, Essex — residential, roof and commercial by Axis Scaffolding Ltd. CISRS qualified. Free quotes — call 01702 820468.",
        "intro": "Axis Scaffolding Ltd covers Chelmsford and surrounding villages including Galleywood, Sandon and Springfield. We provide residential and commercial scaffolding across the CM1 and CM2 postcode areas.",
        "housing": "Chelmsford has a mix of Victorian and Edwardian terraces in the city centre and inner suburbs, 1930s–1970s semi-detached and detached houses in areas such as Moulsham, Galleywood and Writtle, and more modern developments. The city's growth has created demand across all housing types for scaffold access.",
        "typical_projects": "Roof scaffold for detached and semi-detached houses, chimney scaffold for Victorian and Edwardian properties, extension scaffold for growing families, render and cladding scaffold for commercial and residential refurbishment, and commercial scaffolding around the city centre and business parks.",
        "access": "The city centre has parking and access restrictions that require early scheduling and, in some cases, highway licences for scaffold over pavements. Residential areas generally have good access. We confirm access requirements at the quotation stage.",
        "nearby": ["Rayleigh", "Wickford", "Basildon", "Rochford", "Hockley"],
    },
    "Wickford": {
        "slug": "wickford",
        "postcode": "SS11–SS12",
        "desc": "Scaffolding in Wickford, Essex — residential, roof and commercial access by Axis Scaffolding Ltd. CISRS qualified. Free quotes — call 01702 820468.",
        "intro": "Axis Scaffolding Ltd covers Wickford and surrounding villages from our Rayleigh base. We provide residential, domestic and commercial scaffolding across SS11 and SS12.",
        "housing": "Wickford is a predominantly residential market town with a mix of 1930s–1970s semi-detached and detached houses, particularly in the Runwell Road, Market Road and Nevendon areas. New developments on the outskirts are also active.",
        "typical_projects": "Full roof scaffold for residential properties, chimney access, render scaffold for older housing stock, domestic maintenance scaffold, and commercial scaffolding on the High Street and retail areas.",
        "access": "Most residential streets in Wickford have good lorry access. The High Street area may require early morning access and highway licences for scaffold over footpaths.",
        "nearby": ["Rayleigh", "Basildon", "Chelmsford", "Hockley"],
    },
    "Hadleigh": {
        "slug": "hadleigh",
        "postcode": "SS7",
        "desc": "Scaffolding in Hadleigh, Essex — domestic, residential and commercial by Axis Scaffolding Ltd. CISRS qualified. Free quotes — call 01702 820468.",
        "intro": "Axis Scaffolding Ltd provides scaffolding in Hadleigh, SS7. Our Rayleigh base means we are close to Hadleigh for fast response on domestic, residential and commercial scaffold requirements.",
        "housing": "Hadleigh has a mix of pre-war properties along the London Road and Chapel Lane areas, together with post-war semi-detached and detached houses across the residential streets between Hadleigh and Thundersley. Properties on the hillside around Castle Lane often require careful access planning due to gradient and restricted road widths.",
        "typical_projects": "Chimney and roof scaffold on older properties along London Road, residential roof replacement scaffold, render scaffold for 1930s and post-war properties, domestic maintenance scaffold for fascia and guttering, and occasional commercial scaffold on the High Street.",
        "access": "The hilly terrain in parts of Hadleigh, particularly around Castle Lane and the Scrub Lane area, can require additional planning. Lorry access is generally good in the flat residential areas.",
        "nearby": ["Benfleet", "Thundersley", "Leigh-on-Sea", "Canvey Island"],
    },
    "Leigh-on-Sea": {
        "slug": "leigh-on-sea",
        "postcode": "SS9",
        "desc": "Scaffolding in Leigh-on-Sea, Essex — residential, roof and domestic access by Axis Scaffolding Ltd. CISRS qualified. Free quotes — call 01702 820468.",
        "intro": "Axis Scaffolding Ltd covers Leigh-on-Sea across the SS9 postcode, from the Old Town area to Eastwood and Belfairs. We provide residential, domestic and commercial scaffolding throughout.",
        "housing": "Leigh-on-Sea has a particularly varied housing stock. Old Town Leigh contains Victorian fishermen's cottages and historic buildings that often require specialist scaffold approaches due to their age and tight access. The Broadway and surrounding streets have a mix of Edwardian and inter-war properties. Belfairs and Eastwood have predominantly post-war semi-detached and detached houses.",
        "typical_projects": "Old Town Leigh chimney and roof scaffold on historic properties (sometimes requiring highway licences for tight street access), residential roof scaffold across Leigh Hill and the Broadway area, render scaffold for Victorian and Edwardian properties, domestic maintenance scaffold, and commercial scaffolding on The Broadway.",
        "access": "Old Town Leigh has some of the most restricted access we encounter in South Essex — narrow roads, historic buildings and close neighbours require careful planning. We always assess these jobs in detail before committing. The residential streets in Belfairs and Eastwood have good access.",
        "nearby": ["Hadleigh", "Thundersley", "Southend-on-Sea", "Benfleet"],
    },
    "Thundersley": {
        "slug": "thundersley",
        "postcode": "SS7",
        "desc": "Scaffolding in Thundersley, Essex — residential, roof and domestic access by Axis Scaffolding Ltd. CISRS qualified. Free quotes — call 01702 820468.",
        "intro": "Axis Scaffolding Ltd covers Thundersley, SS7. We are based close by in Rayleigh and provide fast response for domestic, residential and commercial scaffold enquiries.",
        "housing": "Thundersley is a largely residential area with a mix of 1930s–1960s semi-detached and detached houses across the Church Road, Kenneth Road and Rushbottom Lane areas, together with some newer developments. The housing stock is at an age where roof replacements, chimney repairs and external improvement projects are common.",
        "typical_projects": "Residential roof scaffold, chimney access scaffold, domestic maintenance scaffold for fascia and guttering, render scaffold for 1930s and post-war properties, and extension scaffold for home improvements.",
        "access": "Residential streets in Thundersley generally have good access for a standard scaffold lorry. Some of the older estate roads with narrower widths require planning, which we assess at the site visit.",
        "nearby": ["Benfleet", "Hadleigh", "Rayleigh", "Canvey Island"],
    },
    "Hockley": {
        "slug": "hockley",
        "postcode": "SS5",
        "desc": "Scaffolding in Hockley, Essex — residential, roof and domestic access by Axis Scaffolding Ltd. CISRS qualified. Free quotes — call 01702 820468.",
        "intro": "Axis Scaffolding Ltd provides scaffolding in Hockley, SS5. Our Rayleigh base puts us within 10 minutes of most Hockley addresses for domestic, residential and commercial scaffold requirements.",
        "housing": "Hockley has a primarily residential character with a mix of inter-war semi-detached and detached houses along Main Road and the surrounding streets, together with newer developments in Hawkwell and Rochford Road areas. The wood areas and rural-edge properties can have longer access routes.",
        "typical_projects": "Residential roof scaffold, domestic chimney access, fascia and guttering scaffold, extension scaffold and occasional commercial scaffold on Main Road.",
        "access": "Most residential streets in Hockley have good access. Properties on rural roads beyond the main residential areas require a site assessment to confirm lorry access before quoting.",
        "nearby": ["Rayleigh", "Rochford", "Wickford", "Chelmsford"],
    },
    "Rochford": {
        "slug": "rochford",
        "postcode": "SS4",
        "desc": "Scaffolding in Rochford, Essex — residential, roof and domestic by Axis Scaffolding Ltd. CISRS qualified. Free quotes — call 01702 820468.",
        "intro": "Axis Scaffolding Ltd covers Rochford, SS4 — a short drive from our Rayleigh base. We provide residential, domestic and commercial scaffolding across the town and surrounding villages.",
        "housing": "Rochford town centre contains some of the oldest properties in South Essex, including a range of listed and historic buildings around the market square. The wider Rochford area has a mix of inter-war and post-war semi-detached and detached houses across the residential streets towards Stambridge and Hockley.",
        "typical_projects": "Chimney and roof scaffold on period town-centre properties, residential roof scaffold, domestic maintenance scaffold, render scaffold for older properties, and commercial scaffolding on the market square and nearby retail premises.",
        "access": "The historic town centre of Rochford has restricted access in places, with narrow roads and on-street parking. Highway licences may be required for scaffold over footpaths in the town centre. Residential areas surrounding the town generally have good lorry access.",
        "nearby": ["Rayleigh", "Hockley", "Southend-on-Sea", "Chelmsford"],
    },
}


def area_page_body(area_name: str, data: dict) -> str:
    nearby_links = " &bull; ".join(
        f'<a href="/contact">{n}</a>' for n in data.get("nearby", [])
    )
    return (
        inner_hero(
            [("Home", "/"), ("Areas", "/areas"), (area_name, f"/areas/{data['slug']}")],
            f"Scaffolding in {area_name}, Essex",
            data["intro"],
        )
        + f"""
<section class="section section-light">
  <div class="container">
    <h2>Housing and Properties in {area_name}</h2>
    <p>{data['housing']}</p>
    <h2>Typical Scaffolding Projects in {area_name}</h2>
    <p>{data['typical_projects']}</p>
  </div>
</section>

<section class="section">
  <div class="container">
    <h2>Site Access in {area_name}</h2>
    <p>{data['access']}</p>
    <h2>Nearby Areas We Also Cover</h2>
    <p>{nearby_links}</p>
    <p>We cover all of South Essex. <a href="/contact">Contact us</a> to confirm coverage for your specific location.</p>
  </div>
</section>

<section class="section section-light">
  <div class="container">
    <h2>Our Services in {area_name}</h2>
    <div class="services-grid">
      {"".join(f'<article class="service-card"><h3>{s["name"]}</h3><p>{s["summary"]}</p><a href="/services/{s["slug"]}">Learn more</a></article>' for s in SERVICES[:6])}
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <h2>Get a Free Quote in {area_name}</h2>
    {quote_form(f'area-{data["slug"]}', f'Request a Free Quote — {area_name}')}
  </div>
</section>

<section class="cta-banner">
  <div class="container cta-banner-inner">
    <div>
      <h2>Scaffolding in {area_name}?</h2>
      <p>Call us for a same-day quote &middot; CISRS qualified &middot; Free quotes</p>
    </div>
    <div class="hero-cta-row">
      <a class="btn btn-primary" href="tel:{NAP['phone_e164']}">{NAP['phone']}</a>
      <a class="btn btn-outline" href="/quote">Request a Quote</a>
    </div>
  </div>
</section>
"""
    )


def generate_pages() -> None:
    write(
        "index.html",
        render_page(
            title="Scaffolding Essex | Axis Scaffolding Ltd Rayleigh Team",
            desc="Axis Scaffolding delivers trusted scaffolding Essex support from Rayleigh for homes and businesses across Essex. Contact our team and get a free quote today.",
            path="/",
            body=homepage(),
            include_faq_schema=True,
            preload_hero=True,
        ),
    )

    services_body = (
        inner_hero(
            [("Home", "/"), ("Services", "/services")],
            "Scaffolding Services in Essex",
            "Axis Scaffolding Ltd provides complete scaffolding Essex services from Rayleigh for residential, domestic and commercial projects. Get a free quote today.",
        )
        + f"""
<section class="section section-light"><div class="container service-listing">{service_list_cards()}</div></section>
<section class="section section-light"><div class="container faq-wrap"><h2>Frequently Asked Questions</h2>{faq_accordion()}</div></section>
<section class="cta-banner"><div class="container cta-banner-inner"><div><h2>Need Scaffolding in Essex?</h2><p>Call us today for a free, no-obligation quote.</p></div><div class="hero-cta-row"><a class="btn btn-light" href="tel:{NAP['phone']}">{NAP['phone']}</a><a class="btn btn-dark" href="/quote">Request a Quote</a></div></div></section>
"""
    )
    write(
        "services/index.html",
        render_page(
            title="Scaffolding Services in Essex | Axis Scaffolding Team",
            desc="Explore scaffolding Essex services from Rayleigh including domestic, roof and emergency access by Axis Scaffolding. Contact us and get a free quote today.",
            path="/services",
            body=services_body,
            breadcrumb_items=[("Home", "/"), ("Services", "/services")],
            include_faq_schema=True,
        ),
    )

    for svc in SERVICES:
        write(
            f"services/{svc['slug']}/index.html",
            render_page(
                title=svc["title"],
                desc=svc["desc"],
                path=f"/services/{svc['slug']}",
                body=service_detail_body(svc),
                breadcrumb_items=[("Home", "/"), ("Services", "/services"), (svc["name"], f"/services/{svc['slug']}")],
            ),
        )

    gallery_body = (
        inner_hero(
            [("Home", "/"), ("Gallery", "/gallery")],
            "Scaffolding Projects Gallery",
            "View real scaffolding Essex projects completed from our Benfleet base. Explore domestic, commercial and roof access works, then get a free quote today.",
        )
        + f"""<section class="section section-dark"><div class="container"><h2>Our Recent Projects</h2><div class="projects-grid">{project_cards(full_gallery=True)}</div></div></section>"""
    )
    write(
        "gallery/index.html",
        render_page(
            title="Scaffolding Projects Gallery | Axis Scaffolding Essex",
            desc="Browse scaffolding Essex projects completed by Axis Scaffolding from Rayleigh across domestic and commercial sites. Review our work and get a free quote today.",
            path="/gallery",
            body=gallery_body,
            breadcrumb_items=[("Home", "/"), ("Gallery", "/gallery")],
        ),
    )

    about_body = (
        inner_hero(
            [("Home", "/"), ("About", "/about")],
            "About Axis Scaffolding Ltd",
            "Axis Scaffolding Ltd delivers scaffolding Essex services from Rayleigh with certified standards and practical project support. Contact us and get a free quote today.",
        )
        + """
<section class="section"><div class="container split-grid"><div><img src="/images/project-5.webp" alt="Roof scaffolding setup at a property in Benfleet, Essex" width="640" height="800" loading="lazy" decoding="async" class="rounded-image"></div><div><h2>Why Choose Axis Scaffolding Essex?</h2><p>Axis Scaffolding Ltd is a fully qualified, CISRS-certified scaffolding company based in Rayleigh, Essex, registered in England and Wales under Company Number 15050136.</p><p>We support residential, domestic and commercial projects with safe scaffold design, reliable communication and punctual site delivery throughout Essex.</p></div></div></section>
"""
    )
    write(
        "about/index.html",
        render_page(
            title="About Axis Scaffolding Ltd | Essex Scaffolders Team",
            desc="Learn about Axis Scaffolding in Rayleigh delivering scaffolding Essex support with CISRS certification and full insurance. Contact us for a free quote today.",
            path="/about",
            body=about_body,
            breadcrumb_items=[("Home", "/"), ("About", "/about")],
        ),
    )

    contact_body = (
        inner_hero(
            [("Home", "/"), ("Contact", "/contact")],
            "Contact Axis Scaffolding Essex",
            "Need scaffolding Essex support from Rayleigh? Call Axis Scaffolding or send your details for a fast response. Get a free quote today.",
        )
        + f"""
<section class="section"><div class="container two-col"><article class="contact-card"><h2>Contact Us</h2><p><strong>Name:</strong> Axis Scaffolding Ltd</p><p><strong>Phone:</strong> <a href="tel:+441702820468">01702 820468</a></p><p><strong>Email:</strong> <a href="mailto:axis-scaffolding@outlook.com">axis-scaffolding@outlook.com</a></p><p><strong>Address:</strong> Arterial Road, Rayleigh, Essex, SS6 7XT</p><p>Email us: <a href="mailto:axis-scaffolding@outlook.com" style="color:#c8cdd4;">axis-scaffolding@outlook.com</a></p></article>{quote_form("contact", "Request a Free Scaffolding Quote")}</div></section>
"""
    )
    write(
        "contact/index.html",
        render_page(
            title="Contact Axis Scaffolding Essex | Free Quote Support",
            desc="Contact Axis Scaffolding in Rayleigh for scaffolding Essex residential and commercial support. Speak to our team now and get a free quote today.",
            path="/contact",
            body=contact_body,
            breadcrumb_items=[("Home", "/"), ("Contact", "/contact")],
        ),
    )

    quote_body = (
        inner_hero(
            [("Home", "/"), ("Quote", "/quote")],
            "Get a Free Scaffolding Quote",
            "Request scaffolding Essex pricing from our Benfleet team for domestic, commercial and emergency access projects. Get a free quote today.",
        )
        + f"""<section class="section section-light"><div class="container">{quote_form("quote", "Request Your Free Quote")}</div></section>"""
    )
    write(
        "quote/index.html",
        render_page(
            title="Get a Free Scaffolding Quote | Axis Scaffolding Essex",
            desc="Request scaffolding Essex pricing from Axis Scaffolding in Rayleigh for home and business projects. Complete the form now and get a free quote today.",
            path="/quote",
            body=quote_body,
            breadcrumb_items=[("Home", "/"), ("Quote", "/quote")],
        ),
    )

    policy_defs = [
        (
            "privacy-policy",
            "Privacy Policy | Axis Scaffolding Essex Rayleigh Team",
            "Read how Axis Scaffolding in Benfleet handles personal data for scaffolding Essex enquiries and projects. Review our policy and get a free quote today.",
            "Privacy Policy",
        ),
        (
            "terms-and-conditions",
            "Terms and Conditions | Axis Scaffolding Essex Team UK",
            "Review Axis Scaffolding terms for Benfleet and scaffolding Essex services including quotations and payment terms. Contact us and get a free quote today.",
            "Terms and Conditions",
        ),
        (
            "cookie-policy",
            "Cookie Policy | Axis Scaffolding Essex Rayleigh Team",
            "Understand how Axis Scaffolding uses cookies on this Benfleet scaffolding Essex website. Manage preferences anytime and get a free quote today.",
            "Cookie Policy",
        ),
    ]
    for slug, title, desc, heading in policy_defs:
        body = (
            inner_hero([("Home", "/"), (heading, f"/{slug}")], heading, f"Axis Scaffolding Ltd provides transparent legal and privacy information for Benfleet and scaffolding Essex customers.")
            + f"""<section class="section"><div class="container"><h2>Policy Information</h2><p>This page explains our {heading.lower()} for Axis Scaffolding Ltd services delivered from Rayleigh across Essex. If you need clarification, please contact our team directly by phone or email.</p></div></section>"""
        )
        write(
            f"{slug}/index.html",
            render_page(
                title=title,
                desc=desc,
                path=f"/{slug}",
                body=body,
                breadcrumb_items=[("Home", "/"), (heading, f"/{slug}")],
            ),
        )


    # ── Guide pages ──────────────────────────────────────────────────────────
    cost_guide_body = (
        inner_hero(
            [("Home", "/"), ("Guides", "/guides"), ("Scaffolding Cost in Essex", "/guides/scaffolding-cost-essex")],
            "How Much Does Scaffolding Cost in Essex?",
            "A straightforward guide to scaffolding prices in Essex — what affects the cost, typical price ranges for common jobs, and how to get an accurate quote from Axis Scaffolding Ltd.",
        )
        + f"""
<section class="section section-light">
  <div class="container direct-answer">
    <h2>The Short Answer</h2>
    <p>Residential scaffolding in Essex typically costs <strong>£350–£600</strong> for smaller single-elevation domestic jobs and <strong>£800–£2,500+</strong> for full roof scaffolding on larger properties. Commercial and multi-storey scaffolding is priced individually. Every job is different — the only reliable figure is a quote from a scaffolder who has assessed your specific project.</p>
    <div class="hero-cta-row" style="margin-top:1.5rem;">
      <a class="btn btn-primary" href="tel:{NAP['phone_e164']}">{NAP['phone']}</a>
      <a class="btn btn-outline" href="/quote">Get a Free Quote</a>
    </div>
  </div>
</section>

<section class="section section-dark">
  <div class="container">
    <h2>What Affects the Cost of Scaffolding?</h2>
    <div class="decision-grid">
      <div class="decision-card">
        <h3>Size and Height</h3>
        <p>More scaffold tubes, boards and fittings means more cost. A single-storey rear elevation is much cheaper than a full three-storey perimeter scaffold.</p>
      </div>
      <div class="decision-card">
        <h3>Number of Elevations</h3>
        <p>A single front-of-house scaffold is cheaper than wrapping all four sides of a property. Chimney scaffold typically involves only a small working platform.</p>
      </div>
      <div class="decision-card">
        <h3>Duration on Hire</h3>
        <p>Scaffolding is usually priced for a set hire period (often two to four weeks for domestic jobs). Extended hire increases cost — plan your trades to reduce standing time.</p>
      </div>
      <div class="decision-card">
        <h3>Site Access</h3>
        <p>Difficult access — narrow gates, slopes, restricted roads — takes longer to erect and may require specialist equipment or licences, affecting price.</p>
      </div>
      <div class="decision-card">
        <h3>Highway Licence</h3>
        <p>If scaffold extends over a public pavement or road, a Section 169 licence is required from Essex Highways. Licence fees vary by council and add to the overall cost.</p>
      </div>
      <div class="decision-card">
        <h3>Temporary Roofing</h3>
        <p>If your project needs weatherproof cover during works (e.g. roof replacement in autumn or winter), a temporary scaffold roof adds to the overall package cost.</p>
      </div>
    </div>
  </div>
</section>

<section class="section section-light">
  <div class="container">
    <h2>Typical Scaffolding Prices — Essex Guide</h2>
    <p style="color:var(--text-muted); margin-bottom:1.5rem;">These are indicative ranges only. Your quote may differ depending on the factors above.</p>
    <div class="decision-grid">
      <div class="decision-card"><h3>Chimney Scaffold</h3><p><strong>£350–£600</strong><br>Single-stack access platform, typically 1–2 week hire.</p></div>
      <div class="decision-card"><h3>Single Elevation Scaffold</h3><p><strong>£400–£900</strong><br>One face of a house for rendering, fascias or guttering.</p></div>
      <div class="decision-card"><h3>Full Roof Scaffold</h3><p><strong>£800–£1,800</strong><br>Full perimeter scaffold for roof replacement on a standard semi or detached.</p></div>
      <div class="decision-card"><h3>Extension Scaffold</h3><p><strong>£500–£1,200</strong><br>Side or rear scaffold for extension builds, typically 4–8 weeks hire.</p></div>
      <div class="decision-card"><h3>Commercial Scaffold</h3><p><strong>Individually quoted</strong><br>Multi-storey, loading bays, complex access and commercial refurbishments.</p></div>
      <div class="decision-card"><h3>Temporary Roofing</h3><p><strong>Additional cost</strong><br>Added to a scaffold package — price depends on span and duration.</p></div>
    </div>
  </div>
</section>

<section class="section section-dark">
  <div class="container">
    <h2>How to Get an Accurate Quote</h2>
    <div class="process-steps">
      <div class="process-step"><div class="process-num">1</div><div><h3>Describe Your Project</h3><p>Tell us the job type, property size and approximate height. Photos of the property and access help us prepare a more accurate figure faster.</p></div></div>
      <div class="process-step"><div class="process-num">2</div><div><h3>Site Visit If Needed</h3><p>For complex jobs we will arrange a brief site visit before quoting. For most standard residential jobs, we can quote from photos and a description.</p></div></div>
      <div class="process-step"><div class="process-num">3</div><div><h3>Receive Your Quote</h3><p>We provide clear, itemised quotations. No hidden charges. If a highway licence is required we will include it and advise on the process.</p></div></div>
    </div>
    <div class="hero-cta-row" style="margin-top:2rem;">
      <a class="btn btn-primary" href="/quote">Request a Free Quote</a>
      <a class="btn btn-outline" href="tel:{NAP['phone_e164']}">Call {NAP['phone']}</a>
    </div>
  </div>
</section>
"""
    )
    write(
        "guides/scaffolding-cost-essex/index.html",
        render_page(
            title="How Much Does Scaffolding Cost in Essex? | Axis Scaffolding",
            desc="Scaffolding cost guide for Essex homeowners and contractors. Typical price ranges for domestic, roof, chimney and commercial scaffolding — with a free quote from Axis Scaffolding.",
            path="/guides/scaffolding-cost-essex",
            body=cost_guide_body,
            breadcrumb_items=[("Home", "/"), ("Guides", "/guides"), ("Scaffolding Cost Essex", "/guides/scaffolding-cost-essex")],
        ),
    )

    need_scaffold_body = (
        inner_hero(
            [("Home", "/"), ("Guides", "/guides"), ("Do I Need Scaffolding?", "/guides/do-i-need-scaffolding")],
            "Do I Need Scaffolding for My Project?",
            "A practical guide to help you work out whether your building or repair project requires scaffold access — and what the alternatives are.",
        )
        + f"""
<section class="section section-light">
  <div class="container direct-answer">
    <h2>The Short Answer</h2>
    <p>You almost certainly need scaffolding if trades need to work at height for more than a brief task, if they need both hands free to work safely, or if the job requires materials to be positioned at roof level. A ladder may be sufficient for a single inspection or brief one-handed task. If in doubt, a CISRS-qualified scaffolder can advise — call <a href="tel:{NAP['phone_e164']}">{NAP['phone']}</a> for a no-obligation discussion.</p>
  </div>
</section>

<section class="section section-dark">
  <div class="container">
    <h2>Jobs That Typically Require Scaffolding</h2>
    <div class="decision-grid">
      <div class="decision-card"><h3>Roof Replacement</h3><p>Any full or partial roof replacement requires a scaffold to allow roofers to work safely and to land materials at roof level. No reputable roofer will re-roof from a ladder.</p></div>
      <div class="decision-card"><h3>Chimney Repointing or Rebuild</h3><p>Chimney work at or above roof level requires a stable working platform. A chimney scaffold is a small but essential structure for this type of job.</p></div>
      <div class="decision-card"><h3>External Rendering</h3><p>Rendering requires a renderer to work across the full face of a wall at height with both hands. A scaffold provides the working platform and access staging needed.</p></div>
      <div class="decision-card"><h3>Fascia, Soffit and Guttering</h3><p>Replacing guttering or roofline materials around the full perimeter of a property requires access at eaves height — typically a scaffold or tower, depending on height.</p></div>
      <div class="decision-card"><h3>Extensions</h3><p>As an extension rises past ground floor, scaffold access is required for bricklayers and other trades working on upper walls and the roof structure.</p></div>
      <div class="decision-card"><h3>Window and Cladding Work</h3><p>Upper-floor window replacement, cladding installation or external insulation work all typically require scaffold access for safe two-handed working.</p></div>
    </div>
  </div>
</section>

<section class="section section-light">
  <div class="container">
    <h2>When a Ladder May Be Sufficient</h2>
    <p>For a licensed tradesperson carrying out a brief task — cleaning a single gutter section, inspecting a roof, replacing a single tile — a ladder used with the correct technique may be appropriate under a risk assessment. This is the roofer's or contractor's decision, not the homeowner's. Where work involves sustained activity, both hands being needed, or working near a roof edge, scaffold is the appropriate solution.</p>
    <h2>Working at Height Regulations</h2>
    <p>The Work at Height Regulations 2005 require that all work at height is properly planned, appropriately supervised and carried out by competent people using appropriate equipment. This applies to all trades working on your property, not just scaffolders. If a tradesperson is proposing to carry out significant work at height without a scaffold or other collective protective measure, it is worth asking how they are meeting this requirement.</p>
    <div class="hero-cta-row" style="margin-top:1.5rem;">
      <a class="btn btn-primary" href="/quote">Get a Free Quote</a>
      <a class="btn btn-outline" href="tel:{NAP['phone_e164']}">Call {NAP['phone']}</a>
    </div>
  </div>
</section>
"""
    )
    write(
        "guides/do-i-need-scaffolding/index.html",
        render_page(
            title="Do I Need Scaffolding for My Project? | Axis Scaffolding Essex",
            desc="Find out whether your building or repair project needs scaffolding. Practical guidance on when scaffold is required and when a ladder may be sufficient.",
            path="/guides/do-i-need-scaffolding",
            body=need_scaffold_body,
            breadcrumb_items=[("Home", "/"), ("Guides", "/guides"), ("Do I Need Scaffolding?", "/guides/do-i-need-scaffolding")],
        ),
    )

    licence_guide_body = (
        inner_hero(
            [("Home", "/"), ("Guides", "/guides"), ("Highway Licence for Scaffolding", "/guides/highway-licence-scaffolding")],
            "Does Scaffolding on a Pavement Need a Licence?",
            "A plain-English guide to Section 169 highway licences for scaffolding over pavements and roads in Essex — when you need one, how to get one, and what it costs.",
        )
        + f"""
<section class="section section-light">
  <div class="container direct-answer">
    <h2>Yes — a Licence Is Required</h2>
    <p>If scaffolding overhangs or occupies any part of a public highway — including the pavement in front of your property — a licence under <strong>Section 169 of the Highways Act 1980</strong> is required before erection begins. Working without a licence can result in enforcement action by the local authority and invalidate your insurance. Axis Scaffolding can advise on the licence process and liaise with Essex Highways on your behalf.</p>
  </div>
</section>

<section class="section section-dark">
  <div class="container">
    <h2>What Is a Section 169 Licence?</h2>
    <p>A Section 169 licence (also called a "scaffolding licence" or "highway licence") is a formal permission granted by the highway authority — in most of Essex this is Essex County Council Highways — to occupy or overhang the public highway with a scaffold structure. It specifies conditions including the scaffold footprint, lighting and signing requirements, and the permitted duration.</p>
    <h2>When Do You Need One?</h2>
    <div class="decision-grid">
      <div class="decision-card"><h3>Pavement Overhang</h3><p>If any part of the scaffold — including ties, standards or boards — extends over the public footpath, a licence is required even if the scaffold base is on private land.</p></div>
      <div class="decision-card"><h3>Scaffold on the Highway</h3><p>If scaffold base plates or any structure is positioned on the public footpath or road surface, a licence is required.</p></div>
      <div class="decision-card"><h3>Protective Fans or Gantries</h3><p>Covered walkways or protective fans over a pavement also require a licence regardless of whether they touch the ground.</p></div>
      <div class="decision-card decision-card-urgent"><h3>Not Required If Fully On Private Land</h3><p>If the scaffold is entirely within the property boundary, away from the highway, no Section 169 licence is needed — though planning restrictions may still apply.</p></div>
    </div>
    <h2>How Long Does It Take?</h2>
    <p>Essex Highways typically requires a minimum of 5–10 working days' notice. Some districts and urban areas may require longer. We recommend raising the licence requirement as early as possible in the project planning process. Axis Scaffolding will identify the requirement at the quotation stage and advise accordingly.</p>
    <h2>What Does It Cost?</h2>
    <p>Licence fees are set by the highway authority and vary. As a guide, Essex Highways charges a fee based on the area of highway occupied and the duration. These fees are passed through at cost. We will include the estimated licence cost in your quotation so there are no surprises.</p>
    <div class="hero-cta-row" style="margin-top:2rem;">
      <a class="btn btn-primary" href="/quote">Get a Free Quote</a>
      <a class="btn btn-outline" href="tel:{NAP['phone_e164']}">Call {NAP['phone']}</a>
    </div>
  </div>
</section>
"""
    )
    write(
        "guides/highway-licence-scaffolding/index.html",
        render_page(
            title="Scaffolding Highway Licence Essex | Section 169 Guide",
            desc="Do you need a licence to erect scaffolding on a pavement in Essex? Plain-English guide to Section 169 highway licences — when required, how to apply, and typical costs.",
            path="/guides/highway-licence-scaffolding",
            body=licence_guide_body,
            breadcrumb_items=[("Home", "/"), ("Guides", "/guides"), ("Highway Licence", "/guides/highway-licence-scaffolding")],
        ),
    )

    # ── Contractors / commercial page ─────────────────────────────────────
    contractors_body = (
        inner_hero(
            [("Home", "/"), ("Contractors", "/contractors")],
            "Scaffolding for Builders &amp; Contractors in Essex",
            "Axis Scaffolding Ltd works directly with builders, developers and principal contractors across South Essex. RAMS available. CISRS qualified. Trade enquiries welcome.",
        )
        + f"""
<section class="section section-light">
  <div class="container direct-answer">
    <h2>A Reliable Scaffolding Partner for Essex Contractors</h2>
    <p>We work with builders, roofing contractors, developers and property managers across South Essex. Our CISRS-qualified team provides planned scaffold packages with clear communication, RAMS documentation when required, and a commitment to erection and strike timescales that keep your programme on track. Call <a href="tel:{NAP['phone_e164']}">{NAP['phone']}</a> to discuss a trade account or one-off project.</p>
  </div>
</section>

<section class="section section-dark">
  <div class="container">
    <h2>What We Offer Contractors</h2>
    <div class="decision-grid">
      <div class="decision-card"><h3>RAMS on Request</h3><p>Risk Assessments and Method Statements available for commercial sites and principal contractors who require them before works begin.</p></div>
      <div class="decision-card"><h3>Planned Erection and Strike</h3><p>We work to agreed dates. If your programme changes, call us early — we will do our best to accommodate. We understand that site programmes flex.</p></div>
      <div class="decision-card"><h3>CISRS Qualified Team</h3><p>All operatives hold valid CISRS cards. You can verify qualifications on request. Full insurance documentation provided on request.</p></div>
      <div class="decision-card"><h3>Trade Enquiries Welcome</h3><p>We work with roofers, builders, developers and property managers on a repeat and one-off basis. Call to discuss your project or set up a trade account.</p></div>
      <div class="decision-card"><h3>Highway Licence Advice</h3><p>We identify licence requirements at the quotation stage and liaise with Essex Highways on your behalf where required.</p></div>
      <div class="decision-card"><h3>Emergency Response</h3><p>Storm-damaged roofs and urgent structural access don't wait. Call us directly for priority attendance on emergency jobs.</p></div>
    </div>
  </div>
</section>

<section class="section section-light">
  <div class="container">
    <h2>Services Available to Contractors</h2>
    <div class="services-grid">
      {"".join(f'<article class="service-card"><h3>{s["name"]}</h3><p>{s["summary"]}</p><a href="/services/{s["slug"]}">Read more</a></article>' for s in SERVICES)}
    </div>
  </div>
</section>

<section class="cta-banner">
  <div class="container cta-banner-inner">
    <div>
      <h2>Trade Enquiries Welcome</h2>
      <p>Call us to discuss your project or request a trade quotation &middot; CISRS qualified &middot; RAMS available</p>
    </div>
    <div class="hero-cta-row">
      <a class="btn btn-primary" href="tel:{NAP['phone_e164']}">{NAP['phone']}</a>
      <a class="btn btn-outline" href="/quote">Send an Enquiry</a>
    </div>
  </div>
</section>
"""
    )
    write(
        "contractors/index.html",
        render_page(
            title="Scaffolding for Builders &amp; Contractors | Axis Scaffolding Essex",
            desc="Axis Scaffolding works with builders, roofers and developers across South Essex. CISRS qualified, RAMS available, trade enquiries welcome. Call 01702 820468.",
            path="/contractors",
            body=contractors_body,
            breadcrumb_items=[("Home", "/"), ("Contractors", "/contractors")],
        ),
    )

    for area_name, area_data in AREA_DATA.items():
        write(
            f"areas/{area_data['slug']}/index.html",
            render_page(
                title=f"Scaffolding in {area_name} | Axis Scaffolding Essex",
                desc=area_data["desc"],
                path=f"/areas/{area_data['slug']}",
                body=area_page_body(area_name, area_data),
                breadcrumb_items=[("Home", "/"), ("Areas", "/areas"), (area_name, f"/areas/{area_data['slug']}")],
            ),
        )

    thank_you_body = """
<section class="inner-hero"><div class="container"><h1>Thank You — We'll Be In Touch!</h1><p>Your enquiry has been received. A member of the Axis Scaffolding team will contact you within 24 hours.</p><p>In the meantime, call us on <a href="tel:+441702820468">01702 820468</a> for urgent enquiries.</p><div class="hero-cta-row"><a class="btn btn-primary" href="/">Back to Home</a><a class="btn btn-outline-orange" href="/services">View Our Services</a></div></div></section>
"""
    write(
        "thank-you/index.html",
        """<!doctype html>
<html lang="en-GB">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Thank You | Axis Scaffolding Essex – Scaffolding in Rayleigh, Essex</title>
  <meta name="description" content="Thank you for contacting Axis Scaffolding in Rayleigh. We will respond quickly regarding your scaffolding Essex enquiry.">
  <meta name="robots" content="noindex, nofollow">
  <link rel="canonical" href="https://www.axisscaffoldingessex.co.uk/thank-you">
  <link rel="stylesheet" href="/assets/css/style.css">
</head>
<body>
  <div id="mouse-glow" aria-hidden="true"></div>
  <a href="#main-content" class="sr-only focus:not-sr-only">Skip to main content</a>
  """ + nav() + """
  """ + moved_site_banner() + """
  <main id="main-content">""" + thank_you_body + """</main>
  """ + footer() + """
  """ + cookie_ui() + f"""
  <script>window.AXIS_GA4_ID = {json.dumps(GA4_MEASUREMENT_ID)};</script>
  <script src="/assets/js/main.js" defer></script>
</body>
</html>
""",
    )

    notfound_body = f"""
<section class="inner-hero">
  <div class="container">
    <p class="breadcrumb-nav"><a href="/">Home</a> &rsaquo; Page Not Found</p>
    <h1>Page Not Found</h1>
    <p>Sorry, we couldn't find that page. Here's how to get back on track:</p>
    <div class="hero-cta-row">
      <a class="btn btn-primary" href="tel:{NAP['phone_e164']}">{NAP['phone']}</a>
      <a class="btn btn-outline" href="/quote">Get a Free Quote</a>
      <a class="btn btn-outline" href="/">Go Home</a>
    </div>
  </div>
</section>
<section class="section section-dark">
  <div class="container">
    <h2>Our Scaffolding Services</h2>
    <div class="services-grid">
      {"".join(f'<article class="service-card"><h3>{s["name"]}</h3><p>{s["summary"]}</p><a href="/services/{s["slug"]}">Learn more &rarr;</a></article>' for s in SERVICES[:6])}
    </div>
    <p style="margin-top:2rem;"><a href="/services" class="btn btn-outline">View All Services</a></p>
  </div>
</section>
"""
    write(
        "404.html",
        """<!doctype html>
<html lang="en-GB">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Page Not Found | Axis Scaffolding Essex</title>
  <meta name="description" content="Page not found on Axis Scaffolding Essex in Rayleigh. Browse scaffolding Essex services and get a free quote today.">
  <link rel="stylesheet" href="/assets/css/style.css">
</head>
<body>
  <div id="mouse-glow" aria-hidden="true"></div>
  <a href="#main-content" class="sr-only focus:not-sr-only">Skip to main content</a>
  """ + moved_site_banner() + """
  """ + nav() + """
  <main id="main-content">""" + notfound_body + """</main>
  """ + footer() + """
  """ + cookie_ui() + """
  <script src="/assets/js/main.js" defer></script>
</body>
</html>
""",
    )


def generate_redirects() -> None:
    redirect_html = (
        "<!doctype html><html lang=\"en\"><head><meta charset=\"utf-8\">"
        "<meta http-equiv=\"refresh\" content=\"0;url={target}\"><link rel=\"canonical\" href=\"{canonical}\">"
        "<title>Redirecting...</title></head><body><div id=\"mouse-glow\" aria-hidden=\"true\"></div><p>Redirecting to <a href=\"{target}\">{target}</a></p>"
        "<script>window.location.replace('{target}');</script></body></html>"
    )
    redirects = {
        "about.html": "/about",
        "gallery.html": "/gallery",
        "contact.html": "/contact",
        "privacy.html": "/privacy-policy",
        "terms.html": "/terms-and-conditions",
        "cookies.html": "/cookie-policy",
        "services/residential.html": "/services/residential-scaffolding",
        "services/commercial.html": "/services/commercial-scaffolding",
        "services/supply-erection.html": "/services/scaffold-supply-erection",
        "services/dismantling.html": "/services/dismantling-scaffolding",
        "services/loading-bays.html": "/services/loading-bay-scaffolding",
        "services/temporary-roofs.html": "/services/temporary-roofing",
    }
    for src, target in redirects.items():
        write(src, redirect_html.format(target=target, canonical=SITE + target))
    legacy_area_targets = {
        "brentwood": "/areas/brentwood",
        "loughton": "/areas/loughton",
        "london": "/areas/london",
        "clacton": "/areas",
        "bromley": "/areas",
        # Stale flat area pages superseded by the canonical /areas/{slug} pages below.
        "basildon": "/areas/basildon",
        "canvey-island": "/areas/canvey-island",
        "chelmsford": "/areas/chelmsford",
        "rayleigh": "/areas/rayleigh",
        "southend": "/areas/southend",
    }
    for area_file, target in legacy_area_targets.items():
        write(f"areas/{area_file}.html", redirect_html.format(target=target, canonical=f"{SITE}{target}"))

    write(
        "_redirects",
        "\n".join(
            [
                f"{OLD_SITE}/* {SITE}/:splat 301!",
                f"https://www.axisscaffolding.co.uk/* {SITE}/:splat 301!",
                "/about.html /about 301",
                "/gallery.html /gallery 301",
                "/contact.html /contact 301",
                "/privacy.html /privacy-policy 301",
                "/terms.html /terms-and-conditions 301",
                "/cookies.html /cookie-policy 301",
                "/services/residential.html /services/residential-scaffolding 301",
                "/services/commercial.html /services/commercial-scaffolding 301",
                "/services/supply-erection.html /services/scaffold-supply-erection 301",
                "/services/dismantling.html /services/dismantling-scaffolding 301",
                "/services/loading-bays.html /services/loading-bay-scaffolding 301",
                "/services/temporary-roofs.html /services/temporary-roofing 301",
            ]
            + [f"/areas/{slug}.html {target} 301" for slug, target in legacy_area_targets.items()]
        ),
    )


def generate_robots_sitemap() -> None:
    robots = (
        "# Axis Scaffolding Ltd — robots.txt\n"
        "# https://www.axisscaffoldingessex.co.uk\n\n"
        "User-agent: Googlebot\n"
        "Allow: /\n\n"
        "User-agent: Bingbot\n"
        "Allow: /\n\n"
        "User-agent: OAI-SearchBot\n"
        "Allow: /\n\n"
        "User-agent: OAI-AdsBot\n"
        "Allow: /\n\n"
        "User-agent: *\n"
        "Allow: /\n"
        "Disallow: /admin/\n"
        "Disallow: /private/\n\n"
        f"Sitemap: {SITE}/sitemap.xml\n"
    )
    write("robots.txt", robots)
    # Only include canonical, indexable pages in sitemap — exclude noindex pages
    pages = [
        ("/", "1.0", "weekly"),
        ("/services", "0.8", "monthly"),
        ("/services/residential-scaffolding", "0.8", "monthly"),
        ("/services/commercial-scaffolding", "0.8", "monthly"),
        ("/services/domestic-scaffolding", "0.8", "monthly"),
        ("/services/roof-scaffolding", "0.8", "monthly"),
        ("/services/temporary-roofing", "0.8", "monthly"),
        ("/services/emergency-scaffolding", "0.8", "monthly"),
        ("/services/dismantling-scaffolding", "0.7", "monthly"),
        ("/services/loading-bay-scaffolding", "0.7", "monthly"),
        ("/services/scaffold-supply-erection", "0.7", "monthly"),
        ("/gallery", "0.7", "monthly"),
        ("/about", "0.7", "monthly"),
        ("/contact", "0.8", "monthly"),
        ("/quote", "0.8", "monthly"),
        ("/contractors", "0.8", "monthly"),
        ("/guides/scaffolding-cost-essex", "0.7", "monthly"),
        ("/guides/do-i-need-scaffolding", "0.7", "monthly"),
        ("/guides/highway-licence-scaffolding", "0.7", "monthly"),
    ] + [(f"/areas/{data['slug']}", "0.7", "monthly") for data in AREA_DATA.values()]
    lines = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for path, priority, changefreq in pages:
        lines.append(
            f"  <url><loc>{SITE}{path}</loc><lastmod>{TODAY}</lastmod><changefreq>{changefreq}</changefreq><priority>{priority}</priority></url>"
        )
    lines.append("</urlset>")
    write("sitemap.xml", "\n".join(lines))


def main() -> None:
    ensure_dirs()
    try:
        generate_media_assets()
    except Exception as exc:
        print(f"Warning: media asset generation skipped — {exc}")
    generate_css()
    generate_js()
    generate_pages()
    generate_redirects()
    generate_robots_sitemap()
    print("Site regeneration completed.")


if __name__ == "__main__":
    main()

