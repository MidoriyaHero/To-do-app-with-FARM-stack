from fastapi import APIRouter, Depends
from app.models.user_model import User
from app.api.dependencies.user_dependency import get_current_user
from app.schemas.todo_schema import TodoOut, TodoCreate
from app.service.todo_service import TodoService
from app.models.todo_model import Todo


todo_router = APIRouter()

@todo_router.get('/', response_model = TodoOut)
async def list(current_user: User = Depends(get_current_user)):
    return await TodoService.list_todos(current_user)

@todo_router.post('/create', response_model = Todo)
async def create(data: TodoCreate, current_user: User = Depends(get_current_user)):
    return await TodoService.create(data, current_user)