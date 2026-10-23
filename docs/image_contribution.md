# Local comparison of image contribution

The configuration `configs/ablations/image_contribution.yaml` fixes the
comparison before execution. Its protocol is the proposal at Git revision
`f99ab56f38956345fbbb92af90c94d2317c86e0f`, in
`docs/replication_protocol.md`. That proposal was written after historical
results were available. This experiment predicts the existing stored labels
on a recovered input snapshot.

The runner compares character text features, the same text features with a
fixed image feature block, and that image block alone. It checks the text
and image blocks for exact equality across the relevant conditions. It uses
the frozen 149 item population, the saved seed 42 folds, and four additional
fold assignments fixed in the configuration. All conditions use the same
classifier parameters and 2,000 iteration limit. Augmentation is disabled.

Before any model fitting, the implementation review added descriptive source
group intervals for each condition's pooled macro F1 and for the secondary
image versus text comparison. The primary comparison and its decision rules
remain those in the proposal. The primary interval from the existing paired
helper must exactly match the separately calculated group bootstrap interval.
These intervals condition on fitted predictions. They do not include model
refitting, annotation, event, or outlet uncertainty. Repeated fold seeds reuse
the same items.

Run from the repository root with the separate CUDA environment:

```sh
.venv-gpu/bin/python -m scripts.image_contribution
```

The command requires a clean, committed implementation. Its default output is
a new directory under `experiments/`. An existing output directory is rejected.
The runner verifies the input bundle, freezes its plan, and downloads only the
named public model revision. It writes image features and processor metadata,
training diagnostics, predictions, scores, and an artifact checksum manifest.
Failures remain in the new directory with a failure record. Historical reports
and input files are not output destinations.

The small local check uses explicitly synthetic text and image features:

```sh
mkdir -p .tmp
rustc --edition=2021 checks/image_contribution.rs -o .tmp/check_image_contribution
.tmp/check_image_contribution .venv-gpu/bin/python
```

It checks that the added image block can affect predictions, that all three
conditions score the same held out items, and that duplicate IDs or fold members
are rejected without changing completed outputs. It does not run a model or
produce a benchmark score.

After the experiment, repeat the text condition through the existing CV runner
with the same selected corpus, seed, folds, and augmentation disabled. Require
identical item predictions before interpreting the new comparison. Recalculate
the summaries from saved predictions and verify every artifact checksum.
Independent Bangla review and historical image byte identity remain separate
evidence requirements. Author adoption of the study remains a separate decision.
