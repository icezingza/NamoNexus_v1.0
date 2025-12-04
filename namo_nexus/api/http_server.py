"""FastAPI gateway exposing NaMo persona reflection endpoints."""
from __future__ import annotations

import time
from typing import Any

from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel

from namo_nexus.core.config import get_settings
from namo_nexus.core.logging_middleware import LoggingMiddleware, setup_logging
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from namo_nexus.cog.namo_persona_core import NamoPersonaCore
from namo_nexus.safety.intention_manager import check_safe
from namo_nexus.safety.threat_analyzer import RiskEvaluator


class ReflectionRequest(BaseModel):
    text: str


def create_app() -> FastAPI:
    settings = get_settings()
    if settings.FEATURE_FLAGS.get("ENABLE_LOGGING", True):
        setup_logging()
    app = FastAPI(title="NaMo Nexus", version="1.0")
    persona = NamoPersonaCore()
    risk = RiskEvaluator()
    logging_middleware = LoggingMiddleware(app)
    safety_enabled = settings.FEATURE_FLAGS.get("ENABLE_SAFETY", True)

    if settings.FEATURE_FLAGS.get("ENABLE_LOGGING", True):
        @app.middleware("http")
        async def log_requests(request: Request, call_next):
            return await logging_middleware.dispatch(request, call_next)

    @app.get("/")
    def root() -> dict[str, str]:
        return {"status": "ok", "message": "NaMo Dharma Dialogue online"}

    @app.get("/health")
    def health() -> dict[str, Any]:
        now = time.time()
        return {"status": "healthy", "timestamp": now, "environment": settings.APP_ENV}

    @app.post("/reflect")
    def reflect(request: ReflectionRequest) -> dict[str, Any]:
        if not request.text or not str(request.text).strip():
            raise HTTPException(status_code=400, detail={"message": "Text is required"})

        text = str(request.text).strip()

        safety = {"flagged": []}
        risk_score = {"score": 0.0, "category": "low"}
        if safety_enabled:
            safety = check_safe(text)
            risk_score = risk.score(safety["flagged"])

        if safety_enabled and risk_score["category"] == "high":
            return {
                "message": "The request was refused for safety reasons.",
                "risk_score": risk_score["score"],
                "risk_level": risk_score["category"],
                "flagged_terms": safety["flagged"],
            }

        result = persona.process(text)
        return {
            **result,
            "risk_score": risk_score["score"],
            "risk_level": risk_score["category"],
            "flagged_terms": safety.get("flagged", []),
        }

    @app.post("/namo/dialogue")
    def dialogue(request: ReflectionRequest) -> dict[str, Any]:
        return reflect(request)

    return app


app = create_app()


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8080)
