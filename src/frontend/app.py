import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
sys.path.append(PROJECT_ROOT)

# above code is saying used this as a working directory when running streamlit than only it can identify
#.env file and other python script that we are using

import streamlit as st

st.set_page_config(
            page_title="DR. ML - Multi-Disease Predictor",
            page_icon="🩺",
            layout='centered'
)


st.title("🧠 Dr. ML - Multi-Disease Predictor")

st.write(
        """
Use the left sidebar to navigate:
- 🩺 Diabetes Risk Predictor
- ❤️ Heart Disease Risk Predictor
"""
)

st.info("Make sure the FASTAPI backend is running before using predictions")


# to run this code: streamlit run src/frontend/app.py