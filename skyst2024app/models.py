from django.db import models

# Create your models here.
class Video(models.Model):
    title = models.CharField(max_length=255, default="")
    user = models.CharField(max_length = 100, default="")
    time = models.IntegerField(default = 0)
    file = models.FileField(upload_to=f"videos/{user}/")
    question = models.CharField(max_length = 500, default="Default")

class Account(models.Model):
    email = models.CharField(max_length = 200)
    password = models.CharField(max_length = 200)
    videos = models.CharField(max_length = 10000)