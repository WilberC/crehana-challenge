from application.models.schemas.crehana_base_schema import CrehanaBaseSchema


class AlbumSchema(CrehanaBaseSchema):
    userId: int
    title: str
