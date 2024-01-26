from rest_framework import generics, status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from ..models import Member
from ..serializers import MemberSerializer


class MemberDetailsView(generics.RetrieveAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    lookup_field = 'Email'

    def get_object(self):
        email = self.kwargs['Email']
        try:
            member = Member.objects.get(Email=email)
            return member
        except Member.DoesNotExist:
            return None

    def post(self, request, Email, *args, **kwargs):
        member = self.get_object()
        if member and member.check_password(request.data.get('Password')):
            # Password is valid
            serializer = self.get_serializer(member)
            return Response({'data': serializer.data}, status=status.HTTP_200_OK)
        else:
            # Password is invalid or member doesn't exist
            return Response({'detail': 'Invalid email or password'}, status=status.HTTP_401_UNAUTHORIZED)
