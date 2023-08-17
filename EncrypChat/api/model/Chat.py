from django.db import models
from .Member import Member
import uuid

def chat_wallpaper_path(instance, filename):
    # This function generates the path for storing the image based on the Chat's ID
    return f'chats_wallpaper_images/{instance.ChatID}/{filename}'

class Chat(models.Model):
    ChatID = models.CharField(max_length=255, primary_key=True, default=uuid.uuid4, editable=False)
    MemOneID = models.OneToOneField(Member, on_delete=models.CASCADE, related_name='mem1')
    MemTwoID = models.OneToOneField(Member, on_delete=models.CASCADE, related_name='mem2')
    Wallpaper_Image = models.ImageField(upload_to=chat_wallpaper_path)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.ChatID
    
    def get_chat_wallpaper_path(self,filename):
        return chat_wallpaper_path(self,filename)