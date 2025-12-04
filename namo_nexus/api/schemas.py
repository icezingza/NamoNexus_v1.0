from pydantic import BaseModel
from typing import List, Optional, Any

class ChatRequest(BaseModel):
    message: str

class EmotionInfo(BaseModel):
    valence: float
    arousal: float
    distress_level: float
    confidence: float

class DharmaInfo(BaseModel):
    alignment_score: float
    principles: List[str]

class SafetyInfo(BaseModel):
    risk_level: str
    actions: List[str]

class MetaInfo(BaseModel):
    model: str
    latency_ms: int
    policy_version: Optional[str]
    trace_id: str

class ChatResponse(BaseModel):
    reply: str
    emotion: EmotionInfo
    dharma: DharmaInfo
    safety: SafetyInfo
    meta: MetaInfo
