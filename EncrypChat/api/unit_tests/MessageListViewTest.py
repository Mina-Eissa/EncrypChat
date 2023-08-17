# tests.py

from django.test import TestCase
from django.urls import reverse
from datetime import date
from ..models import Chat, Message,Member

class MessageListViewTestCase(TestCase):
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
        self.message1 = Message.objects.create(ChatID=self.chat,Sender=self.member1, MsgBody='Hello', SendTime='2023-08-16T10:00:00Z')
        self.message2 = Message.objects.create(ChatID=self.chat,Sender=self.member1, MsgBody='Hi', SendTime='2023-08-16T11:00:00Z')

    def test_get_messages_for_chat(self):
        url = reverse('message-list', kwargs={'ChatID': self.chat.ChatID})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['MsgBody'], 'Hello')
        self.assertEqual(response.data[1]['MsgBody'], 'Hi')
