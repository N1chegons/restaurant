from datetime import time, date

from pydantic import BaseModel, ConfigDict

from src.tables.models import Category


class TableView(BaseModel):
    id: int
    category: str
    is_booked: bool

    model_config = ConfigDict(from_attributes=True)

class BookedView(BaseModel):
    id: int
    table_id: int
    start_time: time
    end_time: time
    guest_name: str
    booking_date: date

    model_config = ConfigDict(from_attributes=True)
