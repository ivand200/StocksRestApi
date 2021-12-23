from django.urls import path
from myblog.views import PostViewSet, get_ip, PostListView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='posts'),


urlpatterns = router.urls + [
    path('all/posts/', PostListView.as_view({'get': 'list'})),
    path('all/posts/<int:pk>/', PostListView.as_view({'get': 'retrieve',
                                                      'put': 'update',
                                                      'delete': 'destroy'})),
]
