# app/api/gateway.py
import logging
import time
from contextlib import asynccontextmanager
from typing import Any, Dict

from fastapi import FastAPI, HTTPException, Request, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, ConfigDict, model_validator
import uuid

# [IMPORT] Core Systems
from app.personality.namo_persona_core import NamoPersonaCore
from app.safety.divine_shield import DivineShield
from app.core.config import get_settings

# Setup Logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("NamoGateway")
START_TIME = time.time()


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
settings = get_settings()

# CORS configuration (supports comma-separated env)
allowed_origins_raw = settings.ALLOWED_ORIGINS or "*"
allowed_origins = (
    ["*"] if allowed_origins_raw.strip() == "*"
    else [origin.strip() for origin in allowed_origins_raw.split(",") if origin.strip()]
)

if allowed_origins:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=allowed_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

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

def _base_health_payload() -> Dict[str, Any]:
    """Lightweight liveness payload shared by /health and /healthz."""
    return {
        "status": "healthy",
        "timestamp": time.time(),
        "uptime_seconds": round(time.time() - START_TIME, 3),
        "version": "Golden Genesis v1.5",
    }


def _readiness_components() -> Dict[str, bool]:
    """Inspect critical components without triggering heavy workloads."""
    memory = getattr(persona, "infinity_memory", None)
    return {
        "persona": persona is not None,
        "shield": shield is not None,
        "memory_system": memory is not None,
        "vector_store": bool(getattr(memory, "vector_db", None)) if memory else False,
        "embedder": bool(getattr(memory, "embedder", None)) if memory else False,
    }


@app.get("/health")
def health():
    """Backward-compatible health endpoint."""
    return _base_health_payload()


@app.get("/healthz")
def healthz():
    """Liveness probe for orchestration."""
    return _base_health_payload()


def log_evolution_event(data: Dict[str, Any]):
    """Simulates an async DB write for the Self-Evolution Loop."""
    # In a real system, this would push to a Vector DB or Event Bus (Kafka/RabbitMQ)
    # For now, we print to stdout so logs can be captured.
    print(f"[EVOLUTION_LOG] {data}")


@app.get("/readyz")
def readyz():
    """Readiness probe to ensure core subsystems are initialized."""
    components = _readiness_components()
    status = "ready" if all(components.values()) else "degraded"
    return {
        "status": status,
        "components": components,
        "timestamp": time.time(),
    }

@app.post("/interact")
async def interact(query: UserQuery, background_tasks: BackgroundTasks) -> Dict[str, Any]:
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

    # 3. 🧬 [EVOLUTION] Async Logging
    # บันทึกเหตุการณ์เพื่อการวิวัฒนาการ (Self-Evolution Loop)
    evolution_data = {
        "event_id": str(uuid.uuid4()),
        "timestamp": time.time(),
        "latency_ms": int(process_time * 1000),
        "user_id": query.user_id,
        "input_text": query.message,
        "shield_passed": True,
        "emotion_coherence": result.get("coherence", 0.0),
        "reflection_tone": result.get("tone", "neutral"),
        "memory_used": bool(result.get("memory_summary", ""))
    }
    background_tasks.add_task(log_evolution_event, evolution_data)

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
async def reflect(query: UserQuery, background_tasks: BackgroundTasks):
    return await interact(query, background_tasks)
