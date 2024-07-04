from sqlalchemy.orm import Session

from app.model import document_model
from app.schema.document_schema import DocumentInput


def create_document(db: Session, document: DocumentInput):
    db_document = document_model.Document(**document.model_dump())
    db.add(db_document)
    db.commit()
    db.refresh(db_document)
    return db_document


def get_document(db: Session, document_id: int):
    return db.query(document_model.Document).filter(document_model.Document.id == document_id).first()


def get_documents(db: Session, skip: int = 0, limit: int = 10):
    return db.query(document_model.Document).offset(skip).limit(limit).all()
