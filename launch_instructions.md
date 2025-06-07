# How to Launch and Run Locally (Sprint 2)

## Prerequisites
- Python 3.8+
- [uv](https://github.com/astral-sh/uv) as Python package manager
- Azure Storage Account and Queue (for async processing)
- Gemini API access (for PDF summarization, placeholder in code)


## 1. Install dependencies

```
uv pip install --system
```

## 2. Configure environment variables and configuration parameters

Create the `.env` file with your Azure and Gemini credentials:

```
AZURE_QUEUE_CONNECTION_STRING="DefaultEndpointsProtocol=https;AccountName=sadkqueue;AccountKey=VsvnXXX;EndpointSuffix=core.windows.net"
GEMINI_API_KEY=AIxxxx
```
Do necessary changes in config.py if needed
## 3. Create DB by launching of  init.py 

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

- All configuration is in `.env` and `config.py`.
- Results are persisted in SQLite (`pdfs.db`).
