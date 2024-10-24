import csv
from src.model import Task
from typing import List
import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_FILE_PATH = os.path.join(BASE_DIR, '../data/task.csv')

def get_tasks() -> List[Task]:
    tasks = []
    with open(CSV_FILE_PATH, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            tasks.append(Task(**row))
    return tasks

def get_all_tasks() -> List[Task]:
    tasks = []
    try:
        with open(CSV_FILE_PATH, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                tasks.append(Task(**row))
    except FileNotFoundError:
        pass
    return tasks

def get_next_id() -> int:
    tasks = get_all_tasks()
    if tasks:
        return len(tasks) + 1
        
    return 1  

def create_task(task: Task):
    if task.id is None:  
        task.id = get_next_id()
    
    with open(CSV_FILE_PATH, mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['id', 'title', 'task', 'completed'])
        if file.tell() == 0:  
            writer.writeheader()
        writer.writerow(task.model_dump(include={'id', 'title', 'task', 'completed'}))

def update_task(task_id: int, task: Task):
    tasks = get_tasks()
    updated_tasks = []
    for t in tasks:
        if t.id == task_id:
            updated_tasks.append(task)
        else:
            updated_tasks.append(t)

    with open(CSV_FILE_PATH, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['id', 'title', 'description', 'completed'])
        writer.writeheader()
        for task in updated_tasks:
            writer.writerow(task.model_dump())

def delete_task(task_id: int):
    tasks = get_tasks()
    updated_tasks = [t for t in tasks if t.id != task_id]

    with open(CSV_FILE_PATH, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['id', 'title', 'task', 'completed'])
        writer.writeheader()
        for task in updated_tasks:
            writer.writerow(task.model_dump())
