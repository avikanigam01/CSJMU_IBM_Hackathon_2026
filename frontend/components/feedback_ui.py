import streamlit as st
from backend.feedback_ai import save_feedback


def feedback_ui(student_id=1):

    st.title("📝 Teacher Feedback")

    st.write("Share your feedback about today's class.")

    teacher = st.text_input(
        "Teacher Name",
        placeholder="Enter teacher's name"
    )

    subject = st.selectbox(
        "Subject",
        [
            "Python",
            "Java",
            "DBMS",
            "Operating System",
            "Computer Networks"
        ]
    )

    rating = st.slider(
        "Rate the Class",
        1,
        5,
        3
    )

    feedback = st.text_area(
        "Write your feedback",
        height=180,
        placeholder="Example: The lecture was very interactive and easy to understand."
    )

    if st.button("Submit Feedback"):

        if teacher == "" or feedback == "":

            st.warning("Please fill all the fields.")

        else:

            sentiment = save_feedback(

                student_id,

                teacher,

                subject,

                rating,

                feedback

            )

            st.success("Feedback Submitted Successfully!")

            st.subheader("AI Feedback Analysis")

            st.metric(
                "Detected Sentiment",
                sentiment
            )

            if sentiment == "Positive":

                st.success("😊 Students are satisfied with this class.")

            elif sentiment == "Negative":

                st.error("⚠️ This feedback needs attention.")

            else:

                st.info("😐 Neutral feedback recorded.")
