from rest_framework.generics import ListAPIView
from ..serilaizers import MessageSerializer
from ..models import Message,Chat


class MessageListView(ListAPIView):
    serializer_class = MessageSerializer

    def get_queryset(self):
        ID = self.kwargs['ChatID']
        return Message.objects.filter(ChatID = ID).order_by('SendTime')
    
