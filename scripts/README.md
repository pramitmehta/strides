# Scripts

Helper scripts for the Stride & Strength research laboratory.

- `download_datasets.py` — downloads registered datasets into `local/datasets/` with checksum verification (reads `research/datasets/dataset-register.yaml`).
- `download_papers.py` — downloads verified paper PDFs into `local/papers/`.

These scripts are infrastructure (AI-maintained). They do NOT acquire data automatically; run them only after explicit approval of the dataset acquisition plan. Downloaded content goes to the gitignored `local/` folder.
