from django.db import models

# Create your models here.
class Video(models.Model):
    title = models.CharField(max_length=255, default="")
    user = models.CharField(max_length = 100, default="")
    time = models.IntegerField(default = 0)
    file = models.FileField(upload_to=f"videos/{user}/")
    question = models.CharField(max_length = 500, default="Default")
    def __str__(self):
        return self.title


class Account(models.Model):
    username = models.CharField(max_length = 100, default="no_username")
    email = models.CharField(max_length = 200)
    password = models.CharField(max_length = 200)
    videos = models.CharField(max_length = 10000, blank=True)

    def __str__(self):
        return self.username


class VideoInfo(models.Model):
    video_id = models.CharField(max_length = 100)
    question = models.CharField(max_length = 255)
    time = models.IntegerField()

    def __str__(self):
        return self.video_id