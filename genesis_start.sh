#!/bin/bash
echo "🚀 Initiating NaMoNexus Genesis Execution Protocol..."

# Step 1. Environment Validation
echo "🔍 Validating Python environment..."
if ! python3 -c 'import sys; assert sys.version_info >= (3, 12)' 2>/dev/null; then
  echo "❌ Python 3.12+ is required. Please install a compatible version."
  exit 1
fi
python3 --version

# Step 2. Dependency installation
echo "📦 Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

# Step 3. Preflight check
echo "🧠 Running system integrity tests..."
if python3 -c "import pytest" &> /dev/null; then
    pytest -q --disable-warnings || { echo "❌ Tests failed. Aborting."; exit 1; }
else
    echo "⚠️ Test dependencies not found. Skipping preflight tests. (Install requirements-dev.txt to enable)"
fi

# Step 4. Launch services
echo "🌐 Starting API Gateway on port 8080..."
mkdir -p logs
nohup python3 -m namo_nexus.api.http_server > logs/api_gateway.log 2>&1 &

echo "🖥️  Starting Dharma Dashboard on port 8050..."
nohup python3 -m namo_nexus.api.dashboard > logs/dashboard.log 2>&1 &

# Step 5. Health verification
echo "🩺 Checking system health..."
sleep 5
curl -s http://127.0.0.1:8080/health || echo "⚠️ API health check failed"
curl -s http://127.0.0.1:8050/health || echo "⚠️ Dashboard health check failed"

echo "✅ NaMoNexus v1.0 is now live under JULES EXECUTION PROTOCOL."
