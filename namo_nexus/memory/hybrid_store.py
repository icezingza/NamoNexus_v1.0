from typing import List, Dict, Any, Optional
from namo_nexus.api.schemas import ChatRequest

class HybridMemoryStore:
    def __init__(self):
        self.memories: List[Dict[str, Any]] = []

    def store_interaction(self, request: ChatRequest, response: str):
        entry = {
            "user_id": request.user_id,
            "session_id": request.session_id,
            "message": request.message,
            "response": response
        }
        self.memories.append(entry)

    def retrieve(self, query: str, limit: int = 5) -> List[Dict[str, Any]]:
        # Simple keyword matching stub
        results = []
        for mem in self.memories:
            if query.lower() in mem["message"].lower():
                results.append(mem)
        return results[-limit:]
