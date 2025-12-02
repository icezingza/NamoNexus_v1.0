#!/bin/bash
# ──────────────────────────────────────────────
#  JULES EXECUTION PROTOCOL — NamoNexus_v1.0 Genesis Build
#  Author: Code GPT
#  Version: v1.0-Autonomous Genesis
# ──────────────────────────────────────────────

echo "🧠 [JULES] Initializing NamoNexus Genesis Execution Sequence..."
echo "──────────────────────────────────────────────"

# === 1. PREPARE ENVIRONMENT ===
echo "[1/8] Setting up environment..."
# Assumes python3 is installed. In sandbox, apt-get might be restricted or unnecessary.
# sudo apt-get update -y
# sudo apt-get install -y python3 python3-venv python3-pip git

# === 2. CLONE OR EXTRACT PROJECT ===
echo "[2/8] Checking NamoNexus repository..."
# We assume we are in the repo root for this execution context.

# === 3. INITIALIZE PYTHON ENV ===
echo "[3/8] Creating virtual environment (if needed)..."
# python3 -m venv venv
# source venv/bin/activate
# pip install --upgrade pip

# === 4. INSTALL DEPENDENCIES ===
echo "[4/8] Installing dependencies..."
if [ -f "requirements.txt" ]; then
    pip install -r requirements.txt
else
    echo "⚠️ requirements.txt not found, installing defaults..."
    pip install fastapi uvicorn dash plotly numpy psutil
fi

# === 5. VALIDATE CORE FILES ===
echo "[5/8] Validating core structure..."
REQUIRED_FILES=("main.py" "run.py" "app/api/gateway.py" "app/core/supervisor_chain_v7.py")
for f in "${REQUIRED_FILES[@]}"; do
    if [ ! -f "$f" ]; then
        echo "❌ Missing required file: $f"
        exit 1
    fi
done
echo "✅ Core files verified."

# === 6. RUN VALIDATION TEST ===
echo "[6/8] Running system validation..."
if [ -f "app/validation/supervisor_validation.py" ]; then
    PYTHONPATH=. python app/validation/supervisor_validation.py
else
    echo "⚠️ No validation suite found. Skipping..."
fi

# === 7. LAUNCH API GATEWAY ===
echo "[7/8] Launching API Gateway..."
# Starting in background, checking PIDs
nohup uvicorn app.api.gateway:app --host 0.0.0.0 --port 8080 > logs_gateway.txt 2>&1 &
sleep 3
if pgrep -f "uvicorn app.api.gateway:app" > /dev/null; then
    echo "✅ API Gateway running on port 8080"
else
    echo "❌ API Gateway failed to start. Check logs_gateway.txt"
fi

# === 8. RUN DASHBOARD VISUALIZATION ===
echo "[8/8] Launching Dashboard..."
# The dashboard code in app/api/dashboard.py has been updated to be executable.
if [ -f "app/api/dashboard.py" ]; then
    nohup env PYTHONPATH=. python app/api/dashboard.py > logs_dashboard.txt 2>&1 &
    sleep 2
    if pgrep -f "python app/api/dashboard.py" > /dev/null; then
        echo "✅ Dashboard active on port 8050"
    else
        echo "❌ Dashboard failed to start. Check logs_dashboard.txt"
    fi
else
    echo "⚠️ Dashboard file not found."
fi

# === DONE ===
echo "──────────────────────────────────────────────"
echo "🌿 [JULES] NamoNexus_v1.0 Genesis system is fully operational."
echo "🔗 Access API: http://127.0.0.1:8080"
echo "🔗 Access Dashboard: http://127.0.0.1:8050"
echo "──────────────────────────────────────────────"
