from pydantic import BaseModel


class DocumentBase(BaseModel):
    document_type: str
    id_number: str
    name_on_id: str
    location_of_issue: str
    contact: str
    location: str
    id_front_image: str
    id_back_image: str


class DocumentInput(DocumentBase):
    pass


class Document(DocumentBase):
    id: int

    class Config:
        orm_mode = True
