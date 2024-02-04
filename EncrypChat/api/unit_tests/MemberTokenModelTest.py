from django.test import TestCase
from datetime import date, datetime, timedelta
from ..models import Member, MemberToken
from ..CurrentTimeZone import get_timenow
from rest_framework_simplejwt.tokens import RefreshToken


class MemberTokenModelTest(TestCase):
    def setUp(self):
        self.member_data = {
            'Email': 'test@example.com',
            'FirstName': 'John',
            'LastName': 'Doe',
            'BirthDate': date(1990, 6, 15),
            'Gender': 'Male',
            'PhoneNumber': '01012345678',
            'PersonalBio': 'Test bio',
            'Password': '1234password',
        }
        self.member = Member.objects.create(**self.member_data)
        exp_date = get_timenow() + timedelta(hour=1)
        refresh = RefreshToken.for_user(self.member)
        refresh.access_token.set_exp(str(exp_date))
        self.member_token_data = {
            'member': self.member,
            'token': str(refresh.access_token),
            'token_expiry': exp_date
        }
        self.member_token = MemberToken.objects.create(
            **self.member_token_data)

    def test_member_token_creation(self):
        # Check if the MemberToken instance was created correctly with the provided data
        self.assertEqual(self.member_token.member,
                         self.member_token_data['member'])
        self.assertEqual(self.member_token.token,
                         self.member_token_data['token'])
        self.assertEqual(self.member_token.token_expiry,
                         self.member_token_data['token_expiry'])
