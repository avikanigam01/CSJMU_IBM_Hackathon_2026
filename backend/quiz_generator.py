import sqlite3
import random

DB_PATH = "database/sakhi.db"


# ------------------------------------
# Database Connection
# ------------------------------------

def connect_db():
    return sqlite3.connect(DB_PATH)


# ------------------------------------
# Generate Quiz from Notes
# ------------------------------------

def generate_quiz(subject):

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT extracted_text
    FROM uploaded_notes
    WHERE subject=?
    """, (subject,))

    rows = cursor.fetchall()

    if not rows:
        conn.close()
        return []

    text = ""

    for row in rows:
        text += row[0] + "\n"

    lines = text.split("\n")

    questions = []

    for line in lines:

        line = line.strip()

        if len(line) < 25:
            continue

        words = line.split()

        if len(words) < 6:
            continue

        answer = words[0]

        question = line.replace(answer, "______", 1)

        option_a = answer
        option_b = "None"
        option_c = "All"
        option_d = "Both"

        questions.append({

            "question": question,

            "a": option_a,

            "b": option_b,

            "c": option_c,

            "d": option_d,

            "answer": option_a

        })

    conn.close()

    return questions


# ------------------------------------
# Save Quiz
# ------------------------------------

def save_quiz(subject):

    quiz = generate_quiz(subject)

    conn = connect_db()

    cursor = conn.cursor()

    for q in quiz:

        cursor.execute("""

        INSERT INTO quizzes

        (subject,
        question,
        option_a,
        option_b,
        option_c,
        option_d,
        answer)

        VALUES(?,?,?,?,?,?,?)

        """,

        (

            subject,

            q["question"],

            q["a"],

            q["b"],

            q["c"],

            q["d"],

            q["answer"]

        ))

    conn.commit()

    conn.close()

    return len(quiz)


# ------------------------------------
# Get Quiz
# ------------------------------------

def get_quiz(subject):

    conn = connect_db()

    cursor = conn.cursor()

    cursor.execute("""

    SELECT *

    FROM quizzes

    WHERE subject=?

    """,(subject,))

    quiz = cursor.fetchall()

    conn.close()

    return quiz


# ------------------------------------
# Calculate Score
# ------------------------------------

def calculate_score(student_answers, quiz):

    score = 0

    for i in range(len(quiz)):

        if student_answers[i] == quiz[i][7]:

            score += 1

    return score


# ------------------------------------
# Save Student Score
# ------------------------------------

def save_score(student_id,
               subject,
               score,
               total):

    conn = connect_db()

    cursor = conn.cursor()

    cursor.execute("""

    INSERT INTO quiz_scores

    (student_id,
     subject,
     score,
     total)

    VALUES(?,?,?,?)

    """,

    (

        student_id,

        subject,

        score,

        total

    ))

    conn.commit()

    conn.close()