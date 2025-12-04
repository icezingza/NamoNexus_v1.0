from typing import Dict, Any
from pydantic import BaseModel, Field

class ChatRequest(BaseModel):
    message: str
    user_id: str
    session_id: str
    locale: str = "en-US"
    metadata: Dict[str, Any] = Field(default_factory=dict)
