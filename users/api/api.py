import typing

from fastapi import APIRouter
from starlette.responses import JSONResponse

from users.api.schema import UserCreateSchema, UserUpdateBalanceSchema
from users.services import list_users, get_user, create_user, update_users_balance

router = APIRouter()


@router.get('/')
def list_users_route():
    return list_users()


@router.get('/{value};{attribute}')
def get_user_route(value, attribute: str = "id"):
    return get_user(value, attribute=attribute)


@router.post('/')
def create_user_route(user_create: UserCreateSchema):
    create_user(user_create.username)
    return {"ack": True}


@router.patch('/update_balance/{value};{attribute}')
def update_users_balance_route(value, balance_change: UserUpdateBalanceSchema, attribute: str = "id"):
    update_users_balance(value, balance_change.balance_change, attribute=attribute)
    return {"ack": True}


# Отключено из-за ненадобности
# @app.get('/users/{id}')
# async def get_user_by_id_route(id: int):
#     return get_user_by_id(id=id)