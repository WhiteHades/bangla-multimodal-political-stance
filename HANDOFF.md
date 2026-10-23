## 23 October 2026, Codex, review preparation

Done: added report checks and run identity validation, corrected model and data
tools, and revised manuscript claims against saved evidence. Recovered image
files remain local. The evidence and repeat procedures are in
`docs/evidence_status.md`, `docs/input_recovery.md`, and `docs/run_verification.md`.
`docs/replication_protocol.md` proposes a study that has not run.

Verified: report arithmetic, four original text baselines, input hashes and
image decoding, Rust checks, and full pretrained BLIP CPU and GPU probes.
GitHub CI passed lint, formatting, Python tests, and imports on all four PRs.
The revised manuscript compiled. Historical numerical reports remain unchanged.

Open: historical image identity, original neural predictions, independent
Bangla annotation review, the proposed dataset comparison, Colab execution,
and the real unannotated export. No local Python test runner was used.
The author must decide scientific framing and whether to adopt the study.

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
