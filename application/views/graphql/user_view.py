import graphene
from application.utils.sqlalchemy import find, create
from application.models.graphene_schemas.user_graph import UserObjectType, UserInput
from application.models.postgres.user_model import User
from graphene.types import generic


class UserQuery(graphene.ObjectType):
    users = graphene.List(UserObjectType, id=graphene.Int(), filters=generic.GenericScalar())

    @staticmethod
    def resolve_users(_root, _info, id, filters):
        if id:
            return [find(User, id=id)]
        elif filters:
            return find(User, all_objs=True, **filters)
        else:
            return find(User, all_objs=True)


class CreateUser(graphene.Mutation):
    class Arguments:
        user_data = UserInput(required=True)

    ok = graphene.Boolean()
    user = graphene.Field(lambda: UserObjectType)

    def mutate(root, info, user_data):
        user = UserObjectType(**user_data)
        create(User, **user_data)
        ok = True
        return CreateUser(user=user, ok=ok)


class UserMutation(graphene.ObjectType):
    create_user = CreateUser.Field()
