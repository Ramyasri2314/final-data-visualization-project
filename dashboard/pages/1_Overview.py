import streamlit as st
from utils import load_data

st.title("📋 Dataset Overview")

df = load_data()

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Missions", len(df))

with col2:
    st.metric("Organizations", df["Company"].nunique())

with col3:
    st.metric("Launch Locations", df["Location"].nunique())

st.markdown("---")

st.subheader("Dataset Preview")

st.dataframe(df.head(10))

st.markdown("---")

st.subheader("Dataset Information")

st.write(df.describe(include="all"))