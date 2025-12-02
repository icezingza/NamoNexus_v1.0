"""Supervisor entry point for validating and running the stability layer."""
import argparse
import logging
import sys
from typing import NoReturn

from app.core.supervisor_chain_v7 import SupervisorChainV7

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
)
logger = logging.getLogger(__name__)

def main() -> NoReturn:
    parser = argparse.ArgumentParser(description="Supervisor Layer Validation")
    parser.add_argument("--check-only", action="store_true", help="Perform a self-check and exit")
    args = parser.parse_args()

    if args.check_only:
        logger.info("Initializing Supervisor Chain for validation...")
        try:
            supervisor = SupervisorChainV7()
            logger.info("Supervisor Chain initialized.")

            logger.info("Running diagnostic step...")
            # Run a dummy step to verify logic
            result = supervisor.step(signal=0.5, symbols=["validation", "check"])
            logger.info("Step Result: %s", result)

            # Additional check: ensure keys exist
            required_keys = ["cycle", "adaptive_factor", "prediction", "plan", "timestamp"]
            missing_keys = [k for k in required_keys if k not in result]
            if missing_keys:
                raise ValueError(f"Missing keys in result: {missing_keys}")

            logger.info("Supervisor check passed.")
            sys.exit(0)
        except Exception as e:
            logger.error("Supervisor check failed: %s", e, exc_info=True)
            sys.exit(1)
    else:
        logger.info("Supervisor running... (Not implemented)")
        # Future implementation for running the loop indefinitely
        sys.exit(0)

if __name__ == "__main__":
    main()
