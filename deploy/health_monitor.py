import sys
import time

import requests

URL = "https://namonexus-api-xxxxxxxx.a.run.app/health"
MAX_RETRIES = 5
SLEEP_SECONDS = 10
TIMEOUT_SECONDS = 5


def main() -> int:
    for attempt in range(MAX_RETRIES):
        try:
            response = requests.get(URL, timeout=TIMEOUT_SECONDS)
            if response.status_code == 200:
                print(f"✅ Health check passed: {response.json()}")
                return 0
            print(f"⏳ Retry {attempt + 1}/{MAX_RETRIES} — status {response.status_code}")
        except Exception as exc:  # pragma: no cover - network exceptions during monitoring
            print(f"⏳ Retry {attempt + 1}/{MAX_RETRIES} — {exc}")
        time.sleep(SLEEP_SECONDS)

    print("❌ Health check failed after 5 retries.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
