#!/usr/bin/env python3
"""
auto_resolve_phase5.py
-----------------------------------------------------
Phase 5 resolver: automatically merges both branch
changes, cleans up conflict markers, and commits
the merged result safely.
-----------------------------------------------------
"""

import os
import subprocess
from pathlib import Path

TARGET_DIRS = [
    ".github/workflows",
    "app/api",
    "app/core",
    "app/memory",
    "app/personality",
    "frontend",
    "tests"
]

def resolve_conflicts():
    print("🔍 Scanning for conflict markers...")
    merged = 0

    for dir_ in TARGET_DIRS:
        for file in Path(dir_).rglob("*.*"):
            text = file.read_text(encoding="utf-8", errors="ignore")
            if "<<<<<<<" in text:
                # ✅ Choose "accept both changes"
                cleaned = []
                skip = False
                for line in text.splitlines():
                    if line.strip().startswith("<<<<<<<") or line.strip().startswith("======="):
                        continue
                    elif line.strip().startswith(">>>>>>>"):
                        skip = False
                        continue
                    cleaned.append(line)
                file.write_text("\n".join(cleaned), encoding="utf-8")
                merged += 1
                print(f"✅ Auto-merged: {file}")

    print(f"\n🎯 {merged} files auto-resolved and cleaned.")
    return merged

def commit_changes():
    print("💾 Committing merge...")
    subprocess.run(["git", "add", "."], check=True)
    subprocess.run(["git", "commit", "-m", "Auto-resolved Phase 5 conflicts [Balanced Merge]"], check=True)
    subprocess.run(["git", "push", "origin", "main"], check=True)
    print("🚀 Push complete!")

if __name__ == "__main__":
    merged = resolve_conflicts()
    if merged > 0:
        commit_changes()
    else:
        print("✅ No conflicts found — repository is clean.")
