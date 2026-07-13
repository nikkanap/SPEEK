from django.urls import include, path
from . import views

urlpatterns = [
  path('users/', views.UserView.as_view({'get':'list', 'post':'create'})),
  path('users/<int:pk>/', views.UserView.as_view({'get':'retrieve'})),
  path('users/<int:pk>/update/', views.UserView.as_view({'put':'update', 'patch':'partial_update'})),
  path('users/<int:pk>/delete/', views.UserView.as_view({'delete':'destroy'})),
  
  path('chats/', views.ChatView.as_view({'get':'list', 'post':'create'})),
  path('chats/<int:pk>/', views.ChatView.as_view({'get':'retrieve'})),
  path('chats/<int:pk>/update/', views.ChatView.as_view({'put':'update', 'patch':'partial_update'})),
  path('chats/<int:pk>/delete/', views.ChatView.as_view({'delete':'destroy'})),
  
  path('chat-members/', views.ChatMemberView.as_view({'get':'list', 'post':'create'})),
  path('chat-members/<int:pk>/', views.ChatMemberView.as_view({'get':'retrieve'})),
  path('chat-members/<int:pk>/update/', views.ChatMemberView.as_view({'put':'update', 'patch':'partial_update'})),
  path('chat-members/<int:pk>/delete/', views.ChatMemberView.as_view({'delete':'destroy'})),
  
  path('messages/', views.MessageView.as_view({'get':'list', 'post':'create'})),
  path('messages/<int:pk>/', views.MessageView.as_view({'get':'retrieve'})),
  path('messages/<int:pk>/update/', views.MessageView.as_view({'put':'update', 'patch':'partial_update'})),
  path('messages/<int:pk>/delete/', views.MessageView.as_view({'delete':'destroy'})),
]
