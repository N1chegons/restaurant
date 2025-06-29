from sqlalchemy import select, func

from src.auth.models import User
from src.database import async_session
from src.tables.models import Table, Booking
from src.tables.schemas import TableView, BookedView


class TableRepository:
    # get
    @classmethod
    async def get_free_tables_list(cls, user: User):
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
    async def get_booked_tables_list(cls, user: User):
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
    async def book_table(cls, user: User):
        async with async_session() as session:
            ...