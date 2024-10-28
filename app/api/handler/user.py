from fastapi import APIRouter 
from app.schemas.user_schema import UserAuth


user_router = APIRouter()
@user_router.post('/create-users')
async def create(data : UserAuth):
    pass