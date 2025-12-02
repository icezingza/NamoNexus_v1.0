import os
import subprocess
import sys

# ========= CONFIG ==========
REPO_URL = "https://github.com/icezingza/NamoNexus_v1.0.git"
TARGET_BRANCH = "codex/create-namonexus-v1.0-deploy"
MAIN_BRANCH = "main"
COMMIT_MESSAGE = (
    "✅ Auto Phase 5 Merge Resolver: kept Codex Deployment Build "
    "(Balanced Dharma Mode + Cloud Run pipeline)"
)
# ============================

def run_cmd(cmd):
    """Run shell command and print output."""
    print(f"\n🔹 Running: {cmd}")
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if result.stdout:
        print("✅ STDOUT:", result.stdout.strip())
    if result.stderr:
        print("⚠️ STDERR:", result.stderr.strip())
    if result.returncode != 0:
        print(f"❌ Command failed with code {result.returncode}. Exiting.")
        sys.exit(result.returncode)
    return result.stdout.strip()

def ensure_repo():
    """Ensure we're in a valid git repo."""
    if not os.path.exists(".git"):
        run_cmd(f"git clone {REPO_URL} .")
        print("✅ Repository cloned.")
    else:
        print("📦 Git repository found.")

def merge_codex_with_main():
    """Perform the merge with auto conflict resolution."""
    run_cmd(f"git fetch origin {MAIN_BRANCH}")
    run_cmd(f"git checkout {TARGET_BRANCH}")
    run_cmd(f"git merge origin/{MAIN_BRANCH} --no-commit --no-ff")
    run_cmd("git checkout --theirs .")
    run_cmd("git add .")
    run_cmd(f'git commit -m "{COMMIT_MESSAGE}"')
    print("🎉 Merge conflicts resolved automatically using Codex branch preference.")

def push_changes():
    """Push merged changes back to remote."""
    run_cmd(f"git push origin {TARGET_BRANCH}")
    print("🚀 Changes pushed successfully. Ready to open Pull Request on GitHub.")

def main():
    print("🧭 Starting Phase 5 Auto Merge Resolver for NamoNexus_v1.0...")
    ensure_repo()
    merge_codex_with_main()
    push_changes()
    print("\n✅ All done! Go to your GitHub Pull Request and press 'Merge Pull Request'.")

if __name__ == "__main__":
    main()
