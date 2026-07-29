import streamlit as st
from backend.leaderboard import (
    get_top_students,
    get_leaderboard
)


def leaderboard_ui():

    st.title("🏆 Leaderboard")

    st.write("Top performing students based on quiz scores.")

    # ---------------------------
    # Top 3 Students
    # ---------------------------

    top_students = get_top_students()

    st.subheader("🥇 Top 3 Students")

    if len(top_students) == 0:

        st.info("Leaderboard is empty.")

    else:

        medals = ["🥇", "🥈", "🥉"]

        cols = st.columns(3)

        for i, student in enumerate(top_students):

            with cols[i]:

                st.metric(

                    medals[i] + " " + student[0],

                    f"{student[1]} Points"

                )

    st.divider()

    # ---------------------------
    # Full Leaderboard
    # ---------------------------

    st.subheader("📊 Complete Leaderboard")

    leaderboard = get_leaderboard()

    if len(leaderboard) == 0:

        st.warning("No student has attempted any quiz yet.")

    else:

        rank = 1

        for student in leaderboard:

            st.write(

                f"**#{rank}**  |  {student[0]}  |  **{student[1]} Points**"

            )

            rank += 1
