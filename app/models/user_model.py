from beanie import Document, Indexed
from uuid import UUID, uuid4
from pydantic import Field, EmailStr


class User(Document):
    user_id: UUID = Field(default_factory = uuid4)
    user_name: str = Indexed(str, unique = True)
    email = Indexed(EmailStr, unique = True)
    hased_pass: str
    first_name: str
    last_name: str
    disable: bool

    