from pydantic import BaseModel
from application.models.schemas.crehana_base_schema import CrehanaBaseSchema


class GeoSchema(BaseModel):
    lat: str
    lng: str

    class Config:
        orm_mode = True


class AddressSchema(BaseModel):
    street: str
    suite: str
    city: str
    zipcode: str
    geo: GeoSchema

    class Config:
        orm_mode = True


class CompanySchema(BaseModel):
    name: str
    catchPhrase: str
    bs: str

    class Config:
        orm_mode = True


class UserSchema(CrehanaBaseSchema):
    name: str
    username: str
    email: str
    address: AddressSchema
    phone: str
    website: str
    company: CompanySchema

    class Config:
        orm_mode = True
