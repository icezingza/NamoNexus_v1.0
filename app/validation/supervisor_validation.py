"""Validation utilities for supervisor chain."""
from __future__ import annotations

from app.core.supervisor_chain_v7 import SupervisorChainV7


def validate_cycle(chain: SupervisorChainV7, signal: float) -> bool:
    return isinstance(chain.step(signal, "check"), dict)
