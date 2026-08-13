import sqlite3
from datetime import datetime
import os


class AttendanceManager:

    def __init__(self):

        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

        db_path = os.path.join(BASE_DIR, "database", "attendance.db")

        self.conn = sqlite3.connect(db_path)

        self.cursor = self.conn.cursor()

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS attendance(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            student_name TEXT,

            date TEXT,

            time TEXT
        )
        """)

        self.conn.commit()

    def mark_attendance(self, student):

        today = datetime.now().strftime("%Y-%m-%d")

        current_time = datetime.now().strftime("%H:%M:%S")

        self.cursor.execute(
            """
            SELECT * FROM attendance
            WHERE student_name=? AND date=?
            """,
            (student, today)
        )

        if self.cursor.fetchone():

            return False

        self.cursor.execute(
            """
            INSERT INTO attendance
            (student_name,date,time)

            VALUES(?,?,?)
            """,
            (student, today, current_time)
        )

        self.conn.commit()

        return True