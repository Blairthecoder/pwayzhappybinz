from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parent.parent
WIDTH, HEIGHT = 1200, 630


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    windows_fonts = Path("C:/Windows/Fonts")
    filename = "seguisb.ttf" if bold else "segoeui.ttf"
    return ImageFont.truetype(str(windows_fonts / filename), size=size)


image = Image.new("RGB", (WIDTH, HEIGHT), "#35106b")
draw = ImageDraw.Draw(image)

# Quiet grid texture, matching the website without using promotional artwork.
for x in range(0, WIDTH, 52):
    draw.line((x, 0, x, HEIGHT), fill="#421777", width=1)
for y in range(0, HEIGHT, 52):
    draw.line((0, y, WIDTH, y), fill="#421777", width=1)

# Branded service badge.
draw.rounded_rectangle((850, 95, 1105, 350), radius=48, fill="#a7ef32")
draw.rounded_rectangle((902, 174, 1053, 315), radius=18, fill="#35106b")
draw.rounded_rectangle((885, 140, 1070, 186), radius=15, fill="#35106b")
draw.rounded_rectangle((932, 112, 1024, 152), radius=13, fill="#35106b")
for x in (948, 978, 1008):
    draw.rounded_rectangle((x, 203, x + 10, 285), radius=5, fill="#a7ef32")

draw.text((75, 62), "P'WAYZ HAPPY BINS", fill="#a7ef32", font=font(24, True))
draw.text((75, 137), "Cleaner bins.", fill="#ffffff", font=font(82, True))
draw.text((75, 232), "A fresher curb.", fill="#a7ef32", font=font(82, True))
draw.text((78, 375), "Eco-friendly trash bin cleaning", fill="#ffffff", font=font(31, True))
draw.text((78, 424), "Southern Colony & Caldwell Ranch  •  Arcola, TX", fill="#d8cceb", font=font(25))

draw.rounded_rectangle((75, 505, 426, 569), radius=32, fill="#a7ef32")
draw.text((111, 518), "CALL OR TEXT  713-231-6321", fill="#24103d", font=font(23, True))

image.save(ROOT / "og-image.png", optimize=True)
