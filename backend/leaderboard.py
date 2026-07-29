import sqlite3

DB_PATH = "database/sakhi.db"


# ------------------------------------
# Connect Database
# ------------------------------------

def connect_db():
    return sqlite3.connect(DB_PATH)


# ------------------------------------
# Update Leaderboard
# ------------------------------------

def update_leaderboard(student_id):

    conn = connect_db()
    cursor = conn.cursor()

    # Get total score of student
    cursor.execute("""
    SELECT SUM(score)
    FROM quiz_scores
    WHERE student_id=?
    """, (student_id,))

    total = cursor.fetchone()[0]

    if total is None:
        total = 0

    # Check if already exists
    cursor.execute("""
    SELECT *
    FROM leaderboard
    WHERE student_id=?
    """, (student_id,))

    existing = cursor.fetchone()

    if existing:

        cursor.execute("""
        UPDATE leaderboard
        SET points=?
        WHERE student_id=?
        """, (total, student_id))

    else:

        cursor.execute("""
        INSERT INTO leaderboard
        (student_id, points)
        VALUES(?,?)
        """, (student_id, total))

    conn.commit()
    conn.close()


# ------------------------------------
# Get Top 3 Students
# ------------------------------------

def get_top_students():

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""

    SELECT students.name,
           leaderboard.points

    FROM leaderboard

    JOIN students

    ON leaderboard.student_id = students.id

    ORDER BY leaderboard.points DESC

    LIMIT 3

    """)

    top_students = cursor.fetchall()

    conn.close()

    return top_students


# ------------------------------------
# Get Full Leaderboard
# ------------------------------------

def get_leaderboard():

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""

    SELECT students.name,
           leaderboard.points

    FROM leaderboard

    JOIN students

    ON leaderboard.student_id = students.id

    ORDER BY leaderboard.points DESC

    """)

    leaderboard = cursor.fetchall()

    conn.close()

    return leaderboard