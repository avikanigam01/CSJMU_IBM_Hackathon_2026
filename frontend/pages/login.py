import streamlit as st

from backend.auth import (
    login,
    register_student,
    register_teacher,
    register_hod
)


def login_page():

    st.title("🎓 SAKHI Login Portal")

    option = st.selectbox(
        "Choose Option",
        [
            "Login",
            "Student Registration",
            "Teacher Registration",
            "HOD Registration"
        ]
    )

    st.divider()


    # ============================
    # LOGIN
    # ============================

    if option == "Login":

        role = st.selectbox(
            "Select Role",
            [
                "Student",
                "Teacher",
                "HOD"
            ]
        )

        email = st.text_input("Email")

        password = st.text_input(
            "Password",
            type="password"
        )


        if st.button("Login"):

            success, user = login(
                email,
                password,
                role
            )


            if success:

                st.success("Login Successful!")

                st.session_state["logged_in"] = True
                st.session_state["role"] = role
                st.session_state["user"] = user

                st.rerun()


            else:

                st.error("Invalid Email or Password")



    # ============================
    # STUDENT REGISTER
    # ============================

    elif option == "Student Registration":

        name = st.text_input("Student Name")

        email = st.text_input("Email")

        password = st.text_input(
            "Password",
            type="password"
        )

        department = st.text_input(
            "Department"
        )

        year = st.number_input(
            "Year",
            min_value=1,
            max_value=4
        )


        if st.button("Register Student"):


            success, message = register_student(
                name,
                email,
                password,
                department,
                year
            )


            if success:
                st.success(message)

            else:
                st.error(message)



    # ============================
    # TEACHER REGISTER
    # ============================

    elif option == "Teacher Registration":


        name = st.text_input("Teacher Name")

        email = st.text_input("Email")

        password = st.text_input(
            "Password",
            type="password"
        )

        subject = st.text_input(
            "Subject"
        )


        if st.button("Register Teacher"):


            success, message = register_teacher(
                name,
                email,
                password,
                subject
            )


            if success:
                st.success(message)

            else:
                st.error(message)



    # ============================
    # HOD REGISTER
    # ============================

    else:


        name = st.text_input("HOD Name")

        email = st.text_input("Email")

        password = st.text_input(
            "Password",
            type="password"
        )

        department = st.text_input(
            "Department"
        )


        if st.button("Register HOD"):


            success, message = register_hod(
                name,
                email,
                password,
                department
            )


            if success:
                st.success(message)

            else:
                st.error(message)