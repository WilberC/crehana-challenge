from application.models.schemas.crehana_base_schema import CrehanaBaseSchema


class CommentSchema(CrehanaBaseSchema):
    postId: int
    name: str
    email: str
    body: str
