import pandas as pd
import pickle
from src.logger import logger
from src.preprocessing import preprocessing
from src.model_loader import get_model
from src.config import MODEL_DIR
import streamlit as st


@st.cache_resource
def _cached_model():
    """
    Load the model once per Streamlit session via the singleton loader.
    """
    return get_model()


def predict(input_data: dict) -> str:
    """
    Run end-to-end inference for a single observation.

    Args:
        - input_data: Mapping of feature name : raw numeric value, exactly as collected from the Streamlit input widgets.

    Returns:
        - "Storm" if the model predicts a thunderstorm event, otherwise "No Storm".
    """
    logger.info("Prediction request received")
    model = _cached_model()
    df = pd.DataFrame([input_data])
    df_processed = preprocessing(df)

    result = model.predict(df_processed)
    label = "Storm" if result[0] == 1 else "No Storm"

    logger.info(f"Prediction result: {label}")
    return label
