from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from typing import Any
from app.service.user_service import UserService
from app.core.security import create_access_token, create_refresh_token
from app.schemas.auth_schema import TokenSchema
from app.schemas.user_schema import UserOut
from app.api.dependencies.user_dependency import get_current_user
from app.models.user_model import User


auth_router = APIRouter()

@auth_router.post('/login', summary= "Create access and refresh token", response_model=TokenSchema)
async def login(data: OAuth2PasswordRequestForm = Depends()) -> Any:
    user = await UserService.authenticate(email= data.username, password= data.password)
    
    if not user:
        raise HTTPException(status_code= 400, detail= "something went wrong!")
    
    return {
        'access_token': create_access_token(user.user_id),
        'refresh_token': create_refresh_token(user.user_id)
    }

@auth_router.post("/test-login", summary= "Test login", response_model=UserOut)
async def testlogin(user_data: User = Depends(get_current_user)) -> Any:
    return user_data