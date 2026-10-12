"""Tabulate the matched sweep and estimate paired macro-F1 differences.

Comparisons are fixed here before results are seen: every vision-language model
against each of two text references, TF-IDF/logistic regression and BanglaBERT,
on the same readable-image items and outer folds. The interval resamples source
groups (not items) 2,000 times, because items sharing a source are not
independent.

    python scripts/matched_analysis.py experiments/matched
"""

import argparse
import json
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.metrics import f1_score

from bmpb.data.groups import source_groups
from bmpb.paths import CORPUS

TEXT_REFERENCES = ["tfidf_logreg", "banglabert"]
MULTIMODAL = ["countvec_vit", "clip", "align", "blip", "vilt", "flava"]
RESAMPLES = 2000
SEED = 42


def macro_f1(y_true, y_pred):
    return f1_score(y_true, y_pred, labels=[0, 1, 2], average="macro", zero_division=0)


def predictions(root: Path, population: str, name: str) -> pd.DataFrame:
    runs = sorted((root / population).glob(f"cv-{name}-*/predictions.csv"))
    if not runs:
        raise FileNotFoundError(f"no predictions for {population}/{name}")
    return pd.read_csv(runs[-1])


def paired_difference(a: pd.DataFrame, b: pd.DataFrame, groups: pd.Series) -> dict:
    merged = a.merge(b, on=["item_id", "label"], suffixes=("_a", "_b"))
    if len(merged) != len(a) or len(merged) != len(b):
        raise AssertionError("paired comparison requires identical item populations")
    if not (merged["fold_a"] == merged["fold_b"]).all():
        raise AssertionError("paired comparison requires identical outer folds")
    merged["group"] = merged["item_id"].map(groups)
    observed = macro_f1(merged.label, merged.predicted_a) - macro_f1(
        merged.label, merged.predicted_b
    )
    members = [g.index.to_numpy() for _, g in merged.groupby("group")]
    rng = np.random.default_rng(SEED)
    y = merged["label"].to_numpy()
    pa, pb = merged["predicted_a"].to_numpy(), merged["predicted_b"].to_numpy()
    deltas = np.empty(RESAMPLES)
    for r in range(RESAMPLES):
        index = np.concatenate([members[i] for i in rng.integers(len(members), size=len(members))])
        deltas[r] = macro_f1(y[index], pa[index]) - macro_f1(y[index], pb[index])
    lo, hi = np.percentile(deltas, [2.5, 97.5])
    return {
        "n": int(len(merged)),
        "groups": len(members),
        "delta_macro_f1": float(observed),
        "ci95": [float(lo), float(hi)],
        "share_resamples_above_zero": float((deltas > 0).mean()),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", type=Path)
    parser.add_argument("--dest", type=Path, default=Path("reports/submission"))
    args = parser.parse_args()

    summary = json.loads((args.root / "sweep_summary.json").read_text())
    lines = [
        "| Population | Model | Status | n | Accuracy | Pooled macro-F1 | 95% CI | "
        "Fold mean ± SD | F1 gc | F1 neu | F1 gl | Notes |",
        "| --- | --- | --- | ---: | ---: | ---: | --- | --- | ---: | ---: | ---: | --- |",
    ]
    for row in summary:
        if row["status"] != "ok":
            lines.append(
                f"| {row['population']} | {row['name']} | failed: {row['error'][:60]} "
                "|  |  |  |  |  |  |  |  |  |"
            )
            continue
        lo, hi = row["macro_f1_ci95"]
        f1 = row["per_class_f1"]
        lines.append(
            f"| {row['population']} | {row['name']} | ok | {row['items_scored']} | "
            f"{row['accuracy']:.3f} | {row['macro_f1']:.3f} | {lo:.3f}–{hi:.3f} | "
            f"{row['fold_macro_f1_mean']:.3f} ± {row['fold_macro_f1_sd']:.3f} | "
            f"{f1['govt_critique']:.3f} | {f1['neutral']:.3f} | {f1['govt_leaning']:.3f} | "
            f"{'; '.join(row['notes'])} |"
        )

    corpus = pd.read_csv(CORPUS)
    groups = pd.Series(source_groups(corpus).to_numpy(), index=corpus["item_id"])
    ok = {(r["population"], r["name"]) for r in summary if r["status"] == "ok"}
    comparisons = []
    for model in MULTIMODAL:
        for reference in TEXT_REFERENCES:
            if {("paired_headlines", model), ("paired_headlines", reference)} - ok:
                comparisons.append({"model": model, "reference": reference, "status": "missing"})
                continue
            result = paired_difference(
                predictions(args.root, "paired_headlines", model),
                predictions(args.root, "paired_headlines", reference),
                groups,
            )
            comparisons.append({"model": model, "reference": reference, **result})

    lines += [
        "",
        "Paired macro-F1 difference (vision-language minus text), readable-image items, "
        f"source-group bootstrap with {RESAMPLES} resamples:",
        "",
        "| Model | Text reference | n | Groups | Δ macro-F1 | 95% CI | Share Δ>0 |",
        "| --- | --- | ---: | ---: | ---: | --- | ---: |",
    ]
    for c in comparisons:
        if c.get("status") == "missing":
            lines.append(f"| {c['model']} | {c['reference']} | missing |  |  |  |  |")
            continue
        lo, hi = c["ci95"]
        lines.append(
            f"| {c['model']} | {c['reference']} | {c['n']} | {c['groups']} | "
            f"{c['delta_macro_f1']:+.3f} | {lo:+.3f} to {hi:+.3f} | "
            f"{c['share_resamples_above_zero']:.3f} |"
        )

    args.dest.mkdir(parents=True, exist_ok=True)
    (args.dest / "matched.json").write_text(
        json.dumps({"runs": summary, "paired_differences": comparisons}, indent=2) + "\n"
    )
    (args.dest / "matched.md").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
