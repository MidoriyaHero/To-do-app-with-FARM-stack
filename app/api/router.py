from fastapi import APIRouter 
from app.api.handler import user, todo
from app.api.auth.jwt import auth_router



router = APIRouter()
router.include_router(user.user_router, prefix='/users', tags= ['Users'])
router.include_router(todo.todo_router, prefix='/todo', tags= ['Todo'])
router.include_router(auth_router, prefix='/auth', tags= ['Authentication'])