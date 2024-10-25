from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

HOST=os.getenv("HOST")
PASSWORD=os.getenv("PASSWORD")
DBNAME=os.getenv("DBNAME")
USER=os.getenv("USER")

DATABASE_URL = f"postgresql://{USER}:{PASSWORD}@{HOST}/{DBNAME}"

engine = create_engine(DATABASE_URL)
Base = declarative_base()

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

