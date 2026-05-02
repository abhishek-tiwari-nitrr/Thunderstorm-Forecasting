from pathlib import Path

# path
BASE_DIR: Path = Path(__file__).resolve().parent.parent
LOG_DIR: Path = BASE_DIR / "logs"
MODEL_DIR: Path = BASE_DIR / "model" / "model.pkl"

# Right-skewed features
log_cols: list[str] = ["SWEAT index"]

# Left-skewed features
reflect_cols: list[str] = ["K index", "Moisture Indices"]

# Features with negative values
shift_log_cols: list[str] = ["Convective Potential"]

# Streamlit app metadata
APP_TITLE: str = "Thunderstorm Forecasting"
APP_ICON: str = "⛈️"
