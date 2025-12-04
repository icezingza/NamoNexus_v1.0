from typing import Dict, Any, List, Optional
from namo_nexus.api.schemas import ChatRequest


class HybridMemoryStore:
    """Hybrid memory store combining semantic, emotional and temporal aspects.
    Current implementation is in-memory stub; later can be backed by DB/vector store.
    """

    def __init__(self) -> None:
        self._store: List[Dict[str, Any]] = []

    def store_interaction(
        self,
        req: ChatRequest,
        reply: str,
        emotion: Dict[str, Any],
        dharma: Dict[str, Any],
    ) -> None:
        item = {
            "user_id": req.user_id,
            "session_id": req.session_id,
            "text": req.message,
            "reply": reply,
            "emotion": emotion,
            "dharma": dharma,
        }
        self._store.append(item)

    def retrieve(
        self,
        query: str,
        user_id: Optional[str],
        k: int,
        weights: Dict[str, float],
    ) -> List[Dict[str, Any]]:
        # TODO: implement real semantic retrieval
        # For now, return last k items for that user
        candidates = [m for m in self._store if m.get("user_id") == user_id]
        return candidates[-k:]
