import requests
from fastapi import APIRouter
from application.models.postgres.user_model import Geo, Address, Company, User
from application.models.postgres.post_model import Post
from application.models.postgres.comment_model import Comment
from application.utils.sqlalchemy import find_or_create, find
from application.utils.update_auto_increment_id import update_ids_of

URL_API_BASE = "https://jsonplaceholder.typicode.com"

sync_data_router = APIRouter(prefix="/sync_data",
                             tags=["sync"],
                             responses={404: {"description": "Not found"}})


def sync_data_from(data_from, sync_function) -> [int, int, int]:
    response_data = requests.get(f"{URL_API_BASE}/{data_from}").json()
    return sync_function(response_data)


def sync_users(response_data):
    saved_correctly = 0
    errors = 0

    for user_dict in response_data:
        address_dict = user_dict.get("address")
        geo_dict = address_dict.get("geo")
        company_dict = user_dict.get("company")

        geo_instance = find_or_create(Geo,
                                      close_session=True,
                                      lat=geo_dict.get("lat"),
                                      lng=geo_dict.get("lng"))

        address_instance = find_or_create(Address,
                                          close_session=True,
                                          street=address_dict.get("street"),
                                          suite=address_dict.get("suite"),
                                          city=address_dict.get("city"),
                                          zipcode=address_dict.get("zipcode"),
                                          geo_id=geo_instance.id)

        company_instance = find_or_create(Company,
                                          close_session=True,
                                          name=company_dict.get("name"),
                                          catchPhrase=company_dict.get("catchPhrase"),
                                          bs=company_dict.get("bs"))

        user_instance = find_or_create(User,
                                       close_session=True,
                                       id=user_dict.get("id"),
                                       name=user_dict.get("name"),
                                       username=user_dict.get("username"),
                                       email=user_dict.get("email"),
                                       address_id=address_instance.id,
                                       phone=user_dict.get("phone"),
                                       website=user_dict.get("website"),
                                       company_id=company_instance.id)
        if user_instance:
            saved_correctly += 1
        else:
            errors += 1
    update_ids_of(["geo", "addresses", "companies", "users"])
    return [len(response_data), saved_correctly, errors]


def sync_posts(response_data):
    saved_correctly = 0
    errors = 0

    for post_dict in response_data:
        user_instance = find(User, close_session=True, id=post_dict.get("userId"))
        post_instance = find_or_create(Post,
                                       close_session=True,
                                       id=post_dict.get("id"),
                                       title=post_dict.get("title"),
                                       body=post_dict.get("body"),
                                       user_id=user_instance.id)
        if post_instance:
            saved_correctly += 1
        else:
            errors += 1
    update_ids_of(["posts"])
    return [len(response_data), saved_correctly, errors]


def sync_comments(response_data):
    saved_correctly = 0
    errors = 0

    for comment_dict in response_data:
        post_instance = find(Post, close_session=True, id=comment_dict.get("postId"))
        comment_instance = find_or_create(Comment,
                                          close_session=True,
                                          id=comment_dict.get("id"),
                                          name=comment_dict.get("name"),
                                          email=comment_dict.get("email"),
                                          body=comment_dict.get("body"),
                                          post_id=post_instance.id)
        if comment_instance:
            saved_correctly += 1
        else:
            errors += 1
    update_ids_of(["comments"])
    return [len(response_data), saved_correctly, errors]


def sync_all_data():
    endpoints = [
        {"data_from": "users", "sync_function": sync_users},
        {"data_from": "posts", "sync_function": sync_posts},
        {"data_from": "comments", "sync_function": sync_comments}
    ]

    result_info = {}
    for sync in endpoints:
        [total_data, saved_correctly, errors] = sync_data_from(**sync)
        result_info[sync.get("data_from")] = {
            "total_data": total_data,
            "saved_correctly": saved_correctly,
            "errors": errors,
        }
    return result_info


@sync_data_router.get("/")
def sync_data():
    return sync_all_data()
