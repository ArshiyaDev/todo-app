from pydantic import BaseModel


class Todo(BaseModel):
    title: str
    completed: bool = False
