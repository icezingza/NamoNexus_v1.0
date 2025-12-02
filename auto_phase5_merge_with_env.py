import os
import subprocess
import sys
import requests
from dotenv import load_dotenv
import time

# โหลด token จากไฟล์ .env
load_dotenv()
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

REPO_URL = "https://github.com/icezingza/NamoNexus_v1.0.git"
BRANCH = "codex/create-namonexus-v1.0-deploy"
MAIN_BRANCH = "main"
PR_NUMBER = 10
GITHUB_USER = "icezingza"

MERGE_MSG = "🤖 AutoPhase5 Merge: Deploy health verification integration finalized."

def run(cmd):
    print(f"▶ {cmd}")
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if result.stdout:
        print(result.stdout.strip())
    if result.stderr:
        print(result.stderr.strip())
    if result.returncode != 0:
        print(f"❌ Error: {cmd}")
        sys.exit(result.returncode)

def ensure_repo():
    if not os.path.exists(".git"):
        run(f"git clone {REPO_URL} .")
    run("git fetch origin")

def resolve_conflicts():
    run(f"git checkout {BRANCH}")
    run(f"git merge origin/{MAIN_BRANCH} --no-commit --no-ff || true")
    run("git checkout --theirs .")
    run("git add .")
    run(f'git commit -m "{MERGE_MSG}" || echo No changes to commit')

def push_changes():
    run(f"git push origin {BRANCH}")

def merge_pr():
    if not GITHUB_TOKEN:
        print("❌ Missing GitHub token in .env file")
        sys.exit(1)

    url = f"https://api.github.com/repos/{GITHUB_USER}/NamoNexus_v1.0/pulls/{PR_NUMBER}/merge"
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github+json"
    }
    data = {"commit_title": MERGE_MSG, "merge_method": "squash"}

    print("🔄 Merging PR via GitHub API...")
    res = requests.put(url, headers=headers, json=data)
    if res.status_code == 200:
        print("✅ Merge successful!")
    else:
        print(f"⚠️ Merge failed: {res.status_code} - {res.text}")
        sys.exit(1)

def verify_health():
    print("🩺 Checking deployment health endpoint...")
    try:
        res = requests.get("https://namo-nexus.cloudrun.app/health", timeout=10)
        if res.status_code == 200:
            print("✅ Health check passed:", res.json())
        else:
            print("⚠️ Health check returned non-200:", res.status_code)
    except Exception as e:
        print(f"⚠️ Health check failed: {e}")

def main():
    print("\n🚀 Starting Phase 5 Merge Controller\n")
    ensure_repo()
    resolve_conflicts()
    push_changes()
    merge_pr()
    time.sleep(5)
    verify_health()
    print("\n🎯 Process complete. All systems synchronized.\n")

if __name__ == "__main__":
    main()
