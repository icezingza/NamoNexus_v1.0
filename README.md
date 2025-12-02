# NaMoNexus v1.0

NaMoNexus v1.0 is a dhammic, emotion-aware AI system that pairs an adaptive supervisor chain with the NaMo persona pipeline. It blends emotional analysis, dhammic reflection, and memory persistence while applying a safety layer and risk evaluation. The Dharma Console frontend lets you interact with NaMo visually and conversationally.

## Quick Start
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
- `GET /health` – Reports system health information.
- `POST /reflect` – Accepts `{ "text": "..." }` and returns NaMo's reflection, tone, moral index, coherence, and safety metadata.

## Safety
The `/reflect` endpoint applies a safety guard and risk evaluator. High-risk inputs are gated and may return a safe refusal message with the associated risk details instead of processing the request.

## Testing
Run the test suite with pytest:
```bash
pytest
```
