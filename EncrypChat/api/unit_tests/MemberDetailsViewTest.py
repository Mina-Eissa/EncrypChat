from datetime import date
from django.test import TestCase
from django.urls import reverse
from ..models import Member

class MemberDetailsViewTest(TestCase):
    def setUp(self):
        self.member1_data = {
            'Email': 'test1@example.com',
            'FirstName': 'mina',
            'LastName': 'eissa',
            'BirthDate': date(2001, 8, 26),
            'Gender': 'Male',
            'PhoneNumber': '01012345678',
            'PersonalBio': 'Test bio',
            'Password': '1234password',
        }
        Member.objects.create(**self.member1_data)
    
    def test_retrive_member(self):
        url = reverse('member-details',kwargs={'Email':self.member1_data['Email']})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)