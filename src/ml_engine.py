import pandas as pd
import pickle
from src.logger import logger
from src.preprocessing import preprocessing
from src.model_loader import get_model
from src.config import MODEL_DIR
import streamlit as st


@st.cache_resource
def _cached_model():
    return get_model()


def predict(input_data: dict) -> str:
    logger.info("Prediction request received")
    model = _cached_model()
    df = pd.DataFrame([input_data])
    df_processed = preprocessing(df)

    result = model.predict(df_processed)
    label = "Storm" if result[0] == 1 else "No Storm"

    logger.info(f"Prediction result: {label}")
    return label
