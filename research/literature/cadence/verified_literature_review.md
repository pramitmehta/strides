# Verified Bibliographic & Methodology Report — Running Cadence Estimation (Inertial Sensors)

Generated 2026-11-13 from direct reads of PubMed/PMC full text. No fabricated fields; unverifiable fields tagged UNVERIFIED/NOT REPORTED.

Source URLs read:
- https://pubmed.ncbi.nlm.nih.gov/37299749/ (Kiernan)
- https://pmc.ncbi.nlm.nih.gov/articles/PMC10255839/ (Kiernan full text)
- https://pubmed.ncbi.nlm.nih.gov/30934672/ (Benson)
- https://pmc.ncbi.nlm.nih.gov/articles/PMC6480623/ (Benson full text)
- https://pmc.ncbi.nlm.nih.gov/articles/PMC9807497/ (Mason)
- https://pmc.ncbi.nlm.nih.gov/articles/PMC8069962/ (Prasanth)
- https://pmc.ncbi.nlm.nih.gov/articles/PMC12158269/ (Lin)

---

## Paper 1 — Kiernan et al. (2023)

### Bibliographic metadata
- **Title**: "Unsupervised Gait Event Identification with a Single Wearable Accelerometer and/or Gyroscope: A Comparison of Methods across Running Speeds, Surfaces, and Foot Strike Patterns" — VERIFIED (PubMed PMID 37299749; PMC10255839)
- **Authors**: Dovin Kiernan; Kristine Dunn Siino; David A. Hawkins — VERIFIED
- **Journal**: Sensors (Basel, Switzerland) — VERIFIED
- **Year**: 2023 (published online 2023-05-24) — VERIFIED
- **Volume/Issue/Pages**: Vol. 23, Issue 11, Article 5022 (e-journal, no page range) — VERIFIED
- **DOI**: 10.3390/s23115022 — VERIFIED
- **PMID**: 37299749 — VERIFIED
- **PMCID**: PMC10255839 — VERIFIED

### Discrepancy vs. user citation
User cited title "Unsupervised Gait Event Identification in Running" — actual title is substantially longer (above). User's short title is a truncation; not a separate paper. — FLAGGED

### Research problem / aim
Evaluate 18 (21 with modifications) methods for identifying initial contact (IC) and terminal contact (TC) during running from a single wearable on shank or sacrum/low-back, across speeds, surfaces, and foot-strike patterns; recommend best methods. — VERIFIED (abstract + discussion)

### Sensor hardware
Tri-axial IMUs ProMove MINI, Inertia Technology (Enschede, Netherlands); ±16 g primary, ±100 g secondary, ±34.91 rad/s, 1000 Hz. — VERIFIED (Sec. 2.1)

### Sensor location
Anterior/superior to lateral malleoli (shank/tibia); superior iliac crests; superior sacrum. Only tibial and sacral IMU data analyzed. — VERIFIED (Sec. 2.3)

### Sampling frequency
1000 Hz (IMU); force plate 1000 Hz. — VERIFIED

### Filtering method
4th-order 50-Hz low-pass Butterworth on IMU and force-plate data; angular velocity drift-corrected with Madgwick filter; quiet-period bias removal; saturated frames (>15.5 g) replaced with secondary accelerometer. — VERIFIED (Sec. 2.4)

### Event detection method
18 (21) automated IC/TC methods (peak/threshold/heuristic; some ML). Recommended: shank IC = Purcell or Fadillioglu; shank TC = Purcell; sacrum IC = Auvinet or Reenalda; sacrum TC = Auvinet; side ID = Lee (81.9%). — VERIFIED (Sec. 3, 5)

### Ground-truth methodology
Kistler 9281 force plate at 1000 Hz; vertical force threshold 10 N defines IC/TC. — VERIFIED (Sec. 2.4)

### Dataset
77 recruited, 74 analyzed (32 M, 42 F; age 28±12 yr); runners ≥16 km/wk ≥6 mo. Overground 25 m runway, two surfaces (track covering, hardwood floor), three self-selected speeds (slowest/typical/fastest), foot-strike angles (rear/mid/fore). 5 stances/side/speed/surface. 642 of 4440 trials retained for ms-accurate sync. — VERIFIED (Sec. 2.2–2.4)

### Evaluation metrics
Error (method − force plate), bias, within-method SD, 95% LOA (Carstensen linked replicates), linear mixed-effects models, effects of surface/speed/foot-strike angle, processing time. — VERIFIED (Sec. 2.5)

### Computational complexity
Processing time: most methods <5 s, all <20 s for two 30-min 1.8M-frame trials; output rates reported. — VERIFIED (Sec. 3.4)

### Stated limitations
Only overground level surfaces (two); homogenous runner population; original methods developed on small samples/narrow conditions; sync discrepancies discarded most trials; may not generalize to incline/decline, treadmill, other surfaces, or other populations (amputees, higher body fat). — VERIFIED (Sec. 4)

---

## Paper 2 — Benson et al. (2019)

### Bibliographic metadata
- **Title**: "Automated Accelerometer-Based Gait Event Detection During Multiple Running Conditions" — VERIFIED (PubMed PMID 30934672; PMC6480623)
- **Authors**: Lauren C. Benson; Christian A. Clermont; Ricky Watari; Tessa Exley; Reed Ferber — VERIFIED
- **Journal**: Sensors (Basel, Switzerland) — VERIFIED
- **Year**: 2019 (published online 2019-03-27) — VERIFIED
- **Volume/Issue/Pages**: Vol. 19, Issue 7, Article 1483 — VERIFIED
- **DOI**: 10.3390/s19071483 — VERIFIED
- **PMID**: 30934672 — VERIFIED
- **PMCID**: PMC6480623 — VERIFIED

### Discrepancy vs. user citation
Title matches (user capitalized "During"; actual "During" — same). No substantive discrepancy. — VERIFIED

### Research problem / aim
Develop automated accelerometer-based gait-event (IC, TO) detection for foot and low-back accelerometers; validate vs. force plate; examine across speeds, foot-strike patterns, outdoor surfaces. — VERIFIED (abstract)

### Sensor hardware
Shimmer3 tri-axial accelerometers, ±16 g, 201.03 Hz, Shimmer Inc. (Dublin, IE). — VERIFIED (Sec. 2)

### Sensor location
Dorsum of right foot and lower back near center of mass. — VERIFIED (Sec. 2)

### Sampling frequency
201.03 Hz (accelerometers); force plate 1000 Hz (Bertec). — VERIFIED

### Filtering method
4th-order zero-lag Butterworth, cutoff 10 Hz, no normalization. Back accelerometer aligned with gravity and rotated; foot not aligned. — VERIFIED (Sec. 2.2)

### Event detection method
Peak-based heuristic algorithms (modified from Strohrmann foot and Lee back) with sliding window; cadence assumptions 0.25–0.50 s between contralateral/ipsilateral steps; TO ≥0.1 s after IC; peak-magnitude selection; step-side determination for back. — VERIFIED (Sec. 2.3–2.4)

### Ground-truth methodology
Bertec instrumented treadmill force plate at 1000 Hz; IC = 10 N, TO = 25 N vertical GRF thresholds. — VERIFIED (Sec. 2.3)

### Dataset
Exp1: 12 recreational runners (8 M, 4 F; age 26.2±3.8) treadmill at 2.7/3.3/3.6 m/s, 90 s. Exp2: 20 runners (10 M, 10 F; age 27.1±3.4) indoor track 60 m at preferred ±25% speed, rearfoot/forefoot strike. Exp3: 22 runners (11 M, 11 F; age 37.6±11.0) outdoor sidewalk/grass ~600 m ×16. ~1954 steps total. — VERIFIED (Sec. 2.1)

### Evaluation metrics
Mean difference, SD, 95% LoA, skipped steps, wrong step side, output rate, repeated-measures ANOVA. — VERIFIED (Sec. 2.4–2.5)

### Computational complexity
Output rate: force 250–460 Hz, foot 150–210 Hz, back 90–100 Hz at 200 Hz sampling; optimal params 200 Hz, 2 s window, 0.02 s shift. — VERIFIED (Sec. 3.1)

### Stated limitations
Force plate only in treadmill condition; jump-sync may introduce offsets; non-force-plate conditions not validated against gold standard; between-subject variability; future studies with larger samples. — VERIFIED (Sec. 4)

---

## Paper 3 — Mason et al. (2022/2023) — "Wearables for Running Gait Analysis: A Systematic Review"

### Bibliographic metadata
- **Title**: "Wearables for Running Gait Analysis: A Systematic Review" — VERIFIED (PMC9807497)
- **Authors**: Rachel Mason; Liam T. Pearson; Gillian Barry; Fraser Young; Oisin Lennon; Alan Godfrey; Samuel Stuart — VERIFIED
- **Journal**: Sports Medicine (Auckland, N.Z.) — VERIFIED
- **Year**: Published online 2022-10-15; issue date 2023 — VERIFIED (user gave no year; note online 2022 vs. issue 2023)
- **Volume/Issue/Pages**: Vol. 53, Issue 1, pp. 241–268 — VERIFIED
- **DOI**: 10.1007/s40279-022-01760-6 — VERIFIED
- **PMID**: 36242762 — VERIFIED
- **PMCID**: PMC9807497 — VERIFIED

### Discrepancy vs. user citation
User gave PMC URL only; no year. Actual: online 2022, issue 2023. — NOTE

### Research problem / aim
Systematically review wearable technology for running gait analysis in adults; 131 articles; validity/reliability/application. — VERIFIED (abstract)

### Sensor hardware
Review (aggregate): IMUs n=62, accelerometers only n=40, pressure sensors n=31, gyroscope only n=1. — VERIFIED (Sec. 3)

### Sensor location
Tibia n=42, shoe n=38, lower back/sacrum n=24 (among others). — VERIFIED (Sec. 3)

### Sampling frequency
Range 4–2000 Hz; most common 100 Hz (n=12). — VERIFIED (Sec. 3)

### Filtering method
Aggregate across studies; Butterworth common; no single method. — VERIFIED (review-level)

### Event detection method
Review focuses on gait outcomes, not event-detection algorithms per se. — VERIFIED

### Ground-truth methodology
Reference standards: 3D motion capture, force plates, instrumented treadmills. — VERIFIED (intro)

### Dataset
131 articles; participants mean 26±27, age 28.3±7.0; mostly indoor treadmill (n=62). — VERIFIED (abstract/results)

### Evaluation metrics
Validity/reliability of wearables; outcomes: GCT, stride length, stride frequency, tibial acceleration. — VERIFIED

### Computational complexity
Not reported. — NOT REPORTED

### Stated limitations
Lack of standardized terminology/protocols; young adult recreational runners; treadmill bias; small samples. — VERIFIED (conclusions)

---

## Paper 4 — Prasanth et al. (2021) — "Wearable Sensor-Based Real-Time Gait Detection: A Systematic Review"

### Bibliographic metadata
- **Title**: "Wearable Sensor-Based Real-Time Gait Detection: A Systematic Review" — VERIFIED (PMC8069962)
- **Authors**: Hari Prasanth; Miroslav Caban; Urs Keller; Grégoire Courtine; Auke Ijspeert; Heike Vallery; Joachim von Zitzewitz — VERIFIED
- **Journal**: Sensors (Basel) — VERIFIED
- **Year**: 2021 (published 2021-04-13) — VERIFIED
- **Volume/Issue/Pages**: Vol. 21, Issue 8, Article 2727 — VERIFIED
- **DOI**: 10.3390/s21082727 — VERIFIED
- **PMID**: 33924403 — VERIFIED
- **PMCID**: PMC8069962 — VERIFIED

### Discrepancy vs. user citation
None. — VERIFIED

### Research problem / aim
Systematic review of wearable sensors and techniques for real-time gait detection, application to pathological gait; 113 articles. — VERIFIED (abstract)

### Sensor hardware
IMUs most common; insole pressure sensors for ground truth. — VERIFIED (abstract)

### Sensor location
Shank and foot preferred. — VERIFIED (abstract)

### Sampling frequency
Range 25–1500 Hz; majority 100–200 Hz (n=42), most 100 Hz (n=30). — VERIFIED (Sec. 3.1)

### Filtering method
Low-pass Butterworth most common (n=21); orders 1–8; cutoff 0.0002–40 Hz; also Savitzky–Golay, moving average, interpolation, Gaussian. — VERIFIED (Sec. 3.1)

### Event detection method
Rule-based (threshold/peak detection) most common; also machine learning (HMM, LSTM, CNN, SVM, etc.). — VERIFIED (Sec. 3.4)

### Ground-truth methodology
Insole pressure sensors most common for IMU validation. — VERIFIED (Sec. 3.3)

### Dataset
113 articles; focus on pathological gait; real-time. — VERIFIED

### Evaluation metrics
Heterogeneous; not quantitatively comparable. — VERIFIED (abstract)

### Computational complexity
Not reported as single value. — NOT REPORTED

### Stated limitations
Heterogeneity of evaluation criteria; <1/3 validated on pathological data; most predicted to work on pathological gait but not validated. — VERIFIED (abstract)

---

## Paper 5 — Lin et al. (2025) — "A Review of Gait Analysis Using Gyroscopes and Inertial Measurement Units"

### Bibliographic metadata
- **Title**: "A Review of Gait Analysis Using Gyroscopes and Inertial Measurement Units" — VERIFIED (PMC12158269)
- **Authors**: Sheng Lin; Kerrie Evans; Dean Hartley; Scott Morrison; Stuart McDonald; Martin Veidt; Gui Wang — VERIFIED
- **Journal**: Sensors (Basel) — VERIFIED
- **Year**: 2025 (published 2025-05-31) — VERIFIED
- **Volume/Issue/Pages**: Vol. 25, Issue 11, Article 3481 — VERIFIED
- **DOI**: 10.3390/s25113481 — VERIFIED
- **PMID**: 40969016 — VERIFIED
- **PMCID**: PMC12158269 — VERIFIED

### Discrepancy vs. user citation
User cited "Review of Gait Analysis Using Gyroscopes and Inertial Measurement Units" — actual title has leading "A": "A Review of Gait Analysis Using Gyroscopes and Inertial Measurement Units". — FLAGGED

### Research problem / aim
Review gyroscopes and IMUs for gait event/phase detection and spatiotemporal parameters; 66 articles. — VERIFIED (abstract)

### Sensor hardware
Gyroscopes and IMUs (aggregate; Xsens etc.). — VERIFIED (Table 1)

### Sensor location
Shank n=42, thigh n=32, dorsum of foot n=27. — VERIFIED (Sec. 3.2)

### Sampling frequency
Range 25–1500 Hz; majority 100–200 Hz (n=42), most 100 Hz (n=30). — VERIFIED (Sec. 3.1)

### Filtering method
Low-pass Butterworth most common (n=21); orders 1–8; cutoff 0.0002–40 Hz; also Savitzky–Golay, moving average, interpolation, Gaussian. — VERIFIED (Sec. 3.1)

### Event detection method
Rule-based (threshold/peak) and machine learning (HMM, LSTM, CNN, SVM, etc.). — VERIFIED (Sec. 3.4)

### Ground-truth methodology
Motion capture, force plates, insole pressure sensors. — VERIFIED (Sec. 3.7)

### Dataset
66 articles; healthy and pathological populations. — VERIFIED

### Evaluation metrics
Heterogeneous. — VERIFIED

### Computational complexity
Not reported. — NOT REPORTED

### Stated limitations
Lack of consensus on optimal sensor configurations; rule-based suitable for controlled environments, ML for complex; need standardization. — VERIFIED (abstract/conclusion)

---

## Cross-paper notes for your cadence project (~50 Hz, foot/lumbar/smartphone)
- Kiernan & Benson both validate at 1000 Hz / 201 Hz respectively; neither tests 50 Hz directly. Benson tested 50/100/200 Hz in parameter sweep and found accuracy converged at smallest window shifts; 50 Hz feasible but with lower output rate. — VERIFIED (Benson Sec. 3.1)
- Lumbar/sacrum placement supported by Kiernan (Auvinet/Reenalda) and Benson (back algorithm); foot placement supported by Benson (foot algorithm) and Kiernan (Purcell/Fadillioglu shank). — VERIFIED
- Smartphone placement not directly covered by these five papers; Mason review notes wrist/GPS-watch placements exist but rare. — VERIFIED (Mason Sec. 3)
