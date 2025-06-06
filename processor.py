import os
import sqlite3
from datetime import datetime
from azure.storage.queue import QueueClient
from google.generativeai import GenerativeModel
import config

UPLOAD_DIR = "uploads"
def init_db():
    with sqlite3.connect(config.DB_PATH) as conn:
        conn.execute('''CREATE TABLE IF NOT EXISTS pdfs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            file_name TEXT,
            upload_date TEXT,
            summary TEXT
        )''')


def process_queue():
    queue_client = QueueClient.from_connection_string(
        config.AZURE_QUEUE_CONNECTION_STRING, config.QUEUE_NAME)
    while True:
        messages = queue_client.receive_messages(messages_per_page=1)
        for msg_batch in messages.by_page():
            for msg in msg_batch:
                file_path = msg.content
                file_name = os.path.basename(file_path)
                # Summarize PDF using Gemini (placeholder)
                summary = summarize_pdf_with_gemini(file_path)
                upload_date = datetime.now().isoformat()
                with sqlite3.connect(config.DB_PATH) as conn:
                    conn.execute(
                        "INSERT OR REPLACE INTO pdfs (file_name, upload_date, summary) VALUES (?, ?, ?)",
                        (file_name, upload_date, summary)
                    )
                queue_client.delete_message(msg)
        # Sleep or break for demo; in production, use time.sleep()
        break

def summarize_pdf_with_gemini(file_path):
    # Placeholder for Gemini API call
    # model = GenerativeModel(token=config.GEMINI_TOKEN)
    # summary = model.summarize_pdf(file_path)
    # return summary
    return f"Summary for {os.path.basename(file_path)} (Gemini placeholder)"

if __name__ == "__main__":
    init_db()
    process_queue()
