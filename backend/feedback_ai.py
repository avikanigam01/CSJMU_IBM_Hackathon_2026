import sqlite3

DB_PATH = "database/sakhi.db"


# ---------------------------------
# Analyze Feedback
# ---------------------------------

def analyze_feedback(feedback):

    feedback = feedback.lower()

    positive_words = [
        "good",
        "excellent",
        "amazing",
        "clear",
        "helpful",
        "best",
        "easy",
        "interesting",
        "understand"
    ]

    negative_words = [
        "bad",
        "boring",
        "fast",
        "confusing",
        "poor",
        "worst",
        "difficult",
        "hard",
        "slow"
    ]

    score = 0

    for word in positive_words:
        if word in feedback:
            score += 1

    for word in negative_words:
        if word in feedback:
            score -= 1

    if score > 0:
        sentiment = "Positive"

    elif score < 0:
        sentiment = "Negative"

    else:
        sentiment = "Neutral"

    return sentiment


# ---------------------------------
# Save Feedback
# ---------------------------------

def save_feedback(student_id,
                  teacher_name,
                  subject,
                  rating,
                  feedback):

    sentiment = analyze_feedback(feedback)

    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    cursor.execute("""

    INSERT INTO feedback

    (student_id,
     teacher_name,
     subject,
     rating,
     feedback,
     sentiment)

    VALUES(?,?,?,?,?,?)

    """,

    (

        student_id,

        teacher_name,

        subject,

        rating,

        feedback,

        sentiment

    ))

    conn.commit()

    conn.close()

    return sentiment


# ---------------------------------
# Get All Feedback
# ---------------------------------

def get_feedback():

    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    cursor.execute("""

    SELECT *

    FROM feedback

    """)

    data = cursor.fetchall()

    conn.close()

    return data


# ---------------------------------
# Generate AI Summary
# ---------------------------------

def generate_summary():

    feedbacks = get_feedback()

    positive = 0
    negative = 0
    neutral = 0

    for row in feedbacks:

        sentiment = row[6]

        if sentiment == "Positive":
            positive += 1

        elif sentiment == "Negative":
            negative += 1

        else:
            neutral += 1

    total = positive + negative + neutral

    if total == 0:
        return "No feedback available."

    summary = f"""
Total Feedback : {total}

Positive : {positive}

Negative : {negative}

Neutral : {neutral}

Overall Analysis:

Most students are giving
{"Positive" if positive>=negative else "Negative"} feedback.
"""

    return summary