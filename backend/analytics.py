import sqlite3

DB_PATH = "database/sakhi.db"


# ----------------------------------
# Connect Database
# ----------------------------------

def connect_db():
    return sqlite3.connect(DB_PATH)


# ----------------------------------
# Dashboard Analytics
# ----------------------------------

def dashboard_statistics():

    conn = connect_db()
    cursor = conn.cursor()

    # Total Students
    cursor.execute("SELECT COUNT(*) FROM students")
    total_students = cursor.fetchone()[0]

    # Total Teachers
    cursor.execute("SELECT COUNT(*) FROM teachers")
    total_teachers = cursor.fetchone()[0]

    # Total Complaints
    cursor.execute("SELECT COUNT(*) FROM complaints")
    total_complaints = cursor.fetchone()[0]

    # Total Feedback
    cursor.execute("SELECT COUNT(*) FROM feedback")
    total_feedback = cursor.fetchone()[0]

    # Total Notes Uploaded
    cursor.execute("SELECT COUNT(*) FROM uploaded_notes")
    total_notes = cursor.fetchone()[0]

    # Average Quiz Score
    cursor.execute("SELECT AVG(score) FROM quiz_scores")
    average_score = cursor.fetchone()[0]

    if average_score is None:
        average_score = 0

    conn.close()

    return {

        "students": total_students,

        "teachers": total_teachers,

        "complaints": total_complaints,

        "feedback": total_feedback,

        "notes": total_notes,

        "average_score": round(average_score,2)

    }


# ----------------------------------
# Complaint Category Analysis
# ----------------------------------

def complaint_statistics():

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""

    SELECT category,
           COUNT(*)

    FROM complaints

    GROUP BY category

    """)

    data = cursor.fetchall()

    conn.close()

    result = {}

    for category,count in data:

        result[category] = count

    return result


# ----------------------------------
# Feedback Analysis
# ----------------------------------

def feedback_statistics():

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""

    SELECT sentiment,
           COUNT(*)

    FROM feedback

    GROUP BY sentiment

    """)

    data = cursor.fetchall()

    conn.close()

    result = {

        "Positive":0,

        "Negative":0,

        "Neutral":0

    }

    for sentiment,count in data:

        result[sentiment] = count

    return result


# ----------------------------------
# Subject Wise Quiz Performance
# ----------------------------------

def quiz_statistics():

    conn = connect_db()

    cursor = conn.cursor()

    cursor.execute("""

    SELECT subject,
           AVG(score)

    FROM quiz_scores

    GROUP BY subject

    """)

    data = cursor.fetchall()

    conn.close()

    result = {}

    for subject,avg in data:

        result[subject] = round(avg,2)

    return result


# ----------------------------------
# Top 5 Students
# ----------------------------------

def top_students():

    conn = connect_db()

    cursor = conn.cursor()

    cursor.execute("""

    SELECT students.name,
           leaderboard.points

    FROM leaderboard

    JOIN students

    ON students.id=leaderboard.student_id

    ORDER BY leaderboard.points DESC

    LIMIT 5

    """)

    data = cursor.fetchall()

    conn.close()

    return data


# ----------------------------------
# Recent Complaints
# ----------------------------------

def latest_complaints(limit=5):

    conn = connect_db()

    cursor = conn.cursor()

    cursor.execute("""

    SELECT complaint,
           category,
           severity

    FROM complaints

    ORDER BY id DESC

    LIMIT ?

    """,(limit,))

    data = cursor.fetchall()

    conn.close()

    return data