import sqlalchemy.exc
from database.exseptions import NotFoundException

from database.repository import AbstractRepository
from users.database.models import User


class UserRepository(AbstractRepository):
    def get(self, value, attribute: str = "id"):
        if hasattr(User, attribute):
            return self.session.query(User).filter(getattr(User, attribute) == value).all()
        else:
            return []

    def list(self):
        return self.session.query(User).all()

    def save(self, obj):
        self.session.add(obj)

    def update(self, obj):
        self.session.add(obj)

    # def get_by_id(self, id: int):
    #     try:
    #         return self.session.query(User).filter_by(id=id).one()
    #     except sqlalchemy.exc.NoResultFound as exc:
    #         raise NotFoundException(exc)
