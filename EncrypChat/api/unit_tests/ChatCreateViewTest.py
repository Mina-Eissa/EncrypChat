from datetime import date
from django.test import TestCase
from django.urls import reverse
from ..models import Member, Chat


class ChatCreateViewTest(TestCase):
    def setUp(self):
        self.member1_data = {
            'Email': 'mina@gmail.com',
            'FirstName': 'mina',
            'LastName': 'eissa',
            'BirthDate': date(2001, 8, 26),
            'Gender': 'Male',
            'PhoneNumber': '01012345678',
            'PersonalBio': 'Test bio',
            'Password': '1234password',
        }
        self.member1 = Member.objects.create(**self.member1_data)
        self.member2_data = {
            'Email': 'test2@example.com',
            'FirstName': 'marco',
            'LastName': 'emad',
            'BirthDate': date(2000, 5, 20),
            'Gender': 'Male',
            'PhoneNumber': '01012345678',
            'PersonalBio': 'Test bio',
            'Password': '1234password',
        }
        self.member2 = Member.objects.create(**self.member2_data)
        self.chat_data = {
            'MemOneID': self.member1.id,
            'MemTwoID': self.member2.id,
        }

    def test_chat_creation(self):
        url = reverse('chat-create')
        response = self.client.post(url, self.chat_data, format='json')
        #print(response.json())
        self.assertEqual(response.status_code, 201)  # HTTP status CREATED
