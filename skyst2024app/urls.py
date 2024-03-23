from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import LoginAPIView

urlpatterns = [
    path('testapi1/', views.hello_rest_api, name='home'),
    path('video/upload/', views.upload_video, name='upload_video'),
    path('video/get/<int:video_id>', views.get_video, name="get_video"),
    path('login/', LoginAPIView.as_view(), name='login'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)