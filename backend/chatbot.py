import sqlite3

DB_PATH = "database/sakhi.db"


# ---------------------------------------
# Get Notes from Database
# ---------------------------------------

def get_notes(subject):

    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    cursor.execute("""

    SELECT extracted_text

    FROM uploaded_notes

    WHERE subject=?

    """, (subject,))

    rows = cursor.fetchall()

    conn.close()

    notes = ""

    for row in rows:
        notes += row[0] + "\n"

    return notes


# ---------------------------------------
# Split Notes into Paragraphs
# ---------------------------------------

def split_notes(text):

    paragraphs = text.split("\n")

    cleaned = []

    for para in paragraphs:

        para = para.strip()

        if len(para) > 15:
            cleaned.append(para)

    return cleaned


# ---------------------------------------
# Find Best Answer
# ---------------------------------------

def search_answer(question, subject):

    notes = get_notes(subject)

    if notes == "":
        return "No notes have been uploaded for this subject."

    paragraphs = split_notes(notes)

    question = question.lower()

    best_match = ""

    highest_score = 0

    keywords = question.split()

    for para in paragraphs:

        score = 0

        lower_para = para.lower()

        for word in keywords:

            if word in lower_para:
                score += 1

        if score > highest_score:

            highest_score = score

            best_match = para

    if highest_score == 0:

        return ("Sorry! I couldn't find this answer "
                "in the uploaded lecture notes.")

    return best_match


# ---------------------------------------
# Chatbot Function
# ---------------------------------------

def ask_question(question, subject):

    answer = search_answer(question, subject)

    return {

        "question": question,

        "subject": subject,

        "answer": answer

    }