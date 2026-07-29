import streamlit as st

from frontend.components.navbar import show_navbar
from frontend.components.sidebar import hod_sidebar
from frontend.components.analytics_ui import analytics_ui

from backend.report_generator import generate_report


def hod_dashboard():

    user = st.session_state.get(
        "user",
        ("HOD",)
    )

    hod_name = user[1] if len(user) > 1 else "HOD"

    show_navbar(
        hod_name,
        "HOD"
    )

    page = hod_sidebar()

    # ---------------- Dashboard ----------------

    if page == "🏠 Dashboard":

        st.title("👨‍💼 HOD Dashboard")

        st.success("Welcome to the HOD Panel")

        st.info("Monitor complaints, analytics and reports.")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Complaints", "--")

        with col2:
            st.metric("Students", "--")

        with col3:
            st.metric("Teachers", "--")

    # ---------------- Complaints ----------------

    elif page == "⚠️ Complaints":

        st.header("⚠️ Complaint Monitoring")

        st.info(
            "High priority complaints detected by AI will appear here."
        )

        st.warning(
            "This section will display complaints from the database."
        )

    # ---------------- Analytics ----------------

    elif page == "📈 Analytics":

        analytics_ui()

    # ---------------- Reports ----------------

    elif page == "📄 Monthly Report":

        st.header("📄 Generate Monthly Report")

        st.write(
            "Generate the monthly report for the HOD."
        )

        if st.button("Generate Report"):

            path = generate_report()

            st.success("Report Generated Successfully!")

            st.write("Saved at:")

            st.code(path)

            with open(path, "rb") as file:

                st.download_button(

                    "⬇ Download Report",

                    data=file,

                    file_name=path.split("/")[-1],

                    mime="text/plain"

                )
