from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont, ImageFilter


def load_font(name: str, size: int) -> ImageFont.FreeTypeFont:
    """Load a truetype font, falling back to a default sans-serif font."""
    search_paths = [
        f"/usr/share/fonts/truetype/{name}",
        f"/usr/share/fonts/{name}",
        f"/usr/local/share/fonts/{name}",
        name,
    ]

    for path in search_paths:
        try:
            return ImageFont.truetype(path, size)
        except OSError:
            continue

    # Final fallback to DejaVuSans
    return ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", size)


def draw_gradient(draw: ImageDraw.ImageDraw, width: int, height: int, colors: list[tuple[int, int, int]]):
    """Draw a multi-stop vertical gradient."""
    for y in range(height):
        ratio = y / max(height - 1, 1)
        segment = ratio * (len(colors) - 1)
        idx = int(segment)
        frac = segment - idx
        r1, g1, b1 = colors[idx]
        r2, g2, b2 = colors[min(idx + 1, len(colors) - 1)]
        r = int(r1 + (r2 - r1) * frac)
        g = int(g1 + (g2 - g1) * frac)
        b = int(b1 + (b2 - b1) * frac)
        draw.line([(0, y), (width, y)], fill=(r, g, b))


def add_soft_spotlight(image: Image.Image, center: tuple[int, int], radius: int, color: tuple[int, int, int, int]):
    overlay = Image.new("RGBA", image.size, (0, 0, 0, 0))
    overlay_draw = ImageDraw.Draw(overlay)
    overlay_draw.ellipse([
        center[0] - radius,
        center[1] - radius,
        center[0] + radius,
        center[1] + radius,
    ], fill=color)

    overlay = overlay.filter(ImageFilter.GaussianBlur(radius / 2))
    image.alpha_composite(overlay)


def rounded_rectangle(draw: ImageDraw.ImageDraw, xy, radius, fill):
    draw.rounded_rectangle(xy, radius=radius, fill=fill)


def main(output_path: Path):
    width, height = 1080, 1080
    base = Image.new("RGBA", (width, height), (10, 22, 51, 255))
    draw = ImageDraw.Draw(base)

    # Background gradient and geometric overlays
    gradient = Image.new("RGBA", (width, height))
    gradient_draw = ImageDraw.Draw(gradient)
    draw_gradient(
        gradient_draw,
        width,
        height,
        [
            (9, 22, 55),
            (12, 35, 80),
            (15, 40, 90),
            (25, 48, 105),
        ],
    )
    base = Image.alpha_composite(base, gradient)

    geometric = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    geo_draw = ImageDraw.Draw(geometric)
    geo_draw.polygon(
        [(0, 0), (width, 0), (width, height // 2), (0, height // 3)],
        fill=(255, 255, 255, 20),
    )
    geo_draw.polygon(
        [(0, height), (width, height), (width, height // 2), (0, 3 * height // 4)],
        fill=(8, 18, 42, 120),
    )
    base = Image.alpha_composite(base, geometric)

    add_soft_spotlight(base, (width - 220, height - 260), 320, (255, 210, 75, 60))
    add_soft_spotlight(base, (220, 200), 260, (78, 133, 255, 50))

    draw = ImageDraw.Draw(base)

    # Typography
    font_brand = load_font("dejavu/DejaVuSans-Bold.ttf", 40)
    font_title = load_font("dejavu/DejaVuSans-Bold.ttf", 78)
    font_subtitle = load_font("dejavu/DejaVuSans.ttf", 46)
    font_highlight = load_font("dejavu/DejaVuSans-Bold.ttf", 52)
    font_body = load_font("dejavu/DejaVuSans.ttf", 32)
    font_small = load_font("dejavu/DejaVuSans.ttf", 26)

    # Brand header
    draw.text((90, 70), "GenAspire", font=font_brand, fill=(255, 215, 0, 255))
    draw.text((90, 120), "Technologies", font=font_small, fill=(220, 230, 255, 200))

    # Accent bar
    draw.rectangle([(60, 70), (80, 200)], fill=(255, 191, 0, 255))

    draw.text((180, 220), "JAVA FULLSTACK", font=font_title, fill=(255, 255, 255, 255))

    rounded_rectangle(
        draw,
        (180, 320, 620, 388),
        radius=32,
        fill=(255, 255, 255, 30),
    )
    draw.text((210, 330), "Training & Internship Program", font=font_subtitle, fill=(235, 238, 255, 255))

    draw.text((180, 420), "Accelerate your career in 12 intensive weeks", font=font_body, fill=(200, 213, 255, 220))

    points_text = (
        "Hands-on enterprise projects  -  Live code reviews\n"
        "Interview prep, resume clinic & placement support\n"
        "Cloud-ready deployment modules + DevOps essentials"
    )
    draw.multiline_text((180, 470), points_text, font=font_small, fill=(210, 220, 255, 220), spacing=18)

    rounded_rectangle(
        draw,
        (180, 620, 520, 710),
        radius=30,
        fill=(22, 50, 110, 255),
    )
    draw.text((200, 632), "Next Cohort: 25 Nov 2025", font=font_body, fill=(255, 255, 255, 255))

    rounded_rectangle(
        draw,
        (560, 620, 900, 710),
        radius=30,
        fill=(255, 193, 62, 255),
    )
    draw.text((585, 632), "Hybrid - Weekend & Evening Batches", font=font_small, fill=(20, 30, 70, 255))

    # Offer & CTA
    rounded_rectangle(
        draw,
        (180, 760, 400, 830),
        radius=26,
        fill=(255, 255, 255, 255),
    )
    draw.text((200, 770), "40% OFF", font=font_highlight, fill=(24, 37, 74, 255))

    rounded_rectangle(
        draw,
        (420, 760, 760, 830),
        radius=26,
        fill=(255, 193, 62, 255),
    )
    draw.text((445, 772), "Register Now", font=font_highlight, fill=(24, 37, 74, 255))

    # Expert tag
    draw.text((780, 320), "with", font=font_small, fill=(205, 214, 240, 220))
    draw.text((770, 355), "industry", font=font_body, fill=(255, 255, 255, 255))
    draw.text((770, 395), "experts", font=font_body, fill=(255, 255, 255, 255))

    # Footer
    footer_text = "Limited seats - www.genaspiretech.com - +1 800 555 0199"
    draw.text((180, 910), footer_text, font=font_small, fill=(210, 220, 255, 200))

    draw.text(
        (180, 960),
        "Scholarships available for top performers | EMI options up to 6 months",
        font=font_small,
        fill=(180, 195, 240, 200),
    )

    # Save output
    output_path.parent.mkdir(parents=True, exist_ok=True)
    base.convert("RGB").save(output_path, format="PNG")


if __name__ == "__main__":
    out_file = Path("assets/genaspire_java_fullstack_updated.png")
    main(out_file)
    print(f"Saved poster to {out_file.resolve()}")
