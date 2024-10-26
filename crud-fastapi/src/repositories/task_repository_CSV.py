from src.interfaces.task_repository_interface import TaskRepositoryInterface
from typing import List
from src.models.modelFinal import Task
import csv
from uuid import UUID
class TaskRespositoryCSV(TaskRepositoryInterface):

    def __init__(self,filename : str):
        self.filename = filename
    
    def get_task(self, task_id: int) -> Task:

        with open(self.filename, mode='r') as file:
            reader = csv.DictReader(file)
            
            for row in reader:
                if int(row['id']) == task_id:  
                    return Task(**row) 

        return None

    def get_all_tasks(self) -> List[Task]:
        tasks = []

        with open(self.filename , mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                print(Task(**row))
                tasks.append(Task(**row))

        return tasks

    
    
    def create_task(self,task: Task) -> None:
        if task.id is None:  
            task.id =  uuid.uuid4()

        with open(self.filename , mode='a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['id', 'title', 'task', 'completed'])
            if file.tell() == 0:  
                writer.writeheader()
        
            data_to_write = task.model_dump(include={'id', 'title', 'task', 'completed'})
            writer.writerow(data_to_write)
        
    def update_task(self,task_id: str, task: Task) -> None:
        tasks = self.get_all_tasks()
        updated_tasks = []

        for t in tasks:
            print(type(t.id))
            if t.id == UUID(task_id):
                task.id = t.id
                updated_tasks.append(task)
            else:
                updated_tasks.append(t)

        with open(self.filename, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['id', 'title', 'task', 'completed'])
            writer.writeheader()
            for task in updated_tasks:
                writer.writerow(task.model_dump())
    
    def delete_task(self, task_id: str) -> None:
        tasks = self.get_all_tasks()
        updated_tasks = [t for t in tasks if t.id != UUID(task_id)]

        with open(self.filename, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['id', 'title', 'task', 'completed'])
            writer.writeheader()
            for task in updated_tasks:
                writer.writerow(task.model_dump())

    