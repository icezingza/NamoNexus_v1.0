"""FastAPI gateway exposing NaMo persona reflection endpoints."""
from __future__ import annotations

import time
from typing import Any, Optional

from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel

from app.core.config import get_settings
from app.core.logging_middleware import LoggingMiddleware, setup_logging
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from app.personality.namo_persona_core import NamoPersonaCore
from app.safety.guard import check_safe
from app.safety.risk_evaluator import RiskEvaluator


class ReflectionRequest(BaseModel):
    text: str


class ChatRequest(BaseModel):
    user_id: Optional[str] = None
    session_id: Optional[str] = None
    message: str
    locale: Optional[str] = "th-TH"


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

    @app.post("/v1/chat")
    def chat(request: ChatRequest) -> dict[str, Any]:
        if not request.message or not str(request.message).strip():
            raise HTTPException(status_code=400, detail={"message": "Message is required"})

        text = str(request.message).strip()

        safety = {"flagged": []}
        risk_score = {"score": 0.0, "category": "low"}
        if safety_enabled:
            safety = check_safe(text)
            risk_score = risk.score(safety["flagged"])

        if safety_enabled and risk_score["category"] == "high":
            return {
                "reply": "The request was refused for safety reasons.",
                "emotion": {},
                "dharma": {},
                "safety": {
                    "risk_score": risk_score["score"],
                    "risk_level": risk_score["category"],
                    "flagged": safety["flagged"],
                },
            }

        result = persona.process(text)

        return {
            "reply": result.get("reflection_text", ""),
            "emotion": result.get("emotion", {}),
            "dharma": {
                "tags": result.get("dhamma_tags", []),
                "moral_index": result.get("moral_index", 0.0),
                "tone": result.get("tone", "neutral"),
            },
            "safety": {
                "risk_score": risk_score["score"],
                "risk_level": risk_score["category"],
                "flagged": safety.get("flagged", []),
            },
        }

    return app


app = create_app()


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8080)
