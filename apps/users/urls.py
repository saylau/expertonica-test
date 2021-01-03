from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter

from .views import UserViewSet, UserCreateViewSet

router = DefaultRouter()
router.register(r'', UserViewSet)
router.register(r'', UserCreateViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
