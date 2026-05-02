# Architecture Decision Record - Thunderstorm Forecasting

This document records all major technical decisions made during model development, preprocessing, and deployment.

---

## ADR-001: Target Design - Next-Day Forecasting via Temporal Shift

### Context

The objective is to predict whether a thunderstorm occurs on the next day using atmospheric indices measured on the current day.

### Decision

Shift the target variable `TH` by -1 (shift(-1)) to align day *T* features with day *T+1* outcome.

### Rationale

- Enables true next-day forecasting instead of same day classification.
- Preserves temporal causality between atmospheric conditions and storm occurrence.

### Trade-offs Accepted

- Last row has no label after shifting; inserted the mode value into that row.

---

## ADR-002: Data Filtering Strategy - No GMT Restriction

### Context

Initial dataset contained multiple daily observations across different GMT timestamps.

### Decision

Do not filter to GMT == 0 (data loss ~83%).

### Rationale

- GMT filtering (GMT == 12) removed ~17% of valid samples.
- No predictive gain observed from restricting time window.

---

## ADR-003: Missing Data Strategy - No Imputation

### Context

~17% of calendar days are missing due to observational gaps.

### Decision

Do not perform imputation for missing dates.

### Rationale

- Missingness reflects real-world weather station outages.
- Imputation would introduce artificial atmospheric patterns.

---

## ADR-004: Feature Engineering - Composite Atmospheric Indices

### Context

Replace raw meteorological variables with engineered composite features.

### Decision

| Feature | Formula | Reason |
| ------- | ------- | ------- |
| Environmental Stability | Showalter + Lifted Index | Combined instability signal |
| Moisture Indices | Precipitable Water | Direct moisture representation |
| Convective Potential | CAPE + CINE | Net convective energy |
| Temperature Pressure | 1000–500 Thickness | Thermal structure proxy |
| Moisture Temp Profiles | PLCL | Low-level moisture structure |

### Rationale

- Reduces multicollinearity.
- Improves interpretability of physical atmospheric states.

---

## ADR-005: Class Imbalance Strategy - SMOTETomek

### Context

Storm occurrences are minority class events.

### Decision

Use SMOTETomek for resampling.

| Method | Performance (Recall) |
| ---- | ---- |
| SMOTE | Moderate |
| BorderlineSMOTE | Slight improvement |
| **SMOTETomek (chosen)** | **Best overall recall** |


### Rationale

- Improves decision boundary separation for QDA and Gaussian NB.

---

## ADR-006: Feature Scaling - StandardScaler

### Decision

Use StandardScaler for all numerical features.

### Rationale

- Consistent performance across Gaussian NB, QDA, and SVC.
- RobustScaler: no meaningful improvement in recall.

---

## ADR-007: Train-Test Split - Time-Based Split

### Decision

Use chronological 80/20 split instead of stratified sampling.

### Rationale

- Preserves real-world forecasting scenario.

### Trade-offs Accepted

- Slightly lower training randomness.
- More realistic evaluation performance.

---

## ADR-008: Transform Strategy - Log Family Functions

### Decision

- Apply:
    - log1p
    - reflect + log1p
    - shift + log1p

### Rationale

- Handles skewed meteorological distributions.
- Preserves zero/negative stability in atmospheric indices.

---

## ADR-009: Model Selection - Quadratic Discriminant Analysis (QDA)

### Context

Multiple probabilistic and linear models evaluated.

### Decision

- Use Quadratic Discriminant Analysis as final production model.
- PipeLine:
    - SMOTETomek
    - StandardScaler
    - QDA 

### Rationale

- Best recall + PR-AUC combination.
