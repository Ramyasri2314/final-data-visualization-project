import streamlit as st

st.title("📊 Analytical Questions")

st.markdown("## Answers to Analytical Questions")

questions = [
    (
        "1. Which company has conducted the highest number of space missions?",
        "RVSN USSR has conducted the highest number of recorded space missions in the dataset."
    ),
    (
        "2. How have space missions changed over time?",
        "The number of space missions has increased significantly, especially after 2000."
    ),
    (
        "3. Which countries have the most launch locations?",
        "Russia, Kazakhstan, and the USA contain the most active launch locations."
    ),
    (
        "4. Which rockets are used most frequently?",
        "Cosmos-3M, Voskhod, and Soyuz rocket families are among the most frequently used."
    ),
    (
        "5. What is the mission success rate?",
        "Most recorded missions were successful, indicating improvements in launch technology."
    ),
    (
        "6. Are active rockets more successful than retired rockets?",
        "Active rockets generally show higher success rates due to technological advancements."
    ),
    (
        "7. Which organisations dominate global space missions?",
        "Government agencies dominated early missions, while private companies such as SpaceX have become increasingly important."
    ),
    (
        "8. Which launch locations are used most often?",
        "Baikonur Cosmodrome and Plesetsk Cosmodrome are among the busiest launch sites."
    ),
    (
        "9. What trend is observed in commercial space missions?",
        "Commercial space missions have grown rapidly in recent years."
    ),
    (
        "10. What is the overall conclusion from the analysis?",
        "Global space exploration has expanded significantly, driven by technological progress and increasing participation from both governments and private organisations."
    ),
]

for q, a in questions:
    with st.expander(q):
        st.write(a)