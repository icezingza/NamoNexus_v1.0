"""Helper to deploy NaMoNexus to Cloud Run via gcloud."""
from __future__ import annotations

import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def deploy(project_id: str, region: str, service_name: str = "namo-nexus") -> None:
    image = f"gcr.io/{project_id}/{service_name}"
    subprocess.run(["gcloud", "builds", "submit", "--tag", image, str(ROOT)], check=True)
    subprocess.run(
        [
            "gcloud",
            "run",
            "deploy",
            service_name,
            "--image",
            image,
            "--platform",
            "managed",
            "--region",
            region,
            "--allow-unauthenticated",
        ],
        check=True,
    )


if __name__ == "__main__":
    print("Invoke deploy(project_id, region) to deploy NaMoNexus.")
