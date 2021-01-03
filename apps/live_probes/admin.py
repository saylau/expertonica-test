from django.contrib import admin

from .models import LiveProbe


@admin.register(LiveProbe)
class LiveProbeAdmin(admin.ModelAdmin):
    list_display = (
                    'http_status_code',
                    'response_time',
                    'ip_address',
                    'is_timeout',
                    'error_type',
                    )
