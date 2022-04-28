from graphene_pydantic import PydanticObjectType, PydanticInputObjectType
from application.models.schemas.user_schema import UserSchema, AddressSchema, GeoSchema, CompanySchema


# Queries
class GeoObjectType(PydanticObjectType):
    class Meta:
        model = GeoSchema


class AddressObjectType(PydanticObjectType):
    class Meta:
        model = AddressSchema


class CompanyObjectType(PydanticObjectType):
    class Meta:
        model = CompanySchema


class UserObjectType(PydanticObjectType):
    class Meta:
        model = UserSchema


# Inputs
class GeoInput(PydanticInputObjectType):
    class Meta:
        model = GeoSchema
        exclude_fields = ("id",)


class AddressInput(PydanticInputObjectType):
    class Meta:
        model = AddressSchema
        exclude_fields = ("id",)


class CompanyInput(PydanticInputObjectType):
    class Meta:
        model = CompanySchema
        exclude_fields = ("id",)


class UserInput(PydanticInputObjectType):
    class Meta:
        model = UserSchema
        exclude_fields = ("id",)
