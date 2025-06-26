from fastapi import APIRouter, Depends
from pydantic import EmailStr
from sqlalchemy import select, update

from src.auth.router import cur_user
from src.auth.schemas import ProfileRead
from src.database import async_session
from src.auth.models import User

router = APIRouter(
    tags=["Profile"],
    prefix="/profile"
)


@router.get("/", summary="Profile")
async def get_profile_rep(user: User = Depends(cur_user)):
    async with async_session() as session:
        query = select(User).filter_by(id=user.id)
        result = await session.execute(query)
        calc = result.unique().scalars().all()
        alr = [ProfileRead.model_validate(p) for p in calc]
        # noinspection PyBroadException
        try:
            if user.is_superuser:
                return {
                    "status": 200,
                    "Role": "Administrator",
                    "Profile": alr,
                }
            return {
                "status": 200,
                "Profile": alr,
            }
        except:
            return {"status": 204, "message": "Unknown error"}

@router.put("/change_data/", summary="Change user data")
async def change_data_for_user(new_username: str, new_email: EmailStr,user: User = Depends(cur_user)):
    async with async_session() as session:
        query = select(User).filter_by(id=user.id)
        result = await session.execute(query)
        res = result.unique().scalars().all()
        # noinspection PyBroadException
        try:
            if res:
                stmt = (
                    update(User)
                    .values(username=new_username, email=new_email)
                    .filter_by(id=user.id)
                )
                await session.execute(stmt)
                await session.commit()

                return {
                    "status": 200,
                    "message": "User data edited"
                }
            else:
                return {"status": 404, "message": f"User undefiled"}
        except:
            return {
                "status": 422,
                "Error": "Check the value of the fields, and try again"
            }