from pydantic import BaseSettings, AnyHttpUrl
from dotenv import load_dotenv
import os
from typing import List
load_dotenv()


class Settings(BaseSettings):
    API_STR: str = "api"
    JWT_KEY: str = os.getenv('JWT_KEY')
    JWT_REFRESH_KEY: str = os.getenv('JWT_REFRESH_KEY')
    ALGORITHM: str = 'HS256'
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 15
    REFRESH_TOKEN_EXPIRE_MINUTES: int = 60*24*7 # 7days
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []
    PROJECT_NAME: str = 'TO DO APP'

    #Database 
    MONGO_DB: str = os.getenv('MONGODB_CONNECTION')

    class Config:
        case_sensitive = False

settings = Settings()