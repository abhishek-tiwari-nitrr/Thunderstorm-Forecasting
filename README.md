# ⛈️ Thunderstorm Forecasting

A machine learning application that predicts whether a **thunderstorm will occur the following day** based on atmospheric sounding indices.

---

## 🧱 Project structure

```
thunderstorm-forecasting/
├── main.py
├── requirements.txt
├── .python-version
├── README.md
├── pyproject.toml
├── requirements-dev.txt
├── artifacts/                # EDA and experiment plots
├── data/
│   ├── raw/                  # Original source data
│   └── processed data/       # Cleaned CSVs
├── docs/
│   ├── DECISIONS.md          # Every modelling decision, with rationale
│   └── FEATURES.md           # Feature dictionary
├── model
│   └──  model.pkl            # Trained QDA pipeline
├── notebook/                 # Exploration & training notebooks
│   ├── 01_data_cleaning.ipynb
│   ├── 02_eda.ipynb
│   └── 03_preprocessing.ipynb
└── src/
    ├── config.py             # Paths & constants
    ├── logger.py
    ├── model_loader.py       # Model loader
    ├── preprocessing.py      # Feature engineering + transforms
    └── ml_engine.py          # predict() API

```

---

## 🚀 Quick start
```bash
# 1. Clone the repository
git clone https://github.com/abhishek-tiwari-nitrr/Thunderstorm-Forecasting
cd Thunderstorm-Forecasting

# 2. Create virtual environment & install dependencies
uv sync

# 3. Activate environment
.venv\Scripts\activate

# 4. Run the app
uv run streamlit run main.py
```

## Tech stack

| Layer | Technology |
|---|---|
| Language | Python 3.10+ |
| UI | Streamlit |
| ML - final model | scikit-learn (QDA, StandardScaler, GridSearchCV) |
| Class imbalance | imbalanced-learn (SMOTETomek) |
| Data | pandas, numpy |
| Model serialisation | pickle |
| Experiment tracking | MLflow |
| Packaging | pyproject.toml |
| Project Management | UV (Astral Python package manager) |
