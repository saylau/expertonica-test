from rest_framework import serializers

from .models import LiveProbe


class LiveProbeSerializer(serializers.ModelSerializer):
    class Meta:
        model = LiveProbe
        fields = "__all__"
