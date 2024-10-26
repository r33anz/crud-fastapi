from fastapi import APIRouter,Depends
from src.controllers.controller import TaskController
#from src.models.modelsSQL.modelSQL import Task
from src.models.modelFinal import Task
from typing import List
from src.dependencies import get_task_service
from src.services.services import TaskService

router = APIRouter()


@router.get("/tasks", response_model=List[Task])
def get_tasks(task_service: TaskService = Depends(get_task_service)):
    task_controller = TaskController(task_service)
    return task_controller.get_all_tasks()

@router.post("/tasks")
def create_task(task: Task, task_service: TaskService = Depends(get_task_service)):
    task_controller = TaskController(task_service)
    return task_controller.create_task(task)

@router.put("/tasks/{task_id}")
def update_task(task_id: str, task: Task, task_service: TaskService = Depends(get_task_service)):
    task_controller = TaskController(task_service)
    return task_controller.update_task(task_id, task)

@router.delete("/tasks/{task_id}")
def delete_task(task_id: str, task_service: TaskService = Depends(get_task_service)):
    task_controller = TaskController(task_service)
    return task_controller.delete_task(task_id)