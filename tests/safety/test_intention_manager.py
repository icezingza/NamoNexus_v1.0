import pytest
from app.safety.intention_manager import IntentionManager

def test_get_intention():
    manager = IntentionManager()
    assert manager.get_intention() == "support_and_non_harm"
