from rest_framework import serializers
from . import models

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = models.User
    fields = [
      'username',
      'password',
      'email'
    ]
    
class ChatSerializer(serializers.ModelSerializer):
  class Meta:
    model = models.Chat
    fields = '__all__'
    
class ChatMemberSerializer(serializers.ModelSerializer):
  class Meta:
    model = models.ChatMember
    fields = '__all__'

class MessageSerializer(serializers.ModelSerializer):
  class Meta:
    model = models.Message
    fields = '__all__'