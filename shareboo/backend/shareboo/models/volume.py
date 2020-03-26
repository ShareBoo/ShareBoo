import uuid

from django.db import models

from .base import BaseModel


class Volume(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=500)
    publisher = models.CharField(max_length=300)
    author = models.CharField(max_length=300)
