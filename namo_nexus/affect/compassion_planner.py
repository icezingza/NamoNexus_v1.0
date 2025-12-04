from typing import Dict, Any

class CompassionPlanner:
    def plan_response_strategy(self, emotion_state: Dict[str, Any]) -> str:
        if emotion_state.get("distress_level") == "high":
            return "supportive_intervention"
        if emotion_state.get("valence", 0) < 0:
            return "empathetic_listening"
        return "balanced_dialogue"
