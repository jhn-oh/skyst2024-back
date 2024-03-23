from django.db import models

# Create your models here.
class Video(models.Model):
    title = models.CharField(max_length=255)
    #id = models.IntegerField()
    file = models.FileField(upload_to='videos/')