"""FastAPI gateway exposing NaMo persona reflection endpoints."""
from __future__ import annotations

import time
from typing import Any

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from app.personality.namo_persona_core import NamoPersonaCore
from app.safety.guard import check_safe
from app.safety.risk_evaluator import RiskEvaluator


class ReflectionRequest(BaseModel):
    text: str


def create_app() -> FastAPI:
    app = FastAPI(title="NaMo Nexus", version="1.0")
    persona = NamoPersonaCore()
    risk = RiskEvaluator()

    @app.get("/")
    def root() -> dict[str, str]:
        return {"status": "ok", "message": "NaMo Dharma Dialogue online"}

    @app.get("/health")
    def health() -> dict[str, Any]:
        now = time.time()
        return {"status": "healthy", "timestamp": now}

    @app.post("/reflect")
    def reflect(request: ReflectionRequest) -> dict[str, Any]:
        safety = check_safe(request.text)
        risk_score = risk.score(safety["flagged"])
        if not safety["safe"]:
            raise HTTPException(status_code=400, detail={"message": "Content blocked", "risk": risk_score})
        result = persona.process(request.text)
        return {"result": result, "risk": risk_score}

    @app.post("/namo/dialogue")
    def dialogue(request: ReflectionRequest) -> dict[str, Any]:
        return reflect(request)

    return app


app = create_app()
