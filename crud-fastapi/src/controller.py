from fastapi import HTTPException
from src.model import Task
from src.services import get_tasks, create_task, update_task, delete_task
from typing import List

def get_all_tasks() -> List[Task]:
    return get_tasks()

def create_new_task(task: Task):
    create_task(task)
    return {"message": "Task created successfully"}

def update_existing_task(task_id: int, task: Task):
    tasks = get_tasks()
    if not any(t.id == task_id for t in tasks):
        raise HTTPException(status_code=404, detail="Task not found")
    update_task(task_id, task)
    return {"message": "Task updated successfully"}

def delete_task_by_id(task_id: int):
    tasks = get_tasks()
    if not any(t.id == task_id for t in tasks):
        raise HTTPException(status_code=404, detail="Task not found")
    delete_task(task_id)
    return {"message": "Task deleted successfully"}
