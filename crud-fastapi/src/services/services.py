#from src.models.modelsSQL.modelSQL import Task
from src.models.modelFinal import Task
from typing import List
from src.interfaces.task_repository_interface import TaskRepositoryInterface

class TaskService:
    def __init__(self,task_repository = TaskRepositoryInterface):
        self.repo = task_repository

    def get_task(self,task_id: int) -> Task:
        return self.repo.get_task(task_id)

    def get_all_tasks(self) -> List[Task]:
        return self.repo.get_all_tasks()
    
    def create_task(self,task: Task) -> None:
        return self.repo.create_task(task)
    
    def update_task(self,task_id: int, task: Task) -> None:
        return self.repo.update_task(task_id,task)
       
    def delete_task(self,task_id: int) -> None:
        return self.repo.delete_task(task_id)
