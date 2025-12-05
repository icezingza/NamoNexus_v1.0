"""
Self-Evolution Loop Check (Deep Simulation & Data Moat)
Ensures metacognitive evolution metrics stay stable for CI/CD regression.
"""
from __future__ import annotations

import itertools

import pytest

from app.core.hypercognitive.metacognitive_evolution_loop import MetacognitiveEvolutionLoop


@pytest.mark.asyncio(scope="function")
async def test_metacognitive_evolution_loop_is_stable(monkeypatch):
    """
    Run a deterministic evolution simulation and assert metrics remain within expected bounds.

    We patch random.uniform to remove noise so CI can catch regressions in the logic, not randomness.
    """

    # Use a predictable generator: first call (fluctuation) yields 0.0, second (adaptation noise) yields 0.65, repeat.
    deterministic_values = itertools.cycle([0.0, 0.65])
    monkeypatch.setattr(
        "app.core.hypercognitive.metacognitive_evolution_loop.random.uniform",
        lambda a, b: next(deterministic_values),
    )

    loop = MetacognitiveEvolutionLoop()
    inputs = [
        (0.82, 0.78, 0.81),
        (0.76, 0.72, 0.79),
        (0.88, 0.80, 0.90),
        (0.70, 0.68, 0.74),
        (0.90, 0.85, 0.88),
    ]

    entries = [loop.simulate_self_model(*vals) for vals in inputs]

    # Evolution/adaptation should stay predictable (no degradation across releases)
    expected_evolution = (0.803, 0.757, 0.86, 0.707, 0.877)
    expected_adaptation = (0.765, 0.730, 0.807, 0.693, 0.820)

    assert [e["evolution_rate"] for e in entries] == pytest.approx(expected_evolution, abs=1e-3, rel=1e-6)
    assert [e["adaptation_score"] for e in entries] == pytest.approx(expected_adaptation, abs=1e-3, rel=1e-6)
    assert loop.summarize()["cycles"] == 5

    projection = loop.project_future_state()
    assert projection["trend"] == "ASCENDING"
    assert projection["predicted_state"] == pytest.approx(0.782, rel=1e-6)
