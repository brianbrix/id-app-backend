from fastapi import UploadFile
from pydantic import BaseModel


class DocumentBase(BaseModel):
    document_type: str
    id_number: str
    name_on_id: str
    location_of_issue: str
    contact: str
    location: str


class DocumentInput(DocumentBase):
    pass


class Document(DocumentBase):
    id: int
    id_front_filename: str
    id_back_filename: str
    id_front_content_type: str
    id_back_content_type: str

    class Config:
        orm_mode = True
