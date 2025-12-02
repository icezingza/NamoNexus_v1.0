"""Tests for Supervisor Stability and Self-Healing."""
import pytest
from app.core.supervisor_chain_v7 import SupervisorChainV7
from app.core.meta_learning_engine import MetaLearningEngine

class FaultyEngine(MetaLearningEngine):
    def __init__(self):
        super().__init__()
        self.should_fail = True

    def adjust(self, feedback: float) -> float:
        if self.should_fail:
            raise ValueError("Simulated Failure")
        return super().adjust(feedback)

    def reset(self) -> None:
        self.should_fail = False
        super().reset()

def test_supervisor_normal_operation():
    chain = SupervisorChainV7()
    result = chain.step(0.5, "test")

    assert result["status"] == "nominal"
    assert "stability_score" in result
    assert "stability_index" in result
    assert result["cycle"] == 1

def test_supervisor_self_healing():
    chain = SupervisorChainV7()

    # Inject faulty engine
    chain.meta_engine = FaultyEngine()

    # Failure 1
    result = chain.step(0.5, "test")
    assert result["status"] == "degraded"
    assert "error" in result
    assert chain.failure_count == 1

    # Failure 2
    result = chain.step(0.5, "test")
    assert result["status"] == "degraded"
    assert chain.failure_count == 2

    # Failure 3 -> Trigger Heal
    # MAX_FAILURES is 3. So at count 3 it triggers heal.
    result = chain.step(0.5, "test")
    assert result["status"] == "healed"
    assert chain.failure_count == 0  # Should be reset by heal

    # Next step should be successful because _heal called reset() which fixed the engine
    result = chain.step(0.5, "test")
    assert result["status"] == "nominal"
    assert chain.failure_count == 0
