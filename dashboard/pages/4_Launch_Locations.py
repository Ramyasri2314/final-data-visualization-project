import streamlit as st
import plotly.express as px
from utils import load_data

st.title("🌍 Launch Locations Analysis")

df = load_data()

# Remove missing locations
df = df.dropna(subset=["Location"])

st.markdown("""
This page explores the geographical distribution of global space missions.
""")

# -----------------------------
# Top Launch Locations
# -----------------------------
top_locations = (
    df["Location"]
    .value_counts()
    .head(10)
    .reset_index()
)

top_locations.columns = ["Location", "Missions"]

fig = px.bar(
    top_locations,
    x="Missions",
    y="Location",
    orientation="h",
    color="Missions",
    title="Top 10 Launch Locations"
)

fig.update_layout(yaxis=dict(categoryorder="total ascending"))

st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# -----------------------------
# Country Analysis
# -----------------------------
df["Country"] = df["Location"].astype(str).str.split(",").str[-1].str.strip()

country = (
    df["Country"]
    .value_counts()
    .head(10)
    .reset_index()
)

country.columns = ["Country", "Launches"]

fig = px.bar(
    country,
    x="Country",
    y="Launches",
    color="Launches",
    title="Top Countries"
)

st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

fig = px.pie(
    country,
    names="Country",
    values="Launches",
    title="Launch Distribution by Country"
)

st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Launch Locations", df["Location"].nunique())

with col2:
    st.metric("Countries", df["Country"].nunique())

with col3:
    st.metric("Top Country", country.iloc[0]["Country"])

st.markdown("---")

st.success("""
• Most launches are concentrated in a few countries.

• Spaceports play a major role in global missions.

• Launch infrastructure is concentrated in established space nations.
""")