from typing import List
from fastapi import APIRouter
from application.utils.sqlalchemy import find
from application.models.postgres.user_model import User
from application.models.schemas.user_schema import UserSchema

user_router = APIRouter(prefix="/users",
                        tags=["sync"],
                        responses={404: {"description": "Not found"}})


@user_router.get("/", response_model=List[UserSchema])
async def users_view():
    return find(User, all_objs=True)


@user_router.get("/{user_id}", response_model=UserSchema)
async def user_detail_view(user_id: int):
    return find(User, id=user_id)
