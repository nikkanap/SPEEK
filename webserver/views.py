from django.shortcuts import render
from rest_framework import views, generics, viewsets
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from . import models
from . import serializers


# Create your views here.
class UserView(viewsets.ModelViewSet):
  """
  POST /api/users/
  PUT /api/users/<int:pk>/update/
  {
    "username": "testUsername123"
    "password": "your_pass"
    "email_address": "testUsername@email.com"  
  }
  
  Patch payloads can contain at least one attribute:
  PATCH /api/users/<int:pk>/update/
  {
    "username": "modifiedUsername123"
  }
  """
  
  queryset = models.User.objects.all()
  serializer_class = serializers.UserSerializer
  parser_classes = [MultiPartParser, FormParser]
  permission_classes = [IsAuthenticated | IsAdminUser]


class ChatView(viewsets.ModelViewSet):
  """
  POST /api/chats/
  PUT /api/chats/<int:pk>/update/
  {
    "is_groupchat": <default=False>
    "chat_name": "Test Chat Name"  
  }
  
  Patch payloads can contain at least one attribute:
  PATCH /api/chats/<int:pk>/update/
  {
    "chat_name": "Modified Chat Name"
  }
  """
  
  queryset = models.Chat.objects.all()
  serializer_class = serializers.ChatSerializer
  parser_classes = [MultiPartParser, FormParser]
  permission_classes = [IsAuthenticated | IsAdminUser]
  

class ChatMemberView(viewsets.ModelViewSet):
  """
  POST /api/chat-members/
  PUT /api/chat-members/<int:pk>/update/
  {
    "member": <user_id>
    "chat": <chat_id>
    "nickname": "Test Nickname"  
  }
  
  Patch payloads can contain at least one attribute:
  PATCH /api/chat-members/<int:pk>/update/
  {
    "nickname": "Modified Nickname"
  }
  """
  
  queryset = models.ChatMember.objects.all()
  serializer_class = serializers.ChatMemberSerializer
  parser_classes = [MultiPartParser, FormParser]
  permission_classes = [IsAuthenticated | IsAdminUser]
  
  
class MessageView(viewsets.ModelViewSet):
  """
  POST /api/messages/
  PUT /api/messages/<int:pk>/update/
  {
    "chat": <chat_id>
    "message": "I like eggs"
  }
  
  Patch payloads can contain at least one attribute:
  PATCH /api/messages/<int:pk>/update/
  {
    "message": "I dislike eggs"
  }
  """
  
  queryset = models.ChatMember.objects.all()
  serializer_class = serializers.ChatMemberSerializer
  parser_classes = [MultiPartParser, FormParser]
  permission_classes = [IsAuthenticated | IsAdminUser]
