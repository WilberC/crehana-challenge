from typing import List, Optional
from fastapi import APIRouter, status
from application.utils.sqlalchemy import find, create, delete, update
from application.models.postgres.post_model import Post
from application.models.schemas.post_schema import PostSchema, PostWithCommentsSchema, PostCreationSchema, \
    PostUpdateSchema

post_router = APIRouter(prefix="/posts",
                        tags=["sync"],
                        responses={404: {"description": "Not found"}})


@post_router.get("/", response_model=List[PostSchema])
async def posts_view():
    return find(Post, all_objs=True)


@post_router.get("/{post_id}", response_model=PostSchema)
async def post_detail_view(post_id: int):
    return find(Post, id=post_id)


@post_router.get("/{post_id}/comments", response_model=PostWithCommentsSchema)
async def post_comments_view(post_id: int):
    return find(Post, id=post_id)


@post_router.post("/", response_model=PostSchema, status_code=status.HTTP_201_CREATED)
async def create_post_view(post: PostCreationSchema):
    return create(Post, **post.dict(exclude={"id"}))


@post_router.delete("/{post_id}", response_model=PostSchema)
async def delete_post_view(post_id: int):
    post_deleted = delete(Post, id=post_id)
    if post_deleted:
        return status.HTTP_202_ACCEPTED
    else:
        return status.HTTP_404_NOT_FOUND


@post_router.delete("/{post_id}", response_model=PostSchema)
async def delete_post_view(post_id: int):
    post_deleted = delete(Post, id=post_id)
    if post_deleted:
        return status.HTTP_202_ACCEPTED
    else:
        return status.HTTP_404_NOT_FOUND


@post_router.patch("/{post_id}", response_model=PostSchema, status_code=status.HTTP_202_ACCEPTED)
async def update_post_view(post_id: int, post: PostUpdateSchema):
    return update(Post, find_by={"id": post_id}, updated_values=post.dict(exclude_unset=True))


@post_router.put("/{post_id}", response_model=Optional[PostWithCommentsSchema], status_code=status.HTTP_202_ACCEPTED)
async def update_post_view(post_id: int, post: PostUpdateSchema):
    return update(Post, find_by={"id": post_id}, updated_values=post.dict(exclude_unset=True))
