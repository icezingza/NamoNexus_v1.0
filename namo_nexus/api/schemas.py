from pydantic import BaseModel
from typing import Optional

class ChatRequest(BaseModel):
    user_id: str
    session_id: str
    message: str
