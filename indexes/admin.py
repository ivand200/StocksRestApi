from django.contrib import admin
from indexes.models import Etf

# Register your models here.

@admin.register(Etf)
class EtfAdmin(admin.ModelAdmin):
    list_display = ['ticker', 'momentum_12_1', 'momentum_avg', 'momentum_3', 'ma10']
    search_fields = ['ticker']
