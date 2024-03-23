from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('testapi1/', views.hello_rest_api, name='home'),
    path('api/video/upload', views.upload_video, name='upload_video')

    # Add other URL patterns here
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)