import sqlite3

from app import config

def init_db():
    with sqlite3.connect(config.DB_PATH) as conn:
        conn.execute('''CREATE TABLE IF NOT EXISTS pdfs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            file_name TEXT UNIQUE,
            upload_date TEXT,
            processed_date TEXT,
            summary TEXT
        )''')
    print(f"Database {config.DB_PATH} initialized with table 'pdfs'.")

def delete_all():
    with sqlite3.connect(config.DB_PATH) as conn:
        conn.execute('''DELETE FROM pdfs''')
    print("All records deleted from the 'pdfs' table.")

if __name__ == "__main__":
    init_db()
    # delete_all()

