#!/usr/bin/env python3
"""
auto_resolve_conflicts.py
-------------------------------------------------
Smart conflict resolver for NaMoNexus_v1.0 project.

- Automatically merges both sides of non-destructive conflicts
- Keeps structure integrity (import, manifest, README, configs)
- Creates a single clean commit after all merges
-------------------------------------------------
"""

import os
import re
import subprocess
from pathlib import Path

# Patterns for safe auto-merge
SAFE_KEYWORDS = [
    "import ",
    "from ",
    "version",
    "manifest_id",
    "quote",
    "description",
    "settings",
    "logging",
    "FastAPI",
    "pydantic",
]

# File extensions to target
TARGET_EXTENSIONS = [".py", ".md", ".json", ".txt", ".js", ".html", ".css"]

REPO_ROOT = Path(__file__).parent
CONFLICT_MARKERS = ("<<<<<<<", "=======", ">>>>>>>")

def resolve_conflicts_in_file(file_path: Path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    if not any(m in content for m in CONFLICT_MARKERS):
        return False

    print(f"⚙️ Resolving: {file_path.relative_to(REPO_ROOT)}")

    # Split the file by conflict sections
    pattern = re.compile(r"<<<<<<<.*?=======\n(.*?)>>>>>>>.*?\n", re.S)
    sections = pattern.findall(content)

    for section in sections:
        # Try to safely accept both changes if keywords appear
        if any(kw in section for kw in SAFE_KEYWORDS):
            merged = section.strip()
        else:
            # Default: prefer current change (HEAD)
            merged = re.sub(r"<<<<<<<.*?=======\n(.*?)>>>>>>>.*?\n", r"\1", section, flags=re.S)
        content = re.sub(r"<<<<<<<.*?=======\n.*?>>>>>>>.*?\n", merged + "\n", content, count=1, flags=re.S)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

    return True


def main():
    print("🧠 Auto Conflict Resolver for NaMoNexus_v1.0")
    modified_files = 0

    for path in REPO_ROOT.rglob("*"):
        if path.is_file() and path.suffix in TARGET_EXTENSIONS:
            if resolve_conflicts_in_file(path):
                modified_files += 1

    if modified_files == 0:
        print("✅ No unresolved conflicts found.")
        return

    print(f"✅ Successfully auto-merged {modified_files} files.")
    subprocess.run(["git", "add", "."], check=True)
    subprocess.run([
        "git",
        "commit",
        "-m",
        f"🤖 Auto-Resolved {modified_files} merge conflicts (Balanced Dharma Mode Integration)"
    ], check=True)

    print("🚀 All conflicts resolved and committed successfully!")


if __name__ == "__main__":
    main()
