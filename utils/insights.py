import streamlit as st


# KPI Metrics
def show_kpis(df):

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Students",
        len(df)
    )

    col2.metric(
        "Avg Score",
        round(
            df["Final_Exam_Score"].mean(),
            2
        )
    )

    col3.metric(
        "Avg Attendance",
        round(
            df["Attendance_Percentage"].mean(),
            2
        )
    )

    col4.metric(
        "Avg Study Hours",
        round(
            df["Study_Hours_Per_Week"].mean(),
            2
        )
    )


# Basic Dataset Insights
def dataset_insights(df):

    st.subheader("Dataset Insights")

    st.success(
        f"Highest Score : {df['Final_Exam_Score'].max()}"
    )

    st.warning(
        f"Lowest Score : {df['Final_Exam_Score'].min()}"
    )

    st.info(
        f"Average Score : {round(df['Final_Exam_Score'].mean(),2)}"
    )

    pass_percent = round(
        (df["Pass_Fail"] == "Pass").mean() * 100,
        2
    )

    st.write(
        f"Pass Percentage : {pass_percent}%"
    )


# Correlation Insights
def correlation_insights(df):

    st.subheader(
        "Relationship Analysis"
    )

    study_corr = df[
        ["Study_Hours_Per_Week",
         "Final_Exam_Score"]
    ].corr().iloc[0, 1]

    attendance_corr = df[
        ["Attendance_Percentage",
         "Final_Exam_Score"]
    ].corr().iloc[0, 1]

    sleep_corr = df[
        ["Sleep_Hours",
         "Final_Exam_Score"]
    ].corr().iloc[0, 1]

    st.write(
        f"Study Hours ↔ Score Correlation : {round(study_corr,2)}"
    )

    st.write(
        f"Attendance ↔ Score Correlation : {round(attendance_corr,2)}"
    )

    st.write(
        f"Sleep ↔ Score Correlation : {round(sleep_corr,2)}"
    )


# Top Students
def top_students(df):

    st.subheader(
        "Top Performers"
    )

    top = df.nlargest(
        10,
        "Final_Exam_Score"
    )

    st.dataframe(top)


# Weak Students
def low_students(df):

    st.subheader(
        "Students Needing Attention"
    )

    low = df.nsmallest(
        10,
        "Final_Exam_Score"
    )

    st.dataframe(low)


# Attendance Insights
def attendance_insights(df):

    st.subheader(
        "Attendance Analytics"
    )

    low_attendance = df[
        df["Attendance_Percentage"] < 75
    ]

    st.write(
        f"Students below 75% attendance : {len(low_attendance)}"
    )

    avg_score = low_attendance[
        "Final_Exam_Score"
    ].mean()

    st.write(
        f"Average score of low attendance students : {round(avg_score,2)}"
    )


# Student Segmentation
def student_segments(df):

    st.subheader(
        "Student Segments"
    )

    high = len(
        df[df["Final_Exam_Score"] >= 85]
    )

    medium = len(
        df[
            (df["Final_Exam_Score"] >= 60) &
            (df["Final_Exam_Score"] < 85)
        ]
    )

    low = len(
        df[df["Final_Exam_Score"] < 60]
    )

    st.write(
        f"High Performers : {high}"
    )

    st.write(
        f"Average Students : {medium}"
    )

    st.write(
        f"At Risk Students : {low}"
    )


# Summary Statistics
def summary_stats(df):

    st.subheader(
        "Summary Statistics"
    )

    st.dataframe(
        df.describe()
    )


# Complete Insight Engine
def run_all_insights(df):

    show_kpis(df)

    dataset_insights(df)

    correlation_insights(df)

    attendance_insights(df)

    student_segments(df)

    top_students(df)

    low_students(df)

    summary_stats(df)
