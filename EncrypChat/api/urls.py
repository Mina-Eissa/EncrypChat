from django.urls import path
from .views import *

urlpatterns = [
    path('chat/<uuid:ChatID>/messages',Message_List,name='message-list'),
    path('chat/send/',Message_Create,name='message-create'),

]