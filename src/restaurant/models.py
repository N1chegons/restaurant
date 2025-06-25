import enum
from datetime import time, date

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




class Booking(Base):
    __tablename__ = "booking"

    id: Mapped[int] = mapped_column(primary_key=True)
    number: Mapped[NumberTable]
    start_time: Mapped[time]
    end_time: Mapped[time]
    guest_name: Mapped[str]
    category: Mapped[Category]
    booking_date: Mapped[date]
    is_booked: Mapped[bool] = mapped_column(default=False)
