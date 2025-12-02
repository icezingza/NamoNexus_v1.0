from app.core.supervisor_chain_v7 import SupervisorChainV7

def test_supervisor_chain_step():
    chain = SupervisorChainV7()
    result = chain.step(1.0, "test")
    assert isinstance(result, dict)
    assert result["cycle"] == 1
    assert "adaptive_factor" in result
