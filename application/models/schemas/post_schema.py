from application.models.schemas.crehana_base_schema import CrehanaBaseSchema


class PostSchema(CrehanaBaseSchema):
    userId: int
    title: str
    body: str

    class Config:
        orm_mode = True
