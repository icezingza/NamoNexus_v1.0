"""
NaMoNexus Self-Healing Supervisor (Ascendant Stability Layer)
Monitors API Gateway and Dashboard processes, auto-restarts if unresponsive.
"""

import subprocess
import time
import requests
import psutil
import os

API_PORT = 8080
DASHBOARD_PORT = 8050
CHECK_INTERVAL = 15  # seconds

def is_healthy(url):
    try:
        res = requests.get(url, timeout=3)
        return res.status_code == 200
    except Exception:
        return False

def restart_process(name, command):
    print(f"🔄 Restarting {name}...")
    subprocess.Popen(command, shell=True)

def monitor():
    print("🩺 Starting Self-Healing Supervisor...")
    while True:
        api_ok = is_healthy(f"http://127.0.0.1:{API_PORT}/health")
        dash_ok = is_healthy(f"http://127.0.0.1:{DASHBOARD_PORT}/health")

        if not api_ok:
            restart_process("API Gateway", "nohup python3 -m app.api.gateway &")

        if not dash_ok:
            restart_process("Dashboard", "nohup python3 -m app.api.dashboard &")

        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    monitor()
