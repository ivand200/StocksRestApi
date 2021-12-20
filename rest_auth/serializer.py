from rest_framework import serializers
from .models import User
from django.contrib.auth.hashers import make_password

def pass_validation(value):
    if not any(x.isupper() for x in value):
        raise serializers.ValidationError("Must be at least one capital letter")
    if len(value) <= 7:
        raise serializers.ValidationError("Must be at least 8 characters long")


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(validators = [pass_validation], write_only=True)
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def create(self, validated_data):
        user = User(
            email = self.validated_data['email'],
            username = self.validated_data['username']
        )
        password = self.validated_data['password']
        user.set_password(password)
        user.save()
        return user
