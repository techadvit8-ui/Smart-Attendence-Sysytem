import sqlite3
import os


class Database:

    def __init__(self):

        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

        db_path = os.path.join(BASE_DIR, "database", "attendance.db")

        self.conn = sqlite3.connect(db_path)

        self.cursor = self.conn.cursor()

        self.create_tables()


    def create_tables(self):

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS students(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            name TEXT NOT NULL,

            roll TEXT UNIQUE,

            class_name TEXT,

            section TEXT,

            mobile TEXT,

            email TEXT,

            image_path TEXT
        )
        """)

        self.conn.commit()


    # ---------------- ADD STUDENT ----------------

    def add_student(
            self,
            name,
            roll,
            class_name,
            section,
            mobile,
            email,
            image_path
        ):

        self.cursor.execute("""
        INSERT INTO students
        (name, roll, class_name, section, mobile, email, image_path)

        VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            name,
            roll,
            class_name,
            section,
            mobile,
            email,
            image_path
        ))

        self.conn.commit()



    # ---------------- GET ALL STUDENTS ----------------

    def get_students(self):

        self.cursor.execute("""
        SELECT * FROM students
        """)

        return self.cursor.fetchall()



    # ---------------- SEARCH STUDENT ----------------

    def search_student(self, roll):

        self.cursor.execute("""
        SELECT * FROM students
        WHERE roll=?
        """, (roll,))

        return self.cursor.fetchone()



    # ---------------- UPDATE STUDENT ----------------

    def update_student(
            self,
            name,
            roll,
            class_name,
            section,
            mobile,
            email
        ):

        self.cursor.execute("""
        UPDATE students

        SET

        name=?,
        class_name=?,
        section=?,
        mobile=?,
        email=?

        WHERE roll=?

        """, (
            name,
            class_name,
            section,
            mobile,
            email,
            roll
        ))

        self.conn.commit()



    # ---------------- DELETE STUDENT ----------------

    def delete_student(self, roll):

        self.cursor.execute("""
        DELETE FROM students
        WHERE roll=?
        """, (roll,))

        self.conn.commit()



    # ---------------- CLOSE DATABASE ----------------

    def close(self):

        self.conn.close()