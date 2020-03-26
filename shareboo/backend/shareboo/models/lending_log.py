import uuid

from django.db import models

from .base import BaseModel
from .book import Book
from .user import User


class LendingLog(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrowing_user = models.ForeignKey(User, on_delete=models.CASCADE)
    checkout_datetime = models.DateTimeField()
    return_datetime = models.DateTimeField(null=True)
