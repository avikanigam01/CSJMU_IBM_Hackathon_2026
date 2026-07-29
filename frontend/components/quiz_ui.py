import streamlit as st

from backend.quiz_generator import (
    get_quiz,
    calculate_score,
    save_score
)

from backend.leaderboard import update_leaderboard


def quiz_ui(student_id=1):

    st.title("📝 AI Quiz")

    subject = st.selectbox(
        "Select Subject",
        [
            "Python",
            "Java",
            "DBMS",
            "Operating System",
            "Computer Networks"
        ]
    )

    if st.button("Load Quiz"):

        quiz = get_quiz(subject)

        if len(quiz) == 0:

            st.warning("No quiz available for this subject.")

        else:

            st.session_state.quiz = quiz

    if "quiz" not in st.session_state:
        return

    quiz = st.session_state.quiz

    answers = []

    st.subheader("Answer the Questions")

    for i, q in enumerate(quiz):

        st.write(f"### Q{i+1}. {q[2]}")

        option = st.radio(

            f"Choose Answer {i+1}",

            [

                q[3],

                q[4],

                q[5],

                q[6]

            ],

            key=f"q{i}"

        )

        answers.append(option)

    if st.button("Submit Quiz"):

        score = calculate_score(
            answers,
            quiz
        )

        total = len(quiz)

        save_score(

            student_id,

            subject,

            score,

            total

        )

        update_leaderboard(student_id)

        percentage = (score / total) * 100

        st.success(
            f"You scored {score} out of {total}"
        )

        st.progress(percentage / 100)

        st.metric(
            "Percentage",
            f"{percentage:.2f}%"
        )

        if percentage >= 80:

            st.balloons()

            st.success(
                "🏆 Excellent Performance!"
            )

        elif percentage >= 50:

            st.info(
                "👍 Good Job!"
            )

        else:

            st.warning(
                "📚 Keep Practicing!"
            )
