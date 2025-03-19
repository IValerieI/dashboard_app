import streamlit as st

# --- PAGE SETUP ---
eda_page = st.Page("eda/eda.py", title="Анализ данных")
arima_page = st.Page("models/arima.py", title="ARIMA")
st.set_page_config(layout="wide")

# --- NAVIGATION SETUP [WITH SECTIONS]---
pg = st.navigation(
        {
            "Датасет": [eda_page],
            "Модели": [arima_page]
        }
    )

# --- RUN NAVIGATION ---
pg.run()