from django.urls import path, include
from rest_auth.views import UserViewSet, UserCreateSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
#router.register(r'user', UserCreateSet, basename='userView')

urlpatterns = router.urls + [

]
