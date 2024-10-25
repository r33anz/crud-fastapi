from src.repositories.task_repository_CSV import TaskRespositoryCSV
from src.repositories.task_repository_SQL import TaskRepositorySQL
from src.services.services import TaskService
from sqlalchemy.orm import Session
from src.database_configuration import get_db
from fastapi import Depends
import os

REPOSITORY_TYPE = "CSV" #CSV || SQL

def get_task_service(db: Session = Depends(get_db)):
    if REPOSITORY_TYPE == "CSV":
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        CSV_FILE_PATH = os.path.join(BASE_DIR, '../data/task.csv')
        task_repo = TaskRespositoryCSV(CSV_FILE_PATH)
    else:
        task_repo = TaskRepositorySQL(db)
    
    return TaskService(task_repo)