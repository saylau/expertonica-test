from django.db import models


class Website(models.Model):
    url = models.URLField()
