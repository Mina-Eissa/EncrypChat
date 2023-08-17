from rest_framework.generics import CreateAPIView
from ..serializers import MessageSerializer
from ..models import Message,Chat


class MessageCreateView(CreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


