from fastapi import APIRouter, HTTPException
from app.schemas.user_schema import UserAuth, UserOut
from app.service.user_service import UserService
import pymongo

user_router = APIRouter()
@user_router.post('/create-users', response_model=UserOut)
async def create(data : UserAuth):
    try:
        return await UserService.create_user(data)
    except:
        raise HTTPException(  
            status_code= 400, 
            detail ="UserName or Email is already exists!")
