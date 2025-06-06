import os
import pathlib
from datetime import datetime

import sqlite3
from dotenv import load_dotenv

from azure.storage.queue import QueueClient
from google import genai
from google.genai import types

import config
load_dotenv()

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
                # TODO use hash sums to avoid processing of the same file been uploaded twice
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
    client = genai.Client()
    file_path = pathlib.Path(file_path)
    # Upload the PDF using the File API
    sample_file = client.files.upload(
    file=file_path,
    )
    response = client.models.generate_content(
    model=config.LLM_MODEL,
    contents=[sample_file, "Summarize this document"])
    return response.text

if __name__ == "__main__":
    init_db()
    process_queue()
