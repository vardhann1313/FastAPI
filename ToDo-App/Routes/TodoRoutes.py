from typing import List
from fastapi import APIRouter
from Models.TodoModel import Todo
from Service import TodoService

router = APIRouter()

# Get all todos route
@router.get("/todos", response_model=List[Todo])
def getAllTodos():
    return TodoService.getTodos()

# Get todo by Id route
@router.get("/todos/{id}", response_model=Todo)
def getTodoById(id: int):
    return TodoService.getTodoById(id)

# Create new todo route
@router.post("/todos", response_model=List[Todo])
def createTodo(todo: Todo):
    print(todo)
    return TodoService.addTodo(todo)

# Update todo using Id route
@router.put("/todos/{id}", response_model=Todo)
def updateTodo(id: int, todo: Todo):
    return TodoService.updateTodo(id, todo)

# Delete todo using Id
@router.delete("/todos/{id}", response_model=Todo)
def deleteTodo(id: int):
    return TodoService.deleteTodo(id)