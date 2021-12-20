from django.urls import path
from stocks.views import (
    StockViewSet, DJ30BestAvg, DJ30ViewSet,
    DJ30Div, SP500BestAvg, SP500BestDiv, SP500ViewSet,
    DJ30BestMom, DJ30Invest
)
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'all', StockViewSet, basename='allStocks')
router.register(r'dj30/avg', DJ30BestAvg, basename='dj30avg')
router.register(r'dj30/ticker', DJ30ViewSet, basename='dj30ticker')
router.register(r'dj30/div', DJ30Div, basename='dj30divs')
router.register(r'dj30/mom', DJ30BestMom, basename='dj30Mom')

router.register(r'sp500/avg', SP500BestAvg, basename='sp500avg')
router.register(r'sp500/div', SP500BestDiv, basename='sp500div')
router.register(r'sp500/ticker', SP500ViewSet, basename = 'sp500ticker')

urlpatterns = router.urls + [
    path('dj30/<str:strategy>/', DJ30Invest.as_view()),
]
