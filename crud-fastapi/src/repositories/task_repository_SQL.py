from sqlalchemy.orm import Session
from typing import List
from src.models.modelFinal import Task,TaskDB
from src.interfaces.task_repository_interface import TaskRepositoryInterface

class TaskRepositorySQL(TaskRepositoryInterface):
    def __init__(self, db: Session):
        self.db = db

    def get_task(self, task_id: int) -> Task:
        return self.db.query(Task).filter(Task.id == task_id).first()
    
    def get_all_tasks(self) -> List[Task]:
        return self.db.query(Task).all()
    
    def create_task(self, task: Task) -> None:
        task_db = TaskDB(title=task.title, task=task.task)  
        self.db.add(task_db)
        self.db.commit()
        self.db.refresh(task_db)
        return task_db
    
    def update_task(self, task_id: int, task: Task) -> None:
        self.db.merge(task)
    
    def delete_task(self,task_id: int) -> None:
        user = self.get_task(task_id)
        if user:
            self.db.delete(user)
            self.db.commit()
