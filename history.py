import sqlite3
import os


class AttendanceHistory:

    def __init__(self):

        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

        db = os.path.join(BASE_DIR, "database", "attendance.db")

        self.conn = sqlite3.connect(db)

        self.cursor = self.conn.cursor()

    def get_today(self):

        self.cursor.execute("""
        SELECT student_name, time
        FROM attendance
        WHERE date = date('now')
        ORDER BY time ASC
        """)

        return self.cursor.fetchall()