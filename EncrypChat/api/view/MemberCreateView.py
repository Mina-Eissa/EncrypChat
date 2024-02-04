from rest_framework import generics,status
from rest_framework.response import Response 
from ..serializers import MemberSerializer, MemberTokenSerializer
from ..models import Member, MemberToken
from rest_framework_simplejwt.tokens import RefreshToken
from datetime import timedelta
from ..CurrentTimeZone import get_timenow

class MemberCreateView(generics.CreateAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Handle exitance of member
        email = serializer.validated_data.get('Email')
        existing_user = Member.objects.filter(Email=email).first()
        if existing_user:
            return Response({'message': 'Member already exists'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            try:
                member = serializer.save()

                # Generate JWT token
                refresh = RefreshToken.for_user(member)
                exp_date = get_timenow() + timedelta(hours=1)
                refresh.access_token.set_exp(str(exp_date))
                token_data = MemberToken.objects.create(
                    member=member, token=str(refresh.access_token), token_expiry=exp_date)
                return Response(MemberTokenSerializer(token_data).data, status=status.HTTP_201_CREATED)

            except Exception as e:
                # Here, we catch any exception and raise a custom error with a more descriptive message
                raise ValueError(
                    "An error occurred while saving member or generating token: " + str(e))
