from sqlalchemy import create_engine
from src.database_configuration import DATABASE_URL
from src.models.modelFinal import TaskDB

engine = create_engine(DATABASE_URL)

def init_db():
    TaskDB.metadata.create_all(bind=engine)


if __name__ == "__main__":
    init_db()

#In this file you add your model to migrate to DB