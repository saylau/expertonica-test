from django.db import models


class Website(models.Model):
    """Website model"""
    url = models.URLField()
