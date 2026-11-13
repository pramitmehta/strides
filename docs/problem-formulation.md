# Problem Formulation

## Running cadence estimation (Phase 0 scope)

Estimate running cadence \(c_t\) (steps per minute) from a non-uniformly sampled inertial stream \(\{(a_i, \omega_i, t_i)\}\), where \(a_i \in \mathbb{R}^3\) is linear acceleration, \(\omega_i \in \mathbb{R}^3\) angular velocity, and \(t_i\) the actual timestamp (ns).

Inputs also include hardware step-detector events where available. Fixed \(\Delta t\) is never assumed.

Processing stages (each independently testable):
1. Timestamp validation
2. Signal preprocessing (magnitude, gravity removal)
3. Filtering (causal IIR; biquad candidate)
4. Event detection (IC/TC with refractory period)
5. Temporal validation (hysteresis, plausibility)
6. Sensor fusion (accel + gyro)
7. Cadence estimation (inter-event intervals, circular buffer)
8. Confidence estimation

## Adaptive curriculum (future workstream A)
Maximize a utility over the next microcycle subject to progression, recovery, volume, strength-allocation, feasibility, and pain-safety constraints. Formulation to be finalized after research.

## Biomechanics (future workstream C)
Convert pose landmarks into temporally consistent, exercise-specific movement assessments. Kinematic, not clinical, claims only.

(Detailed formulations to be expanded as research proceeds.)
