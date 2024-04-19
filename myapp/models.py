from django.db import models


class User(models.Model):
    username = models.CharField(max_length=20, blank=False)
    email = models.EmailField(max_length=40, blank=False)
    password = models.CharField(max_length=20, blank=False)


class Category(models.Model):
    category_name = models.CharField(max_length=30, blank=False)

    def __str__(self):
        return self.category_name


class Ad(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=64, blank=False)
    text = models.TextField(blank=False)


class Response(models.Model):
    text = models.CharField(max_length=256, blank=False)
    ads = models.ForeignKey(Ad, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
