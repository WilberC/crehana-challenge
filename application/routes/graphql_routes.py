import asyncio
from graphene import ObjectType, Schema, Float, Int
from starlette_graphene3 import GraphQLApp, make_playground_handler
from application.views.graphql.user_view import UserQuery, UserMutation


class BaseQuery(UserQuery,
                ObjectType):
    pass


class BaseMutation(UserMutation,
                   ObjectType):
    pass


class BaseSubscription(ObjectType):
    count_seconds = Float(up_to=Int())

    @staticmethod
    async def subscribe_count_seconds(_root, _info, up_to):
        for i in range(up_to):
            yield i
            await asyncio.sleep(1.)
        yield up_to


schema = Schema(query=BaseQuery, mutation=BaseMutation, subscription=BaseSubscription)


def graphql_routes(app):
    app.mount("/graphql/", GraphQLApp(schema, on_get=make_playground_handler()))
