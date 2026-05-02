from src.ml_engine import predict
import streamlit as st
from src.config import APP_ICON, APP_TITLE

# Page configuration

st.set_page_config(
    page_title=APP_TITLE,
    page_icon=APP_ICON,
    layout="wide",
)

st.title(f"{APP_ICON} {APP_TITLE}")
st.caption("Next-day thunderstorm prediction using atmospheric indices.")
st.divider()


st.subheader("Atmospheric Indices")

# Input form

col1, col2, col3, col4 = st.columns(4)
with col1:
    sweat_index = st.number_input("SWEAT Index", step=1.0, format="%.2f")
with col2:
    k_index = st.number_input("K Index", step=1.0, format="%.2f")
with col3:
    total_index = st.number_input(
        "Totals Totals Index",
        help="Cross Totals + Vertical Totals",
        step=1.0,
        format="%.2f",
    )
with col4:
    showalter = st.number_input("Showalter Index", step=1.0, format="%.2f")

col5, col6, col7, col8 = st.columns(4)
with col5:
    lifted = st.number_input("Lifted Index", step=1.0, format="%.2f")
with col6:
    precip_water = st.number_input("Precipitable Water", step=1.0, format="%.2f")
with col7:
    tlcl = st.number_input(
        "Temperature at LCL",
        help="Temperature at the Lifted Condensation Level",
        step=1.0,
        format="%.2f",
    )
with col8:
    cine = st.number_input(
        "CINE", help="Convective Inhibition Energy", step=1.0, format="%.2f"
    )

col9, col10, col11, _ = st.columns(4)
with col9:
    cape = st.number_input(
        "CAPE", help="Convective Available Potential Energy", step=1.0, format="%.2f"
    )
with col10:
    thickness = st.number_input("1000–500 Thickness", step=1.0, format="%.2f")
with col11:
    plcl = st.number_input(
        "PLCL",
        help="Pressure at the Lifted Condensation Level",
        step=1.0,
        format="%.2f",
    )

st.divider()

# Prediction

_, btn_col = st.columns([3, 1])
with btn_col:
    run = st.button("⚡ Run Prediction", type="primary", width="stretch")

if run:
    input_data = {
        "SWEAT index": sweat_index,
        "K index": k_index,
        "Totals totals index": total_index,
        "Showalter Index": showalter,
        "Lifted Index": lifted,
        "PRECIPITABLE WATER": precip_water,
        "Convective Available Potential Energy": cape,
        "Temperature at Lifted Condensation Level": tlcl,
        "Convective Inhibition Energy": cine,
        "1000-500 THICKNESS": thickness,
        "PLCL": plcl,
    }

    with st.spinner("Running prediction…"):
        try:
            result = predict(input_data)
        except FileNotFoundError:
            st.error("Model file not found. Please ensure `model/model.pkl` exists.")
            st.stop()
        except Exception as exc:
            st.error(f"Prediction failed: {exc}")
            st.stop()

    if result == "Storm":
        st.error(
            "⛈️ **Storm predicted** - thunderstorm conditions are likely tomorrow."
        )
    else:
        st.success(
            "☀️ **No Storm** - conditions do not indicate a thunderstorm tomorrow."
        )
