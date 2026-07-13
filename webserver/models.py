from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model() # get Django's default user model

# Create your models here.  
class Chat(models.Model):
  is_groupchat = models.BooleanField(default=False)
  chat_name = models.CharField(max_length=200, null=True, blank=True)
  date_created = models.DateTimeField(auto_now_add=True)
  
  def __str__(self):
    return str(self.pk)
  
class ChatMember(models.Model):
  member = models.ForeignKey(User, on_delete=models.CASCADE)
  chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
  nickname = models.CharField(max_length=100)
  date_added = models.DateTimeField(auto_now_add=True)
  
  def __str__(self):
    return f'{self.chat} - {self.member}'
  
class Message(models.Model):
  chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
  message = models.TextField()
  date_sent = models.DateTimeField(auto_now_add=True)
  date_edited = models.DateTimeField(null=True, blank=True)
  
  def __str__(self):
    return f'{self.chat} - {self.date_edited if self.date_edited else self.date_sent}'
  