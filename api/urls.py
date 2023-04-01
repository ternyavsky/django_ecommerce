from django.urls import path, include
from .routers import router
from . import views


urlpatterns = [
    path('api-auth/',include("rest_framework.urls")),
    path('api/v1/',include(router.urls)),
]