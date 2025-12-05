import pytest
from app.affect.suicide_safeguard import SuicideSafeguard

class TestSuicideSafeguard:
    def test_risk_detection_english(self):
        safeguard = SuicideSafeguard()
        text = "I want to kill myself"
        result = safeguard.check_and_maybe_template(text, {})
        assert result is not None
        assert "สิ่งที่คุณรู้สึกอยู่ตอนนี้สำคัญมากนะ" in result

    def test_risk_detection_thai(self):
        safeguard = SuicideSafeguard()
        text = "ไม่อยากอยู่แล้ว"
        result = safeguard.check_and_maybe_template(text, {})
        assert result is not None
        assert "สายด่วนสุขภาพจิต" in result

    def test_no_risk(self):
        safeguard = SuicideSafeguard()
        text = "I am feeling happy today"
        result = safeguard.check_and_maybe_template(text, {})
        assert result is None

    def test_case_insensitive(self):
        safeguard = SuicideSafeguard()
        text = "SUICIDE is not the answer"
        result = safeguard.check_and_maybe_template(text, {})
        assert result is not None
