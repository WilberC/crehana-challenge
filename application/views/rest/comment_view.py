from typing import List
from fastapi import APIRouter
from application.utils.sqlalchemy import find
from application.models.postgres.comment_model import Comment
from application.models.schemas.comment_schema import CommentSchema

comment_router = APIRouter(prefix="/comments",
                           tags=["sync"],
                           responses={404: {"description": "Not found"}})


@comment_router.get("/", response_model=List[CommentSchema])
async def comments_view(postId: int):
    return find(Comment, all_objs=True, post_id=postId)
