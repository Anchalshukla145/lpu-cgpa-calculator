import streamlit as st
import pandas as pd
import os

st.set_page_config(
    page_title="LPU Smart CGPA Calculator",
    page_icon="🎓",
    layout="wide"
)

# Load CSS
with open(os.path.join("styles", "main.css")) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ---------- HEADER ----------
st.markdown("<h1 class='main-title'>🎓 LPU Smart CGPA & Percentile Estimator</h1>", unsafe_allow_html=True)
st.markdown(
    "<p class='subtitle'>Relative grading based • Subject-wise • TGPA & Percentile estimation</p>",
    unsafe_allow_html=True
)

st.write("")

# ---------- INPUT ----------
st.markdown("### 📘 Enter Subject Details")

num_subjects = st.number_input(
    "Number of Subjects",
    min_value=1,
    max_value=10,
    step=1
)

subjects_data = []

for i in range(num_subjects):
    st.markdown(f"#### Subject {i+1}")
    c1, c2, c3, c4 = st.columns(4)

    name = c1.text_input("Subject Name", key=f"name{i}")
    your = c2.number_input("Your Marks", min_value=0, key=f"your{i}")
    highest = c3.number_input("Highest Marks", min_value=1, key=f"high{i}")
    credit = c4.number_input("Credit", min_value=1, key=f"credit{i}")

    percent = (your / highest) * 100

    if percent >= 85:
        grade = "A+ – O"
        gp = 9.5
        cat = "Excellent"
    elif percent >= 75:
        grade = "A – A+"
        gp = 8.5
        cat = "Very Good"
    elif percent >= 65:
        grade = "B+ – A"
        gp = 7.5
        cat = "Good"
    elif percent >= 55:
        grade = "B – B+"
        gp = 6.5
        cat = "Average"
    else:
        grade = "C / Risk of F"
        gp = 5.0
        cat = "Needs Improvement"

    subjects_data.append([
        name,
        f"{percent:.1f}%",
        grade,
        gp,
        credit,
        cat
    ])

# ---------- OUTPUT ----------
if subjects_data:
    df = pd.DataFrame(
        subjects_data,
        columns=[
            "Subject",
            "% of Highest",
            "Possible Grade",
            "Grade Point",
            "Credit",
            "Percentile Category"
        ]
    )

    st.write("### 📊 Estimated Results")
    st.dataframe(df, use_container_width=True)

    total_points = sum(df["Grade Point"] * df["Credit"])
    total_credits = sum(df["Credit"])

    tgpa_center = total_points / total_credits
    tgpa_lower = max(round(tgpa_center - 0.35, 2), 0)
    tgpa_upper = min(round(tgpa_center + 0.35, 2), 10)

    st.markdown(
        f"<div class='tgpa-card'>🎯 Estimated TGPA Range: <b>{tgpa_lower} – {tgpa_upper}</b></div>",
        unsafe_allow_html=True
    )
    st.markdown(
        "<div style='text-align:center; color:#d0c0ff;'>⚠️ Approximate results based on relative grading trends at LPU.<br>"
        "💡 Actual CGPA may be higher for top performers.</div>",
        unsafe_allow_html=True
    )

# ---------- FOOTER ----------
st.markdown("---")
st.markdown(
    "<center class='footer'>"
    "Made with ❤️ by <b>Anchal Shukla</b>"
    "</center>",
    unsafe_allow_html=True
)
