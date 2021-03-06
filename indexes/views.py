from django.shortcuts import render
from django.http import request, JsonResponse, Http404
from .models import Etf
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import EtfSerializer, EtfBondSerializer
from rest_framework.parsers import JSONParser
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from drf_yasg.utils import swagger_auto_schema

from django.contrib.auth.models import User
# Create your views here.


class EtfViewSet(viewsets.ViewSet):
    """
    All Etf
    """
    authentication_classes = [BasicAuthentication]
    permission_classes = [AllowAny]
    def list(self, request):
        queryset = Etf.objects.all()
        serializer = EtfSerializer(queryset, many=True)
        return Response(serializer.data)


class EtfBond(viewsets.ViewSet):
    """
    ETFs srted by momentum_3
    """
    authentication_classes = [BasicAuthentication]
    permission_classes = [AllowAny]

    def list(self, request):
        queryset = Etf.objects.filter(ticker__in=["LQD", "HYG", "SHV"]).order_by("-momentum_3")
        serializer = EtfBondSerializer(queryset, many=True)
        return Response(serializer.data)



"""
class TestView(viewsets.ViewSet):
    authentication_classes = [BasicAuthentication]
    permission_classes = [AllowAny]
    def list(self, request, format=None):
        content = {
        'user': str(request.user)
        }
        return Response(content)

    def create(self, request, name, code):
        user = User.objects.create_user(name, password=code)
        user.save()
        return Response(user)
"""
