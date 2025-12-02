# API Reference

## Base URLs
- FastAPI gateway: `/`

## Endpoints
- `GET /` – Status check returning a simple message.
- `GET /health` – Health payload with a timestamp.
- `POST /reflect` – Body: `{ "text": "..." }` → Returns persona reflection and risk scores.
- `POST /namo/dialogue` – Alias to `/reflect` for frontend compatibility.

## Response Structure
`/reflect` and `/namo/dialogue` respond with:
- `result.reflection` – Tone, moral index, coherence, reflection string.
- `result.memory` – Memory recall summary and entries.
- `result.coherence` – Emotional coherence score.
- `risk` – Risk score and category derived from safety checks.
