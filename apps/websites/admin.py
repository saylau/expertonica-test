from django.contrib import admin

from apps.live_probes.models import LiveProbe

from .models import Website


class LiveProbeInline(admin.TabularInline):
    collapse = True
    model = LiveProbe
    fields = (
                'http_status_code',
                'response_time',
                'ip_address',
                'is_timeout',
                'error_type',
                )


@admin.register(Website)
class WebsiteAdmin(admin.ModelAdmin):
    inlines = [LiveProbeInline]
    list_display = ('url',)
