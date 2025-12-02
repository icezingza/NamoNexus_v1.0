# NaMoNexus v1.0

NaMoNexus is a lightweight AI system blending compassionate reasoning, emotional awareness, and a dharma-inspired dialogue interface.

## Structure
- `app/`: Core application logic, FastAPI gateway, supervisor chain, emotion, memory, personality, and safety modules.
- `engine/`: Minimal runtime components for dharma reasoning, safety, and emotional scoring.
- `frontend/`: Dharma Console web UI with orb visualization and chat panel.
- `deploy/`: Packaging and Cloud Run helper scripts.
- `docs/`: Architecture and API documentation.

## Quickstart
```bash
pip install -r requirements.txt
uvicorn main:app --reload
```
Then open `frontend/index.html` in a browser to chat with NaMo.
