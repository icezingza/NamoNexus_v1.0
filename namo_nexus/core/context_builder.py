from typing import Dict, Any, List
from namo_nexus.api.schemas import ChatRequest

class ContextBuilder:
    def build_context(self, request: ChatRequest, history: List[Dict[str, Any]]) -> Dict[str, Any]:
        return {
            "user_id": request.user_id,
            "session_id": request.session_id,
            "recent_history": history,
            "derived_intent": "general_chat" # Simplified
        }
