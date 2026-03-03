import os
import platform
import shutil
import subprocess
import sys
import tarfile
import tempfile
import urllib.request
import zipfile
from pathlib import Path
from typing import Final

SOURCE_FILE: Final[Path] = Path("static/css/styles.scss")
TARGET_FILE: Final[Path] = Path("static/css/styles.css")
TOOLS_DIR: Final[Path] = Path(".tools")
BIN_DIR: Final[Path] = TOOLS_DIR / "bin"
DART_SASS_VERSION: Final[str] = os.getenv("DART_SASS_VERSION", "1.77.8")
LIGHTNINGCSS_VERSION: Final[str] = os.getenv("LIGHTNINGCSS_VERSION", "1.27.0")
VENDOR_UI_ROOT: Final[Path] = Path("vendor/@barrys27/ui")


def _platform_slug() -> tuple[str, str]:
    system = platform.system().lower()
    machine = platform.machine().lower()

    if system == "linux":
        os_slug = "linux"
    elif system == "darwin":
        os_slug = "macos"
    elif system == "windows":
        os_slug = "windows"
    else:
        raise RuntimeError(f"Unsupported OS for standalone binaries: {system}")

    if machine in {"x86_64", "amd64"}:
        arch_slug = "x64"
    elif machine in {"aarch64", "arm64"}:
        arch_slug = "arm64"
    else:
        raise RuntimeError(f"Unsupported CPU architecture for standalone binaries: {machine}")

    return os_slug, arch_slug


def _download_file(url: str, destination: Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    with urllib.request.urlopen(url) as response, destination.open("wb") as target:
        shutil.copyfileobj(response, target)


def _extract_archive(archive_path: Path, destination: Path) -> None:
    destination.mkdir(parents=True, exist_ok=True)
    if archive_path.suffix == ".zip":
        with zipfile.ZipFile(archive_path, "r") as archive:
            archive.extractall(destination)
    else:
        with tarfile.open(archive_path, "r:gz") as archive:
            archive.extractall(destination)


def ensure_dart_sass() -> Path:
    sass_binary = BIN_DIR / ("sass.bat" if platform.system().lower() == "windows" else "sass")
    if sass_binary.exists():
        return sass_binary

    os_slug, arch_slug = _platform_slug()
    archive_ext = "zip" if os_slug == "windows" else "tar.gz"
    default_url = (
        f"https://github.com/sass/dart-sass/releases/download/{DART_SASS_VERSION}/"
        f"dart-sass-{DART_SASS_VERSION}-{os_slug}-{arch_slug}.{archive_ext}"
    )
    download_url = os.getenv("DART_SASS_DOWNLOAD_URL", default_url)

    with tempfile.TemporaryDirectory() as tmp:
        archive_path = Path(tmp) / f"dart-sass.{archive_ext}"
        _download_file(download_url, archive_path)
        _extract_archive(archive_path, TOOLS_DIR / "dart-sass")

    extracted_binary = next((TOOLS_DIR / "dart-sass").rglob("sass"), None)
    if extracted_binary is None:
        raise RuntimeError("Dart Sass binary was not found after extraction.")

    BIN_DIR.mkdir(parents=True, exist_ok=True)
    shutil.copy2(extracted_binary, sass_binary)
    sass_binary.chmod(0o755)
    return sass_binary


def ensure_lightningcss() -> Path:
    binary_name = "lightningcss.exe" if platform.system().lower() == "windows" else "lightningcss"
    lightning_binary = BIN_DIR / binary_name
    if lightning_binary.exists():
        return lightning_binary

    os_slug, arch_slug = _platform_slug()
    archive_ext = "zip" if os_slug == "windows" else "tar.gz"
    default_url = (
        f"https://github.com/parcel-bundler/lightningcss/releases/download/v{LIGHTNINGCSS_VERSION}/"
        f"lightningcss-{os_slug}-{arch_slug}.{archive_ext}"
    )
    download_url = os.getenv("LIGHTNINGCSS_DOWNLOAD_URL", default_url)

    with tempfile.TemporaryDirectory() as tmp:
        archive_path = Path(tmp) / f"lightningcss.{archive_ext}"
        _download_file(download_url, archive_path)
        _extract_archive(archive_path, TOOLS_DIR / "lightningcss")

    extracted_binary = next((TOOLS_DIR / "lightningcss").rglob("lightningcss*"), None)
    if extracted_binary is None:
        raise RuntimeError("Lightning CSS binary was not found after extraction.")

    BIN_DIR.mkdir(parents=True, exist_ok=True)
    shutil.copy2(extracted_binary, lightning_binary)
    lightning_binary.chmod(0o755)
    return lightning_binary


def compile_scss(source_file: Path = SOURCE_FILE, target_file: Path = TARGET_FILE) -> bool:
    """Compile SCSS with Dart Sass then post-process/minify with Lightning CSS."""
    target_file.parent.mkdir(parents=True, exist_ok=True)

    # Why: CI vendors @barrys27/ui into ./vendor for deterministic, Node-free dependency resolution.
    if VENDOR_UI_ROOT.exists():
        print(f"📦 Using vendored UI package from {VENDOR_UI_ROOT}")

    try:
        sass_bin = ensure_dart_sass()
        lightning_bin = ensure_lightningcss()
    except Exception as error:
        print(f"❌ Failed to provision CSS binaries: {error}")
        return False

    with tempfile.TemporaryDirectory() as tmp:
        intermediate_css = Path(tmp) / "styles.intermediate.css"

        sass_cmd = [
            str(sass_bin),
            "--no-source-map",
            "--load-path",
            "static/css",
            "--load-path",
            "vendor",
            str(source_file),
            str(intermediate_css),
        ]

        # Why: keep Sass phase unminified so Lightning CSS can own final compatibility + minification.
        lightning_cmd = [
            str(lightning_bin),
            str(intermediate_css),
            "-o",
            str(target_file),
            "--minify",
            "--browserslist",
        ]

        try:
            subprocess.run(sass_cmd, check=True)
            subprocess.run(lightning_cmd, check=True)
        except subprocess.CalledProcessError as error:
            print(f"❌ CSS pipeline failed with exit code {error.returncode}.")
            return False

    print("✅ CSS build complete.")
    return True


if __name__ == "__main__":
    if not compile_scss():
        sys.exit(1)
