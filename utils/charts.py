import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd


# Histogram for score distribution
def score_distribution(df):

    fig, ax = plt.subplots()

    ax.hist(
        df["Final_Exam_Score"],
        bins=10
    )

    ax.set_title("Final Exam Score Distribution")
    ax.set_xlabel("Score")
    ax.set_ylabel("Students")

    st.pyplot(fig)


# Study Hours vs Score
def study_vs_score(df):

    fig, ax = plt.subplots()

    ax.scatter(
        df["Study_Hours_Per_Week"],
        df["Final_Exam_Score"]
    )

    ax.set_title("Study Hours vs Final Score")

    ax.set_xlabel("Study Hours")

    ax.set_ylabel("Final Score")

    st.pyplot(fig)


# Attendance vs Score
def attendance_vs_score(df):

    fig, ax = plt.subplots()

    ax.scatter(
        df["Attendance_Percentage"],
        df["Final_Exam_Score"]
    )

    ax.set_title("Attendance vs Score")

    ax.set_xlabel("Attendance %")

    ax.set_ylabel("Score")

    st.pyplot(fig)


# Sleep Hours Impact
def sleep_analysis(df):

    fig, ax = plt.subplots()

    ax.scatter(
        df["Sleep_Hours"],
        df["Final_Exam_Score"]
    )

    ax.set_title("Sleep Hours Impact")

    ax.set_xlabel("Sleep Hours")

    ax.set_ylabel("Final Score")

    st.pyplot(fig)


# Gender Analysis
def gender_analysis(df):

    gender_avg = df.groupby(
        "Gender"
    )["Final_Exam_Score"].mean()

    fig, ax = plt.subplots()

    gender_avg.plot(
        kind="bar",
        ax=ax
    )

    ax.set_title("Average Score by Gender")

    ax.set_ylabel("Average Score")

    st.pyplot(fig)


# Pass Fail Pie Chart
def pass_fail_chart(df):

    counts = df["Pass_Fail"].value_counts()

    fig, ax = plt.subplots()

    ax.pie(
        counts,
        labels=counts.index,
        autopct="%1.1f%%"
    )

    ax.set_title("Pass vs Fail")

    st.pyplot(fig)


# Correlation Heatmap
def correlation_chart(df):

    numeric = df.select_dtypes(
        include="number"
    )

    corr = numeric.corr()

    fig, ax = plt.subplots()

    image = ax.imshow(corr)

    ax.set_xticks(range(len(corr.columns)))
    ax.set_yticks(range(len(corr.columns)))

    ax.set_xticklabels(
        corr.columns,
        rotation=90
    )

    ax.set_yticklabels(
        corr.columns
    )

    plt.colorbar(image)

    ax.set_title(
        "Correlation Heatmap"
    )

    st.pyplot(fig)


# Boxplot for Outliers
def score_boxplot(df):

    fig, ax = plt.subplots()

    ax.boxplot(
        df["Final_Exam_Score"]
    )

    ax.set_title(
        "Score Outlier Analysis"
    )

    ax.set_ylabel(
        "Final Score"
    )

    st.pyplot(fig)
