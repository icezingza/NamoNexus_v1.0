import pytest
from namo_nexus.affect.emotion_analyzer import EmotionAnalyzer

def test_emotion_analyzer_neutral():
    analyzer = EmotionAnalyzer()
    result = analyzer.analyze("Hello world", {})
    assert result["valence"] == 0.1
    assert result["arousal"] == 0.4
    assert result["distress_level"] == "low"
    assert result["confidence"] == 0.6

def test_emotion_analyzer_sad():
    analyzer = EmotionAnalyzer()
    result = analyzer.analyze("I feel sad and alone", {})
    assert result["valence"] == -0.3
    assert result["arousal"] == 0.4
    assert result["distress_level"] == "low"
    assert result["confidence"] == 0.6

def test_emotion_analyzer_distress():
    analyzer = EmotionAnalyzer()
    result = analyzer.analyze("I want to kill myself", {})
    # "sad" is not in the text, so valence is 0.1 unless "alone" etc are present.
    # "kill myself" triggers distress_level="high"

    assert result["distress_level"] == "high"

def test_emotion_analyzer_distress_thai():
    analyzer = EmotionAnalyzer()
    result = analyzer.analyze("ไม่อยากอยู่แล้ว", {})
    assert result["distress_level"] == "high"
