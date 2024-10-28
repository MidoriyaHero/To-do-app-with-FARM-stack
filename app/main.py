from fastapi import FastAPI
from app.config.config import settings
from beanie import init_beanie
from contextlib import asynccontextmanager
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from app.models.user_model import User


@asynccontextmanager
async def lifespan(app: FastAPI):
    db_client = MongoClient(settings.MONGO_DB, server_api=ServerApi('1'))
    init_beanie(
        database= db_client.BlogClient,
        document_models= [
            User    
        ]
    )
    yield
    print("Run on shutdown!")


app = FastAPI(
    title = settings.PROJECT_NAME,
    openapi_url= f'/{settings.API_STR}/openapi.json',
    lifespan=lifespan
)

#app.include_router()