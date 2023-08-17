from datetime import date
from django.test import TestCase
from django.urls import reverse


class MemberCreateViewTest(TestCase):
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
        self.member2_data = {
            'Email': 'test1@example.com',
            'Password': '1234password',
        }
        self.member3_data = {
            'Email': 'test1@example.com',
            'FirstName': 'kero',
            'LastName': 'emad',
            'BirthDate': date(1999, 10, 24),
            'Gender': 'Male',
            'PhoneNumber': '01012345678',
            'PersonalBio': 'Test bio',
            'Password': '1234password',
        }

    def test_member_creation_success(self):
        url = reverse('member-create')
        response = self.client.post(url, self.member1_data, format='json')
        #print(response.json())
        self.assertEqual(response.status_code, 201)  # HTTP status CREATED

    def test_member_creation_failure(self):
        url = reverse('member-create')
        response = self.client.post(url, self.member2_data, format='json')
        #print(response.json())
        self.assertEqual(response.status_code, 400)  # HTTP status BAD_REQUEST

    def test_email_duplication(self):
        url = reverse('member-create')
        self.client.post(url, self.member1_data, format='json')
        response = self.client.post(url, self.member3_data, format='json')
        #print(response.json())
        self.assertEqual(response.status_code, 400)  # HTTP status BAD_REQUEST
