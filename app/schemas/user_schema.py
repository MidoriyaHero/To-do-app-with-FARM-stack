from pydantic import BaseModel, EmailStr, Field

class UserAuth(BaseModel):
    email: EmailStr = Field(..., description = "User Email")
    username : str = Field(..., max_length = 50, description = "UserName")
    password : str = Field(..., min_length = 5, description ='UserPassword')

