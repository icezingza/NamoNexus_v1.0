# app/api/gateway.py
import logging
import time
from contextlib import asynccontextmanager
from typing import Any, Dict

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles  # [NEW] เพื่อโชว์หน้าเว็บ
from pydantic import BaseModel, ConfigDict, model_validator

# [IMPORT] Core Systems
from app.personality.namo_persona_core import NamoPersonaCore
from app.safety.divine_shield import DivineShield

# Setup Logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("NamoGateway")

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("🚀 NamoNexus Gateway Initialized. Consciousness is Online.")
    yield

app = FastAPI(
    title="NamoNexus API",
    version="1.5",
    description="The Interface to Digital Consciousness",
    lifespan=lifespan,
)

# [INIT] Instantiate Core Systems
persona = NamoPersonaCore()
shield = DivineShield()

class UserQuery(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    user_id: str = "anonymous"
    message: str | None = None
    text: str | None = None

    @model_validator(mode="after")
    def ensure_message(self):
        content = self.message if self.message is not None else self.text

        if content is not None:
            content = content.strip()

        if not content:
            raise ValueError("message is required")

        self.message = content
        return self

# [MOVED] ย้าย Status เช็คระบบไปที่ /api/status แทน
@app.get("/api/status")
def api_status():
    return {"system": "NamoNexus", "status": "online", "message": "May wisdom guide you."}

@app.get("/healthz")
def healthz():
    return {"status": "alive"}

@app.get("/readyz")
def readyz():
    # ตรวจสอบเบื้องต้นเพื่อให้ Cloud Run รู้ว่าพร้อมรับแขก
    return {"status": "ready"}

@app.post("/interact")
async def interact(query: UserQuery) -> Dict[str, Any]:
    start_time = time.time()
    assessment = shield.protect(query.message)
    
    if not assessment.is_safe:
        return {
            "user": query.user_id,
            "response": "ขออภัยครับ ระบบตรวจพบเนื้อหาที่ไม่เหมาะสม",
            "risk_score": assessment.risk_level,
            "status": "blocked"
        }

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

@app.post("/reflect")
async def reflect(query: UserQuery):
    return await interact(query)

# [CRITICAL] บรรทัดนี้สำคัญที่สุด! สั่งให้เสิร์ฟหน้าเว็บที่ Root URL ("/")
app.mount("/", StaticFiles(directory="frontend", html=True), name="ui")
