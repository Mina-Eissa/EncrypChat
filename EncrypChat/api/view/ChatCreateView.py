from rest_framework import generics
from ..models import Chat
from ..serializers import ChatSerializer

class ChatCreateView(generics.CreateAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer