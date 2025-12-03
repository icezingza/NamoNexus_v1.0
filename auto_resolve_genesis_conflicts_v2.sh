#!/bin/bash
# ===============================================================
# 🧠 NaMoNexus Git Supervisor v2.0 (Self-Healing + Auto Push)
# ===============================================================
# แก้ merge conflicts อัตโนมัติ, จัดการไฟล์ runtime ที่ conflict,
# บันทึก log การดำเนินการ และ push การแก้ไขกลับไปยัง branch ปัจจุบัน
# ===============================================================

set -euo pipefail

LOG_DIR="logs"
LOG_FILE="$LOG_DIR/auto_resolve_$(date +%Y%m%d_%H%M%S).log"

mkdir -p $LOG_DIR
echo "🧠 [$(date)] Starting NaMoNexus Git Supervisor v2.0..." | tee -a $LOG_FILE
echo "--------------------------------------------------------" | tee -a $LOG_FILE

# STEP 1: ตรวจสอบ remote origin
if ! git remote | grep -q origin; then
  echo "❌ No remote origin found. Please add your GitHub repo first!" | tee -a $LOG_FILE
  echo "   ➜ git remote add origin <your_repo_url>" | tee -a $LOG_FILE
  exit 1
fi

# STEP 2: ตรวจสอบ branch ปัจจุบัน
CURRENT_BRANCH=$(git rev-parse --abbrev-ref HEAD)
echo "📂 Current branch: $CURRENT_BRANCH" | tee -a $LOG_FILE

# STEP 3: ดึงข้อมูลล่าสุดจาก main
echo "🔄 Fetching latest main..." | tee -a $LOG_FILE
git fetch origin main >> $LOG_FILE 2>&1

# STEP 4: ตรวจจับ conflicts
CONFLICTS=$(git diff --name-only --diff-filter=U)
COMMIT_MADE=false
if [[ -z "$CONFLICTS" ]]; then
  echo "✅ No conflicts detected. Repository is clean." | tee -a $LOG_FILE
else
  echo "⚠️ Detected conflicts in:" | tee -a $LOG_FILE
  echo "$CONFLICTS" | tee -a $LOG_FILE

  # STEP 5: จัดการ memory_log.json
  if echo "$CONFLICTS" | grep -q "data/memory_log.json"; then
    echo "🧹 Cleaning runtime log conflict (memory_log.json)..." | tee -a $LOG_FILE
    if ! grep -q "^data/memory_log.json$" .gitignore 2>/dev/null; then
      echo "data/memory_log.json" >> .gitignore
    fi
    git rm --cached data/memory_log.json 2>/dev/null || true
  fi

  # STEP 6: จัดการ genesis_start.sh
  if echo "$CONFLICTS" | grep -q "genesis_start.sh"; then
    echo "🧩 Restoring genesis_start.sh from main..." | tee -a $LOG_FILE
    git checkout origin/main -- genesis_start.sh
  fi

  # STEP 7: Commit การแก้ไขทั้งหมด
  git add .gitignore genesis_start.sh 2>/dev/null || true
  if ! git diff --cached --quiet; then
    git commit -m "🤖 Auto-resolved merge conflicts (runtime log + genesis_start.sh)" >> $LOG_FILE 2>&1
    COMMIT_MADE=true
    echo "✅ Commit completed." | tee -a $LOG_FILE
  else
    echo "ℹ️ No staged changes to commit." | tee -a $LOG_FILE
  fi
fi

# STEP 8: Push การแก้ไขกลับขึ้น branch ปัจจุบัน
if $COMMIT_MADE; then
  echo "🚀 Pushing resolved branch ($CURRENT_BRANCH) to origin..." | tee -a $LOG_FILE
  if git push origin "$CURRENT_BRANCH" >> $LOG_FILE 2>&1; then
    echo "✅ Push successful. Conflicts resolved and synced to GitHub." | tee -a $LOG_FILE
  else
    echo "⚠️ Push failed — check network or access token permissions." | tee -a $LOG_FILE
  fi
else
  echo "ℹ️ No commit created; skipping push." | tee -a $LOG_FILE
fi

# STEP 9: สรุปผลลัพธ์
echo "--------------------------------------------------------" | tee -a $LOG_FILE
echo "📜 Log saved to: $LOG_FILE"
echo "🧘 NaMoNexus Git Supervisor v2.0 completed."
echo "--------------------------------------------------------" | tee -a $LOG_FILE
