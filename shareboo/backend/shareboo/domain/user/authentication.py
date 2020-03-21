from uuid import UUID
from dataclasses import dataclass


@dataclass
class AuthenticationId:
    value: UUID


@dataclass
class TwitterId:
    value: str


@dataclass
class TwitterToken:
    value: str


@dataclass
class Authentication:
    authentication_id: AuthenticationId
    twitter_id: TwitterId
    twitter_token: TwitterToken
