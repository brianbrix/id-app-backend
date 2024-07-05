from sqlalchemy import Column, Integer, String, Text, LargeBinary

from app.database import Base


class Document(Base):
    __tablename__ = 'documents'

    id = Column(Integer, primary_key=True, index=True)
    document_type = Column(String, index=True)
    id_number = Column(String, unique=True, index=True)
    name_on_id = Column(String)
    location_of_issue = Column(String)
    contact = Column(String)
    location = Column(String)
    id_front_image = Column(LargeBinary)
    id_back_image = Column(LargeBinary)
