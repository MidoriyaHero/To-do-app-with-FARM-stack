from fastapi.security import OAuth2PasswordBearer
from app.core.config import settings
from fastapi import Depends, HTTPException
from app.models.user_model import User
from jose import jwt
from app.schemas.auth_schema import TokenPayLoad
from datetime import datetime
from pydantic import ValidationError
from app.service.user_service import UserService
from json import loads

reusable_auth = OAuth2PasswordBearer(
    tokenUrl= f"{settings.API_STR}/auth/login",
    scheme_name= "JWT"
)

async def get_current_user(token: str = Depends(reusable_auth)) -> User:
    try:
       
        payload = jwt.decode(token, settings.JWT_KEY, algorithms=settings.ALGORITHM)
        token_data = TokenPayLoad(**payload)
        
        if datetime.fromisoformat(loads(token_data.expires)) < datetime.now():
            raise HTTPException(
                status_code=401, 
                detail= "Token expired!!!",
                headers={"WWW-Authenticate": "Bearer"})
    
    except(jwt.JWTError, ValidationError):
        raise HTTPException(status_code=403,
                            detail= "Could not validate credentials!!!",
                            headers={"WWW-Authenticate": "Bearer"})
    
    user = await UserService.get_user_by_id(UserId= token_data.subject)

    if not user:
        raise HTTPException(status_code=404, 
                            detail= "Could not find user")
    return user