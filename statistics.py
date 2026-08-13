import sqlite3
import os


class Statistics:

    def __init__(self):

        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

        db = os.path.join(BASE_DIR, "database", "attendance.db")

        self.conn = sqlite3.connect(db)

        self.cursor = self.conn.cursor()

    def total_present(self):

        self.cursor.execute("""
        SELECT COUNT(*) FROM attendance
        WHERE date=date('now')
        """)

        return self.cursor.fetchone()[0]