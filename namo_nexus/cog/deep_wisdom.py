from typing import List, Dict, Any


class DeepWisdom:
    """Stub deep wisdom engine based on dhammic principles."""

    def __init__(self) -> None:
        self._principles = [
            "อนิจจัง",
            "ทุกข์",
            "อนัตตา",
            "เมตตา",
            "กรุณา",
        ]

    def get_relevant_principles(self, message: str, context: Dict[str, Any]) -> List[str]:
        # TODO: real retrieval; now always return a small fixed subset
        return ["เมตตา", "เห็นทุกข์", "ไม่โทษตัวเอง"]
