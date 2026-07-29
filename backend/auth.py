import sqlite3
import hashlib

DB_PATH = "database/sakhi.db"


def connect_db():
    conn = sqlite3.connect(DB_PATH)
    return conn


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def register_student(name, email, password, department, year):

    conn = connect_db()
    cursor = conn.cursor()

    try:
        cursor.execute("""
        INSERT INTO students
        (name,email,password,department,year)
        VALUES(?,?,?,?,?)
        """,
        (
            name,
            email,
            hash_password(password),
            department,
            year
        ))

        conn.commit()

        return True,"Student Registered Successfully"

    except sqlite3.IntegrityError:
        return False,"Email Already Exists"

    finally:
        conn.close()


def register_teacher(name,email,password,subject):

    conn = connect_db()
    cursor = conn.cursor()

    try:

        cursor.execute("""
        INSERT INTO teachers
        (name,email,password,subject)
        VALUES(?,?,?,?)
        """,
        (
            name,
            email,
            hash_password(password),
            subject
        ))

        conn.commit()

        return True,"Teacher Registered Successfully"

    except sqlite3.IntegrityError:

        return False,"Email Already Exists"

    finally:
        conn.close()


def register_hod(name,email,password,department):

    conn = connect_db()
    cursor = conn.cursor()

    try:

        cursor.execute("""
        INSERT INTO hod
        (name,email,password,department)
        VALUES(?,?,?,?)
        """,
        (
            name,
            email,
            hash_password(password),
            department
        ))

        conn.commit()

        return True,"HOD Registered Successfully"

    except sqlite3.IntegrityError:

        return False,"Email Already Exists"

    finally:
        conn.close()


def login(email,password,role):

    conn = connect_db()

    cursor = conn.cursor()

    password = hash_password(password)

    if role=="Student":
        table="students"

    elif role=="Teacher":
        table="teachers"

    elif role=="HOD":
        table="hod"

    else:
        conn.close()
        return False,None


    cursor.execute(
        f"SELECT * FROM {table} WHERE email=? AND password=?",
        (email,password)
    )

    user = cursor.fetchone()

    conn.close()


    if user:
        return True,user

    return False,None