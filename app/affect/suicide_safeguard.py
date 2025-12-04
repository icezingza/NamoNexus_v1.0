# namo_nexus/affect/suicide_safeguard.py
from typing import Dict, Any, Optional


class SuicideSafeguard:
    """Detects suicidal/self-harm content and routes to safe templates."""

    def check_and_maybe_template(self, text: str, emotion: Dict[str, Any]) -> Optional[str]:
        lowered = text.lower()
        risk = (
            "kill myself" in lowered
            or "suicide" in lowered
            or "ไม่อยากอยู่" in lowered
            or "อยากหายไป" in lowered
        )

        if risk:
            return (
                "สิ่งที่คุณรู้สึกอยู่ตอนนี้สำคัญมากนะ "
                "ถ้ารู้สึกว่าจะทำร้ายตัวเอง ขอให้หยุดทุกอย่างก่อน แล้วติดต่อคนที่ไว้ใจได้ "
                "หรือสายด่วนสุขภาพจิตในพื้นที่ของคุณทันที "
                "ผมอยู่ตรงนี้เพื่อฟังและค่อย ๆ คิดไปด้วยกันกับคุณ"
            )
        return None
