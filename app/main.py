import json

from fastapi import FastAPI, Depends, HTTPException, UploadFile, File
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


@app.post("/document/create", response_model=document_schema.Document)
async def create_document(document: document_schema.DocumentInput, id_front_file: UploadFile = File(...),
                          id_back_file: UploadFile = File(...),
                          db: Session = Depends(get_db)):
    id_front_file_data = await id_front_file.read()
    id_back_file_data = await id_back_file.read()
    document_data = json.loads(document)
    print(document_data)
    document_create = document_schema.DocumentInput(**document_data)

    return services.create_document(document=document_create,
                                    id_front_filename=id_front_file.filename,
                                    id_back_filename=id_back_file.filename,
                                    id_front_content_type=id_front_file.content_type,
                                    id_back_content_type=id_back_file.content_type,
                                    id_front_file_data=id_front_file_data,
                                    id_back_file_data=id_back_file_data, db=db)


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
