import streamlit as st


def student_sidebar():

    st.sidebar.markdown(
        """
        <h1 style="
        color:#ff7b89;
        text-align:center;
        ">
        SAKHI
        </h1>
    
        <p style="
        text-align:center;
        ">
        AI Student Companion
        </p>
        """,
        unsafe_allow_html=True
    )


    option = st.sidebar.radio(

        "Navigation",

        [

            "🏠 Home",

            "📮 CHITTI",

            "🤖 Class Assistant",

            "📝 Quiz",

            "⭐ Feedback"

        ]

    )


    return option



def teacher_sidebar():

    return st.sidebar.radio(
        "Teacher Menu",
        [
            "🏠 Dashboard",
            "📄 Upload Notes",
            "📝 Generate Quiz"
        ]
    )



def hod_sidebar():

    return st.sidebar.radio(
        "HOD Menu",
        [
            "🏠 Dashboard",
            "⚠️ Complaints",
            "📈 Analytics",
            "📄 Monthly Report"
        ]
    )