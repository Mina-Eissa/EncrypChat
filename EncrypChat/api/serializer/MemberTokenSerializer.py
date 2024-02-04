from rest_framework import serializers
from ..models import MemberToken


class MemberTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = MemberToken
        fields = ('token', 'token_expiry')
