from __future__ import annotations

import json
from datetime import date
from pathlib import Path
from typing import Iterable

from PIL import Image, ImageDraw, ImageFont


ROOT = Path("/workspace")
SITE = "https://axisscaffoldingessex.co.uk"
OLD_SITE = "https://axisscaffolding.co.uk"
OG_IMAGE_URL = f"{SITE}/public/og-image.jpg"
TODAY = date.today().isoformat()
CONTACT_EMAIL = 'axis-scaffolding@outlook.com'
FORM_ACTION = 'mailto:axis-scaffolding@outlook.com'
FORM_NEXT = 'https://axisscaffoldingessex.co.uk/thank-you'

NAP = {
    "name": "Axis Scaffolding Ltd",
    "address": "Arterial Road, Rayleigh, Essex, SS6 7XT",
    "phone": "07713245511",
    "email": CONTACT_EMAIL,
    "company_no": "15050136",
}

FAQS = [
    (
        "How much does scaffolding cost in Essex?",
        "Scaffolding costs in Essex depend on property size, scaffold type and project duration. We provide clear quotations from our Benfleet team so you can approve your project confidently.",
    ),
    (
        "How quickly can scaffolding be erected in Benfleet?",
        "Most Benfleet and South Essex installations can be scheduled quickly once your quote is approved. We plan safe access and provide a realistic start date based on project urgency and scope.",
    ),
    (
        "Are you CISRS certified scaffolders?",
        "Yes. Axis Scaffolding Ltd is a fully qualified, CISRS-certified scaffolding company focused on safe, compliant installations for homes and businesses across Essex.",
    ),
    (
        "Do you cover residential and commercial scaffolding in Essex?",
        "Absolutely. We provide residential, domestic and commercial scaffolding, including roof scaffolding, temporary roofing and emergency access support throughout Essex.",
    ),
    (
        "What areas do you cover in Essex?",
        "We are based in Benfleet and regularly cover Canvey Island, Rayleigh, Southend-on-Sea, Basildon, Chelmsford, Wickford, Hadleigh, Leigh-on-Sea, Thundersley, Hockley and Rochford.",
    ),
]

SERVICES = [
    {
        "slug": "residential-scaffolding",
        "name": "Residential Scaffolding",
        "title": "Residential Scaffolding Essex | Axis Scaffolding Ltd",
        "desc": "Need residential scaffolding Essex support in Benfleet? Axis Scaffolding delivers safe home access across scaffolding Essex. Get a free quote today.",
        "summary": "Safe and tidy scaffold systems for extensions, roofing, rendering and exterior home improvements.",
    },
    {
        "slug": "commercial-scaffolding",
        "name": "Commercial Scaffolding",
        "title": "Commercial Scaffolding Essex | Axis Scaffolding Ltd",
        "desc": "Commercial scaffolding Essex support from Rayleigh specialists at Axis Scaffolding for developers across scaffolding Essex. Get a free quote today.",
        "summary": "Reliable scaffold packages for offices, retail units, schools and commercial developments.",
    },
    {
        "slug": "domestic-scaffolding",
        "name": "Domestic Scaffolding",
        "title": "Domestic Scaffolding Essex | Axis Scaffolding Team",
        "desc": "Domestic scaffolding Essex services from Rayleigh with safe, practical access for houses and flats across scaffolding Essex. Get a free quote today.",
        "summary": "Flexible domestic scaffold installations tailored for occupied properties and local builders.",
    },
    {
        "slug": "roof-scaffolding",
        "name": "Roof Scaffolding",
        "title": "Roof Scaffolding Essex | Axis Scaffolding Essex Team",
        "desc": "Roof scaffolding Essex installations from Rayleigh for repairs and refurbishments across scaffolding Essex with dependable access. Get a free quote today.",
        "summary": "Specialist roof access scaffold systems for chimney, guttering and full roofline projects.",
    },
    {
        "slug": "temporary-roofing",
        "name": "Temporary Roofing",
        "title": "Temporary Roofing Essex | Axis Scaffolding Essex Team",
        "desc": "Temporary roofing scaffolding Essex solutions in Rayleigh to protect sites from weather across scaffolding Essex while works continue. Get a free quote today.",
        "summary": "Weather-protected temporary roofing structures that keep projects moving in all seasons.",
    },
    {
        "slug": "emergency-scaffolding",
        "name": "Emergency Scaffolding",
        "title": "Emergency Scaffolding Essex | Axis Scaffolding Ltd",
        "desc": "Emergency scaffolding Essex response from Rayleigh for urgent access and safety works across scaffolding Essex. Contact Axis Scaffolding for a free quote today.",
        "summary": "Rapid-response scaffold support for urgent structural, roof or safety access requirements.",
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
            "Benfleet",
            "Canvey Island",
            "Rayleigh",
            "Southend-on-Sea",
            "Chelmsford",
            "Basildon",
            "Essex",
        ],
        "priceRange": "££",
        "openingHours": "Mo-Fr 07:00-18:00",
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
    return """
<header class="site-header" id="site-header">
  <div class="container nav-wrap">
    <a class="logo-wrap" href="/" aria-label="Axis Scaffolding Ltd homepage">
      <span class="logo-circle logo-circle-nav">
        <img src="/images/logo.webp" alt="Axis Scaffolding Ltd logo" width="64" height="64" loading="lazy" decoding="async">
      </span>
    </a>
    <button class="menu-toggle" id="menu-toggle" aria-label="Toggle mobile menu" aria-controls="site-menu" aria-expanded="false">
      <span></span><span></span><span></span>
    </button>
    <nav class="site-nav" id="site-menu" aria-label="Primary navigation">
      <a href="/">Home</a>
      <a href="/services">Services</a>
      <a href="/gallery">Gallery</a>
      <a href="/about">About</a>
      <a href="/contact">Contact</a>
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
      <p><a href="tel:{NAP["phone"]}">{NAP["phone"]}</a></p>
      <p><a href="mailto:{NAP["email"]}">{NAP["email"]}</a></p>
      <p>{NAP["address"]}</p>
      <p>Company No: {NAP["company_no"]}</p>
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
  <form class="axis-quote-form" data-form-name="{prefix}" action="{FORM_ACTION}" method="POST" enctype="text/plain">
    <input type="hidden" name="_replyto" value="{CONTACT_EMAIL}">
    <input type="hidden" name="_next" value="{FORM_NEXT}">
    <p><label for="{prefix}-name">Full Name *</label><input id="{prefix}-name" name="fullName" required></p>
    <p><label for="{prefix}-phone">Phone Number *</label><input id="{prefix}-phone" name="phone" type="tel" required></p>
    <p><label for="{prefix}-email">Email Address *</label><input id="{prefix}-email" name="email" type="email" required></p>
    <p><label for="{prefix}-postcode">Postcode *</label><input id="{prefix}-postcode" name="postcode" required></p>
    <p><label for="{prefix}-type">Type of Scaffolding *</label>
      <select id="{prefix}-type" name="scaffoldingType" required>
        <option value="">Please select</option><option>Residential</option><option>Commercial</option><option>Roof</option><option>Emergency</option><option>Temporary Roofing</option><option>Other</option>
      </select>
    </p>
    <p><label for="{prefix}-brief">Brief Description of Work</label><textarea id="{prefix}-brief" name="briefDescription"></textarea></p>
    <p><label for="{prefix}-source">How did you hear about us?</label>
      <select id="{prefix}-source" name="source">
        <option value="">Please select</option><option>Google</option><option>Facebook</option><option>Instagram</option><option>Word of Mouth</option><option>Verified Review</option><option>Other</option>
      </select>
    </p>
    <button type="submit" class="btn btn-primary btn-full">Request My Free Quote</button>
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
  --primary-bg: #0d0d0d;
  --alt-bg: #f9f9f9;
  --accent: #f97316;
  --text-dark: #111827;
  --text-light: #ffffff;
  --border: #e5e7eb;
  --footer-bg: #111827;
  --muted: #9ca3af;
}

* { box-sizing: border-box; }
html, body { margin: 0; padding: 0; }
body {
  font-family: 'Inter', system-ui, sans-serif;
  color: var(--text-dark);
  background: #fff;
  line-height: 1.6;
}
h1, h2, h3 {
  font-family: 'Poppins', 'Inter', sans-serif;
  margin: 0 0 1rem;
  line-height: 1.2;
  color: var(--text-dark);
}
p { margin: 0 0 1rem; }
a { color: inherit; }
img { max-width: 100%; display: block; }
.container { width: min(1160px, calc(100% - 2rem)); margin: 0 auto; }

#mouse-glow {
  position: fixed;
  top: 0;
  left: 0;
  width: 420px;
  height: 420px;
  border-radius: 50%;
  background: radial-gradient(
    circle,
    rgba(255, 255, 255, 0.07) 0%,
    rgba(255, 255, 255, 0.03) 30%,
    transparent 70%
  );
  pointer-events: none;
  z-index: 9998;
  transform: translate(-50%, -50%);
  transition: opacity 0.3s ease;
  will-change: left, top;
}

/* Hide on touch/mobile devices */
@media (hover: none), (max-width: 768px) {
  #mouse-glow {
    display: none !important;
  }
}

.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  border: 0;
}
.focus\\:not-sr-only:focus {
  position: fixed;
  left: 1rem;
  top: 1rem;
  width: auto;
  height: auto;
  clip: auto;
  margin: 0;
  padding: 0.6rem 1rem;
  background: #fff;
  color: #000;
  z-index: 3000;
  border-radius: 0.5rem;
}

a:focus-visible,
button:focus-visible,
input:focus-visible,
select:focus-visible,
textarea:focus-visible {
  outline: 3px solid var(--accent);
  outline-offset: 2px;
}

.site-header {
  position: sticky;
  top: 0;
  z-index: 1000;
  background: transparent;
  transition: background 0.3s ease, box-shadow 0.3s ease;
}
.site-header.scrolled {
  background: #111827;
  box-shadow: 0 10px 30px rgba(0,0,0,0.25);
}
.nav-wrap {
  display: grid;
  grid-template-columns: auto 1fr auto;
  align-items: center;
  gap: 1rem;
  min-height: 88px;
}
.logo-circle {
  border-radius: 50%;
  overflow: hidden;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  background: #ffffff;
}
.logo-circle-nav {
  width: 64px;
  height: 64px;
  border: 2px solid #f97316;
}
.logo-circle-footer {
  width: 80px;
  height: 80px;
  border: 2px solid #f97316;
}
.logo-circle img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: center;
}
.site-nav {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 1.2rem;
}
.site-nav a { text-decoration: none; color: var(--text-light); font-weight: 600; }
.cta-pill {
  background: var(--accent);
  color: #fff !important;
  padding: 0.65rem 1.2rem;
  border-radius: 9999px;
}
.menu-toggle {
  display: none;
  width: 48px;
  height: 48px;
  border: 1px solid rgba(255,255,255,0.4);
  background: rgba(255,255,255,0.1);
  border-radius: 0.6rem;
  align-items: center;
  justify-content: center;
  gap: 0.25rem;
  flex-direction: column;
}
.menu-toggle span { width: 22px; height: 2px; background: #fff; }

.hero {
  position: relative;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #fff;
  overflow: hidden;
}
.hero-media {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
}
.hero-overlay {
  position: absolute;
  inset: 0;
  background: rgba(13,13,13,0.55);
}
.hero-content {
  position: relative;
  z-index: 2;
  text-align: center;
}
.hero h1 {
  color: #fff;
  font-size: clamp(2.5rem, 6vw, 4rem);
  max-width: 980px;
  margin-inline: auto;
}
.hero p { color: #fff; font-size: 1.1rem; }
.hero-phone a { color: #fff; text-decoration: underline; font-weight: 600; }

.btn {
  text-decoration: none;
  border-radius: 9999px;
  padding: 0.75rem 1.25rem;
  font-weight: 600;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  border: 2px solid transparent;
  cursor: pointer;
}
.btn-primary { background: var(--accent); color: #fff; }
.btn-outline { border-color: #fff; color: #fff; background: transparent; }
.btn-outline-orange { border-color: var(--accent); color: var(--accent); background: transparent; }
.btn-dark { background: var(--primary-bg); color: #fff; }
.btn-light { background: #fff; color: var(--text-dark); }
.btn-full { width: 100%; }
.hero-cta-row { display: flex; flex-wrap: wrap; gap: 0.75rem; justify-content: center; }

.trust-bar { background: #111827; color: #fff; padding: 1.5rem 0; overflow-x: auto; }
.trust-items { display: flex; gap: 1.5rem; min-width: max-content; }
.trust-items p { margin: 0; font-weight: 600; }

.section { padding: 4.5rem 0; }
.section-light { background: var(--alt-bg); }
.section-dark { background: var(--primary-bg); }
.section-dark h2, .section-dark p { color: #fff; }

.services-grid, .service-listing {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 1rem;
}
.service-card {
  background: #fff;
  border: 1px solid var(--border);
  border-radius: 1rem;
  padding: 1.1rem;
  transition: transform 0.2s ease, box-shadow 0.2s ease, border-color 0.2s ease;
}
.service-card:hover {
  transform: translateY(-4px);
  border-color: var(--accent);
  box-shadow: 0 16px 30px rgba(17,24,39,0.12);
}
.service-icon {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  background: radial-gradient(circle at center, var(--accent), #f59e0b);
  margin-bottom: 0.75rem;
}
.service-card h3, .service-card h2 { margin-bottom: 0.6rem; }
.service-card a { color: var(--accent); font-weight: 600; text-decoration: none; }

.split-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 2rem;
  align-items: center;
}
.rounded-image { border-radius: 1rem; }
.usp-list { list-style: none; padding: 0; margin: 0 0 1.25rem; }
.usp-list li { margin-bottom: 0.7rem; padding-left: 1.5rem; position: relative; }
.usp-list li::before { content: '✔'; color: var(--accent); position: absolute; left: 0; }
.about-blurb { background: #fff7ed; border-left: 4px solid var(--accent); padding: 0.9rem; border-radius: 0.75rem; }

.projects-grid {
  display: grid;
  grid-template-columns: repeat(3, minmax(0,1fr));
  gap: 1rem;
}
.project-item { position: relative; overflow: hidden; border-radius: 1rem; }
.project-item img { width: 100%; height: 100%; object-fit: cover; }
.project-item figcaption {
  position: absolute;
  inset: auto 0 0 0;
  padding: 0.8rem;
  background: linear-gradient(transparent, rgba(0,0,0,0.8));
  color: #fff;
  transform: translateY(100%);
  transition: transform 0.25s ease;
}
.project-item:hover figcaption { transform: translateY(0); }
.project-item figcaption span { display: block; font-weight: 700; }
.project-item figcaption small { color: #f5f5f5; }

.centered { text-align: center; }

.testimonial-carousel { overflow: hidden; }
.testimonial-track { display: flex; transition: transform 0.5s ease; }
.testimonial-card {
  min-width: 100%;
  background: rgba(17, 24, 39, 0.94);
  border: 1px solid rgba(249, 115, 22, 0.24);
  border-radius: 1rem;
  padding: 1.3rem;
}
.glass-card {
  box-shadow: 0 14px 30px rgba(0, 0, 0, 0.28);
  backdrop-filter: blur(10px);
  -webkit-backdrop-filter: blur(10px);
}
.review-stars {
  color: #f5c518;
  font-size: 1.3rem;
  letter-spacing: 2px;
  margin-bottom: 0.75rem;
  display: block;
}
.review-stars span {
  color: #f5c518 !important;
  display: inline-block;
  line-height: 1;
}
.review-text {
  color: #d1d5db;
  font-size: 0.95rem;
  line-height: 1.7;
  font-style: italic;
  margin: 0 0 1.25rem;
  padding: 0;
  border: none;
}
.reviewer-info {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 0.5rem;
  flex-wrap: wrap;
}
.reviewer-name {
  color: #ffffff;
  font-family: 'Poppins', sans-serif;
  font-weight: 600;
  font-size: 0.9rem;
}
.review-source {
  display: flex;
  align-items: center;
  gap: 0.35rem;
  color: #6b7280;
  font-size: 0.78rem;
}
.review-source img {
  width: 16px;
  height: 16px;
  display: inline-block;
}

.area-pills {
  list-style: none;
  padding: 0;
  margin: 0;
  display: flex;
  flex-wrap: wrap;
  gap: 0.6rem;
}
.area-pills li {
  display: inline-flex;
}
.area-pill-link {
  display: inline-block;
  padding: 0.45rem 0.9rem;
  border: 1px solid var(--accent);
  border-radius: 9999px;
  text-decoration: none;
  color: var(--text-dark);
  font-weight: 500;
}
.area-pill-link:hover { background: var(--accent); color: #fff; }

.faq-wrap { max-width: 900px; }
.faq-item { border-bottom: 1px solid var(--border); }
.faq-question {
  width: 100%;
  text-align: left;
  background: transparent;
  border: none;
  padding: 1rem 0;
  font-size: 1rem;
  font-weight: 600;
  cursor: pointer;
}
.faq-answer { display: none; padding-bottom: 1rem; }

.quote-form-card {
  background: #fff;
  border: 1px solid var(--border);
  border-radius: 1rem;
  padding: 1.25rem;
}
.quote-form-card form p { margin-bottom: 0.9rem; }
.quote-form-card label { display: block; margin-bottom: 0.35rem; font-weight: 600; }
.quote-form-card input,
.quote-form-card select,
.quote-form-card textarea {
  width: 100%;
  border: 1px solid #d1d5db;
  border-radius: 0.75rem;
  padding: 0.65rem;
  font: inherit;
}
.quote-form-card textarea { min-height: 120px; }
.form-message { min-height: 1.2rem; font-weight: 600; color: #065f46; }

.cta-banner {
  background: var(--accent);
  color: #fff;
  padding: 2.4rem 0;
}
.cta-banner h2, .cta-banner p { color: #fff; }
.cta-banner-inner { display: flex; align-items: center; justify-content: space-between; gap: 1rem; flex-wrap: wrap; }

.inner-hero {
  background: #f3f4f6;
  padding: 8rem 0 3rem;
}
.inner-hero h1 { margin-bottom: 0.6rem; }
.breadcrumbs {
  font-size: 0.92rem;
  color: #4b5563;
  margin-bottom: 1rem;
}
.breadcrumbs a { color: #374151; text-decoration: none; }

.two-col {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1.5rem;
}
.contact-card {
  background: #fff;
  border: 1px solid var(--border);
  border-radius: 1rem;
  padding: 1.1rem;
}

.site-footer {
  background: var(--footer-bg);
  color: var(--muted);
  padding-top: 3rem;
}
.site-footer h2 { color: #fff; font-size: 1.1rem; margin-bottom: 0.8rem; }
.footer-grid {
  display: grid;
  grid-template-columns: repeat(4, minmax(0,1fr));
  gap: 1.2rem;
}
.site-footer ul { list-style: none; padding: 0; margin: 0; }
.site-footer li { margin-bottom: 0.35rem; }
.site-footer a { color: #d1d5db; text-decoration: none; }
.connect-section {
  background: #0a0a0a;
  padding: 5rem 2rem;
  text-align: center;
  border-top: 1px solid rgba(255, 255, 255, 0.07);
}
.connect-inner {
  max-width: 800px;
  margin: 0 auto;
}
.connect-section h2 {
  font-family: 'Poppins', sans-serif;
  font-size: clamp(1.8rem, 3vw, 2.4rem);
  font-weight: 700;
  color: #ffffff;
  margin: 0 0 1rem;
}
.connect-section p {
  color: #9ca3af;
  font-size: 1rem;
  margin: 0 0 2.5rem;
}
.social-links {
  display: flex;
  justify-content: center;
  gap: 1.5rem;
  flex-wrap: wrap;
}
.social-card {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.5rem;
  padding: 2rem 2.5rem;
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.10);
  backdrop-filter: blur(16px);
  -webkit-backdrop-filter: blur(16px);
  border-radius: 16px;
  text-decoration: none;
  min-width: 160px;
  transition: transform 0.3s ease, border-color 0.3s ease, box-shadow 0.3s ease;
}
.social-card:hover {
  transform: translateY(-6px);
  border-color: rgba(249, 115, 22, 0.45);
  box-shadow: 0 8px 32px rgba(249, 115, 22, 0.12);
}
.social-card svg {
  width: 36px;
  height: 36px;
  color: #ffffff;
  fill: #ffffff;
  transition: color 0.2s, fill 0.2s;
}
.social-card:nth-child(1):hover svg { fill: #1877f2; color: #1877f2; }
.social-card:nth-child(2):hover svg { fill: #e1306c; color: #e1306c; }
.social-card:nth-child(3):hover svg { fill: #34a853; color: #34a853; }
.social-card span {
  color: #ffffff;
  font-family: 'Poppins', sans-serif;
  font-weight: 600;
  font-size: 1rem;
}
.social-card small {
  color: #6b7280;
  font-size: 0.78rem;
}

.footer-social-links {
  display: flex;
  gap: 0.5rem;
}
.footer-social-link {
  width: 36px;
  height: 36px;
  background: rgba(255,255,255,0.07);
  border: 1px solid rgba(255,255,255,0.12);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: background 0.2s, border-color 0.2s;
}
.footer-social-link:hover {
  background: rgba(249,115,22,0.15);
  border-color: rgba(249,115,22,0.4);
}
.footer-social-link svg {
  width: 18px;
  height: 18px;
  fill: #d1d5db;
  transition: fill 0.2s ease;
}
.footer-social-link:hover svg {
  fill: #f97316;
}
.footer-bottom { text-align: center; padding: 1.2rem 0 2rem; }
.footer-bottom hr { border-color: #374151; border-style: solid; border-width: 1px 0 0; margin-bottom: 1rem; }
.footer-bottom p { color: #6b7280; margin-bottom: 0.65rem; }
.footer-legal-links { display: flex; justify-content: center; gap: 1rem; flex-wrap: wrap; }
.text-button {
  border: none;
  background: none;
  color: #d1d5db;
  text-decoration: underline;
  cursor: pointer;
  font: inherit;
}
.domain-move-banner {
  background: #fff7ed;
  border-bottom: 1px solid rgba(249, 115, 22, 0.35);
  color: #7c2d12;
  text-align: center;
  padding: 0.75rem 1rem;
  font-weight: 600;
}
.domain-move-banner a {
  color: #c2410c;
  text-decoration: underline;
}

.not-found-wrap {
  min-height: 100vh;
  display: grid;
  place-content: center;
  gap: 0.8rem;
  text-align: center;
  padding: 2rem;
}

@media (max-width: 1024px) {
  .services-grid, .service-listing, .projects-grid { grid-template-columns: repeat(2, minmax(0,1fr)); }
  .split-grid, .two-col { grid-template-columns: 1fr; }
}
@media (max-width: 768px) {
  .menu-toggle { display: inline-flex; }
  .site-nav {
    position: fixed;
    inset: 0 0 0 35%;
    background: #111827;
    padding: 6rem 1.5rem 1.5rem;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    transform: translateX(100%);
    transition: transform 0.3s ease;
  }
  .site-nav.open { transform: translateX(0); }
  .nav-wrap { grid-template-columns: auto auto; justify-content: space-between; }
  .footer-grid { grid-template-columns: 1fr; }
}
@media (max-width: 480px) {
  .social-card { width: 100%; min-width: unset; }
}
@media (max-width: 375px) {
  .container { width: calc(100% - 1rem); }
  .hero h1 { font-size: 2.2rem; }
}
@media (max-width: 320px) {
  .hero h1 { font-size: 2rem; }
}
@media (min-width: 1440px) {
  .container { width: min(1280px, calc(100% - 3rem)); }
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
          ? 'Thanks. Your quote request has been received. We will respond within 24 hours.'
          : 'Thanks. Your request is saved locally. Please call 07713245511 while webhook setup is pending.';
      }
      form.reset();
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
  <img class="hero-media" src="/images/hero-bg.webp" alt="Scaffolding site installation in Benfleet, Essex" width="1920" height="1280" loading="eager" fetchpriority="high" decoding="async">
  <div class="hero-overlay"></div>
  <div class="container hero-content">
    <h1>Scaffolding in Essex – Fast, Safe &amp; Reliable | Axis Scaffolding Ltd</h1>
    <p>Essex's trusted scaffolding specialists — residential, commercial and emergency cover.</p>
    <div class="hero-cta-row">
      <a class="btn btn-primary" href="/quote">Get a Free Quote</a>
      <a class="btn btn-outline" href="/gallery">View Our Work</a>
    </div>
    <p class="hero-phone"><a href="tel:{NAP['phone']}">Call {NAP['phone']} for fast scaffolding support</a></p>
  </div>
</section>

<section class="trust-bar" aria-label="Company trust bar">
  <div class="container trust-items">
    <p><span aria-hidden="true">🛠</span>10+ Years Experience</p>
    <p><span aria-hidden="true">✅</span>Fully CISRS Certified</p>
    <p><span aria-hidden="true">📋</span>Free Quotes</p>
    <p><span aria-hidden="true">📍</span>Based in Rayleigh</p>
  </div>
</section>

<section class="section section-light">
  <div class="container">
    <h2>Our Scaffolding Services</h2>
    <div class="services-grid">{service_cards()}</div>
  </div>
</section>

<section class="section">
  <div class="container split-grid">
    <div>
      <img src="/images/project-7.webp" alt="Domestic scaffolding structure beside a home in Benfleet, Essex" width="640" height="800" loading="lazy" decoding="async" class="rounded-image">
    </div>
    <div>
      <h2>Why Choose Axis Scaffolding Essex?</h2>
      <ul class="usp-list">
        <li>Fully qualified, CISRS-certified scaffolders</li>
        <li>Prompt installation and responsive site coordination</li>
        <li>Residential and commercial experience across Essex</li>
        <li>Detailed risk-aware planning for safer works</li>
      </ul>
      <p class="about-blurb">Axis Scaffolding Ltd is a fully qualified, CISRS-certified scaffolding company based in Rayleigh, Essex, registered in England and Wales under Company Number 15050136.</p>
      <a class="btn btn-primary" href="/quote">Get a Quote</a>
    </div>
  </div>
</section>

<section class="section section-dark">
  <div class="container">
    <h2>Our Recent Projects</h2>
    <div class="projects-grid">{project_cards()}</div>
    <p class="centered"><a class="btn btn-outline-orange" href="/gallery">View Full Gallery →</a></p>
  </div>
</section>

<section class="section section-light">
  <div class="container">
    <h2>What Our Customers Say</h2>
    <div class="testimonial-carousel" id="testimonial-carousel" aria-live="polite">
      <div class="testimonial-track" id="testimonial-track">{testimonials()}</div>
    </div>
  </div>
</section>

<section class="section" id="areas-covered">
  <div class="container">
    <h2>Areas We Cover in Essex</h2>
    <ul class="area-pills">{area_pills()}</ul>
    <p>Based in Rayleigh, we provide scaffolding services across South Essex and surrounding areas. Contact us to confirm coverage for your project.</p>
  </div>
</section>

<section class="section section-light">
  <div class="container">
    <h2>Get a Free Scaffolding Quote</h2>
    {quote_form("home", "Tell us about your project")}
  </div>
</section>

<section class="section section-light">
  <div class="container faq-wrap">
    <h2>Frequently Asked Questions</h2>
    {faq_accordion()}
  </div>
</section>

<section class="cta-banner">
  <div class="container cta-banner-inner">
    <div>
      <h2>Need Scaffolding in Essex?</h2>
      <p>Call us today for a free, no-obligation quote.</p>
    </div>
    <div class="hero-cta-row">
      <a class="btn btn-light" href="tel:{NAP['phone']}">{NAP['phone']}</a>
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
<section class="section"><div class="container two-col"><article class="contact-card"><h2>Contact Us</h2><p><strong>Name:</strong> Axis Scaffolding Ltd</p><p><strong>Phone:</strong> <a href="tel:07713245511">07713245511</a></p><p><strong>Email:</strong> <a href="mailto:axis-scaffolding@outlook.com">axis-scaffolding@outlook.com</a></p><p><strong>Address:</strong> Arterial Road, Rayleigh, Essex, SS6 7XT</p><p>Email us: <a href="mailto:axis-scaffolding@outlook.com" style="color:#f97316;">axis-scaffolding@outlook.com</a></p></article>{quote_form("contact", "Request a Free Scaffolding Quote")}</div></section>
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
<section class="inner-hero"><div class="container"><h1>Thank You — We'll Be In Touch!</h1><p>Your enquiry has been received. A member of the Axis Scaffolding team will contact you within 24 hours.</p><p>In the meantime, call us on <a href="tel:07713245511">07713245511</a> for urgent enquiries.</p><div class="hero-cta-row"><a class="btn btn-primary" href="/">Back to Home</a><a class="btn btn-outline-orange" href="/services">View Our Services</a></div></div></section>
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
    write("robots.txt", "User-agent: *\nAllow: /\n\nSitemap: https://axisscaffoldingessex.co.uk/sitemap.xml\n")
    pages = [
        ("/", "1.0"),
        ("/services", "0.8"),
        ("/services/residential-scaffolding", "0.8"),
        ("/services/commercial-scaffolding", "0.8"),
        ("/services/domestic-scaffolding", "0.8"),
        ("/services/roof-scaffolding", "0.8"),
        ("/services/temporary-roofing", "0.8"),
        ("/services/emergency-scaffolding", "0.8"),
        ("/gallery", "0.7"),
        ("/about", "0.7"),
        ("/contact", "0.7"),
        ("/quote", "0.7"),
        ("/privacy-policy", "0.5"),
        ("/terms-and-conditions", "0.5"),
        ("/cookie-policy", "0.5"),
        ("/thank-you", "0.1"),
    ]
    lines = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for path, priority in pages:
        changefreq = 'yearly' if path == '/thank-you' else 'monthly'
        lines.append(
            f"  <url><loc>{SITE}{path}</loc><lastmod>{TODAY}</lastmod><changefreq>{changefreq}</changefreq><priority>{priority}</priority></url>"
        )
    lines.append("</urlset>")
    write("sitemap.xml", "\n".join(lines))


def main() -> None:
    ensure_dirs()
    generate_media_assets()
    generate_css()
    generate_js()
    generate_pages()
    generate_redirects()
    generate_robots_sitemap()
    print("Site regeneration completed.")


if __name__ == "__main__":
    main()

