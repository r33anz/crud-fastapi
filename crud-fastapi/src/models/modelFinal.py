from sqlalchemy import Column, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import UUID 
import uuid
from pydantic import BaseModel, Field
from typing import Optional

Base = declarative_base()

class TaskDB(Base):
    __tablename__ = 'tasks'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4) 
    title = Column(String, index=True)
    task = Column(String)
    completed = Column(Boolean, default=False)  

class TaskBase(BaseModel):
    title: str
    task: str
    completed: bool = Field(default=False)  

class Task(TaskBase):
    id: Optional[uuid.UUID] = Field(default=None) 

    class Config:
        orm_mode = True 
