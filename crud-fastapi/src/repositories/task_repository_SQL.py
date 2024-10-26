from sqlalchemy.orm import Session
from typing import List
from src.models.modelFinal import Task,TaskDB
from src.interfaces.task_repository_interface import TaskRepositoryInterface
from uuid import UUID
from fastapi import APIRouter, HTTPException 
from sqlalchemy.exc import NoResultFound

class TaskRepositorySQL(TaskRepositoryInterface):
    def __init__(self, db: Session):
        self.db = db

    def get_task(self, task_id: int) -> Task:
        return self.db.query(TaskDB).filter(TaskDB.id == task_id).first()
    
    def get_all_tasks(self) -> List[Task]:
        return self.db.query(TaskDB).all()
    
    def create_task(self, task: Task) -> None:
        task_db = TaskDB(title=task.title, task=task.task)  
        self.db.add(task_db)
        self.db.commit()
        self.db.refresh(task_db)
        return task_db
    
    def update_task(self, task_id: int, task_updated: Task) -> Task:

        task_uuid = UUID(task_id)
        task = self.db.query(TaskDB).filter(TaskDB.id == task_uuid).first()
        if task is None:
            raise NoResultFound(f"No se encontró la tarea con el ID {task_id}.")

        task.title = task_updated.title
        task.task = task_updated.task
        task.completed = task_updated.completed
        self.db.commit()
        self.db.refresh(task) 
        return task
        
    
    def delete_task(self,task_id: str) -> None:
        task_uuid = UUID(task_id)
        task = self.db.query(TaskDB).filter(TaskDB.id == task_uuid).first()
        if task:
            self.db.delete(task)
            self.db.commit()
        else:
            raise HTTPException(status_code=404, detail="Task not found 33")
