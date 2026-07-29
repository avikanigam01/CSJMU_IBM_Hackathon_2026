import sqlite3
import os


# Database location
DB_PATH = "database/sakhi.db"


def connect_db():

    conn = sqlite3.connect(DB_PATH)

    return conn



def create_tables():

    # Create database folder if missing
    os.makedirs(
        "database",
        exist_ok=True
    )


    conn = connect_db()

    cursor = conn.cursor()


    # ==========================
    # STUDENTS TABLE
    # ==========================

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        name TEXT NOT NULL,

        email TEXT UNIQUE NOT NULL,

        password TEXT NOT NULL,

        department TEXT,

        year INTEGER

    )
    """)


    # ==========================
    # TEACHERS TABLE
    # ==========================

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS teachers(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        name TEXT NOT NULL,

        email TEXT UNIQUE NOT NULL,

        password TEXT NOT NULL,

        subject TEXT

    )
    """)


    # ==========================
    # HOD TABLE
    # ==========================

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS hod(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        name TEXT NOT NULL,

        email TEXT UNIQUE NOT NULL,

        password TEXT NOT NULL,

        department TEXT

    )
    """)


    # ==========================
    # COMPLAINT TABLE
    # ==========================

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS complaints(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        student_id INTEGER,

        complaint TEXT,

        category TEXT,

        severity TEXT,

        status TEXT DEFAULT 'Pending',

        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

    )
    """)


    # ==========================
    # FEEDBACK TABLE
    # ==========================

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS feedback(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        student_id INTEGER,

        teacher TEXT,

        subject TEXT,

        rating INTEGER,

        feedback TEXT,

        sentiment TEXT

    )
    """)


    # ==========================
    # CLASS NOTES TABLE
    # ==========================

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS notes(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        teacher_id INTEGER,

        subject TEXT,

        filename TEXT,

        content TEXT

    )
    """)


    # ==========================
    # QUIZ TABLE
    # ==========================

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS quizzes(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        subject TEXT,

        question TEXT,

        option1 TEXT,

        option2 TEXT,

        option3 TEXT,

        option4 TEXT,

        answer TEXT

    )
    """)


    # ==========================
    # SCORES TABLE
    # ==========================

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS scores(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        student_id INTEGER,

        quiz_id INTEGER,

        score INTEGER,

        points INTEGER

    )
    """)


    conn.commit()

    conn.close()


    print("✅ Database and Tables Created Successfully")



if __name__ == "__main__":

    create_tables()