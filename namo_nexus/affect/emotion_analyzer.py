from typing import Dict, Any


class EmotionAnalyzer:
    """Simple placeholder emotion analyzer."""

    def analyze(self, text: str, context: Dict[str, Any]) -> Dict[str, Any]:
        lowered = text.lower()
        valence = -0.3 if any(w in lowered for w in ["sad", "tired", "empty", "alone"]) else 0.1
        distress_level = "high" if "kill myself" in lowered or "ไม่อยากอยู่" in lowered else "low"

        return {
            "valence": valence,
            "arousal": 0.4,
            "distress_level": distress_level,
            "confidence": 0.6,
        }
