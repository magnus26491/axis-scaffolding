"""One-off helper: re-derive the 480w/768w card variants of the project photos from
their full-size webp at a lighter quality (PageSpeed: "improve image delivery").
Run with Pillow installed: python3 scripts/recompress_card_images.py"""
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
QUALITY_BY_WIDTH = {480: 58, 768: 64}
for full in sorted((ROOT / "images").glob("project-*.webp")) + [ROOT / "images/stock-industrial.webp"]:
    if "w.webp" in full.name and full.stem.split("-")[-1].endswith("w"):
        continue
    with Image.open(full) as im:
        rgb = im.convert("RGB")
        w0, h0 = rgb.size
        for w in (480, 768):
            target = ROOT / "images" / f"{full.stem}-{w}w.webp"
            if w0 > w and target.exists():
                rgb.resize((w, round(h0 * w / w0)), Image.LANCZOS).save(target, format="WEBP", quality=QUALITY_BY_WIDTH[w])
