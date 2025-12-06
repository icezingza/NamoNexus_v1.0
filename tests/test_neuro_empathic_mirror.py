import os
from unittest.mock import patch, MagicMock
from app.emotion.neuro_empathic_mirror import NeuroEmpathicMirror

def test_neuro_empathic_mirror_simulation_mode():
    # Force simulation mode via environment variable
    with patch.dict(os.environ, {"NAMO_EMOTION_SIM_MODE": "1"}):
        mirror = NeuroEmpathicMirror()
        assert mirror.analyzer is None

        # Test keyword matching
        response_joy = mirror.reflect("I am so happy and good!")
        assert response_joy.emotional_matching_score == 0.8
        assert "joy" in str(mirror.analyze_emotion_depth("happy")).lower() or response_joy.emotional_matching_score > 0.5

        response_sad = mirror.reflect("I feel sad and bad.")
        assert response_sad.emotional_matching_score == 0.8

        # Test unknown emotion defaults
        response_neutral = mirror.reflect("Just a neutral statement.")
        assert response_neutral.emotional_matching_score == 0.1 # Default value

def test_neuro_empathic_mirror_transformers_missing():
    # Simulate transformers not installed
    with patch("app.emotion.neuro_empathic_mirror.HAS_TRANSFORMERS", False):
        mirror = NeuroEmpathicMirror()
        assert mirror.analyzer is None

        # Should fall back to simulation
        response = mirror.reflect("I am happy")
        assert response.emotional_matching_score == 0.8

def test_template_loading_failure():
    # Test handling of missing policies.json
    with patch("builtins.open", side_effect=FileNotFoundError):
        with patch.dict(os.environ, {"NAMO_EMOTION_SIM_MODE": "1"}):
            mirror = NeuroEmpathicMirror()
            # It should default to "I am happy for you" for joy or "I am listening deeply" if template missing
            # The code defaults to {"joy": ["I am happy for you."]} on error
            assert mirror.empathy_templates.get("joy") == ["I am happy for you."]

def test_deterministic_template_selection():
    with patch.dict(os.environ, {"NAMO_EMOTION_SIM_MODE": "1"}):
        mirror = NeuroEmpathicMirror()
        templates = ["Template A", "Template B", "Template C"]

        # Same input should yield same template
        result1 = mirror._select_template(templates, "Input 1")
        result2 = mirror._select_template(templates, "Input 1")
        assert result1 == result2

        # Different input might yield different template (depends on hash)
        # We can't guarantee different result but we guarantee determinism
