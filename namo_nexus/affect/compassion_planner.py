from typing import Dict, Any, Optional


class CompassionPlanner:
    """Plans a compassionate, grounded reply."""

    def plan_reply(
        self,
        original_message: str,
        dharma_view: Dict[str, Any],
        emotion: Dict[str, Any],
        safe_template: Optional[str],
    ) -> str:
        if safe_template:
            return safe_template

        base = "ขอบคุณที่ไว้ใจเล่าให้ฟังนะ "
        if emotion["distress_level"] == "high":
            base += "ตอนนี้ขอชวนค่อย ๆ หายใจลึก ๆ แล้วรับรู้ว่าความรู้สึกนี้ไม่ได้อยู่ถาวร "
        base += "เราลองคุยกันทีละขั้นได้เสมอ"

        return base
