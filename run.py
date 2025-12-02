"""Legacy core entry running the supervisor chain loop."""
from __future__ import annotations

import random
from time import sleep

from app.core.supervisor_chain_v7 import SupervisorChainV7


def main() -> None:
    chain = SupervisorChainV7()
    signals = [random.uniform(-0.2, 0.5) for _ in range(5)]
    reports = chain.run_loop(signals, symbols="legacy-loop", delay=0.0)
    for report in reports:
        print(report)


if __name__ == "__main__":
    main()
