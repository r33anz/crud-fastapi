from src.repositories.task_repository_CSV import TaskRespositoryCSV
from src.repositories.task_repository_SQL import TaskRepositorySQL
from src.services.services import TaskService
from sqlalchemy.orm import Session
from src.database_configuration import get_db
from fastapi import Depends
import os
import logging

REPOSITORY_TYPE = "CSV" #CSV || SQL
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def get_task_service(db: Session = Depends(get_db)):
    

    try:
        task_repo = TaskRepositorySQL(db)
        task_repo.get_all_tasks() 
            
        logger.info("Using SQL repository")
            
    except Exception as e:
    
        logger.error("Failed to connect to SQL database. Switching to CSV repository. Error: %s", e)
            
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        CSV_FILE_PATH = os.path.join(BASE_DIR, '../data/task.csv')
        task_repo = TaskRespositoryCSV(CSV_FILE_PATH)

    return TaskService(task_repo)