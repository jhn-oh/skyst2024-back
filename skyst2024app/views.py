from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .models import Video
from django.http import JsonResponse, FileResponse, Http404
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@api_view(['GET', 'POST'])
@permission_classes([AllowAny]) #HasAPIKey로 바꿀 수 있음
def hello_rest_api(request):
    data = {'message': 'Hello, REST API!'}
    return Response(data)

@api_view(['GET', 'POST'])
def login(request):
    pass

@api_view(['GET', 'POST'])
def upload_video(request):
    if request.method == "POST":
        video_file = request.FILES.get('video')
        if video_file:
            video = Video(file=video_file)
            video.save()
            return JsonResponse({'message': 'Video uploaded successfully'}, status=200)
        return JsonResponse({'error': 'Invalid request'}, status=400)

def get_video(request, video_id):
    try:
        video = Video.objects.get(id=video_id)
        return FileResponse(video.file.open(), content_type='video/webm')
    except Video.DoesNotExist:
        raise Http404('Video does not exist')