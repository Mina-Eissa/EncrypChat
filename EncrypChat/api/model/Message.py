from django.db import models
from .Chat import Chat
from .Member import Member

class Message(models.Model):
    MsgID = models.AutoField(primary_key=True)
    ChatID = models.ForeignKey(Chat, on_delete=models.CASCADE)
    Sender = models.ForeignKey(Member, on_delete=models.CASCADE,null=True,blank=True)
    SendTime = models.DateTimeField(auto_now_add=True)
    MsgBody = models.TextField(blank=True, null=True)
    MsgImage = models.BinaryField(blank=True, null=True)

    def __str__(self):
        return f"Message {self.MsgID} in Chat {self.ChatID.ChatID} at {self.SendTime}"