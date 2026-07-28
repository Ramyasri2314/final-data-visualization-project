from pathlib import Path
import pandas as pd
import streamlit as st

@st.cache_data
def load_data():
    csv_path = Path(__file__).parent / "data" / "space_missions.csv"

    df = pd.read_csv(csv_path, encoding="latin1")

    df["Date"] = pd.to_datetime(df["Date"])
    df["Year"] = df["Date"].dt.year

    return df