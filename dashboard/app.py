import streamlit as st
from utils import load_data

st.set_page_config(
    page_title="Space Missions Analytics",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 Space Missions Analytics Dashboard")

df = load_data()

st.write(df.columns)

st.markdown("""
Welcome to the **Space Missions Analytics Dashboard**.

This dashboard presents an interactive analysis of global space missions conducted between **1957 and 2022**.

Use the navigation panel on the left to explore different sections of the dashboard.
""")