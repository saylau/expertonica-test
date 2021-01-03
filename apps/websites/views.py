from rest_framework import viewsets, mixins, generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema

from .models import Website
from .serializers import WebsiteSerializer, UrlSerializer
from .tasks import load_websites_excel, import_website_urls


class WebsiteViewSet(viewsets.ModelViewSet):
    """
    Updates and retrieves user accounts
    """
    queryset = Website.objects.all()
    serializer_class = WebsiteSerializer
    permission_classes = (AllowAny)


class LoadWebsiteExcelView(generics.GenericAPIView):
    """
    Load excel file from url
    """
    serializer_class = UrlSerializer

    def post(self, request, *args, **kwargs):
        body = request.json()
        url = body["url"]
        load_websites_excel.delay(url=url)

        return Response(status=status.HTTP_200_OK)


class LoadWebsiteToDBView(generics.GenericAPIView):
    """
    Import websites from fixtures to db
    """
    def post(self, request, *args, **kwargs):
        import_website_urls.delay()

        return Response(status=status.HTTP_200_OK)
