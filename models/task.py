from pydantic import BaseModel, field_validator

class Category(BaseModel):
    name: str
    color: str

class Task(BaseModel):
    title: str
    description: str
    is_completed: bool = False
    category: Category
    internal_note: str = "Служебная ПОЛЕ"

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
    category: Category