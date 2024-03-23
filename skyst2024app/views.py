from django.shortcuts import render
from rest_framework import serializers
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .models import Video
from django.http import JsonResponse, FileResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from .video_compress import video_compress
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model, authenticate, login, logout
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from .serializers import UserLoginSerializer

# Create your views here.
def login(request):
    email = request['email']
    password = request['password']
    user = authenticate(request, username=email, password=password)
    if user:
        login(request, user)
        return 

'''
{"username": "ohjuhyun1",
"email": "ohjuhyun1@gmail.com",
"password": "ohrora555"}
'''

User = get_user_model()

class LoginAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']
            user = authenticate(request, username=email, password=password)
            if user:
                login(request, user)
                return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
            return Response({'message': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    



@api_view(['GET', 'POST'])
@permission_classes([AllowAny]) #HasAPIKey로 바꿀 수 있음
def hello_rest_api(request):
    data = {'message': 'Hello, REST API!'}
    return Response(data)
    

@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def upload_video(request):
    if request.method == "POST":
        video_file = request.FILES.get('video')
        if video_file:
            video = Video(file=video_file)
            #video = video_compress(video)
            video.save()
            return JsonResponse({'message': 'Video uploaded successfully'}, status=200)
        return JsonResponse({'error': 'Invalid request'}, status=400)

@api_view(['GET', 'POST'])
def get_video(request, video_id):
    try:
        video = Video.objects.get(id=video_id)
        return FileResponse(video.file.open(), content_type='video/webm')
    except Video.DoesNotExist:
        raise Http404('Video does not exist')