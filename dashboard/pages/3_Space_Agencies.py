import streamlit as st
import plotly.express as px
from utils import load_data

st.title("🏢 Space Agencies Analysis")

df = load_data()

st.markdown("""
This page analyses the major organizations that have conducted
space missions around the world.
""")

# -------------------------
# Top Agencies
# -------------------------

agency_count = (
    df["Company"]
    .value_counts()
    .head(10)
    .reset_index()
)

agency_count.columns = ["Company", "Missions"]

fig = px.bar(
    agency_count,
    x="Missions",
    y="Company",
    orientation="h",
    color="Missions",
    title="Top 10 Space Agencies"
)

fig.update_layout(yaxis=dict(categoryorder="total ascending"))

st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# -------------------------
# Pie Chart
# -------------------------

fig = px.pie(
    agency_count,
    names="Company",
    values="Missions",
    title="Share of Missions by Top Agencies"
)

st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# -------------------------
# KPI Cards
# -------------------------

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Organizations", df["Company"].nunique())

with col2:
    st.metric("Top Agency", agency_count.iloc[0]["Company"])

with col3:
    st.metric("Launches", int(agency_count.iloc[0]["Missions"]))

st.markdown("---")

st.subheader("Key Insights")

st.success("""
• A small number of agencies perform most launches.

• Government agencies dominated the early space race.

• Commercial companies are increasing their launch frequency.

• Space exploration has become more competitive over time.
""")