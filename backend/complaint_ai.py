import sqlite3

DB_PATH = "database/sakhi.db"

# -------------------------------
# Complaint Categories
# -------------------------------

CATEGORIES = {
    "Harassment": [
        "harassment",
        "abuse",
        "threat",
        "insult",
        "humiliate",
        "misbehave"
    ],

    "Ragging": [
        "ragging",
        "senior",
        "bully",
        "forced",
        "teasing"
    ],

    "Academic": [
        "marks",
        "attendance",
        "assignment",
        "exam",
        "teacher",
        "lecture",
        "class"
    ],

    "Infrastructure": [
        "fan",
        "light",
        "bench",
        "wifi",
        "computer",
        "projector",
        "lab"
    ]
}


# -------------------------------
# Analyze Complaint
# -------------------------------

def analyze_complaint(text):

    text = text.lower()

    category = "General"

    severity = "Low"

    confidence = 60

    sentiment = "Neutral"

    for key, words in CATEGORIES.items():

        for word in words:

            if word in text:

                category = key

                confidence = 90

                break

    if any(word in text for word in
           ["harassment","abuse","ragging","threat","bully"]):

        severity = "High"

        sentiment = "Negative"

    elif any(word in text for word in
             ["marks","attendance","assignment","teacher"]):

        severity = "Medium"

        sentiment = "Negative"

    elif any(word in text for word in
             ["fan","wifi","light","bench"]):

        severity = "Low"

        sentiment = "Neutral"

    return {

        "category": category,

        "severity": severity,

        "confidence": confidence,

        "sentiment": sentiment

    }


# -------------------------------
# Save Complaint
# -------------------------------

def save_complaint(student_id, complaint):

    result = analyze_complaint(complaint)

    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    cursor.execute("""

    INSERT INTO complaints

    (student_id,
     complaint,
     category,
     sentiment,
     severity,
     confidence)

    VALUES(?,?,?,?,?,?)

    """,

    (

        student_id,

        complaint,

        result["category"],

        result["sentiment"],

        result["severity"],

        result["confidence"]

    ))

    conn.commit()

    conn.close()

    return result


# -------------------------------
# Get All Complaints
# -------------------------------

def get_all_complaints():

    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM complaints")

    data = cursor.fetchall()

    conn.close()

    return data


# -------------------------------
# Get High Priority Complaints
# -------------------------------

def get_high_priority():

    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    cursor.execute("""

    SELECT *

    FROM complaints

    WHERE severity='High'

    """)

    data = cursor.fetchall()

    conn.close()

    return data