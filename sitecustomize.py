"""Compatibility patch for pydantic v1 on Python 3.12 ForwardRef changes."""
from __future__ import annotations

from typing import ForwardRef

_original_forwardref_evaluate = ForwardRef._evaluate


def _patched_evaluate(self, globalns=None, localns=None, type_params=None, *, recursive_guard=None):
    guard = set() if recursive_guard is None else recursive_guard
    return _original_forwardref_evaluate(self, globalns, localns, type_params, recursive_guard=guard)


ForwardRef._evaluate = _patched_evaluate  # type: ignore[attr-defined]
