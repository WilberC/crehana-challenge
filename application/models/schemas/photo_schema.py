from application.models.schemas.crehana_base_schema import CrehanaBaseSchema


class PhotoSchema(CrehanaBaseSchema):
    albumId: int
    title: str
    url: str
    thumbnailUrl: str
