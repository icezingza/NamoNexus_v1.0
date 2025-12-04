import pytest
from namo_nexus.core.orchestrator import Orchestrator
from namo_nexus.api.schemas import ChatRequest

def test_orchestrator_initialization():
    orch = Orchestrator()
    assert orch is not None

def test_orchestrator_process_chat():
    orch = Orchestrator()
    req = ChatRequest(message="Hello, I am feeling sad.")
    resp = orch.process_chat(req)

    assert resp is not None
    assert resp.reply == "This is a compassionate reply."
    assert resp.emotion.confidence == 0.9
    assert resp.dharma.alignment_score == 0.8
    assert resp.safety.risk_level == "low"
    assert resp.meta.model == "upstream-llm"
