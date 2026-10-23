## 23 October 2026, Codex, final review on review-manuscript

Done: reviewed the completed contribution against `a935d11`, with separate
automated reviews of experiment code, data evidence, and paper claims. The
review found an incompatible download dependency requirement and invalid
annotation resume behavior. Both were reproduced and corrected. The fetch
extra now requires `gdown>=6.3`. Annotation resume validates the existing CSV
before dataset loading and rejects conflicting labels without changing records.
The new `checks/annotations.rs` covers valid resume and malformed inputs.

The contributor explicitly replaced the branch naming convention for this
work. The active review branches are `verify-results`, `fix-experiments`,
`fix-data-tools`, and `review-manuscript`, in that order. Files remain in the
existing repository directories. The default branch and historical reports
remain unchanged. Earlier entries retain their historical branch names.
The earlier published contribution branches are preserved as
`historical-evidence-review`, `historical-manuscript-review`,
`historical-integrated-review`, and `historical-replication-review`.
Each renamed remote branch was checked to contain the previous commits before
retiring its old name. The local working branches also use topic names.
No PR may be opened until the contributor explicitly approves that action.

Verified: the full public BLIP retrieval weights loaded on CPU with no
missing, unexpected, or mismatched keys. Wrapper features exactly matched
the native retrieval path. Changing synthetic images changed the output.
Frozen and enabled encoder gradients behaved as expected. The source
revision, weight hash, software, numerical differences, and 18.12 second
probe time are recorded in `reports/verification/pretrained_blip.json`.
This was an implementation check with no optimizer steps or benchmark scores.

Both existing Rust checks passed, as did the new annotation check. Ruff and
Black passed on 46 Python files. The old annotation reader was demonstrated
to mark label 99 as complete; the corrected reader rejects it before loading
data. The installed gdown 5.1.0 distribution reproduced the unsupported
argument error, while 6.3.0 accepted all required call signatures.
The original input manifest still verifies 198 records and 106 file states.
The recovered bundle verifies 198 records and 156 file states, including
149 images that fully decode. Historical numerical reports match `a935d11`.

Primary passages for BanglaBias, Liang, and CANDOR were rechecked, including
annotation roles, example units, controls, and reuse limits. The BanglaBias
dataset card lists MIT. The source locations and scope of targeted reading
are recorded in `docs/research_evidence.md`. The statistical review and
remaining evidence gaps are recorded in `docs/review_branches.md`.

Not verified: GPU or Colab execution, historical image byte identity, original
neural predictions, independent Bangla interpretation, original annotation
history, the real unannotated export, and submission page limits. The existing
Python test suite remains unrun because workspace instructions prohibit its
runner. These limitations are not resolved by automated review. The proposed
controlled image comparison remains unexecuted. Mantis fetched successfully
but its local checkout could not fast forward; its existing guidance was used.

Needs the author: scientific framing, annotation interpretation, and adoption
of the proposed study. Needs the contributor: a later explicit decision to
open a PR. No communication, data upload, dataset publication, or GPU work
was performed.

## 23 October 2026, Codex, replication readiness and review units

Done: recovered current public image files for all 149 saved paired identifiers
without overwriting the existing raw mirror or input manifest. The selected
snapshot has 122 processed images and 27 originals. It is stored privately in
`data/interim/replication_inputs_20261023/`. Per file retrieval records remain
in `data/interim/replication_recovery_20261023.json`. The aggregate evidence is
`reports/verification/input_recovery.json` and `docs/input_recovery.md`.

The processed image table has 149 identifiers but shares only 122 with the
saved evaluation population. All 13 paired report entries agree on the saved
149 identifiers and folds. The new files fully decode, with no exact byte or
decoded pixel duplicates. The saved headline checksum and seed 42 folds
reproduce, with 148 source groups. None of those checks proves historical
image byte identity, semantic pairing, or event independence.

Prepared the ordered review units described in `docs/review_branches.md`.
The branches are `agent/review-01-evidence`, `agent/review-02-experiments`,
`agent/review-03-data`, and `agent/review-04-paper`. Each review base is the
preceding branch; the first starts at `a935d11`. The original integrated branch
and full development history remain available. The default branch and
historical numerical reports remain unchanged.

Verified: the evidence branch passed its Rust report check, including rejection
of corrupted score and image count copies. The experiment branch passed its
Rust synthetic flow check. A clean checkout restored the new private bundle
and verified 198 records and 156 file states. The original snapshot still
verified its 198 records and 106 file states. Data export preserved all 198
canonical titles and labels with 149 decoded images. Ruff and Black passed on
46 relevant Python files, and notebook JSON and plain Python cells parsed.
No full Python test runner was used, as required by workspace instructions.

`docs/replication_protocol.md` is a proposal for the same character text features
alone, with fixed image features, and image features alone. It fixes the text
field, current input bundle, model revision, preprocessing, classifier settings,
primary seed, sensitivity folds, metrics, conditional uncertainty, decision
rules, and cancellation conditions. Independent review led to more explicit
preprocessing and analysis rules. The proposed work is 149 feature extractions
and 75 linear classifier fits. Runtime is unmeasured. No new study has run.

Not verified: historical image bytes and neural predictions, semantic image
pairing, original annotation procedures, full pretrained BLIP, GPU or Colab
execution, the real unannotated export, and submission page limits. Shared
source components do not prove independence across events or outlets. The
current data has already supported development and is not an untouched test
set. Mantis fetched successfully but its local checkout still could not fast
forward; its existing guidance was used without changing that checkout.

Needs the author: review the scientific framing and decide whether a new study
is needed. Independent Bangla review and original annotation records remain
necessary for semantic claims. A meaningful effect threshold needs a stated
reason before new predictions are inspected. No upstream PR, default branch
merge, communication, dataset publication, data upload, or GPU work occurred.

## 23 October 2026, Codex, completed contribution work

Done: integrated the review changes on `agent/review-integrated` and pushed
logical commits. The evidence and initial manuscript branches are also
available as `agent/review-evidence` and
`agent/review-manuscript-corrections`. The default branch and historical
numerical reports remain unchanged. No PR was opened or merged.

The changes identify experiment inputs, model revisions, source code,
software, groups, folds, augmentations, and exact saved artifacts. Resume and
analysis reject incompatible or damaged runs. Macro F1 uses the frozen label
set. BLIP now loads the retrieval architecture and uses image conditioned
text features. Annotation format instructions and local dataset export are
corrected. The downloader selects top level CSV files for the CSV only path.
The current Colab notebook requires a clean pinned checkout and a verified
input manifest. Older notebooks are marked as historical workflows.

Verified: five public source CSVs were recovered locally. `Dataset.csv`
matches the checksum in the committed provenance audit. The original
implementation at `a935d11` reproduced four baseline results exactly, including
folds, confusion matrices, point scores, and bootstrap intervals. Aggregate
evidence and source checksums are in
`reports/verification/original_baselines.json`. Recovered source data and raw
reproduction outputs remain ignored and local.

The report checker verified 20 matched scores, 100 seed scores, and 60 paired
comparisons. Both Rust checks passed. The experiment check uses synthetic
records and covers changed inputs, resume, corruption, preserved outputs,
aggregation, duplicate seeds, and recorded offline failures. Direct CPU probes
checked tiny BLIP retrieval checkpoints under Transformers 4.40.0 and 4.44.2,
including image sensitivity and frozen encoder gradients. Export probes
checked headlines, labels, missing images, and truncated image rejection.
Downloader probes checked CSV selection, resume, and failure status.

Ruff and Black passed on 46 relevant Python files. Notebook JSON and plain
Python cells parsed. The pinned notebook commit was fetched from its public
source. A direct fixture checked dirty and clean checkout handling. Independent
reviews found an offline revision issue and a dirty notebook checkout issue;
both were reproduced and corrected. The final Tectonic build produced nine
pages with no overflow or undefined references. Rendered pages were inspected.
Underfull boxes and local font configuration warnings remain. Submission page
limits were not checked.

`docs/research_evidence.md` records targeted primary reading, six academic
queries, 36 results representing 30 unique papers, and task differences that
exclude automatic dataset merging. Further study proposals are conditional
on the named evidence gaps. They are not completed experiments.

Not verified: GPU or Colab execution, full pretrained BLIP weights, the full
existing Python test suite, complete local image recovery, and the real
unannotated export source. Workspace rules prohibit Python test runners.
The seed summary's original input identity and historical neural training
remain unverified. Automated checks do not establish annotation meaning.
The Mantis checkout refresh could not fast forward because its branches have
diverged; the consulted guidance matched the fetched version.

Needs the author: accept or revise scientific framing and the manuscript
changes. Confirm annotation targets, dates, and adjudication history before
new semantic claims. Independent Bangla review and any new controlled image
study remain separate future work. Corrected scoring or BLIP experiments need
new identified results. No dataset publication, data upload, paid compute,
or communication with the research group was performed.

## 23 October 2026, Codex, verified implementation changes

Done: prepared run identity, exact artifact loading, compatible aggregation,
consistent scoring, BLIP checkpoint and feature corrections, and annotation
and export contract corrections on review branches. `docs/run_verification.md`
describes the new metadata and checks. No historical report was overwritten.

Verified: Rust checks exercise report arithmetic and a synthetic experiment
flow, including resume, changed seed, artifact corruption, preserved old
outputs, aggregate JSON, duplicate seeds, and per model offline failures.
Direct CPU probes check BLIP under Transformers 4.40.0 and 4.44.2 with a tiny
local retrieval checkpoint. Image changes affect logits, and frozen settings
control encoder gradients. Model revisions resolve online or through cached
offline config snapshots. Ruff and Black checks pass on affected code.

Not verified: full pretrained BLIP weights, GPU training, and the full existing
Python test suite. Workspace instructions prohibit Python test runners.
Synthetic probes are not benchmark results. New scoring and BLIP behavior
require separately identified future runs rather than replacement of old scores.

Needs the author: scientific framing, annotation target and history, and any
decision to include further experiments. No default branch merge, dataset
publication, or message to the research group was performed.

## 23 October 2026, Codex, factual manuscript corrections

Done: separated the 149 item matched report from the 86 item seed comparison
in `paper/latex/acl_latex.tex`. Corrected the seed table columns, the selected
checkpoint description, and claims about intervals and image contribution.
Updated README and manuscript guides to distinguish historical snapshots.
Original numerical reports and historical tables are preserved.

Verified: arithmetic through `scripts/verify_reports.py`. The manuscript
builds with Tectonic 0.17.0. Its seed table was adjusted to fit the column.

Not verified: historical training or seed input identity. BLIP's old feature
path selects a separate text output; a corrected implementation needs new
results and must not replace the old score without an identified run.

Needs the author: final scientific framing. The changes describe the surviving
evidence and do not establish new annotation ground truth or image benefit.

## 23 October 2026, Codex, evidence verification

Done: added `scripts/verify_reports.py`, `checks/reports.rs`, and
`docs/evidence_status.md`. Historical reports are preserved. The older entry
below predates the committed seed reports and is retained as history.

Verified: summary arithmetic for 20 matched scores, 100 seed scores, and 60
seed comparisons. The seed comparisons report 86 items and 85 source groups,
whereas the matched report has a separate 149 item paired population.

Not verified: original training, raw predictions, annotation semantics, and
the relationship between the seed inputs and the matched inputs. A summary
check does not establish those facts. No dataset was uploaded or published.

Needs the author: interpretation of the contribution and any change to the
study target. Engineering changes are prepared on review branches.

## 2026-10-12 · Claude (Opus 5.5, Claude Code) · agent/experiments-grouped-evaluation (seeds)

Done: the author asked for a multi-seed rerun on Colab. Added `--seed` to
`scripts/run_matched_sweep.py`, `notebooks/run_seeds_colab.ipynb` (seeds 43–46,
resumable to Google Drive) and `scripts/seed_analysis.py`. The aggregation was
fixed before any extra seed ran: per-model mean/SD/range of macro-F1, and
per-pair paired differences with counts of seeds whose interval is above or
below zero. The bundle is at `experiments/colab/bmpb-bundle.tar.gz` (local,
gitignored, built at bfe2dd3, article bodies stripped).

Verified: the seed override and the analysis were smoke-tested locally on the
sklearn baselines (seed 43 TF-IDF paired macro-F1 0.506 vs 0.543 at seed 42).

Not verified / open: no extra seed has run on a GPU yet. CountVec+ViT fails
locally only because torchvision is missing here; Colab has it.

Needs the author: run the notebook and return `bmpb-seeds.tar.gz`; then unpack
it into `experiments/seeds/` and run
`cd scripts && python seed_analysis.py ../experiments/matched ../experiments/seeds/seed-*`.

## 2026-10-12 · Claude (Opus 5.5, Claude Code) · agent/experiments-grouped-evaluation

Done: ran the corrected matched sweep on a Kaggle T4 (private kernel
`bmpb-matched-sweep`) at commit 1feab08: 13 configs on the 149 readable-image
headline items, 7 text configs on all 198 headlines, all from committed configs,
seed 42, no tuning. Added `scripts/run_matched_sweep.py`,
`scripts/matched_analysis.py` (paired comparisons fixed before results: each VL
model vs TF-IDF and vs BanglaBERT, source-group bootstrap, 2,000 resamples),
`scripts/summarize_training_log.py`, `notebooks/kaggle_matched_sweep.py`.
Outputs: `reports/submission/matched.{json,md}`, `matched_tables.tex` (copied
to `paper/latex/` and `\input`), `early_stopping.json`. Raw runs and the Kaggle
log are in `experiments/matched/` (gitignored). Rewrote the abstract, the
contributions, the protocol, Results, Discussion, Conclusion and Limitations
around the matched results; moved historical tables to Appendix A. Added
verified citations for BERT, XLM-R, mT5, ELECTRA, CLIP, ALIGN, ViLT, BLIP,
FLAVA, ViT; fixed the missing 7th author (Xuelong Li) on `li2025survey`.

Result (null for multimodality): TF-IDF 0.543 (0.457–0.619, n=149) is best;
best VL is CountVec+ViT 0.425; every VL model is below TF-IDF in paired tests
(Δ −0.117 to −0.218, CIs exclude 0) and indistinguishable from BanglaBERT
(Δ −0.042 to +0.058, CIs include 0). Corrected BanglaBERT is 0.366 on 198 items
vs 0.533 historically.

Verified: all 20 runs status ok, every item predicted once (runner asserts).
Kaggle bundle reproduced committed sklearn baselines exactly before upload.
34 tests pass. PDF compiles with no errors, overfull boxes or undefined
references; main text ends on page 6; all 8 pages inspected. The four
pre-existing citations were checked against Crossref; new ones were taken from
the ACL Anthology `.bib` export and arxiv.org/bibtex, with titles checked.

Not verified / open: single seed and single fold assignment; inner-validation
sets are 25–33 items and 65/75 neural fold runs early-stopped (29 at epoch 1–2),
so the encoders may be under-trained. The paired comparisons confound image use
with text representation. The arXiv-only citations may have published venue
versions (CLIP/ALIGN/ViLT ICML 2021, BLIP ICML 2022, FLAVA CVPR 2022, ViT and
ELECTRA ICLR); DBLP was unreachable, so those were not swapped in. The
upload bundle had article bodies stripped. Data was uploaded as a private Kaggle
dataset `kishormorol/bmpb-matched-bundle`, deleted after download (see below);
the private kernel's output still contains the working copy of the bundle.
`reports/submission/audit.json` was untracked before this session; left as is.

Needs the author: whether the paper's claims and title should now centre the
null multimodal result; whether to add multi-seed or larger-validation reruns
(a design change, your call); annotation procedures and dataset contribution as
before; whether to delete the Kaggle kernel too.

Suggested: `Ledger: done experiments` (if you accept single-seed matched runs as
the experiment of record).

## 2026-10-10 · Codex · agent/experiments-grouped-evaluation

Done: repaired shared source grouping and independent neural validation in
`src/bmpb/crossval.py` and `src/bmpb/data/`; recorded the verified Image_29 URL
correction without changing labels. Added provenance audit and headline baseline
scripts, aggregate outputs under `reports/submission/`, and a frozen-population
BanglaBERT notebook. Revised the manuscript to distinguish corrected headline
baselines from historical exploratory neural results.

Verified: 34 tests pass; source-URL regression tests failed before the repair.
Headline TF-IDF pooled macro-F1 is 0.496 on 198 items and 0.543 on 149 readable-image
items; intervals and fold variation are in the saved outputs. The six-page PDF
compiled without overflow or undefined citations and every page was inspected.

Not verified / open: corrected neural and multimodal training has not run.
Image_154/Image_155 remain conservatively grouped pending source-link verification.
Collection and annotation records for additional items remain incomplete.
Dataset and portable input bundles are local and are not committed.

Needs the author: run the frozen BanglaBERT experiment on a CUDA GPU; confirm
annotation procedures and dataset contribution before finalizing claims.
