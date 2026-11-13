# Stride & Strength

> **An Offline-First Adaptive Training System Combining Inertial Sensor Processing, Constrained Optimization, Computer Vision-Based Kinematics and Resource-Constrained Edge Intelligence.**

Stride & Strength is an offline-first, privacy-first Android application and a pure-JVM algorithmic SDK built with Kotlin and Jetpack Compose. It helps non-runners transition into sustainable running through walk-to-run interval training, bodyweight strength training, mobility/recovery work, adaptive training schedules, sensor-based running analysis, on-device exercise-form feedback, and optional on-device AI coaching.

The system runs with **no backend, no user account, no cloud dependency, and no mandatory internet connection**. All training history stays local by default.

---

## Repository Identity

This repository is **not** merely an AI fitness application. It is an **algorithm-design and systems-engineering portfolio** where:

- **Research laboratory** (`research/`, `notebooks/`, `src/stride_lab/`) — experimentation, mathematical reasoning, and evaluation on public datasets.
- **Pure-JVM algorithmic SDK** (`algorithms/`) — production-quality algorithm implementations in Kotlin, with zero Android dependencies.
- **Android consumer** (`android/`) — real-world systems integration of the SDK.
- **Documentation** (`docs/`) — problem formulation, mathematical models, design decisions, evaluation, and limitations.

The research laboratory and the pure-JVM SDK are the primary portfolio contributions. The Android application is their reference consumer.

---

## Status

**Current phase: Phase 0 — DSP Research and Cadence Algorithm Discovery.**

Only research infrastructure and documentation are in scope right now. No Android code, Gradle configuration, Room entities, or Kotlin algorithm implementations exist yet. Algorithm implementations are developer-owned (see § "Algorithms by Human").

---

## Problem

Non-runners face a high dropout and injury risk when starting to run. Stride & Strength addresses this by combining:

1. **Walk-to-run interval training** with progressive overload.
2. **Bodyweight strength training** for injury resilience.
3. **Mobility and recovery** scheduling.
4. **Adaptive training schedules** driven by training load, RPE, and pain observations.
5. **Sensor-based running analysis** (cadence, step events) from noisy, non-periodically sampled IMU streams.
6. **Computer-vision exercise form feedback** (squats, lunges, planks, push-ups, glute bridges).
7. **Optional on-device AI coaching** (Gemma via MediaPipe) that never overrides deterministic safety rules.

---

## Research Question (Phase 0)

> How reliably can computationally efficient inertial-sensor signal-processing techniques estimate running cadence from noisy, non-periodically sampled accelerometer and gyroscope observations?

Cadence is estimated in **steps per minute (SPM)** from linear acceleration, gyroscope rotational velocity, hardware step-detector events, and actual (non-uniform) timestamps. Fixed Δt is never assumed.

---

## Datasets

Public datasets only. Raw data is kept outside version control; manifests, schemas, and checksums are committed.

| Dataset | Role | License | Status |
|---|---|---|---|
| Zenodo 16541185 — "Kinematic and Kinetic Data of Treadmill, Overground and Outdoor Running" (Baker et al., 2025) | Primary running candidate (IMU + force plates) | CC-BY 4.0 | Characterized; acquisition pending approval |
| Zenodo 7997851 — "Multivariate Time Series Data of Fatigued and Non-Fatigued Running" (Kathirgamanathan et al., 2023) | Fatigue-related signal variation | CC-BY 4.0 | Characterized; no step-event GT |
| FDA "Open-Access Wearables Dataset … Smartphone Gait Metrics" (RST24HD01.01) | Transfer validation (smartphone sensors, walking) | CC0-1.0 (repo) | Canonical URL verified |
| Zenodo 11522050 — Dorschky et al. (2019) | Foot + shank IMU + force plate/mocap GT | CC-BY 4.0 | Recommended follow-up |
| Grouvel et al. (Nature Sci Data, 2023) | Foot + shank IMU + force plate/mocap GT | CC-BY 4.0 | Recommended follow-up |

See `RESEARCH_AND_DATASETS.md` and `research/datasets/dataset-register.yaml` for provenance, channels, sampling rates, and ground-truth availability.

---

## Literature

Five papers verified against their primary sources (see `research/bibliography.bib`, `research/evidence-matrix.csv`):

1. Kiernan et al. (2023) — unsupervised gait-event identification across speeds/surfaces/foot-strike.
2. Benson et al. (2019) — automated accelerometer-based gait-event detection (multiple running conditions).
3. Mason et al. (2022/2023) — wearables for running gait analysis (systematic review).
4. Prasanth et al. (2021) — wearable sensor-based real-time gait detection (systematic review).
5. Lin et al. (2025) — gait analysis using gyroscopes and IMUs (review).

---

## Mathematical Problem Formulation (cadence)

Estimate running cadence \(c_t\) (SPM) from a non-uniformly sampled inertial stream \(\{(a_i, \omega_i, t_i)\}\):

- \(a_i \in \mathbb{R}^3\) — linear acceleration
- \(\omega_i \in \mathbb{R}^3\) — angular velocity
- \(t_i\) — actual timestamp (ns), non-uniform

Processing stages (each independently testable):

1. Timestamp validation
2. Signal preprocessing (magnitude, gravity removal)
3. Filtering (causal IIR; biquad candidate)
4. Event detection (IC/TC with refractory period)
5. Temporal validation (hysteresis, plausibility)
6. Sensor fusion (accel + gyro)
7. Cadence estimation (inter-event intervals, circular buffer)
8. Confidence estimation

Full formulation: `docs/problem-formulation.md`, `docs/mathematical-models.md`.

---

## Algorithmic Workstreams

| Workstream | Module | Status |
|---|---|---|
| A — Adaptive Curriculum Optimization | `:algorithms:curriculum` | Specified; not implemented |
| B — Running Cadence & Sensor Processing | `:algorithms:cadence` | Specified; not implemented (first developer-owned algorithm) |
| C — Biomechanics & Exercise Form | `:algorithms:biomechanics` | Specified; not implemented |
| D — On-Device AI Coach | `:algorithms:coach` + `:android:ai` | Specified; not implemented |

All algorithm implementations are **developer-owned**. AI scaffolds interfaces, domain models, tests, and infrastructure only (see § "Plumbing by AI, Algorithms by Human").

---

## Pure-JVM SDK Architecture

- Kotlin JVM modules with **zero** `android.*` imports.
- Strongly typed domain models, interfaces, and algorithm contracts.
- JUnit 5 test harnesses; property-based testing where appropriate.
- JMH benchmarking infrastructure.
- Python and Kotlin share canonical datasets and test vectors with algorithm-appropriate numerical tolerances.

---

## Android Consumer (planned)

Jetpack Compose + Material 3, MVVM/MVI, Room, DataStore, Hilt/Koin, WorkManager, CameraX, MediaPipe Pose Landmarker, Google AI Edge (Gemma, optional). Foreground service for running sessions; explicit lifecycle ownership for camera/sensor/GPU/CPU.

---

## Core Development Philosophy: "Plumbing by AI, Algorithms by Human"

- **AI** implements infrastructure: Gradle, Compose UI, Room, sensors, CameraX, WorkManager, model download/verification, logging, tests, benchmarks.
- **Developer** owns all mathematical and algorithmic implementations: DSP equations, biomechanical calculations, adaptive optimization, decision heuristics.
- AI scaffolds strongly typed Kotlin interfaces with `TODO("Algorithm implementation by developer")` stubs, KDoc contracts, complexity notes, and test specifications. AI never silently replaces a stub with a heuristic.

---

## Privacy & Offline-First

- No backend, no account, no cloud, no mandatory internet.
- All training history local by default.
- Deterministic safety rules cannot be overridden by LLM recommendations.
- Camera, sensor, GPU, CPU resources have explicit lifecycle ownership.
- All model files authenticated (SHA-256) before use.

---

## Repository Layout

```
stride-strength/
├── README.md
├── RESEARCH_AND_DATASETS.md
├── ALGORITHMS.md  BENCHMARKS.md  RESEARCH_NOTES.md
├── research/          # literature, datasets (register, manifests, schemas)
├── notebooks/         # Jupyter experiments (cadence/)
├── src/stride_lab/    # reusable Python implementations
├── algorithms/        # pure-JVM Kotlin SDK (cadence, curriculum, biomechanics, coach)
├── android/           # consumer app (app, core, data, sensors, vision, ai, features)
├── benchmarks/        # synthetic-data, baselines, configurations, results
├── testdata/          # canonical fixtures (cadence, pose-sequences, training-histories)
├── reports/           # cadence, curriculum, biomechanics
├── docs/              # system-architecture, problem-formulation, mathematical-models, ...
├── gradle/            # libs.versions.toml (Phase 1)
├── pyproject.toml     # (Phase 0/1)
└── settings.gradle.kts / build.gradle.kts  # (Phase 1)
```

---

## Evaluation Metrics (cadence)

Precision, recall, F1; cadence MAE (SPM); event timing error; false positives/min; missed steps/min; detection latency; processing time/sample; memory allocation rate. One-to-one event matching with timestamp-tolerance sensitivity. Participant-level splits (no random window splits).

---

## Safety & Limitations

- No algorithm claims to diagnose or predict injuries without clinical validation.
- Missing/low-confidence sensor data never produces definitive assessments.
- Pain reports trigger conservative schedule handling.
- All adaptive decisions explainable and auditable.
- Users can override non-safety preferences.

See `docs/safety-and-limitations.md`.

---

## Portfolio Positioning

**Stride & Strength: An Offline-First Adaptive Training System Combining Inertial Sensor Processing, Constrained Optimization, Computer Vision-Based Kinematics and Resource-Constrained Edge Intelligence.**

The intellectual contribution is the design and evaluation of algorithms operating under noisy observations, incomplete information, limited computational resources, and real-world constraints.

Proposed contributions are kept separate from implemented ones; experimental hypotheses are kept separate from measured results.

---

## License & Data

- Code: to be determined (proposed MIT/Apache-2.0 — decision pending).
- Data: public datasets only, under their own licenses (CC-BY 4.0, CC0-1.0). Raw data is not redistributed; manifests, schemas, and synthetic fixtures are committed.

---

## Current Phase

Phase 0 in progress. Next: dataset acquisition (pending approval), notebook scaffolding, canonical schema, and reproducible signal characterization. See the research proposal for the 10-point plan and open decisions.
