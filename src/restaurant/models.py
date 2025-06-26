import enum
from datetime import time, date

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.database import Base

class Category(enum.Enum):
    basic = "basic"
    VIP = "VIP"

class NumberTable(str, enum.Enum):
    first = "1"
    second = "2"
    third = "3"
    fourth = "4"
    fifth = "5"
    sixth = "6"
    seventh = "7"


class Table(Base):
    __tablename__ = "tables"

    id: Mapped[int] = mapped_column(primary_key=True)
    number: Mapped[NumberTable]
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
