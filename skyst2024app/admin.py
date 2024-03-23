from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Video, Account

admin.site.register(Video)
admin.site.register(Account)