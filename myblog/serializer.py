from rest_framework.serializers import ModelSerializer
from .models import Post
from rest_auth.models import User


class UserEmailSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']


class PostSerializer(ModelSerializer):
    author = UserEmailSerializer(read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'author', 'created_at', 'title', 'content']
