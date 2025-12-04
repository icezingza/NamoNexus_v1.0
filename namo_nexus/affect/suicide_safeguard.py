from typing import Dict, Any, Optional

class SuicideSafeguard:
    def check_safety(self, text: str, emotion_state: Dict[str, Any]) -> Optional[str]:
        triggers = ["kill myself", "suicide", "end it all", "ไม่อยากอยู่"]
        for trigger in triggers:
            if trigger in text.lower():
                return "DETECTED_SELF_HARM_RISK"
        return None
