"""Web-sized Universidad de Caldas logos for the site.

Run: uv run --no-project --with pillow python tools/web_logos.py
Reads the full-resolution PNGs in tools/assets/src/ and writes tools/assets/<name>.png at twice the
largest CSS height each logo is shown at (crisp on 2x screens), as a 64-colour palette PNG that keeps
transparency. build_bank.py copies tools/assets/*.png (not src/) into docs/.
"""
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
SRC, DST = ROOT / "tools/assets/src", ROOT / "tools/assets"
HEIGHTS = {"ucaldas_logo_horizontal": 92, "ucaldas_logo_vertical": 112, "ucaldas_supersigno": 136}


def main():
    for f in sorted(SRC.glob("*.png")):
        h = next(v for k, v in HEIGHTS.items() if f.stem.startswith(k))
        im = Image.open(f).convert("RGBA")
        w = round(im.width * h / im.height)
        out = im.resize((w, h), Image.LANCZOS).quantize(colors=64, method=Image.Quantize.FASTOCTREE)
        out.save(DST / f.name, optimize=True)
        print(f"{f.name}: {im.size} -> {(w, h)}, {(DST / f.name).stat().st_size // 1024} KB")


if __name__ == "__main__":
    main()
