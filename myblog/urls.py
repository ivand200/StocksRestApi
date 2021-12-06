from django.urls import path
from myblog.views import PostViewSet, get_ip
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='posts')


urlpatterns = router.urls + [

]
