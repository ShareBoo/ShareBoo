from typing import List

from shareboo.domain.user.user_repository_interface import UserRepositoryInterface
from shareboo.domain.user.user import User, UserId, IconUrl
from shareboo.domain.user.authentication import (
    Authentication,
    AuthenticationId,
    TwitterId,
    TwitterToken,
)


class InMemoryUserRepository(UserRepositoryInterface):
    users: List[User]

    def __init__(
        self,
        users: List[User] = [
            User(
                user_id=UserId("123"),
                icon_url=IconUrl("https://image.com/image.png"),
                authentication=Authentication(
                    authentication_id=AuthenticationId("auth_id"),
                    twitter_id=TwitterId("twiiter"),
                    twitter_token=TwitterToken("token"),
                ),
            ),
            User(
                user_id=UserId("456"),
                icon_url=IconUrl("https://image.com/image2.png"),
                authentication=Authentication(
                    authentication_id=AuthenticationId("auth_id"),
                    twitter_id=TwitterId("twiiter"),
                    twitter_token=TwitterToken("token"),
                ),
            ),
        ],
    ):
        self.users = users

    def get_user(self, user_id: UserId) -> User:
        for user in self.users:
            if user_id == user.user_id:
                return user
        raise Exception

    def update_user(self, user: User) -> None:
        target_user = user
        for user in self.users:
            if user.user_id == target_user.user_id:
                user = target_user
                return None
        raise Exception
