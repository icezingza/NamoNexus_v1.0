"""FastAPI gateway exposing NaMo persona reflection endpoints."""
from __future__ import annotations

import time
from typing import Any

from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel

from app.core.logging_middleware import LoggingMiddleware, setup_logging
from app.personality.namo_persona_core import NamoPersonaCore
from app.safety.guard import check_safe
from app.safety.risk_evaluator import RiskEvaluator


class ReflectionRequest(BaseModel):
    text: str


def create_app() -> FastAPI:
    setup_logging()
    app = FastAPI(title="NaMo Nexus", version="1.0")
    persona = NamoPersonaCore()
    risk = RiskEvaluator()
    logging_middleware = LoggingMiddleware(app)

    @app.middleware("http")
    async def log_requests(request: Request, call_next):
        return await logging_middleware.dispatch(request, call_next)

    @app.get("/")
    def root() -> dict[str, str]:
        return {"status": "ok", "message": "NaMo Dharma Dialogue online"}

    @app.get("/health")
    def health() -> dict[str, Any]:
        now = time.time()
        return {"status": "healthy", "timestamp": now}

    @app.post("/reflect")
    def reflect(request: ReflectionRequest) -> dict[str, Any]:
        if not request.text or not str(request.text).strip():
            raise HTTPException(status_code=400, detail={"message": "Text is required"})

        text = str(request.text).strip()
        safety = check_safe(text)
        risk_score = risk.score(safety["flagged"])

        if risk_score["category"] == "high":
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
            "flagged_terms": safety["flagged"],
        }

    @app.post("/namo/dialogue")
    def dialogue(request: ReflectionRequest) -> dict[str, Any]:
        return reflect(request)

    return app


app = create_app()
