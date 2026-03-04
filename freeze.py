import os
import shutil
import sys
from pathlib import Path
from typing import Iterable

try:
    from PIL import Image, UnidentifiedImageError

    PILLOW_AVAILABLE = True
except ModuleNotFoundError:  # pragma: no cover - only for constrained local environments
    Image = None  # type: ignore[assignment]

    class UnidentifiedImageError(Exception):
        pass

    PILLOW_AVAILABLE = False

from flask_frozen import Freezer

from app import app
from scss import compile_scss

# Configure Freezer
app.config["FREEZER_DESTINATION"] = "build"
app.config["FREEZER_IGNORE_MIMETYPE_WARNINGS"] = True
app.config["FREEZER_RELATIVE_URLS"] = True
app.config["FREEZER_REMOVE_EXTRA_FILES"] = True
app.config["FREEZER_BASE_URL"] = os.getenv("FREEZER_BASE_URL", "http://localhost/")

freezer = Freezer(app)

REQUIRED_BUILD_ARTIFACTS = [
    "index.html",
    os.path.join("static", "css", "styles.css"),
    os.path.join("static", "images", "favicon-96x96.png"),
    os.path.join("static", "images", "favicon.svg"),
    os.path.join("static", "images", "favicon.ico"),
    os.path.join("static", "images", "apple-touch-icon.png"),
    os.path.join("static", "images", "site.webmanifest"),
    os.path.join("static", "images", "profile.webp"),
    os.path.join("static", "images", "og-card.png"),
    os.path.join("static", "images", "background.webp"),
]


IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".webp"}


def optimize_images(image_root: Path = Path("static/images")) -> bool:
    """Optimize raster images in-place to reduce transfer size in static builds."""
    if not PILLOW_AVAILABLE:
        print("❌ Pillow is required for image optimization but is not installed.")
        return False

    if not image_root.exists():
        print(f"❌ Image directory not found: {image_root}")
        return False

    for image_path in image_root.rglob("*"):
        if not image_path.is_file() or image_path.suffix.lower() not in IMAGE_EXTENSIONS:
            continue

        try:
            with Image.open(image_path) as image:
                image_format = image.format
                save_kwargs: dict[str, int | bool | str] = {"optimize": True}

                # Why: lossy formats benefit from explicit quality, while PNG relies on optimize flag.
                if image_format in {"JPEG", "WEBP"}:
                    save_kwargs["quality"] = 85

                image.save(image_path, format=image_format, **save_kwargs)
        except (UnidentifiedImageError, OSError) as error:
            print(f"❌ Failed to optimize image {image_path}: {error}")
            return False

    print("✅ Image optimization complete.")
    return True


def clean_build_dir() -> None:
    """Clean build directory before freezing."""
    build_dir = app.config["FREEZER_DESTINATION"]
    if os.path.exists(build_dir):
        print("Cleaning build directory...")
        shutil.rmtree(build_dir)


def copy_extra_files() -> bool:
    """Copy root-level files that are not emitted by Flask-Frozen."""
    print("Copying extra static files...")
    build_dir = app.config["FREEZER_DESTINATION"]
    os.makedirs(build_dir, exist_ok=True)

    extra_files = ["robots.txt", "sitemap.xml"]

    for filename in extra_files:
        if not os.path.exists(filename):
            print(f"❌ Missing required source file: {filename}")
            return False

        target = os.path.join(build_dir, filename)
        os.makedirs(os.path.dirname(target) or build_dir, exist_ok=True)
        shutil.copy2(filename, target)
        print(f"✅ Copied {filename}")

    return True


def _missing_artifacts(required_paths: Iterable[str]) -> list[str]:
    build_dir = app.config["FREEZER_DESTINATION"]
    return [
        file_path
        for file_path in required_paths
        if not os.path.exists(os.path.join(build_dir, file_path))
    ]


def verify_build() -> bool:
    """Verify required files exist in frozen output."""
    print("Verifying build output...")
    build_dir = app.config["FREEZER_DESTINATION"]

    if not os.path.exists(build_dir):
        print("❌ Error: Build directory does not exist")
        return False

    required = REQUIRED_BUILD_ARTIFACTS + ["robots.txt", "sitemap.xml"]
    missing_files = _missing_artifacts(required)

    if missing_files:
        print("❌ Error: Missing required artifacts:")
        for file_path in missing_files:
            print(f"   - {file_path}")
        return False

    print("✅ Verification passed! Build complete.")
    return True


if __name__ == "__main__":
    # Why: freezing targets production parity and avoids debug overhead in static generation.
    os.environ["FLASK_ENV"] = "production"

    if not compile_scss():
        print("❌ Build failed due to CSS errors")
        sys.exit(1)

    if not optimize_images():
        print("❌ Build failed during image optimization")
        sys.exit(1)

    clean_build_dir()

    print(f"Freezing site with FREEZER_BASE_URL={app.config['FREEZER_BASE_URL']}")
    try:
        freezer.freeze()
    except Exception as error:
        print(f"❌ Critical error during freezing:\n{error}")
        sys.exit(1)

    if not copy_extra_files():
        print("❌ Failed while copying extra files")
        sys.exit(1)

    if not verify_build():
        print("❌ Build verification failed")
        sys.exit(1)

    print("🎉 All set!")
