# src/routes.py
from fastapi import APIRouter
from src.controller import get_all_tasks, create_new_task, update_existing_task, delete_task_by_id
from src.model import Task
from typing import List

router = APIRouter()

@router.get("/tasks", response_model=List[Task])
def get_tasks():
    return get_all_tasks()

@router.post("/tasks")
def create_task(task: Task):
    return create_new_task(task)

@router.put("/tasks/{task_id}")
def update_task(task_id: int, task: Task):
    return update_existing_task(task_id, task)

@router.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    return delete_task_by_id(task_id)
