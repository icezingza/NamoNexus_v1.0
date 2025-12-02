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
