import streamlit as st

def load_css():

    st.markdown(
        """
        <style>

        /* Main background */

        .stApp {

            background: linear-gradient(
                135deg,
                #FFF1F5,
                #E5F9F2
            );

        }


        /* Hide default menu */

        #MainMenu {

            visibility:hidden;

        }


        footer {

            visibility:hidden;

        }



        /* Hero title */

        .hero {

            text-align:center;

            padding:40px;

            background:rgba(255,255,255,0.35);

            border-radius:25px;

            backdrop-filter:blur(10px);

            box-shadow:
            0 8px 32px rgba(0,0,0,0.1);

            margin-bottom:30px;

        }



        .hero h1 {

            font-size:55px;

            font-weight:800;

            background:
            linear-gradient(
            90deg,
            #ff7b89,
            #59c3c3
            );

            -webkit-background-clip:text;

            color:transparent;

        }



        .hero p {

            font-size:20px;

            color:#444;

        }




        /* Feature cards */


        .card {

            background:

            rgba(255,255,255,0.55);

            padding:25px;

            border-radius:20px;

            text-align:center;

            height:150px;

            box-shadow:
            0 10px 25px rgba(0,0,0,0.08);

            transition:0.3s;

        }


        .card:hover {

            transform:translateY(-8px);

        }


        </style>
        """,
        unsafe_allow_html=True
    )

from frontend.components.navbar import show_navbar
from frontend.components.sidebar import student_sidebar


def student_dashboard():
    st.markdown(
        """
        <style>
    
        .stApp {
    
        background:#E5F9F2;
    
        }
    
    
        /* remove overlap */
    
        h1,h2,h3,p {
    
        font-family: "Arial";
    
        line-height:1.5;
    
        color:#163832;
    
        }
    
    
    
        .feature-card {
    
    
        background:white;
    
        padding:25px;
    
        border-radius:25px;
    
        box-shadow:
        0px 8px 25px rgba(0,0,0,0.08);
    
        text-align:center;
    
        }
    
    
    
        .chitti {
    
    
        background:#ff4b5c;
    
        color:white;
    
        padding:30px;
    
        border-radius:25px;
    
        font-weight:800;
    
        box-shadow:
        0px 8px 25px rgba(255,0,0,0.25);
    
        }
    
    
    
        .footer {
    
        text-align:center;
    
        margin-top:60px;
    
        font-size:18px;
    
        font-weight:700;
    
        color:#163832;
    
        }
    
    
        </style>
        """,
        unsafe_allow_html=True
    )
    load_css()

    user = st.session_state.get(
        "user",
        None
    )


    # User name handling
    if user:

        try:
            name = user[1]

        except:

            name = "Student"

    else:

        name = "Student"


    # Navbar
    show_navbar(
        name,
        "Student"
    )


    # Sidebar
    page = student_sidebar()



    # ==========================
    # HOME
    # ==========================

    if page == "🏠 Home":
        st.markdown(
            """
            <div class="hero">

            <h1>SAKHI</h1>

            <p>
            Smart Academic Knowledge & Help Interface
            </p>

            <p>
            Empowering students with AI-driven learning,
            safety and communication.
            </p>

            </div>
            """,
            unsafe_allow_html=True
        )

        col1, col2, col3 = st.columns(3)

        with col1:

            st.markdown(
                """
                <div class="card">

                🛡️

                <h3>
                Student Safety
                </h3>

                Anonymous complaint analysis

                </div>
                """,
                unsafe_allow_html=True
            )

        with col2:

            st.markdown(
                """
                <div class="card">

                🤖

                <h3>
                AI Learning Assistant
                </h3>

                Smart class material assistant

                </div>
                """,
                unsafe_allow_html=True
            )

        with col3:

            st.markdown(
                """
                <div class="card">

                🏆

                <h3>
                Rewards & Quiz
                </h3>

                Learn and earn points

                </div>
                """,
                unsafe_allow_html=True
            )


        st.title("🎓 Welcome to SAKHI")

        st.subheader(
            "Smart Academic Knowledge & Help Interface"
        )


        st.write(
            """
            SAKHI is an AI-powered student support platform
            designed to improve classroom communication,
            learning experience and student safety.
            """
        )


        col1,col2,col3 = st.columns(3)


        with col1:

            st.info(
                "🛡️ Anonymous Complaint System"
            )


        with col2:

            st.info(
                "🤖 AI Class Assistant"
            )


        with col3:

            st.info(
                "📝 AI Quiz & Rewards"
            )



    # ==========================
    # COMPLAINT CHATBOT
    # ==========================

    # ==========================

    # CHITTI COMPLAINT CHATBOT

    # ==========================

    elif page == "📮 CHITTI":

        st.markdown(

            """
    
            <div class="chitti">
    
    
            📮 CHITTI
    
    
            <br>
    
    
            Your Anonymous Student Voice Box
    
    
            </div>
    
            """,

            unsafe_allow_html=True

        )

        st.write(

            """
    
            CHITTI helps students safely share classroom concerns,
    
            harassment, ragging, teaching issues or any academic problems.
    
    
            Your identity remains protected.
    
            """

        )

        complaint = st.text_area(

            "Write your concern here..."

        )

        category = st.selectbox(

            "Select Issue Category",

            [

                "Teacher Behaviour",

                "Ragging",

                "Harassment",

                "Academic Issue",

                "Other"

            ]

        )

        if st.button("📨 Submit to CHITTI"):

            if complaint.strip() == "":

                st.warning(

                    "Please describe your issue."

                )



            else:

                # Demo AI Analysis

                keywords = [

                    "harass",

                    "rag",

                    "threat",

                    "abuse",

                    "problem"

                ]

                genuine = any(

                    word in complaint.lower()

                    for word in keywords

                )

                if genuine:

                    status = "Genuine Concern Detected"


                else:

                    status = "Needs Further Review"

                st.success(

                    "Complaint Submitted Successfully"

                )

                st.info(

                    f"""

                    AI Analysis Result:


                    Category:

                    {category}


                    Status:

                    {status}


                    Complaint securely stored for HOD review.

                    """

                )


        st.title(
            "🛡️ Student Complaint Assistant"
        )


        complaint = st.text_area(
            "Describe your issue anonymously"
        )


        if st.button("Submit Complaint"):


            st.success(
                "Your complaint has been analysed and securely recorded."
            )


            st.info(
                "AI Status: Genuine Concern Detected"
            )



    # ==========================
    # AI CLASS ASSISTANT
    # ==========================


    elif page == "🤖 Class Assistant":


        st.title(
            "🤖 SAKHI Class AI Assistant"
        )


        question = st.text_input(
            "Ask your class related question"
        )


        if st.button("Ask"):


            st.success(
                "AI Response:"
            )


            st.write(
                "Based on uploaded class material, this concept can be explained as..."
            )



    # ==========================
    # QUIZ
    # ==========================


    elif page == "📝 Quiz":


        st.title(
            "📝 AI Quiz System"
        )


        st.write(
            "Weekly AI generated quizzes with reward points."
        )


        answer = st.radio(
            "Python is a:",
            [
                "Programming Language",
                "Database",
                "Browser"
            ]
        )


        if st.button("Submit Quiz"):


            if answer=="Programming Language":

                st.success(
                    "Correct! +10 Points"
                )

            else:

                st.error(
                    "Wrong Answer"
                )



    # ==========================
    # FEEDBACK
    # ==========================


    elif page == "⭐ Feedback":


        st.title(
            "⭐ Class Feedback"
        )


        rating = st.slider(
            "Rate your class",
            1,
            5
        )


        feedback = st.text_area(
            "Write feedback"
        )


        if st.button("Submit Feedback"):

            st.success(
                "Feedback submitted successfully"
            )
