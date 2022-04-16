from application.models.schemas.crehana_base_schema import CrehanaBaseSchema


class TodoSchema(CrehanaBaseSchema):
    userId: int
    title: str
    completed: bool
