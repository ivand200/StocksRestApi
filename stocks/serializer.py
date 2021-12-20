from rest_framework.serializers import ModelSerializer, StringRelatedField
from .models import Stock, Index

class StockSerializer(ModelSerializer):
    class Meta:
        model = Stock
        fields = '__all__'


class StockMomSerializer(ModelSerializer):

    class Meta:
        model = Stock
        fields = ['ticker', 'name', 'momentum_12_2']

class StockAvgMomentumSerializer(ModelSerializer):

    class Meta:
        model = Stock
        fields = ['ticker', 'name', 'momentum_avg']


class StockDivSerializer(ModelSerializer):

    class Meta:
        model = Stock
        fields = ['ticker', 'name', 'div_p', 'e_p']
