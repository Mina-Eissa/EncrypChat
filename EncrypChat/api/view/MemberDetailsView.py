from rest_framework import generics
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from ..models import Member
from ..serializers import MemberSerializer


class MemberDetailsView(generics.RetrieveAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    lookup_field = 'Email'

