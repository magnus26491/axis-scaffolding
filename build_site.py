from __future__ import annotations

import json
from datetime import date
from pathlib import Path
from typing import Iterable

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).parent
SITE = "https://axisscaffoldingessex.co.uk"
OLD_SITE = "https://axisscaffolding.co.uk"
OG_IMAGE_URL = f"{SITE}/public/og-image.jpg"
TODAY = date.today().isoformat()
CONTACT_EMAIL = 'axis-scaffolding@outlook.com'
FORM_ACTION = 'https://formsubmit.co/axis-scaffolding@outlook.com'
FORM_NEXT = 'https://axisscaffoldingessex.co.uk/thank-you'

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
  <meta name="revisit-after" content="30 days">
  <meta name="google-site-verification" content="REPLACE_WITH_GSC_CODE">
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
<div id="axis-cookie-bar" style="
  display: none;
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
  z-index: 99999;
  background: rgba(10, 10, 10, 0.92);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  border-top: 1px solid rgba(255,255,255,0.1);
  padding: 1rem 2rem;
  flex-wrap: wrap;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
  font-family: Inter, sans-serif;
">
  <p style="color:#d1d5db; font-size:0.875rem; max-width:600px; margin:0;">
    We use cookies to improve your experience and analyse site traffic.
    By clicking <strong style="color:#fff;">Accept All</strong> you consent
    to our use of cookies.
    <a href="/privacy-policy" style="color:#f97316; text-decoration:underline;">
      Read our Privacy Policy
    </a>
  </p>
  <div style="display:flex; flex-wrap:wrap; gap:0.75rem; align-items:center;">
    <button id="axis-cookie-accept" style="
      background:#f97316; color:#000; border:none; border-radius:9999px;
      padding:0.5rem 1.25rem; font-weight:700; font-size:0.875rem;
      cursor:pointer; white-space:nowrap;
    ">Accept All</button>
    <button id="axis-cookie-reject" style="
      background:transparent; color:#fff;
      border:1px solid rgba(255,255,255,0.5);
      border-radius:9999px; padding:0.5rem 1.25rem;
      font-size:0.875rem; cursor:pointer; white-space:nowrap;
    ">Reject Non-Essential</button>
    <button id="axis-cookie-manage" style="
      background:none; border:none; color:#9ca3af;
      font-size:0.875rem; cursor:pointer;
      text-decoration:underline; padding:0.5rem 0;
    ">Manage Preferences</button>
  </div>
</div>
"""


def moved_site_banner() -> str:
    return """
<div id="domain-move-banner" class="domain-move-banner" hidden>
  We've moved! Visit us at
  <a href="https://axisscaffoldingessex.co.uk" rel="canonical">axisscaffoldingessex.co.uk</a>
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
  <script type="text/plain" data-consent-category="analytics">window.axisAnalyticsAllowed = true;</script>
  <script type="text/plain" data-consent-category="marketing">window.axisMarketingAllowed = true;</script>
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
            im.convert("RGB").save(ROOT / "images/hero-bg.webp", format="WEBP", quality=85)

    og = Image.new("RGB", (1200, 630), "#0d0d0d")
    draw = ImageDraw.Draw(og)
    with Image.open(src_logo) as logo:
        logo = logo.convert("RGB").resize((220, 220))
        mask = Image.new("L", (220, 220), 0)
        mask_draw = ImageDraw.Draw(mask)
        mask_draw.ellipse((0, 0, 219, 219), fill=255)
        og.paste(logo, (490, 120), mask)
        draw.ellipse((488, 118, 712, 342), outline="#f97316", width=4)
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
}
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
.site-nav a {
  text-decoration:none; color:#ffffff;
  font-weight:600; transition:color 0.2s;
}
.site-nav a:hover { color: #c8cdd4; }
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
.btn-primary {
  background: linear-gradient(135deg, #e8eaed 0%, #9ba3ab 40%, #c8cdd4 60%, #e2e5e8 100%) !important;
  color: #000000 !important; font-weight: 700 !important; border: none !important;
  box-shadow: inset 0 1px 0 rgba(255,255,255,0.4), 0 4px 15px rgba(200,205,212,0.15) !important;
}
.btn-primary:hover {
  background: linear-gradient(135deg, #ffffff 0%, #c8cdd4 40%, #e2e5e8 100%) !important;
  transform: translateY(-1px) !important;
}
.btn-outline { border-color:#fff; color:#fff; background:transparent; }
.btn-outline:hover { background:rgba(255,255,255,0.1); }
.btn-outline-orange { border-color:var(--accent); color:var(--accent); background:transparent; }
.btn-dark { background:rgba(255,255,255,0.08); color:#fff; }
.btn-light { background:#fff; color:#000; }
.btn-full { width:100%; }
.hero-cta-row { display:flex; flex-wrap:wrap; gap:0.75rem; justify-content:center; }

.cta-pill {
  background: linear-gradient(135deg, #e8eaed 0%, #9ba3ab 40%, #c8cdd4 60%, #e2e5e8 100%) !important;
  color: #000000 !important; font-weight: 700 !important;
  padding: 0.65rem 1.4rem !important; border-radius: 9999px !important;
  text-decoration: none !important; display: inline-block !important;
  border: none !important;
}
.cta-pill:hover {
  background: linear-gradient(135deg, #ffffff 0%, #c8cdd4 40%, #e2e5e8 100%) !important;
  transform: translateY(-1px) !important; color: #000000 !important;
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

/* Hero trust badges */
.hero-trust-badges {
  display:flex; flex-wrap:wrap; gap:0.5rem; margin-top:1.5rem;
}
.hero-trust-badges span {
  background:rgba(255,255,255,0.1);
  border:1px solid rgba(255,255,255,0.22);
  color:#fff; font-size:0.82rem; font-weight:600;
  padding:0.3rem 0.8rem; border-radius:9999px;
}

/* ── SECTIONS ── */
.section { padding:4.5rem 0; }
.section-light { background:#0a0a0a !important; }
.section-dark  { background:#000000 !important; }
.section-dark h2,.section-dark h3,.section-dark p { color:#ffffff; }
.section-intro { color:#9ca3af; margin-bottom:1.5rem; }

/* ── TRUST BAR ── */
.trust-bar {
  background:rgba(255,255,255,0.03) !important;
  border-top:1px solid rgba(255,255,255,0.07);
  border-bottom:1px solid rgba(255,255,255,0.07);
  padding:2rem 0; overflow-x:auto;
}
.trust-items { display:flex; gap:3rem; justify-content:center; flex-wrap:wrap; }
.trust-item { display:flex; flex-direction:column; align-items:center; gap:0.25rem; }
.trust-number,.trust-static { font-family:'Poppins',sans-serif; font-size:2rem; font-weight:700; color:#ffffff; }
.trust-label { color:#9ca3af; font-size:0.85rem; text-align:center; }

/* ── GLASS CARDS ── */
.glass-card,
.service-card,
.testimonial-card,
.contact-card,
.social-card,
.quote-form-card {
  position: relative; overflow: hidden;
  background: rgba(255,255,255,0.04) !important;
  border: 1px solid rgba(255,255,255,0.12) !important;
  backdrop-filter: blur(20px) saturate(200%) brightness(110%) !important;
  -webkit-backdrop-filter: blur(20px) saturate(200%) brightness(110%) !important;
  border-radius: 16px !important;
  box-shadow:
    0 4px 6px rgba(0,0,0,0.4),
    0 10px 40px rgba(0,0,0,0.5),
    inset 0 1px 0 rgba(255,255,255,0.10),
    inset 0 -1px 0 rgba(0,0,0,0.2) !important;
  transition: transform 0.3s ease, border-color 0.3s ease, box-shadow 0.3s ease !important;
}
.glass-card::before,
.service-card::before,
.testimonial-card::before {
  content:''; position:absolute; inset:0; border-radius:inherit;
  background:linear-gradient(135deg,rgba(255,255,255,0.08) 0%,transparent 50%,rgba(255,255,255,0.02) 100%);
  pointer-events:none; z-index:0;
}
.glass-card > *,
.service-card > *,
.testimonial-card > * { position:relative; z-index:1; }
.glass-card:hover,
.service-card:hover,
.testimonial-card:hover,
.social-card:hover {
  transform: translateY(-6px) !important;
  border-color: rgba(255,255,255,0.28) !important;
  box-shadow:
    0 8px 12px rgba(0,0,0,0.5),
    0 20px 60px rgba(0,0,0,0.6),
    inset 0 1px 0 rgba(255,255,255,0.18),
    0 0 0 1px rgba(255,255,255,0.06) !important;
}
.quote-form-card:hover { transform: none !important; }

/* ── SERVICES GRID ── */
.services-grid, .service-listing {
  display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); gap:1rem;
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

/* ── PROJECTS GRID ── */
.projects-grid { display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); gap:1rem; }
.project-item { position:relative; overflow:hidden; border-radius:1rem; }
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

/* ── DECISION CARDS ── */
.decision-section { padding-bottom:3rem; }
.decision-grid {
  display:grid; grid-template-columns:repeat(4,1fr);
  gap:1.25rem; margin-top:1.5rem;
}
.decision-card {
  background:rgba(255,255,255,0.04) !important;
  border:1px solid rgba(255,255,255,0.12) !important;
  backdrop-filter:blur(20px) !important;
  -webkit-backdrop-filter:blur(20px) !important;
  border-radius:1.25rem; padding:1.75rem 1.25rem 1.5rem;
  text-decoration:none; color:#ffffff;
  transition:border-color 0.2s, box-shadow 0.2s, transform 0.2s;
  display:flex; flex-direction:column; gap:0.5rem;
}
.decision-card:hover {
  border-color:rgba(255,255,255,0.32) !important;
  box-shadow:0 8px 32px rgba(0,0,0,0.5) !important;
  transform:translateY(-4px);
}
.decision-card-urgent {
  border-color:rgba(255,100,100,0.3) !important;
  background:rgba(255,50,50,0.06) !important;
}
.decision-card-urgent:hover { border-color:rgba(255,120,120,0.5) !important; }
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
  z-index:9999; background:#1a1a2e; padding:0;
  padding-bottom:env(safe-area-inset-bottom);
  height:56px; box-shadow:0 -2px 10px rgba(0,0,0,0.3);
}
.mobile-cta-bar .cta-buttons { display:flex; height:100%; }
.mobile-cta-bar .btn-call,
.mobile-cta-bar .btn-quote {
  flex:1; display:flex; align-items:center; justify-content:center;
  gap:0.5rem; font-size:16px; font-weight:700;
  text-decoration:none; transition:background 0.2s ease;
}
.mobile-cta-bar .btn-call { background:#4CAF50; color:#ffffff; }
.mobile-cta-bar .btn-quote { background:#c8cdd4; color:#000000; }
.mobile-cta-bar svg { width:18px; height:18px; }
@media (max-width:768px) { .mobile-cta-bar { display:flex; } }

/* ── RESPONSIVE ── */
@media (max-width:1024px) {
  .services-grid,.service-listing,.projects-grid { grid-template-columns:repeat(2,minmax(0,1fr)); }
  .split-grid,.two-col { grid-template-columns:1fr; }
  .decision-grid { grid-template-columns:repeat(2,1fr); }
}
@media (max-width:768px) {
  .menu-toggle { display:inline-flex; }
  .nav-phone-mobile { display:inline-flex; align-items:center; }
  .nav-phone-desktop { display:none; }
  .site-nav {
    position:fixed; inset:0 0 0 35%;
    background:rgba(0,0,0,0.97); backdrop-filter:blur(20px);
    padding:6rem 1.5rem 1.5rem; display:flex;
    flex-direction:column; align-items:flex-start;
    transform:translateX(100%); transition:transform 0.3s ease;
  }
  .site-nav.open { transform:translateX(0); }
  .nav-wrap { grid-template-columns:auto auto; justify-content:space-between; }
  .footer-grid { grid-template-columns:1fr; }
  .hero-media { top:0 !important; height:100% !important; transform:none !important; }
}
@media (max-width:480px) {
  .social-card { width:100%; min-width:unset; }
  .decision-grid { grid-template-columns:1fr; }
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
    const nextUrl = `https://axisscaffoldingessex.co.uk${window.location.pathname}${window.location.search}${window.location.hash}`;
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
    });
  }
  var rejectBtn = document.getElementById('axis-cookie-reject');
  if (rejectBtn) {
    rejectBtn.addEventListener('click', function() {
      setConsent('rejected');
    });
  }
  var manageBtn = document.getElementById('axis-cookie-manage');
  if (manageBtn) {
    manageBtn.addEventListener('click', function() {
      var existing = document.getElementById('axis-cookie-prefs');
      if (existing) { existing.remove(); return; }
      var panel = document.createElement('div');
      panel.id = 'axis-cookie-prefs';
      panel.style.cssText = 'position:fixed;bottom:80px;left:0;right:0;z-index:99998;' +
        'background:rgba(15,15,15,0.97);border-top:1px solid rgba(255,255,255,0.1);' +
        'padding:1.5rem 2rem;font-family:Inter,sans-serif;color:#d1d5db;font-size:0.875rem;';
      panel.innerHTML = '<p style="color:#fff;font-weight:600;margin:0 0 1rem;">Cookie Preferences</p>' +
        '<div style="display:flex;flex-direction:column;gap:0.75rem;">' +
        '<label style="display:flex;justify-content:space-between;align-items:center;">' +
        '<span>Necessary <span style="color:#6b7280;font-size:0.75rem;">(always on)</span></span>' +
        '<input type="checkbox" checked disabled></label>' +
        '<label style="display:flex;justify-content:space-between;align-items:center;">' +
        '<span>Analytics</span><input type="checkbox" id="axis-pref-analytics"></label>' +
        '<label style="display:flex;justify-content:space-between;align-items:center;">' +
        '<span>Marketing</span><input type="checkbox" id="axis-pref-marketing"></label>' +
        '</div>' +
        '<button id="axis-pref-save" style="margin-top:1rem;background:#f97316;color:#000;' +
        'border:none;border-radius:9999px;padding:0.5rem 1.5rem;font-weight:700;cursor:pointer;">' +
        'Save Preferences</button>';
      document.body.appendChild(panel);
      var save = document.getElementById('axis-pref-save');
      if (save) {
        save.addEventListener('click', function() {
          panel.remove();
          setConsent('custom');
        });
      }
    });
  }
  var footerBtn = document.getElementById('axis-footer-cookie-btn');
  if (footerBtn) {
    footerBtn.addEventListener('click', function() {
      localStorage.removeItem(CONSENT_KEY);
      showBar();
    });
  }

  document.querySelectorAll('.axis-quote-form').forEach((form) => {
    form.addEventListener('submit', async (event) => {
      event.preventDefault();
      const message = form.querySelector('.form-message');
      const data = Object.fromEntries(new FormData(form).entries());
      const webhook = window.AXIS_QUOTE_WEBHOOK;
      const payload = { ...data, notification_email: CONTACT_EMAIL };
      let ok = true;
      if (webhook) {
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
      }
      if (message) {
        message.textContent = ok
          ? 'Thanks. Your quote request has been received. We will respond within one working day.'
          : 'There was a problem submitting your request. Please call 01702 820468 to reach us directly.';
      }
      if (ok) form.reset();
    });
  });
})();

// ── WHITE MOUSE GLOW ──────────────────────
(function() {
  // Only run on non-touch desktop devices
  if (window.matchMedia('(hover: none)').matches) return;
  if (window.matchMedia('(max-width: 768px)').matches) return;

  var glow = document.getElementById('mouse-glow');
  if (!glow) return;

  var mouseX = window.innerWidth / 2;
  var mouseY = window.innerHeight / 2;
  var currentX = mouseX;
  var currentY = mouseY;
  var rafId;

  // Smooth lerp follow (makes it feel soft and organic)
  function lerp(start, end, factor) {
    return start + (end - start) * factor;
  }

  function animate() {
    currentX = lerp(currentX, mouseX, 0.12);
    currentY = lerp(currentY, mouseY, 0.12);
    glow.style.left = currentX + 'px';
    glow.style.top  = currentY + 'px';
    rafId = requestAnimationFrame(animate);
  }

  document.addEventListener('mousemove', function(e) {
    mouseX = e.clientX;
    mouseY = e.clientY;
  }, { passive: true });

  // Start animation loop
  animate();

  // Fade out when mouse leaves window
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


def project_cards() -> str:
    rows = [
        (1, "Residential Scaffolding", "Benfleet"),
        (2, "Commercial Scaffolding", "Canvey Island"),
        (3, "Shopfront Access Scaffold", "Rayleigh"),
        (4, "Temporary Roofing Scaffold", "Southend-on-Sea"),
        (5, "Roof Scaffolding", "Basildon"),
        (6, "Domestic Scaffolding", "Chelmsford"),
    ]
    return "".join(
        f"""
<figure class="project-item">
  <img src="/images/project-{idx}.webp" alt="{label} installation in {location}, Essex" width="640" height="800" loading="lazy" decoding="async">
  <figcaption><span>{label}</span><small>{location}</small></figcaption>
</figure>
"""
        for idx, label, location in rows
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
    return "".join(f'<li><a class="area-pill-link" href="/contact">{area}</a></li>' for area in AREAS)


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
<div class="testimonial-card glass-card">
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
  <img class="hero-media" src="/images/hero-bg.webp" alt="Scaffolding erected on a residential property in South Essex by Axis Scaffolding Ltd" width="1920" height="1280" loading="eager" fetchpriority="high" decoding="async">
  <div class="hero-overlay"></div>
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
    <h2 id="decision-heading">What type of scaffolding do you need?</h2>
    <p class="section-intro">Not sure? <a href="/contact">Tell us about your project</a> and we'll point you in the right direction.</p>
    <div class="decision-grid">
      <a href="/services/residential-scaffolding" class="decision-card">
        <div class="decision-icon" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 9.5L12 3l9 6.5V20a1 1 0 01-1 1H4a1 1 0 01-1-1V9.5z"/><path d="M9 21V12h6v9"/></svg></div>
        <h3>Homeowner</h3>
        <p>Roofing &middot; rendering &middot; extensions &middot; chimneys</p>
        <span class="decision-link" aria-hidden="true">Find out more &rarr;</span>
      </a>
      <a href="/services/commercial-scaffolding" class="decision-card">
        <div class="decision-icon" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="7" width="20" height="14" rx="1"/><path d="M16 7V5a2 2 0 00-2-2h-4a2 2 0 00-2 2v2"/><line x1="12" y1="12" x2="12" y2="16"/><line x1="10" y1="14" x2="14" y2="14"/></svg></div>
        <h3>Builder / Roofer</h3>
        <p>Access scaffold &middot; bespoke setups &middot; fast turnaround</p>
        <span class="decision-link" aria-hidden="true">Find out more &rarr;</span>
      </a>
      <a href="/services/commercial-scaffolding" class="decision-card">
        <div class="decision-icon" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="1"/><path d="M3 9h18M9 21V9"/></svg></div>
        <h3>Commercial</h3>
        <p>Sites &middot; offices &middot; retail &middot; schools &middot; developments</p>
        <span class="decision-link" aria-hidden="true">Find out more &rarr;</span>
      </a>
      <a href="/services/emergency-scaffolding" class="decision-card decision-card-urgent">
        <div class="decision-icon" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M10.29 3.86L1.82 18a2 2 0 001.71 3h16.94a2 2 0 001.71-3L13.71 3.86a2 2 0 00-3.42 0z"/><line x1="12" y1="9" x2="12" y2="13"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg></div>
        <h3>Emergency</h3>
        <p>Storm damage &middot; urgent access &middot; temporary protection</p>
        <span class="decision-link" aria-hidden="true">Call us now &rarr;</span>
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


def service_detail_body(service: dict) -> str:
    path = [("Home", "/"), ("Services", "/services"), (service["name"], f"/services/{service['slug']}")]
    return (
        inner_hero(
            path,
            f"{service['name']} Scaffolding in Essex",
            f"{service['summary']} From Benfleet to wider scaffolding Essex projects, we provide clear planning and practical delivery. Get a free quote today.",
        )
        + """
<section class="section"><div class="container"><h2>What's Included</h2><p>Every package includes site assessment, safe scaffold design, installation by CISRS-certified operatives, routine checks and structured dismantling. We coordinate with homeowners, trades and principal contractors to ensure safe access and efficient scheduling across Benfleet and surrounding Essex locations.</p></div></section>
<section class="section section-light"><div class="container"><h2>Our Process</h2><ol><li>Site review and scope confirmation.</li><li>Detailed quotation with timings and requirements.</li><li>Installation, inspections and responsive adjustments.</li><li>Safe dismantle and tidy handover on completion.</li></ol></div></section>
<section class="section"><div class="container"><h2>Why Choose Axis Scaffolding?</h2><p>Axis Scaffolding Ltd combines local knowledge, rapid communication and safety-first delivery. Our Benfleet team supports residential and commercial scaffolding Essex projects with practical access systems, transparent pricing and dependable on-site professionalism.</p><p><a href="/services">Back to all scaffolding services</a></p></div></section>
"""
        + f"""
<section class="section section-light"><div class="container faq-wrap"><h2>Frequently Asked Questions</h2>{faq_accordion()}</div></section>
<section class="cta-banner"><div class="container cta-banner-inner"><div><h2>Get a Free Quote</h2><p>Talk to our Benfleet team about your {service['name'].lower()} requirements.</p></div><div class="hero-cta-row"><a class="btn btn-light" href="tel:{NAP['phone']}">{NAP['phone']}</a><a class="btn btn-dark" href="/quote">Request a Quote</a></div></div></section>
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
        + f"""<section class="section section-dark"><div class="container"><h2>Our Recent Projects</h2><div class="projects-grid">{project_cards()}</div></div></section>"""
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
<section class="section"><div class="container two-col"><article class="contact-card"><h2>Contact Us</h2><p><strong>Name:</strong> Axis Scaffolding Ltd</p><p><strong>Phone:</strong> <a href="tel:+441702820468">01702 820468</a></p><p><strong>Email:</strong> <a href="mailto:axis-scaffolding@outlook.com">axis-scaffolding@outlook.com</a></p><p><strong>Address:</strong> Arterial Road, Rayleigh, Essex, SS6 7XT</p><p>Email us: <a href="mailto:axis-scaffolding@outlook.com" style="color:#f97316;">axis-scaffolding@outlook.com</a></p></article>{quote_form("contact", "Request a Free Scaffolding Quote")}</div></section>
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
  <link rel="canonical" href="https://axisscaffoldingessex.co.uk/thank-you">
  <link rel="stylesheet" href="/assets/css/style.css">
</head>
<body>
  <div id="mouse-glow" aria-hidden="true"></div>
  <a href="#main-content" class="sr-only focus:not-sr-only">Skip to main content</a>
  """ + nav() + """
  """ + moved_site_banner() + """
  <main id="main-content">""" + thank_you_body + """</main>
  """ + footer() + """
  """ + cookie_ui() + """
  <script src="/assets/js/main.js" defer></script>
</body>
</html>
""",
    )

    write(
        "404.html",
        """<!doctype html>
<html lang="en-GB">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Page Not Found | Axis Scaffolding Essex – Scaffolding in Rayleigh, Essex</title>
  <meta name="description" content="Page not found on Axis Scaffolding Essex in Rayleigh. Browse scaffolding Essex services and get a free quote today.">
  <link rel="stylesheet" href="/assets/css/style.css">
</head>
<body>
  <div id="mouse-glow" aria-hidden="true"></div>
  <a href="#main-content" class="sr-only focus:not-sr-only">Skip to main content</a>
  """ + moved_site_banner() + """
  <main id="main-content" class="not-found-wrap">
    <h1>Page Not Found</h1>
    <p>Sorry, we couldn't find that page. Let us help you find what you need.</p>
    <div class="hero-cta-row">
      <a class="btn btn-primary" href="/">Go Home</a>
      <a class="btn btn-outline" href="/services">Our Services</a>
      <a class="btn btn-outline" href="/contact">Contact Us</a>
    </div>
  </main>
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
        "services/supply-erection.html": "/services/domestic-scaffolding",
        "services/dismantling.html": "/services/emergency-scaffolding",
        "services/loading-bays.html": "/services/roof-scaffolding",
        "services/temporary-roofs.html": "/services/temporary-roofing",
    }
    for src, target in redirects.items():
        write(src, redirect_html.format(target=target, canonical=SITE + target))
    for area_file in [
        "southend",
        "rayleigh",
        "canvey-island",
        "chelmsford",
        "basildon",
        "brentwood",
        "loughton",
        "clacton",
        "bromley",
        "london",
    ]:
        write(f"areas/{area_file}.html", redirect_html.format(target="/#areas-covered", canonical=f"{SITE}/#areas-covered"))

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
                "/services/supply-erection.html /services/domestic-scaffolding 301",
                "/services/dismantling.html /services/emergency-scaffolding 301",
                "/services/loading-bays.html /services/roof-scaffolding 301",
                "/services/temporary-roofs.html /services/temporary-roofing 301",
                "/areas/* /#areas-covered 301",
            ]
        ),
    )


def generate_robots_sitemap() -> None:
    robots = (
        "# Axis Scaffolding Ltd — robots.txt\n"
        "# https://axisscaffoldingessex.co.uk\n\n"
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
    ]
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

