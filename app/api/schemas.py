from typing import Optional, Dict, Any, List
from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    user_id: Optional[str] = Field(default=None)
    session_id: Optional[str] = Field(default=None)
    message: str
    locale: str = Field(default="th-TH")
    client: Optional[str] = Field(default=None)
    metadata: Dict[str, Any] = Field(default_factory=dict)


class EmotionInfo(BaseModel):
    valence: float
    arousal: float
    distress_level: str
    confidence: float


class DharmaInfo(BaseModel):
    alignment_score: float
    principles: List[str] = Field(default_factory=list)


class SafetyInfo(BaseModel):
    risk_level: str
    actions: List[str] = Field(default_factory=list)


class MetaInfo(BaseModel):
    model: Optional[str] = None
    latency_ms: Optional[int] = None
    policy_version: Optional[str] = None
    trace_id: Optional[str] = None


class ChatResponse(BaseModel):
    reply: str
    emotion: EmotionInfo
    dharma: DharmaInfo
    safety: SafetyInfo
    meta: MetaInfo
