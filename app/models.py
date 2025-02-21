from pydantic import BaseModel
from typing import Optional
from sqlalchemy import Column, Integer, String, Boolean
from .database import Base


class TaskCreate(BaseModel):
    """_summary_
    A Pydantic model for creating a new task.
    This model is used to validate the input data when creating a new task.

    Args:
        TaskCreate (BaseModel): The base model for Pydantic models.
    Returns:
        TaskCreate: A Pydantic model for creating a new task.
    """

    title: str  # title of the task
    description: Optional[str] = None  # description of the task
    completed: bool = False  # whether the task is completed or not


class Task(TaskCreate):
    """_summary_
    A Pydantic model for a task.
    This model is used to validate the output data when retrieving a task.

    Args:
        TaskCreate (_type_): _description_
    Returns:
        Task: A Pydantic model for a task.
    """

    id: int  # id of the task

    class Config:
        from_attributes = True


class TaskDB(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(
        String(224),
        index=True,
    )
    description = Column(String(224), index=True)
    completed = Column(Boolean, default=False)
