"""restApi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from myblog.views import get_ip
from django.conf import settings
import debug_toolbar

from rest_auth.views import UserCreateSet


schema_view = get_schema_view(
    openapi.Info(
        title="Investment blog Swagger",
        default_version='v1',
        description="API description for AgroHub Backend",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="xxxxxxx@gmail.com"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('stocks/', include('stocks.urls')),
    path('indexes/', include('indexes.urls')),
    path('myblog/', include('myblog.urls')),
    path('users/', include('rest_auth.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('ip/', get_ip),

    path('auth/', UserCreateSet.as_view()),
]

if settings.DEBUG:
    urlpatterns += [
        path("__debug__", include(debug_toolbar.urls)),
    ]
