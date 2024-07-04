# app/database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base
from sqlalchemy.orm import sessionmaker
import os

# Database URL (adjust as needed)
SQLALCHEMY_DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql+psycopg2://id_app_user:123@localhost:5433/id_app')

# Create the database engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a base class for our models
Base: DeclarativeMeta = declarative_base()
