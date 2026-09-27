from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from config import settings
from models.task import Task, TaskOut

app = FastAPI(
    title="Task Manager API",
    description="Управления задачами",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.FRONTEND_URL],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

fake_db = []

@app.get("/tasks/", response_model=list[TaskOut], tags=["tasks"])
def get_tasks():
    return fake_db

"/tasks/", response_model=TaskOut, tags=["tasks"]
def create_task(task: Task):
    fake_db.append(task)
    return task

@app.get("/tasks/{task_id}", response_model=TaskOut, tags=["tasks"])
def get_task(task_id: int):
    if task_id < 0 or task_id >= len(fake_db):
        raise HTTPException(status_code=404, detail="Задача не найдена")
    return fake_db[task_id]