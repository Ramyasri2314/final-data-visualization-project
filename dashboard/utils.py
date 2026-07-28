import pandas as pd
import streamlit as st

@st.cache_data
def load_data():
    df = pd.read_csv("data/space_missions.csv", encoding="latin1")

    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
    df["Year"] = df["Date"].dt.year

    return df