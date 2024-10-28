from fastapi import APIRouter, HTTPException
from app.schemas.user_schema import UserAuth
from app.service.user_service import UserService
import pymongo

user_router = APIRouter()
@user_router.post('/create-users')
async def create(data : UserAuth):
    try:
        await UserService.create_user(data)
    except pymongo.errors.DuplicateKeyError:
        raise HTTPException(
            status_code= 400,
            details = "UserName or Email is already exists"
        )
