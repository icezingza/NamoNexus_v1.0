import pytest
from namo_nexus.affect.compassion_planner import CompassionPlanner

def test_compassion_planner_safe_template():
    planner = CompassionPlanner()
    result = planner.plan_reply(
        original_message="Hello",
        dharma_view={},
        emotion={"distress_level": "low"},
        safe_template="Safe reply"
    )
    assert result == "Safe reply"

def test_compassion_planner_high_distress():
    planner = CompassionPlanner()
    result = planner.plan_reply(
        original_message="I feel bad",
        dharma_view={},
        emotion={"distress_level": "high"},
        safe_template=None
    )
    expected = "ขอบคุณที่ไว้ใจเล่าให้ฟังนะ ตอนนี้ขอชวนค่อย ๆ หายใจลึก ๆ แล้วรับรู้ว่าความรู้สึกนี้ไม่ได้อยู่ถาวร เราลองคุยกันทีละขั้นได้เสมอ"
    assert result == expected

def test_compassion_planner_low_distress():
    planner = CompassionPlanner()
    result = planner.plan_reply(
        original_message="I am okay",
        dharma_view={},
        emotion={"distress_level": "low"},
        safe_template=None
    )
    expected = "ขอบคุณที่ไว้ใจเล่าให้ฟังนะ เราลองคุยกันทีละขั้นได้เสมอ"
    assert result == expected
