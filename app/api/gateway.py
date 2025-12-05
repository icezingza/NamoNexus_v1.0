# app/api/gateway.py
import logging
import time
from contextlib import asynccontextmanager
from typing import Any, Dict

from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel, ConfigDict, model_validator

# [IMPORT] Core Systems
from app.personality.namo_persona_core import NamoPersonaCore
from app.safety.divine_shield import DivineShield
from app.core.config import get_settings

# Setup Logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("NamoGateway")


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("🚀 NamoNexus Gateway Initialized. Consciousness is Online.")
    yield


# Initialize App
app = FastAPI(
    title="NamoNexus API", 
    version="1.0",
    description="The Interface to Digital Consciousness",
    lifespan=lifespan,
)

# [INIT] Instantiate Core Systems
# Persona = สมอง (Infinity) + หัวใจ (Neuro-Empathy) + ปัญญา (Dharma)
persona = NamoPersonaCore()
# Shield = เกราะป้องกัน (Chinabanchorn 8-Layers)
shield = DivineShield()

class UserQuery(BaseModel):
    """Inbound chat payload with backward-compatible alias for message."""

    model_config = ConfigDict(populate_by_name=True)

    user_id: str = "anonymous"
    message: str | None = None
    text: str | None = None

    @model_validator(mode="after")
    def ensure_message(self):
        if not self.message and self.text:
            self.message = self.text
        if not self.message:
            raise ValueError("message is required")
        return self

@app.get("/")
def root():
    return {
        "system": "NamoNexus",
        "status": "online", 
        "message": "May wisdom and compassion guide you."
    }

@app.get("/health")
def health():
    """System Health Check"""
    return {
        "status": "healthy",
        "timestamp": time.time(),
        "version": "Golden Genesis v1.5"
    }

@app.post("/interact")
async def interact(query: UserQuery) -> Dict[str, Any]:
    """
    Main Interaction Endpoint
    Flow: User -> Shield -> Persona (Brain+Heart) -> Response
    """
    start_time = time.time()
    
    # 1. 🛡️ [SHIELD] Check for threats first
    assessment = shield.protect(query.message)
    
    if not assessment.is_safe:
        logger.warning(f"Blocked threat: {assessment.reason}")
        return {
            "user": query.user_id,
            "response": "ขออภัยครับ ระบบตรวจพบเนื้อหาที่ไม่เหมาะสม (Safety Protocol Activated)",
            "risk_score": assessment.risk_level,
            "status": "blocked"
        }

    # 2. 🧠 [PERSONA] Process consciousness
    # Persona จะจัดการเรื่องความจำ (Store) และอารมณ์ (Feel) ให้เองภายใน
    result = await persona.process(query.message)
    
    process_time = round(time.time() - start_time, 3)

    return {
        "user": query.user_id,
        "response": result.get("reflection_text", ""),
        "reflection_text": result.get("reflection_text", ""),
        "tone": result.get("tone"),
        "meta_data": {
            "tone": result.get("tone"),
            "coherence": result.get("coherence"),
            "memory_context": result.get("memory_summary"),
            "process_time": process_time
        }
    }

# Alias endpoint for compatibility
@app.post("/reflect")
async def reflect(query: UserQuery):
    return await interact(query)
