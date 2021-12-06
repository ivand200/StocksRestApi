from django.urls import path
from rest_auth.views import UserViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'user', UserViewSet, basename='userView')

urlpatterns = router.urls
