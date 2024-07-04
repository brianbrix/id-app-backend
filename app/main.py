# app/main.py
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import engine, SessionLocal
from app.model import document_model
from app.schema import document_schema
from app.service import services

document_model.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/heart")
def heart():
    return {"message": "Heartbeat is okay"}


@app.post("/documents/", response_model=document_schema.Document)
def create_document(document: document_schema.DocumentInput, db: Session = Depends(get_db)):
    return services.create_document(db=db, document=document)


@app.get("/documents/{document_id}", response_model=document_schema.Document)
def read_document(document_id: int, db: Session = Depends(get_db)):
    db_document = services.get_document(db, document_id=document_id)
    if db_document is None:
        raise HTTPException(status_code=404, detail="Document not found")
    return db_document


@app.get("/documents/", response_model=list[document_schema.Document])
def read_documents(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    documents = services.get_documents(db, skip=skip, limit=limit)
    return documents
