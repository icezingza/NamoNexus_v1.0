"""Risk evaluator returning simple score and category."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class RiskEvaluator:
    def score(self, flagged_terms: list[str]) -> dict[str, object]:
        score = min(1.0, 0.2 * len(flagged_terms))
        if score >= 0.6:
            category = "high"
        elif score >= 0.3:
            category = "medium"
        else:
            category = "low"
        return {"score": score, "category": category}
