from beanie import Document, Indexed, Link, before_event, Replace, Insert
from uuid import UUID, uuid4
from pydantic import Field, EmailStr
from datetime import datetime
from typing import Optional
from app.models.user_model import User


class Todo(Document):
    todo_id: UUID = Field(default_factory = uuid4, unique = True)
    status: bool = False
    title: Indexed(str)
    description: str = None
    create_at: datetime = Field(default_factory = datetime.now)
    update_at: datetime = Field(default_factory = datetime.now)
    owner: Link[User]

    def __repr__(self) -> str:
        return f'<User {self.title}>'
    
    def __str__(self) -> str:
        return self.title
    
    def __hash__(self) -> int:
        return hash(self.title)
    
    def __eq__(self, other: object) -> bool:
        if isinstance(other, Todo):
            return self.todo_id == other.todo_id
        return False
    @before_event([Replace, Insert])
    async def updat_time(self):
        self.update_at = datetime.now()

    class Settings:
        name = 'To-do'