from fastapi import FastAPI
from pydantic import BaseModel, field_validator

app = FastAPI()

class Category(BaseModel):
    name: str
    color: str

class Task(BaseModel):
    title: str
    description: str
    is_completed: bool = False
    category: Category

    @field_validator("title")
    @classmethod
    def title_not_small(cls, value: str) -> str:
        if len(value) < 3:
            raise ValueError("Название задачи должно быть не короче 3 символов")
        return value

class TaskOut(BaseModel):
    title: str
    description: str
    is_completed: bool = False

@app.post("/response/", response_model=TaskOut)
def response(user: Task):
    return user