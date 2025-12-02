"""Supervisor chain orchestrating core adaptive loop."""
from __future__ import annotations

import time
from dataclasses import dataclass, field
from typing import Any

from .logging_middleware import LoggingMiddleware
from .meta_learning_engine import MetaLearningEngine
from .predictive_optimizer import PredictiveOptimizer
from .symbolic_planner import plan


@dataclass
class SupervisorChainV7:
    logger: LoggingMiddleware = field(default_factory=LoggingMiddleware)
    meta_engine: MetaLearningEngine = field(default_factory=MetaLearningEngine)
    optimizer: PredictiveOptimizer = field(default_factory=PredictiveOptimizer)
    cycle_count: int = 0

    def step(self, signal: float, symbols: str | list[str]) -> dict[str, Any]:
        """Run a single supervisory cycle."""
        self.cycle_count += 1
        adaptive_factor = self.meta_engine.adjust(signal)
        prediction = self.optimizer.predict(signal * adaptive_factor)
        plan_text = plan(symbols)
        timestamp = time.time()
        self.logger.info(
            "Cycle executed",
            cycle=self.cycle_count,
            adaptive_factor=adaptive_factor,
            prediction=prediction,
            plan=plan_text,
        )
        return {
            "cycle": self.cycle_count,
            "adaptive_factor": adaptive_factor,
            "prediction": prediction,
            "plan": plan_text,
            "timestamp": timestamp,
        }

    def run_loop(self, signals: list[float], symbols: str | list[str], delay: float = 0.0) -> list[dict[str, Any]]:
        """Run through a batch of signals."""
        reports: list[dict[str, Any]] = []
        for signal in signals:
            reports.append(self.step(signal, symbols))
            if delay:
                time.sleep(delay)
        return reports
