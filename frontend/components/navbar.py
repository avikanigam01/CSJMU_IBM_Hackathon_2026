import streamlit as st


def show_navbar(name, role):

    st.markdown(
        """
        <style>

        .sakhi-header {

            text-align:center;

            padding:25px;

            margin-bottom:25px;

        }


        .sakhi-title {

            font-size:60px;

            font-weight:900;

            letter-spacing:3px;

            color:#163832;

            margin-bottom:5px;

        }


        .sakhi-subtitle {

            font-size:20px;

            color:#3B5D50;

            font-weight:600;

        }


        .profile-card {

            background:white;

            padding:12px;

            border-radius:20px;

            text-align:center;

            color:#163832;

            font-weight:700;

            box-shadow:0px 5px 20px rgba(0,0,0,0.08);

        }


        </style>


        <div class="sakhi-header">


        <div class="sakhi-title">

        🌸 SAKHI

        </div>


        <div class="sakhi-subtitle">

        Smart Academic Knowledge & Help Interface

        </div>


        </div>

        """,
        unsafe_allow_html=True
    )


    st.markdown(

        f"""
        <div class="profile-card">

        👤 {name} &nbsp; | &nbsp; {role}

        </div>

        """,

        unsafe_allow_html=True

    )