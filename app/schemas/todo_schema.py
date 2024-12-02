from pydantic import BaseModel, Field
from typing import Optional
from uuid import UUID
from datetime import datetime
from pydantic import ConfigDict

class OurBaseModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)


class TodoCreate(OurBaseModel):
    title: str = Field(..., title = "Title")
    description: str = Field(..., title= "Description")
    status: Optional[bool] = False

class TodoUpdate(OurBaseModel):
    title: Optional[str] = Field(..., title = "Title")
    description: Optional[str] = Field(..., title= "Description")
    status: Optional[bool] = False

class TodoOut(OurBaseModel):
    todo_id: UUID
    status: bool
    title: str
    description: str
    create_at: datetime
    update_at: datetime
    