from rest_framework import views, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from apps.websites.models import Website

from .tasks import take_live_probe


url_param = openapi.Parameter('url', openapi.IN_QUERY, description="url param", type=openapi.TYPE_STRING)
@swagger_auto_schema(manual_parameters=[url_param])
class SiteCheckView(views.APIView):
    """
    Check Site and save live probe
    """
    permission_classes = (AllowAny,)

    def post(self, request, url, *args, **kwargs):
        website, _created = Website.objects.get_or_create(url=url)
        live_probe = take_live_probe(url, website.id)

        return Response(status=status.HTTP_200_OK, data=live_probe)
