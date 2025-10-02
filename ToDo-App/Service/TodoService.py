from typing import List
from fastapi import HTTPException
from starlette.status import HTTP_404_NOT_FOUND
from Models.TodoModel import Todo

# Temp List to store todos
todos : List[Todo] = []

# Return all todos
def getTodos() -> List[Todo]:
    return todos

# Append new todo in the list
def addTodo(todo: Todo) -> List[Todo]:
    todos.append(todo)
    return todos

# Find and return the todo with the matching ID
def getTodoById(id: int) -> Todo:
    found_todo = None
    for todo in todos:
        if todo.id == id:
           return todo

    raise HTTPException(
        status_code=HTTP_404_NOT_FOUND,
        detail="Todo not found with id {id}"
    )

# Find and update the todo with the matching ID
def updateTodo(id: int, todo: Todo) -> Todo:
    for todo in todos:
        if todo.id == id:
            todos[todo.id] = todo
            return todo
    
    raise HTTPException(
        status_code=HTTP_404_NOT_FOUND,
        detail=f"Todo not found with Id : {id}"
    )

# Find and remove the todo with the matching ID
def deleteTodo(id: int) -> Todo:
    for todo in todos:
        if todo.id == id:
           found_todo = todo
           todos.pop(found_todo.id)
           return found_todo

    raise HTTPException(
        status_code=HTTP_404_NOT_FOUND,
        detail="Todo not found with id {id}"
    )