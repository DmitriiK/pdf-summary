import pathlib
import datetime
import time

from dotenv import load_dotenv
import sqlite3
from azure.storage.queue import QueueClient
from google import genai

import config
from data_classes import MessageData
load_dotenv()

def process_queue():
    queue_client = QueueClient.from_connection_string(
        config.AZURE_QUEUE_CONNECTION_STRING, config.QUEUE_NAME)
    print('Queue client created, starting to process messages')
    while True:
        messages = queue_client.receive_messages(messages_per_page=1)
        for msg_batch in messages.by_page():
            for msg in msg_batch:
                message_data = MessageData.model_validate_json(msg.content)
                file_path = message_data.file_path
                file_name = message_data.file_name
                # TODO use hash sums to avoid processing of the same file been uploaded twice
                summary = summarize_pdf_with_gemini(file_path)
                upload_date = message_data.upload_date.isoformat()
                procecessing_date = datetime.datetime.now().isoformat()
                with sqlite3.connect(config.DB_PATH) as conn:
                    conn.execute(
                        "INSERT OR REPLACE INTO pdfs (file_name, upload_date, processed_date, summary) VALUES (?, ?, ?, ?)",
                        (file_name, upload_date, procecessing_date, summary)
                    )
                    print('message processed and saved to the database')
            time.sleep(config.POLLING_INTERVAL)

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
    process_queue()
