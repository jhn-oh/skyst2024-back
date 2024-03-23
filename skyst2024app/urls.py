from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import LoginAPIView

urlpatterns = [
    path('testapi1/', views.hello_rest_api, name='home'),
    #path('video/upload/', views.upload_video2, name='upload_video'),
    path('video/get/<int:video_id>', views.get_video, name="get_video"),
    path('login/', views.login, name='login'),
    path('video/upload/', views.get_s3_url, name="get_s3_url")
    path('video/get/<str:username>', views.get_all_video, name="get_all_video")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)