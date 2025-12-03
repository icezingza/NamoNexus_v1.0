#!/usr/bin/env python3
"""
NaMoNexus Supervisor v3.0 (Python edition)
- Auto-resolve conflicts
- Auto-push fixed changes
- Monitor PR Health via GitHub API
- Comment automatically on PR if health fails

This script replaces shell-based curl commands with Python standard
library HTTP handling while preserving existing behaviour.
"""
from __future__ import annotations

import json
import subprocess
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import List, Optional

REPO_OWNER = "icezingza"
REPO_NAME = "NamoNexus_v1.0"
LOG_DIR = Path("logs")
LOG_FILE = LOG_DIR / f"supervisor_{time.strftime('%Y%m%d_%H%M%S')}.log"
TOKEN_FILE = Path(".github_token")


def log(message: str) -> None:
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    formatted = f"{message}"
    print(formatted)
    LOG_FILE.parent.mkdir(parents=True, exist_ok=True)
    with LOG_FILE.open("a", encoding="utf-8") as fh:
        fh.write(f"{formatted}\n")


def run_cmd(args: List[str], check: bool = True, capture_output: bool = True) -> subprocess.CompletedProcess:
    return subprocess.run(
        args,
        check=check,
        capture_output=capture_output,
        text=True,
    )


def get_current_branch() -> str:
    result = run_cmd(["git", "rev-parse", "--abbrev-ref", "HEAD"])
    return result.stdout.strip()


def read_github_token() -> Optional[str]:
    if not TOKEN_FILE.exists():
        return None
    return TOKEN_FILE.read_text(encoding="utf-8").strip()


def detect_conflicts() -> List[str]:
    result = run_cmd(["git", "diff", "--name-only", "--diff-filter=U"], capture_output=True)
    files = result.stdout.strip().splitlines()
    return [f for f in files if f]


def append_gitignore_entry(entry: str) -> None:
    gitignore = Path(".gitignore")
    if gitignore.exists():
        existing = gitignore.read_text(encoding="utf-8").splitlines()
    else:
        existing = []
    if entry not in existing:
        existing.append(entry)
        gitignore.write_text("\n".join(existing) + "\n", encoding="utf-8")


def checkout_main_version(path: str) -> None:
    run_cmd(["git", "checkout", "origin/main", "--", path], check=False)


def commit_and_push(branch: str) -> None:
    run_cmd(["git", "add", ".gitignore", "genesis_start.sh"], check=False)
    run_cmd(["git", "commit", "-m", "🤖 Auto-resolved conflicts by NaMo Supervisor v3.0"], check=False)
    run_cmd(["git", "push", "origin", branch, "--force"], check=False)


def fetch_pr_data(token: str, branch: str) -> Optional[dict]:
    params = urllib.parse.urlencode({"head": f"{REPO_OWNER}:{branch}"})
    url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/pulls?{params}"
    req = urllib.request.Request(url, headers={"Authorization": f"token {token}"})
    try:
        with urllib.request.urlopen(req) as resp:
            body = resp.read().decode("utf-8")
            data = json.loads(body)
    except (urllib.error.URLError, json.JSONDecodeError) as exc:
        log(f"❌ Failed to fetch PR data: {exc}")
        return None
    if not data:
        return None
    return data[0] if isinstance(data, list) else None


def post_pr_comment(token: str, pr_number: int, body: str) -> None:
    url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/issues/{pr_number}/comments"
    payload = json.dumps({"body": body}).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=payload,
        method="POST",
        headers={
            "Authorization": f"token {token}",
            "Content-Type": "application/json",
        },
    )
    try:
        with urllib.request.urlopen(req):
            log("✅ Posted comment to PR.")
    except urllib.error.URLError as exc:
        log(f"❌ Failed to post PR comment: {exc}")


def health_check(url: str = "https://example.com") -> int:
    try:
        with urllib.request.urlopen(url) as resp:
            return resp.getcode()
    except urllib.error.URLError:
        return 500


def handle_conflicts(conflicts: List[str], branch: str) -> None:
    if not conflicts:
        log("✅ No conflicts detected.")
        return

    log(f"⚠️ Conflicts found: {' '.join(conflicts)}")

    if any(path == "data/memory_log.json" for path in conflicts):
        log("🧹 Cleaning runtime log conflict...")
        append_gitignore_entry("data/memory_log.json")
        run_cmd(["git", "rm", "--cached", "data/memory_log.json"], check=False)

    if any(path == "genesis_start.sh" for path in conflicts):
        log("🧩 Restoring genesis_start.sh from main...")
        checkout_main_version("genesis_start.sh")

    commit_and_push(branch)
    log("✅ Conflict resolved and pushed.")


def main() -> int:
    log("🧠 NaMoNexus Supervisor v3.0 (Python) starting...")
    log("--------------------------------------------------------")

    token = read_github_token()
    if not token:
        log("❌ GitHub Token not found. Please create a file named '.github_token' and paste your PAT token inside.")
        return 1

    branch = get_current_branch()
    conflicts = detect_conflicts()
    handle_conflicts(conflicts, branch)

    log(f"🔍 Checking active Pull Requests for branch: {branch}")
    pr_data = fetch_pr_data(token, branch)

    if not pr_data or "number" not in pr_data:
        log("⚠️ No active PR found for this branch.")
    else:
        pr_number = pr_data["number"]
        pr_url = f"https://github.com/{REPO_OWNER}/{REPO_NAME}/pull/{pr_number}"
        log(f"📦 Active PR detected: #{pr_number} ({pr_url})")

        log("🩺 Running simulated health check...")
        status = health_check()
        if status != 200:
            log("❌ Health check failed. Commenting on PR...")
            comment_body = (
                f"NaMo Supervisor detected failed health checks on branch **{branch}**.\n"
                "Auto-resolve completed but deployment failed health verification.\n"
                "Please review configuration or CI pipeline."
            )
            post_pr_comment(token, pr_number, comment_body)
        else:
            log("✅ Health check passed successfully.")

    log("--------------------------------------------------------")
    log("🧘 NaMoNexus Supervisor v3.0 finished successfully.")
    log(f"📜 Log saved at: {LOG_FILE}")
    log("--------------------------------------------------------")
    return 0


if __name__ == "__main__":
    sys.exit(main())
