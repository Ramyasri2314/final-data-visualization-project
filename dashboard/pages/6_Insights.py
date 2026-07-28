import streamlit as st
import plotly.express as px
from utils import load_data

st.title("💡 Project Insights")

df = load_data()

st.markdown("""
This page summarises the most important findings from the analysis of
global space missions.
""")

# KPI Cards
col1, col2, col3, col4 = st.columns(4)

col1.metric("🚀 Missions", len(df))
col2.metric("🏢 Companies", df["Company"].nunique())
col3.metric("🌍 Locations", df["Location"].nunique())
col4.metric("🛰 Rockets", df["Rocket"].nunique())

st.markdown("---")

# Top Companies
company = (
    df["Company"]
    .value_counts()
    .head(10)
    .reset_index()
)

company.columns = ["Company", "Missions"]

fig = px.bar(
    company,
    x="Company",
    y="Missions",
    color="Missions",
    title="Top 10 Space Organizations"
)

st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# Top Rockets
rocket = (
    df["Rocket"]
    .value_counts()
    .head(10)
    .reset_index()
)

rocket.columns = ["Rocket", "Launches"]

fig = px.bar(
    rocket,
    x="Rocket",
    y="Launches",
    color="Launches",
    title="Top Rockets Used"
)

st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

st.subheader("📌 Key Findings")

st.success("""
• Space missions have increased steadily since 1957.

• Government agencies dominated early exploration.

• Private companies are becoming major contributors.

• Kazakhstan, Russia and the USA host the busiest launch sites.

• Rocket technology has advanced significantly over time.
""")

st.markdown("---")

st.subheader("✅ Conclusion")

st.info("""
This dashboard provides an interactive analysis of global space missions,
highlighting mission growth, leading organizations, major launch
locations, and the evolution of rocket technology.
""")
