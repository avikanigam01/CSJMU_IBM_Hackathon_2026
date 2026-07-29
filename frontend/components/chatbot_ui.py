import streamlit as st
from backend.chatbot import ask_question


def chatbot_ui():

    st.title("🤖 AI Subject Chatbot")

    st.write("Ask questions from the uploaded lecture notes.")

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

    question = st.text_input(
        "Enter your question"
    )

    if st.button("Ask AI"):

        if question.strip() == "":

            st.warning("Please enter a question.")

        else:

            response = ask_question(
                question,
                subject
            )

            st.success("Answer")

            st.write(response["answer"])

    st.markdown("---")

    st.info(
        "The chatbot answers only from the PDF notes uploaded by the teacher."
    )
