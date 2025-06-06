from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse, FileResponse
from fastapi.middleware.cors import CORSMiddleware
import sqlite3
from datetime import datetime
import os

app = FastAPI()

# Allow CORS for local frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

DB_PATH = "pdfs.db"
UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute('''CREATE TABLE IF NOT EXISTS pdfs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            file_name TEXT,
            upload_date TEXT,
            summary TEXT
        )''')

init_db()

@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are allowed.")
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_path, "wb") as f:
        f.write(await file.read())
    summary = f"Summary for {file.filename}"  # Placeholder summary
    upload_date = datetime.now().isoformat()
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute(
            "INSERT INTO pdfs (file_name, upload_date, summary) VALUES (?, ?, ?)",
            (file.filename, upload_date, summary)
        )
    return {"status": "success", "file_name": file.filename}

@app.get("/files")
def list_files():
    with sqlite3.connect(DB_PATH) as conn:
        rows = conn.execute("SELECT file_name, upload_date, summary FROM pdfs ORDER BY id DESC").fetchall()
    files = [
        {"file_name": r[0], "upload_date": r[1], "summary": r[2]} for r in rows
    ]
    return JSONResponse(content=files)

@app.get("/")
def root():
    return FileResponse("index.html")
