import datetime

from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from pydantic import EmailStr
from sqlalchemy import text
from sqlalchemy.orm import Mapped
from sqlalchemy.testing.schema import mapped_column

from src.database import Base


class User(SQLAlchemyBaseUserTable[int], Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[EmailStr]
    hashed_password: Mapped[str]
    registered_at: Mapped[datetime.datetime] = mapped_column(
        server_default=text(
            "TIMEZONE('utc', now())")
    )
    is_active: Mapped[bool] = mapped_column(default=True, nullable=False)
    is_superuser: Mapped[bool] = mapped_column(default=False, nullable=False)
    is_verified: Mapped[bool] = mapped_column(default=True, nullable=False)
    is_blocked: Mapped[bool] = mapped_column(default=False, nullable=False)
