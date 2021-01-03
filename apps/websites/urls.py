from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter

from .views import WebsiteViewSet, LoadWebsiteExcelView, LoadWebsiteToDBView

router = DefaultRouter()
router.register(r'', WebsiteViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('load-excel/', LoadWebsiteExcelView.as_view()),
    path('load-websites/', LoadWebsiteToDBView.as_view()),
]
