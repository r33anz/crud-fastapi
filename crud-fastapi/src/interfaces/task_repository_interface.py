from src.models.modelFinal import Task
from abc import ABC, abstractmethod
from typing import List

class TaskRepositoryInterface(ABC):
    
    @abstractmethod
    def get_task(task_id: int) -> Task:
        pass

    @abstractmethod
    def get_all_tasks() -> List[Task]:
        pass
    
    @abstractmethod
    def create_task(task: Task) -> None:
        pass
    
    @abstractmethod
    def update_task(task_id: int, task: Task) -> None:
        pass
    
    @abstractmethod    
    def delete_task(task_id: int) -> None:
        pass