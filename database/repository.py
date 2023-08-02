from abc import ABC, abstractmethod


class AbstractRepository(ABC):
    def __init__(self, session):
        self.session = session

    @abstractmethod
    def get(self, value, attribute: str = "id"):
        raise NotImplementedError()

    @abstractmethod
    def list(self):
        raise NotImplementedError()

    @abstractmethod
    def save(self, obj):
        raise NotImplementedError()

    @abstractmethod
    def update(self, obj):
        raise NotImplementedError()

    # @abstractmethod
    # def get_by_id(self, id: int):
    #     raise NotImplementedError()
