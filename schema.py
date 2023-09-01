from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True

class UserList(BaseModel):
    user_list: list[User]= []

class UserCreate(BaseModel):
    name: str
