from typing import Optional
from pydantic import EmailStr
from sqlmodel import Field, SQLModel

from helpers.types.date import dt


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(unique=True, index=True)
    email: EmailStr = Field(unique=True, index=True)
    is_active: Optional[bool] = Field(default=False)
    created_at: dt = Field(default_factory=dt.now)
    updated_at: dt = Field(default_factory=dt.now)
