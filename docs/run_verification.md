# Experiment identity and verification

The matched sweep records a resolved configuration before training. Remote
model references are resolved to immutable repository commits, and both the
model and its processor load that revision. `params.revision` applies to the
configured pretrained model. `params.vision_revision` applies to the ViT
source in the hybrid model. Supplying a full commit avoids another reference
lookup. Local model directories are hashed by file names and bytes.
With `HF_HUB_OFFLINE=1`, an unpinned source uses the cached config's snapshot
commit. An absent cache fails clearly before training. Lookup and preparation
failures are recorded per model so that one failed source does not abort the
remaining sweep.

The run identity also records input IDs, text and label hashes, image byte
hashes, frozen source groups, folds, augmentation availability and membership,
implementation hashes, and software versions. Missing augmentation files are
recorded as unavailable rather than as applied augmentation. Per fold records
identify the augmented items actually attached to training.

Each CV run has a unique directory containing `config.yaml`, `cv.json`,
`predictions.csv`, and a final `run.json` manifest. The manifest identifies the
inputs and contains checksums of the other artifacts. The sweep summary
points to that exact directory. Its summary is replaced atomically.

Resume requires matching identity and valid artifacts. An incompatible or
incomplete run is not accepted as completed, and a new run keeps the older
directory. A malformed metadata document fails visibly rather than being
silently treated as a successful experiment. These checks prevent accidental
reuse; they are not a signature or proof against deliberate alteration.

The analysis scripts load the exact referenced artifacts and check their
checksums and summary fields. Pairing requires the same examples, labels,
outer folds, and frozen groups. Across seeds, aggregation requires comparable
configurations, inputs, augmentation, implementation, and software. The seed
and its fold assignment may differ. Duplicate seed entries are rejected.
An aggregate retains the identities and artifact paths. One seed has no
sample standard deviation, which is represented as null in JSON and NA in
tables.

Older bundles without this metadata remain historical evidence. Use
`scripts/verify_reports.py` to inspect committed summary arithmetic. Do not
invent manifests for missing historical inputs or mix those records with new
verified runs.

## Freeze inputs before transfer

After preparing and reviewing the intended corpus and image availability,
create an input manifest with `python scripts/input_manifest.py --write`.
The command records current file hashes and missing file states without
overwriting an existing manifest. Keep the manifest with the private input
bundle. Check it after transfer with `python scripts/input_manifest.py`.
A changed corpus, source table, configuration, or referenced image stops
verification. A manifest preserves the chosen snapshot; it does not certify
its annotation meaning, permissions, or suitability as an evaluation set.

`notebooks/run_seeds_colab_pro.ipynb` records its pinned source checkout and
verifies the supplied local data bundle before training. It saves new runs
and their aggregate analysis under a separate Drive directory. It does not
silently substitute a public dataset snapshot.
Each model still resumes through the same identity checks. Review and freeze
the notebook's source reference and the input bundle before running a study.
The notebook's JSON and Python cells were parsed locally. Its Colab flow and
GPU training have not been executed. The older CV and seed notebooks are
marked as historical workflows.
The pinned commit was fetched from the configured public repository. A reused
checkout must be clean before installation. A local fixture confirmed that
the notebook rejects an edited checkout and accepts a clean checkout.

## Local checks

The checks below need the data and analysis dependencies already used by the
project. They use synthetic records for the experiment flow and do not load
original news content or pretrained model weights.

```sh
mkdir -p .tmp
rustc --edition=2021 checks/reports.rs -o .tmp/check_reports
.tmp/check_reports .venv/bin/python
rustc --edition=2021 checks/experiments.rs -o .tmp/check_experiments
.tmp/check_experiments .venv/bin/python
```

The experiment check covers resume, a changed seed, corrupt prediction
rejection, preservation of the old output, aggregation without paired models,
retained identity, valid JSON, duplicate seed rejection, and changed input
manifest rejection.

The BLIP wrapper was also checked with a tiny synthetic retrieval checkpoint
under Transformers 4.40.0 and 4.44.2 on CPU. Changing pixels changed its logits.
Frozen and unfrozen encoder gradients followed the configured setting. The
synthetic vision weights used an initialization scale of 0.02 to make the
check sensitive to pixels; the tiny model's default near zero scale would
make that probe uninformative. No pretrained BLIP weights were downloaded,
and these checks provide no new benchmark score.

The full existing Python test suite was not run because the workspace
instructions prohibit Python test runners. The small Rust checks and direct
runtime probes are separate evidence and do not claim that suite passed.
