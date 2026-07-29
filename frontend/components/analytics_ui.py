import streamlit as st
import pandas as pd

from backend.analytics import (
    dashboard_statistics,
    complaint_statistics,
    feedback_statistics,
    quiz_statistics,
    top_students,
    latest_complaints
)


def analytics_ui():

    st.title("📊 Analytics Dashboard")

    # ==========================
    # Dashboard Statistics
    # ==========================

    stats = dashboard_statistics()

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric("👨‍🎓 Students", stats["students"])

    with c2:
        st.metric("👩‍🏫 Teachers", stats["teachers"])

    with c3:
        st.metric("⚠️ Complaints", stats["complaints"])

    c4, c5, c6 = st.columns(3)

    with c4:
        st.metric("📝 Feedback", stats["feedback"])

    with c5:
        st.metric("📚 Uploaded Notes", stats["notes"])

    with c6:
        st.metric("🎯 Avg Quiz Score", stats["average_score"])

    st.divider()

    # ==========================
    # Complaint Statistics
    # ==========================

    st.subheader("📌 Complaint Categories")

    complaints = complaint_statistics()

    if complaints:

        df = pd.DataFrame({

            "Category": complaints.keys(),

            "Count": complaints.values()

        })

        st.bar_chart(df.set_index("Category"))

    else:

        st.info("No complaints available.")

    st.divider()

    # ==========================
    # Feedback Statistics
    # ==========================

    st.subheader("😊 Feedback Analysis")

    feedback = feedback_statistics()

    df = pd.DataFrame({

        "Sentiment": feedback.keys(),

        "Count": feedback.values()

    })

    st.bar_chart(df.set_index("Sentiment"))

    st.divider()

    # ==========================
    # Quiz Statistics
    # ==========================

    st.subheader("📖 Subject Wise Quiz Performance")

    quiz = quiz_statistics()

    if quiz:

        df = pd.DataFrame({

            "Subject": quiz.keys(),

            "Average Score": quiz.values()

        })

        st.bar_chart(df.set_index("Subject"))

    else:

        st.info("No quiz data available.")

    st.divider()

    # ==========================
    # Top Students
    # ==========================

    st.subheader("🏆 Top 5 Students")

    students = top_students()

    if students:

        df = pd.DataFrame(

            students,

            columns=["Student", "Points"]

        )

        st.dataframe(df, use_container_width=True)

    else:

        st.info("Leaderboard is empty.")

    st.divider()

    # ==========================
    # Recent Complaints
    # ==========================

    st.subheader("🚨 Recent Complaints")

    recent = latest_complaints()

    if recent:

        df = pd.DataFrame(

            recent,

            columns=[

                "Complaint",

                "Category",

                "Severity"

            ]

        )

        st.dataframe(df, use_container_width=True)

    else:

        st.info("No complaints found.")
