from pydantic import BaseModel
from uuid import UUID

class OurBaseModel(BaseModel):
    class Config:
        orm_mode = True

class TokenSchema(OurBaseModel):
    access_token: str 
    refresh_token: str

class TokenPayLoad(OurBaseModel):
    subject: UUID
    expires: str
    