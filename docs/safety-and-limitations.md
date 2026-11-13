# Safety and Limitations

- Hard safety constraints are deterministic; LLM recommendations cannot override them.
- Missing or low-confidence sensor data never produces definitive assessments.
- Pain reports trigger conservative schedule handling.
- No algorithm claims to diagnose or predict injuries without clinical validation.
- Adaptive decisions are explainable and auditable.
- Users can override non-safety preferences.
- All training history remains local by default.
- Model files are authenticated (SHA-256) before use.
- Camera, sensor, GPU, and CPU resources have explicit lifecycle ownership.

Known limitations will be recorded here as research and implementation proceed.
