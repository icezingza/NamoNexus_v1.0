"""Supervisor chain orchestrating core adaptive loop."""
from __future__ import annotations

import time
import logging
from dataclasses import dataclass, field
from typing import Any

from .meta_learning_engine import MetaLearningEngine
from .predictive_optimizer import PredictiveOptimizer
from .symbolic_planner import plan
from engine.runtime_governor import RuntimeGovernor


class SupervisorLogger:
    """Simple logger adapter to support key-value logging."""

    def info(self, msg: str, **kwargs: Any) -> None:
        kv = " ".join(f"{k}={v}" for k, v in kwargs.items())
        logging.getLogger("supervisor").info(f"{msg} {kv}")

    def error(self, msg: str, **kwargs: Any) -> None:
        kv = " ".join(f"{k}={v}" for k, v in kwargs.items())
        logging.getLogger("supervisor").error(f"{msg} {kv}")


@dataclass
class SupervisorChainV7:
    logger: SupervisorLogger = field(default_factory=SupervisorLogger)
    meta_engine: MetaLearningEngine = field(default_factory=MetaLearningEngine)
    optimizer: PredictiveOptimizer = field(default_factory=PredictiveOptimizer)
    governor: RuntimeGovernor = field(default_factory=RuntimeGovernor)
    cycle_count: int = 0
    failure_count: int = 0
    MAX_FAILURES: int = 3

    def _heal(self) -> None:
        """Reset internal engines to recover from persistent failures."""
        self.logger.info("Self-healing triggered: resetting internal engines.")
        self.meta_engine.reset()
        self.optimizer.reset()
        self.governor.reset()
        self.failure_count = 0

    def step(self, signal: float, symbols: str | list[str]) -> dict[str, Any]:
        """Run a single supervisory cycle with self-healing and stability checks."""
        try:
            self.cycle_count += 1
            adaptive_factor = self.meta_engine.adjust(signal)
            prediction = self.optimizer.predict(signal * adaptive_factor)
            plan_text = plan(symbols)

            # Integrated stability check using RuntimeGovernor
            # Derived metrics for the governor
            metrics = {
                "clarity": 0.5,  # Baseline clarity
                "coherence": min(1.0, adaptive_factor / 2.0),
                "stability": max(0.0, 1.0 - abs(prediction - signal)),
                "growth_index": adaptive_factor
            }
            stability_score = self.governor.composite_score(metrics)

            timestamp = time.time()
            self.logger.info(
                "Cycle executed",
                cycle=self.cycle_count,
                adaptive_factor=adaptive_factor,
                prediction=prediction,
                plan=plan_text,
                stability=stability_score
            )

            # Reset failure count on success
            self.failure_count = 0

            return {
                "cycle": self.cycle_count,
                "adaptive_factor": adaptive_factor,
                "prediction": prediction,
                "plan": plan_text,
                "timestamp": timestamp,
                "stability_index": self.governor.energy_state,
                "stability_score": stability_score,
                "status": "nominal"
            }

        except Exception as e:
            self.failure_count += 1
            self.logger.error("Cycle failed", error=str(e), failure_count=self.failure_count)

            if self.failure_count >= self.MAX_FAILURES:
                self._heal()
                return {
                    "cycle": self.cycle_count,
                    "error": str(e),
                    "status": "healed",
                    "message": "Self-healing triggered"
                }

            return {
                "cycle": self.cycle_count,
                "error": str(e),
                "status": "degraded"
            }

    def run_loop(self, signals: list[float], symbols: str | list[str], delay: float = 0.0) -> list[dict[str, Any]]:
        """Run through a batch of signals."""
        reports: list[dict[str, Any]] = []
        for signal in signals:
            reports.append(self.step(signal, symbols))
            if delay:
                time.sleep(delay)
        return reports
