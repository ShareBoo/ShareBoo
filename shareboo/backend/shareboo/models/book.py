import uuid

from django.db import models

from .base import BaseModel
from .user import User
from .volume import Volume


class Book(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    volume = models.ForeignKey(Volume, on_delete=models.CASCADE)
    like_count = models.IntegerField()
    short_description = models.CharField(max_length=200)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)


class LendingStatus(models.IntegerChoices):
    LENDABLE = 10, "貸出可"
    LENDING = 20, "貸出中"
    UNLENDABLE = 30, "貸出不可"


class Lending(BaseModel):
    lending_status = models.IntegerField(choices=LendingStatus.choices)
    borrower = models.ForeignKey(User, on_delete=models.CASCADE)
    return_due_date = models.DateField()
