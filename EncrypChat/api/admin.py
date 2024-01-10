from django.contrib import admin

from .models import Member, Message, Chat

admin.site.register(Member)
admin.site.register(Message)
admin.site.register(Chat)
