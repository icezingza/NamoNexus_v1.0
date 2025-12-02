"""Self-Healing Supervisor for NaMoNexus.
Monitors the API Gateway and Dashboard, and attempts to restart them if they fail.
Supervisor entry point for validating and running the stability layer.
"""

import time
import subprocess
import sys
import os
import logging
import httpx
import argparse
from typing import NoReturn

from app.core.supervisor_chain_v7 import SupervisorChainV7

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)]
)

logger = logging.getLogger("Supervisor")

def check_health(url: str) -> bool:
    try:
        response = httpx.get(url, timeout=5)
        return response.status_code == 200
    except Exception as e:
        logger.warning(f"Health check failed for {url}: {e}")
        return False

def restart_service(service_name: str) -> None:
    logger.info(f"Restarting {service_name}...")
    subprocess.run(["systemctl", "restart", service_name], check=False)
    time.sleep(3)

def monitor_loop() -> NoReturn:
    urls = {
        "gateway": "http://localhost:8000/health",
        "dashboard": "http://localhost:3000"
    }

    supervisor = SupervisorChainV7()

    while True:
        for name, url in urls.items():
            if not check_health(url):
                logger.warning(f"{name} service unhealthy. Attempting restart...")
                restart_service(name)

        supervisor.step(signal=1.0, symbols=["stability"])
        time.sleep(10)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run NaMoNexus Self-Healing Supervisor")
    args = parser.parse_args()
    monitor_loop()
