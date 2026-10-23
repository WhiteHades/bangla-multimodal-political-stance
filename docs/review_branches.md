# Ordered review branches

The branches below separate the completed contribution into four review units.
They form a stack. Each branch starts from the preceding branch, so its review
diff contains only the next unit. The original integrated branch remains
available. No default branch merge or upstream PR is part of this work.

The review branches use topic names at the contributor's request. Files remain
in the existing source, scripts, checks, documentation, and paper directories.

| Order | Review branch | Base | Scope |
| :--- | :--- | :--- | :--- |
| 1 | `verify-results` | `main` at `a935d11` | Summary checks, original baseline reproduction record, and recovered image input evidence |
| 2 | `fix-experiments` | `verify-results` | Run identity, resume, aggregation, scoring, BLIP, and input verification |
| 3 | `fix-data-tools` | `fix-experiments` | Download behavior, annotation formats, local export, and dataset card corrections |
| 4 | `review-manuscript` | `fix-data-tools` | Factual manuscript corrections, primary literature comparison, proposed study, and handoff |

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
The subsequent full pretrained CPU check also passed, with no missing or
mismatched checkpoint keys. Its pooled features matched the native retrieval
model exactly, and image sensitivity and gradient checks passed. See the
record and repeat procedure in `docs/run_verification.md`. These checks provide
no new benchmark result. GPU execution and the existing Python test suite
remain unverified. Workspace instructions prohibit Python test runners.

## Data unit

Review the CSV only download path separately from image folder fetching.
The existing targeted probes checked top level selection, resumed transfers,
and failure status. Downloading the whole public collection is not a required
acceptance check.

The final review reproduced a dependency compatibility failure. The old
`gdown>=5.1` requirement allowed a version that rejected the downloader's
arguments. Version 6.3 introduced the required timeout support, so the fetch
dependency now requires `gdown>=6.3`. The installed 5.1.0 distribution reproduced
the failure without network access. All three call signatures accepted the
required arguments under 6.3.0. See the
[upstream release](https://github.com/wkentaro/gdown/releases/tag/v6.3.0).

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

## Final review limits

The final review covered the 39 changed files at `67eb497` against `a935d11`,
their relevant callers, and the subsequent dependency and verification changes.
Separate automated reviews covered experiment code, data evidence, and paper
claims. Their findings were checked by the primary reviewer. No external human
review or author acceptance is claimed.

The original annotation CSV reader still assumes a valid prior output file.
A malformed existing header can raise an error, and an invalid nonempty label
can mark an item complete. This behavior predates the contribution. Reviewers
must validate an existing annotation file before using it to resume annotation.
No annotation was resumed or changed during this review.

Historical image identity, semantic pairing, annotation history, and seed
input membership remain evidence gaps. GPU training, the real unannotated
export, and submission page limits remain unchecked. A proposal with those
limits stated can be reviewed, but it cannot be described as a complete study
replication. Opening a PR requires the contributor's later explicit approval.
