from django.db import models
from django.contrib.auth.hashers import make_password,check_password
from datetime import date
import random
import string

def generate_unique_id():
    letters = string.ascii_uppercase
    return ''.join(random.choice(letters) for _ in range(7))

def member_image_path(instance, filename):
    # This function generates the path for storing the image based on the Member's ID
    return f'images/{instance.ID}/{filename}'

class Member(models.Model):
    GenderTypes = [('Male', 'Male'), ('Female', 'Female')]
    ID = models.CharField(max_length=7, unique=True, default=generate_unique_id, primary_key=True)
    Email = models.EmailField(unique=True)
    FirstName = models.CharField(max_length=255, default='bruno')
    LastName = models.CharField(max_length=255, default='mars')
    BirthDate = models.DateField()
    Gender = models.CharField(max_length=255, choices=GenderTypes, default='Male')
    PhoneNumber = models.CharField(max_length=255, default='01012345678')
    CreatedAt = models.DateTimeField(auto_now_add=True)
    PersonalImage = models.ImageField(upload_to=member_image_path,null=True)
    PersonalBio = models.TextField(blank=True)
    Password = models.CharField(max_length=255)


    def __str__(self):
        return f'{self.FirstName} {self.LastName}'
    
    def save(self, *args, **kwargs):
        # Hash the password before saving
        self.Password = make_password(self.Password)
        super().save(*args, **kwargs)

        
    @property
    def Age(self):
        today = date.today() 
        age = today.year - self.BirthDate.year - ((today.month, today.day) < (self.BirthDate.month, self.BirthDate.day))
        return age

    @classmethod
    def generate_unique_id(cls):
        while True:
            unique_id = generate_unique_id()
            try:
                with models.transaction.atomic():
                    cls.objects.create(ID=unique_id)
                return unique_id
            except models.IntegrityError:
                pass

    def check_password(self,tempPassword):
        return check_password(tempPassword, self.Password)


