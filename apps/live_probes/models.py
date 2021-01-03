from django.db import models

from apps.websites.models import Website


class LiveProbe(models.Model):
    """
    Live Probe Model
    """
    website = models.ForeignKey(Website, on_delete=models.CASCADE, related_name='live_probes')
    http_status_code = models.PositiveSmallIntegerField('HTTP code', null=True)
    response_time = models.PositiveIntegerField('Response time(milliseconds)', default=0, null=True)
    ip_address = models.CharField('IP address', max_length=127, null=True, blank=True)
    is_timeout = models.BooleanField('Timedout accured', default=False)
    error_type = models.CharField('Error type', max_length=127, null=True)
    response = models.TextField('Response', null=True, blank=True)
