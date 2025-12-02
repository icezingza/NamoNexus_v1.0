"""Builder script to package NaMoNexus_v1.0 into a zip archive."""
from __future__ import annotations

import os
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TARGET = ROOT / "NamoNexus_v1.0.zip"


def ensure_structure() -> None:
    required_dirs = [
        ROOT / "app",
        ROOT / "engine",
        ROOT / "frontend",
        ROOT / "deploy",
        ROOT / "docs",
    ]
    for directory in required_dirs:
        directory.mkdir(parents=True, exist_ok=True)


def build_zip() -> Path:
    ensure_structure()
    if TARGET.exists():
        TARGET.unlink()
    shutil.make_archive(TARGET.with_suffix(""), "zip", ROOT)
    return TARGET


if __name__ == "__main__":
    archive = build_zip()
    print(f"Created archive at {archive}")
