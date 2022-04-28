from application.views.rest.sync_data import sync_data_router
from application.views.rest.user_view import user_router
from application.views.rest.post_view import post_router
from application.views.rest.comment_view import comment_router


def rest_api_routes(app):
    app.include_router(sync_data_router)
    app.include_router(user_router)
    app.include_router(post_router)
    app.include_router(comment_router)
