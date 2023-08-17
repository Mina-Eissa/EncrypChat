from rest_framework import generics,status
from rest_framework.response import Response 
from ..serializers import MemberSerializer
from ..models import Member
from django.db import IntegrityError

class MemberCreateView(generics.CreateAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer