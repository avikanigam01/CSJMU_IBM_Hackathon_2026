import streamlit as st
from backend.complaint_ai import save_complaint


def complaint_ui(student_id=1):

    st.title("⚠️ AI Complaint Assistant")

    st.write(
        "Your complaint will be analyzed by AI and forwarded to the HOD if necessary."
    )

    complaint = st.text_area(
        "Describe your complaint",
        height=180,
        placeholder="Example: My seniors are ragging me in the hostel..."
    )

    if st.button("Submit Complaint"):

        if complaint.strip() == "":

            st.warning("Please write your complaint.")

        else:

            result = save_complaint(
                student_id,
                complaint
            )

            st.success("Complaint Submitted Successfully!")

            st.subheader("AI Analysis")

            col1, col2 = st.columns(2)

            with col1:

                st.metric(
                    "Category",
                    result["category"]
                )

                st.metric(
                    "Severity",
                    result["severity"]
                )

            with col2:

                st.metric(
                    "Sentiment",
                    result["sentiment"]
                )

                st.metric(
                    "Confidence",
                    f'{result["confidence"]}%'
                )

            if result["severity"] == "High":

                st.error(
                    "🚨 High Priority Complaint. This will be highlighted in the HOD dashboard."
                )

            elif result["severity"] == "Medium":

                st.warning(
                    "⚠️ Medium Priority Complaint."
                )

            else:

                st.info(
                    "✅ Complaint recorded successfully."
                )
