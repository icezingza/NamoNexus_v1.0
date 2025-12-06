from unittest.mock import MagicMock, patch
import pytest
from app.personality.namo_persona_core import NamoPersonaCore
from app.emotion.neuro_empathic_mirror import EmpathicResponse

@pytest.mark.asyncio
async def test_namo_persona_core_process():
    # Mock dependencies
    mock_mirror = MagicMock()
    mock_mirror.reflect.return_value = EmpathicResponse(
        response_text="I understand your feelings.",
        emotional_matching_score=0.9,
        support_level="High"
    )

    mock_memory = MagicMock()
    mock_memory.retrieve_context.return_value = ["Previous interaction about happiness"]

    mock_reflection = MagicMock()
    mock_reflection.reflect.return_value = {
        "reflection": "Mindfulness is key.",
        "moral_index": 0.85,
        "tone": "compassionate"
    }

    # Instantiate Core with mocks
    core = NamoPersonaCore(
        empathic_mirror=mock_mirror,
        infinity_memory=mock_memory,
        reflection_engine=mock_reflection,
        retrieval_engine=MagicMock()
    )

    # Act
    result = await core.process("I am feeling great today!")

    # Assert
    assert result["tone"] == "High"
    assert result["coherence"] == 0.9
    assert "I understand your feelings." in result["reflection_text"]
    assert "Mindfulness is key." in result["reflection_text"]
    assert result["dhamma_tags"] == ["compassionate"]

    # Verify interactions
    mock_mirror.reflect.assert_called_once_with("I am feeling great today!")
    mock_memory.store_memory.assert_called_once()
    mock_reflection.reflect.assert_called_once()

@pytest.mark.asyncio
async def test_namo_persona_core_process_memory_disabled():
    # Mock dependencies
    mock_mirror = MagicMock()
    mock_mirror.reflect.return_value = EmpathicResponse("Response", 0.5, "Medium")

    mock_memory = MagicMock()
    mock_reflection = MagicMock()
    mock_reflection.reflect.return_value = {"reflection": "Reflect"}

    core = NamoPersonaCore(
        empathic_mirror=mock_mirror,
        infinity_memory=mock_memory,
        reflection_engine=mock_reflection
    )

    # Mock settings using patch
    with patch("app.personality.namo_persona_core.get_settings") as mock_settings:
        mock_settings.return_value.FEATURE_FLAGS = {"ENABLE_INFINITY_MEMORY": False}

        result = await core.process("Hello")

        assert "Memory system inactive" in result["memory_summary"]
        mock_memory.store_memory.assert_not_called()
