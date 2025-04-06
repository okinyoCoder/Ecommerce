from django.shortcuts import render
from django.contrib.auth import authenticate, login
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from .serializers import CustomUserSerializer
from django.contrib.auth import get_user_model


@api_view(['POST'])
def login_view(request):
    email = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, email=email, password=password)
    if user is not None:
        token, created = Token.objects.get_or_create(user=user)
        login(request, user)
        return Response({'token': token.key}, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    
@api_view(['POST'])
def register_view(request):
    if request.method == "POST":
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            user = get_user_model().objects.get(username=request.data['username'])
            token = Token.objects.get(user=user)
            serializer = CustomUserSerializer(user)
            data = {
                'response': 'User registered successfully',
                'token': token.key,
                'user': serializer.data,
            }
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        