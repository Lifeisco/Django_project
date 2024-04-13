from django.db import models


class User(models.Model):
    username = models.CharField(max_length=20, blank=False)
    email = models.EmailField(max_length=40, blank=False)
    password = models.CharField(max_length=20, blank=False)
