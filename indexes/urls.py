from django.urls import path
from indexes.views import EtfViewSet, EtfBond
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'all', EtfViewSet, basename='allEtf')
router.register(r'etfbond', EtfBond, basename='etfBond')
urlpatterns = router.urls
