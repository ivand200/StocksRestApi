from django.contrib import admin
from stocks.models import Stock, Index

# Register your models here.

@admin.register(Stock)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ['ticker', 'momentum_avg', 'div_p', 'e_p', 'index']
    search_fields = ['ticker']
    list_filter = ['index']
