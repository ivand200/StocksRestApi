from django.urls import path
from indexes.views import EtfViewSet, EtfMom
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'all', EtfViewSet, basename='allEtf')
router.register(r'etfmom', EtfMom, basename='etfMom')
urlpatterns = router.urls
