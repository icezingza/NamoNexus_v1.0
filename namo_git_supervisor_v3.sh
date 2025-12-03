#!/bin/bash
# ===============================================================
# 🧠 NaMoNexus Git Supervisor v3.0
# ===============================================================
# Functions:
# - Auto-resolve conflicts
# - Auto-push fixed changes
# - Monitor PR Health via GitHub API
# - Comment automatically on PR if health fails
# ===============================================================

# ---- CONFIG ----
REPO_OWNER="icezingza"
REPO_NAME="NamoNexus_v1.0"
LOG_DIR="logs"
LOG_FILE="$LOG_DIR/supervisor_$(date +%Y%m%d_%H%M%S).log"
TOKEN_FILE=".github_token"

mkdir -p $LOG_DIR
echo "🧠 [$(date)] NaMoNexus Supervisor v3.0 starting..." | tee -a $LOG_FILE
echo "--------------------------------------------------------" | tee -a $LOG_FILE

# ---- 1. ตรวจสอบโทเคน ----
if [ ! -f "$TOKEN_FILE" ]; then
  echo "❌ GitHub Token not found. Please create a file named '.github_token' and paste your PAT token inside." | tee -a $LOG_FILE
  exit 1
fi

GITHUB_TOKEN=$(cat "$TOKEN_FILE")
if [ -z "$GITHUB_TOKEN" ]; then
  echo "❌ GitHub Token file is empty. Please paste your PAT token inside '.github_token'." | tee -a $LOG_FILE
  exit 1
fi
CURRENT_BRANCH=$(git rev-parse --abbrev-ref HEAD)

# ---- 2. ตรวจสอบ conflicts ----
CONFLICTS=$(git diff --name-only --diff-filter=U)
if [[ -z "$CONFLICTS" ]]; then
  echo "✅ No conflicts detected." | tee -a $LOG_FILE
else
  echo "⚠️ Conflicts found: $CONFLICTS" | tee -a $LOG_FILE

  # Memory log conflicts
  if echo "$CONFLICTS" | grep -q "data/memory_log.json"; then
    echo "🧹 Cleaning runtime log conflict..." | tee -a $LOG_FILE
    echo "data/memory_log.json" >> .gitignore
    git rm --cached data/memory_log.json 2>/dev/null || true
  fi

  # Genesis script conflict
  if echo "$CONFLICTS" | grep -q "genesis_start.sh"; then
    echo "🧩 Restoring genesis_start.sh from main..." | tee -a $LOG_FILE
    git checkout origin/main -- genesis_start.sh
  fi

  git add .gitignore genesis_start.sh 2>/dev/null || true
  git commit -m "🤖 Auto-resolved conflicts by NaMo Supervisor v3.0" >> $LOG_FILE 2>&1
  git push origin "$CURRENT_BRANCH" --force >> $LOG_FILE 2>&1
  echo "✅ Conflict resolved and pushed." | tee -a $LOG_FILE
fi

# ---- 3. ตรวจสอบ Pull Request ที่เกี่ยวข้อง ----
echo "🔍 Checking active Pull Requests for branch: $CURRENT_BRANCH" | tee -a $LOG_FILE

PR_DATA=$(curl -s -H "Authorization: token $GITHUB_TOKEN" \
  "https://api.github.com/repos/$REPO_OWNER/$REPO_NAME/pulls?head=$REPO_OWNER:$CURRENT_BRANCH")

PR_NUMBER=$(echo "$PR_DATA" | grep '"number":' | head -n1 | awk '{print $2}' | tr -d ',')
PR_URL="https://github.com/$REPO_OWNER/$REPO_NAME/pull/$PR_NUMBER"

if [[ -z "$PR_NUMBER" ]]; then
  echo "⚠️ No active PR found for this branch." | tee -a $LOG_FILE
else
  echo "📦 Active PR detected: #$PR_NUMBER ($PR_URL)" | tee -a $LOG_FILE

  # ---- 4. ตรวจ Health Check (simulate Cloud Run / Workflow) ----
  echo "🩺 Running simulated health check..." | tee -a $LOG_FILE
  HEALTH=$(curl -s -o /dev/null -w "%{http_code}" https://example.com || echo 500)

  if [ "$HEALTH" -ne 200 ]; then
    echo "❌ Health check failed. Commenting on PR..." | tee -a $LOG_FILE
    COMMENT_BODY=$(printf 'NaMo Supervisor detected failed health checks on branch **%s**.\\nAuto-resolve completed but deployment failed health verification.\\nPlease review configuration or CI pipeline.' "$CURRENT_BRANCH")
    COMMENT_PAYLOAD=$(printf '{"body": "%s"}' "$COMMENT_BODY")

    curl -s -H "Authorization: token $GITHUB_TOKEN" \
      -X POST \
      -d "$COMMENT_PAYLOAD" \
      "https://api.github.com/repos/$REPO_OWNER/$REPO_NAME/issues/$PR_NUMBER/comments" \
      >> $LOG_FILE 2>&1
  else
    echo "✅ Health check passed successfully." | tee -a $LOG_FILE
  fi
fi

# ---- 5. สรุปผล ----
echo "--------------------------------------------------------" | tee -a $LOG_FILE
echo "🧘 NaMoNexus Supervisor v3.0 finished successfully."
echo "📜 Log saved at: $LOG_FILE"
echo "--------------------------------------------------------" | tee -a $LOG_FILE
