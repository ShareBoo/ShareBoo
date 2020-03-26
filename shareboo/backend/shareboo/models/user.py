from django.db import models

from .base import BaseModel


class User(BaseModel):
    uid = models.CharField(max_length=100)
    photo_url = models.URLField()
