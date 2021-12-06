from rest_framework.serializers import ModelSerializer
from .models import Etf

class EtfSerializer(ModelSerializer):
    class Meta:
        model = Etf
        fields = '__all__'
