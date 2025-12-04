"""Simple symbolic planner for text-based inputs."""
from __future__ import annotations

from typing import Iterable


def plan(symbols: str | Iterable[str]) -> str:
    """Return a high-level plan string given symbols or text."""
    if isinstance(symbols, str):
        tokens = symbols.split()
    else:
        tokens = list(symbols)
    if not tokens:
        return "Observe quietly and hold space for reflection."
    primary = tokens[0]
    return f"Acknowledge '{primary}', explore intentions, respond with care."
