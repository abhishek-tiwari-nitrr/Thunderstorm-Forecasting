# Feature Dictionary

This document describes every feature that enters `model.predict()`. All features are present **after** the preprocessing pipeline runs.

---

## Raw inputs

| UI label | Internal key | Unit | Description |
|---|---|---|---|
| SWEAT Index | `SWEAT index` | — | Severe Weather Threat Index - composite measure of shear, moisture, and instability |
| K Index | `K index` | — | Empirical thunderstorm potential index based on temperature lapse rate and moisture |
| Totals Totals Index | `Totals totals index` | — | Cross Totals + Vertical Totals; measures instability through the mid-troposphere |
| Showalter Index | `Showalter Index` | °C | Stability index comparing 500 hPa temperature to a parcel lifted from 850 hPa |
| Lifted Index | `Lifted Index` | °C | Stability index based on a surface parcel lifted to 500 hPa; negative = unstable |
| Precipitable Water | `PRECIPITABLE WATER` | mm | Total column precipitable water vapour |
| Temperature at LCL | `Temperature at Lifted Condensation Level` | °C | Temperature at the level where a parcel becomes saturated |
| CINE | `Convective Inhibition Energy` | J/kg | Energy that inhibits convective initiation; usually negative |
| CAPE | `Convective Available Potential Energy` | J/kg | Positive buoyancy energy available to a rising parcel |
| 1000–500 Thickness | `1000-500 THICKNESS` | m / dam | Thickness of the 1000–500 hPa layer; proxy for mean tropospheric temperature |
| PLCL | `PLCL` | hPa | Pressure level of the Lifted Condensation Level |

---


## Engineered features

| Feature | Derivation | Purpose |
|---|---|---|
| `Environmental Stability` | `Showalter Index + Lifted Index` | Single stability signal from two complementary indices |
| `Moisture Indices` | `PRECIPITABLE WATER` | Retains precipitable water under a domain-aligned name |
| `Convective Potential` | `CAPE + CINE` | Net energy for convection after accounting for inhibition |
| `Temperature Pressure` | `1000-500 THICKNESS` | Renamed for clarity |
| `Moisture Temperature Profiles` | `PLCL` | Renamed for clarity |

--- 

## Target variable

The target was **shifted by one day** at data cleaning time so that atmospheric indices observed on day *T* are paired with the storm outcome on day *T+1* (next-day forecasting).
