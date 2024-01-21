from pydantic import BaseModel

class Todo(BaseModel):
    id: int
    task: str
    isDone: str


todo = Todo(id=1, task='Create', isDone="False")

print(todo.id)
print(todo.task)
print(todo.isDone)