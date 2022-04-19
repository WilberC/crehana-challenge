from typing import List
from application.models.schemas.crehana_base_schema import CrehanaBaseSchema
from application.models.schemas.user_schema import UserSchema
from application.models.schemas.comment_schema import CommentSchema
from application.utils.make_optional_schema import _AllOptionalMeta


class BasePostSchema(CrehanaBaseSchema):
    title: str
    body: str


class PostSchema(BasePostSchema):
    user: UserSchema

    class Config:
        orm_mode = True


class PostWithCommentsSchema(PostSchema):
    comments: List[CommentSchema]

    class Config:
        orm_mode = True


class PostCreationSchema(BasePostSchema):
    user_id: int

    class Config:
        orm_mode = True


class PostUpdateSchema(PostCreationSchema, metaclass=_AllOptionalMeta):
    pass
