from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello_rest_api, name='home'),
    # Add other URL patterns here
]