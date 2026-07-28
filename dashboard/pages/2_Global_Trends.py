import streamlit as st
import plotly.express as px
from utils import load_data

st.title("📈 Global Space Mission Trends")

df = load_data()

# Missions per Year
missions = df.groupby("Year").size().reset_index(name="Missions")

fig = px.line(
    missions,
    x="Year",
    y="Missions",
    markers=True,
    title="Number of Space Missions per Year"
)

st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# Mission Status
if "MissionStatus" in df.columns:
    status = df["MissionStatus"].value_counts().reset_index()
    status.columns = ["Status", "Count"]

    fig = px.pie(
        status,
        names="Status",
        values="Count",
        title="Mission Status"
    )

    st.plotly_chart(fig, use_container_width=True)
else:
    st.warning("MissionStatus column not found.")

st.markdown("---")

# Launches by Decade
df["Decade"] = (df["Year"] // 10) * 10

decade = df.groupby("Decade").size().reset_index(name="Launches")

fig = px.bar(
    decade,
    x="Decade",
    y="Launches",
    color="Launches",
    title="Launches by Decade"
)

st.plotly_chart(fig, use_container_width=True)