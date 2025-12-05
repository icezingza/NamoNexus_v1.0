"""
Test for Supervisor Chain & Scenario Test (Phase 6)
"""
import pytest
from app.core.supervisor_chain_v7 import SupervisorChainV7
from app.validation.supervisor_validation import validate_cycle

def test_supervisor_initialization():
    chain = SupervisorChainV7()
    assert chain.cycle_count == 0
    assert chain.meta_engine is not None
    assert chain.optimizer is not None

def test_supervisor_step():
    chain = SupervisorChainV7()
    signal = 0.85
    symbols = "TEST_SYMBOL_FLOW"
    
    result = chain.step(signal, symbols)
    
    # Using the existing validation utility
    assert validate_cycle(chain, signal)
    
    # Detailed assertions
    assert result["cycle"] == 1
    assert "adaptive_factor" in result
    assert "prediction" in result
    assert "plan" in result
    assert result["plan"] == f"Plan derived for {symbols}"

def test_supervisor_scenario_loop():
    chain = SupervisorChainV7()
    signals = [0.1, 0.5, 0.9, 0.3]
    symbols = ["INIT", "PROCESS", "REFLECT", "CONCLUDE"]
    
    # We pass the list of symbols as a string or handle it if step accepts list?
    # Checking implementation: step takes "symbols: str | list[str]"
    # But run_loop passes "symbols" directly to step.
    # If we want vary symbols per step, run_loop in v7 doesn't support it (it passes same symbols to all).
    # We will test run_loop with a single symbol context.
    
    context_symbols = "SCENARIO_CONTEXT"
    reports = chain.run_loop(signals, context_symbols)
    
    assert len(reports) == 4
    assert chain.cycle_count == 4
    
    for i, report in enumerate(reports):
        assert report["cycle"] == i + 1
        assert "adaptive_factor" in report

if __name__ == "__main__":
    test_supervisor_initialization()
    test_supervisor_step()
    test_supervisor_scenario_loop()
    print("✅ V6 Supervisor Chain Test Passed")
