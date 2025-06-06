import os
from dotenv import load_dotenv

load_dotenv()

# Configuration values
STORAGE_ACCOUNT_NAME = 'sadkqueue'
QUEUE_NAME = 'queuepdfprocessing'
DB_PATH='pdfs.db'
UPLOAD_DIR = 'uploads'
LLM_MODEL = "gemini-2.0-flash"

AZURE_QUEUE_CONNECTION_STRING = os.getenv("AZURE_QUEUE_CONNECTION_STRING")

