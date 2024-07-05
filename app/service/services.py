from sqlalchemy.orm import Session

from app.model import document_model
from app.model.document_model import Document
from app.schema import document_schema
from app.schema.document_schema import DocumentInput


def create_document(document: document_schema.DocumentInput, id_front_filename: str,
                    id_back_filename: str,
                    id_front_content_type: str,
                    id_back_content_type: str, id_front_file_data: bytes, id_back_file_data: bytes,
                    db: Session):
    db_document = document_schema.Document(
        **document.model_dump(),
        id_front_filename=id_front_filename,
        id_back_filename=id_back_filename,
        id_front_content_type=id_front_content_type,
        id_back_content_type=id_back_content_type,
        id_front_image=id_front_file_data,
        id_back_image=id_back_file_data
    )
    db.add(db_document)
    db.commit()
    db.refresh(db_document)
    return db_document


def get_document(db: Session, document_id: int):
    return db.query(document_model.Document).filter(document_model.Document.id == document_id).first()


def get_documents(db: Session, skip: int = 0, limit: int = 10):
    return db.query(document_model.Document).offset(skip).limit(limit).all()
