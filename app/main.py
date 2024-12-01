from fastapi import FastAPI
from beanie import init_beanie
from contextlib import asynccontextmanager
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from motor.motor_asyncio import AsyncIOMotorClient
from fastapi.middleware.cors import CORSMiddleware

from app.models.user_model import User
from app.models.todo_model import Todo
from app.api.router import router
from app.core.config import settings




@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup code goes here:
    client: AsyncIOMotorClient = AsyncIOMotorClient(
        settings.MONGO_DB,
    )
    await init_beanie(client.BlogClient, 
                      document_models=[User, Todo])
    yield
    # shutdown code goes here:
    client.close()

app = FastAPI(
    title = settings.PROJECT_NAME,
    openapi_url= f'/{settings.API_STR}/openapi.json',
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins = settings.BACKEND_CORS_ORIGINS,
    allow_credentials = True,
    allow_methods = ['*'],
    allow_headers = ['*']
)

app.include_router(router, prefix= f'/{settings.API_STR}')