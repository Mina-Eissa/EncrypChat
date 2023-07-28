from django.test import TestCase
from datetime import date
from ..models import Member

class MemberModelTest(TestCase):
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
    
    def test_member_creation(self):
        # Check if the Member instance was created correctly with the provided data
        self.assertEqual(self.member.Email, self.member_data['Email'])
        self.assertEqual(self.member.FirstName, self.member_data['FirstName'])
        self.assertEqual(self.member.LastName, self.member_data['LastName'])
        self.assertEqual(self.member.BirthDate, self.member_data['BirthDate'])
        self.assertEqual(self.member.Gender, self.member_data['Gender'])
        self.assertEqual(self.member.PhoneNumber, self.member_data['PhoneNumber'])
        self.assertEqual(self.member.PersonalBio, self.member_data['PersonalBio'])
        # Password should be hashed, so we need to check using the check_password method
        self.assertTrue(self.member.check_password(self.member_data['Password']))

    def test_age_calculation(self):
        # Create a Member instance with a specific birth date
        birth_date = date(1990, 6, 15)
        member = Member.objects.create(BirthDate=birth_date)

        # Calculate the expected age based on the birth date and today's date
        today = date.today()
        expected_age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))

        # Call the Age function on the Member instance and check if it matches the expected age
        self.assertEqual(member.Age, expected_age)
