from django.urls import path, include
from rest_auth.views import UserCreateSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
#router.register(r'user', UserCreateSet, basename='userView')

urlpatterns = router.urls + [
    path('auth/', UserCreateSet.as_view())
]
