"""Validation utilities for supervisor chain."""
from __future__ import annotations

from namo_nexus.core.orchestrator import SupervisorChainV7


def validate_cycle(chain: SupervisorChainV7, signal: float) -> bool:
    return isinstance(chain.step(signal, "check"), dict)
