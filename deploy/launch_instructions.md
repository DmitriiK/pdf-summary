

## Prerequisites
- Python 3.12+
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
## 3. Create DB by launching of  deploy/init.py
python -m deploy.init
## 4. Start the FastAPI backend and processor (queue consumer)

Run the following script to start both the FastAPI backend and the processor in separate Terminal windows:

```
./run_all.sh
```

- The app will be available at http://127.0.0.1:8000 for local development (or by external ip address)
- The default page (index.html) will open at the root URL

## 5. Open the web UI

Go to http://127.0.0.1:8000 in your browser (or by external ip address).

## Notes

- All configuration is in `.env` and `config.py`.
- Results are persisted in SQLite (`pdfs.db`).
- for remote deployment on cloud VM neeed to add inbound allow rule for TCP 8000 port