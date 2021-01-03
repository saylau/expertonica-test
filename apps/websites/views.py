from rest_framework import viewsets, mixins, views, status
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
    permission_classes = (AllowAny,)


class LoadWebsiteExcelView(views.APIView):
    """
    Load excel file from url
    """
    http_method_names = ['post']
    permission_classes = (AllowAny,)

    @swagger_auto_schema(request_body=UrlSerializer(), responses={200: None})
    def post(self, request, *args, **kwargs):
        serializer = UrlSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        load_websites_excel.delay(url=serializer.validated_data.get('url', None))

        return Response(status=status.HTTP_200_OK)


class LoadWebsiteToDBView(views.APIView):
    """
    Import websites from fixtures to db
    """
    permission_classes = (AllowAny,)
    http_method_names = ['post']

    @swagger_auto_schema(request_body=None, responses={200: None})
    def post(self, request, *args, **kwargs):
        import_website_urls.delay()

        return Response(status=status.HTTP_200_OK)
