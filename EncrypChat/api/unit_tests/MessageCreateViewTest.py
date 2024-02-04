# tests.py

from django.test import TestCase
from django.urls import reverse
from datetime import date
from ..models import Chat, Message, Member


class MessageCreateViewTestCase(TestCase):
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
        self.chat_data = {
            'MemOneID': self.member1,
            'MemTwoID': self.member2,
        }
        self.chat = Chat.objects.create(**self.chat_data)
        self.message_data = {
            'ChatID': self.chat.ChatID,
            'Sender': self.member1.id,
            'MsgBody': 'Hello',
            'SendTime': '2023-08-16T10:00:00Z'
        }

    def test_send_message(self):
        url = reverse('message-create')
        response = self.client.post(url, self.message_data, format='json')
        self.assertEqual(response.status_code, 201)  # HTTP Created
