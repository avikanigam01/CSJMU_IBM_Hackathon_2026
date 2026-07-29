import PyPDF2
import sqlite3


DB_PATH = "database/sakhi.db"



def extract_text_from_pdf(uploaded_file):

    reader = PyPDF2.PdfReader(uploaded_file)

    text = ""

    for page in reader.pages:

        text += page.extract_text()


    return text



def save_notes(teacher_id, subject, filename, content):

    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()


    cursor.execute(
        """
        INSERT INTO notes
        (teacher_id, subject, filename, content)

        VALUES(?,?,?,?)
        """,
        (
            teacher_id,
            subject,
            filename,
            content
        )
    )


    conn.commit()

    conn.close()


    return True