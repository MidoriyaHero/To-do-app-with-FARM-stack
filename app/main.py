from fastapi import FastAPI
from app.core.config import settings
from beanie import init_beanie
from contextlib import asynccontextmanager
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from app.models.user_model import User
from motor.motor_asyncio import AsyncIOMotorClient
from app.api.router import router
from app.api.handler.user import user_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup code goes here:
    client: AsyncIOMotorClient = AsyncIOMotorClient(
        settings.MONGO_DB,
    )
    await init_beanie(client.BlogClient, 
                      document_models=[User])
    yield
    # shutdown code goes here:
    client.close()

app = FastAPI(
    title = settings.PROJECT_NAME,
    openapi_url= f'/{settings.API_STR}/openapi.json',
    lifespan=lifespan
)

app.include_router(user_router, prefix= f'/{settings.API_STR}')