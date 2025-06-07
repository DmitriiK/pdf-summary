import sqlite3

import config

def init_db():
    with sqlite3.connect(config.DB_PATH) as conn:
        conn.execute('''CREATE TABLE IF NOT EXISTS pdfs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            file_name TEXT,
            upload_date TEXT,
            processed_date TEXT,   -- looks like SQLite does not have type for dates     
            summary TEXT
        )''')


if __name__ == "__main__":
    init_db()

