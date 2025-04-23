from pydantic import BaseModel, EmailStr
from typing import Optional
from enum import Enum

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: int
    name: str
    email: EmailStr
    bio: Optional[str] = ""

class Config:
    orm_mode: True

class Token(BaseModel):
    access_token: str
    token_type: str

class FriendRequestCreate(BaseModel):
    receiver_id: int

class FriendRequestAction(BaseModel):
    request_id: int
    action: str