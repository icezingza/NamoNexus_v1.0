# Deployment Guide

## Local Development
1. Create a virtual environment and install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Start the API server:
   ```bash
   uvicorn main:app --reload
   ```
3. Open `frontend/index.html` in a browser or serve it via a simple HTTP server.

## Cloud Run (via `deploy/cloudrun_auto_deploy.py`)
1. Ensure the Google Cloud CLI is installed and authenticated.
2. Run the deployment helper with your project and region:
   ```bash
   python deploy/cloudrun_auto_deploy.py
   ```
3. Alternatively, call `deploy(project_id, region)` from the module to automate build and deploy.

## Packaging
Use the builder to create a distributable zip:
```bash
python deploy/build_namonexus_zip.py
```
