from rest_framework import viewsets, mixins, views, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import Website
from .serializers import WebsiteSerializer
from .tasks import load_websites_excel


class WebsiteViewSet(viewsets.ModelViewSet):
    """
    Updates and retrieves user accounts
    """
    queryset = Website.objects.all()
    serializer_class = WebsiteSerializer
    permission_classes = (AllowAny)


class LoadWebsiteExcelView(views.APIView):
    def post(self, request, *args, **kwargs):
        body = request.json()
        url = body["url"]
        load_websites_excel.delay(url=url)

        return Response(status=status.HTTP_200_OK)
