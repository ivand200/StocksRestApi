from django.shortcuts import render
from django.http import request, JsonResponse, Http404
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import UserSerializer
from rest_framework import viewsets
from rest_framework.parsers import JSONParser
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.decorators import permission_classes
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_auth.models import User
from rest_framework.generics import CreateAPIView


# Create your views here.
class UserCreateSet(CreateAPIView):
    authemtication_classes = [BasicAuthentication]
    permission_classes = [AllowAny]

    serializer_class = UserSerializer


"""
class UserViewSet(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication]
    permission_classes = [AllowAny]
    serializer_class = UserSerializer

    def get_queryset(self):
        user = self.request.user
        return Post.objects.filter(author=user)
"""
