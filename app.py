import streamlit as st

from frontend.pages.login import login_page


st.set_page_config(
    page_title="SAKHI",
    layout="wide"
)


if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False


if "role" not in st.session_state:
    st.session_state["role"] = None


if st.session_state["logged_in"]:

    role = st.session_state["role"]


    if role == "Student":

        from frontend.pages.student_dashboard import student_dashboard

        student_dashboard()


    elif role == "Teacher":

        from frontend.pages.teacher_dashboard import teacher_dashboard

        teacher_dashboard()


    elif role == "HOD":

        from frontend.pages.hod_dashboard import hod_dashboard

        hod_dashboard()


else:

    login_page()