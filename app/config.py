import os
from dotenv import load_dotenv

load_dotenv()

# Configuration values
STORAGE_ACCOUNT_NAME = 'sadkqueue'
QUEUE_NAME = 'queuepdfprocessing'
DB_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'pdfs.db'))
UPLOAD_DIR = 'uploads'
LLM_MODEL = "gemini-2.0-flash"
POLLING_INTERVAL = 2  # seconds - to avoid too frequent polling of azure queue

AZURE_QUEUE_CONNECTION_STRING = os.getenv("AZURE_QUEUE_CONNECTION_STRING")

