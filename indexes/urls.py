from django.urls import path
from indexes.views import EtfViewSet, EtfBond, EtfStocks
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'all', EtfViewSet, basename='allEtf')
router.register(r'stocks', EtfStocks, basename='EtfStocks')
router.register(r'etf/bond', EtfBond, basename='EtfMom')
router.register(r'all/<str:pk>', EtfViewSet, basename='EtfRetrieve')
urlpatterns = router.urls
