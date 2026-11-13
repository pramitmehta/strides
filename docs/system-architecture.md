# System Architecture

Stride & Strength follows a modular Clean Architecture with strict separation between the pure-JVM algorithmic SDK and the Android consumer.

## Layers
- **Research laboratory** (`research/`, `notebooks/`, `src/stride_lab/`) — experimentation and mathematical reasoning.
- **Pure-JVM SDK** (`algorithms/`) — Kotlin JVM modules, zero Android imports.
- **Android consumer** (`android/`) — Jetpack Compose, Room, sensors, vision, AI.

## Principles
- Offline-first, zero-backend, privacy by default.
- Deterministic safety behaviour.
- Graceful degradation on low-end devices.
- Explicit resource/lifecycle ownership.
- Reproducible experiments; shared datasets/test vectors Python ↔ Kotlin.

(Detailed architecture to be expanded as phases proceed.)
