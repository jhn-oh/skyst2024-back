from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
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
from rest_framework.parsers import JSONParser
from rest_framework import status
#from .serializers import AccountSerializer
import json
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password, check_password
from time import time
username = "skyst2024"

# Create your views here.
@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def login_user1(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username)
        login(request, user)
        return JsonResponse({"success": True, "message": "Login successful."})
        '''
        if user is not None:
            login(request, user)
            return JsonResponse({"success": True, "message": "Login successful."})
        else:
            return JsonResponse({"success": False, "message": "Invalid credentials."})
        '''
@csrf_exempt
def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.get(username=username)
        stored_password = user.password
        if check_password(password, stored_password):
            login(request, user)
            return JsonResponse({"success": True, "message": "Login successful."})
        else:
            return JsonResponse({"success": False, "message": "Invalid credentials."})
        user = authenticate(request, username=username, password=make_password(password))
        if user is not None:
            # The credentials are valid
            login(request, user)
            return JsonResponse({"success": True, "message": "Login successful."})
        else:
            # Authentication failed
            return JsonResponse({"success": False, "message": "Invalid credentials."})
        # 왜안돼!!!!!!

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
        question = request.POST.get('question')
        unix_timestamp = round(time())
        video = Video(user = username, time = unix_timestamp, title = f"{username}///{unix_timestamp}", question = question, file = video_file)
        #video = video_compress(video)
        video.save()
        return JsonResponse({'message': 'Video uploaded successfully'}, status=200)
        if video_file:
            unix_timestamp = round(time())
            video = Video(user = username, time = unix_timestamp, title = f"{username}///{unix_timestamp}", question = question, file = video_file)
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