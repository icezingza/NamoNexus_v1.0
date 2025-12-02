# Deployment Guide

## 1. Local Development
1. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the API locally:
   ```bash
   uvicorn main:app --reload
   ```
4. Open the Dharma Console frontend in your browser:
   - Open `frontend/index.html` directly, or
   - Serve the `frontend/` folder via a simple HTTP server for same-origin requests.

## 2. Docker
1. Build the image using the provided `Dockerfile`:
   ```bash
   docker build -t namonexus:latest .
   ```
2. Run the container and expose the API on port 8000:
   ```bash
   docker run -p 8000:8000 namonexus:latest
   ```
   Access the API at `http://localhost:8000` and load `frontend/index.html` pointing to the same origin.

## 3. Cloud Run Helper
Use `deploy/cloudrun_auto_deploy.py` to streamline Cloud Run deployment.

- Expected arguments: `project_id`, `region`, and `service_name`.
- The script packages the repo, submits a build via `gcloud builds submit`, and deploys the resulting image with `gcloud run deploy`.
- Ensure the Google Cloud CLI is installed, authenticated, and the target project is set before running.
- Example invocation:
  ```bash
  python deploy/cloudrun_auto_deploy.py --project-id <PROJECT_ID> --region <REGION> --service-name <SERVICE_NAME>
  ```
