from pydantic import BaseModel

class MessageData(BaseModel):
    file_name: str
    file_path: str
    upload_date: str # ISO format string, we have some issues with datetime serialization 
