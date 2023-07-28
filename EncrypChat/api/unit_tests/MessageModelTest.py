from datetime import date
from django.test import TestCase
from ..models import Member, Chat, Message
from django.core.files.uploadedfile import SimpleUploadedFile
from PIL import Image
import io


class MessageModelTest(TestCase):

    def setUp(self):
        self.member1_data = {
            'Email': 'test1@example.com',
            'FirstName': 'mina',
            'LastName': 'kero',
            'BirthDate': date(1999, 1, 15),
            'Gender': 'Male',
            'PhoneNumber': '01012345678',
            'PersonalBio': 'Test bio',
            'Password': '1234password',
        }
        self.member1 = Member.objects.create(**self.member1_data)
        self.member2_data = {
            'Email': 'test2@example.com',
            'FirstName': 'kero',
            'LastName': 'emad',
            'BirthDate': date(1999, 10, 24),
            'Gender': 'Male',
            'PhoneNumber': '01012345678',
            'PersonalBio': 'Test bio',
            'Password': '1234password',
        }
        self.member2 = Member.objects.create(**self.member2_data)

        # Create a temporary image file
        image_data = io.BytesIO()
        image = Image.new('RGB', (100, 100), color='red')
        image.save(image_data, 'png')
        image_data.seek(0)

        # Use SimpleUploadedFile to create an image file that can be used for testing
        wallpaper_image = SimpleUploadedFile(
            'test_chat_wallpaper.png', image_data.read(), content_type='image/png')
        self.chat_data = {
            'MemOneID': self.member1,
            'MemTwoID': self.member2,
            'Wallpaper_Image': wallpaper_image,
        }
        self.chat = Chat.objects.create(**self.chat_data)
        self.chat_data['Wallpaper_Image'] = self.chat.get_chat_wallpaper_path(
            'test_chat_wallpaper.png')

        self.message_data = {
            'ChatID': self.chat,
            'MsgBody': "Hi,\n welcome to my app",
        }
        self.message = Message.objects.create(**self.message_data)

    def test_chat_creation(self):
        # Check if the Chat instance was created correctly with the provided data
        self.assertEqual(self.message.ChatID, self.message_data['ChatID'])
        self.assertEqual(self.message.MsgBody, self.message_data['MsgBody'])
