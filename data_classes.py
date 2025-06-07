from pydantic import BaseModel
from datetime import datetime

class MessageData(BaseModel):
    file_name: str
    file_path: str
    upload_date: datetime
