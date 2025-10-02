from pydantic import BaseModel

# Todo modelling and validation
class Todo(BaseModel):
    id: int
    title: str 
    description: str
    completed: bool = False
