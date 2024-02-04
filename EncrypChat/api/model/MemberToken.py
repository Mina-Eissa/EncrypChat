from django.db import models
from .Member import Member
from django.utils import timezone


class MemberToken(models.Model):
    member = models.OneToOneField(Member, on_delete=models.CASCADE)
    token = models.CharField(max_length=255, unique=True, db_index=True)
    token_expiry = models.DateTimeField()

    def __str__(self):
        return f"{self.member.FirstName} {self.member.LastName} has token {self.token}"
