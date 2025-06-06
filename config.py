import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configuration values
STORAGE_ACCOUNT_NAME = 'sadkqueue'
QUEUE_NAME = 'queuepdfprocessing'
DB_PATH='pdfs.db'
UPLOAD_DIR = 'uploads'

AZURE_QUEUE_CONNECTION_STRING = os.getenv("AZURE_QUEUE_CONNECTION_STRING")
GEMINI_TOKEN = os.getenv("GEMINI_TOKEN")
