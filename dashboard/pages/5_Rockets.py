import streamlit as st
import plotly.express as px
from utils import load_data

st.title("🚀 Rockets Analysis")

df = load_data()

st.markdown("""
This page analyses the rockets used in global space missions,
their usage over time, and the organisations that use them.
""")

# ---------------------------------------
# Top 10 Most Used Rockets
# ---------------------------------------

rocket_count = (
    df["Rocket"]
    .value_counts()
    .head(10)
    .reset_index()
)

rocket_count.columns = ["Rocket", "Missions"]

fig = px.bar(
    rocket_count,
    x="Missions",
    y="Rocket",
    orientation="h",
    color="Missions",
    title="Top 10 Most Frequently Used Rockets"
)

fig.update_layout(yaxis=dict(categoryorder="total ascending"))

st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# ---------------------------------------
# Top Companies Using Rockets
# ---------------------------------------

company = (
    df["Company"]
    .value_counts()
    .head(10)
    .reset_index()
)

company.columns = ["Company", "Launches"]

fig = px.bar(
    company,
    x="Company",
    y="Launches",
    color="Launches",
    title="Top Companies by Rocket Launches"
)

st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# ---------------------------------------
# Rocket Usage Over Time
# ---------------------------------------

rocket_year = (
    df.groupby("Year")
      .size()
      .reset_index(name="Launches")
)

fig = px.line(
    rocket_year,
    x="Year",
    y="Launches",
    markers=True,
    title="Rocket Launches Over Time"
)

st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# ---------------------------------------
# KPI Cards
# ---------------------------------------

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Rocket Types", df["Rocket"].nunique())

with col2:
    st.metric("Companies", df["Company"].nunique())

with col3:
    st.metric("Total Missions", len(df))

st.markdown("---")

st.subheader("📌 Key Insights")

st.success("""
• A small number of rocket families account for a large proportion of launches.

• Launch frequency has increased significantly over time.

• Multiple organisations use a wide variety of launch vehicles.

• Continuous rocket innovation has driven modern space exploration.
""")