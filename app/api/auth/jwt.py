from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from typing import Any
from app.service.user_service import UserService
from app.core.security import create_access_token, create_refresh_token


auth_router = APIRouter()

@auth_router.post('/login')
async def login(data: OAuth2PasswordRequestForm = Depends()) -> Any:
    user = await UserService.authenticate(email= data.username, password= data.password)
    if not user:
        raise HTTPException(status_code= 400, detail= "something went wrong!")
    return {
        'access_token': create_access_token(user.user_id),
        'refresh_token': create_refresh_token(user.user_id)
    }