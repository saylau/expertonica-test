from rest_framework import serializers

from .models import Website


class WebsiteSerializer(serializers.ModelSerializer):
    """Common Website serializer"""
    class Meta:
        model = Website
        fields = "__all__"


class UrlSerializer(serializers.Serializer):
    """Url serializer"""
    url = serializers.URLField(required=False, allow_null=True)
