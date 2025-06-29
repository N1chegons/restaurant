from sqlalchemy import select, func

from src.auth.models import User
from src.database import async_session
from src.tables.models import Table, Booking
from src.tables.schemas import TableView, BookedView, BookingCreate


class TableRepository:
    # get
    @classmethod
    async def get_free_tables_list(cls):
        async with async_session() as session:
            #count
            res = await session.execute(select(func.count()).select_from(Table))
            count = res.scalar()

            query = select(Table).filter_by(is_booked=False)
            query_calc = await session.execute(query)
            result = query_calc.unique().scalars().all()
            result_schemas = [TableView.model_validate(i) for i in result]
            try:
                if result_schemas:
                    return {
                        "status": 200,
                        "count tables": count,
                        "tables": result_schemas
                    }
                else:
                    return {
                        "status": 404,
                        "message": "There is not a single object"
                    }
            except:
                return {"status": 204, "message": "Unknown error"}

    @classmethod
    async def get_booked_tables_list(cls):
        async with async_session() as session:
            # count
            res = await session.execute(select(func.count()).select_from(Booking))
            count = res.scalar()

            query = select(Booking)
            query_calc = await session.execute(query)
            result = query_calc.unique().scalars().all()
            result_schemas = [BookedView.model_validate(i) for i in result]
            try:
                if result_schemas:
                    return {
                        "status": 200,
                        "count tables": count,
                        "notes": result_schemas
                    }
                else:
                    return {
                        "status": 404,
                        "message": "There is not a single object"
                    }
            except:
                return {"status": 204, "message": "Unknown error"}

    # post
    @classmethod
    async def book_table(cls, user: User, bok_data: BookingCreate):
        async with async_session() as session:
            # check actual table
            existing_booking = await session.execute(
                select(Booking).where(
                    (Booking.table_id == bok_data.table_id) &
                    (Booking.booking_date == bok_data.booking_date) &
                    (Booking.start_time < bok_data.end_time) &
                    (Booking.end_time > bok_data.start_time)
                )
            )
            if existing_booking.scalar():
                raise ValueError("Столик уже забронирован на это время")

            # create booking
            new_booking = Booking(
                user_id=user.id,
                **bok_data.model_sump()
            )

            session.add(new_booking)
            await session.commit()
            await session.refresh(new_booking)
            return new_booking