import numpy as np
import pandas as pd
from src.config import log_cols, reflect_cols, shift_log_cols
from src.logger import logger


def _log_conversion(col: pd.Series) -> pd.Series:
    logger.info(f"Applying log transform to '{col.name}'")
    return np.log1p(col)


def _reflect_conversion(col: pd.Series) -> pd.Series:
    logger.info(f"Applying reflect-log transform to '{col.name}'")
    return np.log1p(col.max() - col)


def _shift_log_conversion(col: pd.Series) -> pd.Series:
    shift = abs(col.min()) + 1
    logger.info(f"Applying shift-log transform to '{col.name}'")
    return np.log1p(col + shift)


def _apply_transformation(df: pd.DataFrame) -> pd.DataFrame:
    for col in log_cols:
        if col in df.columns:
            df[col] = _log_conversion(df[col])
    for col in reflect_cols:
        if col in df.columns:
            df[col] = _reflect_conversion(df[col])
    for col in shift_log_cols:
        if col in df.columns:
            df[col] = _shift_log_conversion(df[col])
    return df


def preprocessing(df: pd.DataFrame) -> pd.DataFrame:
    df["Environmental Stability"] = df["Showalter Index"] + df["Lifted Index"]
    df["Moisture Indices"] = df["PRECIPITABLE WATER"]
    df["Convective Potential"] = (
        df["Convective Available Potential Energy"] + df["Convective Inhibition Energy"]
    )
    df["Temperature Pressure"] = df["1000-500 THICKNESS"]
    df["Moisture Temperature Profiles"] = df["PLCL"]

    cols_to_drop = [
        "Showalter Index",
        "Lifted Index",
        "Convective Available Potential Energy",
        "Convective Inhibition Energy",
        "Vertical Totals Index",
        "Cross Totals Index",
        "Temperature at Lifted Condensation Level",
        "PLCL",
        "1000-500 THICKNESS",
        "PRECIPITABLE WATER",
    ]

    df.drop(columns=cols_to_drop, inplace=True, errors="ignore")
    logger.info("Feature engineering complete")

    df = _apply_transformation(df)
    logger.info("Preprocessing complete for inference request")
    return df
