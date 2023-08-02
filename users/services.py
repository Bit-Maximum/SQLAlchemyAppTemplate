from dependency_injector.wiring import inject, Provide
from containers import Container

from database.repository import AbstractRepository
from database.unit_of_work import UnitOfWork
from users.database.models import User

from database.exseptions import NotFoundException


@inject
def list_users(repository: AbstractRepository = Provide[Container.users_repository]):
    return repository.list()


@inject
def get_user(value, attribute: str = "id", repository: AbstractRepository = Provide[Container.users_repository]):
    return repository.get(value, attribute=attribute)


@inject
def create_user(username: str, unit_of_work: UnitOfWork = Provide[Container.users_uow]):
    with unit_of_work:
        unit_of_work.repository.save(User(username=username))
        unit_of_work.commit()


@inject
def update_users_balance(
        value, balance_change: float, attribute: str = "id", unit_of_work: UnitOfWork = Provide[Container.users_uow]):
    with unit_of_work:
        users = unit_of_work.repository.get(value, attribute=attribute)
        for user in users:
            user.balance += balance_change
            unit_of_work.repository.update(user)
        unit_of_work.commit()


# @inject
# def get_user_by_id(id: int, repository: AbstractRepository = Provide[Container.users_repository]):
#     try:
#         return repository.get_by_id(id=id)
#     except NotFoundException:
#         print(User not found: , exc)
#         return None
