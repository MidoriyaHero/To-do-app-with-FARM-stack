from fastapi import APIRouter, Depends, HTTPException, Body
from fastapi.security import OAuth2PasswordRequestForm
from typing import Any
from app.service.user_service import UserService
from app.core.security import create_access_token, create_refresh_token
from app.schemas.auth_schema import TokenSchema
from app.schemas.user_schema import UserOut
from app.api.dependencies.user_dependency import get_current_user
from app.models.user_model import User
from jose import jwt
from app.schemas.auth_schema import TokenPayLoad
from pydantic import ValidationError
from app.core.config import settings


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

@auth_router.post("/refresh", summary= "Refresh token", response_model= TokenSchema)
async def refresh(refresh_token: str = Body(...)):
    try:
       
        payload = jwt.decode(refresh_token, settings.JWT_REFRESH_KEY, algorithms=settings.ALGORITHM)
        token_data = TokenPayLoad(**payload)
    
    except(jwt.JWTError, ValidationError):
        raise HTTPException(status_code=403,
                            detail= "Invalid token!!!",
                            headers={"WWW-Authenticate": "Bearer"})
    
    user = await UserService.get_user_by_id(UserId= token_data.subject)

    if not user:
        raise HTTPException(status_code=404, 
                            detail= "Could not find user")
    return {
        'access_token': create_access_token(user.user_id),
        'refresh_token': create_refresh_token(user.user_id)
    }