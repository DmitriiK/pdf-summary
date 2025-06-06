# How to Launch and Run Locally (Sprint 2)

## Prerequisites
- Python 3.8+
- [uv](https://github.com/astral-sh/uv) as Python package manager
- Azure Storage Account and Queue (for async processing)
- Gemini API access (for PDF summarization, placeholder in code)

## 1. Clone the repository and enter the project directory

```
git clone <your-repo-url>
cd pdf-summary
```

## 2. Install dependencies

```
uv pip install --system
```

## 3. Configure environment variables

Edit the `.env` file with your Azure and Gemini credentials:

```
AZURE_QUEUE_CONNECTION_STRING=your_connection_string
GEMINI_TOKEN=your_gemini_token
DB_PATH=pdfs.db
STORAGE_ACCOUNT_NAME=your_storage_account
QUEUE_NAME=your_queue_name
```

## 4. Start the FastAPI backend

```
uvicorn backend:app --reload
```
- The app will be available at http://127.0.0.1:8000
- The default page (index.html) will open at the root URL

## 5. Open the web UI

Go to http://127.0.0.1:8000 in your browser.

## 6. Start the processor (queue consumer)

In a separate terminal:

```
python processor.py
```
This will process messages from the Azure Queue, summarize PDFs (placeholder), and update the database.

## Notes
- The Gemini summarization is a placeholder. Integrate the real API as needed.
- All configuration is in `.env` and `config.py`.
- Uploaded PDFs are stored in the `uploads/` directory.
- Results are persisted in SQLite (`pdfs.db`).
