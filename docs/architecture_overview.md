# NaMoNexus v1.0 Architecture Overview

NaMoNexus is organized into three primary layers:

- **app/**: Core application logic including the supervisor chain, emotional processing, memory management, safety, and API gateway.
- **engine/**: Lightweight dharma-inspired runtime utilities and evaluators that can be used independently.
- **frontend/**: The Dharma Console web interface for dialogue and status.

Key flows:
- The FastAPI gateway in `app/api/gateway.py` receives user text, routes it through safety checks, and then forwards to `NamoPersonaCore` for processing.
- `NamoPersonaCore` leverages the emotion analyzer, reflection engine, and memory store to produce a structured response.
- The supervisor chain in `app/core/supervisor_chain_v7.py` coordinates adaptive learning through meta-learning and predictive optimization utilities.

Deployment aids live in `deploy/` and documentation in `docs/`. The manifest `Namo_FormGenesis_v1.0_RELEASE_MANIFEST.md` captures project identity.
