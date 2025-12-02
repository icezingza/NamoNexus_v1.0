"""
Self-Healing Supervisor for NaMoNexus.
Monitors the API Gateway and Dashboard, and attempts to restart them if they fail.
"""
import time
import subprocess
import sys
import os
import logging
import httpx
from app.core.supervisor_chain_v7 import SupervisorChainV7

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

API_URL = "http://127.0.0.1:8080/health"
DASHBOARD_URL = "http://127.0.0.1:8050/"

last_restart_time = {
    "API Gateway": 0,
    "Dashboard": 0
}
RESTART_COOLDOWN = 60  # seconds

def check_service(name, url):
    try:
        response = httpx.get(url, timeout=5)
        if response.status_code == 200:
            return True
        logger.warning(f"{name} returned status code {response.status_code}")
        return False
    except Exception as e:
        logger.error(f"{name} check failed: {e}")
        return False

def restart_api():
    if time.time() - last_restart_time["API Gateway"] < RESTART_COOLDOWN:
        logger.warning("API Gateway restart cooldown active. Skipping.")
        return
    logger.info("Restarting API Gateway...")
    cmd = "nohup uvicorn app.api.gateway:app --host 0.0.0.0 --port 8080 > logs_gateway.txt 2>&1 &"
    subprocess.Popen(cmd, shell=True)
    last_restart_time["API Gateway"] = time.time()

def restart_dashboard():
    if time.time() - last_restart_time["Dashboard"] < RESTART_COOLDOWN:
        logger.warning("Dashboard restart cooldown active. Skipping.")
        return
    logger.info("Restarting Dashboard...")
    cmd = "nohup env PYTHONPATH=. python app/api/dashboard.py > logs_dashboard.txt 2>&1 &"
    subprocess.Popen(cmd, shell=True)
    last_restart_time["Dashboard"] = time.time()

def main():
    logger.info("Supervisor starting up...")
    chain = SupervisorChainV7()

    while True:
        # Check API
        if not check_service("API Gateway", API_URL):
            restart_api()

        # Check Dashboard
        if not check_service("Dashboard", DASHBOARD_URL):
            restart_dashboard()

        # Run chain logic (just for simulation/logging as per "Ascendant" theme)
        chain.step(1.0, "health_check")

        time.sleep(15)

if __name__ == "__main__":
    main()
