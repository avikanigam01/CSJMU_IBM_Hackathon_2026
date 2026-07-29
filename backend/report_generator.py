import sqlite3
import os
from datetime import datetime

DB_PATH = "database/sakhi.db"
REPORT_FOLDER = "uploads/reports"

os.makedirs(REPORT_FOLDER, exist_ok=True)


# --------------------------------------
# Connect Database
# --------------------------------------

def connect_db():
    return sqlite3.connect(DB_PATH)


# --------------------------------------
# Generate Monthly Report
# --------------------------------------

def generate_report():

    conn = connect_db()
    cursor = conn.cursor()

    # ---------------- Complaints ----------------

    cursor.execute("SELECT COUNT(*) FROM complaints")
    total_complaints = cursor.fetchone()[0]

    cursor.execute("""
    SELECT COUNT(*)
    FROM complaints
    WHERE severity='High'
    """)
    high_priority = cursor.fetchone()[0]

    # ---------------- Feedback ----------------

    cursor.execute("SELECT COUNT(*) FROM feedback")
    total_feedback = cursor.fetchone()[0]

    cursor.execute("""
    SELECT sentiment,
           COUNT(*)
    FROM feedback
    GROUP BY sentiment
    """)

    sentiments = cursor.fetchall()

    # ---------------- Quiz ----------------

    cursor.execute("""
    SELECT AVG(score)
    FROM quiz_scores
    """)

    avg_score = cursor.fetchone()[0]

    if avg_score is None:
        avg_score = 0

    # ---------------- Leaderboard ----------------

    cursor.execute("""

    SELECT students.name,
           leaderboard.points

    FROM leaderboard

    JOIN students

    ON students.id = leaderboard.student_id

    ORDER BY leaderboard.points DESC

    LIMIT 3

    """)

    top_students = cursor.fetchall()

    conn.close()

    # ---------------- Create Report ----------------

    report = f"""
===============================
      SAKHI MONTHLY REPORT
===============================

Date : {datetime.now().strftime('%d-%m-%Y')}

--------------------------------
COMPLAINT ANALYSIS
--------------------------------

Total Complaints : {total_complaints}

High Priority Complaints : {high_priority}

--------------------------------
FEEDBACK ANALYSIS
--------------------------------

Total Feedback : {total_feedback}

"""

    for item in sentiments:

        report += f"{item[0]} : {item[1]}\n"

    report += f"""

--------------------------------
QUIZ PERFORMANCE
--------------------------------

Average Quiz Score : {avg_score:.2f}

--------------------------------
TOP 3 STUDENTS
--------------------------------

"""

    for student in top_students:

        report += f"{student[0]}  --->  {student[1]} Points\n"

    filename = f"Monthly_Report_{datetime.now().strftime('%d_%m_%Y')}.txt"

    filepath = os.path.join(REPORT_FOLDER, filename)

    with open(filepath, "w", encoding="utf-8") as file:

        file.write(report)

    # Save report entry

    conn = connect_db()

    cursor = conn.cursor()

    cursor.execute("""

    INSERT INTO reports

    (report_name,
     report_type)

    VALUES(?,?)

    """,

    (

        filename,

        "Monthly"

    ))

    conn.commit()

    conn.close()

    return filepath