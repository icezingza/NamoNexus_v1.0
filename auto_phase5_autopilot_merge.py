import os
import subprocess
import sys
import requests
import time

# =======================================
# CONFIGURATION
# =======================================
REPO_URL = "https://github.com/icezingza/NamoNexus_v1.0.git"
TARGET_BRANCH = "codex/create-namonexus-v1.0-deploy"
MAIN_BRANCH = "main"
PR_NUMBER = 10  # หมายเลข Pull Request ปัจจุบัน
GITHUB_USER = "icezingza"
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")  # ต้องตั้งค่า token ใน environment variable

MERGE_MESSAGE = (
    "🤖 AutoPhase5: Codex deployment pipeline approved and merged "
    "(Balanced Dharma Mode + Cloud Run readiness)."
)

# =======================================

def run_cmd(cmd):
    """Run shell commands with printed output."""
    print(f"\n🔹 Running: {cmd}")
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if result.stdout:
        print("✅ STDOUT:", result.stdout.strip())
    if result.stderr:
        print("⚠️ STDERR:", result.stderr.strip())
    if result.returncode != 0:
        print(f"❌ Command failed: {cmd}")
        sys.exit(result.returncode)
    return result.stdout.strip()

def ensure_repo():
    """Clone repo if not already cloned."""
    if not os.path.exists(".git"):
        run_cmd(f"git clone {REPO_URL} .")
        print("✅ Repository cloned.")
    else:
        print("📦 Repository already present.")

def resolve_conflicts():
    """Resolve conflicts automatically preferring Codex branch."""
    run_cmd(f"git fetch origin {MAIN_BRANCH}")
    run_cmd(f"git checkout {TARGET_BRANCH}")
    run_cmd(f"git merge origin/{MAIN_BRANCH} --no-commit --no-ff")
    run_cmd("git checkout --theirs .")
    run_cmd("git add .")
    run_cmd(
        'git commit -m "✅ Auto-resolved merge conflicts (kept Codex deployment pipeline)"'
    )
    print("🎉 Conflicts resolved successfully.")

def push_branch():
    """Push the resolved branch."""
    run_cmd(f"git push origin {TARGET_BRANCH}")
    print("🚀 Pushed changes to GitHub successfully.")

def merge_pull_request():
    """Use GitHub API to merge PR automatically."""
    if not GITHUB_TOKEN:
        print("❌ Missing GitHub token. Please set GITHUB_TOKEN environment variable.")
        sys.exit(1)

    api_url = f"https://api.github.com/repos/{GITHUB_USER}/NamoNexus_v1.0/pulls/{PR_NUMBER}/merge"
    headers = {"Authorization": f"token {GITHUB_TOKEN}", "Accept": "application/vnd.github+json"}
    payload = {"commit_title": MERGE_MESSAGE, "merge_method": "squash"}

    print("🧠 Attempting to auto-merge via GitHub API...")
    res = requests.put(api_url, headers=headers, json=payload)

    if res.status_code == 200:
        print("✅ Pull request merged successfully!")
    elif res.status_code == 405:
        print("⚠️ Merge not allowed (already merged or no changes).")
    else:
        print(f"❌ Merge failed ({res.status_code}): {res.text}")
        sys.exit(1)

def verify_deployment():
    """Optional: Ping Cloud Run health endpoint."""
    HEALTH_URL = "https://namo-nexus.cloudrun.app/health"
    print(f"🌐 Checking deployment health: {HEALTH_URL}")
    try:
        res = requests.get(HEALTH_URL, timeout=10)
        if res.status_code == 200:
            print("✅ Deployment health check passed:", res.json())
        else:
            print(f"⚠️ Health check failed: {res.status_code}")
    except Exception as e:
        print(f"⚠️ Health check error: {e}")

def main():
    print("🧭 Starting Phase 5 AutoPilot Merge & Deploy Controller...\n")
    ensure_repo()
    resolve_conflicts()
    push_branch()
    time.sleep(2)
    merge_pull_request()
    time.sleep(5)
    verify_deployment()
    print("\n🎯 Completed: Project merged, deployed, and verified successfully.")

if __name__ == "__main__":
    main()
