from django.urls import path
from stocks.views import (
    StockViewSet, DJ30BestAvg, DJ30ViewSet,
    DJ30Div, SP500BestAvg, SP500BestDiv, SP500ViewSet
)
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'all', StockViewSet, basename='allStocks')
router.register(r'dj30avg', DJ30BestAvg, basename='dj30avg')
router.register(r'dj30/ticker', DJ30ViewSet, basename='dj30ticker')
router.register(r'dj30div', DJ30Div, basename='dj30divs')

router.register(r'sp500avg', SP500BestAvg, basename='sp500avg')
router.register(r'sp500div', SP500BestDiv, basename='sp500div')
router.register(r'sp500/ticker', SP500ViewSet, basename = 'sp500ticker')
urlpatterns = router.urls
