from django.db import models


class Profile(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    education = models.CharField(max_length=20)
    image = models.FilePathField(path="/img")