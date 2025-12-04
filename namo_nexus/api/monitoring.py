"""System monitoring utilities."""
from __future__ import annotations

import time
from typing import Any

try:
    import psutil
except ImportError:  # pragma: no cover - optional dependency
    psutil = None  # type: ignore


def get_metrics() -> dict[str, Any]:
    metrics: dict[str, Any] = {"timestamp": time.time()}
    if psutil:
        metrics["cpu_percent"] = psutil.cpu_percent(interval=0.1)
        metrics["memory_percent"] = psutil.virtual_memory().percent
    else:
        metrics["cpu_percent"] = None
        metrics["memory_percent"] = None
    return metrics
