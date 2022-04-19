from application.models.schemas.crehana_base_schema import CrehanaBaseSchema


class CommentSchema(CrehanaBaseSchema):
    post_id: int
    name: str
    email: str
    body: str

    class Config:
        orm_mode = True
