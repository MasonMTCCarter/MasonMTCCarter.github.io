from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "assets" / "capybara-astronaut-480.webp"
DOWNLOADS = ROOT / "assets" / "downloads"
DOWNLOADS.mkdir(parents=True, exist_ok=True)

FONT_PATH = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
FOOTER = "Little Wonder Paper Co. | www.littlewonderpaperco.works"


def make_page(size, illustration_box, footer_y):
    page = Image.new("RGB", size, "white")
    art = Image.open(SOURCE).convert("RGB")
    art.thumbnail(illustration_box, Image.Resampling.LANCZOS)
    x = (size[0] - art.width) // 2
    y = int(size[1] * 0.18)
    page.paste(art, (x, y))
    draw = ImageDraw.Draw(page)
    try:
        font = ImageFont.truetype(FONT_PATH, max(18, size[0] // 55))
    except OSError:
        font = ImageFont.load_default()
    bbox = draw.textbbox((0, 0), FOOTER, font=font)
    text_w = bbox[2] - bbox[0]
    draw.text(((size[0] - text_w) // 2, footer_y), FOOTER, fill=(70, 70, 70), font=font)
    return page


letter = make_page((1700, 2200), (1450, 1350), 2050)
a4 = make_page((1654, 2339), (1410, 1390), 2185)

letter.save(DOWNLOADS / "free-capybara-astronaut-us-letter.pdf", "PDF", resolution=200.0, quality=95)
a4.save(DOWNLOADS / "free-capybara-astronaut-a4.pdf", "PDF", resolution=200.0, quality=95)

preview = letter.resize((850, 1100), Image.Resampling.LANCZOS)
preview.save(ROOT / "assets" / "free-capybara-astronaut-preview.webp", "WEBP", quality=92, method=6)
