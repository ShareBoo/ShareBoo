from abc import ABCMeta, abstractmethod

from .user import User, UserId


class UserRepositoryInterface(metaclass=ABCMeta):
    @abstractmethod
    def get_user(self, user_id: UserId) -> User:
        pass

    @abstractmethod
    def update_user(self, user: User) -> None:
        pass
