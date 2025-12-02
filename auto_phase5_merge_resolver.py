#!/usr/bin/env python3
import argparse
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
        print("   Configure it, for example:")
        print(f"   git remote add {remote_name} <YOUR_REMOTE_URL>")
        sys.exit(1)


def ensure_branch_exists(branch: str) -> None:
    result = subprocess.run(["git", "show-ref", "--verify", f"refs/heads/{branch}"], capture_output=True, text=True)
    if result.returncode != 0:
        print(f"❌ Branch '{branch}' does not exist locally. Create it or fetch it before retrying.")
        sys.exit(1)


def merge_main_into_codex_branch(remote: str, target_branch: str, main_ref: str) -> None:
    merge_message = "Force resolve all conflicts: keep Codex build as truth"

    ensure_remote(remote)
    ensure_branch_exists(target_branch)

    print(f"🔄 Fetching latest from {remote}...")
    run_command(["git", "fetch", remote])

    print(f"📂 Checking out {target_branch}...")
    run_command(["git", "checkout", target_branch])

    print(f"🔀 Merging {main_ref} with ours strategy (Codex branch wins)...")
    run_command(["git", "merge", main_ref, "--strategy-option=ours", "-m", merge_message])

    print("✅ Merge completed. Current status:")
    run_command(["git", "status", "-sb"], check=False)


def parse_args(argv: List[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Merge origin/main into the Codex deploy branch using ours strategy.")
    parser.add_argument("--remote", default="origin", help="Remote name that hosts main (default: origin)")
    parser.add_argument("--target-branch", default="codex/create-namonexus-v1.0-deploy", help="Target Codex branch to receive the merge")
    parser.add_argument("--main-ref", default="origin/main", help="Reference for main to merge (default: origin/main)")
    return parser.parse_args(argv)


def main(argv: List[str] | None = None) -> None:
    args = parse_args(argv or sys.argv[1:])
    try:
        merge_main_into_codex_branch(args.remote, args.target_branch, args.main_ref)
    except SystemExit:
        raise
    except Exception as exc:
        print(f"❌ Unexpected error: {exc}")
        sys.exit(1)


if __name__ == "__main__":
    main()
