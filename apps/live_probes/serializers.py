from rest_framework import serializers

from .models import LiveProbe


class LiveProbeSerializer(serializers.ModelSerializer):
    """
    Common Live Probe serializer
    """
    class Meta:
        model = LiveProbe
        fields = "__all__"
