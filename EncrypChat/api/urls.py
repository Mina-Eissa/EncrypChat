from django.urls import path
from .views import Message_List

urlpatterns = [
    path('chat/<uuid:ChatID>/messages',Message_List,name='message-list'),
]