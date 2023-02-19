"""quien_da_mas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from rest_framework import routers
from django.conf import settings

from django.urls import re_path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

urlpatterns = [
    path('admin/', admin.site.urls),
    path('subasta_producto/',include('subasta_producto.urls'))
]


schema_view = get_schema_view(
    openapi.Info(
        title="Curso de Dajango 4.1",
        default_version="v1",
        description="Curso de Django by Micaela Machicado",
        terms_of_service="https://github",
        contact=openapi.Contact(email="micaela.ss501@gmail.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny]
)

if settings.DEBUG:
    urlpatterns += [
        re_path(
            r"^apidoc(?P<format>\.json|\.yaml)$",
            schema_view.with_ui(cache_timeout=0),
            name="schema-json"
        ),
        re_path(
            r"^apidoc/$",
            schema_view.with_ui("swagger",cache_timeout=0),
            name="schema-swagger-ui"
        ),
    ]

