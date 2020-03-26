from django.db import models


class User(models.Model):
    uid = models.CharField(max_length=100)
    photo_url = models.URLField()
