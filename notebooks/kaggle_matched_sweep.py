# Kaggle kernel: run the matched sweep on a GPU.
#
# Input: a private Kaggle dataset holding bmpb-bundle.tar.gz (committed code,
# corpus.csv, the augmentation table and the image folders). Requires the GPU
# accelerator and internet access (HuggingFace checkpoints).
# Output: /kaggle/working/bmpb-matched-results.tar.gz, read back locally by
# scripts/matched_analysis.py.

import glob
import json
import os
import subprocess
import sys
import tarfile

import torch

assert torch.cuda.is_available(), "Enable the GPU accelerator for this kernel"
print(torch.cuda.get_device_name(0), flush=True)

WORK = "/kaggle/working/bmpb"
archives = glob.glob("/kaggle/input/**/bmpb-bundle.tar.gz", recursive=True)
if archives:
    os.makedirs(WORK, exist_ok=True)
    with tarfile.open(archives[0]) as archive:
        archive.extractall(WORK)
else:  # Kaggle unpacks some archives on upload
    manifests = glob.glob("/kaggle/input/**/bundle-manifest.json", recursive=True)
    assert manifests, "bundle not found under /kaggle/input"
    subprocess.run(["cp", "-r", os.path.dirname(manifests[0]), WORK], check=True)
os.chdir(WORK)
print(json.load(open("bundle-manifest.json")), flush=True)

pip = [sys.executable, "-m", "pip", "install", "-q"]
subprocess.run(pip + ["--no-deps", "-e", "."], check=True)
subprocess.run(pip + ["typer", "rich", "git+https://github.com/csebuetnlp/normalizer"], check=True)

env = {**os.environ, "PYTHONUNBUFFERED": "1", "TOKENIZERS_PARALLELISM": "false"}
subprocess.run(
    [sys.executable, "-u", "scripts/run_matched_sweep.py", "--out", "experiments/matched"],
    check=True,
    env=env,
)

subprocess.run(["cp", "bundle-manifest.json", "experiments/matched/"], check=True)
with tarfile.open("/kaggle/working/bmpb-matched-results.tar.gz", "w:gz") as out:
    out.add("experiments/matched", arcname="matched")
print("done", flush=True)
