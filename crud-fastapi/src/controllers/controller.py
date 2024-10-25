from fastapi import APIRouter, HTTPException
from typing import List
#from src.models.modelsSQL.modelSQL import Task
from src.models.modelFinal import Task
from src.services.services import TaskService


class TaskController:
    def __init__(self, service: TaskService):
        self.service = service

    def get_all_tasks(self) -> List[Task]:
        return self.service.get_all_tasks()

    def create_task(self, task: Task):
        self.service.create_task(task)
        return {"message": "Task created successfully"}

    def update_task(self, task_id: int, task: Task):
        tasks = self.service.get_all_tasks()
        if not any(t.id == task_id for t in tasks):
            raise HTTPException(status_code=404, detail="Task not found")
        self.service.update_task(task_id, task)
        return {"message": "Task updated successfully"}

    def delete_task(self, task_id: int):
        tasks = self.service.get_all_tasks()
        if not any(t.id == task_id for t in tasks):
            raise HTTPException(status_code=404, detail="Task not found")
        self.service.delete_task(task_id)
        return {"message": "Task deleted successfully"}
