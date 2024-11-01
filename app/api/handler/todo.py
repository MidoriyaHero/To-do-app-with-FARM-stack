from fastapi import APIRouter, Depends
from app.models.user_model import User
from app.api.dependencies.user_dependency import get_current_user
from app.schemas.todo_schema import TodoOut


todo_router = APIRouter()
@todo_router.get('/', response_model = TodoOut)
async def list(current_user: User = Depends(get_current_user)):
    pass