from django.contrib.gis.db import models

class Post(models.Model):
    title = models.CharField(max_length=20)
    body = models.CharField(max_length=40)
    date = models.DateTimeField(auto_now_add=True)

