from src.models.model import Task
from abc import ABC, abstractmethod
from typing import List

class TaskRepositoryInterface(ABC):

    @abstractmethod
    def get_task():
        return 0