"""Safety guard for basic content checks."""
from __future__ import annotations

from typing import Any

HARMFUL_KEYWORDS = {"harm", "violence", "attack", "weapon", "kill"}


def check_safe(text: str) -> dict[str, Any]:
    lowered = text.lower()
    flagged = [word for word in HARMFUL_KEYWORDS if word in lowered]
    safe = not flagged
    return {"safe": safe, "flagged": flagged}
