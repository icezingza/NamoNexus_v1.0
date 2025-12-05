"""Simple symbolic planner for text-based inputs."""
from __future__ import annotations

from typing import Iterable


def plan(symbols: str | Iterable[str]) -> str:
    """Return a high-level plan string given symbols or text."""
    if isinstance(symbols, str):
        symbol_text = symbols.strip()
    else:
        symbol_text = " ".join(str(s) for s in symbols).strip()

    if not symbol_text:
        return "Observe quietly and hold space for reflection."

    return f"Plan derived for {symbol_text}"
