from typing import Dict, Any


class MetaAwareness:
    """Tracks coarse-grained internal state for evolution and drift detection."""

    def __init__(self) -> None:
        self._counter = 0

    def observe(
        self,
        message: str,
        reply: str,
        emotion: Dict[str, Any],
        dharma: Dict[str, Any],
    ) -> None:
        self._counter += 1
        # TODO: store lightweight signals somewhere if needed
