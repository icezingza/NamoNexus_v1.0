# NaMoNexus v1.0

NaMoNexus v1.0 is a dhammic, emotion-aware AI system that pairs an adaptive supervisor chain with the NaMo persona pipeline. It blends emotional analysis, dhammic reflection, and memory persistence while applying a safety layer and risk evaluation. The Dharma Console frontend lets you interact with NaMo visually and conversationally.

## Quick Start
Python **3.11** is required for development, CI, and container builds.
1. Create and activate a virtual environment.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the API locally:
   ```bash
   uvicorn main:app --reload
   ```
4. Open `frontend/index.html` in your browser and start chatting with NaMo.

## Production Config (Balanced Dharma Mode)
Configuration is managed via `app/core/config.py` using Pydantic settings. Environment variables are prefixed with `NAMO_` and drive feature toggles for safety, memory, dhammic reflection, coherence scoring, and logging.

Key settings:
- `NAMO_LOG_LEVEL` (default: `INFO`)
- `NAMO_MEMORY_PATH` (default: `data/memory_log.json`)
- `NAMO_MAX_MEMORY_ENTRIES` (default: `200`)
- `NAMO_FEATURE_FLAGS` (JSON dict) controlling:
  - `ENABLE_SAFETY`
  - `ENABLE_MEMORY`
  - `ENABLE_DHAMMA_REFLECTION`
  - `ENABLE_COHERENCE_SCORE`
  - `ENABLE_LOGGING`

Example `.env` snippet:
```
NAMO_APP_ENV=production
NAMO_LOG_LEVEL=INFO
NAMO_MEMORY_PATH=/var/lib/namo/memory_log.json
NAMO_MAX_MEMORY_ENTRIES=500
NAMO_FEATURE_FLAGS={"ENABLE_SAFETY":true,"ENABLE_MEMORY":true,"ENABLE_DHAMMA_REFLECTION":true,"ENABLE_COHERENCE_SCORE":true,"ENABLE_LOGGING":true}
```

## API Endpoints
- `GET /` – Basic status message to confirm the service is reachable.
- `GET /health` – Backward-compatible health payload.
- `GET /healthz` – Liveness probe (lightweight).
- `GET /readyz` – Readiness probe; surfaces component flags (persona, shield, memory, vector store, embedder).
- `POST /reflect` – Accepts `{ "text": "..." }` and returns NaMo's reflection, tone, moral index, coherence, and safety metadata.

## Safety
The `/reflect` endpoint applies a safety guard and risk evaluator. High-risk inputs are gated and may return a safe refusal message with the associated risk details instead of processing the request.

## Health & Readiness Checks
Run quick probes while the API is up:
```bash
curl -s http://127.0.0.1:8000/healthz | jq
curl -s http://127.0.0.1:8000/readyz | jq
```

## Operational Checks
- Smoke/system check: `python system_health_check.py`
- Full tests: `pytest`

## Dependency Pins & Security
- Runtime pins: `chromadb==1.3.5`, `sentence-transformers==5.1.2`, `transformers==4.57.3` (aligned with the current environment for deterministic deploys).
- CI runs `pip-audit` with temporary ignores for upstream-pinned deps (Werkzeug<3.1 via Dash; urllib3<2.4 via kubernetes). Remove the ignores once upstreams relax their upper bounds.

## Cloud Run Deploy (Stateless)
Container build (local):
```bash
docker build -t namonexus:cloudrun .
docker run -p 8080:8080 -e PORT=8080 namonexus:cloudrun
```

Deploy via gcloud (example):
```bash
gcloud builds submit --tag gcr.io/PROJECT_ID/namonexus:latest .
gcloud run deploy namonexus \
  --image gcr.io/PROJECT_ID/namonexus:latest \
  --region YOUR_REGION \
  --port 8080 \
  --allow-unauthenticated \
  --cpu 1 --memory 1Gi --max-instances 3
```

Recommended env vars for Cloud Run:
- `NAMO_LOG_LEVEL=INFO`
- `NAMO_FEATURE_FLAGS={"ENABLE_SAFETY":true,"ENABLE_MEMORY":false,"ENABLE_DHAMMA_REFLECTION":true,"ENABLE_COHERENCE_SCORE":true,"ENABLE_LOGGING":true,"ENABLE_INFINITY_MEMORY":false}` (disables local persistence on ephemeral disk; point to external vector DB if needed)
- `ALLOWED_ORIGINS=https://your-frontend.example.com` (comma-separated; use "*" only for dev)
- `ANONYMIZED_TELEMETRY=false` (disable Chroma telemetry by default)
- External Chroma (optional, for stateful vector memory): `CHROMA_HOST`, `CHROMA_PORT`, `CHROMA_SSL=true|false`, `CHROMA_AUTH_TOKEN` (if your service requires auth). Set `ENABLE_INFINITY_MEMORY=true` when pointing to a persistent/remote store.

Probes (configure in Cloud Run):
- Liveness: `GET /healthz`
- Readiness: `GET /readyz`

Notes on state:
- Cloud Run provides only ephemeral filesystem. The default local Chroma path `data/chroma_db` will not persist across instances. Use an external vector store or keep `ENABLE_INFINITY_MEMORY=false` for stateless runs.
- If you mount storage (e.g., Cloud Storage FUSE) or attach an external DB, update `NAMO_FEATURE_FLAGS` and connection settings accordingly.

## Persistent Memory (External Vector Store)
- Provision a managed vector DB (Chroma Cloud, Supabase/PGVector, or other HTTP Chroma service).
- Set env vars: `CHROMA_HOST`, `CHROMA_PORT` (default 443), `CHROMA_SSL=true|false`, `CHROMA_AUTH_TOKEN` (if required).
- Enable: `NAMO_FEATURE_FLAGS` with `"ENABLE_INFINITY_MEMORY": true` and `"ENABLE_MEMORY": true`.
- Deploy to Cloud Run; `/readyz` will report `vector_store=true` when connected to the external store.
- For stateless mode, keep `"ENABLE_INFINITY_MEMORY": false` and skip external Chroma.

## Performance for Instant Empathy
- Cloud Run recommended: `--cpu 2 --memory 4Gi --min-instances 1` to avoid cold starts and reduce transformer latency.
- Keep `uvicorn` single-worker first; scale CPU before adding workers to avoid model duplication overhead, then tune `--workers`/`--limit-concurrency` if needed after measuring p95 latency.

## Testing
Run the test suite with pytest:
```bash
pytest
```
