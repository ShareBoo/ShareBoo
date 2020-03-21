from uuid import UUID
from dataclasses import dataclass

from .authentication import Authentication


@dataclass(frozen=True)
class UserId:
    value: UUID


@dataclass
class IconUrl:
    value: str


@dataclass
class User:
    user_id: UserId
    icon_url: IconUrl
    authentication: Authentication
