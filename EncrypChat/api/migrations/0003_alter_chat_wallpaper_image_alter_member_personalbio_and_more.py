# Generated by Django 4.2.1 on 2023-08-17 09:06

import api.model.Chat
import api.model.Member
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_message_sender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='Wallpaper_Image',
            field=models.ImageField(blank=True, null=True, upload_to=api.model.Chat.chat_wallpaper_path),
        ),
        migrations.AlterField(
            model_name='member',
            name='PersonalBio',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='PersonalImage',
            field=models.ImageField(null=True, upload_to=api.model.Member.member_image_path),
        ),
    ]
