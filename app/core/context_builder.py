from typing import Dict, Any
from app.api.schemas import ChatRequest
from app.memory.hybrid_store import HybridMemoryStore


class ContextBuilder:
    """Builds contextual information from memory and request metadata."""

    def build_context(self, req: ChatRequest, memory: HybridMemoryStore) -> Dict[str, Any]:
        retrieved = memory.retrieve(
            query=req.message,
            user_id=req.user_id,
            k=5,
            weights={"semantic": 0.6, "emotional": 0.25, "temporal": 0.15},
        )
        return {
            "user_id": req.user_id,
            "session_id": req.session_id,
            "retrieved_memory": retrieved,
            "locale": req.locale,
            "metadata": req.metadata,
        }
