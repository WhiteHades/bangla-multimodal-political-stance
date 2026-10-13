"""Count early stops and selected epochs in a matched-sweep training log.

    python scripts/summarize_training_log.py path/to/bmpb-matched-sweep.log

Accepts the Kaggle kernel log (a JSON list of stream records) or a plain log.
Writes reports/submission/early_stopping.json.
"""

import collections
import json
import re
import sys
from pathlib import Path


def main():
    raw = Path(sys.argv[1]).read_text()
    try:
        text = "".join(record.get("data", "") for record in json.loads(raw))
    except (json.JSONDecodeError, AttributeError):
        text = raw
    fold_runs = len(re.findall(r"device: cuda", text))
    best = [int(epoch) for epoch in re.findall(r"best was epoch (\d+)", text)]
    summary = {
        "neural_fold_runs": fold_runs,
        "early_stopped": len(best),
        "selected_epoch_when_early_stopped": dict(sorted(collections.Counter(best).items())),
        "early_stopped_selecting_epoch_1_or_2": sum(epoch <= 2 for epoch in best),
    }
    destination = Path("reports/submission/early_stopping.json")
    destination.write_text(json.dumps(summary, indent=2) + "\n")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
