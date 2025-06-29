from fastapi import APIRouter
from fastapi.params import Depends

from src.auth.models import User
from src.auth.router import cur_user
from src.tables.repository import TableRepository
router = APIRouter(
    tags=["Tables"],
    prefix="/table"
)

@router.get("/get_free_tables/", summary="Get all free tables")
async def get_tables():
    table_list = await TableRepository.get_free_tables_list()
    return table_list

@router.get("/get_booked_tables/", summary="Get all booked tables")
async def get_booked_tables():
    table_list = await TableRepository.get_booked_tables_list()
    return table_list

