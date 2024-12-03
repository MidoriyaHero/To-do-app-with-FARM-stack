from fastapi import APIRouter, Depends
from app.models.user_model import User
from app.api.dependencies.user_dependency import get_current_user
from app.schemas.todo_schema import TodoOut, TodoCreate, TodoUpdate
from app.service.todo_service import TodoService
from app.models.todo_model import Todo
from uuid import UUID
from typing import List

todo_router = APIRouter()

@todo_router.get('/', response_model = List[TodoOut])
async def list(current_user: User = Depends(get_current_user)):
    return await TodoService.list_todos(current_user)

@todo_router.post('/create', response_model = Todo)
async def create(data: TodoCreate, current_user: User = Depends(get_current_user)):
    return await TodoService.create( current_user, data)

@todo_router.get('/{todo_id}', response_model=TodoOut)
async def get_todo_by_id(todo_id: UUID, current_user: User = Depends(get_current_user)):
    print(await TodoService.retrieve(current_user, todo_id))
    return await TodoService.retrieve(current_user, todo_id)

@todo_router.put('/{todo_id}', response_model = TodoOut)
async def update(todo_id: UUID, data: TodoUpdate, current_user: User = Depends(get_current_user)):
    return await TodoService.update_todo(current_user, todo_id, data)

@todo_router.delete('/{todo_id}')
async def delete(todo_id: UUID, current_user: User = Depends(get_current_user)):
    await TodoService.delete_todo(current_user,todo_id)
    return {"Message":"Successfully deleted!"}