from fastapi import FastAPI, Depends
from .database import get_db
from sqlalchemy.orm import Session
from .models import TaskCreate, TaskDB

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/test_db")
async def test_db(db: Session = Depends(get_db)):
    return {"message": "Database connection successful"}


@app.post("/tasks/", status_code=201)
async def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    """_summary_
    Create a new task in the database.

    Args:
        task (TaskCreate): _description_ - The task to create.
        db (Session, optional): _description_
        The database session to use.
        Defaults to Depends(get_db).

    Returns:
        _type_: _description_
        Dict: The created task.
    """
    db_task = TaskDB(**task.model_dump())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task


@app.get("/tasks/")
async def read_tasks(db: Session = Depends(get_db)):
    """_summary_
    Get all tasks from the database.
    Args:
       db (Session, optional): _description_
       The database session to use.
       Defaults to Depends(get_db).
    Returns:
      _type_ List: _description_  The list of tasks.
    """
    tasks = db.query(TaskDB).all()
    return tasks
