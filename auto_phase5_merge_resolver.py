#!/usr/bin/env python3
import subprocess
import sys
from typing import List


def run_command(command: List[str], check: bool = True) -> subprocess.CompletedProcess:
    result = subprocess.run(command, text=True, capture_output=True)
    if result.stdout:
        print(result.stdout.strip())
    if result.stderr:
        print(result.stderr.strip(), file=sys.stderr)
    if check and result.returncode != 0:
        sys.exit(result.returncode)
    return result


def ensure_remote(remote_name: str) -> None:
    result = subprocess.run(["git", "remote", "show", remote_name], capture_output=True, text=True)
    if result.returncode != 0:
        print(f"❌ Remote '{remote_name}' is not configured. Add it before running the merge.")
        sys.exit(1)


def merge_main_into_codex_branch() -> None:
    target_branch = "codex/create-namonexus-v1.0-deploy"
    main_ref = "origin/main"
    merge_message = "Force resolve all conflicts: keep Codex build as truth"

    ensure_remote("origin")

    print("🔄 Fetching latest from origin...")
    run_command(["git", "fetch", "origin"])

    print(f"📂 Checking out {target_branch}...")
    run_command(["git", "checkout", target_branch])

    print(f"🔀 Merging {main_ref} with ours strategy (Codex branch wins)...")
    run_command(["git", "merge", main_ref, "--strategy-option=ours", "-m", merge_message])

    print("✅ Merge completed. Current status:")
    run_command(["git", "status", "-sb"], check=False)


def main() -> None:
    try:
        merge_main_into_codex_branch()
    except SystemExit:
        raise
    except Exception as exc:
        print(f"❌ Unexpected error: {exc}")
        sys.exit(1)


if __name__ == "__main__":
    main()
