from rest_framework.serializers import ModelSerializer
from .models import Etf

class EtfSerializer(ModelSerializer):
    class Meta:
        model = Etf
        fields = "__all__"


class EtfBondSerializer(ModelSerializer):

    class Meta:
        model = Etf
        fields = ['ticker' ,'momentum_3', 'ma10']
