from django.shortcuts import render, get_object_or_404
from django.http import request, JsonResponse, Http404
from .models import Stock, Index
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.permissions import IsAdminUser
from rest_framework.decorators import permission_classes
from rest_framework.response import Response
from .serializer import (StockSerializer, StockAvgMomentumSerializer,
                         StockDivSerializer, StockMomSerializer)
from rest_framework.parsers import JSONParser
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
# Create your views here.


class StockViewSet(viewsets.ViewSet):
    """
    List of all stocks
    """
    authentication_classes = [BasicAuthentication]
    permission_classes = [AllowAny]

    def list(self, request):
        queryset = Stock.objects.all()
        serializer = StockSerializer(queryset, many=True)
        return Response(serializer.data)


class DJ30Invest(APIView):
    """
    Get DJ30 stocks list ordered by strategy
    """
    authenticated_classes = [BasicAuthentication]
    permission_classes = [AllowAny]

    def get(self, request, strategy=None):
        index = Index.objects.filter(name="DJ30").values_list("id", flat=True)
        if strategy == "avgmom":
            queryset = Stock.objects.filter(index_id=index[0]).order_by("-momentum_avg")[:6]
        elif strategy == "mom12":
            queryset = Stock.objects.filter(index_id=index[0]).order_by("-momentum_12_2")[:6]
        serializer = StockSerializer(queryset, many=True).data
        return Response(serializer)


class DJ30BestMom(viewsets.ViewSet):
    """
    DJ30 best stocks sorted by momentum_12_2
    """
    authenticated_classes = [BasicAuthentication]
    permission_classes = [AllowAny]

    def list(self, request):
        index = Index.objects.filter(name="DJ30").values_list('id', flat=True)
        queryset = Stock.objects.filter(index_id=index[0]).order_by('-momentum_12_2')[:6]
        serializer = StockMomSerializer(queryset, many=True).data
        return Response(serializer)


class DJ30BestAvg(viewsets.ViewSet):
    """
    DJ30 best 6 stocks sorted by avg_mom
    """
    authentication_classes = [BasicAuthentication]
    permission_classes = [AllowAny]

    def list(self, request):
        index = Index.objects.filter(name="DJ30").values_list('id', flat=True)
        queryset = Stock.objects.filter(index_id=index[0]).order_by('-momentum_avg')[:6]
        serializer = StockAvgMomentumSerializer(queryset, many=True)
        return Response(serializer.data)


class DJ30ViewSet(viewsets.ViewSet):
    """
    DJ30 ViewSet for retrieving ticker or post
    """
    authentication_classes = [BasicAuthentication]
    permission_classes = [AllowAny]

    def retrieve(self, request, pk=None):
        index = Index.objects.filter(name="DJ30").values_list('id', flat=True)
        queryset = Stock.objects.filter(index_id=index[0])
        share = get_object_or_404(queryset, ticker=pk)
        serializer = StockSerializer(share)
        return Response(serializer.data)


class DJ30Div(viewsets.ViewSet):
    """
    DJ30 ViewSet for stocks list ordered by div/p
    """
    authentication_classes = [BasicAuthentication]
    permission_classes = [AllowAny]

    def list(self, request):
        index = Index.objects.filter(name="DJ30").values_list('id', flat=True)
        queryset = Stock.objects.filter(index_id=index[0]).order_by("-div_p")
        serializer = StockDivSerializer(queryset, many=True)
        return Response(serializer.data)


class SP500BestAvg(viewsets.ViewSet):
    """
    SP500 ViewSet for stocks list order by momentum_avg
    """
    authentication_classes = [BasicAuthentication]
    permission_classes = [AllowAny]

    def list(self, request):
        index = Index.objects.filter(name="SP500").values_list('id', flat=True)
        queryset = Stock.objects.filter(index_id=index[0]).order_by("-momentum_avg")[:20]
        serializer = StockAvgMomentumSerializer(queryset, many=True)
        return Response(serializer.data)


class SP500BestMom(viewsets.ViewSet):
    """
    SP500 Best stocks list order by momentum_12_2
    """
    authentication_classes = [BasicAuthentication]
    permission_classes = [AllowAny]

    def list(self, request):
        index = Index.objects.filter(name="SP500").values_list('id', flat=True)
        queryset = Stock.objects.filter(index_id=index[0]).order_by("-momentum_12_2")[:20]
        serializer = StockMomSerializer(queryset, many=True).data
        return Response(serializer)


class SP500BestDiv(viewsets.ViewSet):
    """
    SP500 list best 20 stocks sorted by div_p
    """
    authentication_classes = [BasicAuthentication]
    permission_classes = [AllowAny]

    def list(self, request):
        index = Index.objects.filter(name="SP500").values_list('id', flat=True)
        queryset = Stock.objects.filter(index_id=index[0]).order_by("-div_p")[:20]
        serializer = StockDivSerializer(queryset, many=True)
        return Response(serializer.data)


class SP500ViewSet(viewsets.ViewSet):
    """
    SP500 by ticker
    """
    authentication_classes = [BasicAuthentication]
    permission_classes = [AllowAny]

    def retrieve(self, request, pk=None):
        index = Index.objects.filter(name="SP500").values_list('id', flat=True)
        queryset = Stock.objects.filter(index_id=index[0])
        share = get_object_or_404(queryset, ticker=pk)
        serializer = StockSerializer(share)
        return Response(serializer.data)
