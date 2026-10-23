# Ordered review branches

The branches below separate the completed contribution into four review units.
They form a stack. Each branch starts from the preceding branch, so its review
diff contains only the next unit. The original integrated branch remains
available. No default branch merge or upstream PR is part of this work.

GitHub uses `tree` in a URL when displaying a branch. The slash in a branch
name such as `agent/review-01-evidence` does not create a repository directory.
The `agent/` prefix follows this repository's contribution instructions.

| Order | Review branch | Base | Scope |
| :--- | :--- | :--- | :--- |
| 1 | `agent/review-01-evidence` | `main` at `a935d11` | Summary checks, original baseline reproduction record, and recovered image input evidence |
| 2 | `agent/review-02-experiments` | `agent/review-01-evidence` | Run identity, resume, aggregation, scoring, BLIP, and input verification |
| 3 | `agent/review-03-data` | `agent/review-02-experiments` | Download behavior, annotation formats, local export, and dataset card corrections |
| 4 | `agent/review-04-paper` | `agent/review-03-data` | Factual manuscript corrections, primary literature comparison, proposed study, and handoff |

The grouping keeps revision resolution with all model loaders that use it.
It also keeps BLIP loading and feature selection in that unit because they
change the same wrapper. The evidence check comes first because it is small
and works without the private data or model packages. The paper unit comes
last because its descriptions refer to the completed implementation.

## Evidence unit

Run `python scripts/verify_reports.py` from the branch checkout. It recalculates
20 matched scores and checks 100 seed scores and 60 paired comparisons. It
checks four separately recorded baseline reproduction summaries and the new
image recovery summary. It does not train models or open the private inputs.

Compile `checks/reports.rs` with Rust 2021 and pass the Python executable to
the resulting program. The check must accept the committed reports, preserve
the originals, and reject deliberately corrupted score and image count copies.
The original numerical files under `reports/submission/` must match `a935d11`.

The original baseline reproduction remains a separate evidence record, with
source and artifact checksums. The image recovery proves present availability
for the saved membership. It does not prove historical identity of image bytes
or validate image meaning. See `docs/input_recovery.md`.

## Experiment unit

Follow `docs/run_verification.md`. The Rust experiment check must exercise
resume, changed seeds, corrupted predictions, preserved old outputs, duplicate
seed rejection, partial aggregation, recorded offline failures, and changed
input manifest rejection. The report check remains available from unit 1.

Ruff and Black must pass on the changed Python implementation. Notebook JSON
and plain Python cells must parse. The pinned public notebook source must be
fetchable. Restoring the private 149 image bundle into this checkout must make
`scripts/input_manifest.py` verify 198 corpus items and 156 file states.
No data transfer or GPU execution is needed to review these conditions.

The prior direct BLIP probes used tiny local retrieval checkpoints under
Transformers 4.40.0 and 4.44.2. They checked image sensitivity and gradients.
They are engineering checks, not new benchmark results. Full pretrained BLIP,
GPU execution, and the existing Python test suite remain unverified. Workspace
instructions prohibit Python test runners.

## Data unit

Review the CSV only download path separately from image folder fetching.
The existing targeted probes checked top level selection, resumed transfers,
and failure status. Downloading the whole public collection is not a required
acceptance check.

Review export without invoking its publication option. The targeted probes
checked canonical titles and label IDs, image path containment, missing images,
and actual image decoding. A restored bundle exported all 198 canonical titles
and labels, with 149 decoded images and 49 absent images. The real
unannotated source remains unavailable, so the full real export is not claimed
as verified. Format documentation must distinguish CSV annotator output from
the JSON expected by the annotation merger.

## Paper and study unit

Every factual change must trace to the saved report or an identified primary
source. Keep the 149 item matched report separate from the 86 item seed
comparison. Keep selected checkpoint epochs separate from stopping epochs.
An interval containing zero must not be described as equivalence.

The manuscript must build without errors, overflow, or undefined references.
Inspect the rendered pages. Submission page limits remain a separate author
check. The proposed image comparison in `docs/replication_protocol.md` is not
an executed or registered study. It does not authorize compute or decide the
paper's contribution.

## What can cancel later work

A satisfactory narrower manuscript claim can remove the need for a new model
study. Missing input identity or incomplete predictions cancel an affected
comparison. A negative or inconclusive image result remains reportable.
Unresolved label meaning limits semantic claims regardless of model accuracy.
Independent Bangla review is needed for those judgments.

The user can retain the contribution on the fork while communication is
unavailable. Review branches and verified evidence are useful contributions;
upstream adoption and membership in the research group are not established by
pushing them.
