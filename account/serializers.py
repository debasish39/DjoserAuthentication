from djoser.serializers import UserCreateSerializer
from account.models import User

class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model=User
        fields=('id', 'email', 'name', 'password')
        
        
# account/serializers.py

from djoser.serializers import SendEmailResetSerializer
from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()

class CustomResendActivationSerializer(SendEmailResetSerializer):
    def validate_email(self, value):
        user = User.objects.filter(email=value).first()
        if user and user.is_active:
            raise serializers.ValidationError("User is already active.")
        return value
