import streamlit as st

from frontend.components.navbar import show_navbar
from frontend.components.sidebar import teacher_sidebar

from backend.pdf_processor import extract_text_from_pdf
from backend.quiz_generator import save_quiz


def teacher_dashboard():

    user = st.session_state.get(
        "user",
        ("Teacher",)
    )

    teacher_name = user[1] if len(user) > 1 else "Teacher"

    show_navbar(
        teacher_name,
        "Teacher"
    )

    page = teacher_sidebar()

    # ---------------- Dashboard ----------------

    if page == "🏠 Dashboard":

        st.title("👩‍🏫 Teacher Dashboard")

        st.info("Upload lecture notes.")

        st.info("Generate quizzes.")

        st.info("View student feedback.")

    # ---------------- Upload Notes ----------------

    elif page == "📄 Upload Notes":

        st.header("📄 Upload Lecture Notes")

        subject = st.text_input("Subject")

        uploaded_file = st.file_uploader(
            "Choose PDF",
            type=["pdf"]
        )

        if st.button("Upload Notes"):

            if uploaded_file is None:

                st.warning("Please upload a PDF.")

            else:

                text = extract_text_from_pdf(
                    uploaded_file,
                    subject
                )

                st.success("PDF Uploaded Successfully!")

                st.write(text[:500])

    # ---------------- Feedback ----------------

    elif page == "📊 Student Feedback":

        st.header("Student Feedback")

        st.info("Feedback page will display all feedback collected from students.")

    # ---------------- Quiz ----------------

    elif page == "📝 Generate Quiz":

        st.header("Generate Quiz")

        subject = st.text_input("Subject Name")

        if st.button("Generate"):

            total = save_quiz(subject)

            st.success(f"{total} Questions Generated Successfully")
