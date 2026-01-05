from typing import Optional
from pydantic import BaseModel
from helpers.types.date import dt


class UserRead(BaseModel):
    id: int
    username: str
    email: str
    is_active: bool
    created_at: dt


class UserUpdate(BaseModel):
    username: Optional[str]
    email: Optional[str]
    is_active: Optional[bool] = False
    updated_at: dt = dt.now()


class UserCreate(BaseModel):
    username: str
    email: str
