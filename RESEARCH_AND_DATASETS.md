# Research and Datasets — Stride & Strength

This document records the data strategy, provenance, and licensing for the Stride & Strength research laboratory. Raw datasets are **never** committed. Only manifests, schemas, checksums, acquisition instructions, and permitted synthetic fixtures are committed.

## Data Policy

1. Preserve original data unchanged.
2. Separate raw, processed, and synthetic data.
3. Track licenses and checksums for every dataset.
4. Version processed datasets and transformations.
5. Never fabricate benchmark results.
6. Clearly label hypotheses and preliminary findings.
7. Make notebooks reproducible.

## Directory Layout

```
research/datasets/
├── dataset-register.yaml   # canonical registry (committed)
├── manifests/              # per-dataset checksums & file lists (committed)
├── schemas/                # JSON schemas for imu_sample and step_event (committed)
└── README.md
research/datasets/raw/       # gitignored — downloaded archives
research/datasets/processed/ # gitignored — derived datasets
```

## Candidate Datasets

### Dataset A — Zenodo 16541185 (PRIMARY)
- **Title:** Kinematic and Kinetic Data of Treadmill, Overground and Outdoor Running
- **DOI:** 10.5281/zenodo.16541185 | **Version:** 0.1 | **Published:** 2025-07-28
- **License:** CC-BY 4.0
- **Source:** https://zenodo.org/records/16541185
- **Paper:** Baker LM et al. (2025) "Estimating braking and propulsion forces during overground running in and out of the lab." PLOS ONE 20(9): e0330042. https://doi.org/10.1371/journal.pone.0330042
- **Participants:** 15 recreational runners
- **Sensors:** IMU at pelvis, thigh, shank, foot (tri-axial accel + gyro; sagittal angle for thigh/shank/foot)
- **Sampling rate:** Not stated in record — verify in paper / derive from `delta_time`
- **Ground truth:** 3D GRF (ap/ml/vertical) from force plates in `TM_FP` and `OG_FP` settings. No explicit IC/TC annotation files; step events derivable via GRF threshold (proposed 10 N).
- **Archive:** `running_treadmill_overground_outside.zip`, 312.1 MB, md5 `d0ede3df73a04279e31e98a699bde86d`
- **Suitability:** Primary candidate for cadence/step-event validation.

### Dataset B — Zenodo 7997851 (FATIGUE)
- **Title:** Multivariate Time Series Data of Fatigued and Non-Fatigued Running from Inertial Measurement Units
- **DOI:** 10.5281/zenodo.7997851 | **Version:** 0.0 | **Published:** 2023-06-02
- **License:** CC-BY 4.0
- **Source:** https://zenodo.org/records/7997851
- **Papers:** Kathirgamanathan B et al. (2023) IEEE BSN, doi 10.1109/BSN58485.2023.10331612; XKDD 2023 workshop paper
- **Participants:** 19 recreational runners
- **Sensor:** Single Shimmer3 IMU on lumbar; 256 Hz; accel (3-axis), gyro (3-axis), magnetometer; derived magnitudes
- **Ground truth:** None for step events. Labels are fatigue state per segmented stride ('F'/'NF').
- **Suitability:** Fatigue-related signal variation and robustness only. **Do not** use fatigue labels as a proxy for step-event ground truth.

### Dataset C — FDA Open-Access Wearables (TRANSFER VALIDATION)
- **Title:** Open-Access Wearables Dataset to Evaluate Factors Impacting Accuracy of Smartphone Gait Metrics
- **RST Reference:** RST24HD01.01 | **Published:** 04/18/2024
- **Canonical URL:** https://cdrh-rst.fda.gov/open-access-wearables-dataset-evaluate-factors-impacting-accuracy-smartphone-gait-metrics
- **License:** CC0-1.0 (GitHub repo); full-dataset license on Synapse unverified
- **Download:** Synapse syn51664250 (data access wiki 623161; protocol wiki 622541); GitHub sample data (dbp-osel)
- **Participants:** 20 healthy; smartphone IMU (iPhone 10, Galaxy S22) + reference IMU (Xsens MTw) + walkway (Protokinetics Zeno)
- **Sampling rate:** 100 Hz
- **Ground truth:** Walkway binary left/right foot contact
- **Suitability:** Smartphone sensor characteristics, orientation/placement effects. **Walking only — not running ground truth.**

### Recommended Follow-ups
- **Zenodo 11522050 (Dorschky et al., 2019)** — foot + shank IMU + OMC + force plate; running at 3 speeds; CC-BY 4.0; 11.8 GB.
- **Grouvel et al. (Nature Sci Data, 2023)** — 8 IMUs (feet, shanks, thighs, pelvis, trunk) + 3 force plates + mocap; 2 running trials/subject; CC-BY 4.0.

### Rejected
- Gait3D (vision-based, no IMU/GT); PhysioNet multimodal gait (walking only); Zenodo 7997851 (no step-event GT); FDA dataset (walking only).

## Acquisition Checklist (per dataset)
1. Inspect metadata before downloading.
2. Verify license.
3. Record source URL, version, publication date.
4. Record archive checksums.
5. Inspect file formats.
6. Identify sensor channels and units.
7. Determine sampling frequency.
8. Establish event-label availability.
9. Document synchronization limitations.
10. Record any preprocessing performed.
