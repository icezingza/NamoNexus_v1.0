from typing import Optional, Any, Dict
from pydantic import BaseModel

class ChatRequest(BaseModel):
    user_id: Optional[str] = None
    session_id: Optional[str] = None
    message: str

class ChatResponse(BaseModel):
    reply: str
    metadata: Optional[Dict[str, Any]] = {}
    safety_flag: bool = False
