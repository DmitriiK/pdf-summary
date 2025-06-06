
import logging
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse, FileResponse
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
import os
from azure.storage.queue import QueueClient
import config
import sqlite3

logging.basicConfig(level=logging.INFO)
app = FastAPI()

# Allow CORS for local frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

os.makedirs(config.UPLOAD_DIR, exist_ok=True)



@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are allowed.")
    file_path = os.path.join(config.UPLOAD_DIR, file.filename)
    with open(file_path, "wb") as f:
        f.write(await file.read())
    logging.info(f'adding of file {file_path} to the queue')
    queue_client = QueueClient.from_connection_string(
        config.AZURE_QUEUE_CONNECTION_STRING, config.QUEUE_NAME)
    queue_client.send_message(file_path)
    logging.info(f'Have added file {file_path} to the queue')
    return {"status": "queued", "file_name": file.filename, "upload_date": datetime.now()}

@app.get("/files")
def list_files():
    with sqlite3.connect(config.DB_PATH) as conn:
        rows = conn.execute("SELECT file_name, upload_date, summary FROM pdfs ORDER BY id DESC").fetchall()
    files = [
        {"file_name": r[0], "upload_date": r[1], "summary": r[2]} for r in rows
    ]
    return JSONResponse(content=files)

@app.get("/")
def root():
    return FileResponse("index.html")
