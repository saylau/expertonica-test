from django.urls import path


from .views import SiteCheckView


urlpatterns = [
    path('site-check/<str:url>', SiteCheckView.as_view())
]
