import enum
from datetime import time, date

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.auth import models
from src.database import Base

class Category(str, enum.Enum):
    basic = "basic"
    VIP = "VIP"


class Table(Base):
    __tablename__ = "tables"

    id: Mapped[int] = mapped_column(primary_key=True)
    category: Mapped[Category]
    is_booked: Mapped[bool] = mapped_column(default=False)



class Booking(Base):
    __tablename__ = "bookings"

    id: Mapped[int] = mapped_column(primary_key=True)
    table_id: Mapped[int] = mapped_column(ForeignKey("tables.id"), index=True)
    start_time: Mapped[time]
    end_time: Mapped[time]
    guest_name: Mapped[str]
    booking_date: Mapped[date]
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), on_delete=True)

    booked_man: Mapped["models.User"] = relationship(
        back_populates="booked_table"
    )