import datetime
from typing import List

from fastapi_users import schemas
from pydantic import EmailStr, field_validator, BaseModel, ConfigDict

from src.tables.schemas import BookedView


class ProfileRead(BaseModel):
    id: int
    username: str
    email: EmailStr
    registered_at: datetime.datetime
    booked_table: list[BookedView]


    @field_validator('registered_at')
    def custom(cls, v: datetime):
        return datetime.datetime.strftime(v, "%m.%d.%Y")

    model_config = ConfigDict(from_attributes=True)

class UserRead(schemas.BaseUser[int]):
    id: int
    username: str
    email: EmailStr
    hashed_password: str
    registered_at: datetime.datetime
    is_active: bool
    is_superuser: bool
    is_verified: bool

    @field_validator('registered_at')
    def custom(cls, v):
        return datetime.datetime.strftime(v, "%m.%d.%Y")

class UserCreate(schemas.BaseUserCreate):
    username: str
    password: str
    email: EmailStr