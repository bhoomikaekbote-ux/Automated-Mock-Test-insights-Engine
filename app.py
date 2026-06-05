import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Student Performance Analytics",
    page_icon="📊",
    layout="wide"
)

# Load Data
@st.cache_data
def load_data():
    df = pd.read_csv("student_exam_performance.csv")
    return df

df = load_data()

st.title("📚 Student Performance Analytics Dashboard")
st.markdown("Deep analytics dashboard for student exam performance")

# Sidebar Filters
st.sidebar.header("Filters")

gender = st.sidebar.multiselect(
    "Select Gender",
    options=df["Gender"].unique(),
    default=df["Gender"].unique()
)

pass_filter = st.sidebar.multiselect(
    "Pass/Fail",
    options=df["Pass_Fail"].unique(),
    default=df["Pass_Fail"].unique()
)

filtered = df[
    (df["Gender"].isin(gender)) &
    (df["Pass_Fail"].isin(pass_filter))
]

# KPIs
col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Students",
    len(filtered)
)

col2.metric(
    "Average Final Score",
    round(filtered["Final_Exam_Score"].mean(),2)
)

col3.metric(
    "Average Attendance",
    round(filtered["Attendance_Percentage"].mean(),2)
)

col4.metric(
    "Average Study Hours",
    round(filtered["Study_Hours_Per_Week"].mean(),2)
)

st.divider()

# Dataset Preview
st.subheader("Dataset Preview")
st.dataframe(filtered)

# Charts
c1, c2 = st.columns(2)

with c1:
    st.subheader("Final Exam Score Distribution")

    fig, ax = plt.subplots()

    ax.hist(
        filtered["Final_Exam_Score"],
        bins=8
    )

    ax.set_xlabel("Score")
    ax.set_ylabel("Count")

    st.pyplot(fig)

with c2:
    st.subheader("Study Hours vs Final Score")

    fig, ax = plt.subplots()

    ax.scatter(
        filtered["Study_Hours_Per_Week"],
        filtered["Final_Exam_Score"]
    )

    ax.set_xlabel("Study Hours")
    ax.set_ylabel("Final Score")

    st.pyplot(fig)

# Attendance Chart
st.subheader("Attendance vs Final Score")

fig, ax = plt.subplots()

ax.scatter(
    filtered["Attendance_Percentage"],
    filtered["Final_Exam_Score"]
)

ax.set_xlabel("Attendance %")
ax.set_ylabel("Final Score")

st.pyplot(fig)

# Gender Performance
st.subheader("Average Score by Gender")

gender_avg = filtered.groupby(
    "Gender"
)["Final_Exam_Score"].mean()

fig, ax = plt.subplots()

gender_avg.plot(
    kind="bar",
    ax=ax
)

st.pyplot(fig)

# Sleep Analysis
st.subheader("Sleep Hours Impact")

fig, ax = plt.subplots()

ax.scatter(
    filtered["Sleep_Hours"],
    filtered["Final_Exam_Score"]
)

ax.set_xlabel("Sleep Hours")
ax.set_ylabel("Final Score")

st.pyplot(fig)

# Insights
st.subheader("Insights")

top_score = filtered["Final_Exam_Score"].max()
low_score = filtered["Final_Exam_Score"].min()

st.success(
    f"Highest score: {top_score}"
)

st.warning(
    f"Lowest score: {low_score}"
)

st.info(
    f"Pass Percentage: {round((filtered['Pass_Fail']=='Pass').mean()*100,2)}%"
)

study_corr = filtered[
    ["Study_Hours_Per_Week","Final_Exam_Score"]
].corr().iloc[0,1]

attendance_corr = filtered[
    ["Attendance_Percentage","Final_Exam_Score"]
].corr().iloc[0,1]

st.write(
    f"Correlation Study Hours ↔ Score: {round(study_corr,2)}"
)

st.write(
    f"Correlation Attendance ↔ Score: {round(attendance_corr,2)}"
)

st.subheader("Summary Statistics")

st.dataframe(
    filtered.describe()
)
