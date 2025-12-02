"""Signature matrix evolving with each reflection."""
from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class SignatureMatrix:
    signatures: dict[str, float] = field(default_factory=dict)

    def update(self, key: str, value: float) -> dict[str, float]:
        current = self.signatures.get(key, 0.0)
        self.signatures[key] = round(0.7 * current + 0.3 * value, 4)
        return self.signatures

    def snapshot(self) -> dict[str, float]:
        return dict(self.signatures)
